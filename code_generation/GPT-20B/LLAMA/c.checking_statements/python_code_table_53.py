import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles that traveled in clear weather had an average speed greater than 45 kph."""
    clear = df[df["weather"] == "clear"]
    if clear.empty:
        return True, "No vehicles traveled in clear weather, statement vacuously true."
    condition = clear["avg_speed_kph"] > 45
    truth = condition.all()
    if truth:
        expl = f"All {len(clear)} vehicles in clear weather have avg speed > 45 kph."
    else:
        viol = clear[~condition]
        expl = f"{len(viol)} vehicles in clear weather violate the rule (avg speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a van, then its fuel used is less than 20 liters."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        return True, "No vans in dataset, statement vacuously true."
    condition = vans["fuel_used_l"] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans have fuel used < 20 liters."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one bus that traveled a distance greater than 180 km."""
    buses = df[(df["vehicle_type"] == "bus") & (df["distance_km"] > 180)]
    truth = not buses.empty
    if truth:
        expl = f"Found {len(buses)} bus(es) with distance > 180 km."
    else:
        expl = "No bus with distance > 180 km found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All trucks that traveled in windy weather had a delay of less than 17 minutes."""
    trucks_windy = df[(df["vehicle_type"] == "truck") & (df["weather"] == "windy")]
    if trucks_windy.empty:
        return True, "No trucks in windy weather, statement vacuously true."
    condition = trucks_windy["delay_minutes"] < 17
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks_windy)} trucks in windy weather have delay < 17 minutes."
    else:
        viol = trucks_windy[~condition]
        expl = f"{len(viol)} truck(s) violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle is a bus, then its average speed is greater than 51 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        return True, "No buses in dataset, statement vacuously true."
    condition = buses["avg_speed_kph"] > 51
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have avg speed > 51 kph."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} bus(es) violate the rule (avg speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most vehicles that traveled in rain had a delay of less than 22 minutes."""
    rain = df[df["weather"] == "rain"]
    if rain.empty:
        return True, "No vehicles in rain, statement vacuously true."
    condition = rain["delay_minutes"] < 22
    count = len(rain)
    satisfied = condition.sum()
    proportion = satisfied / count
    truth = proportion > 0.5
    if truth:
        expl = f"{satisfied} out of {count} rain vehicles have delay < 22 minutes ({proportion*100:.1f}%)."
    else:
        expl = f"{satisfied} out of {count} rain vehicles have delay < 22 minutes ({proportion*100:.1f}%)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All vehicles with a distance traveled greater than 200 km had an average speed greater than 50 kph."""
    long = df[df["distance_km"] > 200]
    if long.empty:
        return True, "No vehicles with distance > 200 km, statement vacuously true."
    condition = long["avg_speed_kph"] > 50
    truth = condition.all()
    if truth:
        expl = f"All {len(long)} vehicles with distance > 200 km have avg speed > 50 kph."
    else:
        viol = long[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (avg speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a truck, then its fuel used is greater than 13 liters."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        return True, "No trucks in dataset, statement vacuously true."
    condition = trucks["fuel_used_l"] > 13
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have fuel used > 13 liters."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} truck(s) violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one van that traveled a distance less than 70 km."""
    vans = df[(df["vehicle_type"] == "van") & (df["distance_km"] < 70)]
    truth = not vans.empty
    if truth:
        expl = f"Found {len(vans)} van(s) with distance < 70 km."
    else:
        expl = "No van with distance < 70 km found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All buses that traveled in clear weather had a fuel used greater than 20 liters."""
    buses_clear = df[(df["vehicle_type"] == "bus") & (df["weather"] == "clear")]
    if buses_clear.empty:
        return True, "No buses in clear weather, statement vacuously true."
    condition = buses_clear["fuel_used_l"] > 20
    truth = condition.all()
    if truth:
        expl = f"All {len(buses_clear)} buses in clear weather have fuel used > 20 liters."
    else:
        viol = buses_clear[~condition]
        expl = f"{len(viol)} bus(es) violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle's average speed is greater than 60 kph, then its delay is less than 15 minutes."""
    fast = df[df["avg_speed_kph"] > 60]
    if fast.empty:
        return True, "No vehicles with avg speed > 60 kph, statement vacuously true."
    condition = fast["delay_minutes"] < 15
    truth = condition.all()
    if truth:
        expl = f"All {len(fast)} vehicles with avg speed > 60 kph have delay < 15 minutes."
    else:
        viol = fast[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most vehicles that traveled in clear weather had an average speed greater than 50 kph."""
    clear = df[df["weather"] == "clear"]
    if clear.empty:
        return True, "No vehicles in clear weather, statement vacuously true."
    condition = clear["avg_speed_kph"] > 50
    count = len(clear)
    satisfied = condition.sum()
    proportion = satisfied / count
    truth = proportion > 0.5
    if truth:
        expl = f"{satisfied} out of {count} clear vehicles have avg speed > 50 kph ({proportion*100:.1f}%)."
    else:
        expl = f"{satisfied} out of {count} clear vehicles have avg speed > 50 kph ({proportion*100:.1f}%)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All vehicles with a delay of less than 10 minutes had an average speed greater than 45 kph."""
    early = df[df["delay_minutes"] < 10]
    if early.empty:
        return True, "No vehicles with delay < 10 minutes, statement vacuously true."
    condition = early["avg_speed_kph"] > 45
    truth = condition.all()
    if truth:
        expl = f"All {len(early)} vehicles with delay < 10 minutes have avg speed > 45 kph."
    else:
        viol = early[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (avg speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a bus, then its distance traveled is greater than 70 km."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        return True, "No buses in dataset, statement vacuously true."
    condition = buses["distance_km"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have distance > 70 km."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} bus(es) violate the rule (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one truck that traveled a distance greater than 220 km."""
    trucks = df[(df["vehicle_type"] == "truck") & (df["distance_km"] > 220)]
    truth = not trucks.empty
    if truth:
        expl = f"Found {len(trucks)} truck(s) with distance > 220 km."
    else:
        expl = "No truck with distance > 220 km found."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All vans that traveled in rain had a fuel used less than 20 liters."""
    vans_rain = df[(df["vehicle_type"] == "van") & (df["weather"] == "rain")]
    if vans_rain.empty:
        return True, "No vans in rain, statement vacuously true."
    condition = vans_rain["fuel_used_l"] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(vans_rain)} vans in rain have fuel used < 20 liters."
    else:
        viol = vans_rain[~condition]
        expl = f"{len(viol)} van(s) violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a vehicle's fuel used is greater than 30 liters, then its distance traveled is greater than 150 km."""
    high_fuel = df[df["fuel_used_l"] > 30]
    if high_fuel.empty:
        return True, "No vehicles with fuel used > 30 liters, statement vacuously true."
    condition = high_fuel["distance_km"] > 150
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fuel)} vehicles with fuel used > 30 liters have distance > 150 km."
    else:
        viol = high_fuel[~condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most vehicles that traveled in rain had a fuel used greater than 15 liters."""
    rain = df[df["weather"] == "rain"]
    if rain.empty:
        return True, "No vehicles in rain, statement vacuously true."
    condition = rain["fuel_used_l"] > 15
    count = len(rain)
    satisfied = condition.sum()
    proportion = satisfied / count
    truth = proportion > 0.5
    if truth:
        expl = f"{satisfied} out of {count} rain vehicles have fuel used > 15 liters ({proportion*100:.1f}%)."
    else:
        expl = f"{satisfied} out of {count} rain vehicles have fuel used > 15 liters ({proportion*100:.1f}%)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_53.csv")

    # Convert numeric columns safely.
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
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