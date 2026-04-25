import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All residential sensors have avg_temp_c between 20.6°C and 25.1°C."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_temp_c"].between(20.6, 25.1, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors meet the avg_temp_c range."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the range (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a sensor is in the park zone, then its avg_temp_c is at least 22.7°C."""
    park = df[df["zone"] == "park"]
    if len(park) == 0:
        expl = "No sensors in park zone."
        return True, expl
    condition = park["avg_temp_c"] >= 22.7
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors meet the avg_temp_c threshold."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the threshold (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All downtown sensors have avg_temp_c no higher than 25.0°C."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["avg_temp_c"] <= 25.0
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors meet the avg_temp_c limit."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors exceed the limit (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All sensors with pm25 ≥ 30 have power_use_kwh ≥ 341.5 kWh."""
    high_pm25 = df[df["pm25"] >= 30]
    if len(high_pm25) == 0:
        expl = "No sensors with pm25 >= 30."
        return True, expl
    condition = high_pm25["power_use_kwh"] >= 341.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_pm25)} high pm25 sensors meet the power_use_kwh threshold."
    else:
        viol = high_pm25[~condition]
        expl = f"{len(viol)} high pm25 sensors violate the threshold (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All industrial sensors have avg_humidity of at least 58.8%."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_humidity"] >= 58.8
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors meet the avg_humidity threshold."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the threshold (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All park sensors have foot_traffic of at least 537."""
    park = df[df["zone"] == "park"]
    if len(park) == 0:
        expl = "No sensors in park zone."
        return True, expl
    condition = park["foot_traffic"] >= 537
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors meet the foot_traffic threshold."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the threshold (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors (14 out of 15) have avg_temp_c ≤ 25.1°C."""
    condition = df["avg_temp_c"] <= 25.1
    count = condition.sum()
    truth = count >= 14
    if truth:
        expl = f"{count} out of {len(df)} sensors meet the avg_temp_c limit (≥14)."
    else:
        expl = f"{count} out of {len(df)} sensors meet the avg_temp_c limit (<14)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All residential sensors have noise_db no greater than 68.2 dB."""
    residential = df[df["zone"] == "residential"]
    condition = residential["noise_db"] <= 68.2
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors meet the noise_db limit."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors exceed the limit (noise_db: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_87.csv")

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