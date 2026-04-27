import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All industrial sensors have average humidity of at least 65.8%."""
    industrial = df[df["zone"] == "industrial"]
    if industrial.empty:
        return True, "No industrial sensors to evaluate."
    condition = industrial["avg_humidity"] >= 65.8
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg humidity >= 65.8%."
    else:
        viol = industrial[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} industrial sensors violate the rule (sensor_ids: {', '.join(ids)})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All residential sensors have noise levels of at least 64.5 dB."""
    residential = df[df["zone"] == "residential"]
    if residential.empty:
        return True, "No residential sensors to evaluate."
    condition = residential["noise_db"] >= 64.5
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have noise >= 64.5 dB."
    else:
        viol = residential[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} residential sensors violate the rule (sensor_ids: {', '.join(ids)})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the downtown zone, its foot traffic is at least 432."""
    downtown = df[df["zone"] == "downtown"]
    if downtown.empty:
        return True, "No downtown sensors to evaluate."
    condition = downtown["foot_traffic"] >= 432
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot traffic >= 432."
    else:
        viol = downtown[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} downtown sensors violate the rule (sensor_ids: {', '.join(ids)})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a sensor is in the industrial zone, its average temperature is between 24.6°C and 25.9°C."""
    industrial = df[df["zone"] == "industrial"]
    if industrial.empty:
        return True, "No industrial sensors to evaluate."
    condition = industrial["avg_temp_c"].between(24.6, 25.9, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg temp between 24.6°C and 25.9°C."
    else:
        viol = industrial[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} industrial sensors violate the rule (sensor_ids: {', '.join(ids)})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All park sensors have average humidity of at most 66.5%."""
    park = df[df["zone"] == "park"]
    if park.empty:
        return True, "No park sensors to evaluate."
    condition = park["avg_humidity"] <= 66.5
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg humidity <= 66.5%."
    else:
        viol = park[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} park sensors violate the rule (sensor_ids: {', '.join(ids)})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All sensors with average temperature below 22°C have power use greater than 213.8 kWh."""
    cold = df[df["avg_temp_c"] < 22]
    if cold.empty:
        return True, "No sensors with avg temp below 22°C to evaluate."
    condition = cold["power_use_kwh"] > 213.8
    truth = condition.all()
    if truth:
        expl = f"All {len(cold)} sensors with avg temp < 22°C have power use > 213.8 kWh."
    else:
        viol = cold[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} sensors with avg temp < 22°C violate the rule (sensor_ids: {', '.join(ids)})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a sensor records noise above 70 dB, it is located in either the downtown or park zone."""
    noisy = df[df["noise_db"] > 70]
    if noisy.empty:
        return True, "No sensors with noise > 70 dB to evaluate."
    condition = noisy["zone"].isin(["downtown", "park"])
    truth = condition.all()
    if truth:
        expl = f"All {len(noisy)} sensors with noise > 70 dB are in downtown or park zones."
    else:
        viol = noisy[~condition]
        ids = viol["sensor_id"].tolist()
        expl = f"{len(viol)} sensors with noise > 70 dB violate the rule (sensor_ids: {', '.join(ids)})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_97.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col not in ["sensor_id", "zone"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    checks = [
        (1, stmt_1),
        (2, stmt_2),
        (3, stmt_3),
        (4, stmt_4),
        (5, stmt_5),
        (6, stmt_6),
        (7, stmt_7),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()