"""
GigShield — Fraud Detection
Isolation Forest anomaly detection + rule-based validation.
Flags suspicious claims before payout is processed.
"""

# from sklearn.ensemble import IsolationForest
# import numpy as np

# Trained model (load from saved artifact in production)
# fraud_model = IsolationForest(contamination=0.05, random_state=42)


def is_fraudulent(claim_data: dict) -> dict:
    """
    Input:  claim_data (gps_coords, device_id, claim_time, claim_count_7d, activity_log)
    Output: {"flagged": bool, "reason": str, "anomaly_score": float}
    """
    flags = []

    # Rule 1: Too many claims in 7 days
    if claim_data.get("claim_count_7d", 0) > 3:
        flags.append("EXCESSIVE_CLAIMS")

    # Rule 2: GPS not within the triggered zone
    if not claim_data.get("gps_in_zone", True):
        flags.append("GPS_OUT_OF_ZONE")

    # Rule 3: Device ID mismatch
    if claim_data.get("device_mismatch", False):
        flags.append("DEVICE_MISMATCH")

    # Rule 4: Claim filed within 60s of trigger (too fast = suspicious)
    if claim_data.get("response_time_seconds", 999) < 60:
        flags.append("INSTANT_CLAIM_SUSPICIOUS")

    # ML anomaly score (Isolation Forest)
    # features = extract_fraud_features(claim_data)
    # score = fraud_model.decision_function([features])[0]
    score: float = 0.1  # Mock: positive = normal, negative = anomalous

    flagged = len(flags) > 0 or score < -0.2
    return {
        "flagged": flagged,
        "reason": ", ".join(flags) if flags else "NONE",
        "anomaly_score": round(float(score), 4),
    }
