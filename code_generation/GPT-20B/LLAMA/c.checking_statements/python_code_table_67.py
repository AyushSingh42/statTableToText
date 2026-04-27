import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the industrial zone have an average temperature greater than 20 degrees Celsius."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_temp_c"] > 20
    truth = condition.all() if not industrial.empty else True
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg_temp > 20."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (avg_temp: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a sensor is in the park zone, then its average humidity is greater than 60%."""
    park = df[df["zone"] == "park"]
    antecedent = park
    if antecedent.empty:
        return True, "No park sensors to evaluate."
    condition = antecedent["avg_humidity"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(antecedent)} park sensors have avg_humidity > 60%."
    else:
        viol = antecedent[~condition]
        expl = f"{len(viol)} park sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one sensor in the residential zone with a PM2.5 level greater than 30."""
    residential = df[df["zone"] == "residential"]
    condition = residential["pm25"] > 30
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"Found {count} residential sensor(s) with pm25 > 30."
    else:
        expl = "No residential sensor has pm25 > 30."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All sensors in the downtown zone have a noise level greater than 45 decibels."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["noise_db"] > 45
    truth = condition.all() if not downtown.empty else True
    if truth:
        expl = f"All {len(downtown)} downtown sensors have noise_db > 45."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (noise_db: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a sensor has a foot traffic greater than 1000, then its power use is greater than 200 kWh."""
    antecedent = df[df["foot_traffic"] > 1000]
    if antecedent.empty:
        return True, "No sensors with foot_traffic > 1000."
    condition = antecedent["power_use_kwh"] > 200
    truth = condition.all()
    if truth:
        expl = f"All {len(antecedent)} sensors with foot_traffic > 1000 have power_use > 200 kWh."
    else:
        viol = antecedent[~condition]
        expl = f"{len(viol)} sensors with foot_traffic > 1000 violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most sensors in the industrial zone have a power use greater than 250 kWh."""
    industrial = df[df["zone"] == "industrial"]
    count = len(industrial)
    if count == 0:
        return False, "No industrial sensors to evaluate."
    majority = (industrial["power_use_kwh"] > 250).sum()
    proportion = majority / count
    truth = proportion > 0.5
    if truth:
        expl = f"{int(proportion*100)}% of {count} industrial sensors have power_use > 250 kWh."
    else:
        expl = f"{int(proportion*100)}% of {count} industrial sensors have power_use > 250 kWh, which is not a majority."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All sensors with an average temperature less than 23 degrees Celsius have a foot traffic less than 800."""
    antecedent = df[df["avg_temp_c"] < 23]
    if antecedent.empty:
        return True, "No sensors with avg_temp_c < 23."
    condition = antecedent["foot_traffic"] < 800
    truth = condition.all()
    if truth:
        expl = f"All {len(antecedent)} sensors with avg_temp_c < 23 have foot_traffic < 800."
    else:
        viol = antecedent[~condition]
        expl = f"{len(viol)} sensors with avg_temp_c < 23 violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a sensor is in the residential zone, then its average humidity is less than 65%."""
    residential = df[df["zone"] == "residential"]
    antecedent = residential
    if antecedent.empty:
        return True, "No residential sensors to evaluate."
    condition = antecedent["avg_humidity"] < 65
    truth = condition.all()
    if truth:
        expl = f"All {len(antecedent)} residential sensors have avg_humidity < 65%."
    else:
        viol = antecedent[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one sensor in the downtown zone with a PM2.5 level less than 15."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["pm25"] < 15
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"Found {count} downtown sensor(s) with pm25 < 15."
    else:
        expl = "No downtown sensor has pm25 < 15."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All sensors with a noise level greater than 60 decibels have an average temperature greater than 22 degrees Celsius."""
    antecedent = df[df["noise_db"] > 60]
    if antecedent.empty:
        return True, "No sensors with noise_db > 60."
    condition = antecedent["avg_temp_c"] > 22
    truth = condition.all()
    if truth:
        expl = f"All {len(antecedent)} sensors with noise_db > 60 have avg_temp_c > 22."
    else:
        viol = antecedent[~condition]
        expl = f"{len(viol)} sensors with noise_db > 60 violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a sensor has a foot traffic greater than 1200, then its power use is greater than 350 kWh."""
    antecedent = df[df["foot_traffic"] > 1200]
    if antecedent.empty:
        return True, "No sensors with foot_traffic > 1200."
    condition = antecedent["power_use_kwh"] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(antecedent)} sensors with foot_traffic > 1200 have power_use > 350 kWh."
    else:
        viol = antecedent[~condition]
        expl = f"{len(viol)} sensors with foot_traffic > 1200 violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most sensors in the downtown zone have a foot traffic greater than 700."""
    downtown = df[df["zone"] == "downtown"]
    count = len(downtown)
    if count == 0:
        return False, "No downtown sensors to evaluate."
    majority = (downtown["foot_traffic"] > 700).sum()
    proportion = majority / count
    truth = proportion > 0.5
    if truth:
        expl = f"{int(proportion*100)}% of {count} downtown sensors have foot_traffic > 700."
    else:
        expl = f"{int(proportion*100)}% of {count} downtown sensors have foot_traffic > 700, which is not a majority."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All sensors with an average humidity greater than 65% have a power use greater than 300 kWh."""
    antecedent = df[df["avg_humidity"] > 65]
    if antecedent.empty:
        return True, "No sensors with avg_humidity > 65."
    condition = antecedent["power_use_kwh"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(antecedent)} sensors with avg_humidity > 65 have power_use > 300 kWh."
    else:
        viol = antecedent[~condition]
        expl = f"{len(viol)} sensors with avg_humidity > 65 violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a sensor is in the park zone, then its noise level is less than 75 decibels."""
    park = df[df["zone"] == "park"]
    antecedent = park
    if antecedent.empty:
        return True, "No park sensors to evaluate."
    condition = antecedent["noise_db"] < 75
    truth = condition.all()
    if truth:
        expl = f"All {len(antecedent)} park sensors have noise_db < 75."
    else:
        viol = antecedent[~condition]
        expl = f"{len(viol)} park sensors violate the rule (noise_db: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one sensor in the industrial zone with a PM2.5 level greater than 35."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["pm25"] > 35
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"Found {count} industrial sensor(s) with pm25 > 35."
    else:
        expl = "No industrial sensor has pm25 > 35."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All sensors with a power use less than 200 kWh have an average temperature less than 25 degrees Celsius."""
    antecedent = df[df["power_use_kwh"] < 200]
    if antecedent.empty:
        return True, "No sensors with power_use_kwh < 200."
    condition = antecedent["avg_temp_c"] < 25
    truth = condition.all()
    if truth:
        expl = f"All {len(antecedent)} sensors with power_use_kwh < 200 have avg_temp_c < 25."
    else:
        viol = antecedent[~condition]
        expl = f"{len(viol)} sensors with power_use_kwh < 200 violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a sensor has a foot traffic less than 600, then its power use is less than 300 kWh."""
    antecedent = df[df["foot_traffic"] < 600]
    if antecedent.empty:
        return True, "No sensors with foot_traffic < 600."
    condition = antecedent["power_use_kwh"] < 300
    truth = condition.all()
    if truth:
        expl = f"All {len(antecedent)} sensors with foot_traffic < 600 have power_use_kwh < 300."
    else:
        viol = antecedent[~condition]
        expl = f"{len(viol)} sensors with foot_traffic < 600 violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_67.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()