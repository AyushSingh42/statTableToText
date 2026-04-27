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
        expl = f"All {len(downtown)} downtown sensors satisfy the temperature range."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the range (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All industrial sensors have noise levels of at least 61.2 dB."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["noise_db"] >= 61.2
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have noise ≥ 61.2 dB."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (noise: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All park sensors have PM2.5 concentrations of at least 21.5 µg/m³."""
    park = df[df["zone"] == "park"]
    if park.empty:
        return True, "No park sensors present; statement vacuously true."
    condition = park["pm25"] >= 21.5
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors satisfy the PM2.5 threshold."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (PM2.5: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All residential sensors have humidity of at most 58.8%."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_humidity"] <= 58.8
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have humidity ≤ 58.8%."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a sensor records noise above 70 dB, its foot traffic exceeds 1400."""
    high_noise = df[df["noise_db"] > 70]
    if high_noise.empty:
        return True, "No sensors with noise > 70 dB; statement vacuously true."
    condition = high_noise["foot_traffic"] > 1400
    truth = condition.all()
    if truth:
        expl = f"All {len(high_noise)} high‑noise sensors have foot traffic > 1400."
    else:
        viol = high_noise[~condition]
        expl = f"{len(viol)} high‑noise sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If PM2.5 is 34 µg/m³ or higher, the zone is downtown."""
    high_pm25 = df[df["pm25"] >= 34]
    if high_pm25.empty:
        return True, "No sensors with PM2.5 ≥ 34 µg/m³; statement vacuously true."
    condition = high_pm25["zone"] == "downtown"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_pm25)} high‑PM2.5 sensors are in downtown."
    else:
        viol = high_pm25[~condition]
        expl = f"{len(viol)} high‑PM2.5 sensors are not downtown (zones: {', '.join(viol['zone'].unique())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All sensors with humidity above 62% are located in industrial or downtown zones."""
    high_humidity = df[df["avg_humidity"] > 62]
    if high_humidity.empty:
        return True, "No sensors with humidity > 62%; statement vacuously true."
    condition = high_humidity["zone"].isin(["industrial", "downtown"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_humidity)} high‑humidity sensors are in industrial or downtown zones."
    else:
        viol = high_humidity[~condition]
        expl = f"{len(viol)} high‑humidity sensors are not in industrial/downtown zones (zones: {', '.join(viol['zone'].unique())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most sensors have average temperature between 21.8°C and 25.4°C."""
    condition = df["avg_temp_c"].between(21.8, 25.4, inclusive="both")
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of sensors (>{len(df)//2}) satisfy the temperature range."
    else:
        expl = f"Only {proportion*100:.1f}% of sensors satisfy the temperature range; not a majority."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_7.csv")

    # Convert numeric columns safely
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