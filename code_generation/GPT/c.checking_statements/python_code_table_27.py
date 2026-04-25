import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All residential zones have avg_temp_c of at least 23.8 °C."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_temp_c"] >= 23.8
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential zones meet the temperature requirement."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential zones violate the rule (temperatures: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All park zones have pm25 of at least 12.8 µg/m³."""
    park = df[df["zone"] == "park"]
    condition = park["pm25"] >= 12.8
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park zones meet the PM2.5 requirement."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park zones violate the rule (PM2.5 levels: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All industrial zones have power_use_kwh of at least 302.3 kWh."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["power_use_kwh"] >= 302.3
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial zones meet the power usage requirement."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial zones violate the rule (power usage: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All downtown zones have foot_traffic between 823 and 1184 per day."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["foot_traffic"].between(823, 1184, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown zones meet the foot traffic requirement."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown zones violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most sensors record noise below 65 dB."""
    condition = df["noise_db"] < 65
    count_below = condition.sum()
    total = len(df)
    truth = count_below > total / 2
    expl = f"{count_below} out of {total} sensors record noise below 65 dB, which is {'more than half' if truth else 'not more than half'}."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All sensors with foot_traffic exceeding 1300 record noise of at least 57.1 dB."""
    high_foot = df[df["foot_traffic"] > 1300]
    condition = high_foot["noise_db"] >= 57.1
    truth = condition.all()
    if truth:
        expl = f"All {len(high_foot)} sensors with high foot traffic meet the noise requirement."
    else:
        viol = high_foot[~condition]
        expl = f"{len(viol)} sensors with high foot traffic violate the rule (noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All sensors with power consumption exceeding 350 kWh have foot_traffic of at least 990."""
    high_power = df[df["power_use_kwh"] > 350]
    condition = high_power["foot_traffic"] >= 990
    truth = condition.all()
    if truth:
        expl = f"All {len(high_power)} sensors with high power consumption meet the foot traffic requirement."
    else:
        viol = high_power[~condition]
        expl = f"{len(viol)} sensors with high power consumption violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Sensors with average temperature at most 22.5 °C are located in park zones."""
    low_temp = df[df["avg_temp_c"] <= 22.5]
    condition = low_temp["zone"] == "park"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_temp)} sensors with low temperature are located in park zones."
    else:
        viol = low_temp[~condition]
        expl = f"{len(viol)} sensors with low temperature are not located in park zones (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_27.csv")

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