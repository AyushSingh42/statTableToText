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
        expl = f"All {len(residential)} residential sensors meet the temperature requirement."
    else:
        viol = residential[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} residential sensors violate the rule (IDs: {', '.join(map(str, ids))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All park zones have pm25 of at least 12.8 µg/m³."""
    park = df[df["zone"] == "park"]
    condition = park["pm25"] >= 12.8
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors meet the PM2.5 requirement."
    else:
        viol = park[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} park sensors violate the rule (IDs: {', '.join(map(str, ids))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All industrial zones have power_use_kwh of at least 302.3 kWh."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["power_use_kwh"] >= 302.3
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors meet the power usage requirement."
    else:
        viol = industrial[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} industrial sensors violate the rule (IDs: {', '.join(map(str, ids))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All downtown zones have foot_traffic between 823 and 1184 per day."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["foot_traffic"].between(823, 1184, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot traffic in the required range."
    else:
        viol = downtown[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} downtown sensors violate the rule (IDs: {', '.join(map(str, ids))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most sensors record noise below 65 dB."""
    total = len(df)
    below = df[df["noise_db"] < 65]
    count_below = len(below)
    truth = count_below > total / 2
    if truth:
        expl = f"{count_below} out of {total} sensors (>{total/2}) record noise below 65 dB."
    else:
        expl = f"Only {count_below} out of {total} sensors record noise below 65 dB, which is not a majority."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All sensors with foot_traffic exceeding 1300 record noise of at least 57.1 dB."""
    high_ft = df[df["foot_traffic"] > 1300]
    condition = high_ft["noise_db"] >= 57.1
    truth = condition.all()
    if truth:
        expl = f"All {len(high_ft)} high foot-traffic sensors meet the noise requirement."
    else:
        viol = high_ft[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} high foot-traffic sensors violate the rule (IDs: {', '.join(map(str, ids))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All sensors with power consumption exceeding 350 kWh have foot_traffic of at least 990."""
    high_power = df[df["power_use_kwh"] > 350]
    condition = high_power["foot_traffic"] >= 990
    truth = condition.all()
    if truth:
        expl = f"All {len(high_power)} high power sensors meet the foot-traffic requirement."
    else:
        viol = high_power[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} high power sensors violate the rule (IDs: {', '.join(map(str, ids))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Sensors with average temperature at most 22.5 °C are located in park zones."""
    cold = df[df["avg_temp_c"] <= 22.5]
    condition = cold["zone"] == "park"
    truth = condition.all()
    if truth:
        expl = f"All {len(cold)} low-temperature sensors are in park zones."
    else:
        viol = cold[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} low-temperature sensors are not in park zones (IDs: {', '.join(map(str, ids))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_27.csv")

    # Convert numeric columns where possible
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