import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All industrial sensors have average temperature between 21.6°C and 26.7°C."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_temp_c"].between(21.6, 26.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg_temp_c in [21.6, 26.7]."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All park sensors have average noise level no greater than 70.4 dB."""
    park = df[df["zone"] == "park"]
    condition = park["noise_db"] <= 70.4
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have noise_db ≤ 70.4."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (noise_db: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All downtown sensors have foot traffic of at most 1031 persons."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["foot_traffic"] <= 1031
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot_traffic ≤ 1031."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All residential sensors have power consumption of at least 156.0 kWh."""
    residential = df[df["zone"] == "residential"]
    condition = residential["power_use_kwh"] >= 156.0
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have power_use_kwh ≥ 156.0."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Any sensor with average temperature above 26°C is located in either the industrial or park zone."""
    high_temp = df[df["avg_temp_c"] > 26]
    condition = high_temp["zone"].isin(["industrial", "park"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_temp)} sensors with avg_temp_c > 26 are in industrial or park zones."
    else:
        viol = high_temp[~condition]
        expl = f"{len(viol)} sensors with avg_temp_c > 26 are not in industrial or park zones (zones: {', '.join(viol['zone'].unique())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. The only sensor with foot traffic exceeding 1300 is in the industrial zone (sensor SN037013 with 1358 foot traffic)."""
    high_ft = df[df["foot_traffic"] > 1300]
    count = len(high_ft)
    truth = (count == 1) and (high_ft.iloc[0]["zone"] == "industrial") and (high_ft.iloc[0]["sensor_id"] == "SN037013") and (high_ft.iloc[0]["foot_traffic"] == 1358)
    if truth:
        expl = f"Only sensor {high_ft.iloc[0]['sensor_id']} has foot_traffic > 1300 and is in industrial zone."
    else:
        if count == 0:
            expl = "No sensor has foot_traffic > 1300."
        else:
            viol = high_ft
            expl = f"{count} sensors have foot_traffic > 1300; they are in zones: {', '.join(viol['zone'].unique())}."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors (13 out of 15) have average humidity between 52.8% and 64.3%."""
    total = len(df)
    in_range = df["avg_humidity"].between(52.8, 64.3, inclusive="both")
    count_in_range = in_range.sum()
    truth = (total == 15) and (count_in_range == 13)
    if truth:
        expl = f"15 sensors total, 13 have avg_humidity in [52.8, 64.3]."
    else:
        expl = f"Total sensors: {total}. Sensors in humidity range: {count_in_range}."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with noise ≤44.2 dB are in the residential zone."""
    low_noise = df[df["noise_db"] <= 44.2]
    condition = low_noise["zone"] == "residential"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_noise)} sensors with noise_db ≤ 44.2 are in residential zone."
    else:
        viol = low_noise[~condition]
        expl = f"{len(viol)} sensors with noise_db ≤ 44.2 are not in residential zone (zones: {', '.join(viol['zone'].unique())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_37.csv")

    # Convert numeric columns
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