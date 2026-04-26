import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the downtown zone have an average temperature between 21.9 and 25.0 degrees Celsius."""
    downtown = df[df["zone"] == "downtown"]
    if downtown.empty:
        truth = True
        expl = "No sensors in downtown zone."
    else:
        condition = downtown["avg_temp_c"].between(21.9, 25.0, inclusive="both")
        truth = condition.all()
        if truth:
            expl = f"All {len(downtown)} downtown sensors have avg temp between 21.9 and 25.0°C."
        else:
            viol = downtown[~condition]
            expl = f"{len(viol)} downtown sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the residential zone have an average humidity between 54.7 and 62.5 percent."""
    residential = df[df["zone"] == "residential"]
    if residential.empty:
        truth = True
        expl = "No sensors in residential zone."
    else:
        condition = residential["avg_humidity"].between(54.7, 62.5, inclusive="both")
        truth = condition.all()
        if truth:
            expl = f"All {len(residential)} residential sensors have avg humidity between 54.7 and 62.5%."
        else:
            viol = residential[~condition]
            expl = f"{len(viol)} residential sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the industrial zone, then its average temperature is between 20.8 and 24.3 degrees Celsius."""
    industrial = df[df["zone"] == "industrial"]
    if industrial.empty:
        truth = True
        expl = "No sensors in industrial zone."
    else:
        condition = industrial["avg_temp_c"].between(20.8, 24.3, inclusive="both")
        truth = condition.all()
        if truth:
            expl = f"All {len(industrial)} industrial sensors have avg temp between 20.8 and 24.3°C."
        else:
            viol = industrial[~condition]
            expl = f"{len(viol)} industrial sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the park zone with an average noise level less than 60 decibels."""
    park = df[df["zone"] == "park"]
    if park.empty:
        truth = False
        expl = "No sensors in park zone."
    else:
        condition = park["noise_db"] < 60
        truth = condition.any()
        if truth:
            expl = f"At least one of {len(park)} park sensors has noise < 60 dB."
        else:
            expl = f"No park sensors have noise < 60 dB (all >= 60 dB)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with an average particulate matter 2.5 level greater than 30 have a power usage less than or equal to 433.6 kilowatt-hours."""
    high_pm25 = df[df["pm25"] > 30]
    if high_pm25.empty:
        truth = True
        expl = "No sensors with pm25 > 30."
    else:
        condition = high_pm25["power_use_kwh"] <= 433.6
        truth = condition.all()
        if truth:
            expl = f"All {len(high_pm25)} sensors with pm25 > 30 have power use <= 433.6 kWh."
        else:
            viol = high_pm25[~condition]
            expl = f"{len(viol)} sensors with pm25 > 30 violate the rule (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a sensor is in the downtown zone, then its foot traffic is greater than or equal to 439."""
    downtown = df[df["zone"] == "downtown"]
    if downtown.empty:
        truth = True
        expl = "No sensors in downtown zone."
    else:
        condition = downtown["foot_traffic"] >= 439
        truth = condition.all()
        if truth:
            expl = f"All {len(downtown)} downtown sensors have foot traffic >= 439."
        else:
            viol = downtown[~condition]
            expl = f"{len(viol)} downtown sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors have an average temperature between 20 and 25 degrees Celsius."""
    condition = df["avg_temp_c"].between(20, 25, inclusive="both")
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} sensors have avg temp between 20 and 25°C (more than half)."
    else:
        expl = f"{count} out of {total} sensors have avg temp between 20 and 25°C (not more than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average humidity less than 50 percent are in the park or downtown zone."""
    low_humid = df[df["avg_humidity"] < 50]
    if low_humid.empty:
        truth = True
        expl = "No sensors with avg humidity < 50%."
    else:
        valid_zones = ["park", "downtown"]
        condition = low_humid["zone"].isin(valid_zones)
        truth = condition.all()
        if truth:
            expl = f"All {len(low_humid)} sensors with humidity < 50% are in park or downtown zones."
        else:
            viol = low_humid[~condition]
            expl = f"{len(viol)} sensors with humidity < 50% are not in park or downtown zones (zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a sensor is in the residential zone, then its average noise level is greater than or equal to 43.4 decibels."""
    residential = df[df["zone"] == "residential"]
    if residential.empty:
        truth = True
        expl = "No sensors in residential zone."
    else:
        condition = residential["noise_db"] >= 43.4
        truth = condition.all()
        if truth:
            expl = f"All {len(residential)} residential sensors have noise >= 43.4 dB."
        else:
            viol = residential[~condition]
            expl = f"{len(viol)} residential sensors violate the rule (noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the industrial zone with an average particulate matter 2.5 level greater than 20."""
    industrial = df[df["zone"] == "industrial"]
    if industrial.empty:
        truth = False
        expl = "No sensors in industrial zone."
    else:
        condition = industrial["pm25"] > 20
        truth = condition.any()
        if truth:
            expl = f"At least one of {len(industrial)} industrial sensors has pm25 > 20."
        else:
            expl = f"No industrial sensors have pm25 > 20 (all <= 20)."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All sensors with a power usage greater than 400 kilowatt-hours are in the residential or industrial zone."""
    high_power = df[df["power_use_kwh"] > 400]
    if high_power.empty:
        truth = True
        expl = "No sensors with power use > 400 kWh."
    else:
        valid_zones = ["residential", "industrial"]
        condition = high_power["zone"].isin(valid_zones)
        truth = condition.all()
        if truth:
            expl = f"All {len(high_power)} sensors with power use > 400 kWh are in residential or industrial zones."
        else:
            viol = high_power[~condition]
            expl = f"{len(viol)} sensors with power use > 400 kWh are not in residential or industrial zones (zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a sensor is in the park zone, then its foot traffic is less than or equal to 1237."""
    park = df[df["zone"] == "park"]
    if park.empty:
        truth = True
        expl = "No sensors in park zone."
    else:
        condition = park["foot_traffic"] <= 1237
        truth = condition.all()
        if truth:
            expl = f"All {len(park)} park sensors have foot traffic <= 1237."
        else:
            viol = park[~condition]
            expl = f"{len(viol)} park sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most sensors have an average particulate matter 2.5 level between 10 and 35."""
    condition = df["pm25"].between(10, 35, inclusive="both")
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} sensors have pm25 between 10 and 35 (more than half)."
    else:
        expl = f"{count} out of {total} sensors have pm25 between 10 and 35 (not more than half)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All sensors with an average temperature greater than 25 degrees Celsius are in the park zone."""
    high_temp = df[df["avg_temp_c"] > 25]
    if high_temp.empty:
        truth = True
        expl = "No sensors with avg temp > 25°C."
    else:
        condition = high_temp["zone"] == "park"
        truth = condition.all()
        if truth:
            expl = f"All {len(high_temp)} sensors with avg temp > 25°C are in park zone."
        else:
            viol = high_temp[~condition]
            expl = f"{len(viol)} sensors with avg temp > 25°C are not in park zone (zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a sensor is in the downtown zone, then its average humidity is between 49.6 and 65.3 percent."""
    downtown = df[df["zone"] == "downtown"]
    if downtown.empty:
        truth = True
        expl = "No sensors in downtown zone."
    else:
        condition = downtown["avg_humidity"].between(49.6, 65.3, inclusive="both")
        truth = condition.all()
        if truth:
            expl = f"All {len(downtown)} downtown sensors have avg humidity between 49.6 and 65.3%."
        else:
            viol = downtown[~condition]
            expl = f"{len(viol)} downtown sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one sensor in the residential zone with an average noise level less than 60 decibels."""
    residential = df[df["zone"] == "residential"]
    if residential.empty:
        truth = False
        expl = "No sensors in residential zone."
    else:
        condition = residential["noise_db"] < 60
        truth = condition.any()
        if truth:
            expl = f"At least one of {len(residential)} residential sensors has noise < 60 dB."
        else:
            expl = f"No residential sensors have noise < 60 dB (all >= 60 dB)."
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
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()