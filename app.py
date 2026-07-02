import streamlit as st
import os
from src.utils import load_css

# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="FraudLens AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# ======================================================
# Sidebar
# ======================================================

with st.sidebar:

    logo = "assets/logo.png"

    if os.path.exists(logo):
        st.image(logo, width=120)

    st.title("FraudLens AI")

    st.caption("Enterprise Recruitment Intelligence")

    st.divider()

    st.success("🟢 System Online")

    st.markdown("""
### Navigation

Use the pages below

🔍 Predict Job

🤖 Model Information

📊 Dataset Insights

📖 About Project

📜 Prediction History
""")

    st.divider()

    st.info("""
### Current Model

**Algorithm**

Logistic Regression

**Vectorizer**

TF-IDF

**Status**

Production Ready
""")

# ======================================================
# Hero Section
# ======================================================

st.markdown("""

<div class="hero">

<h1>🛡 FraudLens AI</h1>

<p>

Detect fraudulent job postings using Machine Learning,
Natural Language Processing and Explainable AI.

</p>

</div>

""", unsafe_allow_html=True)

# ======================================================
# KPI Dashboard
# ======================================================

st.subheader("📊 Platform Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(

        "Accuracy",

        "98.7%"

    )

with c2:

    st.metric(

        "Dataset",

        "20K+ Jobs"

    )

with c3:

    st.metric(

        "Features",

        "653"

    )

with c4:

    st.metric(

        "Prediction Time",

        "< 1 sec"

    )

st.divider()

# ======================================================
# About Platform
# ======================================================

st.subheader("🚀 About FraudLens AI")

left, right = st.columns([2,1])

with left:

    st.markdown("""

FraudLens AI is an intelligent recruitment fraud detection platform designed
to identify fake job advertisements before candidates apply.

The platform combines **Machine Learning**, **Natural Language Processing**
and **Explainable AI** to classify job postings as **Legitimate** or
**Fraudulent**.

### The platform can

- ✅ Detect fake job postings

- ✅ Generate confidence scores

- ✅ Explain model predictions

- ✅ Export professional PDF reports

- ✅ Store prediction history

- ✅ Visualize recruitment analytics

- ✅ Help job seekers avoid recruitment scams

""")

with right:

    st.success("""

### Platform Highlights

✔ AI Powered

✔ Explainable AI

✔ Interactive Dashboard

✔ Prediction Reports

✔ Dataset Analytics

✔ Recruiter Friendly

""")

st.divider()

# ======================================================
# Key Features
# ======================================================

st.subheader("⭐ Core Features")

f1, f2, f3 = st.columns(3)

with f1:

    st.info("""

### 🔍 Fraud Detection

Detect suspicious job advertisements using
Natural Language Processing and Machine Learning.

""")

with f2:

    st.info("""

### 📈 Analytics Dashboard

Interactive visualizations,
dataset insights and model performance.

""")

with f3:

    st.info("""

### 🤖 Explainable AI

Understand why the model classified
a job as fake or legitimate.

""")

st.divider()

# ======================================================
# AI Workflow
# ======================================================

st.subheader("⚙ AI Workflow")

workflow = [

    "📂 Dataset Collection",

    "🧹 Data Cleaning",

    "📊 Exploratory Data Analysis",

    "📝 Text Preprocessing",

    "🔤 TF-IDF Feature Extraction",

    "🤖 Model Training",

    "📈 Model Evaluation",

    "🎯 Fraud Prediction",

    "📄 PDF Report Generation",

    "🌐 Interactive Dashboard"

]

for i, step in enumerate(workflow, start=1):

    st.markdown(f"**{i}.** {step}")

st.divider()

# ======================================================
# Technology Stack
# ======================================================

st.subheader("🛠 Technology Stack")

t1, t2, t3, t4 = st.columns(4)

with t1:

    st.markdown("""

### 🐍 Programming

- Python

- Pandas

- NumPy

- Scikit-Learn

""")

with t2:

    st.markdown("""

### 🤖 Machine Learning

- Logistic Regression

- Naive Bayes

- TF-IDF

- NLP

""")

with t3:

    st.markdown("""

### 📊 Visualization

- Plotly

- Matplotlib

- Streamlit

- ReportLab

""")

with t4:

    st.markdown("""

### 🚀 Deployment

- Git

- GitHub

- Streamlit

- Render

""")

st.divider()

# ======================================================
# Model Performance
# ======================================================

st.subheader("📈 Model Performance")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Accuracy", "98.7%")

with m2:
    st.metric("Precision", "98.2%")

with m3:
    st.metric("Recall", "97.9%")

with m4:
    st.metric("F1 Score", "98.0%")

st.divider()

# ======================================================
# Why FraudLens AI
# ======================================================

st.subheader("💡 Why Choose FraudLens AI?")

c1, c2, c3 = st.columns(3)

with c1:

    st.success("""

### ⚡ Fast

Predicts job authenticity
within seconds.

""")

with c2:

    st.success("""

### 🛡 Secure

Helps identify fraudulent
job advertisements before
applying.

""")

with c3:

    st.success("""

### 🤖 Explainable

Provides confidence score
and reasoning behind
every prediction.

""")

st.divider()

# ======================================================
# Project Statistics
# ======================================================

st.subheader("📊 Project Statistics")

s1, s2, s3 = st.columns(3)

with s1:

    st.metric(

        "Models Compared",

        "4"

    )

with s2:

    st.metric(

        "Dataset Size",

        "20,000+"

    )

with s3:

    st.metric(

        "Best Model",

        "Logistic Regression"

    )

st.divider()

# ======================================================
# Developer
# ======================================================

st.subheader("👩‍💻 Developer")

st.info("""

**Bhagyashri Raut**

AI • Machine Learning • Data Science

Passionate about building practical AI applications
using Machine Learning, NLP and Data Analytics.

**Core Skills**

• Python

• Machine Learning

• Data Science

• NLP

• Streamlit

• SQL

• Power BI

• Git & GitHub

""")

st.divider()

# ======================================================
# Call To Action
# ======================================================

st.success("""

## 🚀 Ready to Try?

Use the **Predict Job** page from the sidebar to analyze
a new job posting and detect whether it is legitimate
or fraudulent.

""")

st.divider()

# ======================================================
# Footer
# ======================================================

st.markdown("""

<div class="footer">

<h3>🛡 FraudLens AI</h3>

Enterprise Recruitment Fraud Detection Platform

<br><br>

Built with ❤️ using Python • Machine Learning • NLP • Streamlit

<br><br>

© 2026 Bhagyashri Raut

</div>

""", unsafe_allow_html=True)