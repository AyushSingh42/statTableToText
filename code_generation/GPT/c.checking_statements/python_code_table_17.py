import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All industrial sensors have avg_temp_c ≤ 22.8°C."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_temp_c"] <= 22.8
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg_temp_c ≤ 22.8°C."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All industrial sensors have foot_traffic ≤ 979."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["foot_traffic"] <= 979
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have foot_traffic ≤ 979."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All industrial sensors have noise_db between 63.6 dB and 68.5 dB inclusive."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["noise_db"].between(63.6, 68.5, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have noise_db between 63.6 and 68.5 dB."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (noise_db: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All residential sensors have avg_humidity ≥ 56.6%."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_humidity"] >= 56.6
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have avg_humidity ≥ 56.6%."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All residential sensors have power_use_kwh ≤ 443.1."""
    residential = df[df["zone"] == "residential"]
    condition = residential["power_use_kwh"] <= 443.1
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have power_use_kwh ≤ 443.1."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All downtown sensors have foot_traffic ≤ 630."""
    # Assume downtown sensors are those with zone = 'downtown'
    downtown = df[df["zone"] == "downtown"]
    if len(downtown) == 0:
        truth = True
        expl = "No downtown sensors found."
    else:
        condition = downtown["foot_traffic"] <= 630
        truth = condition.all()
        if truth:
            expl = f"All {len(downtown)} downtown sensors have foot_traffic ≤ 630."
        else:
            viol = downtown[~condition]
            expl = f"{len(viol)} downtown sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a sensor records noise_db > 70 dB, then its zone is either residential or park."""
    condition = (df["noise_db"] > 70) & (~df["zone"].isin(["residential", "park"]))
    viol = df[condition]
    truth = len(viol) == 0
    if truth:
        expl = "No sensor with noise_db > 70 dB has a zone other than residential or park."
    else:
        expl = f"{len(viol)} sensors violate the rule (noise_db > 70 but zone is {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If avg_temp_c > 27°C, then the zone is either park or residential."""
    condition = (df["avg_temp_c"] > 27) & (~df["zone"].isin(["park", "residential"]))
    viol = df[condition]
    truth = len(viol) == 0
    if truth:
        expl = "No sensor with avg_temp_c > 27°C has a zone other than park or residential."
    else:
        expl = f"{len(viol)} sensors violate the rule (avg_temp_c > 27 but zone is {', '.join(viol['zone'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_17.csv")

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