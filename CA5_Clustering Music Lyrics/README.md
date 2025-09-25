# 🧠 AI Course Assignment 5: English Lyrics Clustering  
## 📝 Text Clustering with Sentence Embeddings

---

## 🎯 Project Overview

This project focuses on **clustering English song lyrics** using unsupervised machine learning techniques. The goal is to group similar lyrics into meaningful clusters based on their semantic content using various clustering algorithms and text embedding methods.

---

## 📊 Dataset Description

The dataset contains **English song lyrics** from various music genres. Each entry consists of raw text lyrics that need to be processed and transformed into numerical features for clustering.

---

## 🛠️ Project Pipeline

### 1. Text Preprocessing
- 🧹 Remove stop words, punctuation, and irrelevant characters
- 🔄 Apply stemming or lemmatization
- 📝 Compare different preprocessing methods and select the most effective one

### 2. Feature Extraction
- 🤖 Use **SentenceTransformers** with `all-MiniLM-L6-v2` model
- 📊 Convert lyrics into dense vector embeddings (384 dimensions)
- 🔍 Explain why feature extraction is necessary for textual data

### 3. Clustering Algorithms
Implement and compare three clustering methods:
- **K-Means** (with Elbow Method for optimal K)
- **DBSCAN** (density-based clustering)
- **Hierarchical Clustering** (agglomerative)

### 4. Dimensionality Reduction
- 📉 Apply **PCA** to visualize clusters in 2D/3D space
- 🎨 Create scatter plots to visualize clustering results
- 📋 Compare cluster formations across different algorithms

### 5. Evaluation Metrics
- 📊 **Silhouette Score**
- 🎯 **Homogeneity Score**
- 📈 Visual analysis of cluster quality
- 🔍 Print 2 sample lyrics from each cluster for semantic comparison

---


## Prerequisites
```bash
pip install sentence-transformers scikit-learn matplotlib pandas numpy