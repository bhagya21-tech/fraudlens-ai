"""
====================================================
FraudLens AI Utility Functions
Author : Bhagyashri Raut
====================================================
"""

from pathlib import Path
import streamlit as st
import pandas as pd

# ==========================================
# Project Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
REPORT_DIR = BASE_DIR / "reports"
ASSET_DIR = BASE_DIR / "assets"

# ==========================================
# Load Custom CSS
# ==========================================

def load_css():

    css_file = ASSET_DIR / "style.css"

    if css_file.exists():

        with open(css_file, "r", encoding="utf-8") as f:

            st.markdown(

                f"<style>{f.read()}</style>",

                unsafe_allow_html=True

            )

# ==========================================
# Load Dataset
# ==========================================

def load_dataset():

    dataset = DATA_DIR / "fake_real_job_postings.csv"

    return pd.read_csv(dataset)

# ==========================================
# Load Processed Dataset
# ==========================================

def load_processed_dataset():

    dataset = DATA_DIR / "processed_jobs.csv"

    return pd.read_csv(dataset)

# ==========================================
# Page Header
# ==========================================

def page_header(title, subtitle):

    st.markdown(f"""
    <div class="hero">

    <h1>{title}</h1>

    <p>{subtitle}</p>

    </div>
    """, unsafe_allow_html=True)

# ==========================================
# Metric Card
# ==========================================

def metric_card(label, value):

    st.metric(

        label,

        value

    )

# ==========================================
# Success Message
# ==========================================

def success(message):

    st.success(message)

# ==========================================
# Warning Message
# ==========================================

def warning(message):

    st.warning(message)

# ==========================================
# Error Message
# ==========================================

def error(message):

    st.error(message)

# ==========================================
# Footer
# ==========================================

def footer():

    st.markdown("""

    <div class="footer">

    <b>FraudLens AI</b>

    <br>

    Enterprise Recruitment Fraud Detection Platform

    <br><br>

    Built using Python • Machine Learning • NLP • Streamlit

    <br><br>

    © 2026 Bhagyashri Raut

    </div>

    """, unsafe_allow_html=True)

# ==========================================
# Dataset Summary
# ==========================================

def dataset_summary(df):

    return {

        "Rows": len(df),

        "Columns": len(df.columns),

        "Missing": int(df.isnull().sum().sum()),

        "Duplicates": int(df.duplicated().sum())

    }

# ==========================================
# Prediction Summary
# ==========================================

def prediction_summary(result):

    confidence = max(

        result["real_probability"],

        result["fake_probability"]

    )

    return {

        "Prediction": result["prediction"],

        "Confidence": round(confidence * 100, 2)

    }

# ==========================================
# Check File Exists
# ==========================================

def file_exists(path):

    return Path(path).exists()