import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All park zone sensors have average temperature between 20.6 °C and 28.1 °C."""
    park = df[df["zone"] == "park"]
    condition = park["avg_temp_c"].between(20.6, 28.1, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg_temp_c between 20.6 and 28.1."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All industrial zone sensors have average humidity between 53.6 % and 67.3 %."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_humidity"].between(53.6, 67.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg_humidity between 53.6 and 67.3."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All residential zone sensors have power usage of at least 200.8 kWh."""
    residential = df[df["zone"] == "residential"]
    condition = residential["power_use_kwh"] >= 200.8
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have power_use_kwh >= 200.8."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All sensors with noise level of at least 70 dB are located in the park zone."""
    noisy = df[df["noise_db"] >= 70]
    condition = noisy["zone"] == "park"
    truth = condition.all()
    if truth:
        expl = f"All {len(noisy)} sensors with noise_db >= 70 are in the park zone."
    else:
        viol = noisy[~condition]
        expl = f"{len(viol)} sensors with noise_db >= 70 are not in the park zone (zones: {', '.join(viol['zone'].unique())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with PM2.5 concentration below 10 µg/m³ are in the park zone."""
    low_pm = df[df["pm25"] < 10]
    condition = low_pm["zone"] == "park"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_pm)} sensors with pm25 < 10 are in the park zone."
    else:
        viol = low_pm[~condition]
        expl = f"{len(viol)} sensors with pm25 < 10 are not in the park zone (zones: {', '.join(viol['zone'].unique())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most sensors (12 out of 15) have foot traffic exceeding 600 per day."""
    count = (df["foot_traffic"] > 600).sum()
    truth = count >= 12
    if truth:
        expl = f"{count} out of {len(df)} sensors have foot_traffic > 600."
    else:
        expl = f"Only {count} sensors have foot_traffic > 600, which is less than 12."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All residential sensors have average temperature no higher than 27.5 °C."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_temp_c"] <= 27.5
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have avg_temp_c <= 27.5."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All industrial sensors have noise levels no greater than 64.6 dB."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["noise_db"] <= 64.6
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have noise_db <= 64.6."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (noise_db: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_47.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()