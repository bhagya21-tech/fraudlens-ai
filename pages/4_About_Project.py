import streamlit as st
from src.utils import load_css

# ==========================================
# Page Config
# ==========================================

st.set_page_config(
    page_title="About FraudLens AI",
    page_icon="🛡️",
    layout="wide"
)

load_css()

# ==========================================
# Hero Banner
# ==========================================

st.markdown("""
<div class="hero">
<h1>🛡 FraudLens AI</h1>
<p>
Enterprise AI Platform for Detecting Fraudulent Job Postings using
Machine Learning, Natural Language Processing and Explainable AI.
</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# Project Overview
# ==========================================

st.header("🚀 Project Overview")

st.write("""
FraudLens AI is an intelligent recruitment fraud detection platform designed to
identify fake job advertisements before candidates apply.

The application combines Natural Language Processing (NLP) and Machine Learning
to analyze textual information along with structured job attributes to classify
job postings as **Legitimate** or **Fraudulent**.

The project demonstrates an end-to-end machine learning workflow, from
data preprocessing and feature engineering to model deployment through
an interactive Streamlit dashboard.
""")

st.divider()

# ==========================================
# Highlights
# ==========================================

st.header("✨ Key Highlights")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
### 🤖 AI Powered

- TF-IDF Vectorization
- NLP Processing
- Logistic Regression
- Explainable AI
""")

with c2:
    st.info("""
### 📊 Analytics

- Dataset Dashboard
- Model Evaluation
- Interactive Charts
- Prediction History
""")

with c3:
    st.warning("""
### 🚀 Production Ready

- PDF Reports
- Streamlit Deployment
- Modern Dashboard
- Clean UI
""")

st.divider()

# ==========================================
# Workflow
# ==========================================

st.header("⚙ Project Workflow")

workflow = [
    "📂 Dataset Collection",
    "🧹 Data Cleaning",
    "📊 Exploratory Data Analysis",
    "📝 Text Preprocessing",
    "🔤 TF-IDF Feature Extraction",
    "🤖 Model Training",
    "📈 Model Evaluation",
    "🎯 Fraud Prediction",
    "📄 Report Generation",
    "🌐 Streamlit Deployment"
]

for step in workflow:
    st.success(step)

st.divider()

# ==========================================
# Technologies
# ==========================================

st.header("🛠 Technology Stack")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
### 💻 Programming

- Python
- Pandas
- NumPy
""")

with col2:
    st.markdown("""
### 🧠 Machine Learning

- Scikit-Learn
- Logistic Regression
- Naive Bayes
- Random Forest
""")

with col3:
    st.markdown("""
### 📚 NLP

- TF-IDF
- Text Cleaning
- Feature Engineering
""")

with col4:
    st.markdown("""
### 📊 Visualization

- Plotly
- Matplotlib
- Streamlit
""")

st.divider()

# ==========================================
# Features
# ==========================================

st.header("⭐ Platform Features")

left, right = st.columns(2)

with left:

    st.markdown("""
### Current Features

- ✅ Fake Job Prediction
- ✅ Confidence Score
- ✅ AI Explanation
- ✅ PDF Report Download
- ✅ Dataset Dashboard
- ✅ Model Dashboard
- ✅ Prediction History
- ✅ Interactive Visualizations
""")

with right:

    st.markdown("""
### Future Enhancements

- 🔹 BERT-based Classification
- 🔹 SHAP Explainability
- 🔹 REST API (FastAPI)
- 🔹 Docker Support
- 🔹 Cloud Deployment
- 🔹 Recruiter Dashboard
- 🔹 Resume Matching
- 🔹 Job Recommendation
""")

st.divider()

# ==========================================
# Performance
# ==========================================

st.header("📈 Model Performance")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Accuracy", "98.7%")

with m2:
    st.metric("Precision", "98.1%")

with m3:
    st.metric("Recall", "97.9%")

with m4:
    st.metric("F1 Score", "98.0%")

st.divider()

# ==========================================
# Developer
# ==========================================

st.header("👩‍💻 Developer")

st.markdown("""
### Bhagyashri Raut

AI • Machine Learning • Data Science

Passionate about building practical AI solutions that solve real-world
problems using Machine Learning, NLP and Data Analytics.

### Skills

- Python
- Machine Learning
- Data Science
- NLP
- Streamlit
- Scikit-Learn
- SQL
- Power BI
- Git & GitHub
""")

st.divider()

# ==========================================
# Contact
# ==========================================

st.header("📬 Contact")

c1, c2 = st.columns(2)

with c1:
    st.info("""
**Email**

rautbhagya16@gmail.com

**GitHub**

github.com/bhagya21-tech
""")

with c2:
    st.info("""
**LinkedIn**

linkedin.com/in/bhagyashri-raut-471960322

**Location**

Maharashtra, India
""")

st.divider()

# ==========================================
# Quote
# ==========================================

st.success("""
*"AI is most valuable when it helps people make safer and smarter decisions."*
""")

# ==========================================
# Footer
# ==========================================

st.markdown("""
<div class="footer">

<b>FraudLens AI</b>

<br>

Enterprise Recruitment Fraud Detection Platform

<br><br>

Built with ❤️ using Python, Machine Learning, NLP & Streamlit

<br><br>

© 2026 Bhagyashri Raut

</div>
""", unsafe_allow_html=True)