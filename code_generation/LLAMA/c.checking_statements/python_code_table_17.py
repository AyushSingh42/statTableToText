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
        expl = f"All {len(industrial)} industrial sensors have avg temp between 21.5 and 22.8°C."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the residential zone have an average humidity between 56.6 and 68.0%."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_humidity"].between(56.6, 68.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have avg humidity between 56.6 and 68.0%."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the park zone, then its average PM2.5 level is greater than 26.9."""
    park = df[df["zone"] == "park"]
    condition = park["pm25"] > 26.9
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have PM2.5 > 26.9."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (PM2.5 levels: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the downtown zone with a noise level less than 50.6 decibels."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["noise_db"] < 50.6
    truth = condition.any()
    if truth:
        expl = f"At least one downtown sensor has noise < 50.6 dB ({downtown[condition]['noise_db'].iloc[0]} dB)."
    else:
        expl = f"No downtown sensors have noise < 50.6 dB."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with foot traffic greater than 1000 have a power usage less than or equal to 443.1 kWh."""
    high_foot = df[df["foot_traffic"] > 1000]
    condition = high_foot["power_use_kwh"] <= 443.1
    truth = condition.all()
    if truth:
        expl = f"All {len(high_foot)} sensors with foot traffic > 1000 have power use <= 443.1 kWh."
    else:
        viol = high_foot[~condition]
        expl = f"{len(viol)} sensors with foot traffic > 1000 violate the rule (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a sensor is in the residential zone, then its average temperature is between 23.0 and 27.6 degrees Celsius."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_temp_c"].between(23.0, 27.6, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have avg temp between 23.0 and 27.6°C."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors in the park zone have an average humidity less than 64.4%."""
    park = df[df["zone"] == "park"]
    condition = park["avg_humidity"] < 64.4
    count_true = condition.sum()
    total = len(park)
    truth = count_true > total / 2
    if truth:
        expl = f"More than half of {total} park sensors (specifically {count_true}) have avg humidity < 64.4%."
    else:
        expl = f"Only {count_true}/{total} park sensors have avg humidity < 64.4%, which is not'most'."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average temperature greater than 26.0 degrees Celsius have a foot traffic less than 1204."""
    high_temp = df[df["avg_temp_c"] > 26.0]
    condition = high_temp["foot_traffic"] < 1204
    truth = condition.all()
    if truth:
        expl = f"All {len(high_temp)} sensors with avg temp > 26.0°C have foot traffic < 1204."
    else:
        viol = high_temp[~condition]
        expl = f"{len(viol)} sensors with avg temp > 26.0°C violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a sensor is in the industrial zone, then its power usage is less than or equal to 154.3 kWh."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["power_use_kwh"] <= 154.3
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have power use <= 154.3 kWh."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the downtown zone with an average PM2.5 level greater than 34.5."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["pm25"] > 34.5
    truth = condition.any()
    if truth:
        expl = f"At least one downtown sensor has PM2.5 > 34.5 ({downtown[condition]['pm25'].iloc[0]})."
    else:
        expl = f"No downtown sensors have PM2.5 > 34.5."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All sensors with a noise level greater than 68.5 decibels have an average temperature less than 27.8 degrees Celsius."""
    high_noise = df[df["noise_db"] > 68.5]
    condition = high_noise["avg_temp_c"] < 27.8
    truth = condition.all()
    if truth:
        expl = f"All {len(high_noise)} sensors with noise > 68.5 dB have avg temp < 27.8°C."
    else:
        viol = high_noise[~condition]
        expl = f"{len(viol)} sensors with noise > 68.5 dB violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a sensor is in the park zone, then its foot traffic is greater than 537."""
    park = df[df["zone"] == "park"]
    condition = park["foot_traffic"] > 537
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have foot traffic > 537."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most sensors in the residential zone have a power usage less than 443.1 kWh."""
    residential = df[df["zone"] == "residential"]
    condition = residential["power_use_kwh"] < 443.1
    count_true = condition.sum()
    total = len(residential)
    truth = count_true > total / 2
    if truth:
        expl = f"More than half of {total} residential sensors (specifically {count_true}) have power use < 443.1 kWh."
    else:
        expl = f"Only {count_true}/{total} residential sensors have power use < 443.1 kWh, which is not'most'."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All sensors with an average humidity less than 56.0% have a foot traffic greater than 630."""
    low_humid = df[df["avg_humidity"] < 56.0]
    condition = low_humid["foot_traffic"] > 630
    truth = condition.all()
    if truth:
        expl = f"All {len(low_humid)} sensors with avg humidity < 56.0% have foot traffic > 630."
    else:
        viol = low_humid[~condition]
        expl = f"{len(viol)} sensors with avg humidity < 56.0% violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a sensor is in the downtown zone, then its average temperature is between 23.9 and 25.3 degrees Celsius."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["avg_temp_c"].between(23.9, 25.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have avg temp between 23.9 and 25.3°C."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one sensor in the industrial zone with a noise level greater than 63.6 decibels."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["noise_db"] > 63.6
    truth = condition.any()
    if truth:
        expl = f"At least one industrial sensor has noise > 63.6 dB ({industrial[condition]['noise_db'].iloc[0]} dB)."
    else:
        expl = f"No industrial sensors have noise > 63.6 dB."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All sensors with a foot traffic less than 630 have an average PM2.5 level less than 20.0."""
    low_foot = df[df["foot_traffic"] < 630]
    condition = low_foot["pm25"] < 20.0
    truth = condition.all()
    if truth:
        expl = f"All {len(low_foot)} sensors with foot traffic < 630 have PM2.5 < 20.0."
    else:
        viol = low_foot[~condition]
        expl = f"{len(viol)} sensors with foot traffic < 630 violate the rule (PM2.5 levels: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a sensor is in the park zone, then its average humidity is between 50.3 and 64.4%."""
    park = df[df["zone"] == "park"]
    condition = park["avg_humidity"].between(50.3, 64.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg humidity between 50.3 and 64.4%."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. Most sensors in the downtown zone have a power usage less than 307.1 kWh."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["power_use_kwh"] < 307.1
    count_true = condition.sum()
    total = len(downtown)
    truth = count_true > total / 2
    if truth:
        expl = f"More than half of {total} downtown sensors (specifically {count_true}) have power use < 307.1 kWh."
    else:
        expl = f"Only {count_true}/{total} downtown sensors have power use < 307.1 kWh, which is not'most'."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_17.csv")

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
        (19, stmt_19)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()