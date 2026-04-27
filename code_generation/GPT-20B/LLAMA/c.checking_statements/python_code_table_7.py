import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the downtown zone have an average temperature between 21.8 and 25.4 degrees Celsius."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["avg_temp_c"].between(21.8, 25.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors satisfy the temperature range."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the residential zone have an average humidity between 53.7 and 63.0%."""
    residential = df[df["zone"] == "residential"]
    condition = residential["avg_humidity"].between(53.7, 63.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors satisfy the humidity range."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the industrial zone, then its noise level is greater than 61.2 decibels."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["noise_db"] > 61.2
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have noise > 61.2 dB."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (noise: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the park zone with a PM2.5 level greater than 32.0."""
    park = df[df["zone"] == "park"]
    exists = (park["pm25"] > 32.0).any()
    if exists:
        viol = park[park["pm25"] > 32.0]
        expl = f"Found {len(viol)} park sensors with PM2.5 > 32.0 (IDs: {', '.join(viol['sensor_id'])})."
    else:
        expl = "No park sensor has PM2.5 > 32.0."
    return exists, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with foot traffic greater than 1000 have a power use less than or equal to 305.3 kWh."""
    high_ft = df[df["foot_traffic"] > 1000]
    condition = high_ft["power_use_kwh"] <= 305.3
    truth = condition.all()
    if truth:
        expl = f"All {len(high_ft)} high foot-traffic sensors satisfy power use ≤ 305.3 kWh."
    else:
        viol = high_ft[~condition]
        expl = f"{len(viol)} high foot-traffic sensors violate the rule (power: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a sensor is in the downtown zone, then its foot traffic is greater than 525."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["foot_traffic"] > 525
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot traffic > 525."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors in the industrial zone have an average temperature greater than 22.0 degrees Celsius."""
    industrial = df[df["zone"] == "industrial"]
    if len(industrial) == 0:
        return True, "No industrial sensors; statement vacuously true."
    count_gt = (industrial["avg_temp_c"] > 22.0).sum()
    truth = count_gt > len(industrial) / 2
    if truth:
        expl = f"{count_gt}/{len(industrial)} industrial sensors have avg_temp > 22.0."
    else:
        expl = f"Only {count_gt}/{len(industrial)} industrial sensors have avg_temp > 22.0."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average humidity less than 55.0% are in the park zone."""
    low_hum = df[df["avg_humidity"] < 55.0]
    condition = low_hum["zone"] == "park"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_hum)} low-humidity sensors are in the park zone."
    else:
        viol = low_hum[~condition]
        expl = f"{len(viol)} low-humidity sensors are not in the park zone (IDs: {', '.join(viol['sensor_id'])})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a sensor has a PM2.5 level less than 15.0, then it is in the residential zone."""
    low_pm = df[df["pm25"] < 15.0]
    condition = low_pm["zone"] == "residential"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_pm)} low PM2.5 sensors are in the residential zone."
    else:
        viol = low_pm[~condition]
        expl = f"{len(viol)} low PM2.5 sensors are not in residential zone (IDs: {', '.join(viol['sensor_id'])})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the downtown zone with a power use less than 200.0 kWh."""
    downtown = df[df["zone"] == "downtown"]
    exists = (downtown["power_use_kwh"] < 200.0).any()
    if exists:
        viol = downtown[downtown["power_use_kwh"] < 200.0]
        expl = f"Found {len(viol)} downtown sensors with power use < 200.0 kWh (IDs: {', '.join(viol['sensor_id'])})."
    else:
        expl = "No downtown sensor has power use < 200.0 kWh."
    return exists, expl

def stmt_11(df: pd.DataFrame):
    """11. All sensors with foot traffic less than 700 have a noise level greater than 60.0 decibels."""
    low_ft = df[df["foot_traffic"] < 700]
    condition = low_ft["noise_db"] > 60.0
    truth = condition.all()
    if truth:
        expl = f"All {len(low_ft)} low foot-traffic sensors have noise > 60.0 dB."
    else:
        viol = low_ft[~condition]
        expl = f"{len(viol)} low foot-traffic sensors violate the rule (noise: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a sensor is in the park zone, then its average temperature is between 21.2 and 26.0 degrees Celsius."""
    park = df[df["zone"] == "park"]
    condition = park["avg_temp_c"].between(21.2, 26.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg_temp between 21.2 and 26.0."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most sensors in the downtown zone have a PM2.5 level greater than 20.0."""
    downtown = df[df["zone"] == "downtown"]
    if len(downtown) == 0:
        return True, "No downtown sensors; statement vacuously true."
    count_gt = (downtown["pm25"] > 20.0).sum()
    truth = count_gt > len(downtown) / 2
    if truth:
        expl = f"{count_gt}/{len(downtown)} downtown sensors have PM2.5 > 20.0."
    else:
        expl = f"Only {count_gt}/{len(downtown)} downtown sensors have PM2.5 > 20.0."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All sensors with an average temperature greater than 25.0 degrees Celsius are in the downtown or industrial zones."""
    high_temp = df[df["avg_temp_c"] > 25.0]
    condition = high_temp["zone"].isin(["downtown", "industrial"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_temp)} high-temp sensors are in downtown or industrial zones."
    else:
        viol = high_temp[~condition]
        expl = f"{len(viol)} high-temp sensors are not in downtown/industrial (IDs: {', '.join(viol['sensor_id'])})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a sensor has a power use greater than 300.0 kWh, then it is in the residential or park zones."""
    high_power = df[df["power_use_kwh"] > 300.0]
    condition = high_power["zone"].isin(["residential", "park"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_power)} high-power sensors are in residential or park zones."
    else:
        viol = high_power[~condition]
        expl = f"{len(viol)} high-power sensors are not in residential/park (IDs: {', '.join(viol['sensor_id'])})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one sensor in the industrial zone with a foot traffic less than 700."""
    industrial = df[df["zone"] == "industrial"]
    exists = (industrial["foot_traffic"] < 700).any()
    if exists:
        viol = industrial[industrial["foot_traffic"] < 700]
        expl = f"Found {len(viol)} industrial sensors with foot traffic < 700 (IDs: {', '.join(viol['sensor_id'])})."
    else:
        expl = "No industrial sensor has foot traffic < 700."
    return exists, expl

def stmt_17(df: pd.DataFrame):
    """17. All sensors with a noise level less than 50.0 decibels are in the residential zone."""
    low_noise = df[df["noise_db"] < 50.0]
    condition = low_noise["zone"] == "residential"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_noise)} low-noise sensors are in the residential zone."
    else:
        viol = low_noise[~condition]
        expl = f"{len(viol)} low-noise sensors are not in residential zone (IDs: {', '.join(viol['sensor_id'])})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a sensor is in the park zone, then its average humidity is between 50.2 and 57.9%."""
    park = df[df["zone"] == "park"]
    condition = park["avg_humidity"].between(50.2, 57.9, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg_humidity between 50.2 and 57.9."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. Most sensors in the residential zone have an average temperature less than 25.0 degrees Celsius."""
    residential = df[df["zone"] == "residential"]
    if len(residential) == 0:
        return True, "No residential sensors; statement vacuously true."
    count_lt = (residential["avg_temp_c"] < 25.0).sum()
    truth = count_lt > len(residential) / 2
    if truth:
        expl = f"{count_lt}/{len(residential)} residential sensors have avg_temp < 25.0."
    else:
        expl = f"Only {count_lt}/{len(residential)} residential sensors have avg_temp < 25.0."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_7.csv")

    # Convert numeric columns safely
    for col in ["avg_temp_c", "avg_humidity", "pm25", "noise_db", "foot_traffic", "power_use_kwh"]:
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()