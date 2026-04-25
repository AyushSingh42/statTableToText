import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All downtown sensors have average temperature between 21.8°C and 25.4°C."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["avg_temp_c"].between(21.8, 25.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors meet the temperature range."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All industrial sensors have noise levels of at least 61.2 dB."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["noise_db"] >= 61.2
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors meet the noise level requirement."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All park sensors have PM2.5 concentrations of at least 21.5 µg/m³."""
    park = df[df["zone"] == "park"]
    condition = park["pm25"] >= 21.5
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors meet the PM2.5 concentration requirement."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (PM2.5 levels: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All residential sensors have humidity of at most 58.8%."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_humidity"] <= 58.8
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors meet the humidity limit."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (humidity levels: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a sensor records noise above 70 dB, its foot traffic exceeds 1400."""
    condition = (df["noise_db"] > 70) & (df["foot_traffic"] <= 1400)
    truth = not condition.any()
    if truth:
        expl = "No sensor violates the rule: those with noise > 70 dB also have foot traffic > 1400."
    else:
        viol = df[condition]
        expl = f"{len(viol)} sensors violate the rule (noise: {', '.join(map(str, viol['noise_db'].tolist()))}, foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If PM2.5 is 34 µg/m³ or higher, the zone is downtown."""
    condition = (df["pm25"] >= 34) & (df["zone"]!= "downtown")
    truth = not condition.any()
    if truth:
        expl = "All sensors with PM2.5 ≥ 34 µg/m³ are correctly classified as downtown."
    else:
        viol = df[condition]
        expl = f"{len(viol)} sensors violate the rule (PM2.5: {', '.join(map(str, viol['pm25'].tolist()))}, zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All sensors with humidity above 62% are located in industrial or downtown zones."""
    condition = (df["avg_humidity"] > 62) & (~df["zone"].isin(["industrial", "downtown"]))
    truth = not condition.any()
    if truth:
        expl = "All sensors with humidity > 62% are correctly located in industrial or downtown zones."
    else:
        viol = df[condition]
        expl = f"{len(viol)} sensors violate the rule (humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))}, zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most sensors have average temperature between 21.8°C and 25.4°C."""
    total = len(df)
    condition = df["avg_temp_c"].between(21.8, 25.4, inclusive="both")
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} sensors ({count/total*100:.1f}%) have temperatures in the specified range."
    else:
        expl = f"Only {count} out of {total} sensors ({count/total*100:.1f}%) have temperatures in the specified range."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_7.csv")

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