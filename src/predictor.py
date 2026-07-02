import pickle 
import pandas as pd 
from scipy.sparse import hstack

# Load saved objects

model = pickle.load(open("models/best_model.pkl","rb"))
tfidf = pickle.load(open("models/tfidf.pkl","rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

structured_cols = [
    "required_experience_years",
    "num_open_positions",
    "has_logo",
    "telecommuting"
]

def predict_job(job_data: dict):
    """
    Predict whether a job posting is fake or real.

    Parameters
    ----------
    job_data : dict
        Dictionary containing job information.
    
    Returns
    -------
    dict
    """

    text = " ".join([
        str(job_data.get("job_title", "")),
        str(job_data.get("company_profile", "")),
        str(job_data.get("requirements", "")),
        str(job_data.get("job_description", "")),
        str(job_data.get("benefits", "")),
        str(job_data.get("industry", "")),
        str(job_data.get("department", "")),
        str(job_data.get("job_function", ""))
    ])

    text_vector = tfidf.transform([text])

    structured = pd.DataFrame([{
        col: job_data.get(col, 0)
        for col in structured_cols
    }])

    structured_scaled = scaler.transform(structured)

    features = hstack([
        text_vector,
        structured_scaled
    ])

    prediction = model.predict(features)[0]

    result = {
        "prediction": "Fake Job" if prediction == 1 else "Real Job"

    }

    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(features)[0]

        result["real_probability"] = round(float(probs[0]), 4)
        result["fake_probability"] = round(float(probs[1]), 4)

    return result 