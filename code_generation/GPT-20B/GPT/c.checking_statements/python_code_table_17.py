import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All industrial sensors have avg_temp_c ≤ 22.8°C."""
    mask = df["zone"] == "industrial"
    condition = df.loc[mask, "avg_temp_c"] <= 22.8
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} industrial sensors have avg_temp_c ≤ 22.8°C."
    else:
        viol = df.loc[mask & ~condition, ["sensor_id", "avg_temp_c"]]
        values = ", ".join(f"{row.sensor_id} ({row.avg_temp_c})" for _, row in viol.iterrows())
        expl = f"{viol.shape[0]} industrial sensors violate the rule (values: {values})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All industrial sensors have foot_traffic ≤ 979."""
    mask = df["zone"] == "industrial"
    condition = df.loc[mask, "foot_traffic"] <= 979
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} industrial sensors have foot_traffic ≤ 979."
    else:
        viol = df.loc[mask & ~condition, ["sensor_id", "foot_traffic"]]
        values = ", ".join(f"{row.sensor_id} ({row.foot_traffic})" for _, row in viol.iterrows())
        expl = f"{viol.shape[0]} industrial sensors violate the rule (values: {values})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All industrial sensors have noise_db between 63.6 dB and 68.5 dB inclusive."""
    mask = df["zone"] == "industrial"
    condition = df.loc[mask, "noise_db"].between(63.6, 68.5, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} industrial sensors have noise_db between 63.6 and 68.5 dB."
    else:
        viol = df.loc[mask & ~condition, ["sensor_id", "noise_db"]]
        values = ", ".join(f"{row.sensor_id} ({row.noise_db})" for _, row in viol.iterrows())
        expl = f"{viol.shape[0]} industrial sensors violate the rule (values: {values})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All residential sensors have avg_humidity ≥ 56.6%."""
    mask = df["zone"] == "residential"
    condition = df.loc[mask, "avg_humidity"] >= 56.6
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} residential sensors have avg_humidity ≥ 56.6%."
    else:
        viol = df.loc[mask & ~condition, ["sensor_id", "avg_humidity"]]
        values = ", ".join(f"{row.sensor_id} ({row.avg_humidity})" for _, row in viol.iterrows())
        expl = f"{viol.shape[0]} residential sensors violate the rule (values: {values})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All residential sensors have power_use_kwh ≤ 443.1."""
    mask = df["zone"] == "residential"
    condition = df.loc[mask, "power_use_kwh"] <= 443.1
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} residential sensors have power_use_kwh ≤ 443.1."
    else:
        viol = df.loc[mask & ~condition, ["sensor_id", "power_use_kwh"]]
        values = ", ".join(f"{row.sensor_id} ({row.power_use_kwh})" for _, row in viol.iterrows())
        expl = f"{viol.shape[0]} residential sensors violate the rule (values: {values})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All downtown sensors have foot_traffic ≤ 630."""
    mask = df["zone"] == "downtown"
    condition = df.loc[mask, "foot_traffic"] <= 630
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} downtown sensors have foot_traffic ≤ 630."
    else:
        viol = df.loc[mask & ~condition, ["sensor_id", "foot_traffic"]]
        values = ", ".join(f"{row.sensor_id} ({row.foot_traffic})" for _, row in viol.iterrows())
        expl = f"{viol.shape[0]} downtown sensors violate the rule (values: {values})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a sensor records noise_db > 70 dB, then its zone is either residential or park."""
    mask = df["noise_db"] > 70
    condition = df.loc[mask, "zone"].isin(["residential", "park"])
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} sensors with noise_db > 70 dB are in residential or park zones."
    else:
        viol = df.loc[mask & ~condition, ["sensor_id", "zone", "noise_db"]]
        values = ", ".join(f"{row.sensor_id} ({row.zone}, {row.noise_db})" for _, row in viol.iterrows())
        expl = f"{viol.shape[0]} sensors violate the rule (values: {values})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If avg_temp_c > 27°C, then the zone is either park or residential."""
    mask = df["avg_temp_c"] > 27
    condition = df.loc[mask, "zone"].isin(["park", "residential"])
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} sensors with avg_temp_c > 27°C are in park or residential zones."
    else:
        viol = df.loc[mask & ~condition, ["sensor_id", "zone", "avg_temp_c"]]
        values = ", ".join(f"{row.sensor_id} ({row.zone}, {row.avg_temp_c})" for _, row in viol.iterrows())
        expl = f"{viol.shape[0]} sensors violate the rule (values: {values})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_17.csv")

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
        (8, stmt_8),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()