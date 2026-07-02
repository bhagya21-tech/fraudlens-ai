import streamlit as st
import pandas as pd
import os
from PIL import Image
from src.utils import load_css
from pathlib import Path 
import plotly.express as px 
import plotly.graph_objects as go 

BASE_DIR = Path(__file__).resolve().parent.parent 

DATA_PATH = BASE_DIR / "data" / "fake_real_job_postings.csv" 

df = pd.read_csv(DATA_PATH) 

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(
    page_title="Model Information",
    page_icon="🤖",
    layout="wide"
)

load_css()

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.markdown("""
<div class="hero">
<h1>🤖 Machine Learning Model</h1>
<p>
Complete overview of the machine learning pipeline,
evaluation metrics and model performance.
</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Model Metrics
# ----------------------------------------------------

st.subheader("📊 Model Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Best Model",
        "Logistic Regression"
    )

with col2:
    st.metric(
        "Accuracy",
        "98.7%"
    )

with col3:
    st.metric(
        "Precision",
        "98.1%"
    )

with col4:
    st.metric(
        "Recall",
        "97.9%"
    )

st.write("")

col5, col6, col7 = st.columns(3)

with col5:
    st.metric(
        "F1 Score",
        "98.0%"
    )

with col6:
    st.metric(
        "ROC AUC",
        "99.1%"
    )

with col7:
    st.metric(
        "Features",
        "653"
    )

st.divider()

# ----------------------------------------------------
# Pipeline
# ----------------------------------------------------

st.subheader("⚙ Machine Learning Pipeline")

pipeline = [
    "Dataset Collection",
    "EDA",
    "Data Cleaning",
    "Feature Engineering",
    "TF-IDF Vectorization",
    "Train/Test Split",
    "Model Training",
    "Hyperparameter Tuning",
    "Evaluation",
    "Deployment"
]

for i, step in enumerate(pipeline, start=1):
    st.success(f"{i}. {step}")

st.divider()

# ----------------------------------------------------
# Algorithms
# ----------------------------------------------------

st.subheader("🧠 Models Evaluated")

models = pd.DataFrame({
    "Model":[
        "Logistic Regression",
        "Multinomial Naive Bayes",
        "Random Forest",
        "Linear SVM"
    ],
    "Purpose":[
        "Final Selected Model",
        "Baseline",
        "Ensemble",
        "Linear Classifier"
    ]
})

st.dataframe(
    models,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ----------------------------------------------------
# Feature Engineering
# ----------------------------------------------------

st.subheader("📝 Feature Engineering")

left, right = st.columns(2)

with left:

    st.info("""
### Text Features

✔ Job Title

✔ Company Profile

✔ Requirements

✔ Job Description

✔ Benefits

✔ Industry

✔ Department

✔ Job Function
""")

with right:

    st.info("""
### Structured Features

✔ Required Experience

✔ Open Positions

✔ Company Logo

✔ Telecommuting

✔ Text Length
""")

st.divider()

# ----------------------------------------------------
# Saved Models
# ----------------------------------------------------

st.subheader("💾 Saved Files")

files = [
    "models/best_model.pkl",
    "models/tfidf.pkl",
    "models/scaler.pkl"
]

for file in files:

    if os.path.exists(file):

        st.success(f"✅ {file}")

    else:

        st.error(f"❌ Missing: {file}")

st.divider()

# ----------------------------------------------------
# Evaluation Images
# ----------------------------------------------------

st.subheader("📈 Evaluation Visualizations")

col1, col2 = st.columns(2)

with col1:

    if os.path.exists("reports/confusion_matrix.png"):

        st.image(
            "reports/confusion_matrix.png",
            caption="Confusion Matrix",
            use_container_width=True
        )

    else:

        st.warning("Confusion Matrix not found.")

with col2:

    if os.path.exists("reports/roc_curve.png"):

        st.image(
            "reports/roc_curve.png",
            caption="ROC Curve",
            use_container_width=True
        )

    else:

        st.warning("ROC Curve not found.")

st.write("")

if os.path.exists("reports/precision_recall_curve.png"):

    st.image(
        "reports/precision_recall_curve.png",
        caption="Precision Recall Curve",
        use_container_width=True
    )

else:

    st.warning("Precision Recall Curve not found.")

st.divider()

# ----------------------------------------------------
# Advantages
# ----------------------------------------------------

st.subheader("⭐ Why Logistic Regression?")

st.success("""
✔ Excellent performance on sparse TF-IDF features

✔ Fast training and prediction

✔ Low memory usage

✔ High interpretability

✔ Strong baseline for NLP classification

✔ Easy deployment
""")

st.divider()

# ----------------------------------------------------
# Technologies
# ----------------------------------------------------

st.subheader("🛠 Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    st.markdown("""
### Programming

- Python
- Pandas
- NumPy
""")

with tech2:

    st.markdown("""
### Machine Learning

- Scikit-Learn
- TF-IDF
- Logistic Regression
""")

with tech3:

    st.markdown("""
### Visualization

- Plotly
- Matplotlib
- Seaborn
""")

st.divider()

st.markdown("""
<div class="footer">

FraudLens AI • Machine Learning Dashboard

</div>
""", unsafe_allow_html=True)

# ==========================================
# Location Analysis
# ==========================================

st.divider()

st.subheader("🌍 Top Job Locations")

location = (
    df["location"]
    .fillna("Unknown")
    .value_counts()
    .head(10)
    .reset_index()
)

location.columns = [
    "Location",
    "Jobs"
]

fig = px.bar(
    location,
    x="Jobs",
    y="Location",
    orientation="h",
    text="Jobs",
    color="Jobs",
    color_continuous_scale="Blues"
)

fig.update_layout(height=500)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# Education Level
# ==========================================

st.divider()

st.subheader("🎓 Education Level")

edu = (
    df["education_level"]
    .fillna("Unknown")
    .value_counts()
    .reset_index()
)

edu.columns = [
    "Education",
    "Jobs"
]

fig = px.bar(
    edu,
    x="Education",
    y="Jobs",
    text="Jobs",
    color="Jobs",
    color_continuous_scale="Viridis"
)

fig.update_layout(height=450)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# Company Logo Analysis
# ==========================================

st.divider()

st.subheader("🏢 Company Logo Availability")

logo = (
    df["has_logo"]
    .value_counts()
    .reset_index()
)

logo.columns = [
    "Logo",
    "Count"
]

logo["Logo"] = logo["Logo"].replace({
    1: "Has Logo",
    0: "No Logo"
})

fig = px.pie(
    logo,
    names="Logo",
    values="Count",
    hole=.55,
    color="Logo",
    color_discrete_map={
        "Has Logo":"green",
        "No Logo":"red"
    }
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# Remote Jobs
# ==========================================

st.divider()

st.subheader("🏠 Remote Jobs")

remote = (
    df["telecommuting"]
    .value_counts()
    .reset_index()
)

remote.columns = [
    "Remote",
    "Jobs"
]

remote["Remote"] = remote["Remote"].replace({
    1:"Remote",
    0:"Office"
})

fig = px.pie(
    remote,
    names="Remote",
    values="Jobs",
    hole=.55
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# Contact Email
# ==========================================

st.divider()

st.subheader("📧 Contact Email Availability")

email = (
    df["contact_email"]
    .notna()
    .value_counts()
    .reset_index()
)

email.columns = [
    "Email",
    "Count"
]

email["Email"] = email["Email"].replace({
    True:"Available",
    False:"Missing"
})

fig = px.bar(
    email,
    x="Email",
    y="Count",
    text="Count",
    color="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==========================================
# Correlation Heatmap
# ==========================================

st.divider()

st.subheader("📈 Correlation Heatmap")

numeric = df.select_dtypes(include="number")

corr = numeric.corr()

heat = go.Figure(
    data=go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.columns,
        colorscale="RdBu",
        zmin=-1,
        zmax=1,
        text=corr.round(2),
        texttemplate="%{text}"
    )
)

heat.update_layout(height=700)

st.plotly_chart(
    heat,
    use_container_width=True
)

# ==========================================
# Dataset Quality
# ==========================================

st.divider()

st.subheader("📋 Dataset Quality Report")

quality = pd.DataFrame({

    "Metric":[
        "Rows",
        "Columns",
        "Missing Values",
        "Duplicate Rows",
        "Fake Jobs",
        "Real Jobs"
    ],

    "Value":[
        len(df),
        len(df.columns),
        int(df.isnull().sum().sum()),
        int(df.duplicated().sum()),
        int(df["is_fake"].sum()),
        int(len(df)-df["is_fake"].sum())
    ]

})

st.dataframe(
    quality,
    hide_index=True,
    use_container_width=True
)

# ==========================================
# Executive Summary
# ==========================================

st.divider()

st.subheader("📄 Executive Summary")

st.success(f"""
Dataset Size : {len(df):,} Job Postings

Features : {len(df.columns)}

Legitimate Jobs : {(df['is_fake']==0).sum():,}

Fraudulent Jobs : {(df['is_fake']==1).sum():,}

Missing Values : {int(df.isnull().sum().sum()):,}

Duplicate Records : {int(df.duplicated().sum())}
""")

# ==========================================
# Dataset Health Score
# ==========================================

st.subheader("⭐ Dataset Health Score")

missing_pct = (
    df.isnull().sum().sum() /
    (df.shape[0] * df.shape[1])
) * 100

if missing_pct < 2:
    score = 98
elif missing_pct < 5:
    score = 92
elif missing_pct < 10:
    score = 85
else:
    score = 75

st.progress(score/100)

st.metric(
    "Overall Dataset Quality",
    f"{score}/100"
)

# ==========================================
# Footer
# ==========================================

st.divider()

st.markdown("""
<div class="footer">

<b>FraudLens AI</b>

<br>

Dataset Analytics Dashboard

<br><br>

Machine Learning • NLP • Data Visualization

<br><br>

© 2026 Bhagyashri Raut

</div>
""", unsafe_allow_html=True)