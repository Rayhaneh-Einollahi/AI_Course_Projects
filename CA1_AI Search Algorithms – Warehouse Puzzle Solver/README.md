

# 🧩 AI Search Algorithms – Warehouse Puzzle Solver

## 📖 Overview

This project is a course assignment for **Artificial Intelligence (AI)**, focusing on **uninformed** and **informed search algorithms**.
The task is inspired by *Monsters, Inc.*: Mike Wazowski works in a scream warehouse, where he must **push boxes (scream capsules) to their target locations** while navigating walls, portals, and other constraints.

The goal is to **find an optimal sequence of moves** that leads to a valid solution, using different search algorithms.

---

## 🎯 Problem Description

* Mike can move **up, down, left, or right**.
* He can **push boxes** but cannot pull them.
* Each box has a **goal position**.
* There may be **paired portals** that teleport boxes or the player.
* The warehouse is represented as a **grid map**.

The challenge is to implement different search strategies to guide Mike toward the solution.

---

## 📥 Input

* A grid map where:

  * `H` → Mike’s starting position
  * `B` → Boxes
  * `G` → Goal positions
  * `P` → Portals
  * `W` → Walls
  * `.` → Empty spaces

**Example Map:**

```
W   P1  H    W   W    W   W
W   W   W   G1  W   W   W
W   W   W   B1  W   W   W
W   G2  B2  .   P1  W   W
```

---

## 📤 Output

* A **sequence of moves** (e.g., `LUDDUL`) that solves the puzzle.
* If no solution exists → `"No solution"`.
* Additionally, the algorithm reports the **number of visited states**.

Moves are encoded as:

* `U` → Up
* `D` → Down
* `L` → Left
* `R` → Right

---

## ⚙️ Implemented Algorithms

### 🔹 Uninformed Search

* **BFS (Breadth-First Search)**
* **DFS (Depth-First Search)**
* **IDS (Iterative Deepening Search)**

### 🔹 Informed Search

* **A*** (with admissible and consistent heuristics)
* **Weighted A*** (using `f(n) = w * h(n) + g(n)` with tunable weight `w`)

Heuristics used include **Manhattan distance** and improved variants combining player-to-box and box-to-goal distances.

---

## 📊 Performance Evaluation

Each algorithm is tested on different maps.
Metrics include:

* Execution time ⏱
* Number of expanded states 📈
* Solution length (optimality) 🎯

---

## 🖥 Project Structure

```
├── game.py        # Game environment & state management
├── gui.py         # Optional GUI (requires raylib)
├── solvers.py     # Search algorithms
├── maps/          # Test cases
├── report/        # Written report & analysis
```

* **`Game` class**: handles initialization, movement, portals, and win conditions.
* **`gui.py`**: allows visualizing the game using `raylib-python`.
---

## 📌 Features

✔️ Multiple search algorithms implemented
✔️ Supports **portals, multiple boxes, and obstacles**
✔️ Visual game simulation (optional)
✔️ Performance comparison across algorithms

---

## 📚 Questions & Analysis

The project also includes theoretical discussions on:

* State representation
* Action definitions
* Heuristic design & admissibility
* Trade-offs between BFS, DFS, IDS, A*, and Weighted A*

---