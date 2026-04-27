import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles that traveled in windy weather had an average speed of less than 60 kph."""
    windy = df[df["weather"] == "windy"]
    if windy.empty:
        return True, "No vehicles traveled in windy weather."
    condition = windy["avg_speed_kph"] < 60
    truth = condition.all()
    if truth:
        expl = f"All {len(windy)} windy vehicles have avg_speed < 60 kph."
    else:
        viol = windy[~condition]
        expl = f"{len(viol)} windy vehicles violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a bus, then its fuel used is greater than 10 liters."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        return True, "No buses in the data."
    condition = buses["fuel_used_l"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have fuel_used > 10 liters."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one truck that traveled a distance of more than 160 km."""
    exists = df[(df["vehicle_type"] == "truck") & (df["distance_km"] > 160)].any(axis=1).any()
    if exists:
        expl = "At least one truck traveled > 160 km."
    else:
        expl = "No truck traveled > 160 km."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All vehicles that had a delay of less than 10 minutes had an average speed of greater than 50 kph."""
    early = df[df["delay_minutes"] < 10]
    if early.empty:
        return True, "No vehicles with delay < 10 minutes."
    condition = early["avg_speed_kph"] > 50
    truth = condition.all()
    if truth:
        expl = f"All {len(early)} vehicles with delay < 10 min have avg_speed > 50 kph."
    else:
        viol = early[~condition]
        expl = f"{len(viol)} vehicles violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle is a van, then its distance traveled is less than 200 km."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        return True, "No vans in the data."
    condition = vans["distance_km"] < 200
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans have distance < 200 km."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most vehicles that traveled in clear weather had an average speed of greater than 55 kph."""
    clear = df[df["weather"] == "clear"]
    if clear.empty:
        return True, "No vehicles with clear weather."
    condition = clear["avg_speed_kph"] > 55
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of clear-weather vehicles have avg_speed > 55 kph."
    else:
        expl = f"Only {proportion*100:.1f}% of clear-weather vehicles have avg_speed > 55 kph."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All buses that traveled a distance of more than 200 km had a fuel used of greater than 25 liters."""
    buses = df[(df["vehicle_type"] == "bus") & (df["distance_km"] > 200)]
    if buses.empty:
        return True, "No buses traveled > 200 km."
    condition = buses["fuel_used_l"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses with distance > 200 km have fuel_used > 25 liters."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle had a delay of more than 20 minutes, then its average speed was less than 55 kph."""
    delayed = df[df["delay_minutes"] > 20]
    if delayed.empty:
        return True, "No vehicles with delay > 20 minutes."
    condition = delayed["avg_speed_kph"] < 55
    truth = condition.all()
    if truth:
        expl = f"All {len(delayed)} vehicles with delay > 20 min have avg_speed < 55 kph."
    else:
        viol = delayed[~condition]
        expl = f"{len(viol)} vehicles violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one bus that traveled in rainy weather and had a fuel used of more than 30 liters."""
    exists = df[(df["vehicle_type"] == "bus") & (df["weather"] == "rain") & (df["fuel_used_l"] > 30)].any(axis=1).any()
    if exists:
        expl = "At least one bus traveled in rain with fuel_used > 30 liters."
    else:
        expl = "No such bus found."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All trucks that had an average speed of greater than 55 kph had a distance traveled of less than 180 km."""
    trucks = df[(df["vehicle_type"] == "truck") & (df["avg_speed_kph"] > 55)]
    if trucks.empty:
        return True, "No trucks with avg_speed > 55 kph."
    condition = trucks["distance_km"] < 180
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks with avg_speed > 55 kph have distance < 180 km."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle had a fuel used of less than 15 liters, then its distance traveled was less than 150 km."""
    low_fuel = df[df["fuel_used_l"] < 15]
    if low_fuel.empty:
        return True, "No vehicles with fuel_used < 15 liters."
    condition = low_fuel["distance_km"] < 150
    truth = condition.all()
    if truth:
        expl = f"All {len(low_fuel)} vehicles with fuel_used < 15 liters have distance < 150 km."
    else:
        viol = low_fuel[~condition]
        expl = f"{len(viol)} vehicles violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most vehicles that had a delay of more than 15 minutes had a fuel used of greater than 20 liters."""
    delayed = df[df["delay_minutes"] > 15]
    if delayed.empty:
        return True, "No vehicles with delay > 15 minutes."
    condition = delayed["fuel_used_l"] > 20
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of vehicles with delay > 15 min have fuel_used > 20 liters."
    else:
        expl = f"Only {proportion*100:.1f}% of vehicles with delay > 15 min have fuel_used > 20 liters."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All vehicles that traveled in cloudy weather had a delay of more than 10 minutes."""
    cloudy = df[df["weather"] == "cloudy"]
    if cloudy.empty:
        return True, "No vehicles with cloudy weather."
    condition = cloudy["delay_minutes"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(cloudy)} cloudy vehicles have delay > 10 minutes."
    else:
        viol = cloudy[~condition]
        expl = f"{len(viol)} vehicles violate the rule (delay: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a truck, then its average speed is less than 60 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        return True, "No trucks in the data."
    condition = trucks["avg_speed_kph"] < 60
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have avg_speed < 60 kph."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one van that had a fuel used of more than 35 liters and traveled a distance of less than 100 km."""
    exists = df[(df["vehicle_type"] == "van") & (df["fuel_used_l"] > 35) & (df["distance_km"] < 100)].any(axis=1).any()
    if exists:
        expl = "At least one van has fuel_used > 35 liters and distance < 100 km."
    else:
        expl = "No such van found."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. All buses that had an average speed of greater than 60 kph had a distance traveled of less than 150 km."""
    buses = df[(df["vehicle_type"] == "bus") & (df["avg_speed_kph"] > 60)]
    if buses.empty:
        return True, "No buses with avg_speed > 60 kph."
    condition = buses["distance_km"] < 150
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses with avg_speed > 60 kph have distance < 150 km."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a vehicle had a delay of less than 5 minutes, then its average speed was greater than 50 kph."""
    early = df[df["delay_minutes"] < 5]
    if early.empty:
        return True, "No vehicles with delay < 5 minutes."
    condition = early["avg_speed_kph"] > 50
    truth = condition.all()
    if truth:
        expl = f"All {len(early)} vehicles with delay < 5 min have avg_speed > 50 kph."
    else:
        viol = early[~condition]
        expl = f"{len(viol)} vehicles violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_43.csv")

    # Convert numeric columns safely, skip route_id
    for col in df.columns:
        if col!= "route_id":
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
        (17, stmt_17),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()