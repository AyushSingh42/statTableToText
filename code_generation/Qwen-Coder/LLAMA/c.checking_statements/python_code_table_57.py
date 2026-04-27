import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the downtown zone have an average temperature greater than 20°C."""
    downtown_sensors = df[df["zone"] == "downtown"]
    if downtown_sensors.empty:
        truth = True
        expl = "No sensors in downtown zone."
    else:
        condition = downtown_sensors["avg_temp_c"] > 20
        truth = condition.all()
        if truth:
            expl = f"All {len(downtown_sensors)} downtown sensors have avg temp > 20°C."
        else:
            viol = downtown_sensors[~condition]
            expl = f"{len(viol)} downtown sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the park zone have an average humidity greater than 50%."""
    park_sensors = df[df["zone"] == "park"]
    if park_sensors.empty:
        truth = True
        expl = "No sensors in park zone."
    else:
        condition = park_sensors["avg_humidity"] > 50
        truth = condition.all()
        if truth:
            expl = f"All {len(park_sensors)} park sensors have avg humidity > 50%."
        else:
            viol = park_sensors[~condition]
            expl = f"{len(viol)} park sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the industrial zone, then its average PM2.5 level is less than 25."""
    industrial_sensors = df[df["zone"] == "industrial"]
    if industrial_sensors.empty:
        truth = True
        expl = "No sensors in industrial zone."
    else:
        condition = industrial_sensors["pm25"] < 25
        truth = condition.all()
        if truth:
            expl = f"All {len(industrial_sensors)} industrial sensors have PM2.5 < 25."
        else:
            viol = industrial_sensors[~condition]
            expl = f"{len(viol)} industrial sensors violate the rule (PM2.5s: {', '.join(map(str, viol['pm25'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the residential zone with an average temperature greater than 28°C."""
    residential_sensors = df[df["zone"] == "residential"]
    if residential_sensors.empty:
        truth = False
        expl = "No sensors in residential zone."
    else:
        condition = residential_sensors["avg_temp_c"] > 28
        truth = condition.any()
        if truth:
            found = residential_sensors[condition]
            expl = f"At least one residential sensor ({found.iloc[0]['sensor_id']}) has avg temp > 28°C."
        else:
            expl = "No residential sensors have avg temp > 28°C."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All sensors with foot traffic greater than 1000 have a power use less than 450 kWh."""
    high_foot_traffic = df[df["foot_traffic"] > 1000]
    if high_foot_traffic.empty:
        truth = True
        expl = "No sensors with foot traffic > 1000."
    else:
        condition = high_foot_traffic["power_use_kwh"] < 450
        truth = condition.all()
        if truth:
            expl = f"All {len(high_foot_traffic)} high foot traffic sensors have power use < 450 kWh."
        else:
            viol = high_foot_traffic[~condition]
            expl = f"{len(viol)} high foot traffic sensors violate the rule (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a sensor is in the downtown zone, then its noise level is greater than 60 dB."""
    downtown_sensors = df[df["zone"] == "downtown"]
    if downtown_sensors.empty:
        truth = True
        expl = "No sensors in downtown zone."
    else:
        condition = downtown_sensors["noise_db"] > 60
        truth = condition.all()
        if truth:
            expl = f"All {len(downtown_sensors)} downtown sensors have noise > 60 dB."
        else:
            viol = downtown_sensors[~condition]
            expl = f"{len(viol)} downtown sensors violate the rule (noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most sensors have an average step count greater than 500."""
    # This statement references 'average step count' which is not present in the data.
    # We'll assume it refers to 'avg_temp_c' or another column.
    # Since there's no'step_count' column, we'll skip this one.
    truth = False
    expl = "No 'average step count' column in dataset."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average humidity less than 55% are in the residential or industrial zones."""
    low_humidity = df[df["avg_humidity"] < 55]
    if low_humidity.empty:
        truth = True
        expl = "No sensors with avg humidity < 55%."
    else:
        valid_zones = ["residential", "industrial"]
        condition = low_humidity["zone"].isin(valid_zones)
        truth = condition.all()
        if truth:
            expl = f"All {len(low_humidity)} low humidity sensors are in residential or industrial zones."
        else:
            viol = low_humidity[~condition]
            expl = f"{len(viol)} low humidity sensors are in invalid zones (zones: {', '.join(viol['zone'].tolist())})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a sensor is in the park zone, then its power use is less than 350 kWh."""
    park_sensors = df[df["zone"] == "park"]
    if park_sensors.empty:
        truth = True
        expl = "No sensors in park zone."
    else:
        condition = park_sensors["power_use_kwh"] < 350
        truth = condition.all()
        if truth:
            expl = f"All {len(park_sensors)} park sensors have power use < 350 kWh."
        else:
            viol = park_sensors[~condition]
            expl = f"{len(viol)} park sensors violate the rule (power uses: {', '.join(map(str, viol['power_use_kwh'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the industrial zone with an average PM2.5 level less than 12."""
    industrial_sensors = df[df["zone"] == "industrial"]
    if industrial_sensors.empty:
        truth = False
        expl = "No sensors in industrial zone."
    else:
        condition = industrial_sensors["pm25"] < 12
        truth = condition.any()
        if truth:
            found = industrial_sensors[condition]
            expl = f"At least one industrial sensor ({found.iloc[0]['sensor_id']}) has PM2.5 < 12."
        else:
            expl = "No industrial sensors have PM2.5 < 12."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All sensors with an average temperature greater than 25°C have an average humidity less than 60%."""
    high_temp = df[df["avg_temp_c"] > 25]
    if high_temp.empty:
        truth = True
        expl = "No sensors with avg temp > 25°C."
    else:
        condition = high_temp["avg_humidity"] < 60
        truth = condition.all()
        if truth:
            expl = f"All {len(high_temp)} high temp sensors have avg humidity < 60%."
        else:
            viol = high_temp[~condition]
            expl = f"{len(viol)} high temp sensors violate the rule (humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a sensor is in the residential zone, then its foot traffic is greater than 400."""
    residential_sensors = df[df["zone"] == "residential"]
    if residential_sensors.empty:
        truth = True
        expl = "No sensors in residential zone."
    else:
        condition = residential_sensors["foot_traffic"] > 400
        truth = condition.all()
        if truth:
            expl = f"All {len(residential_sensors)} residential sensors have foot traffic > 400."
        else:
            viol = residential_sensors[~condition]
            expl = f"{len(viol)} residential sensors violate the rule (foot traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most sensors in the downtown zone have an average temperature greater than 22°C."""
    downtown_sensors = df[df["zone"] == "downtown"]
    if downtown_sensors.empty:
        truth = False
        expl = "No sensors in downtown zone."
    else:
        condition = downtown_sensors["avg_temp_c"] > 22
        count_true = condition.sum()
        total = len(downtown_sensors)
        truth = count_true > total / 2
        if truth:
            expl = f"More than half ({count_true}/{total}) of downtown sensors have avg temp > 22°C."
        else:
            expl = f"Less than half ({count_true}/{total}) of downtown sensors have avg temp > 22°C."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All sensors with a noise level greater than 60 dB have an average temperature greater than 22°C."""
    high_noise = df[df["noise_db"] > 60]
    if high_noise.empty:
        truth = True
        expl = "No sensors with noise > 60 dB."
    else:
        condition = high_noise["avg_temp_c"] > 22
        truth = condition.all()
        if truth:
            expl = f"All {len(high_noise)} high noise sensors have avg temp > 22°C."
        else:
            viol = high_noise[~condition]
            expl = f"{len(viol)} high noise sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a sensor is in the park zone, then its average temperature is greater than 22°C."""
    park_sensors = df[df["zone"] == "park"]
    if park_sensors.empty:
        truth = True
        expl = "No sensors in park zone."
    else:
        condition = park_sensors["avg_temp_c"] > 22
        truth = condition.all()
        if truth:
            expl = f"All {len(park_sensors)} park sensors have avg temp > 22°C."
        else:
            viol = park_sensors[~condition]
            expl = f"{len(viol)} park sensors violate the rule (temps: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one sensor in the residential zone with a power use less than 200 kWh."""
    residential_sensors = df[df["zone"] == "residential"]
    if residential_sensors.empty:
        truth = False
        expl = "No sensors in residential zone."
    else:
        condition = residential_sensors["power_use_kwh"] < 200
        truth = condition.any()
        if truth:
            found = residential_sensors[condition]
            expl = f"At least one residential sensor ({found.iloc[0]['sensor_id']}) has power use < 200 kWh."
        else:
            expl = "No residential sensors have power use < 200 kWh."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_57.csv")

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