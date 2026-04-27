import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All park zone sensors have average temperature between 20.6 °C and 28.1 °C."""
    park_sensors = df[df["zone"] == "park"]
    condition = park_sensors["avg_temp_c"].between(20.6, 28.1, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park zone sensors have avg temp between 20.6°C and 28.1°C."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park sensors violate the range (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All industrial zone sensors have average humidity between 53.6 % and 67.3 %."""
    industrial_sensors = df[df["zone"] == "industrial"]
    condition = industrial_sensors["avg_humidity"].between(53.6, 67.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial_sensors)} industrial zone sensors have avg humidity between 53.6% and 67.3%."
    else:
        viol = industrial_sensors[~condition]
        expl = f"{len(viol)} industrial sensors violate the range (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All residential zone sensors have power usage of at least 200.8 kWh."""
    residential_sensors = df[df["zone"] == "residential"]
    condition = residential_sensors["power_use_kwh"] >= 200.8
    truth = condition.all()
    if truth:
        expl = f"All {len(residential_sensors)} residential zone sensors have power use >= 200.8 kWh."
    else:
        viol = residential_sensors[~condition]
        expl = f"{len(viol)} residential sensors violate the minimum (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All sensors with noise level of at least 70 dB are located in the park zone."""
    high_noise_sensors = df[df["noise_db"] >= 70]
    condition = high_noise_sensors["zone"] == "park"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_noise_sensors)} sensors with noise >= 70 dB are in park zone."
    else:
        viol = high_noise_sensors[~condition]
        expl = f"{len(viol)} sensors with noise >= 70 dB are not in park zone (zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with PM2.5 concentration below 10 µg/m³ are in the park zone."""
    low_pm25_sensors = df[df["pm25"] < 10]
    condition = low_pm25_sensors["zone"] == "park"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_pm25_sensors)} sensors with PM2.5 < 10 µg/m³ are in park zone."
    else:
        viol = low_pm25_sensors[~condition]
        expl = f"{len(viol)} sensors with PM2.5 < 10 µg/m³ are not in park zone (zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most sensors (12 out of 15) have foot traffic exceeding 600 per day."""
    total_sensors = len(df)
    high_foot_traffic = df[df["foot_traffic"] > 600]
    count = len(high_foot_traffic)
    truth = count >= 12
    if truth:
        expl = f"{count} out of {total_sensors} sensors have foot traffic > 600/day (≥12)."
    else:
        expl = f"{count} out of {total_sensors} sensors have foot traffic > 600/day (<12)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All residential sensors have average temperature no higher than 27.5 °C."""
    residential_sensors = df[df["zone"] == "residential"]
    condition = residential_sensors["avg_temp_c"] <= 27.5
    truth = condition.all()
    if truth:
        expl = f"All {len(residential_sensors)} residential sensors have avg temp ≤ 27.5°C."
    else:
        viol = residential_sensors[~condition]
        expl = f"{len(viol)} residential sensors exceed 27.5°C (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All industrial sensors have noise levels no greater than 64.6 dB."""
    industrial_sensors = df[df["zone"] == "industrial"]
    condition = industrial_sensors["noise_db"] <= 64.6
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial_sensors)} industrial sensors have noise ≤ 64.6 dB."
    else:
        viol = industrial_sensors[~condition]
        expl = f"{len(viol)} industrial sensors exceed 64.6 dB (noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_47.csv")

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