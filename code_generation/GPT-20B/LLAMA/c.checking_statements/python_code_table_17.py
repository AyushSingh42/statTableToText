import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the industrial zone have an average temperature between 21.5 and 22.8 degrees Celsius."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_temp_c"].between(21.5, 22.8, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg_temp_c between 21.5 and 22.8."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the residential zone have an average humidity between 56.6 and 68.0%."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_humidity"].between(56.6, 68.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have avg_humidity between 56.6 and 68.0%."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the park zone, then its average PM2.5 level is greater than 26.9."""
    park = df[df["zone"] == "park"]
    condition = park["pm25"] > 26.9
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have pm25 > 26.9."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (pm25: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the downtown zone with a noise level less than 50.6 decibels."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["noise_db"] < 50.6
    truth = condition.any()
    if truth:
        found = downtown[condition]
        expl = f"Found {len(found)} downtown sensor(s) with noise_db < 50.6 (IDs: {', '.join(found['sensor_id'].tolist())})."
    else:
        expl = "No downtown sensor has noise_db < 50.6."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with foot traffic greater than 1000 have a power usage less than or equal to 443.1 kWh."""
    subset = df[df["foot_traffic"] > 1000]
    condition = subset["power_use_kwh"] <= 443.1
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} sensors with foot_traffic > 1000 have power_use_kwh <= 443.1."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} sensors violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a sensor is in the residential zone, then its average temperature is between 23.0 and 27.6 degrees Celsius."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_temp_c"].between(23.0, 27.6, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have avg_temp_c between 23.0 and 27.6."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors in the park zone have an average humidity less than 64.4%."""
    park = df[df["zone"] == "park"]
    if len(park) == 0:
        truth = True
        expl = "No park sensors present; condition vacuously satisfied."
    else:
        condition = park["avg_humidity"] < 64.4
        count_true = condition.sum()
        truth = count_true > len(park) / 2
        percent = count_true / len(park) * 100
        if truth:
            expl = f"{count_true} out of {len(park)} park sensors have avg_humidity < 64.4% ({percent:.1f}%)."
        else:
            expl = f"Only {count_true} out of {len(park)} park sensors have avg_humidity < 64.4% ({percent:.1f}%)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average temperature greater than 26.0 degrees Celsius have a foot traffic less than 1204."""
    subset = df[df["avg_temp_c"] > 26.0]
    condition = subset["foot_traffic"] < 1204
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} sensors with avg_temp_c > 26.0 have foot_traffic < 1204."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a sensor is in the industrial zone, then its power usage is less than or equal to 154.3 kWh."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["power_use_kwh"] <= 154.3
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have power_use_kwh <= 154.3."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the downtown zone with an average PM2.5 level greater than 34.5."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["pm25"] > 34.5
    truth = condition.any()
    if truth:
        found = downtown[condition]
        expl = f"Found {len(found)} downtown sensor(s) with pm25 > 34.5 (IDs: {', '.join(found['sensor_id'].tolist())})."
    else:
        expl = "No downtown sensor has pm25 > 34.5."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All sensors with a noise level greater than 68.5 decibels have an average temperature less than 27.8 degrees Celsius."""
    subset = df[df["noise_db"] > 68.5]
    condition = subset["avg_temp_c"] < 27.8
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} sensors with noise_db > 68.5 have avg_temp_c < 27.8."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a sensor is in the park zone, then its foot traffic is greater than 537."""
    park = df[df["zone"] == "park"]
    condition = park["foot_traffic"] > 537
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have foot_traffic > 537."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most sensors in the residential zone have a power usage less than 443.1 kWh."""
    residential = df[df["zone"] == "residential"]
    if len(residential) == 0:
        truth = True
        expl = "No residential sensors present; condition vacuously satisfied."
    else:
        condition = residential["power_use_kwh"] < 443.1
        count_true = condition.sum()
        truth = count_true > len(residential) / 2
        percent = count_true / len(residential) * 100
        if truth:
            expl = f"{count_true} out of {len(residential)} residential sensors have power_use_kwh < 443.1 ({percent:.1f}%)."
        else:
            expl = f"Only {count_true} out of {len(residential)} residential sensors have power_use_kwh < 443.1 ({percent:.1f}%)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All sensors with an average humidity less than 56.0% have a foot traffic greater than 630."""
    subset = df[df["avg_humidity"] < 56.0]
    condition = subset["foot_traffic"] > 630
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} sensors with avg_humidity < 56.0 have foot_traffic > 630."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a sensor is in the downtown zone, then its average temperature is between 23.9 and 25.3 degrees Celsius."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["avg_temp_c"].between(23.9, 25.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have avg_temp_c between 23.9 and 25.3."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one sensor in the industrial zone with a noise level greater than 63.6 decibels."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["noise_db"] > 63.6
    truth = condition.any()
    if truth:
        found = industrial[condition]
        expl = f"Found {len(found)} industrial sensor(s) with noise_db > 63.6 (IDs: {', '.join(found['sensor_id'].tolist())})."
    else:
        expl = "No industrial sensor has noise_db > 63.6."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All sensors with a foot traffic less than 630 have an average PM2.5 level less than 20.0."""
    subset = df[df["foot_traffic"] < 630]
    condition = subset["pm25"] < 20.0
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} sensors with foot_traffic < 630 have pm25 < 20.0."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} sensors violate the rule (pm25: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a sensor is in the park zone, then its average humidity is between 50.3 and 64.4%."""
    park = df[df["zone"] == "park"]
    condition = park["avg_humidity"].between(50.3, 64.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg_humidity between 50.3 and 64.4%."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. Most sensors in the downtown zone have a power usage less than 307.1 kWh."""
    downtown = df[df["zone"] == "downtown"]
    if len(downtown) == 0:
        truth = True
        expl = "No downtown sensors present; condition vacuously satisfied."
    else:
        condition = downtown["power_use_kwh"] < 307.1
        count_true = condition.sum()
        truth = count_true > len(downtown) / 2
        percent = count_true / len(downtown) * 100
        if truth:
            expl = f"{count_true} out of {len(downtown)} downtown sensors have power_use_kwh < 307.1 ({percent:.1f}%)."
        else:
            expl = f"Only {count_true} out of {len(downtown)} downtown sensors have power_use_kwh < 307.1 ({percent:.1f}%)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_17.csv")

    # Convert numeric columns
    numeric_cols = ["avg_temp_c", "avg_humidity", "pm25", "noise_db", "foot_traffic", "power_use_kwh"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()