import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the downtown zone have an average temperature between 21.9 and 25.0 degrees Celsius."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["avg_temp_c"].between(21.9, 25.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have avg_temp_c between 21.9 and 25.0."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the residential zone have an average humidity between 54.7 and 62.5 percent."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_humidity"].between(54.7, 62.5, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have avg_humidity between 54.7 and 62.5."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the industrial zone, then its average temperature is between 20.8 and 24.3 degrees Celsius."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_temp_c"].between(20.8, 24.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg_temp_c between 20.8 and 24.3."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the park zone with an average noise level less than 60 decibels."""
    park = df[df["zone"] == "park"]
    condition = park["noise_db"] < 60
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"Found {count} park sensor(s) with noise_db < 60."
    else:
        expl = "No park sensor has noise_db < 60."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with an average particulate matter 2.5 level greater than 30 have a power usage less than or equal to 433.6 kilowatt-hours."""
    high_pm = df[df["pm25"] > 30]
    condition = high_pm["power_use_kwh"] <= 433.6
    truth = condition.all()
    if truth:
        expl = f"All {len(high_pm)} sensors with pm25 > 30 have power_use_kwh <= 433.6."
    else:
        viol = high_pm[~condition]
        expl = f"{len(viol)} sensors with pm25 > 30 violate the rule (power_use_kwh: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a sensor is in the downtown zone, then its foot traffic is greater than or equal to 439."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["foot_traffic"] >= 439
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot_traffic >= 439."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors have an average temperature between 20 and 25 degrees Celsius."""
    condition = df["avg_temp_c"].between(20, 25, inclusive="both")
    count = condition.sum()
    truth = count > df.shape[0] / 2
    if truth:
        expl = f"{count} of {df.shape[0]} sensors ({count / df.shape[0] * 100:.1f}%) have avg_temp_c between 20 and 25."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average humidity less than 50 percent are in the park or downtown zone."""
    low_humidity = df[df["avg_humidity"] < 50]
    condition = low_humidity["zone"].isin(["park", "downtown"])
    truth = condition.all()
    if truth:
        expl = f"All {len(low_humidity)} sensors with avg_humidity < 50 are in park or downtown."
    else:
        viol = low_humidity[~condition]
        expl = f"{len(viol)} sensors with avg_humidity < 50 are not in park or downtown (zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a sensor is in the residential zone, then its average noise level is greater than or equal to 43.4 decibels."""
    residential = df[df["zone"] == "residential"]
    condition = residential["noise_db"] >= 43.4
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have noise_db >= 43.4."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (noise_db: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the industrial zone with an average particulate matter 2.5 level greater than 20."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["pm25"] > 20
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"Found {count} industrial sensor(s) with pm25 > 20."
    else:
        expl = "No industrial sensor has pm25 > 20."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All sensors with a power usage greater than 400 kilowatt-hours are in the residential or industrial zone."""
    high_power = df[df["power_use_kwh"] > 400]
    condition = high_power["zone"].isin(["residential", "industrial"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_power)} sensors with power_use_kwh > 400 are in residential or industrial."
    else:
        viol = high_power[~condition]
        expl = f"{len(viol)} sensors with power_use_kwh > 400 are not in residential or industrial (zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a sensor is in the park zone, then its foot traffic is less than or equal to 1237."""
    park = df[df["zone"] == "park"]
    condition = park["foot_traffic"] <= 1237
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have foot_traffic <= 1237."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most sensors have an average particulate matter 2.5 level between 10 and 35."""
    condition = df["pm25"].between(10, 35, inclusive="both")
    count = condition.sum()
    truth = count > df.shape[0] / 2
    if truth:
        expl = f"{count} of {df.shape[0]} sensors ({count / df.shape[0] * 100:.1f}%) have pm25 between 10 and 35."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} sensors violate the rule (pm25: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All sensors with an average temperature greater than 25 degrees Celsius are in the park zone."""
    high_temp = df[df["avg_temp_c"] > 25]
    condition = high_temp["zone"] == "park"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_temp)} sensors with avg_temp_c > 25 are in park."
    else:
        viol = high_temp[~condition]
        expl = f"{len(viol)} sensors with avg_temp_c > 25 are not in park (zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a sensor is in the downtown zone, then its average humidity is between 49.6 and 65.3 percent."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["avg_humidity"].between(49.6, 65.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have avg_humidity between 49.6 and 65.3."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one sensor in the residential zone with an average noise level less than 60 decibels."""
    residential = df[df["zone"] == "residential"]
    condition = residential["noise_db"] < 60
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"Found {count} residential sensor(s) with noise_db < 60."
    else:
        expl = "No residential sensor has noise_db < 60."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_87.csv")

    # Convert numeric columns safely
    numeric_cols = ["avg_temp_c", "avg_humidity", "pm25", "noise_db", "foot_traffic", "power_use_kwh"]
    for col in numeric_cols:
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
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()