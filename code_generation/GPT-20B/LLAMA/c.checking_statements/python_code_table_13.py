import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles with an average speed greater than 62 kph have a fuel usage less than 25 liters."""
    subset = df[df["avg_speed_kph"] > 62]
    if subset.empty:
        return True, "No vehicles have avg_speed > 62, so the statement holds vacuously."
    condition = subset["fuel_used_l"] < 25
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vehicles with avg_speed > 62 have fuel_used_l < 25."
    viol = subset[~condition]
    return False, f"{len(viol)} vehicles violate the rule (fuel_used_l: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a truck, then its average speed is greater than 52 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        return True, "No trucks present, so the statement holds vacuously."
    condition = trucks["avg_speed_kph"] > 52
    truth = condition.all()
    if truth:
        return True, f"All {len(trucks)} trucks have avg_speed > 52."
    viol = trucks[~condition]
    return False, f"{len(viol)} trucks violate the rule (avg_speed_kph: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. All buses with a distance greater than 200 km have an average speed greater than 53 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    subset = buses[buses["distance_km"] > 200]
    if subset.empty:
        return True, "No buses have distance > 200 km, so the statement holds vacuously."
    condition = subset["avg_speed_kph"] > 53
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} buses with distance > 200 km have avg_speed > 53."
    viol = subset[~condition]
    return False, f"{len(viol)} buses violate the rule (avg_speed_kph: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one van with a fuel usage greater than 32 liters."""
    vans = df[df["vehicle_type"] == "van"]
    exists = (vans["fuel_used_l"] > 32).any()
    if exists:
        count = vans[vans["fuel_used_l"] > 32].shape[0]
        return True, f"Found {count} van(s) with fuel_used_l > 32."
    return False, "No van has fuel_used_l > 32."

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle is a bus, then its delay is less than 27 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        return True, "No buses present, so the statement holds vacuously."
    condition = buses["delay_minutes"] < 27
    truth = condition.all()
    if truth:
        return True, f"All {len(buses)} buses have delay < 27 minutes."
    viol = buses[~condition]
    return False, f"{len(viol)} buses violate the rule (delay_minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."

def stmt_6(df: pd.DataFrame):
    """6. All vehicles with a distance less than 150 km have a fuel usage greater than 30 liters."""
    subset = df[df["distance_km"] < 150]
    if subset.empty:
        return True, "No vehicles have distance < 150 km, so the statement holds vacuously."
    condition = subset["fuel_used_l"] > 30
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vehicles with distance < 150 km have fuel_used_l > 30."
    viol = subset[~condition]
    return False, f"{len(viol)} vehicles violate the rule (fuel_used_l: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."

def stmt_7(df: pd.DataFrame):
    """7. Most vehicles have a delay less than 10 minutes."""
    total = len(df)
    if total == 0:
        return True, "No vehicles present, so the statement holds vacuously."
    count = (df["delay_minutes"] < 10).sum()
    truth = count > total / 2
    if truth:
        return True, f"{count} out of {total} vehicles have delay < 10 minutes."
    return False, f"Only {count} out of {total} vehicles have delay < 10 minutes."

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a truck, then its distance is greater than 90 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        return True, "No trucks present, so the statement holds vacuously."
    condition = trucks["distance_km"] > 90
    truth = condition.all()
    if truth:
        return True, f"All {len(trucks)} trucks have distance > 90 km."
    viol = trucks[~condition]
    return False, f"{len(viol)} trucks violate the rule (distance_km: {', '.join(map(str, viol['distance_km'].tolist()))})."

def stmt_9(df: pd.DataFrame):
    """9. All vehicles with an average speed greater than 60 kph have a fuel usage less than 40 liters."""
    subset = df[df["avg_speed_kph"] > 60]
    if subset.empty:
        return True, "No vehicles have avg_speed > 60 kph, so the statement holds vacuously."
    condition = subset["fuel_used_l"] < 40
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vehicles with avg_speed > 60 have fuel_used_l < 40."
    viol = subset[~condition]
    return False, f"{len(viol)} vehicles violate the rule (fuel_used_l: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one bus with an average speed greater than 64 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    exists = (buses["avg_speed_kph"] > 64).any()
    if exists:
        count = buses[buses["avg_speed_kph"] > 64].shape[0]
        return True, f"Found {count} bus(es) with avg_speed_kph > 64."
    return False, "No bus has avg_speed_kph > 64."

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle is a van, then its average speed is greater than 48 kph."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        return True, "No vans present, so the statement holds vacuously."
    condition = vans["avg_speed_kph"] > 48
    truth = condition.all()
    if truth:
        return True, f"All {len(vans)} vans have avg_speed > 48 kph."
    viol = vans[~condition]
    return False, f"{len(viol)} vans violate the rule (avg_speed_kph: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."

def stmt_12(df: pd.DataFrame):
    """12. All vehicles with a fuel usage less than 20 liters have an average speed greater than 60 kph."""
    subset = df[df["fuel_used_l"] < 20]
    if subset.empty:
        return True, "No vehicles have fuel_used_l < 20, so the statement holds vacuously."
    condition = subset["avg_speed_kph"] > 60
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vehicles with fuel_used_l < 20 have avg_speed > 60."
    viol = subset[~condition]
    return False, f"{len(viol)} vehicles violate the rule (avg_speed_kph: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."

def stmt_13(df: pd.DataFrame):
    """13. Most vehicles have an average speed greater than 50 kph."""
    total = len(df)
    if total == 0:
        return True, "No vehicles present, so the statement holds vacuously."
    count = (df["avg_speed_kph"] > 50).sum()
    truth = count > total / 2
    if truth:
        return True, f"{count} out of {total} vehicles have avg_speed > 50 kph."
    return False, f"Only {count} out of {total} vehicles have avg_speed > 50 kph."

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a bus, then its distance is greater than 100 km."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        return True, "No buses present, so the statement holds vacuously."
    condition = buses["distance_km"] > 100
    truth = condition.all()
    if truth:
        return True, f"All {len(buses)} buses have distance > 100 km."
    viol = buses[~condition]
    return False, f"{len(viol)} buses violate the rule (distance_km: {', '.join(map(str, viol['distance_km'].tolist()))})."

def stmt_15(df: pd.DataFrame):
    """15. All vehicles with a delay greater than 20 minutes have a weather condition of rain."""
    subset = df[df["delay_minutes"] > 20]
    if subset.empty:
        return True, "No vehicles have delay > 20 minutes, so the statement holds vacuously."
    condition = subset["weather"].str.lower() == "rain"
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vehicles with delay > 20 minutes have weather 'rain'."
    viol = subset[~condition]
    return False, f"{len(viol)} vehicles violate the rule (weather: {', '.join(map(str, viol['weather'].tolist()))})."

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one truck with a fuel usage less than 10 liters."""
    trucks = df[df["vehicle_type"] == "truck"]
    exists = (trucks["fuel_used_l"] < 10).any()
    if exists:
        count = trucks[trucks["fuel_used_l"] < 10].shape[0]
        return True, f"Found {count} truck(s) with fuel_used_l < 10."
    return False, "No truck has fuel_used_l < 10."

def main():
    df = pd.read_csv("../inference_generation/tables/table_13.csv")

    # Convert numeric columns safely
    numeric_cols = ["distance_km", "avg_speed_kph", "fuel_used_l", "delay_minutes"]
    for col in numeric_cols:
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