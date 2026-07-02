# 🛡️ FraudLens AI

An AI-powered Fake Job Posting Detection system that identifies fraudulent job advertisements using **Machine Learning**, **Natural Language Processing (NLP)**, and an interactive **Streamlit** dashboard.

# Live demo link
https://fraudlens-ai-lqiameepcx57uicgwry96c.streamlit.app/


## 📌 Overview

FraudLens AI helps job seekers and recruiters detect fake job postings before applying. The application analyzes both textual and structured job information to classify a job advertisement as **Legitimate** or **Fraudulent**.

The project demonstrates a complete machine learning workflow including data preprocessing, feature engineering, model training, evaluation, explainability, and deployment.

---

## ✨ Features

- 🔍 Fake Job Prediction
- 🤖 Explainable AI
- 📊 Confidence Score
- 📈 Interactive Dashboard
- 📋 Dataset Insights
- 📄 PDF Report Generation
- 📜 Prediction History
- 📉 Model Performance Dashboard
- 💻 Modern Streamlit UI

---

## 🧠 Machine Learning Pipeline

```
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Prediction Dashboard
```

---

## 📂 Project Structure

```
fraudlens-ai/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   ├── logo.png
│   └── style.css
│
├── data/
│   ├── fake_real_job_postings.csv
│   ├── processed_jobs.csv
│   └── prediction_history.csv
│
├── models/
│   ├── best_model.pkl
│   └── tfidf.pkl
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_Model_Evaluation.ipynb
│
├── pages/
│   ├── 1_Predict.py
│   ├── 2_Model_Information.py
│   ├── 3_Dataset_Insights.py
│   ├── 4_About_Project.py
│   └── 5_Prediction_History.py
│
├── reports/
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   └── precision_recall_curve.png
│
└── src/
    ├── predictor.py
    ├── explain.py
    ├── report.py
    └── utils.py
```

---

## 📊 Dataset

The dataset contains job advertisements with both structured and textual information.

### Features Used

- Job Title
- Company Profile
- Requirements
- Job Description
- Benefits
- Industry
- Department
- Job Function
- Required Experience
- Open Positions
- Company Logo
- Telecommuting

**Target Variable**

```
is_fake

0 → Legitimate Job
1 → Fake Job
```

---

## ⚙️ Technologies Used

### Programming

- Python
- Pandas
- NumPy

### Machine Learning

- Scikit-Learn
- Logistic Regression
- TF-IDF Vectorizer
- Naive Bayes
- Random Forest (comparison)

### Visualization

- Plotly
- Matplotlib
- Streamlit

### Other Tools

- ReportLab
- Git
- GitHub

---

## 📈 Model Evaluation

The project evaluates multiple classification models using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC Curve
- Confusion Matrix

The best-performing model is used for deployment.

---

## 🖥️ Installation

Clone the repository

```bash
git clone https://github.com/bhagya21-tech/fraudlens-ai.git
```

Move into the project directory

```bash
cd fraudlens-ai
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📷 Application Pages

- 🏠 Home
- 🔍 Predict Job
- 🤖 Model Information
- 📊 Dataset Insights
- 📖 About Project
- 📜 Prediction History

---

## 🎯 Future Improvements

- BERT-based Classification
- SHAP Explainability
- FastAPI Backend
- Docker Support
- Cloud Database
- User Authentication
- Resume Matching
- Recruiter Dashboard

---

## 👩‍💻 Developer

**Bhagyashri Raut**

AI • Machine Learning • Data Science

### Connect with Me

- GitHub: https://github.com/bhagya21-tech
- LinkedIn: https://linkedin.com/in/bhagyashri-raut-471960322

---

## 📄 License

This project is developed for educational and portfolio purposes.
