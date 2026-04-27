import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the park zone have an average temperature between 20.7 and 27.5 degrees Celsius."""
    zone_df = df[df["zone"] == "park"]
    if zone_df.empty:
        return True, "No park sensors to evaluate."
    condition = zone_df["avg_temp_c"].between(20.7, 27.5, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} park sensors have avg_temp_c in [20.7, 27.5]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} park sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the downtown zone have an average temperature between 21.3 and 22.0 degrees Celsius."""
    zone_df = df[df["zone"] == "downtown"]
    if zone_df.empty:
        return True, "No downtown sensors to evaluate."
    condition = zone_df["avg_temp_c"].between(21.3, 22.0, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} downtown sensors have avg_temp_c in [21.3, 22.0]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} downtown sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_3(df: pd.DataFrame):
    """3. All sensors in the residential zone have an average temperature between 23.2 and 27.5 degrees Celsius."""
    zone_df = df[df["zone"] == "residential"]
    if zone_df.empty:
        return True, "No residential sensors to evaluate."
    condition = zone_df["avg_temp_c"].between(23.2, 27.5, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} residential sensors have avg_temp_c in [23.2, 27.5]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} residential sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_4(df: pd.DataFrame):
    """4. All sensors in the industrial zone have an average temperature of 25.7 degrees Celsius."""
    zone_df = df[df["zone"] == "industrial"]
    if zone_df.empty:
        return True, "No industrial sensors to evaluate."
    condition = zone_df["avg_temp_c"] == 25.7
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} industrial sensors have avg_temp_c exactly 25.7."
    viol = zone_df[~condition]
    return False, f"{len(viol)} industrial sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_5(df: pd.DataFrame):
    """5. If a sensor is in the park zone, then its average humidity is between 49.9 and 64.2 percent."""
    zone_df = df[df["zone"] == "park"]
    if zone_df.empty:
        return True, "No park sensors to evaluate."
    condition = zone_df["avg_humidity"].between(49.9, 64.2, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} park sensors have avg_humidity in [49.9, 64.2]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} park sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_6(df: pd.DataFrame):
    """6. If a sensor is in the downtown zone, then its average humidity is between 61.6 and 65.1 percent."""
    zone_df = df[df["zone"] == "downtown"]
    if zone_df.empty:
        return True, "No downtown sensors to evaluate."
    condition = zone_df["avg_humidity"].between(61.6, 65.1, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} downtown sensors have avg_humidity in [61.6, 65.1]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} downtown sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_7(df: pd.DataFrame):
    """7. If a sensor is in the residential zone, then its average humidity is between 51.0 and 67.3 percent."""
    zone_df = df[df["zone"] == "residential"]
    if zone_df.empty:
        return True, "No residential sensors to evaluate."
    condition = zone_df["avg_humidity"].between(51.0, 67.3, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} residential sensors have avg_humidity in [51.0, 67.3]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} residential sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_8(df: pd.DataFrame):
    """8. All sensors in the park zone have a PM2.5 level between 9.7 and 27.8."""
    zone_df = df[df["zone"] == "park"]
    if zone_df.empty:
        return True, "No park sensors to evaluate."
    condition = zone_df["pm25"].between(9.7, 27.8, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} park sensors have pm25 in [9.7, 27.8]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} park sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_9(df: pd.DataFrame):
    """9. All sensors in the downtown zone have a PM2.5 level between 12.6 and 27.3."""
    zone_df = df[df["zone"] == "downtown"]
    if zone_df.empty:
        return True, "No downtown sensors to evaluate."
    condition = zone_df["pm25"].between(12.6, 27.3, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} downtown sensors have pm25 in [12.6, 27.3]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} downtown sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_10(df: pd.DataFrame):
    """10. All sensors in the residential zone have a PM2.5 level between 22.7 and 30.6."""
    zone_df = df[df["zone"] == "residential"]
    if zone_df.empty:
        return True, "No residential sensors to evaluate."
    condition = zone_df["pm25"].between(22.7, 30.6, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} residential sensors have pm25 in [22.7, 30.6]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} residential sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_11(df: pd.DataFrame):
    """11. If a sensor is in the park zone, then its noise level is between 41.6 and 75.4 decibels."""
    zone_df = df[df["zone"] == "park"]
    if zone_df.empty:
        return True, "No park sensors to evaluate."
    condition = zone_df["noise_db"].between(41.6, 75.4, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} park sensors have noise_db in [41.6, 75.4]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} park sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_12(df: pd.DataFrame):
    """12. If a sensor is in the downtown zone, then its noise level is between 46.6 and 55.0 decibels."""
    zone_df = df[df["zone"] == "downtown"]
    if zone_df.empty:
        return True, "No downtown sensors to evaluate."
    condition = zone_df["noise_db"].between(46.6, 55.0, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} downtown sensors have noise_db in [46.6, 55.0]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} downtown sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_13(df: pd.DataFrame):
    """13. If a sensor is in the residential zone, then its noise level is between 40.2 and 69.0 decibels."""
    zone_df = df[df["zone"] == "residential"]
    if zone_df.empty:
        return True, "No residential sensors to evaluate."
    condition = zone_df["noise_db"].between(40.2, 69.0, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} residential sensors have noise_db in [40.2, 69.0]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} residential sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_14(df: pd.DataFrame):
    """14. All sensors in the park zone have foot traffic between 591 and 1416."""
    zone_df = df[df["zone"] == "park"]
    if zone_df.empty:
        return True, "No park sensors to evaluate."
    condition = zone_df["foot_traffic"].between(591, 1416, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} park sensors have foot_traffic in [591, 1416]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} park sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_15(df: pd.DataFrame):
    """15. All sensors in the downtown zone have foot traffic between 474 and 1435."""
    zone_df = df[df["zone"] == "downtown"]
    if zone_df.empty:
        return True, "No downtown sensors to evaluate."
    condition = zone_df["foot_traffic"].between(474, 1435, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} downtown sensors have foot_traffic in [474, 1435]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} downtown sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_16(df: pd.DataFrame):
    """16. All sensors in the residential zone have foot traffic between 580 and 658."""
    zone_df = df[df["zone"] == "residential"]
    if zone_df.empty:
        return True, "No residential sensors to evaluate."
    condition = zone_df["foot_traffic"].between(580, 658, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} residential sensors have foot_traffic in [580, 658]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} residential sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_17(df: pd.DataFrame):
    """17. If a sensor is in the park zone, then its power usage is between 210.8 and 439.7 kilowatt-hours."""
    zone_df = df[df["zone"] == "park"]
    if zone_df.empty:
        return True, "No park sensors to evaluate."
    condition = zone_df["power_use_kwh"].between(210.8, 439.7, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} park sensors have power_use_kwh in [210.8, 439.7]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} park sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_18(df: pd.DataFrame):
    """18. If a sensor is in the downtown zone, then its power usage is between 127.4 and 362.6 kilowatt-hours."""
    zone_df = df[df["zone"] == "downtown"]
    if zone_df.empty:
        return True, "No downtown sensors to evaluate."
    condition = zone_df["power_use_kwh"].between(127.4, 362.6, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} downtown sensors have power_use_kwh in [127.4, 362.6]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} downtown sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_19(df: pd.DataFrame):
    """19. If a sensor is in the residential zone, then its power usage is between 116.5 and 366.0 kilowatt-hours."""
    zone_df = df[df["zone"] == "residential"]
    if zone_df.empty:
        return True, "No residential sensors to evaluate."
    condition = zone_df["power_use_kwh"].between(116.5, 366.0, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(zone_df)} residential sensors have power_use_kwh in [116.5, 366.0]."
    viol = zone_df[~condition]
    return False, f"{len(viol)} residential sensors violate the rule (ids: {', '.join(viol['sensor_id'])})."

def stmt_20(df: pd.DataFrame):
    """20. Most sensors in the park zone have an average temperature greater than 22 degrees Celsius."""
    zone_df = df[df["zone"] == "park"]
    if zone_df.empty:
        return True, "No park sensors to evaluate."
    condition = zone_df["avg_temp_c"] > 22
    count_true = condition.sum()
    total = len(zone_df)
    truth = count_true > total / 2
    if truth:
        return True, f"{count_true} of {total} park sensors have avg_temp_c > 22."
    else:
        return False, f"{count_true} of {total} park sensors have avg_temp_c > 22 (not a majority)."

def stmt_21(df: pd.DataFrame):
    """21. Most sensors in the downtown zone have an average temperature less than 22 degrees Celsius."""
    zone_df = df[df["zone"] == "downtown"]
    if zone_df.empty:
        return True, "No downtown sensors to evaluate."
    condition = zone_df["avg_temp_c"] < 22
    count_true = condition.sum()
    total = len(zone_df)
    truth = count_true > total / 2
    if truth:
        return True, f"{count_true} of {total} downtown sensors have avg_temp_c < 22."
    else:
        return False, f"{count_true} of {total} downtown sensors have avg_temp_c < 22 (not a majority)."

def stmt_22(df: pd.DataFrame):
    """22. Most sensors in the residential zone have an average temperature greater than 25 degrees Celsius."""
    zone_df = df[df["zone"] == "residential"]
    if zone_df.empty:
        return True, "No residential sensors to evaluate."
    condition = zone_df["avg_temp_c"] > 25
    count_true = condition.sum()
    total = len(zone_df)
    truth = count_true > total / 2
    if truth:
        return True, f"{count_true} of {total} residential sensors have avg_temp_c > 25."
    else:
        return False, f"{count_true} of {total} residential sensors have avg_temp_c > 25 (not a majority)."

def main():
    df = pd.read_csv("../inference_generation/tables/table_77.csv")

    # Convert numeric columns safely
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            pass

    checks = [
        (1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5),
        (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10),
        (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14),
        (15, stmt_15), (16, stmt_16), (17, stmt_17), (18, stmt_18),
        (19, stmt_19), (20, stmt_20), (21, stmt_21), (22, stmt_22)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()