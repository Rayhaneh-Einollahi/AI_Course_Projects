# 🧠 AI Course Assignment 4: Image Classification with Neural Networks  
## 🖼️ Comparing Fully Connected vs CNN on CIFAR-10

---

## 🎯 Project Overview

This project involves **comparing two neural network architectures** for image classification on the CIFAR-10 dataset. You'll implement both a **Fully Connected Network** and a **Convolutional Neural Network (CNN)** using PyTorch, then analyze their performance, feature spaces, and internal representations.

---

## 📊 Dataset: CIFAR-10

**60,000 images** across 10 classes:
- ✈️ Airplane, 🚗 Automobile, 🐦 Bird, 🐱 Cat, 🦌 Deer  
- 🐶 Dog, 🐸 Frog, 🐴 Horse, 🚢 Ship, 🚚 Truck

**Image specs**: 32×32 pixels, RGB (3 channels)  
**Split**: 50,000 training, 10,000 test images

---

## 🏗️ Project Architecture

### Part 1: Fully Connected Network
- 🔗 Design FC network with ~500,000 ± 33,500 parameters
- 📐 Manual parameter calculation and verification
- ⚙️ **CrossEntropyLoss** + **Adam optimizer**
- 📈 Train for 60 epochs, track loss/accuracy
- 📊 Analyze overfitting with validation curves

### Part 2: Convolutional Neural Network (CNN)
- 🎯 Design CNN with similar parameter count for fair comparison
- 🏗️ Convolutional + Pooling + Fully Connected layers
- 🔁 Same training setup: 60 epochs, CrossEntropy + Adam
- 👁️ Visualize misclassified images and feature maps

---

## 🔍 Advanced Analysis

### Feature Space Exploration
- 🎯 Extract feature vectors from CNN intermediate layers
- 👥 Find **5 nearest neighbors** using KNN in feature space
- 📉 Apply **t-SNE** for 2D visualization of feature space
- 🔍 Analyze semantic clustering patterns

### Feature Map Visualization
- 👁️ Visualize **convolutional feature maps**
- 🔍 Understand what patterns CNN layers detect
- 📊 Compare attention patterns across network depth

---

## 📈 Expected Deliverables

### 1. Model Performance Comparison
- 📊 Training/validation loss curves for both models
- ✅ Accuracy metrics on test set
- 🔍 Analysis of overfitting patterns

### 2. Visualizations
- 🖼️ 24 misclassified images with predictions
- 📉 t-SNE plots of feature space
- 🎨 Feature maps from convolutional layers
- 👥 Nearest neighbor visualizations

### 3. Technical Analysis
- 📐 Manual parameter calculation proofs
- 🔧 Dropout effectiveness analysis
- 🏗️ Architecture design rationale
- 🎯 Feature space interpretation

---

## 💡 Key Learning Objectives

- 🏗️ **Neural Network Design**: Architecting FC vs CNN networks
- ⚙️ **PyTorch Mastery**: Dataset, Dataloader, training loops
- 📊 **Model Evaluation**: Loss curves, accuracy metrics, overfitting detection
- 🔍 **Feature Analysis**: t-SNE, KNN, interpretability techniques
- 👁️ **Computer Vision**: Understanding what CNNs "see"

---
