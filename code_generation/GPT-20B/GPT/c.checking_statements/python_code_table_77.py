import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all sensors in the park zone, average temperature is between 20.7°C and 27.5°C."""
    park = df[df["zone"] == "park"]
    condition = park["avg_temp_c"].between(20.7, 27.5, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg_temp_c between 20.7 and 27.5."
    else:
        viol = park[~condition]
        expl = f"{len(viol)} park sensors violate the rule (avg_temp_c: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all residential sensors, average humidity is between 51.0% and 67.3%."""
    res = df[df["zone"] == "residential"]
    condition = res["avg_humidity"].between(51.0, 67.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(res)} residential sensors have avg_humidity between 51.0% and 67.3%."
    else:
        viol = res[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (avg_humidity: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all downtown sensors, foot traffic is at least 474."""
    downtown = df[df["zone"] == "downtown"]
    condition = downtown["foot_traffic"] >= 474
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot_traffic >= 474."
    else:
        viol = downtown[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (foot_traffic: {', '.join(map(str, viol['foot_traffic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists a residential sensor (SN077007) with the highest PM2.5 value of 30.6 µg/m³ among all sensors."""
    sensor = df[df["sensor_id"] == "SN077007"]
    if sensor.empty:
        truth = False
        expl = "Sensor SN077007 does not exist."
    else:
        zone = sensor["zone"].iloc[0]
        pm25 = sensor["pm25"].iloc[0]
        max_pm25 = df["pm25"].max()
        truth = (zone == "residential" and abs(pm25 - max_pm25) < 1e-6 and abs(max_pm25 - 30.6) < 1e-6)
        if truth:
            expl = "Sensor SN077007 is residential and has the highest PM2.5 of 30.6 µg/m³."
        else:
            if zone!= "residential":
                expl = f"Sensor SN077007 is not residential (zone: {zone})."
            elif abs(pm25 - max_pm25) >= 1e-6:
                expl = f"Sensor SN077007 has PM2.5 {pm25} µg/m³, but the maximum is {max_pm25} µg/m³."
            else:
                expl = f"Maximum PM2.5 is {max_pm25} µg/m³, not 30.6 µg/m³."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most sensors (8 out of 15) record noise levels above 50 dB."""
    total = len(df)
    count_above = (df["noise_db"] > 50).sum()
    truth = (total == 15 and count_above == 8)
    if truth:
        expl = "There are 15 sensors, 8 of which have noise levels above 50 dB."
    else:
        if total!= 15:
            expl = f"Total sensors is {total}, not 15."
        else:
            expl = f"{count_above} sensors have noise >50 dB, not 8."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all sensors with foot traffic exceeding 1300, power use is at least 215.0 kWh."""
    high_ft = df[df["foot_traffic"] > 1300]
    condition = high_ft["power_use_kwh"] >= 215.0
    truth = condition.all()
    if truth:
        expl = "All sensors with foot traffic >1300 have power use >= 215.0 kWh."
    else:
        viol = high_ft[~condition]
        ft_vals = ', '.join(map(str, viol["foot_traffic"].tolist()))
        pu_vals = ', '.join(map(str, viol["power_use_kwh"].tolist()))
        expl = f"{len(viol)} sensors violate the rule (foot_traffic: {ft_vals}, power_use_kwh: {pu_vals})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If average temperature is at least 27.0°C, then PM2.5 is at least 22.7 µg/m³."""
    temp_ge_27 = df[df["avg_temp_c"] >= 27.0]
    condition = temp_ge_27["pm25"] >= 22.7
    truth = condition.all()
    if truth:
        expl = "All sensors with avg_temp_c >=27.0 have pm25 >=22.7 µg/m³."
    else:
        viol = temp_ge_27[~condition]
        temp_vals = ', '.join(map(str, viol["avg_temp_c"].tolist()))
        pm25_vals = ', '.join(map(str, viol["pm25"].tolist()))
        expl = f"{len(viol)} sensors violate the rule (avg_temp_c: {temp_vals}, pm25: {pm25_vals})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If average humidity is 52% or lower, then noise level does not exceed 41.6 dB."""
    hum_le_52 = df[df["avg_humidity"] <= 52]
    condition = hum_le_52["noise_db"] <= 41.6
    truth = condition.all()
    if truth:
        expl = "All sensors with avg_humidity <=52 have noise_db <=41.6 dB."
    else:
        viol = hum_le_52[~condition]
        hum_vals = ', '.join(map(str, viol["avg_humidity"].tolist()))
        noise_vals = ', '.join(map(str, viol["noise_db"].tolist()))
        expl = f"{len(viol)} sensors violate the rule (avg_humidity: {hum_vals}, noise_db: {noise_vals})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_77.csv")

    # Convert numeric columns safely.
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