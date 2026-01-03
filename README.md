# Failure Prediction in CI/CD Pipelines Using Machine Learning

This repository contains the implementation of an M.Phil. research thesis focused on predicting failures in Continuous Integration and Continuous Deployment (CI/CD) pipelines using machine learning. The project develops an end-to-end workflow that ingests CI/CD pipeline data, preprocesses heterogeneous information, engineers features, handles class imbalance, trains supervised learning models, and evaluates their performance for failure prediction.

The work investigates how historical pipeline executions, build metadata, logs, and code-related attributes can be transformed into predictive signals. By identifying failure-prone pipeline runs in advance, the system supports proactive decision-making and helps reduce disruption in software delivery processes.

---

## 📌 Research Objectives

* predict failure-prone CI/CD pipeline executions
* analyse heterogeneous pipeline data and log information
* apply preprocessing, feature engineering, and resampling techniques
* train supervised machine learning models for binary classification
* compare ensemble and boosting models
* evaluate results using standard performance metrics

---

## 🧠 Problem Motivation

Modern CI/CD systems integrate code changes frequently and execute automated builds and tests. These pipelines often fail due to code modifications, configuration changes, infrastructure issues, and environmental variability. Such failures:

* delay software releases
* consume developer time
* increase operational cost
* affect software reliability

Manual log inspection is slow and error-prone. This project explores machine learning-based prediction to support timely intervention.

---

## 🏗️ Repository Structure

```
failure-prediction-cicd/
│
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   ├── processed/
│   └── samples/
├── notebooks/
│   └── Failure_Detection_CI_CD.ipynb
├── src/
│   ├── data_ingestion.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── imbalance_handling.py
│   ├── model_training.py
│   ├── evaluation.py
│   └── utils.py
└── reports/
    ├── figures/
```

---

## ⚙️ Main Components Implemented

* data loading and exploratory data analysis
* preprocessing and handling missing values
* categorical encoding and feature scaling
* extensive feature engineering capturing CI/CD context
* class imbalance treatment through oversampling
* training of multiple ensemble and boosting classifiers
* comparative evaluation and reporting

---

## 🧩 Machine Learning Models Used

* Random Forest
* Extra Trees
* Gradient Boosting
* AdaBoost
* Bagging Classifier
* XGBoost
* LightGBM

---

## 📊 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

---

## ▶️ How to Run

1. Install dependencies

```
pip install -r requirements.txt
```

2. Place dataset files in `data/raw/`

3. Run the notebook located in:

```
notebooks/Failure_Detection_CI_CD.ipynb
```

or execute modular scripts inside `src/`.

---

## 🎓 Academic Context

This repository forms part of an **M.Phil. thesis** in software engineering and machine learning.
It demonstrates:

* research methodology implementation
* reproducible experimental workflow
* empirical evaluation of predictive models

The code serves both as a research artefact and a practical demonstration of applied machine learning in DevOps environments.

---

## 🛡️ Ethical and Usage Notes

* dataset sources should be cited where applicable
* use results responsibly in academic work
* reproduction of experiments should acknowledge the original thesis
