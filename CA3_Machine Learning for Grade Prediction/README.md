# 🧠 AI Course Assignment 3: Student Grade Prediction  
## 📊 Machine Learning Classification Project

---

## 🎯 Project Overview

This project focuses on **predicting students' final grades** in an Artificial Intelligence course using demographic, social, and academic data. The goal is to build and compare multiple machine learning models to classify students into four grade categories based on their performance.

---

## 📁 Dataset Description

The dataset includes **21 features** related to student profiles, such as:

- 🏫 **University** – Place of study
- 👤 **Demographics** – Age, gender, address type
- 👨‍👩‍👧 **Family Background** – Parent education and jobs
- 🎓 **Academic Factors** – Study time, failures, extra support
- 🧠 **Lifestyle** – Free time, going out, alcohol consumption
- 📚 **Previous Grades** – Statistics and Data Science grades
- ✅ **Target Variable** – Final grade (categorized into 4 classes)

---

## 🛠️ Project Phases

### 1. Data Preprocessing & Feature Engineering
- 🧹 Handling missing values using 3 different methods
- 🔄 Encoding categorical variables
- 📊 Converting final grade into 4 classes:
  - A: >17  
  - B: 14–17  
  - C: 10–14  
  - Fail: <10

### 2. Model Development & Evaluation
- 📈 Train-Test Split (780 train / 720 test)
- ⚖️ Feature scaling and normalization
- 🌳 **Models Implemented**:
  - Naive Bayes
  - Decision Tree (with pruning and visualization)
  - Random Forest (with RandomizedSearchCV)
  - XGBoost (with GridSearchCV)
  - ✅ **Decision Tree from Scratch** (using entropy)

### 3. Model Evaluation Metrics
- 📊 Confusion Matrix
- ✅ Accuracy, Precision, Recall, F1-Score
- 📉 Micro/Macro Averaging
- 📋 Comparative analysis of all models
