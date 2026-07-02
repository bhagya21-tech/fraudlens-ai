import streamlit as st
import plotly.express as px
import pandas as pd
import os
from datetime import datetime

from src.predictor import predict_job
from src.report import create_report
from src.explain import explain
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

    st.title("🛡 FraudLens AI")

    st.caption("Enterprise Recruitment Intelligence")

    st.divider()

    st.success("🟢 AI Model Ready")

    st.write("**Model:** Logistic Regression")

    st.write("**Vectorizer:** TF-IDF")

    st.write("**Status:** Online")

    st.divider()

    st.info("""
### Features

✔ Fraud Detection

✔ Confidence Score

✔ AI Explanation

✔ PDF Report

✔ Prediction History
""")

# ======================================================
# Hero Banner
# ======================================================

st.markdown("""
<div class="hero">

<h1>🛡 FraudLens AI</h1>

<p>

AI Powered Fake Job Posting Detection using
Machine Learning & Natural Language Processing

</p>

</div>
""", unsafe_allow_html=True)

# ======================================================
# Dashboard Metrics
# ======================================================

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        "Model",
        "Logistic Regression"
    )

with m2:
    st.metric(
        "Accuracy",
        "98.7%"
    )

with m3:
    st.metric(
        "Dataset",
        "20K+ Jobs"
    )

with m4:
    st.metric(
        "Features",
        "653"
    )

st.divider()

# ======================================================
# Job Information
# ======================================================

st.subheader("📋 Job Information")

left, right = st.columns(2)

# ------------------------------------------------------
# Left
# ------------------------------------------------------

with left:

    job_title = st.text_input(
        "Job Title"
    )

    industry = st.text_input(
        "Industry"
    )

    department = st.text_input(
        "Department"
    )

    job_function = st.text_input(
        "Job Function"
    )

# ------------------------------------------------------
# Right
# ------------------------------------------------------

with right:

    company_profile = st.text_area(

        "Company Profile",

        height=170

    )

    benefits = st.text_area(

        "Benefits",

        height=120

    )

st.divider()

# ======================================================
# Description
# ======================================================

st.subheader("📝 Job Description")

job_description = st.text_area(

    "Job Description",

    height=220

)

requirements = st.text_area(

    "Requirements",

    height=180

)

st.divider()

# ======================================================
# Additional Information
# ======================================================

st.subheader("⚙ Additional Information")

c1, c2, c3, c4 = st.columns(4)

with c1:

    required_experience_years = st.number_input(

        "Experience",

        min_value=0,

        max_value=30,

        value=1

    )

with c2:

    num_open_positions = st.number_input(

        "Open Positions",

        min_value=1,

        max_value=100,

        value=1

    )

with c3:

    has_logo = st.selectbox(

        "Company Logo",

        ["Yes", "No"]

    )

with c4:

    telecommuting = st.selectbox(

        "Remote Job",

        ["Yes", "No"]

    )

st.write("")

# ======================================================
# Analyze Button
# ======================================================

analyze = st.button(

    "🔍 Analyze Job Posting",

    use_container_width=True

)

# ======================================================
# Prediction Starts Here
# ======================================================

if analyze:

    if job_title.strip() == "" and job_description.strip() == "":

        st.warning(
            "Please enter at least Job Title or Job Description."
        )

        st.stop()

    job = {

        "job_title": job_title,

        "company_profile": company_profile,

        "requirements": requirements,

        "job_description": job_description,

        "benefits": benefits,

        "industry": industry,

        "department": department,

        "job_function": job_function,

        "required_experience_years": required_experience_years,

        "num_open_positions": num_open_positions,

        "has_logo": 1 if has_logo == "Yes" else 0,

        "telecommuting": 1 if telecommuting == "Yes" else 0

    }

    with st.spinner("Analyzing job posting..."):

        result = predict_job(job)

    confidence = max(

        result["real_probability"],

        result["fake_probability"]

    )

    st.divider()

    st.subheader("🎯 Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:

        if result["prediction"] == "Fake Job":

            st.error("🚨 Fake Job Posting")

        else:

            st.success("✅ Legitimate Job")

    with col2:

        st.metric(

            "Confidence",

            f"{confidence*100:.2f}%"

        )

    with col3:

        if confidence >= 0.95:

            risk = "Very Low"

        elif confidence >= 0.80:

            risk = "Low"

        elif confidence >= 0.60:

            risk = "Medium"

        else:

            risk = "High"

        st.metric(

            "Risk Level",

            risk

        )

        # ======================================================
    # Probability Donut Chart
    # ======================================================

    st.divider()

    st.subheader("📊 Prediction Probability")

    donut = px.pie(

        names=["Real Job", "Fake Job"],

        values=[
            result["real_probability"],
            result["fake_probability"]
        ],

        hole=0.65,

        color=["Real Job", "Fake Job"],

        color_discrete_map={
            "Real Job": "#22C55E",
            "Fake Job": "#EF4444"
        }

    )

    donut.update_layout(
        height=420,
        showlegend=True
    )

    st.plotly_chart(
        donut,
        use_container_width=True
    )

    # ======================================================
    # Probability Bar Chart
    # ======================================================

    fig = px.bar(

        x=["Real Job", "Fake Job"],

        y=[
            result["real_probability"],
            result["fake_probability"]
        ],

        text=[
            f"{result['real_probability']:.2%}",
            f"{result['fake_probability']:.2%}"
        ],

        color=[
            "Real Job",
            "Fake Job"
        ],

        color_discrete_map={
            "Real Job": "#22C55E",
            "Fake Job": "#EF4444"
        }

    )

    fig.update_layout(

        height=400,

        xaxis_title="Prediction",

        yaxis_title="Probability"

    )

    fig.update_yaxes(range=[0,1])

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ======================================================
    # AI Decision Center
    # ======================================================

    st.divider()

    st.subheader("🤖 AI Decision Center")

    left, right = st.columns([2,1])

    with left:

        st.markdown("### Why did the AI make this prediction?")

        reasons = explain(job)

        if len(reasons) == 0:

            st.success(
                "No suspicious indicators were detected."
            )

        else:

            for reason in reasons:

                st.write(f"✅ {reason}")

    with right:

        score = confidence * 100

        st.metric(
            "Trust Score",
            f"{score:.1f}/100"
        )

        if score >= 90:

            st.success("Excellent")

        elif score >= 75:

            st.info("Good")

        elif score >= 60:

            st.warning("Needs Verification")

        else:

            st.error("Highly Suspicious")

    # ======================================================
    # AI Recommendations
    # ======================================================

    st.divider()

    st.subheader("💡 AI Recommendations")

    recommendations = []

    if has_logo == "No":
        recommendations.append(
            "Company logo is missing."
        )

    if required_experience_years == 0:
        recommendations.append(
            "Experience requirement is not specified."
        )

    if len(company_profile) < 50:
        recommendations.append(
            "Company profile is very short."
        )

    if len(job_description) < 150:
        recommendations.append(
            "Job description is unusually short."
        )

    if telecommuting == "Yes":
        recommendations.append(
            "Verify remote jobs carefully before applying."
        )

    if len(recommendations) == 0:

        st.success(
            "This posting follows most characteristics of a legitimate job advertisement."
        )

    else:

        for rec in recommendations:

            st.warning(rec)

    # ======================================================
    # Prediction Summary
    # ======================================================

    st.divider()

    st.subheader("📋 Prediction Summary")

    summary = pd.DataFrame({

        "Field":[

            "Prediction",

            "Confidence",

            "Industry",

            "Department",

            "Experience",

            "Remote",

            "Company Logo"

        ],

        "Value":[

            result["prediction"],

            f"{confidence*100:.2f}%",

            industry,

            department,

            required_experience_years,

            telecommuting,

            has_logo

        ]

    })

    st.dataframe(

        summary,

        hide_index=True,

        use_container_width=True

    )

        # ======================================================
    # Save Prediction History
    # ======================================================

    history = {

        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "Prediction": result["prediction"],

        "Confidence": round(confidence * 100, 2),

        "Job Title": job_title,

        "Industry": industry

    }

    history_file = "data/prediction_history.csv"

    history_df = pd.DataFrame([history])

    if os.path.exists(history_file):

        history_df.to_csv(

            history_file,

            mode="a",

            header=False,

            index=False

        )

    else:

        history_df.to_csv(

            history_file,

            index=False

        )

    # ======================================================
    # PDF Report
    # ======================================================

    st.divider()

    st.subheader("📄 Download Prediction Report")

    try:

        create_report(

            result,

            "prediction_report.pdf"

        )

        with open(

            "prediction_report.pdf",

            "rb"

        ) as pdf:

            st.download_button(

                label="📥 Download PDF Report",

                data=pdf,

                file_name="Prediction_Report.pdf",

                mime="application/pdf",

                use_container_width=True

            )

    except Exception as e:

        st.warning(

            f"Unable to generate PDF report.\n\n{e}"

        )

    # ======================================================
    # Export Prediction Summary
    # ======================================================

    st.divider()

    csv_summary = summary.to_csv(index=False)

    st.download_button(

        label="📊 Download Prediction Summary (CSV)",

        data=csv_summary,

        file_name="prediction_summary.csv",

        mime="text/csv",

        use_container_width=True

    )

    # ======================================================
    # Final Success Message
    # ======================================================

    st.success(

        "✅ Analysis completed successfully."

    )

# ======================================================
# Footer
# ======================================================

st.divider()

st.markdown("""

<div class="footer">

<h3>🛡 FraudLens AI</h3>

Enterprise Recruitment Intelligence Platform

<br><br>

Built with Python • Scikit-Learn • NLP • Plotly • Streamlit

<br><br>

Developed by <b>Bhagyashri Raut</b>

<br>

© 2026 All Rights Reserved

</div>

""", unsafe_allow_html=True)