 
# 🧬 Genetic Algorithm & 🎮 Minimax with Pentago  

---

## 📋 Project Overview

This repository contains the implementation of **Assignment 2** for the Artificial Intelligence course. The project is divided into two distinct and challenging parts involving evolutionary algorithms and game-playing AI.

---

## 📈 Part 1: Genetic Algorithm for Fourier Series Approximation

### 🎯 Objective
Use a **genetic algorithm (GA)** to approximate the **Fourier series coefficients** of an unknown periodic function using only sampled data points.

### 🔧 Technical Details
- **Approximation Terms**: First 25 terms of the Fourier series (a₀, a₁..a₂₁, b₁..b₂₁)
- **Coefficient Range**: Limited to [-A, A] (e.g., A = 10)
- **Fitness Metrics**: 
  - ✅ RMSE (Root Mean Square Error) - Primary metric
  - ✅ Additional error functions (e.g., MAE, R-squared)
- **GA Components**:
  - 🧬 Chromosome representation of coefficients
  - 👥 Population initialization with diversity
  - 🔁 Crossover and mutation operations
  - 📊 Fitness evaluation and selection strategies
- **Visualization**: Comparison plots between target function and GA approximation

---

## 🎲 Part 2: Minimax Algorithm for Pentago Game

### 🎯 Objective
Implement the **Minimax algorithm with Alpha-Beta pruning** for the strategic board game **Pentago**.

### 🕹️ Game Rules (Pentago)
- **Board**: 6×6 grid divided into four 3×3 rotating blocks
- **Players**: Two players (Human vs AI)
- **Gameplay**: 
  - Place a marble on an empty cell
  - Rotate one 3×3 block 90° (clockwise or counterclockwise)
- **Win Condition**: Create a row, column, or diagonal of 5 consecutive marbles

### 🔧 Technical Implementation
- **Algorithm**: Minimax with Alpha-Beta pruning
- **Heuristic Function**: Custom evaluation function for board states
- **Depth Analysis**: Performance evaluation across different search depths
- **Performance Metrics**:
  - ⏱️ Average execution time
  - 📊 Win rate against random opponent
  - 🌳 Number of nodes explored

---

## 📊 Expected Outputs
- **Fourier Approximation**: Graphs comparing original function vs GA approximation
- **GA Convergence**: Fitness improvement over generations
- **Pentago Performance**: Win rates, execution times, and node counts at different depths
- **Alpha-Beta Analysis**: Comparison of performance with and without pruning

---