import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the downtown zone have an average temperature greater than 21°C."""
    downtown_sensors = df[df["zone"] == "downtown"]
    if downtown_sensors.empty:
        truth = True
        expl = "No sensors in downtown zone."
    else:
        condition = downtown_sensors["avg_temp_c"] > 21
        truth = condition.all()
        if truth:
            expl = f"All {len(downtown_sensors)} downtown sensors have avg temp > 21°C."
        else:
            viol = downtown_sensors[~condition]
            expl = f"{len(viol)} downtown sensors violate (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the industrial zone have an average humidity greater than 65%."""
    industrial_sensors = df[df["zone"] == "industrial"]
    if industrial_sensors.empty:
        truth = True
        expl = "No sensors in industrial zone."
    else:
        condition = industrial_sensors["avg_humidity"] > 65
        truth = condition.all()
        if truth:
            expl = f"All {len(industrial_sensors)} industrial sensors have avg humidity > 65%."
        else:
            viol = industrial_sensors[~condition]
            expl = f"{len(viol)} industrial sensors violate (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the residential zone, then its average noise level is greater than 64 dB."""
    residential_sensors = df[df["zone"] == "residential"]
    if residential_sensors.empty:
        truth = True
        expl = "No sensors in residential zone."
    else:
        condition = residential_sensors["noise_db"] > 64
        truth = condition.all()
        if truth:
            expl = f"All {len(residential_sensors)} residential sensors have avg noise > 64 dB."
        else:
            viol = residential_sensors[~condition]
            expl = f"{len(viol)} residential sensors violate (noises: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the park zone with an average PM2.5 level less than 20."""
    park_sensors = df[df["zone"] == "park"]
    if park_sensors.empty:
        truth = False
        expl = "No sensors in park zone."
    else:
        condition = park_sensors["pm25"] < 20
        truth = condition.any()
        if truth:
            found = park_sensors[condition]
            expl = f"At least one park sensor has PM2.5 < 20 ({found.iloc[0]['sensor_id']}, {found.iloc[0]['pm25']})."
        else:
            expl = f"No park sensors have PM2.5 < 20."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with an average temperature less than 24°C have a foot traffic greater than 1000."""
    low_temp_sensors = df[df["avg_temp_c"] < 24]
    if low_temp_sensors.empty:
        truth = True
        expl = "No sensors with avg temp < 24°C."
    else:
        condition = low_temp_sensors["foot_traffic"] > 1000
        truth = condition.all()
        if truth:
            expl = f"All {len(low_temp_sensors)} low-temp sensors have foot traffic > 1000."
        else:
            viol = low_temp_sensors[~condition]
            expl = f"{len(viol)} low-temp sensors violate (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a sensor's average humidity is greater than 60%, then its power use is greater than 200 kWh."""
    high_humid_sensors = df[df["avg_humidity"] > 60]
    if high_humid_sensors.empty:
        truth = True
        expl = "No sensors with avg humidity > 60%."
    else:
        condition = high_humid_sensors["power_use_kwh"] > 200
        truth = condition.all()
        if truth:
            expl = f"All {len(high_humid_sensors)} high-humidity sensors have power use > 200 kWh."
        else:
            viol = high_humid_sensors[~condition]
            expl = f"{len(viol)} high-humidity sensors violate (power use: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors in the downtown zone have an average noise level less than 50 dB."""
    downtown_sensors = df[df["zone"] == "downtown"]
    if downtown_sensors.empty:
        truth = True
        expl = "No sensors in downtown zone."
    else:
        condition = downtown_sensors["noise_db"] < 50
        count_less = condition.sum()
        total = len(downtown_sensors)
        truth = count_less > total / 2
        if truth:
            expl = f"Most ({count_less}/{total}) downtown sensors have noise < 50 dB."
        else:
            expl = f"Only {count_less}/{total} downtown sensors have noise < 50 dB."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average PM2.5 level greater than 30 have a foot traffic less than 700."""
    high_pm25_sensors = df[df["pm25"] > 30]
    if high_pm25_sensors.empty:
        truth = True
        expl = "No sensors with PM2.5 > 30."
    else:
        condition = high_pm25_sensors["foot_traffic"] < 700
        truth = condition.all()
        if truth:
            expl = f"All {len(high_pm25_sensors)} high-PM2.5 sensors have foot traffic < 700."
        else:
            viol = high_pm25_sensors[~condition]
            expl = f"{len(viol)} high-PM2.5 sensors violate (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a sensor is in the park zone, then its average temperature is less than 28°C."""
    park_sensors = df[df["zone"] == "park"]
    if park_sensors.empty:
        truth = True
        expl = "No sensors in park zone."
    else:
        condition = park_sensors["avg_temp_c"] < 28
        truth = condition.all()
        if truth:
            expl = f"All {len(park_sensors)} park sensors have avg temp < 28°C."
        else:
            viol = park_sensors[~condition]
            expl = f"{len(viol)} park sensors violate (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the residential zone with an average noise level greater than 67 dB."""
    residential_sensors = df[df["zone"] == "residential"]
    if residential_sensors.empty:
        truth = False
        expl = "No sensors in residential zone."
    else:
        condition = residential_sensors["noise_db"] > 67
        truth = condition.any()
        if truth:
            found = residential_sensors[condition]
            expl = f"At least one residential sensor has noise > 67 dB ({found.iloc[0]['sensor_id']}, {found.iloc[0]['noise_db']} dB)."
        else:
            expl = f"No residential sensors have noise > 67 dB."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All sensors with a foot traffic greater than 1200 have an average humidity greater than 50%."""
    high_foot_sensors = df[df["foot_traffic"] > 1200]
    if high_foot_sensors.empty:
        truth = True
        expl = "No sensors with foot traffic > 1200."
    else:
        condition = high_foot_sensors["avg_humidity"] > 50
        truth = condition.all()
        if truth:
            expl = f"All {len(high_foot_sensors)} high-foot sensors have avg humidity > 50%."
        else:
            viol = high_foot_sensors[~condition]
            expl = f"{len(viol)} high-foot sensors violate (humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a sensor's power use is less than 250 kWh, then its average temperature is greater than 22°C."""
    low_power_sensors = df[df["power_use_kwh"] < 250]
    if low_power_sensors.empty:
        truth = True
        expl = "No sensors with power use < 250 kWh."
    else:
        condition = low_power_sensors["avg_temp_c"] > 22
        truth = condition.all()
        if truth:
            expl = f"All {len(low_power_sensors)} low-power sensors have avg temp > 22°C."
        else:
            viol = low_power_sensors[~condition]
            expl = f"{len(viol)} low-power sensors violate (temp: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most sensors in the industrial zone have an average PM2.5 level less than 25."""
    industrial_sensors = df[df["zone"] == "industrial"]
    if industrial_sensors.empty:
        truth = True
        expl = "No sensors in industrial zone."
    else:
        condition = industrial_sensors["pm25"] < 25
        count_less = condition.sum()
        total = len(industrial_sensors)
        truth = count_less > total / 2
        if truth:
            expl = f"Most ({count_less}/{total}) industrial sensors have PM2.5 < 25."
        else:
            expl = f"Only {count_less}/{total} industrial sensors have PM2.5 < 25."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All sensors with an average noise level greater than 70 dB have a foot traffic less than 1300."""
    high_noise_sensors = df[df["noise_db"] > 70]
    if high_noise_sensors.empty:
        truth = True
        expl = "No sensors with noise > 70 dB."
    else:
        condition = high_noise_sensors["foot_traffic"] < 1300
        truth = condition.all()
        if truth:
            expl = f"All {len(high_noise_sensors)} high-noise sensors have foot traffic < 1300."
        else:
            viol = high_noise_sensors[~condition]
            expl = f"{len(viol)} high-noise sensors violate (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a sensor is in the downtown zone, then its average humidity is greater than 55%."""
    downtown_sensors = df[df["zone"] == "downtown"]
    if downtown_sensors.empty:
        truth = True
        expl = "No sensors in downtown zone."
    else:
        condition = downtown_sensors["avg_humidity"] > 55
        truth = condition.all()
        if truth:
            expl = f"All {len(downtown_sensors)} downtown sensors have avg humidity > 55%."
        else:
            viol = downtown_sensors[~condition]
            expl = f"{len(viol)} downtown sensors violate (humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one sensor in the park zone with an average temperature less than 22°C."""
    park_sensors = df[df["zone"] == "park"]
    if park_sensors.empty:
        truth = False
        expl = "No sensors in park zone."
    else:
        condition = park_sensors["avg_temp_c"] < 22
        truth = condition.any()
        if truth:
            found = park_sensors[condition]
            expl = f"At least one park sensor has temp < 22°C ({found.iloc[0]['sensor_id']}, {found.iloc[0]['avg_temp_c']}°C)."
        else:
            expl = f"No park sensors have temp < 22°C."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All sensors with an average humidity less than 55% have a foot traffic greater than 600."""
    low_humid_sensors = df[df["avg_humidity"] < 55]
    if low_humid_sensors.empty:
        truth = True
        expl = "No sensors with avg humidity < 55%."
    else:
        condition = low_humid_sensors["foot_traffic"] > 600
        truth = condition.all()
        if truth:
            expl = f"All {len(low_humid_sensors)} low-humidity sensors have foot traffic > 600."
        else:
            viol = low_humid_sensors[~condition]
            expl = f"{len(viol)} low-humidity sensors violate (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a sensor's average PM2.5 level is less than 20, then its power use is greater than 300 kWh."""
    low_pm25_sensors = df[df["pm25"] < 20]
    if low_pm25_sensors.empty:
        truth = True
        expl = "No sensors with PM2.5 < 20."
    else:
        condition = low_pm25_sensors["power_use_kwh"] > 300
        truth = condition.all()
        if truth:
            expl = f"All {len(low_pm25_sensors)} low-PM2.5 sensors have power use > 300 kWh."
        else:
            viol = low_pm25_sensors[~condition]
            expl = f"{len(viol)} low-PM2.5 sensors violate (power use: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_97.csv")

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