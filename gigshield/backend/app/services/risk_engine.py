"""
GigShield — Risk Engine
Calls the trained XGBoost model and returns a risk score (0–100)
for a given worker profile.
"""

# from app.ml.risk_model import RiskModel
# from app.schemas.user import WorkerProfile

# model = RiskModel()


def calculate_risk_score(worker_profile: dict) -> dict:
    """
    Input:  worker_profile (location, history, work_pattern, zone, claims_history)
    Output: risk_score (0–100), risk_level (Low / Medium / High)
    """
    # TODO: Replace with actual model inference
    # features = extract_features(worker_profile)
    # score = model.predict(features)
    score = 42  # Mock value
    level = "Low" if score < 35 else "Medium" if score < 70 else "High"
    return {"risk_score": score, "risk_level": level}


def extract_features(profile: dict) -> list:
    """
    Transforms raw worker profile into feature vector for ML model.
    Features: [zone_risk, avg_daily_orders, claim_count, shift_hours,
               weather_exposure_score, loyalty_weeks]
    """
    return [
        profile.get("zone_risk", 0.5),
        profile.get("avg_daily_orders", 20),
        profile.get("claim_count", 0),
        profile.get("shift_hours", 8),
        profile.get("weather_exposure", 0.3),
        profile.get("loyalty_weeks", 1),
    ]
