import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All industrial sensors have an average temperature of at most 20.9°C."""
    industrial = df[df["zone"] == "industrial"]
    if industrial.empty:
        return True, "No industrial sensors present; statement vacuously true."
    condition = industrial["avg_temp_c"] <= 20.9
    truth = condition.all()
    if truth:
        return True, f"All {len(industrial)} industrial sensors have avg_temp_c <= 20.9°C."
    else:
        viol = industrial[~condition]
        ids = viol["sensor_id"].tolist()
        temps = viol["avg_temp_c"].tolist()
        return False, f"{len(viol)} industrial sensors violate the rule (sensor_ids: {', '.join(ids)}; temps: {', '.join(map(str, temps))})."

def stmt_2(df: pd.DataFrame):
    """2. All park sensors record foot traffic of at least 443 people."""
    park = df[df["zone"] == "park"]
    if park.empty:
        return True, "No park sensors present; statement vacuously true."
    condition = park["foot_traffic"] >= 443
    truth = condition.all()
    if truth:
        return True, f"All {len(park)} park sensors have foot_traffic >= 443."
    else:
        viol = park[~condition]
        ids = viol["sensor_id"].tolist()
        ft = viol["foot_traffic"].tolist()
        return False, f"{len(viol)} park sensors violate the rule (sensor_ids: {', '.join(ids)}; foot_traffic: {', '.join(map(str, ft))})."

def stmt_3(df: pd.DataFrame):
    """3. All residential sensors record foot traffic of at least 432 people."""
    residential = df[df["zone"] == "residential"]
    if residential.empty:
        return True, "No residential sensors present; statement vacuously true."
    condition = residential["foot_traffic"] >= 432
    truth = condition.all()
    if truth:
        return True, f"All {len(residential)} residential sensors have foot_traffic >= 432."
    else:
        viol = residential[~condition]
        ids = viol["sensor_id"].tolist()
        ft = viol["foot_traffic"].tolist()
        return False, f"{len(viol)} residential sensors violate the rule (sensor_ids: {', '.join(ids)}; foot_traffic: {', '.join(map(str, ft))})."

def stmt_4(df: pd.DataFrame):
    """4. All sensors with an average temperature of 27°C or higher have power use of at least 223.9 kWh."""
    high_temp = df[df["avg_temp_c"] >= 27]
    if high_temp.empty:
        return True, "No sensors with avg_temp_c >= 27°C; statement vacuously true."
    condition = high_temp["power_use_kwh"] >= 223.9
    truth = condition.all()
    if truth:
        return True, f"All {len(high_temp)} sensors with avg_temp_c >= 27°C have power_use_kwh >= 223.9 kWh."
    else:
        viol = high_temp[~condition]
        ids = viol["sensor_id"].tolist()
        pu = viol["power_use_kwh"].tolist()
        return False, f"{len(viol)} sensors violate the rule (sensor_ids: {', '.join(ids)}; power_use_kwh: {', '.join(map(str, pu))})."

def stmt_5(df: pd.DataFrame):
    """5. All sensors with PM2.5 concentrations of 25 µg/m³ or higher have noise levels of at most 60.1 dB."""
    high_pm25 = df[df["pm25"] >= 25]
    if high_pm25.empty:
        return True, "No sensors with pm25 >= 25 µg/m³; statement vacuously true."
    condition = high_pm25["noise_db"] <= 60.1
    truth = condition.all()
    if truth:
        return True, f"All {len(high_pm25)} sensors with pm25 >= 25 µg/m³ have noise_db <= 60.1 dB."
    else:
        viol = high_pm25[~condition]
        ids = viol["sensor_id"].tolist()
        noise = viol["noise_db"].tolist()
        return False, f"{len(viol)} sensors violate the rule (sensor_ids: {', '.join(ids)}; noise_db: {', '.join(map(str, noise))})."

def stmt_6(df: pd.DataFrame):
    """6. All sensors with average humidity above 60% have foot traffic of at least 582 people."""
    high_humidity = df[df["avg_humidity"] > 60]
    if high_humidity.empty:
        return True, "No sensors with avg_humidity > 60%; statement vacuously true."
    condition = high_humidity["foot_traffic"] >= 582
    truth = condition.all()
    if truth:
        return True, f"All {len(high_humidity)} sensors with avg_humidity > 60% have foot_traffic >= 582."
    else:
        viol = high_humidity[~condition]
        ids = viol["sensor_id"].tolist()
        ft = viol["foot_traffic"].tolist()
        return False, f"{len(viol)} sensors violate the rule (sensor_ids: {', '.join(ids)}; foot_traffic: {', '.join(map(str, ft))})."

def stmt_7(df: pd.DataFrame):
    """7. All sensors with noise levels of 60 dB or higher have an average temperature of at most 25.5°C."""
    high_noise = df[df["noise_db"] >= 60]
    if high_noise.empty:
        return True, "No sensors with noise_db >= 60 dB; statement vacuously true."
    condition = high_noise["avg_temp_c"] <= 25.5
    truth = condition.all()
    if truth:
        return True, f"All {len(high_noise)} sensors with noise_db >= 60 dB have avg_temp_c <= 25.5°C."
    else:
        viol = high_noise[~condition]
        ids = viol["sensor_id"].tolist()
        temps = viol["avg_temp_c"].tolist()
        return False, f"{len(viol)} sensors violate the rule (sensor_ids: {', '.join(ids)}; avg_temp_c: {', '.join(map(str, temps))})."

def stmt_8(df: pd.DataFrame):
    """8. All downtown sensors have average temperatures between 20.9°C and 25.5°C inclusive."""
    downtown = df[df["zone"] == "downtown"]
    if downtown.empty:
        return True, "No downtown sensors present; statement vacuously true."
    condition = downtown["avg_temp_c"].between(20.9, 25.5, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(downtown)} downtown sensors have avg_temp_c between 20.9°C and 25.5°C inclusive."
    else:
        viol = downtown[~condition]
        ids = viol["sensor_id"].tolist()
        temps = viol["avg_temp_c"].tolist()
        return False, f"{len(viol)} downtown sensors violate the rule (sensor_ids: {', '.join(ids)}; avg_temp_c: {', '.join(map(str, temps))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_57.csv")

    # Convert numeric columns safely, keep sensor_id as string
    for col in df.columns:
        if col!= "sensor_id":
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