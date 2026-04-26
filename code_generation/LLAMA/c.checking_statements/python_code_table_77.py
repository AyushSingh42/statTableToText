import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the park zone have an average temperature between 20.7 and 27.5 degrees Celsius."""
    park_sensors = df[df["zone"] == "park"]
    condition = park_sensors["avg_temp_c"].between(20.7, 27.5, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park zone sensors have avg temp between 20.7 and 27.5°C."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the downtown zone have an average temperature between 21.3 and 22.0 degrees Celsius."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["avg_temp_c"].between(21.3, 22.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown_sensors)} downtown zone sensors have avg temp between 21.3 and 22.0°C."
    else:
        viol = downtown_sensors[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All sensors in the residential zone have an average temperature between 23.2 and 27.5 degrees Celsius."""
    residential_sensors = df[df["zone"] == "residential"]
    condition = residential_sensors["avg_temp_c"].between(23.2, 27.5, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential_sensors)} residential zone sensors have avg temp between 23.2 and 27.5°C."
    else:
        viol = residential_sensors[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All sensors in the industrial zone have an average temperature of 25.7 degrees Celsius."""
    industrial_sensors = df[df["zone"] == "industrial"]
    condition = industrial_sensors["avg_temp_c"] == 25.7
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial_sensors)} industrial zone sensors have avg temp of exactly 25.7°C."
    else:
        viol = industrial_sensors[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a sensor is in the park zone, then its average humidity is between 49.9 and 64.2 percent."""
    park_sensors = df[df["zone"] == "park"]
    condition = park_sensors["avg_humidity"].between(49.9, 64.2, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park zone sensors have avg humidity between 49.9 and 64.2%."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a sensor is in the downtown zone, then its average humidity is between 61.6 and 65.1 percent."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["avg_humidity"].between(61.6, 65.1, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown_sensors)} downtown zone sensors have avg humidity between 61.6 and 65.1%."
    else:
        viol = downtown_sensors[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a sensor is in the residential zone, then its average humidity is between 51.0 and 67.3 percent."""
    residential_sensors = df[df["zone"] == "residential"]
    condition = residential_sensors["avg_humidity"].between(51.0, 67.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential_sensors)} residential zone sensors have avg humidity between 51.0 and 67.3%."
    else:
        viol = residential_sensors[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors in the park zone have a PM2.5 level between 9.7 and 27.8."""
    park_sensors = df[df["zone"] == "park"]
    condition = park_sensors["pm25"].between(9.7, 27.8, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park zone sensors have PM2.5 between 9.7 and 27.8."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park sensors violate the rule (PM2.5s: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All sensors in the downtown zone have a PM2.5 level between 12.6 and 27.3."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["pm25"].between(12.6, 27.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown_sensors)} downtown zone sensors have PM2.5 between 12.6 and 27.3."
    else:
        viol = downtown_sensors[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (PM2.5s: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All sensors in the residential zone have a PM2.5 level between 22.7 and 30.6."""
    residential_sensors = df[df["zone"] == "residential"]
    condition = residential_sensors["pm25"].between(22.7, 30.6, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential_sensors)} residential zone sensors have PM2.5 between 22.7 and 30.6."
    else:
        viol = residential_sensors[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (PM2.5s: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a sensor is in the park zone, then its noise level is between 41.6 and 75.4 decibels."""
    park_sensors = df[df["zone"] == "park"]
    condition = park_sensors["noise_db"].between(41.6, 75.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park zone sensors have noise level between 41.6 and 75.4 dB."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park sensors violate the rule (noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a sensor is in the downtown zone, then its noise level is between 46.6 and 55.0 decibels."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["noise_db"].between(46.6, 55.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown_sensors)} downtown zone sensors have noise level between 46.6 and 55.0 dB."
    else:
        viol = downtown_sensors[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a sensor is in the residential zone, then its noise level is between 40.2 and 69.0 decibels."""
    residential_sensors = df[df["zone"] == "residential"]
    condition = residential_sensors["noise_db"].between(40.2, 69.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential_sensors)} residential zone sensors have noise level between 40.2 and 69.0 dB."
    else:
        viol = residential_sensors[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All sensors in the park zone have foot traffic between 591 and 1416."""
    park_sensors = df[df["zone"] == "park"]
    condition = park_sensors["foot_traffic"].between(591, 1416, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park zone sensors have foot traffic between 591 and 1416."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All sensors in the downtown zone have foot traffic between 474 and 1435."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["foot_traffic"].between(474, 1435, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown_sensors)} downtown zone sensors have foot traffic between 474 and 1435."
    else:
        viol = downtown_sensors[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All sensors in the residential zone have foot traffic between 580 and 658."""
    residential_sensors = df[df["zone"] == "residential"]
    condition = residential_sensors["foot_traffic"].between(580, 658, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential_sensors)} residential zone sensors have foot traffic between 580 and 658."
    else:
        viol = residential_sensors[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a sensor is in the park zone, then its power usage is between 210.8 and 439.7 kilowatt-hours."""
    park_sensors = df[df["zone"] == "park"]
    condition = park_sensors["power_use_kwh"].between(210.8, 439.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park zone sensors have power usage between 210.8 and 439.7 kWh."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park sensors violate the rule (power usage: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a sensor is in the downtown zone, then its power usage is between 127.4 and 362.6 kilowatt-hours."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["power_use_kwh"].between(127.4, 362.6, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown_sensors)} downtown zone sensors have power usage between 127.4 and 362.6 kWh."
    else:
        viol = downtown_sensors[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (power usage: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. If a sensor is in the residential zone, then its power usage is between 116.5 and 366.0 kilowatt-hours."""
    residential_sensors = df[df["zone"] == "residential"]
    condition = residential_sensors["power_use_kwh"].between(116.5, 366.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential_sensors)} residential zone sensors have power usage between 116.5 and 366.0 kWh."
    else:
        viol = residential_sensors[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (power usage: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. Most sensors in the park zone have an average temperature greater than 22 degrees Celsius."""
    park_sensors = df[df["zone"] == "park"]
    condition = park_sensors["avg_temp_c"] > 22
    count_above = condition.sum()
    total = len(park_sensors)
    truth = count_above > total / 2
    if truth:
        expl = f"{count_above} out of {total} park sensors have temp > 22°C (more than half)."
    else:
        expl = f"{count_above} out of {total} park sensors have temp > 22°C (not more than half)."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. Most sensors in the downtown zone have an average temperature less than 22 degrees Celsius."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["avg_temp_c"] < 22
    count_below = condition.sum()
    total = len(downtown_sensors)
    truth = count_below > total / 2
    if truth:
        expl = f"{count_below} out of {total} downtown sensors have temp < 22°C (more than half)."
    else:
        expl = f"{count_below} out of {total} downtown sensors have temp < 22°C (not more than half)."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. Most sensors in the residential zone have an average temperature greater than 25 degrees Celsius."""
    residential_sensors = df[df["zone"] == "residential"]
    condition = residential_sensors["avg_temp_c"] > 25
    count_above = condition.sum()
    total = len(residential_sensors)
    truth = count_above > total / 2
    if truth:
        expl = f"{count_above} out of {total} residential sensors have temp > 25°C (more than half)."
    else:
        expl = f"{count_above} out of {total} residential sensors have temp > 25°C (not more than half)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_77.csv")

    # Convert likely numeric columns safely.
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            pass

    checks = [
        (1, stmt_1),
        (2, stmt_2),
        (3, stmt_3),
        (4, stmt_4),
        (5, stmt_5),
        (6, stmt_6),
        (7, stmt_7),
        (8, stmt_8),
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
        (18, stmt_18),
        (19, stmt_19),
        (20, stmt_20),
        (21, stmt_21),
        (22, stmt_22)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()