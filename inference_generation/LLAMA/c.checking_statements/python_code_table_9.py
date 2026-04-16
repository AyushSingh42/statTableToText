import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All sensors in the downtown zone have an average temperature above 24 degrees Celsius."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["avg_temp_c"] > 24
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown_sensors)} downtown sensors have an average temperature above 24 degrees Celsius."
    else:
        viol = downtown_sensors[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (average temperatures: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a sensor is in the industrial zone, then its average humidity is below 56%."""
    industrial_sensors = df[df["zone"] == "industrial"]
    condition = industrial_sensors["avg_humidity"] < 56
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial_sensors)} industrial sensors have an average humidity below 56%."
    else:
        viol = industrial_sensors[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (average humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every sensor with a high foot traffic (above 1000) is located in either the downtown or industrial zone."""
    high_foot_traffic_sensors = df[df["foot_traffic"] > 1000]
    condition = high_foot_traffic_sensors["zone"].isin(["downtown", "industrial"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_foot_traffic_sensors)} sensors with high foot traffic are located in either the downtown or industrial zone."
    else:
        viol = high_foot_traffic_sensors[~condition]
        expl = f"{len(viol)} sensors with high foot traffic violate the rule (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All sensors with a power use above 400 KWh are located in the downtown or industrial zone."""
    high_power_use_sensors = df[df["power_use_kwh"] > 400]
    condition = high_power_use_sensors["zone"].isin(["downtown", "industrial"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_power_use_sensors)} sensors with high power use are located in the downtown or industrial zone."
    else:
        viol = high_power_use_sensors[~condition]
        expl = f"{len(viol)} sensors with high power use violate the rule (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a sensor is in the residential zone, then its average noise level is below 53 decibels."""
    residential_sensors = df[df["zone"] == "residential"]
    condition = residential_sensors["noise_db"] < 53
    truth = condition.all()
    if truth:
        expl = f"All {len(residential_sensors)} residential sensors have an average noise level below 53 decibels."
    else:
        viol = residential_sensors[~condition]
        expl = f"{len(viol)} residential sensors violate the rule (average noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All sensors with a PM2.5 level above 30 are located in the industrial zone."""
    high_pm25_sensors = df[df["pm25"] > 30]
    condition = high_pm25_sensors["zone"] == "industrial"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_pm25_sensors)} sensors with high PM2.5 levels are located in the industrial zone."
    else:
        viol = high_pm25_sensors[~condition]
        expl = f"{len(viol)} sensors with high PM2.5 levels violate the rule (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every sensor in the park zone has an average humidity above 64%."""
    park_sensors = df[df["zone"] == "park"]
    condition = park_sensors["avg_humidity"] > 64
    truth = condition.all()
    if truth:
        expl = f"All {len(park_sensors)} park sensors have an average humidity above 64%."
    else:
        viol = park_sensors[~condition]
        expl = f"{len(viol)} park sensors violate the rule (average humidities: {', '.join(map(str, viol['avg_humidity'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a sensor has a high average temperature (above 26 degrees Celsius), then it is located in either the industrial or downtown zone."""
    high_temp_sensors = df[df["avg_temp_c"] > 26]
    condition = high_temp_sensors["zone"].isin(["industrial", "downtown"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_temp_sensors)} sensors with high average temperatures are located in either the industrial or downtown zone."
    else:
        viol = high_temp_sensors[~condition]
        expl = f"{len(viol)} sensors with high average temperatures violate the rule (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All sensors with a low foot traffic (below 600) are located in either the residential or park zone."""
    low_foot_traffic_sensors = df[df["foot_traffic"] < 600]
    condition = low_foot_traffic_sensors["zone"].isin(["residential", "park"])
    truth = condition.all()
    if truth:
        expl = f"All {len(low_foot_traffic_sensors)} sensors with low foot traffic are located in either the residential or park zone."
    else:
        viol = low_foot_traffic_sensors[~condition]
        expl = f"{len(viol)} sensors with low foot traffic violate the rule (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Every sensor with a high power use (above 350 KWh) has a high average temperature (above 25 degrees Celsius)."""
    high_power_use_sensors = df[df["power_use_kwh"] > 350]
    condition = high_power_use_sensors["avg_temp_c"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(high_power_use_sensors)} sensors with high power use have a high average temperature."
    else:
        viol = high_power_use_sensors[~condition]
        expl = f"{len(viol)} sensors with high power use violate the rule (average temperatures: {', '.join(map(str, viol['avg_temp_c'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a sensor is in the downtown zone, then its average noise level is above 65 decibels."""
    downtown_sensors = df[df["zone"] == "downtown"]
    condition = downtown_sensors["noise_db"] > 65
    truth = condition.all()
    if truth:
        expl = f"All {len(downtown_sensors)} downtown sensors have an average noise level above 65 decibels."
    else:
        viol = downtown_sensors[~condition]
        expl = f"{len(viol)} downtown sensors violate the rule (average noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All sensors with a low PM2.5 level (below 15) are located in either the residential or park zone."""
    low_pm25_sensors = df[df["pm25"] < 15]
    condition = low_pm25_sensors["zone"].isin(["residential", "park"])
    truth = condition.all()
    if truth:
        expl = f"All {len(low_pm25_sensors)} sensors with low PM2.5 levels are located in either the residential or park zone."
    else:
        viol = low_pm25_sensors[~condition]
        expl = f"{len(viol)} sensors with low PM2.5 levels violate the rule (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Every sensor in the industrial zone has a high average noise level (above 70 decibels)."""
    industrial_sensors = df[df["zone"] == "industrial"]
    condition = industrial_sensors["noise_db"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(industrial_sensors)} industrial sensors have a high average noise level."
    else:
        viol = industrial_sensors[~condition]
        expl = f"{len(viol)} industrial sensors violate the rule (average noise levels: {', '.join(map(str, viol['noise_db'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a sensor has a high average humidity (above 62%), then it is located in either the residential or park zone."""
    high_humidity_sensors = df[df["avg_humidity"] > 62]
    condition = high_humidity_sensors["zone"].isin(["residential", "park"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_humidity_sensors)} sensors with high average humidity are located in either the residential or park zone."
    else:
        viol = high_humidity_sensors[~condition]
        expl = f"{len(viol)} sensors with high average humidity violate the rule (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All sensors with a low power use (below 200 KWh) are located in the park zone."""
    low_power_use_sensors = df[df["power_use_kwh"] < 200]
    condition = low_power_use_sensors["zone"] == "park"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_power_use_sensors)} sensors with low power use are located in the park zone."
    else:
        viol = low_power_use_sensors[~condition]
        expl = f"{len(viol)} sensors with low power use violate the rule (zones: {', '.join(map(str, viol['zone'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_9.csv")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10), (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()