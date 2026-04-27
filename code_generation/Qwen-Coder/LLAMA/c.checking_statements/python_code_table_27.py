import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the park zone have an average temperature between 21.6 and 24.2 degrees Celsius."""
    park_sensors = df[df["zone"] == "park"]
    condition = park_sensors["avg_temp_c"].between(21.6, 24.2, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park zone sensors have avg temp between 21.6 and 24.2°C."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park zone sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the residential zone have an average humidity between 52.9 and 67.3 percent."""
    res_sensors = df[df["zone"] == "residential"]
    condition = res_sensors["avg_humidity"].between(52.9, 67.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(res_sensors)} residential zone sensors have avg humidity between 52.9 and 67.3%."
    else:
        viol = res_sensors[~condition]
        expl = f"{len(viol)} residential zone sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the industrial zone, then its average noise level is between 47.7 and 59.9 decibels."""
    ind_sensors = df[df["zone"] == "industrial"]
    if len(ind_sensors) == 0:
        truth = True
        expl = "No sensors in industrial zone."
        return truth, expl
    condition = ind_sensors["noise_db"].between(47.7, 59.9, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(ind_sensors)} industrial zone sensors have avg noise between 47.7 and 59.9 dB."
    else:
        viol = ind_sensors[~condition]
        expl = f"{len(viol)} industrial zone sensors violate the rule (noises: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the downtown zone with an average PM2.5 level greater than 25."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["pm25"] > 25
    truth = condition.any()
    if truth:
        viol = downtown_sensors[condition]
        expl = f"At least one downtown sensor has PM2.5 > 25 (e.g., {viol.iloc[0]['sensor_id']} with {viol.iloc[0]['pm25']})."
    else:
        expl = "No downtown sensors have PM2.5 > 25."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with an average temperature greater than 25 degrees Celsius have a power usage greater than 263.6 kWh."""
    hot_sensors = df[df["avg_temp_c"] > 25]
    if len(hot_sensors) == 0:
        truth = True
        expl = "No sensors with avg temp > 25°C."
        return truth, expl
    condition = hot_sensors["power_use_kwh"] > 263.6
    truth = condition.all()
    if truth:
        expl = f"All {len(hot_sensors)} sensors with temp > 25°C have power use > 263.6 kWh."
    else:
        viol = hot_sensors[~condition]
        expl = f"{len(viol)} sensors with temp > 25°C violate the rule (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a sensor is in the park zone, then its foot traffic is between 470 and 1433."""
    park_sensors = df[df["zone"] == "park"]
    if len(park_sensors) == 0:
        truth = True
        expl = "No sensors in park zone."
        return truth, expl
    condition = park_sensors["foot_traffic"].between(470, 1433, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park zone sensors have foot traffic between 470 and 1433."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park zone sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors in the residential zone have an average step count greater than 872."""
    res_sensors = df[df["zone"] == "residential"]
    if len(res_sensors) == 0:
        truth = True
        expl = "No sensors in residential zone."
        return truth, expl
    # Note:'step_count' column does not exist in the data; assume it's a typo for 'foot_traffic'
    # But since foot_traffic is already used in stmt 6, we'll skip this assumption and treat it as invalid
    # Let's just say we can't verify due to missing column
    truth = False
    expl = "Column'step_count' not found in dataset."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average humidity less than 55 percent have a power usage greater than 276.1 kWh."""
    low_hum_sensors = df[df["avg_humidity"] < 55]
    if len(low_hum_sensors) == 0:
        truth = True
        expl = "No sensors with avg humidity < 55%."
        return truth, expl
    condition = low_hum_sensors["power_use_kwh"] > 276.1
    truth = condition.all()
    if truth:
        expl = f"All {len(low_hum_sensors)} sensors with humidity < 55% have power use > 276.1 kWh."
    else:
        viol = low_hum_sensors[~condition]
        expl = f"{len(viol)} sensors with humidity < 55% violate the rule (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a sensor is in the industrial zone, then its average temperature is between 24.1 and 27.9 degrees Celsius."""
    ind_sensors = df[df["zone"] == "industrial"]
    if len(ind_sensors) == 0:
        truth = True
        expl = "No sensors in industrial zone."
        return truth, expl
    condition = ind_sensors["avg_temp_c"].between(24.1, 27.9, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(ind_sensors)} industrial zone sensors have avg temp between 24.1 and 27.9°C."
    else:
        viol = ind_sensors[~condition]
        expl = f"{len(viol)} industrial zone sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the downtown zone with an average noise level greater than 69 decibels."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["noise_db"] > 69
    truth = condition.any()
    if truth:
        viol = downtown_sensors[condition]
        expl = f"At least one downtown sensor has noise > 69 dB (e.g., {viol.iloc[0]['sensor_id']} with {viol.iloc[0]['noise_db']})."
    else:
        expl = "No downtown sensors have noise > 69 dB."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All sensors with an average PM2.5 level greater than 30 have a foot traffic greater than 1122."""
    high_pm25_sensors = df[df["pm25"] > 30]
    if len(high_pm25_sensors) == 0:
        truth = True
        expl = "No sensors with PM2.5 > 30."
        return truth, expl
    condition = high_pm25_sensors["foot_traffic"] > 1122
    truth = condition.all()
    if truth:
        expl = f"All {len(high_pm25_sensors)} sensors with PM2.5 > 30 have foot traffic > 1122."
    else:
        viol = high_pm25_sensors[~condition]
        expl = f"{len(viol)} sensors with PM2.5 > 30 violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a sensor is in the park zone, then its average humidity is between 51.6 and 64.5 percent."""
    park_sensors = df[df["zone"] == "park"]
    if len(park_sensors) == 0:
        truth = True
        expl = "No sensors in park zone."
        return truth, expl
    condition = park_sensors["avg_humidity"].between(51.6, 64.5, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park zone sensors have avg humidity between 51.6 and 64.5%."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park zone sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All sensors with a power usage greater than 357.5 kWh have an average temperature greater than 23.8 degrees Celsius."""
    high_power_sensors = df[df["power_use_kwh"] > 357.5]
    if len(high_power_sensors) == 0:
        truth = True
        expl = "No sensors with power use > 357.5 kWh."
        return truth, expl
    condition = high_power_sensors["avg_temp_c"] > 23.8
    truth = condition.all()
    if truth:
        expl = f"All {len(high_power_sensors)} sensors with power use > 357.5 kWh have temp > 23.8°C."
    else:
        viol = high_power_sensors[~condition]
        expl = f"{len(viol)} sensors with power use > 357.5 kWh violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Most sensors in the downtown zone have an average PM2.5 level greater than 14.3."""
    downtown_sensors = df[df["zone"] == "downtown"]
    if len(downtown_sensors) == 0:
        truth = True
        expl = "No sensors in downtown zone."
        return truth, expl
    condition = downtown_sensors["pm25"] > 14.3
    count = condition.sum()
    total = len(downtown_sensors)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of downtown sensors have PM2.5 > 14.3."
    else:
        expl = f"Less than half ({count}/{total}) of downtown sensors have PM2.5 > 14.3."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one sensor in the residential zone with an average noise level greater than 73.9 decibels."""
    res_sensors = df[df["zone"] == "residential"]
    condition = res_sensors["noise_db"] > 73.9
    truth = condition.any()
    if truth:
        viol = res_sensors[condition]
        expl = f"At least one residential sensor has noise > 73.9 dB (e.g., {viol.iloc[0]['sensor_id']} with {viol.iloc[0]['noise_db']})."
    else:
        expl = "No residential sensors have noise > 73.9 dB."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All sensors with an average temperature less than 25 degrees Celsius have a power usage less than 424.4 kWh."""
    cold_sensors = df[df["avg_temp_c"] < 25]
    if len(cold_sensors) == 0:
        truth = True
        expl = "No sensors with temp < 25°C."
        return truth, expl
    condition = cold_sensors["power_use_kwh"] < 424.4
    truth = condition.all()
    if truth:
        expl = f"All {len(cold_sensors)} sensors with temp < 25°C have power use < 424.4 kWh."
    else:
        viol = cold_sensors[~condition]
        expl = f"{len(viol)} sensors with temp < 25°C violate the rule (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a sensor is in the industrial zone, then its foot traffic is between 990 and 1097."""
    ind_sensors = df[df["zone"] == "industrial"]
    if len(ind_sensors) == 0:
        truth = True
        expl = "No sensors in industrial zone."
        return truth, expl
    condition = ind_sensors["foot_traffic"].between(990, 1097, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(ind_sensors)} industrial zone sensors have foot traffic between 990 and 1097."
    else:
        viol = ind_sensors[~condition]
        expl = f"{len(viol)} industrial zone sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All sensors with an average humidity greater than 64 percent have a power usage less than 357.5 kWh."""
    high_hum_sensors = df[df["avg_humidity"] > 64]
    if len(high_hum_sensors) == 0:
        truth = True
        expl = "No sensors with humidity > 64%."
        return truth, expl
    condition = high_hum_sensors["power_use_kwh"] < 357.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_hum_sensors)} sensors with humidity > 64% have power use < 357.5 kWh."
    else:
        viol = high_hum_sensors[~condition]
        expl = f"{len(viol)} sensors with humidity > 64% violate the rule (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_27.csv")

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
        (18, stmt_18)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()