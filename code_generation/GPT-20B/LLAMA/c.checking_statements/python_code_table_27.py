import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the park zone have an average temperature between 21.6 and 24.2 degrees Celsius."""
    park = df[df["zone"] == "park"]
    if park.empty:
        return True, "No park sensors to evaluate."
    condition = park["avg_temp_c"].between(21.6, 24.2, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(park)} park sensors have avg_temp_c in [21.6, 24.2]."
    viol = park[~condition]
    return False, f"{len(viol)} park sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c']))})."

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the residential zone have an average humidity between 52.9 and 67.3 percent."""
    res = df[df["zone"] == "residential"]
    if res.empty:
        return True, "No residential sensors to evaluate."
    condition = res["avg_humidity"].between(52.9, 67.3, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(res)} residential sensors have avg_humidity in [52.9, 67.3]."
    viol = res[~condition]
    return False, f"{len(viol)} residential sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity']))})."

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the industrial zone, then its average noise level is between 47.7 and 59.9 decibels."""
    ind = df[df["zone"] == "industrial"]
    if ind.empty:
        return True, "No industrial sensors to evaluate."
    condition = ind["noise_db"].between(47.7, 59.9, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(ind)} industrial sensors have noise_db in [47.7, 59.9]."
    viol = ind[~condition]
    return False, f"{len(viol)} industrial sensors violate the rule (noise_db: {', '.join(map(str, viol['noise_db']))})."

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the downtown zone with an average PM2.5 level greater than 25."""
    dow = df[df["zone"] == "downtown"]
    if dow.empty:
        return False, "No downtown sensors present."
    exists = (dow["pm25"] > 25).any()
    if exists:
        sensors = dow[dow["pm25"] > 25]
        return True, f"{len(sensors)} downtown sensor(s) have pm25 > 25 (values: {', '.join(map(str, sensors['pm25']))})."
    return False, "No downtown sensor has pm25 > 25."

def stmt_5(df: pd.DataFrame):
    """5. All sensors with an average temperature greater than 25 degrees Celsius have a power usage greater than 263.6 kWh."""
    high_temp = df[df["avg_temp_c"] > 25]
    if high_temp.empty:
        return True, "No sensors with avg_temp_c > 25 to evaluate."
    condition = high_temp["power_use_kwh"] > 263.6
    truth = condition.all()
    if truth:
        return True, f"All {len(high_temp)} sensors with avg_temp_c > 25 have power_use_kwh > 263.6."
    viol = high_temp[~condition]
    return False, f"{len(viol)} sensors violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh']))})."

def stmt_6(df: pd.DataFrame):
    """6. If a sensor is in the park zone, then its foot traffic is between 470 and 1433."""
    park = df[df["zone"] == "park"]
    if park.empty:
        return True, "No park sensors to evaluate."
    condition = park["foot_traffic"].between(470, 1433, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(park)} park sensors have foot_traffic in [470, 1433]."
    viol = park[~condition]
    return False, f"{len(viol)} park sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic']))})."

def stmt_7(df: pd.DataFrame):
    """7. Most sensors in the residential zone have an average step count greater than 872."""
    res = df[df["zone"] == "residential"]
    if res.empty:
        return False, "No residential sensors to evaluate."
    # Assume foot_traffic represents step count
    count_gt = (res["foot_traffic"] > 872).sum()
    proportion = count_gt / len(res)
    truth = proportion > 0.5
    if truth:
        return True, f"{count_gt}/{len(res)} residential sensors have foot_traffic > 872 ({proportion*100:.1f}%)."
    return False, f"{count_gt}/{len(res)} residential sensors have foot_traffic > 872 ({proportion*100:.1f}%)."

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average humidity less than 55 percent have a power usage greater than 276.1 kWh."""
    low_hum = df[df["avg_humidity"] < 55]
    if low_hum.empty:
        return True, "No sensors with avg_humidity < 55 to evaluate."
    condition = low_hum["power_use_kwh"] > 276.1
    truth = condition.all()
    if truth:
        return True, f"All {len(low_hum)} sensors with avg_humidity < 55 have power_use_kwh > 276.1."
    viol = low_hum[~condition]
    return False, f"{len(viol)} sensors violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh']))})."

def stmt_9(df: pd.DataFrame):
    """9. If a sensor is in the industrial zone, then its average temperature is between 24.1 and 27.9 degrees Celsius."""
    ind = df[df["zone"] == "industrial"]
    if ind.empty:
        return True, "No industrial sensors to evaluate."
    condition = ind["avg_temp_c"].between(24.1, 27.9, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(ind)} industrial sensors have avg_temp_c in [24.1, 27.9]."
    viol = ind[~condition]
    return False, f"{len(viol)} industrial sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c']))})."

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the downtown zone with an average noise level greater than 69 decibels."""
    dow = df[df["zone"] == "downtown"]
    if dow.empty:
        return False, "No downtown sensors present."
    exists = (dow["noise_db"] > 69).any()
    if exists:
        sensors = dow[dow["noise_db"] > 69]
        return True, f"{len(sensors)} downtown sensor(s) have noise_db > 69 (values: {', '.join(map(str, sensors['noise_db']))})."
    return False, "No downtown sensor has noise_db > 69."

def stmt_11(df: pd.DataFrame):
    """11. All sensors with an average PM2.5 level greater than 30 have a foot traffic greater than 1122."""
    high_pm = df[df["pm25"] > 30]
    if high_pm.empty:
        return True, "No sensors with pm25 > 30 to evaluate."
    condition = high_pm["foot_traffic"] > 1122
    truth = condition.all()
    if truth:
        return True, f"All {len(high_pm)} sensors with pm25 > 30 have foot_traffic > 1122."
    viol = high_pm[~condition]
    return False, f"{len(viol)} sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic']))})."

def stmt_12(df: pd.DataFrame):
    """12. If a sensor is in the park zone, then its average humidity is between 51.6 and 64.5 percent."""
    park = df[df["zone"] == "park"]
    if park.empty:
        return True, "No park sensors to evaluate."
    condition = park["avg_humidity"].between(51.6, 64.5, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(park)} park sensors have avg_humidity in [51.6, 64.5]."
    viol = park[~condition]
    return False, f"{len(viol)} park sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity']))})."

def stmt_13(df: pd.DataFrame):
    """13. All sensors with a power usage greater than 357.5 kWh have an average temperature greater than 23.8 degrees Celsius."""
    high_power = df[df["power_use_kwh"] > 357.5]
    if high_power.empty:
        return True, "No sensors with power_use_kwh > 357.5 to evaluate."
    condition = high_power["avg_temp_c"] > 23.8
    truth = condition.all()
    if truth:
        return True, f"All {len(high_power)} sensors with power_use_kwh > 357.5 have avg_temp_c > 23.8."
    viol = high_power[~condition]
    return False, f"{len(viol)} sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c']))})."

def stmt_14(df: pd.DataFrame):
    """14. Most sensors in the downtown zone have an average PM2.5 level greater than 14.3."""
    dow = df[df["zone"] == "downtown"]
    if dow.empty:
        return False, "No downtown sensors to evaluate."
    count_gt = (dow["pm25"] > 14.3).sum()
    proportion = count_gt / len(dow)
    truth = proportion > 0.5
    if truth:
        return True, f"{count_gt}/{len(dow)} downtown sensors have pm25 > 14.3 ({proportion*100:.1f}%)."
    return False, f"{count_gt}/{len(dow)} downtown sensors have pm25 > 14.3 ({proportion*100:.1f}%)."

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one sensor in the residential zone with an average noise level greater than 73.9 decibels."""
    res = df[df["zone"] == "residential"]
    if res.empty:
        return False, "No residential sensors present."
    exists = (res["noise_db"] > 73.9).any()
    if exists:
        sensors = res[res["noise_db"] > 73.9]
        return True, f"{len(sensors)} residential sensor(s) have noise_db > 73.9 (values: {', '.join(map(str, sensors['noise_db']))})."
    return False, "No residential sensor has noise_db > 73.9."

def stmt_16(df: pd.DataFrame):
    """16. All sensors with an average temperature less than 25 degrees Celsius have a power usage less than 424.4 kWh."""
    low_temp = df[df["avg_temp_c"] < 25]
    if low_temp.empty:
        return True, "No sensors with avg_temp_c < 25 to evaluate."
    condition = low_temp["power_use_kwh"] < 424.4
    truth = condition.all()
    if truth:
        return True, f"All {len(low_temp)} sensors with avg_temp_c < 25 have power_use_kwh < 424.4."
    viol = low_temp[~condition]
    return False, f"{len(viol)} sensors violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh']))})."

def stmt_17(df: pd.DataFrame):
    """17. If a sensor is in the industrial zone, then its foot traffic is between 990 and 1097."""
    ind = df[df["zone"] == "industrial"]
    if ind.empty:
        return True, "No industrial sensors to evaluate."
    condition = ind["foot_traffic"].between(990, 1097, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(ind)} industrial sensors have foot_traffic in [990, 1097]."
    viol = ind[~condition]
    return False, f"{len(viol)} industrial sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic']))})."

def stmt_18(df: pd.DataFrame):
    """18. All sensors with an average humidity greater than 64 percent have a power usage less than 357.5 kWh."""
    high_hum = df[df["avg_humidity"] > 64]
    if high_hum.empty:
        return True, "No sensors with avg_humidity > 64 to evaluate."
    condition = high_hum["power_use_kwh"] < 357.5
    truth = condition.all()
    if truth:
        return True, f"All {len(high_hum)} sensors with avg_humidity > 64 have power_use_kwh < 357.5."
    viol = high_hum[~condition]
    return False, f"{len(viol)} sensors violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh']))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_27.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col!= "sensor_id" and col!= "zone":
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()