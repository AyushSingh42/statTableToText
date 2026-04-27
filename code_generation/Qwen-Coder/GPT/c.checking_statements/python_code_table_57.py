import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All industrial sensors have an average temperature of at most 20.9°C."""
    industrial = df[df["zone"] == "industrial"]
    if industrial.empty:
        truth = True
        expl = "No industrial sensors in dataset."
    else:
        condition = industrial["avg_temp_c"] <= 20.9
        truth = condition.all()
        if truth:
            expl = f"All {len(industrial)} industrial sensors have avg temp <= 20.9°C."
        else:
            viol = industrial[~condition]
            expl = f"{len(viol)} industrial sensors exceed 20.9°C (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All park sensors record foot traffic of at least 443 people."""
    park = df[df["zone"] == "park"]
    if park.empty:
        truth = True
        expl = "No park sensors in dataset."
    else:
        condition = park["foot_traffic"] >= 443
        truth = condition.all()
        if truth:
            expl = f"All {len(park)} park sensors record foot traffic >= 443."
        else:
            viol = park[~condition]
            expl = f"{len(viol)} park sensors record < 443 foot traffic (values: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All residential sensors record foot traffic of at least 432 people."""
    residential = df[df["zone"] == "residential"]
    if residential.empty:
        truth = True
        expl = "No residential sensors in dataset."
    else:
        condition = residential["foot_traffic"] >= 432
        truth = condition.all()
        if truth:
            expl = f"All {len(residential)} residential sensors record foot traffic >= 432."
        else:
            viol = residential[~condition]
            expl = f"{len(viol)} residential sensors record < 432 foot traffic (values: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All sensors with an average temperature of 27°C or higher have power use of at least 223.9 kWh."""
    hot_sensors = df[df["avg_temp_c"] >= 27]
    if hot_sensors.empty:
        truth = True
        expl = "No sensors with avg temp >= 27°C."
    else:
        condition = hot_sensors["power_use_kwh"] >= 223.9
        truth = condition.all()
        if truth:
            expl = f"All {len(hot_sensors)} hot sensors have power use >= 223.9 kWh."
        else:
            viol = hot_sensors[~condition]
            expl = f"{len(viol)} hot sensors have power use < 223.9 kWh (values: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with PM2.5 concentrations of 25 µg/m³ or higher have noise levels of at most 60.1 dB."""
    high_pm25 = df[df["pm25"] >= 25]
    if high_pm25.empty:
        truth = True
        expl = "No sensors with PM2.5 >= 25 µg/m³."
    else:
        condition = high_pm25["noise_db"] <= 60.1
        truth = condition.all()
        if truth:
            expl = f"All {len(high_pm25)} high PM2.5 sensors have noise level <= 60.1 dB."
        else:
            viol = high_pm25[~condition]
            expl = f"{len(viol)} high PM2.5 sensors have noise > 60.1 dB (values: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All sensors with average humidity above 60% have foot traffic of at least 582 people."""
    humid = df[df["avg_humidity"] > 60]
    if humid.empty:
        truth = True
        expl = "No sensors with avg humidity > 60%."
    else:
        condition = humid["foot_traffic"] >= 582
        truth = condition.all()
        if truth:
            expl = f"All {len(humid)} humid sensors have foot traffic >= 582."
        else:
            viol = humid[~condition]
            expl = f"{len(viol)} humid sensors have foot traffic < 582 (values: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All sensors with noise levels of 60 dB or higher have an average temperature of at most 25.5°C."""
    loud = df[df["noise_db"] >= 60]
    if loud.empty:
        truth = True
        expl = "No sensors with noise level >= 60 dB."
    else:
        condition = loud["avg_temp_c"] <= 25.5
        truth = condition.all()
        if truth:
            expl = f"All {len(loud)} loud sensors have avg temp <= 25.5°C."
        else:
            viol = loud[~condition]
            expl = f"{len(viol)} loud sensors have avg temp > 25.5°C (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All downtown sensors have average temperatures between 20.9°C and 25.5°C inclusive."""
    downtown = df[df["zone"] == "downtown"]
    if downtown.empty:
        truth = True
        expl = "No downtown sensors in dataset."
    else:
        condition = downtown["avg_temp_c"].between(20.9, 25.5, inclusive="both")
        truth = condition.all()
        if truth:
            expl = f"All {len(downtown)} downtown sensors have avg temp between 20.9°C and 25.5°C."
        else:
            viol = downtown[~condition]
            expl = f"{len(viol)} downtown sensors have avg temp outside 20.9-25.5°C range (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_57.csv")

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