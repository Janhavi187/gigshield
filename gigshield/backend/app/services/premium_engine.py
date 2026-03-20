"""
GigShield — Premium Engine
Calculates the weekly insurance premium based on:
  - AI risk score (0–100)
  - Zone volatility
  - Loyalty tier (weeks of continuous coverage)
  - Past claim history
"""


BASE_PREMIUM: float = 30.0  # ₹ base weekly premium
MIN_PREMIUM:  float = 20.0  # ₹ floor
MAX_PREMIUM:  float = 60.0  # ₹ ceiling

LOYALTY_DISCOUNT = {    # weeks → discount %
    4:  0.05,           # 1 month: 5% off
    12: 0.10,           # 3 months: 10% off
    24: 0.15,           # 6 months: 15% off
}


def calculate_premium(risk_score: int, zone_volatility: float,
                      loyalty_weeks: int, claim_count: int) -> dict:
    """
    Returns the weekly premium in ₹ with a full breakdown.

    risk_score      : 0–100 (from XGBoost risk model)
    zone_volatility : 0.0–1.0 (how volatile the zone is historically)
    loyalty_weeks   : consecutive weeks the worker has been covered
    claim_count     : total claims in the last 30 days
    """

    # Step 1: Risk-adjusted premium
    risk_factor = 1 + (risk_score / 100) * 0.8         # +0% to +80%
    premium = BASE_PREMIUM * risk_factor

    # Step 2: Zone volatility adjustment
    premium += zone_volatility * 10                     # Up to +₹10

    # Step 3: Claims loading (frequent claimants pay slightly more)
    if claim_count > 1:
        premium += claim_count * 2                      # +₹2 per extra claim

    # Step 4: Loyalty discount
    discount_pct = 0.0
    for weeks, discount in sorted(LOYALTY_DISCOUNT.items(), reverse=True):
        if loyalty_weeks >= weeks:
            discount_pct = discount
            break
    premium = premium * (1 - discount_pct)

    # Clamp to [MIN, MAX]
    premium = max(MIN_PREMIUM, min(MAX_PREMIUM, round(float(premium), 2)))

    return {
        "weekly_premium_inr": premium,
        "risk_factor": round(float(risk_factor), 3),
        "loyalty_discount_pct": round(float(discount_pct) * 100, 1),
        "zone_volatility": zone_volatility,
    }
