import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All industrial sensors have average humidity of at least 65.8%."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_humidity"] >= 65.8
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have humidity >= 65.8%."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All residential sensors have noise levels of at least 64.5 dB."""
    residential = df[df["zone"] == "residential"]
    condition = residential["noise_db"] >= 64.5
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have noise >= 64.5 dB."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (noise: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the downtown zone, its foot traffic is at least 432."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["foot_traffic"] >= 432
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot traffic >= 432."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a sensor is in the industrial zone, its average temperature is between 24.6°C and 25.9°C."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_temp_c"].between(24.6, 25.9, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have temp between 24.6°C and 25.9°C."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (temp: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All park sensors have average humidity of at most 66.5%."""
    park = df[df["zone"] == "park"]
    condition = park["avg_humidity"] <= 66.5
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have humidity <= 66.5%."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All sensors with average temperature below 22°C have power use greater than 213.8 kWh."""
    cold = df[df["avg_temp_c"] < 22]
    condition = cold["power_use_kwh"] > 213.8
    truth = condition.all()
    if truth:
        expl = f"All {len(cold)} cold sensors have power use > 213.8 kWh."
    else:
        viol = cold[~condition]
        expl = f"{len(viol)} cold sensors violate the rule (power use: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a sensor records noise above 70 dB, it is located in either the downtown or park zone."""
    loud = df[df["noise_db"] > 70]
    condition = loud["zone"].isin(["downtown", "park"])
    truth = condition.all()
    if truth:
        expl = f"All {len(loud)} loud sensors are in downtown or park zones."
    else:
        viol = loud[~condition]
        expl = f"{len(viol)} loud sensors violate the rule (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_97.csv")

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
        (7, stmt_7)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()