import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all sensors in the park zone, average temperature is between 20.7°C and 27.5°C."""
    park_sensors = df[df["zone"] == "park"]
    condition = park_sensors["avg_temp_c"].between(20.7, 27.5, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park sensors have avg temp between 20.7°C and 27.5°C."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all residential sensors, average humidity is between 51.0% and 67.3%."""
    res_sensors = df[df["zone"] == "residential"]
    condition = res_sensors["avg_humidity"].between(51.0, 67.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(res_sensors)} residential sensors have avg humidity between 51.0% and 67.3%."
    else:
        viol = res_sensors[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all downtown sensors, foot traffic is at least 474."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["foot_traffic"] >= 474
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown_sensors)} downtown sensors have foot traffic >= 474."
    else:
        viol = downtown_sensors[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists a residential sensor (SN077007) with the highest PM2.5 value of 30.6 µg/m³ among all sensors."""
    res_sensors = df[df["zone"] == "residential"]
    max_pm25 = res_sensors["pm25"].max()
    sn077007_pm25 = df[df["sensor_id"] == "SN077007"]["pm25"].iloc[0]
    truth = sn077007_pm25 == max_pm25 and max_pm25 == 30.6
    expl = f"SN077007 has PM2.5={sn077007_pm25} which is the maximum among all sensors ({max_pm25}), and matches 30.6 µg/m³."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most sensors (8 out of 15) record noise levels above 50 dB."""
    above_50 = df[df["noise_db"] > 50]
    total = len(df)
    truth = len(above_50) >= 8
    expl = f"{len(above_50)} out of {total} sensors record noise > 50 dB."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all sensors with foot traffic exceeding 1300, power use is at least 215.0 kWh."""
    high_foot = df[df["foot_traffic"] > 1300]
    condition = high_foot["power_use_kwh"] >= 215.0
    truth = condition.all()
    if truth:
        expl = f"All {len(high_foot)} sensors with foot traffic > 1300 have power use >= 215.0 kWh."
    else:
        viol = high_foot[~condition]
        expl = f"{len(viol)} sensors with foot traffic > 1300 violate the rule (power use: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If average temperature is at least 27.0°C, then PM2.5 is at least 22.7 µg/m³."""
    filtered = df[df["avg_temp_c"] >= 27.0]
    condition = filtered["pm25"] >= 22.7
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} sensors with avg temp >= 27.0°C have PM2.5 >= 22.7 µg/m³."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} sensors with avg temp >= 27.0°C violate the rule (PM2.5: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If average humidity is 52% or lower, then noise level does not exceed 41.6 dB."""
    filtered = df[df["avg_humidity"] <= 52]
    condition = filtered["noise_db"] <= 41.6
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} sensors with avg humidity <= 52% have noise level <= 41.6 dB."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} sensors with avg humidity <= 52% violate the rule (noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()