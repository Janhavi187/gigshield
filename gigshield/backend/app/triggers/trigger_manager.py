"""
GigShield — Parametric Trigger Manager
Celery task that runs every 5 minutes and checks all triggers.
If a trigger fires → auto-initiate claim for affected workers.
"""

# from celery import Celery
# from app.triggers.weather_trigger import check_weather
# from app.triggers.aqi_trigger import check_aqi
# from app.triggers.traffic_trigger import check_traffic
# from app.triggers.zone_trigger import check_zone_closures
# from app.services.payout_service import initiate_claim

# celery_app = Celery("gigshield", broker="redis://localhost:6379/0")


# @celery_app.task
def run_all_triggers(zone_id: str, coordinates: dict):
    """
    Runs every 5 minutes via Celery Beat.
    Checks all parametric conditions and triggers claims if thresholds breached.
    """
    results = {}

    # 1. Weather check
    # weather_event = check_weather(coordinates)
    # if weather_event["triggered"]:
    #     initiate_claim(zone_id, trigger_type="WEATHER", data=weather_event)
    #     results["weather"] = weather_event

    # 2. AQI check
    # aqi_event = check_aqi(coordinates)
    # if aqi_event["triggered"]:
    #     initiate_claim(zone_id, trigger_type="AQI", data=aqi_event)
    #     results["aqi"] = aqi_event

    # 3. Traffic check
    # traffic_event = check_traffic(zone_id)
    # if traffic_event["triggered"]:
    #     initiate_claim(zone_id, trigger_type="TRAFFIC", data=traffic_event)
    #     results["traffic"] = traffic_event

    # 4. Zone closure check
    # zone_event = check_zone_closures(zone_id)
    # if zone_event["triggered"]:
    #     initiate_claim(zone_id, trigger_type="ZONE_CLOSURE", data=zone_event)
    #     results["zone"] = zone_event

    return results


TRIGGER_THRESHOLDS = {
    "RAIN_MM": 15,           # Rainfall > 15mm triggers
    "AQI_INDEX": 200,        # AQI > 200 (Hazardous) triggers
    "TRAFFIC_SPEED_KMPH": 10, # Avg speed < 10 km/h for > 30 min
    "ZONE_CLOSURE": True,    # Any official closure triggers
}
