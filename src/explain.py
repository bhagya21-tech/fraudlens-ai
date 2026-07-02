def explain(job):

    reasons = []

    if len(job["company_profile"]) < 20:
        reasons.append("Company profile is very short.")

    if job["telecommuting"] == 1:
        reasons.append("Remote jobs may require additional verification.")

    if job["has_logo"] == 0:
        reasons.append("Company logo is missing.")

    if job["required_experience_years"] == 0:
        reasons.append("No experience requirement specified.")

    return reasons 

    