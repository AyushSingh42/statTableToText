import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles that traveled in clear weather had an average speed greater than 47 kph."""
    clear = df[df["weather"] == "clear"]
    if clear.empty:
        return True, "No vehicles traveled in clear weather, so the statement holds vacuously."
    condition = clear["avg_speed_kph"] > 47
    truth = condition.all()
    if truth:
        expl = f"All {len(clear)} vehicles that traveled in clear weather had avg speed > 47 kph."
    else:
        viol = clear[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (avg speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a van, then its fuel used is less than 40 liters."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        return True, "No vans in the data, so the statement holds vacuously."
    condition = vans["fuel_used_l"] < 40
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans had fuel used < 40 liters."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} van(s) violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one bus that traveled in cloudy weather with a delay of less than 10 minutes."""
    condition = (df["vehicle_type"] == "bus") & (df["weather"] == "cloudy") & (df["delay_minutes"] < 10)
    exists = condition.any()
    if exists:
        count = condition.sum()
        expl = f"Found {count} bus(es) that traveled in cloudy weather with delay < 10 minutes."
    else:
        expl = "No bus meets the criteria."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All trucks had a distance traveled greater than 220 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        return True, "No trucks in the data, so the statement holds vacuously."
    condition = trucks["distance_km"] > 220
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks had distance > 220 km."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} truck(s) violate the rule (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle traveled in windy weather, then its delay was greater than 20 minutes."""
    windy = df[df["weather"] == "windy"]
    if windy.empty:
        return True, "No vehicles traveled in windy weather, so the statement holds vacuously."
    condition = windy["delay_minutes"] > 20
    truth = condition.all()
    if truth:
        expl = f"All {len(windy)} vehicles that traveled in windy weather had delay > 20 minutes."
    else:
        viol = windy[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most vehicles had a fuel used greater than 20 liters."""
    condition = df["fuel_used_l"] > 20
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of vehicles had fuel used > 20 liters."
    else:
        expl = f"Only {proportion*100:.1f}% of vehicles had fuel used > 20 liters."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All vehicles that traveled in rain had a delay greater than 10 minutes."""
    rain = df[df["weather"] == "rain"]
    if rain.empty:
        return True, "No vehicles traveled in rain, so the statement holds vacuously."
    condition = rain["delay_minutes"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(rain)} vehicles that traveled in rain had delay > 10 minutes."
    else:
        viol = rain[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a bus, then its average speed is greater than 50 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        return True, "No buses in the data, so the statement holds vacuously."
    condition = buses["avg_speed_kph"] > 50
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses had avg speed > 50 kph."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} bus(es) violate the rule (avg speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one van that traveled in clear weather with a delay of less than 5 minutes."""
    condition = (df["vehicle_type"] == "van") & (df["weather"] == "clear") & (df["delay_minutes"] < 5)
    exists = condition.any()
    if exists:
        count = condition.sum()
        expl = f"Found {count} van(s) that traveled in clear weather with delay < 5 minutes."
    else:
        expl = "No van meets the criteria."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All vehicles with a distance traveled greater than 240 km had an average speed less than 60 kph."""
    long = df[df["distance_km"] > 240]
    if long.empty:
        return True, "No vehicles with distance > 240 km, so the statement holds vacuously."
    condition = long["avg_speed_kph"] < 60
    truth = condition.all()
    if truth:
        expl = f"All {len(long)} vehicles with distance > 240 km had avg speed < 60 kph."
    else:
        viol = long[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (avg speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle traveled in cloudy weather, then its fuel used is greater than 30 liters."""
    cloudy = df[df["weather"] == "cloudy"]
    if cloudy.empty:
        return True, "No vehicles traveled in cloudy weather, so the statement holds vacuously."
    condition = cloudy["fuel_used_l"] > 30
    truth = condition.all()
    if truth:
        expl = f"All {len(cloudy)} vehicles that traveled in cloudy weather had fuel used > 30 liters."
    else:
        viol = cloudy[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most vehicles had a distance traveled greater than 150 km."""
    condition = df["distance_km"] > 150
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of vehicles had distance > 150 km."
    else:
        expl = f"Only {proportion*100:.1f}% of vehicles had distance > 150 km."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All vehicles with a delay greater than 25 minutes had a fuel used less than 50 liters."""
    delayed = df[df["delay_minutes"] > 25]
    if delayed.empty:
        return True, "No vehicles with delay > 25 minutes, so the statement holds vacuously."
    condition = delayed["fuel_used_l"] < 50
    truth = condition.all()
    if truth:
        expl = f"All {len(delayed)} vehicles with delay > 25 minutes had fuel used < 50 liters."
    else:
        viol = delayed[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a truck, then its average speed is less than 60 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        return True, "No trucks in the data, so the statement holds vacuously."
    condition = trucks["avg_speed_kph"] < 60
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks had avg speed < 60 kph."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} truck(s) violate the rule (avg speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one bus that traveled in clear weather with a fuel used greater than 30 liters."""
    condition = (df["vehicle_type"] == "bus") & (df["weather"] == "clear") & (df["fuel_used_l"] > 30)
    exists = condition.any()
    if exists:
        count = condition.sum()
        expl = f"Found {count} bus(es) that traveled in clear weather with fuel used > 30 liters."
    else:
        expl = "No bus meets the criteria."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. All vehicles that traveled in windy weather had a fuel used less than 50 liters."""
    windy = df[df["weather"] == "windy"]
    if windy.empty:
        return True, "No vehicles traveled in windy weather, so the statement holds vacuously."
    condition = windy["fuel_used_l"] < 50
    truth = condition.all()
    if truth:
        expl = f"All {len(windy)} vehicles that traveled in windy weather had fuel used < 50 liters."
    else:
        viol = windy[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a vehicle traveled in clear weather, then its delay is less than 30 minutes."""
    clear = df[df["weather"] == "clear"]
    if clear.empty:
        return True, "No vehicles traveled in clear weather, so the statement holds vacuously."
    condition = clear["delay_minutes"] < 30
    truth = condition.all()
    if truth:
        expl = f"All {len(clear)} vehicles that traveled in clear weather had delay < 30 minutes."
    else:
        viol = clear[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most vehicles had an average speed greater than 50 kph."""
    condition = df["avg_speed_kph"] > 50
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of vehicles had avg speed > 50 kph."
    else:
        expl = f"Only {proportion*100:.1f}% of vehicles had avg speed > 50 kph."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_83.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()