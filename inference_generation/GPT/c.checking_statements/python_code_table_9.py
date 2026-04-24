import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All industrial sensors have an average noise level of at least 72.8 dB."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["noise_db"] >= 72.8
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors meet the noise threshold (min: {industrial['noise_db'].min():.2f} dB)."
    else:
        viol = industrial[~condition]
        ids = ", ".join(map(str, viol["sensor_id"].tolist()))
        expl = f"{len(viol)} industrial sensors violate the rule (sensor_id(s): {ids}; noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All park sensors have an average PM2.5 concentration of no more than 9.8 µg/m³."""
    park = df[df["zone"] == "park"]
    condition = park["pm25"] <= 9.8
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors meet the PM2.5 limit (max: {park['pm25'].max():.2f} µg/m³)."
    else:
        viol = park[~condition]
        ids = ", ".join(map(str, viol["sensor_id"].tolist()))
        expl = f"{len(viol)} park sensors exceed the limit (sensor_id(s): {ids}; PM2.5: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All downtown sensors record foot traffic of at least 1240 persons per day."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["foot_traffic"] >= 1240
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors meet the foot traffic requirement (min: {downtown['foot_traffic'].min():.0f})."
    else:
        viol = downtown[~condition]
        ids = ", ".join(map(str, viol["sensor_id"].tolist()))
        expl = f"{len(viol)} downtown sensors fall short (sensor_id(s): {ids}; foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All residential sensors use no more than 205.1 kWh of power on average."""
    residential = df[df["zone"] == "residential"]
    condition = residential["power_use_kwh"] <= 205.1
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors stay within power limit (max: {residential['power_use_kwh'].max():.2f} kWh)."
    else:
        viol = residential[~condition]
        ids = ", ".join(map(str, viol["sensor_id"].tolist()))
        expl = f"{len(viol)} residential sensors exceed the limit (sensor_id(s): {ids}; power use: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All industrial sensors have an average PM2.5 concentration of at least 31.6 µg/m³."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["pm25"] >= 31.6
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors meet the PM2.5 minimum (min: {industrial['pm25'].min():.2f} µg/m³)."
    else:
        viol = industrial[~condition]
        ids = ", ".join(map(str, viol["sensor_id"].tolist()))
        expl = f"{len(viol)} industrial sensors fall below the threshold (sensor_id(s): {ids}; PM2.5: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All park sensors have an average temperature below 23 °C."""
    park = df[df["zone"] == "park"]
    condition = park["avg_temp_c"] < 23
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have temperature below 23 °C (max: {park['avg_temp_c'].max():.2f} °C)."
    else:
        viol = park[~condition]
        ids = ", ".join(map(str, viol["sensor_id"].tolist()))
        expl = f"{len(viol)} park sensors violate the temperature rule (sensor_id(s): {ids}; temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All downtown sensors have average humidity between 56.4 % and 58.9 %."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["avg_humidity"].between(56.4, 58.9, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have humidity within the range (min: {downtown['avg_humidity'].min():.2f} %, max: {downtown['avg_humidity'].max():.2f} %)."
    else:
        viol = downtown[~condition]
        ids = ", ".join(map(str, viol["sensor_id"].tolist()))
        expl = f"{len(viol)} downtown sensors fall outside the humidity range (sensor_id(s): {ids}; humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All residential sensors have average noise levels between 50.8 dB and 52.6 dB."""
    residential = df[df["zone"] == "residential"]
    condition = residential["noise_db"].between(50.8, 52.6, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have noise within the range (min: {residential['noise_db'].min():.2f} dB, max: {residential['noise_db'].max():.2f} dB)."
    else:
        viol = residential[~condition]
        ids = ", ".join(map(str, viol["sensor_id"].tolist()))
        expl = f"{len(viol)} residential sensors violate the noise range (sensor_id(s): {ids}; noise: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def main():
    # Load data
    df = pd.read_csv("tables/table_9.csv")
    # Convert numeric columns that may be stored as strings
    numeric_cols = ["avg_temp_c", "avg_humidity", "pm25", "noise_db", "foot_traffic", "power_use_kwh"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    # Define checks
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