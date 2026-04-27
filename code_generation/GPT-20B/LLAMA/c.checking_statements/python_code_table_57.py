import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the downtown zone have an average temperature greater than 20°C."""
    if "zone" not in df.columns or "avg_temp_c" not in df.columns:
        return False, "Required columns missing."
    downtown = df[df["zone"].str.lower() == "downtown"]
    if downtown.empty:
        return True, "No downtown sensors; statement vacuously true."
    condition = downtown["avg_temp_c"] > 20
    truth = condition.all()
    if truth:
        return True, f"All {len(downtown)} downtown sensors have avg_temp_c > 20."
    else:
        viol = downtown[~condition]
        temps = viol["avg_temp_c"].tolist()
        return False, f"{len(viol)} downtown sensors violate the rule (temps: {temps})."

def stmt_2(df: pd.DataFrame):
    """2. All sensors in the park zone have an average humidity greater than 50%."""
    if "zone" not in df.columns or "avg_humidity" not in df.columns:
        return False, "Required columns missing."
    park = df[df["zone"].str.lower() == "park"]
    if park.empty:
        return True, "No park sensors; statement vacuously true."
    condition = park["avg_humidity"] > 50
    truth = condition.all()
    if truth:
        return True, f"All {len(park)} park sensors have avg_humidity > 50."
    else:
        viol = park[~condition]
        hums = viol["avg_humidity"].tolist()
        return False, f"{len(viol)} park sensors violate the rule (humidities: {hums})."

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is in the industrial zone, then its average PM2.5 level is less than 25."""
    if "zone" not in df.columns or "pm25" not in df.columns:
        return False, "Required columns missing."
    industrial = df[df["zone"].str.lower() == "industrial"]
    if industrial.empty:
        return True, "No industrial sensors; statement vacuously true."
    condition = industrial["pm25"] < 25
    truth = condition.all()
    if truth:
        return True, f"All {len(industrial)} industrial sensors have pm25 < 25."
    else:
        viol = industrial[~condition]
        pms = viol["pm25"].tolist()
        return False, f"{len(viol)} industrial sensors violate the rule (pm25: {pms})."

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one sensor in the residential zone with an average temperature greater than 28°C."""
    if "zone" not in df.columns or "avg_temp_c" not in df.columns:
        return False, "Required columns missing."
    residential = df[df["zone"].str.lower() == "residential"]
    exists = (residential["avg_temp_c"] > 28).any()
    if exists:
        temps = residential[residential["avg_temp_c"] > 28]["avg_temp_c"].tolist()
        return True, f"Found {len(temps)} residential sensors with avg_temp_c > 28 (temps: {temps})."
    else:
        return False, "No residential sensor has avg_temp_c > 28."

def stmt_5(df: pd.DataFrame):
    """5. All sensors with foot traffic greater than 1000 have a power use less than 450 kWh."""
    if "foot_traffic" not in df.columns or "power_use_kwh" not in df.columns:
        return False, "Required columns missing."
    high_ft = df[df["foot_traffic"] > 1000]
    if high_ft.empty:
        return True, "No sensors with foot_traffic > 1000; statement vacuously true."
    condition = high_ft["power_use_kwh"] < 450
    truth = condition.all()
    if truth:
        return True, f"All {len(high_ft)} high foot traffic sensors have power_use_kwh < 450."
    else:
        viol = high_ft[~condition]
        powers = viol["power_use_kwh"].tolist()
        return False, f"{len(viol)} high foot traffic sensors violate the rule (power_use_kwh: {powers})."

def stmt_6(df: pd.DataFrame):
    """6. If a sensor is in the downtown zone, then its noise level is greater than 60 dB."""
    if "zone" not in df.columns or "noise_db" not in df.columns:
        return False, "Required columns missing."
    downtown = df[df["zone"].str.lower() == "downtown"]
    if downtown.empty:
        return True, "No downtown sensors; statement vacuously true."
    condition = downtown["noise_db"] > 60
    truth = condition.all()
    if truth:
        return True, f"All {len(downtown)} downtown sensors have noise_db > 60."
    else:
        viol = downtown[~condition]
        noises = viol["noise_db"].tolist()
        return False, f"{len(viol)} downtown sensors violate the rule (noise_db: {noises})."

def stmt_7(df: pd.DataFrame):
    """7. Most sensors have an average step count greater than 500."""
    if "step_count" not in df.columns:
        return False, "Column'step_count' not found; cannot evaluate."
    total = len(df)
    if total == 0:
        return True, "No sensors; statement vacuously true."
    condition = df["step_count"] > 500
    count = condition.sum()
    truth = count > total / 2
    percent = (count / total) * 100
    if truth:
        return True, f"{count} out of {total} sensors ({percent:.1f}%) have step_count > 500."
    else:
        return False, f"{count} out of {total} sensors ({percent:.1f}%) have step_count > 500."

def stmt_8(df: pd.DataFrame):
    """8. All sensors with an average humidity less than 55% are in the residential or industrial zones."""
    if "avg_humidity" not in df.columns or "zone" not in df.columns:
        return False, "Required columns missing."
    low_hum = df[df["avg_humidity"] < 55]
    if low_hum.empty:
        return True, "No sensors with avg_humidity < 55; statement vacuously true."
    condition = low_hum["zone"].str.lower().isin(["residential", "industrial"])
    truth = condition.all()
    if truth:
        return True, f"All {len(low_hum)} sensors with avg_humidity < 55 are in residential or industrial zones."
    else:
        viol = low_hum[~condition]
        zones = viol["zone"].tolist()
        return False, f"{len(viol)} sensors with avg_humidity < 55 are in zones: {zones}."

def stmt_9(df: pd.DataFrame):
    """9. If a sensor is in the park zone, then its power use is less than 350 kWh."""
    if "zone" not in df.columns or "power_use_kwh" not in df.columns:
        return False, "Required columns missing."
    park = df[df["zone"].str.lower() == "park"]
    if park.empty:
        return True, "No park sensors; statement vacuously true."
    condition = park["power_use_kwh"] < 350
    truth = condition.all()
    if truth:
        return True, f"All {len(park)} park sensors have power_use_kwh < 350."
    else:
        viol = park[~condition]
        powers = viol["power_use_kwh"].tolist()
        return False, f"{len(viol)} park sensors violate the rule (power_use_kwh: {powers})."

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one sensor in the industrial zone with an average PM2.5 level less than 12."""
    if "zone" not in df.columns or "pm25" not in df.columns:
        return False, "Required columns missing."
    industrial = df[df["zone"].str.lower() == "industrial"]
    exists = (industrial["pm25"] < 12).any()
    if exists:
        pms = industrial[industrial["pm25"] < 12]["pm25"].tolist()
        return True, f"Found {len(pms)} industrial sensors with pm25 < 12 (pm25: {pms})."
    else:
        return False, "No industrial sensor has pm25 < 12."

def stmt_11(df: pd.DataFrame):
    """11. All sensors with an average temperature greater than 25°C have an average humidity less than 60%."""
    if "avg_temp_c" not in df.columns or "avg_humidity" not in df.columns:
        return False, "Required columns missing."
    high_temp = df[df["avg_temp_c"] > 25]
    if high_temp.empty:
        return True, "No sensors with avg_temp_c > 25; statement vacuously true."
    condition = high_temp["avg_humidity"] < 60
    truth = condition.all()
    if truth:
        return True, f"All {len(high_temp)} sensors with avg_temp_c > 25 have avg_humidity < 60."
    else:
        viol = high_temp[~condition]
        hums = viol["avg_humidity"].tolist()
        return False, f"{len(viol)} sensors with avg_temp_c > 25 violate the rule (avg_humidity: {hums})."

def stmt_12(df: pd.DataFrame):
    """12. If a sensor is in the residential zone, then its foot traffic is greater than 400."""
    if "zone" not in df.columns or "foot_traffic" not in df.columns:
        return False, "Required columns missing."
    residential = df[df["zone"].str.lower() == "residential"]
    if residential.empty:
        return True, "No residential sensors; statement vacuously true."
    condition = residential["foot_traffic"] > 400
    truth = condition.all()
    if truth:
        return True, f"All {len(residential)} residential sensors have foot_traffic > 400."
    else:
        viol = residential[~condition]
        fts = viol["foot_traffic"].tolist()
        return False, f"{len(viol)} residential sensors violate the rule (foot_traffic: {fts})."

def stmt_13(df: pd.DataFrame):
    """13. Most sensors in the downtown zone have an average temperature greater than 22°C."""
    if "zone" not in df.columns or "avg_temp_c" not in df.columns:
        return False, "Required columns missing."
    downtown = df[df["zone"].str.lower() == "downtown"]
    total = len(downtown)
    if total == 0:
        return False, "No downtown sensors; cannot evaluate majority."
    condition = downtown["avg_temp_c"] > 22
    count = condition.sum()
    truth = count > total / 2
    percent = (count / total) * 100
    if truth:
        return True, f"{count} out of {total} downtown sensors ({percent:.1f}%) have avg_temp_c > 22."
    else:
        return False, f"{count} out of {total} downtown sensors ({percent:.1f}%) have avg_temp_c > 22."

def stmt_14(df: pd.DataFrame):
    """14. All sensors with a noise level greater than 60 dB have an average temperature greater than 22°C."""
    if "noise_db" not in df.columns or "avg_temp_c" not in df.columns:
        return False, "Required columns missing."
    high_noise = df[df["noise_db"] > 60]
    if high_noise.empty:
        return True, "No sensors with noise_db > 60; statement vacuously true."
    condition = high_noise["avg_temp_c"] > 22
    truth = condition.all()
    if truth:
        return True, f"All {len(high_noise)} sensors with noise_db > 60 have avg_temp_c > 22."
    else:
        viol = high_noise[~condition]
        temps = viol["avg_temp_c"].tolist()
        return False, f"{len(viol)} sensors with noise_db > 60 violate the rule (avg_temp_c: {temps})."

def stmt_15(df: pd.DataFrame):
    """15. If a sensor is in the park zone, then its average temperature is greater than 22°C."""
    if "zone" not in df.columns or "avg_temp_c" not in df.columns:
        return False, "Required columns missing."
    park = df[df["zone"].str.lower() == "park"]
    if park.empty:
        return True, "No park sensors; statement vacuously true."
    condition = park["avg_temp_c"] > 22
    truth = condition.all()
    if truth:
        return True, f"All {len(park)} park sensors have avg_temp_c > 22."
    else:
        viol = park[~condition]
        temps = viol["avg_temp_c"].tolist()
        return False, f"{len(viol)} park sensors violate the rule (avg_temp_c: {temps})."

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one sensor in the residential zone with a power use less than 200 kWh."""
    if "zone" not in df.columns or "power_use_kwh" not in df.columns:
        return False, "Required columns missing."
    residential = df[df["zone"].str.lower() == "residential"]
    exists = (residential["power_use_kwh"] < 200).any()
    if exists:
        powers = residential[residential["power_use_kwh"] < 200]["power_use_kwh"].tolist()
        return True, f"Found {len(powers)} residential sensors with power_use_kwh < 200 (values: {powers})."
    else:
        return False, "No residential sensor has power_use_kwh < 200."

def main():
    df = pd.read_csv("../inference_generation/tables/table_57.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col not in ["sensor_id", "zone"]:
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()