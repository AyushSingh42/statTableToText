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
        expl = f"All {len(industrial)} industrial sensors have avg temp between 21.6°C and 26.7°C."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All park sensors have average noise level no greater than 70.4 dB."""
    park = df[df["zone"] == "park"]
    condition = park["noise_db"] <= 70.4
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have noise level ≤ 70.4 dB."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All downtown sensors have foot traffic of at most 1031 persons."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["foot_traffic"] <= 1031
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot traffic ≤ 1031."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All residential sensors have power consumption of at least 156.0 kWh."""
    residential = df[df["zone"] == "residential"]
    condition = residential["power_use_kwh"] >= 156.0
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have power use ≥ 156.0 kWh."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (power use: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Any sensor with average temperature above 26°C is located in either the industrial or park zone."""
    hot_sensors = df[df["avg_temp_c"] > 26]
    valid_zones = hot_sensors["zone"].isin(["industrial", "park"])
    truth = valid_zones.all()
    if truth:
        expl = f"All {len(hot_sensors)} hot sensors are in industrial or park zones."
    else:
        viol = hot_sensors[~valid_zones]
        expl = f"{len(viol)} hot sensors are in invalid zones ({', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. The only sensor with foot traffic exceeding 1300 is in the industrial zone (sensor SN037013 with 1358 foot traffic)."""
    high_foot = df[df["foot_traffic"] > 1300]
    if len(high_foot)!= 1:
        return False, f"There are {len(high_foot)} sensors with foot traffic > 1300, expected exactly 1."
    if high_foot.iloc[0]["sensor_id"]!= "SN037013":
        return False, f"Sensor with foot traffic > 1300 is {high_foot.iloc[0]['sensor_id']}, expected SN037013."
    if high_foot.iloc[0]["foot_traffic"]!= 1358:
        return False, f"Foot traffic value is {high_foot.iloc[0]['foot_traffic']}, expected 1358."
    if high_foot.iloc[0]["zone"]!= "industrial":
        return False, f"Sensor with foot traffic > 1300 is in zone {high_foot.iloc[0]['zone']}, expected industrial."
    return True, "Only sensor SN037013 with foot traffic 1358 is in industrial zone."

def stmt_7(df: pd.DataFrame):
    """7. Most sensors (13 out of 15) have average humidity between 52.8% and 64.3%."""
    condition = df["avg_humidity"].between(52.8, 64.3, inclusive="both")
    count = condition.sum()
    if count >= 13:
        expl = f"{count} out of {len(df)} sensors have humidity between 52.8% and 64.3%."
    else:
        expl = f"Only {count} out of {len(df)} sensors meet the humidity range, expected at least 13."
    return count >= 13, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with noise ≤44.2 dB are in the residential zone."""
    quiet_sensors = df[df["noise_db"] <= 44.2]
    if len(quiet_sensors) == 0:
        return True, "No sensors have noise ≤ 44.2 dB."
    valid_zones = quiet_sensors["zone"] == "residential"
    truth = valid_zones.all()
    if truth:
        expl = f"All {len(quiet_sensors)} quiet sensors are in residential zone."
    else:
        viol = quiet_sensors[~valid_zones]
        expl = f"{len(viol)} quiet sensors are in non-residential zones ({', '.join(viol['zone'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_37.csv")

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