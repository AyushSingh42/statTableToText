import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the industrial zone have an average temperature between 22.4 and 27.7 degrees Celsius."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["avg_temp_c"].between(22.4, 27.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg temp between 22.4 and 27.7°C."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all sensors in the park zone, the average humidity is between 58.8 and 67.3 percent."""
    park = df[df["zone"] == "park"]
    condition = park["avg_humidity"].between(58.8, 67.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg humidity between 58.8 and 67.3%."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the downtown zone, then its foot traffic is greater than 1000."""
    downtown = df[df["zone"] == "downtown"]
    if len(downtown) == 0:
        return True, "No sensors in downtown zone."
    condition = downtown["foot_traffic"] > 1000
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot traffic > 1000."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All sensors in the residential zone have a power use less than or equal to 384.1 kWh."""
    residential = df[df["zone"] == "residential"]
    condition = residential["power_use_kwh"] <= 384.1
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have power use <= 384.1 kWh."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (power use: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. There exists at least one sensor in the park zone with a noise level greater than 70 dB."""
    park = df[df["zone"] == "park"]
    condition = park["noise_db"] > 70
    truth = condition.any()
    if truth:
        found = park[condition]
        expl = f"At least one park sensor has noise > 70 dB ({found.iloc[0]['noise_db']} dB)."
    else:
        expl = "No park sensors have noise > 70 dB."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all sensors with an average temperature greater than 25 degrees Celsius, the average humidity is less than 65 percent."""
    hot = df[df["avg_temp_c"] > 25]
    if len(hot) == 0:
        return True, "No sensors with avg temp > 25°C."
    condition = hot["avg_humidity"] < 65
    truth = condition.all()
    if truth:
        expl = f"All {len(hot)} hot sensors have avg humidity < 65%."
    else:
        viol = hot[~condition]
        expl = f"{len(viol)} hot sensors violate the rule (humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a sensor is in the industrial zone, then its PM2.5 level is greater than 15."""
    industrial = df[df["zone"] == "industrial"]
    if len(industrial) == 0:
        return True, "No sensors in industrial zone."
    condition = industrial["pm25"] > 15
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have PM2.5 > 15."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (PM2.5: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most sensors in the park zone have an average step count greater than 700."""
    # Note: No'step_count' column in dataset; assume it's a typo or missing data.
    # We'll skip this statement since it cannot be evaluated.
    return None, "Missing'step_count' column."

def stmt_9(df: pd.DataFrame):
    """9. All sensors with a foot traffic greater than 1000 have a power use less than or equal to 396.4 kWh."""
    busy = df[df["foot_traffic"] > 1000]
    if len(busy) == 0:
        return True, "No sensors with foot traffic > 1000."
    condition = busy["power_use_kwh"] <= 396.4
    truth = condition.all()
    if truth:
        expl = f"All {len(busy)} busy sensors have power use <= 396.4 kWh."
    else:
        viol = busy[~condition]
        expl = f"{len(viol)} busy sensors violate the rule (power use: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a sensor is in the residential zone, then its average temperature is between 21 and 28 degrees Celsius."""
    residential = df[df["zone"] == "residential"]
    if len(residential) == 0:
        return True, "No sensors in residential zone."
    condition = residential["avg_temp_c"].between(21, 28, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have avg temp between 21 and 28°C."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. There exists at least one sensor in the industrial zone with a noise level less than 60 dB."""
    industrial = df[df["zone"] == "industrial"]
    condition = industrial["noise_db"] < 60
    truth = condition.any()
    if truth:
        found = industrial[condition]
        expl = f"At least one industrial sensor has noise < 60 dB ({found.iloc[0]['noise_db']} dB)."
    else:
        expl = "No industrial sensors have noise < 60 dB."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all sensors with an average humidity greater than 60 percent, the average temperature is less than 28 degrees Celsius."""
    humid = df[df["avg_humidity"] > 60]
    if len(humid) == 0:
        return True, "No sensors with avg humidity > 60%."
    condition = humid["avg_temp_c"] < 28
    truth = condition.all()
    if truth:
        expl = f"All {len(humid)} humid sensors have avg temp < 28°C."
    else:
        viol = humid[~condition]
        expl = f"{len(viol)} humid sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All sensors in the downtown zone have a foot traffic greater than 1000."""
    downtown = df[df["zone"] == "downtown"]
    if len(downtown) == 0:
        return True, "No sensors in downtown zone."
    condition = downtown["foot_traffic"] > 1000
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot traffic > 1000."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a sensor is in the park zone, then its PM2.5 level is less than 35."""
    park = df[df["zone"] == "park"]
    if len(park) == 0:
        return True, "No sensors in park zone."
    condition = park["pm25"] < 35
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have PM2.5 < 35."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (PM2.5: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most sensors in the industrial zone have a power use greater than 200 kWh."""
    industrial = df[df["zone"] == "industrial"]
    if len(industrial) == 0:
        return True, "No sensors in industrial zone."
    condition = industrial["power_use_kwh"] > 200
    count = condition.sum()
    total = len(industrial)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of industrial sensors have power use > 200 kWh."
    else:
        expl = f"Less than half ({count}/{total}) of industrial sensors have power use > 200 kWh."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All sensors with a power use greater than 300 kWh have an average temperature greater than 24 degrees Celsius."""
    high_power = df[df["power_use_kwh"] > 300]
    if len(high_power) == 0:
        return True, "No sensors with power use > 300 kWh."
    condition = high_power["avg_temp_c"] > 24
    truth = condition.all()
    if truth:
        expl = f"All {len(high_power)} high-power sensors have avg temp > 24°C."
    else:
        viol = high_power[~condition]
        expl = f"{len(viol)} high-power sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a sensor is in the residential zone, then its average humidity is between 51 and 67 percent."""
    residential = df[df["zone"] == "residential"]
    if len(residential) == 0:
        return True, "No sensors in residential zone."
    condition = residential["avg_humidity"].between(51, 67, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have avg humidity between 51 and 67%."
    else:
        viol = residential[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. There exists at least one sensor in the park zone with an average temperature greater than 28 degrees Celsius."""
    park = df[df["zone"] == "park"]
    condition = park["avg_temp_c"] > 28
    truth = condition.any()
    if truth:
        found = park[condition]
        expl = f"At least one park sensor has avg temp > 28°C ({found.iloc[0]['avg_temp_c']}°C)."
    else:
        expl = "No park sensors have avg temp > 28°C."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. For all sensors with a foot traffic less than 500, the average humidity is greater than 60 percent."""
    low_foot = df[df["foot_traffic"] < 500]
    if len(low_foot) == 0:
        return True, "No sensors with foot traffic < 500."
    condition = low_foot["avg_humidity"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(low_foot)} low-foot sensors have avg humidity > 60%."
    else:
        viol = low_foot[~condition]
        expl = f"{len(viol)} low-foot sensors violate the rule (humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. All sensors in the industrial zone have a noise level greater than 48 dB."""
    industrial = df[df["zone"] == "industrial"]
    if len(industrial) == 0:
        return True, "No sensors in industrial zone."
    condition = industrial["noise_db"] > 48
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have noise > 48 dB."
    else:
        viol = industrial[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (noise: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. If a sensor is in the downtown zone, then its average humidity is between 59 and 60 percent."""
    downtown = df[df["zone"] == "downtown"]
    if len(downtown) == 0:
        return True, "No sensors in downtown zone."
    condition = downtown["avg_humidity"].between(59, 60, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have avg humidity between 59 and 60%."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. Most sensors in the park zone have an average temperature between 24 and 28 degrees Celsius."""
    park = df[df["zone"] == "park"]
    if len(park) == 0:
        return True, "No sensors in park zone."
    condition = park["avg_temp_c"].between(24, 28, inclusive="both")
    count = condition.sum()
    total = len(park)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of park sensors have avg temp between 24 and 28°C."
    else:
        expl = f"Less than half ({count}/{total}) of park sensors have avg temp between 24 and 28°C."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_47.csv")

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
        (16, stmt_16),
        (17, stmt_17),
        (18, stmt_18),
        (19, stmt_19),
        (20, stmt_20),
        (21, stmt_21),
        (22, stmt_22)
    ]

    for num, func in checks:
        if func is None:
            continue
        truth, explanation = func(df)
        if truth is None:
            print(f"\nStatement {num}: SKIPPED")
            print(f"  - {func.__doc__.strip()}")
            print(f"  - Explanation: {explanation}")
        else:
            print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()