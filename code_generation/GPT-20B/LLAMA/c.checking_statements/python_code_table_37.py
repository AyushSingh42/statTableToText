import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the industrial zone have an average temperature between 21.6 and 26.7 degrees Celsius."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_temp_c"].between(21.6, 26.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors satisfy the temperature range."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the range (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the park zone have an average humidity between 53.9 and 61.8 percent."""
    park = df[df["zone"] == "park"]
    condition = park["avg_humidity"].between(53.9, 61.8, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors satisfy the humidity range."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the range (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the downtown zone, then its average PM2.5 level is greater than 10.9."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["pm25"] > 10.9
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have pm25 > 10.9."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (pm25: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the residential zone with an average noise level greater than 70 decibels."""
    residential = df[df["zone"] == "residential"]
    exists = (residential["noise_db"] > 70).any()
    if exists:
        viol = residential[residential["noise_db"] > 70]
        expl = f"Found {len(viol)} residential sensors with noise > 70 dB (ids: {', '.join(map(str, viol['sensor_id'].tolist()))})."
    else:
        expl = "No residential sensor has noise > 70 dB."
    return exists, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with foot traffic greater than 1200 have a power use greater than 250 kWh."""
    high_ft = df[df["foot_traffic"] > 1200]
    condition = high_ft["power_use_kwh"] > 250
    truth = condition.all()
    if truth:
        expl = f"All {len(high_ft)} high foot-traffic sensors have power use > 250 kWh."
    else:
        viol = high_ft[~condition]
        expl = f"{len(viol)} sensors violate the rule (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a sensor has an average humidity less than 55 percent, then it is in the park or residential zone."""
    low_hum = df[df["avg_humidity"] < 55]
    condition = low_hum["zone"].isin(["park", "residential"])
    truth = condition.all()
    if truth:
        expl = f"All {len(low_hum)} low-humidity sensors are in park or residential zones."
    else:
        viol = low_hum[~condition]
        expl = f"{len(viol)} low-humidity sensors are not in park or residential (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors in the industrial zone have an average temperature greater than 24 degrees Celsius."""
    industrial = df[df["zone"] == "industrial"]
    if len(industrial) == 0:
        return True, "No industrial sensors to evaluate; statement considered true."
    count_gt = (industrial["avg_temp_c"] > 24).sum()
    truth = count_gt > len(industrial) / 2
    if truth:
        expl = f"{count_gt}/{len(industrial)} industrial sensors have temp > 24°C."
    else:
        expl = f"Only {count_gt}/{len(industrial)} industrial sensors have temp > 24°C."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average temperature greater than 26 degrees Celsius are in the park or industrial zone."""
    high_temp = df[df["avg_temp_c"] > 26]
    condition = high_temp["zone"].isin(["park", "industrial"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_temp)} high-temp sensors are in park or industrial zones."
    else:
        viol = high_temp[~condition]
        expl = f"{len(viol)} high-temp sensors are not in park or industrial (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a sensor is in the park zone, then its average noise level is less than 75 decibels."""
    park = df[df["zone"] == "park"]
    condition = park["noise_db"] < 75
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have noise < 75 dB."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (noise: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the downtown zone with an average PM2.5 level greater than 30."""
    downtown = df[df["zone"] == "downtown"]
    exists = (downtown["pm25"] > 30).any()
    if exists:
        viol = downtown[downtown["pm25"] > 30]
        expl = f"Found {len(viol)} downtown sensors with pm25 > 30 (ids: {', '.join(map(str, viol['sensor_id'].tolist()))})."
    else:
        expl = "No downtown sensor has pm25 > 30."
    return exists, expl

def stmt_11(df: pd.DataFrame):
    """11. All sensors with foot traffic less than 600 have a power use less than 250 kWh."""
    low_ft = df[df["foot_traffic"] < 600]
    condition = low_ft["power_use_kwh"] < 250
    truth = condition.all()
    if truth:
        expl = f"All {len(low_ft)} low foot-traffic sensors have power use < 250 kWh."
    else:
        viol = low_ft[~condition]
        expl = f"{len(viol)} sensors violate the rule (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a sensor has an average temperature less than 23 degrees Celsius, then it is in the residential or industrial zone."""
    low_temp = df[df["avg_temp_c"] < 23]
    condition = low_temp["zone"].isin(["residential", "industrial"])
    truth = condition.all()
    if truth:
        expl = f"All {len(low_temp)} low-temp sensors are in residential or industrial zones."
    else:
        viol = low_temp[~condition]
        expl = f"{len(viol)} low-temp sensors are not in residential or industrial (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most sensors in the residential zone have an average humidity greater than 55 percent."""
    residential = df[df["zone"] == "residential"]
    if len(residential) == 0:
        return True, "No residential sensors to evaluate; statement considered true."
    count_gt = (residential["avg_humidity"] > 55).sum()
    truth = count_gt > len(residential) / 2
    if truth:
        expl = f"{count_gt}/{len(residential)} residential sensors have humidity > 55%."
    else:
        expl = f"Only {count_gt}/{len(residential)} residential sensors have humidity > 55%."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All sensors with an average noise level greater than 65 decibels are in the industrial or residential zone."""
    high_noise = df[df["noise_db"] > 65]
    condition = high_noise["zone"].isin(["industrial", "residential"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_noise)} high-noise sensors are in industrial or residential zones."
    else:
        viol = high_noise[~condition]
        expl = f"{len(viol)} high-noise sensors are not in industrial or residential (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a sensor is in the industrial zone, then its average PM2.5 level is greater than 15."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["pm25"] > 15
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have pm25 > 15."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (pm25: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one sensor in the park zone with an average temperature greater than 27 degrees Celsius."""
    park = df[df["zone"] == "park"]
    exists = (park["avg_temp_c"] > 27).any()
    if exists:
        viol = park[park["avg_temp_c"] > 27]
        expl = f"Found {len(viol)} park sensors with temp > 27°C (ids: {', '.join(map(str, viol['sensor_id'].tolist()))})."
    else:
        expl = "No park sensor has temp > 27°C."
    return exists, expl

def stmt_17(df: pd.DataFrame):
    """17. All sensors with foot traffic greater than 1000 have an average temperature greater than 24 degrees Celsius."""
    high_ft = df[df["foot_traffic"] > 1000]
    condition = high_ft["avg_temp_c"] > 24
    truth = condition.all()
    if truth:
        expl = f"All {len(high_ft)} high foot-traffic sensors have temp > 24°C."
    else:
        viol = high_ft[~condition]
        expl = f"{len(viol)} sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a sensor has an average humidity greater than 60 percent, then it is in the industrial or residential zone."""
    high_hum = df[df["avg_humidity"] > 60]
    condition = high_hum["zone"].isin(["industrial", "residential"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_hum)} high-humidity sensors are in industrial or residential zones."
    else:
        viol = high_hum[~condition]
        expl = f"{len(viol)} high-humidity sensors are not in industrial or residential (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. Most sensors in the downtown zone have an average PM2.5 level greater than 15."""
    downtown = df[df["zone"] == "downtown"]
    if len(downtown) == 0:
        return True, "No downtown sensors to evaluate; statement considered true."
    count_gt = (downtown["pm25"] > 15).sum()
    truth = count_gt > len(downtown) / 2
    if truth:
        expl = f"{count_gt}/{len(downtown)} downtown sensors have pm25 > 15."
    else:
        expl = f"Only {count_gt}/{len(downtown)} downtown sensors have pm25 > 15."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. All sensors with an average temperature less than 25 degrees Celsius are in the residential or downtown zone."""
    low_temp = df[df["avg_temp_c"] < 25]
    condition = low_temp["zone"].isin(["residential", "downtown"])
    truth = condition.all()
    if truth:
        expl = f"All {len(low_temp)} low-temp sensors are in residential or downtown zones."
    else:
        viol = low_temp[~condition]
        expl = f"{len(viol)} low-temp sensors are not in residential or downtown (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_37.csv")

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
        (17, stmt_17),
        (18, stmt_18),
        (19, stmt_19),
        (20, stmt_20),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()