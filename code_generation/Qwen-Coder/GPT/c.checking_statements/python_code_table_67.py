import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All industrial sensors have average temperature between 20.5°C and 27.7°C."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_temp_c"].between(20.5, 27.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg temp between 20.5°C and 27.7°C."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All park sensors have average humidity between 55.0% and 61.2%."""
    park = df[df["zone"] == "park"]
    condition = park["avg_humidity"].between(55.0, 61.2, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg humidity between 55.0% and 61.2%."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All residential sensors have PM2.5 of at least 25.9 µg/m³."""
    residential = df[df["zone"] == "residential"]
    condition = residential["pm25"] >= 25.9
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have PM2.5 >= 25.9 µg/m³."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (PM2.5 values: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All downtown sensors have noise levels below 63 dB."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["noise_db"] < 63
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have noise levels below 63 dB."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All park sensors have PM2.5 ≤24.7 µg/m³."""
    park = df[df["zone"] == "park"]
    condition = park["pm25"] <= 24.7
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have PM2.5 <= 24.7 µg/m³."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (PM2.5 values: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Any sensor with foot traffic exceeding 1300 is in the residential or downtown zone."""
    high_foot = df[df["foot_traffic"] > 1300]
    condition = high_foot["zone"].isin(["residential", "downtown"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_foot)} sensors with foot traffic > 1300 are in residential or downtown zones."
    else:
        viol = high_foot[~condition]
        expl = f"{len(viol)} sensors with foot traffic > 1300 are not in residential or downtown zones (zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. The highest noise level recorded (74.9 dB) occurs at an industrial sensor."""
    max_noise = df["noise_db"].max()
    max_noise_row = df[df["noise_db"] == max_noise]
    is_industrial = max_noise_row["zone"].iloc[0] == "industrial"
    truth = is_industrial and max_noise == 74.9
    if truth:
        expl = f"The highest noise level ({max_noise} dB) occurs at an industrial sensor."
    else:
        expl = f"The highest noise level ({max_noise} dB) does not occur at an industrial sensor."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. The greatest power consumption (443.8 kWh) is observed at a residential sensor."""
    max_power = df["power_use_kwh"].max()
    max_power_row = df[df["power_use_kwh"] == max_power]
    is_residential = max_power_row["zone"].iloc[0] == "residential"
    truth = is_residential and max_power == 443.8
    if truth:
        expl = f"The greatest power consumption ({max_power} kWh) is observed at a residential sensor."
    else:
        expl = f"The greatest power consumption ({max_power} kWh) is not observed at a residential sensor."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_67.csv")

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