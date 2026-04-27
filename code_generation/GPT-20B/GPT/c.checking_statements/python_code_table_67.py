import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All industrial sensors have average temperature between 20.5°C and 27.7°C."""
    industrial = df[df["zone"] == "industrial"]
    if industrial.empty:
        return True, "No industrial sensors to evaluate."
    condition = industrial["avg_temp_c"].between(20.5, 27.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial)} industrial sensors have avg_temp_c within 20.5-27.7°C."
    else:
        viol = industrial[~condition]
        viol_ids = viol["sensor_id"].tolist()
        viol_temps = viol["avg_temp_c"].tolist()
        expl = f"{len(viol)} industrial sensors violate the rule (IDs: {', '.join(map(str, viol_ids))}, temps: {', '.join(map(str, viol_temps))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All park sensors have average humidity between 55.0% and 61.2%."""
    park = df[df["zone"] == "park"]
    if park.empty:
        return True, "No park sensors to evaluate."
    condition = park["avg_humidity"].between(55.0, 61.2, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have avg_humidity within 55.0-61.2%."
    else:
        viol = park[~condition]
        viol_ids = viol["sensor_id"].tolist()
        viol_hum = viol["avg_humidity"].tolist()
        expl = f"{len(viol)} park sensors violate the rule (IDs: {', '.join(map(str, viol_ids))}, humidities: {', '.join(map(str, viol_hum))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All residential sensors have PM2.5 of at least 25.9 µg/m³."""
    residential = df[df["zone"] == "residential"]
    if residential.empty:
        return True, "No residential sensors to evaluate."
    condition = residential["pm25"] >= 25.9
    truth = condition.all()
    if truth:
        expl = f"All {len(residential)} residential sensors have pm25 ≥ 25.9 µg/m³."
    else:
        viol = residential[~condition]
        viol_ids = viol["sensor_id"].tolist()
        viol_pm = viol["pm25"].tolist()
        expl = f"{len(viol)} residential sensors violate the rule (IDs: {', '.join(map(str, viol_ids))}, pm25: {', '.join(map(str, viol_pm))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All downtown sensors have noise levels below 63 dB."""
    downtown = df[df["zone"] == "downtown"]
    if downtown.empty:
        return True, "No downtown sensors to evaluate."
    condition = downtown["noise_db"] < 63
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown)} downtown sensors have noise_db < 63 dB."
    else:
        viol = downtown[~condition]
        viol_ids = viol["sensor_id"].tolist()
        viol_noise = viol["noise_db"].tolist()
        expl = f"{len(viol)} downtown sensors violate the rule (IDs: {', '.join(map(str, viol_ids))}, noise_db: {', '.join(map(str, viol_noise))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All park sensors have PM2.5 ≤24.7 µg/m³."""
    park = df[df["zone"] == "park"]
    if park.empty:
        return True, "No park sensors to evaluate."
    condition = park["pm25"] <= 24.7
    truth = condition.all()
    if truth:
        expl = f"All {len(park)} park sensors have pm25 ≤ 24.7 µg/m³."
    else:
        viol = park[~condition]
        viol_ids = viol["sensor_id"].tolist()
        viol_pm = viol["pm25"].tolist()
        expl = f"{len(viol)} park sensors violate the rule (IDs: {', '.join(map(str, viol_ids))}, pm25: {', '.join(map(str, viol_pm))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Any sensor with foot traffic exceeding 1300 is in the residential or downtown zone."""
    high_ft = df[df["foot_traffic"] > 1300]
    if high_ft.empty:
        return True, "No sensors exceed foot traffic of 1300."
    condition = high_ft["zone"].isin(["residential", "downtown"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_ft)} sensors with foot_traffic > 1300 are in residential or downtown zones."
    else:
        viol = high_ft[~condition]
        viol_ids = viol["sensor_id"].tolist()
        viol_zones = viol["zone"].tolist()
        expl = f"{len(viol)} sensors violate the rule (IDs: {', '.join(map(str, viol_ids))}, zones: {', '.join(map(str, viol_zones))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. The highest noise level recorded (74.9 dB) occurs at an industrial sensor."""
    max_noise = df["noise_db"].max()
    if pd.isna(max_noise):
        return False, "No noise data available."
    sensors_with_max = df[df["noise_db"] == max_noise]
    zones = sensors_with_max["zone"].unique()
    truth = (max_noise == 74.9) and all(z == "industrial" for z in zones)
    if truth:
        expl = f"Maximum noise_db is {max_noise} dB at sensor(s) {', '.join(sensors_with_max['sensor_id'])} in industrial zone."
    else:
        expl = f"Maximum noise_db is {max_noise} dB but occurs at zone(s): {', '.join(zones)}."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. The greatest power consumption (443.8 kWh) is observed at a residential sensor."""
    max_power = df["power_use_kwh"].max()
    if pd.isna(max_power):
        return False, "No power consumption data available."
    sensors_with_max = df[df["power_use_kwh"] == max_power]
    zones = sensors_with_max["zone"].unique()
    truth = (max_power == 443.8) and all(z == "residential" for z in zones)
    if truth:
        expl = f"Maximum power_use_kwh is {max_power} kWh at sensor(s) {', '.join(sensors_with_max['sensor_id'])} in residential zone."
    else:
        expl = f"Maximum power_use_kwh is {max_power} kWh but occurs at zone(s): {', '.join(zones)}."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_67.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col!= "sensor_id" and col!= "zone":
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()