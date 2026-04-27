import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the downtown zone have an average temperature greater than 21°C."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["avg_temp_c"] > 21
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have avg_temp > 21°C."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (avg_temp: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the industrial zone have an average humidity greater than 65%."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_humidity"] > 65
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg_humidity > 65%."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the residential zone, then its average noise level is greater than 64 dB."""
    residential = df[df["zone"] == "residential"]
    if residential.empty:
        return True, "No residential sensors, rule vacuously satisfied."
    condition = residential["noise_db"] > 64
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have noise > 64 dB."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (noise_db: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the park zone with an average PM2.5 level less than 20."""
    park = df[df["zone"] == "park"]
    condition = park["pm25"] < 20
    truth = condition.any()
    if truth:
        expl = f"At least one park sensor has pm25 < 20 (found {park[condition]['sensor_id'].iloc[0]})."
    else:
        expl = "No park sensor has pm25 < 20."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with an average temperature less than 24°C have a foot traffic greater than 1000."""
    temp_lt_24 = df[df["avg_temp_c"] < 24]
    if temp_lt_24.empty:
        return True, "No sensors with avg_temp < 24°C, rule vacuously satisfied."
    condition = temp_lt_24["foot_traffic"] > 1000
    truth = condition.all()
    if truth:
        expl = f"All {len(temp_lt_24)} sensors with avg_temp < 24°C have foot_traffic > 1000."
    else:
        viol = temp_lt_24[~condition]
        expl = f"{len(viol)} sensors with avg_temp < 24°C violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a sensor's average humidity is greater than 60%, then its power use is greater than 200 kWh."""
    hum_gt_60 = df[df["avg_humidity"] > 60]
    if hum_gt_60.empty:
        return True, "No sensors with avg_humidity > 60%, rule vacuously satisfied."
    condition = hum_gt_60["power_use_kwh"] > 200
    truth = condition.all()
    if truth:
        expl = f"All {len(hum_gt_60)} sensors with avg_humidity > 60% have power_use > 200 kWh."
    else:
        viol = hum_gt_60[~condition]
        expl = f"{len(viol)} sensors with avg_humidity > 60% violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors in the downtown zone have an average noise level less than 50 dB."""
    downtown = df[df["zone"] == "downtown"]
    if downtown.empty:
        return True, "No downtown sensors, rule vacuously satisfied."
    condition = downtown["noise_db"] < 50
    count_true = condition.sum()
    total = len(downtown)
    truth = count_true > total / 2
    if truth:
        expl = f"{count_true} of {total} downtown sensors have noise < 50 dB (majority)."
    else:
        expl = f"Only {count_true} of {total} downtown sensors have noise < 50 dB (not majority)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average PM2.5 level greater than 30 have a foot traffic less than 700."""
    pm_gt_30 = df[df["pm25"] > 30]
    if pm_gt_30.empty:
        return True, "No sensors with pm25 > 30, rule vacuously satisfied."
    condition = pm_gt_30["foot_traffic"] < 700
    truth = condition.all()
    if truth:
        expl = f"All {len(pm_gt_30)} sensors with pm25 > 30 have foot_traffic < 700."
    else:
        viol = pm_gt_30[~condition]
        expl = f"{len(viol)} sensors with pm25 > 30 violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a sensor is in the park zone, then its average temperature is less than 28°C."""
    park = df[df["zone"] == "park"]
    if park.empty:
        return True, "No park sensors, rule vacuously satisfied."
    condition = park["avg_temp_c"] < 28
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg_temp < 28°C."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (avg_temp: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the residential zone with an average noise level greater than 67 dB."""
    residential = df[df["zone"] == "residential"]
    condition = residential["noise_db"] > 67
    truth = condition.any()
    if truth:
        expl = f"At least one residential sensor has noise > 67 dB (found {residential[condition]['sensor_id'].iloc[0]})."
    else:
        expl = "No residential sensor has noise > 67 dB."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All sensors with a foot traffic greater than 1200 have an average humidity greater than 50%."""
    ft_gt_1200 = df[df["foot_traffic"] > 1200]
    if ft_gt_1200.empty:
        return True, "No sensors with foot_traffic > 1200, rule vacuously satisfied."
    condition = ft_gt_1200["avg_humidity"] > 50
    truth = condition.all()
    if truth:
        expl = f"All {len(ft_gt_1200)} sensors with foot_traffic > 1200 have avg_humidity > 50%."
    else:
        viol = ft_gt_1200[~condition]
        expl = f"{len(viol)} sensors with foot_traffic > 1200 violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a sensor's power use is less than 250 kWh, then its average temperature is greater than 22°C."""
    power_lt_250 = df[df["power_use_kwh"] < 250]
    if power_lt_250.empty:
        return True, "No sensors with power_use < 250 kWh, rule vacuously satisfied."
    condition = power_lt_250["avg_temp_c"] > 22
    truth = condition.all()
    if truth:
        expl = f"All {len(power_lt_250)} sensors with power_use < 250 kWh have avg_temp > 22°C."
    else:
        viol = power_lt_250[~condition]
        expl = f"{len(viol)} sensors with power_use < 250 kWh violate the rule (avg_temp: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most sensors in the industrial zone have an average PM2.5 level less than 25."""
    industrial = df[df["zone"] == "industrial"]
    if industrial.empty:
        return True, "No industrial sensors, rule vacuously satisfied."
    condition = industrial["pm25"] < 25
    count_true = condition.sum()
    total = len(industrial)
    truth = count_true > total / 2
    if truth:
        expl = f"{count_true} of {total} industrial sensors have pm25 < 25 (majority)."
    else:
        expl = f"Only {count_true} of {total} industrial sensors have pm25 < 25 (not majority)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All sensors with an average noise level greater than 70 dB have a foot traffic less than 1300."""
    noise_gt_70 = df[df["noise_db"] > 70]
    if noise_gt_70.empty:
        return True, "No sensors with noise_db > 70, rule vacuously satisfied."
    condition = noise_gt_70["foot_traffic"] < 1300
    truth = condition.all()
    if truth:
        expl = f"All {len(noise_gt_70)} sensors with noise_db > 70 have foot_traffic < 1300."
    else:
        viol = noise_gt_70[~condition]
        expl = f"{len(viol)} sensors with noise_db > 70 violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a sensor is in the downtown zone, then its average humidity is greater than 55%."""
    downtown = df[df["zone"] == "downtown"]
    if downtown.empty:
        return True, "No downtown sensors, rule vacuously satisfied."
    condition = downtown["avg_humidity"] > 55
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have avg_humidity > 55%."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one sensor in the park zone with an average temperature less than 22°C."""
    park = df[df["zone"] == "park"]
    condition = park["avg_temp_c"] < 22
    truth = condition.any()
    if truth:
        expl = f"At least one park sensor has avg_temp < 22°C (found {park[condition]['sensor_id'].iloc[0]})."
    else:
        expl = "No park sensor has avg_temp < 22°C."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All sensors with an average humidity less than 55% have a foot traffic greater than 600."""
    hum_lt_55 = df[df["avg_humidity"] < 55]
    if hum_lt_55.empty:
        return True, "No sensors with avg_humidity < 55%, rule vacuously satisfied."
    condition = hum_lt_55["foot_traffic"] > 600
    truth = condition.all()
    if truth:
        expl = f"All {len(hum_lt_55)} sensors with avg_humidity < 55% have foot_traffic > 600."
    else:
        viol = hum_lt_55[~condition]
        expl = f"{len(viol)} sensors with avg_humidity < 55% violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a sensor's average PM2.5 level is less than 20, then its power use is greater than 300 kWh."""
    pm_lt_20 = df[df["pm25"] < 20]
    if pm_lt_20.empty:
        return True, "No sensors with pm25 < 20, rule vacuously satisfied."
    condition = pm_lt_20["power_use_kwh"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(pm_lt_20)} sensors with pm25 < 20 have power_use > 300 kWh."
    else:
        viol = pm_lt_20[~condition]
        expl = f"{len(viol)} sensors with pm25 < 20 violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_97.csv")

    # Convert numeric columns safely.
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()