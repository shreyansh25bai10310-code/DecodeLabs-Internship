# Project 2 — Iris KNN Classifier

**DecodeLabs AI Internship | Batch 2026**

## Overview
A supervised learning classification model built using the Iris benchmark dataset.
Classifies flowers into 3 species using K-Nearest Neighbors algorithm.

## Key Concepts
- Supervised learning pipeline
- Feature scaling with StandardScaler
- Train-test split (80/20)
- KNN classification (k=5)
- Confusion Matrix + F1 Score evaluation

## How to Run
```bash
pip install scikit-learn numpy
python classifier.py
```

## Results
| Metric | Score |
|--------|-------|
| F1 Score (weighted) | 1.0000 |
| Accuracy | 100% |
| Test Samples | 30 |

## Dataset
- 150 samples, 4 features, 3 classes
- Classes: Setosa, Versicolor, Virginica
- Source: sklearn.datasets (built-in)

## Tech Stack
- Python 3.x
- scikit-learn
- NumPy
