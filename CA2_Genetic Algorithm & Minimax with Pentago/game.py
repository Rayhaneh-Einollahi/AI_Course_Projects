import random
import numpy as np
from math import inf
import time
import pygame


class PentagoGame:
    def __init__(self, ui=False, print=False, depth=2):
        self.board = np.zeros((6, 6), dtype=int)
        self.current_player = 1
        self.ui = ui
        self.depth = depth
        self.nodes_visited = 0
        self.game_over = False
        self.result = None
        self.selected_block = None
        self.move_stage = 0  # 0: place piece, 1: select block, 2: rotate
        self.temp_piece = None
        self.print = print

        if ui:
            pygame.font.init()
            self.screen = pygame.display.set_mode((800, 600))
            pygame.display.set_caption("Pygame Board")
            # self.font = pygame.font.SysFont("Arial", 20)
            self.show_buttons = False
            self.buttons = {
                "rotate_cw": pygame.Rect(650, 200, 100, 50),
                "rotate_ccw": pygame.Rect(650, 300, 100, 50),
            }
            self.setup_controls()
            self.draw_board()

    def setup_controls(self):
        if self.show_buttons:
            pygame.draw.rect(self.screen, (144, 238, 144), self.buttons["rotate_cw"])   # Light Green
            pygame.draw.rect(self.screen, (173, 216, 230), self.buttons["rotate_ccw"])  # Light Blue

            self.screen.draw_text("CLOCKWISE", self.buttons["rotate_cw"].center)
            self.screen.draw_text("COUNTER-CLOCKWISE", self.buttons["rotate_ccw"].center)



    def hide_rotation_buttons(self):
        self.show_buttons = False

    def show_rotation_buttons(self):
        self.show_buttons = True

    def copy_board(self, board):
        return np.copy(board)

    def rotate_block(self, board, block, direction):
        row_start = (block // 2) * 3
        col_start = (block % 2) * 3
        sub = board[row_start : row_start + 3, col_start : col_start + 3]
        rotated = np.rot90(sub, 3 if direction == "cw" else 1)
        board[row_start : row_start + 3, col_start : col_start + 3] = rotated

    def get_possible_moves(self, board):
        empty = np.argwhere(board == 0)
        directions = ["cw", "ccw"]
        moves = []
        for k in range(len(empty)):
            i, j = empty[k]
            for block in range(4):
                for dir in directions:
                    moves.append((i, j, block, dir))
        return moves

    def apply_move(self, board, move, player):
        new_board = self.copy_board(board)
        row, col, block, direction = move
        if new_board[row][col] != 0:
            return None
        new_board[row][col] = player
        self.rotate_block(new_board, block, direction)
        return new_board

    def check_winner(self, board):
        for i in range(6):
            for j in range(6):
                if board[i][j] == 0:
                    continue

                if j <= 1 and np.all(board[i, j : j + 5] == board[i][j]):
                    return board[i][j]
                if i <= 1 and np.all(board[i : i + 5, j] == board[i][j]):
                    return board[i][j]
                if i <= 1 and j <= 1 and all(board[i + k][j + k] == board[i][j] for k in range(5)):
                    return board[i][j]
                if i <= 1 and j >= 4 and all(board[i + k][j - k] == board[i][j] for k in range(5)):
                    return board[i][j]
        if np.all(board != 0):
            return 0
        return None

    def minimax(self, board, depth, maximizing_player, alpha, beta):
        game_over = self.game_over
        if game_over or depth == 0:
            return self.get_board_score(board, -1), None

        self.nodes_visited += 1
        best_move = None

        if maximizing_player:
            max_eval = -inf
            moves = self.get_possible_moves(board)
            random.shuffle(moves)
            for move in moves:
                new_board = self.apply_move(board, move, 1)
                child_score, _ = self.minimax(new_board, depth - 1, False, alpha, beta)
                if child_score > max_eval:
                    max_eval = child_score
                    best_move = move
                alpha = max(alpha, child_score)
                if beta <= alpha:
                    break
            return max_eval, best_move

        else:
            min_eval = inf
            moves = self.get_possible_moves(board)
            random.shuffle(moves)
            for move in moves:
                new_board = self.apply_move(board, move, -1)
                child_score, _ = self.minimax(new_board, depth - 1, True, alpha, beta)
                if child_score < min_eval:
                    min_eval = child_score
                    best_move = move
                beta = min(beta, child_score)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def get_board_score(self, board, player):
        winner = self.check_winner(board)
        if winner == 1:
            return 1000
        elif winner == -1:
            return -1000
        score = 0
        center_positions = [(1,1), (1,4), (4,1), (4,4)]
        for x, y in center_positions:
            if board[x][y] == 1:
                score += 2
            elif board[x][y] == -1:
                score -= 2
        
        def line_score(line):
            count_1 = line.count(1)
            count_neg1 = line.count(-1)
            if count_1 > 0 and count_neg1 > 0:
                return 0  # blocked line
            if count_1 > 0:
                return count_1 ** 2  # reward more for longer chains
            if count_neg1 > 0:
                return -(count_neg1 ** 2)
            return 0

        lines = []

        # Rows and columns
        for i in range(6):
            for j in range(2):  # only start from index 0 to 1 (0-4 window)
                lines.append([board[i][j+k] for k in range(5)])  # rows
                lines.append([board[j+k][i] for k in range(5)])  # columns

        # Diagonals (\ and /)
        for i in range(2):  # top rows
            for j in range(2):  # left columns
                lines.append([board[i+k][j+k] for k in range(5)])  # \
                lines.append([board[i+4-k][j+k] for k in range(5)])  # /

        for line in lines:
            score += line_score(line)
        return score

    def get_computer_move(self):
        start_time = time.time()
        value, best_move = self.minimax(self.board, self.depth, False, -inf, inf)
        if self.print:
            print(f"Move took {time.time()-start_time:.2f}s, nodes visited: {self.nodes_visited}")
        self.nodes_visited = 0
        return best_move

    def draw_text(self, text, center_pos, max_width):
        font_size = 24
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, (0, 0, 0))

        text_width = text_surface.get_width()
        if text_width > max_width:
            scale_factor = max_width / text_width
            new_font_size = int(font_size * scale_factor)
            font = pygame.font.Font(None, new_font_size)
            text_surface = font.render(text, True, (0, 0, 0))

        text_rect = text_surface.get_rect(center=center_pos)
        self.screen.blit(text_surface, text_rect)

    def draw_board(self):
        self.screen.fill((0, 0, 0))

        for i in range(6):
            for j in range(6):
                x0 = j * 100
                y0 = i * 100

                if self.board[i][j] == 1:
                    pygame.draw.circle(self.screen, (255, 0, 0), (x0 + 50, y0 + 50), 40)
                elif self.board[i][j] == -1:
                    pygame.draw.circle(self.screen, (0, 0, 255), (x0 + 50, y0 + 50), 40)

                pygame.draw.rect(self.screen, (255, 255, 255), (x0, y0, 100, 100), 1)

        for i in [3, 6]:
            pygame.draw.line(self.screen, (255, 255, 255), (0, i * 100), (600, i * 100), 3)  # Horizontal
            pygame.draw.line(self.screen, (255, 255, 255), (i * 100, 0), (i * 100, 600), 3)  # Vertical

        # Show rotation buttons if in move_stage 2
        if self.move_stage == 2:
            self.highlight_selected_block()
            self.show_rotation_buttons()

        if self.show_buttons:
            pygame.draw.rect(self.screen, (144, 238, 144), self.buttons["rotate_cw"])  # Light Green
            pygame.draw.rect(self.screen, (173, 216, 230), self.buttons["rotate_ccw"])  # Light Blue

            self.draw_text(
                "CLOCKWISE",
                self.buttons["rotate_cw"].center,
                self.buttons["rotate_cw"].width,
            )
            self.draw_text(
                "COUNTER-CLOCKWISE",
                self.buttons["rotate_ccw"].center,
                self.buttons["rotate_ccw"].width,
            )

    def click_handler(self, event):
        if self.game_over or self.current_player != 1:
            return

        x, y = event.pos
        if self.move_stage == 0:  # Place piece
            if x > 600:
                return  # clicks on control area
            col = x // 100
            row = y // 100
            if 0 <= row < 6 and 0 <= col < 6 and self.board[row][col] == 0:
                self.temp_piece = (row, col)
                self.board[row][col] = 1
                self.move_stage = 1
                self.draw_board()

        elif self.move_stage == 1:  # Select block
            if x > 600:
                return
            # which block was clicked
            block_x = 0 if x < 300 else 1
            block_y = 0 if y < 300 else 1
            self.selected_block = block_y * 2 + block_x
            self.move_stage = 2
            self.show_rotation_buttons()
            self.highlight_selected_block()

        elif self.move_stage == 2:  # Rotate
            if self.buttons["rotate_cw"].collidepoint(event.pos):
                self.apply_rotation("cw")
            if self.buttons["rotate_ccw"].collidepoint(event.pos):
                self.apply_rotation("ccw")

    def apply_rotation(self, direction):
        self.rotate_block(self.board, self.selected_block, direction)
        self.current_player = -1
        self.move_stage = 0
        self.selected_block = None
        self.temp_piece = None
        self.hide_rotation_buttons()
        self.draw_board()
        pygame.display.flip()
        self.check_game_over()
        pygame.time.delay(1000)
        self.play_computer_move()

    def highlight_selected_block(self):
        colors = [
            (255, 153, 153),
            (153, 255, 153),
            (153, 153, 255),
            (255, 255, 153),
        ]  # RGB colors

        row_start = (self.selected_block // 2) * 3
        col_start = (self.selected_block % 2) * 3

        pygame.draw.rect(
            self.screen,
            colors[self.selected_block],
            (col_start * 100, row_start * 100, 300, 300),
            5,
        )

    def play_computer_move(self):
        move = self.get_computer_move()
        if move and not self.game_over:
            new_board = self.apply_move(self.board, move, -1)
            if new_board is not None:
                self.board = new_board
                self.current_player = 1
                self.draw_board()
                pygame.display.flip()
                self.check_game_over()
            else:
                print("Invalid computer move!")

    def check_game_over(self):
        winner = self.check_winner(self.board)
        if winner is not None:
            self.game_over = True
            self.result = winner
            print("Game over! Result:", winner)
            # if self.ui:
            #     self.show_game_over_message()

    def show_game_over_message(self):
        self.screen.fill((200, 200, 200))
        pygame.draw.rect(self.screen, (255, 255, 255), (100, 200, 500, 200))
        pygame.draw.rect(self.screen, (0, 0, 0), (100, 200, 500, 200), 3)

        result_text = f"Player {self.result} wins!" if self.result != 0 else "Draw!"
        print(result_text)
        # text_surface = self.font_large.render(result_text, True, (255, 0, 0))
        # self.screen.blit(text_surface, (250, 250))
        # self.draw_text(result_text, (250, 250),1000)

        exit_text = self.font_small.render("Click anywhere to exit", True, (0, 0, 0))
        self.screen.blit(exit_text, (230, 350))
        pygame.display.flip()

    def play(self):
        if self.ui:
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.click_handler(event)
                self.draw_board()
                pygame.display.flip()
            pygame.quit()
            return self.result
        else:
            while not self.game_over:
                self.print_board()
                winner = self.check_winner(self.board)
                if winner is not None:
                    return winner

                if self.current_player == 1:
                    move = random.choice(self.get_possible_moves(self.board))
                else:
                    move = self.get_computer_move()

                self.board = self.apply_move(self.board, move, self.current_player)
                self.current_player *= -1
            return self.result

    def print_board(self):
        if self.print == False:
            return
        print("-" * 25)
        for row in self.board:
            print(" ".join(f"{x:2}" for x in row))
        print("-" * 25)


numGames = 1
numWins, numTies, numLosses = 0, 0, 0
for i in range(numGames):
    game = PentagoGame(ui=False, print=True, depth=2)  # depth=2 for faster
    result = game.play()
    if result == -1:
        numWins += 1
        print("win")
    elif result == 0:
        numTies += 1
        print("tie")
    else:
        numLosses += 1
        print("lose")


print(f"{numWins} wins, {numTies} ties, {numLosses} losses")