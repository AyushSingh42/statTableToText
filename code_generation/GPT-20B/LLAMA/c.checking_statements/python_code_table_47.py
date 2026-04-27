import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the industrial zone have an average temperature between 22.4 and 27.7 degrees Celsius."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_temp_c"].between(22.4, 27.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg_temp_c in [22.4, 27.7]."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all sensors in the park zone, the average humidity is between 58.8 and 67.3 percent."""
    park = df[df["zone"] == "park"]
    condition = park["avg_humidity"].between(58.8, 67.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg_humidity in [58.8, 67.3]."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the downtown zone, then its foot traffic is greater than 1000."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["foot_traffic"] > 1000
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot_traffic > 1000."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All sensors in the residential zone have a power use less than or equal to 384.1 kWh."""
    residential = df[df["zone"] == "residential"]
    condition = residential["power_use_kwh"] <= 384.1
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have power_use_kwh <= 384.1."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. There exists at least one sensor in the park zone with a noise level greater than 70 dB."""
    exists = not df[(df["zone"] == "park") & (df["noise_db"] > 70)].empty
    truth = exists
    if truth:
        count = df[(df["zone"] == "park") & (df["noise_db"] > 70)].shape[0]
        expl = f"Found {count} park sensor(s) with noise_db > 70 dB."
    else:
        expl = "No park sensor has noise_db > 70 dB."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all sensors with an average temperature greater than 25 degrees Celsius, the average humidity is less than 65 percent."""
    temp_gt_25 = df[df["avg_temp_c"] > 25]
    condition = temp_gt_25["avg_humidity"] < 65
    truth = condition.all()
    if truth:
        expl = f"All {len(temp_gt_25)} sensors with avg_temp_c > 25 have avg_humidity < 65."
    else:
        viol = temp_gt_25[~condition]
        expl = f"{len(viol)} sensors with avg_temp_c > 25 violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a sensor is in the industrial zone, then its PM2.5 level is greater than 15."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["pm25"] > 15
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have pm25 > 15."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (pm25: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most sensors in the park zone have an average step count greater than 700."""
    if "step_count" not in df.columns:
        truth = False
        expl = "Column'step_count' not found in dataset."
    else:
        park = df[df["zone"] == "park"]
        condition = park["step_count"] > 700
        proportion = condition.mean()
        truth = proportion > 0.5
        if truth:
            expl = f"{proportion*100:.1f}% of {len(park)} park sensors have step_count > 700."
        else:
            expl = f"{proportion*100:.1f}% of {len(park)} park sensors have step_count > 700, which is not a majority."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All sensors with a foot traffic greater than 1000 have a power use less than or equal to 396.4 kWh."""
    ft_gt_1000 = df[df["foot_traffic"] > 1000]
    condition = ft_gt_1000["power_use_kwh"] <= 396.4
    truth = condition.all()
    if truth:
        expl = f"All {len(ft_gt_1000)} sensors with foot_traffic > 1000 have power_use_kwh <= 396.4."
    else:
        viol = ft_gt_1000[~condition]
        expl = f"{len(viol)} sensors with foot_traffic > 1000 violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a sensor is in the residential zone, then its average temperature is between 21 and 28 degrees Celsius."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_temp_c"].between(21, 28, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have avg_temp_c in [21, 28]."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. There exists at least one sensor in the industrial zone with a noise level less than 60 dB."""
    exists = not df[(df["zone"] == "industrial") & (df["noise_db"] < 60)].empty
    truth = exists
    if truth:
        count = df[(df["zone"] == "industrial") & (df["noise_db"] < 60)].shape[0]
        expl = f"Found {count} industrial sensor(s) with noise_db < 60 dB."
    else:
        expl = "No industrial sensor has noise_db < 60 dB."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all sensors with an average humidity greater than 60 percent, the average temperature is less than 28 degrees Celsius."""
    hum_gt_60 = df[df["avg_humidity"] > 60]
    condition = hum_gt_60["avg_temp_c"] < 28
    truth = condition.all()
    if truth:
        expl = f"All {len(hum_gt_60)} sensors with avg_humidity > 60 have avg_temp_c < 28."
    else:
        viol = hum_gt_60[~condition]
        expl = f"{len(viol)} sensors with avg_humidity > 60 violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All sensors in the downtown zone have a foot traffic greater than 1000."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["foot_traffic"] > 1000
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot_traffic > 1000."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a sensor is in the park zone, then its PM2.5 level is less than 35."""
    park = df[df["zone"] == "park"]
    condition = park["pm25"] < 35
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have pm25 < 35."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (pm25: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most sensors in the industrial zone have a power use greater than 200 kWh."""
    industrial = df[df["zone"] == "industrial"]
    if industrial.empty:
        truth = False
        expl = "No industrial sensors in dataset."
    else:
        condition = industrial["power_use_kwh"] > 200
        proportion = condition.mean()
        truth = proportion > 0.5
        if truth:
            expl = f"{proportion*100:.1f}% of {len(industrial)} industrial sensors have power_use_kwh > 200."
        else:
            expl = f"{proportion*100:.1f}% of {len(industrial)} industrial sensors have power_use_kwh > 200, which is not a majority."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All sensors with a power use greater than 300 kWh have an average temperature greater than 24 degrees Celsius."""
    power_gt_300 = df[df["power_use_kwh"] > 300]
    condition = power_gt_300["avg_temp_c"] > 24
    truth = condition.all()
    if truth:
        expl = f"All {len(power_gt_300)} sensors with power_use_kwh > 300 have avg_temp_c > 24."
    else:
        viol = power_gt_300[~condition]
        expl = f"{len(viol)} sensors with power_use_kwh > 300 violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a sensor is in the residential zone, then its average humidity is between 51 and 67 percent."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_humidity"].between(51, 67, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have avg_humidity in [51, 67]."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. There exists at least one sensor in the park zone with an average temperature greater than 28 degrees Celsius."""
    exists = not df[(df["zone"] == "park") & (df["avg_temp_c"] > 28)].empty
    truth = exists
    if truth:
        count = df[(df["zone"] == "park") & (df["avg_temp_c"] > 28)].shape[0]
        expl = f"Found {count} park sensor(s) with avg_temp_c > 28."
    else:
        expl = "No park sensor has avg_temp_c > 28."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. For all sensors with a foot traffic less than 500, the average humidity is greater than 60 percent."""
    ft_lt_500 = df[df["foot_traffic"] < 500]
    condition = ft_lt_500["avg_humidity"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(ft_lt_500)} sensors with foot_traffic < 500 have avg_humidity > 60."
    else:
        viol = ft_lt_500[~condition]
        expl = f"{len(viol)} sensors with foot_traffic < 500 violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. All sensors in the industrial zone have a noise level greater than 48 dB."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["noise_db"] > 48
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have noise_db > 48."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (noise_db: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. If a sensor is in the downtown zone, then its average humidity is between 59 and 60 percent."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["avg_humidity"].between(59, 60, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have avg_humidity in [59, 60]."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. Most sensors in the park zone have an average temperature between 24 and 28 degrees Celsius."""
    park = df[df["zone"] == "park"]
    if park.empty:
        truth = False
        expl = "No park sensors in dataset."
    else:
        condition = park["avg_temp_c"].between(24, 28, inclusive="both")
        proportion = condition.mean()
        truth = proportion > 0.5
        if truth:
            expl = f"{proportion*100:.1f}% of {len(park)} park sensors have avg_temp_c in [24, 28]."
        else:
            expl = f"{proportion*100:.1f}% of {len(park)} park sensors have avg_temp_c in [24, 28], which is not a majority."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_47.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col not in ["sensor_id", "zone"]:
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
        (20, stmt_20),
        (21, stmt_21),
        (22, stmt_22),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()