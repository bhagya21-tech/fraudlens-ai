MODEL_PATH = "models/best_model.pkl"
TFIDF_PATH = "models/tfidf.pkl"
SCALER_PATH = "models/scaler.pkl" 

TEXT_COLUMNS = [
    "job_title",
    "company_profile",
    "requirements",
    "job_description",
    "benefits",
    "industry",
    "department",
    "job_function"
]

STRUCTURED_COLUMNS = [
    "required_experience_years",
    "num_open_positions",
    "has_logo",
    "telecommuting"
]