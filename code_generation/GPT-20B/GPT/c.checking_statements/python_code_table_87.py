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
        expl = f"All {len(residential)} residential sensors have avg_temp_c in the range 20.6–25.1°C."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a sensor is in the park zone, then its avg_temp_c is at least 22.7°C."""
    park = df[df["zone"] == "park"]
    condition = park["avg_temp_c"] >= 22.7
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg_temp_c ≥ 22.7°C."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All downtown sensors have avg_temp_c no higher than 25.0°C."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["avg_temp_c"] <= 25.0
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have avg_temp_c ≤ 25.0°C."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All sensors with pm25 ≥ 30 have power_use_kwh ≥ 341.5 kWh."""
    high_pm25 = df[df["pm25"] >= 30]
    condition = high_pm25["power_use_kwh"] >= 341.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_pm25)} sensors with pm25 ≥ 30 have power_use_kwh ≥ 341.5 kWh."
    else:
        viol = high_pm25[~condition]
        expl = f"{len(viol)} sensors with pm25 ≥ 30 violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All industrial sensors have avg_humidity of at least 58.8%."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_humidity"] >= 58.8
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg_humidity ≥ 58.8%."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All park sensors have foot_traffic of at least 537."""
    park = df[df["zone"] == "park"]
    condition = park["foot_traffic"] >= 537
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have foot_traffic ≥ 537."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors (14 out of 15) have avg_temp_c ≤ 25.1°C."""
    count = df[df["avg_temp_c"] <= 25.1].shape[0]
    total = df.shape[0]
    truth = count >= 14
    if truth:
        expl = f"{count} out of {total} sensors have avg_temp_c ≤ 25.1°C."
    else:
        expl = f"Only {count} out of {total} sensors have avg_temp_c ≤ 25.1°C."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All residential sensors have noise_db no greater than 68.2 dB."""
    residential = df[df["zone"] == "residential"]
    condition = residential["noise_db"] <= 68.2
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have noise_db ≤ 68.2 dB."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (noise_db: {', '.join(map(str, viol['noise_db'].tolist()))})."
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
        (8, stmt_8),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()