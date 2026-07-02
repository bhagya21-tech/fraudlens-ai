import streamlit as st
import pandas as pd
import os
from PIL import Image
from src.utils import load_css

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