import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles with a distance greater than 200 km have an average speed greater than 60 kph."""
    condition = (df["distance_km"] > 200) & (df["avg_speed_kph"] <= 60)
    truth = not condition.any()
    if truth:
        expl = "No vehicle with distance > 200 km has avg speed <= 60 kph."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate this rule (distance > 200 but speed <= 60)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a bus, then its fuel used is less than 50 liters."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        expl = "No buses in dataset."
        return True, expl
    condition = buses["fuel_used_l"] >= 50
    truth = not condition.any()
    if truth:
        expl = "All buses use < 50 liters."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} bus(es) violate this rule (fuel >= 50)."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one truck with a delay of less than 12 minutes."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        expl = "No trucks in dataset."
        return False, expl
    condition = trucks["delay_minutes"] < 12
    truth = condition.any()
    if truth:
        expl = "At least one truck has delay < 12 minutes."
    else:
        expl = "No truck has delay < 12 minutes."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All vans with a distance less than 120 km have an average speed greater than 50 kph."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        expl = "No vans in dataset."
        return True, expl
    condition = (vans["distance_km"] < 120) & (vans["avg_speed_kph"] <= 50)
    truth = not condition.any()
    if truth:
        expl = "All vans with distance < 120 km have speed > 50 kph."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} van(s) violate this rule (distance < 120 but speed <= 50)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle is a truck, then its average speed is less than 60 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        expl = "No trucks in dataset."
        return True, expl
    condition = trucks["avg_speed_kph"] >= 60
    truth = not condition.any()
    if truth:
        expl = "All trucks have speed < 60 kph."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} truck(s) violate this rule (speed >= 60)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most vehicles have a delay of less than 20 minutes."""
    condition = df["delay_minutes"] < 20
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} vehicles have delay < 20 minutes (>50%)."
    else:
        expl = f"{count} out of {total} vehicles have delay < 20 minutes (<=50%)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All vehicles with a distance greater than 180 km have a fuel used greater than 30 liters."""
    condition = (df["distance_km"] > 180) & (df["fuel_used_l"] <= 30)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with distance > 180 km use > 30 liters."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate this rule (distance > 180 but fuel <= 30)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a van, then its distance is greater than 100 km."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        expl = "No vans in dataset."
        return True, expl
    condition = vans["distance_km"] <= 100
    truth = not condition.any()
    if truth:
        expl = "All vans have distance > 100 km."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} van(s) violate this rule (distance <= 100)."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one vehicle with a delay of less than 5 minutes."""
    condition = df["delay_minutes"] < 5
    truth = condition.any()
    if truth:
        expl = "At least one vehicle has delay < 5 minutes."
    else:
        expl = "No vehicle has delay < 5 minutes."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All buses have a distance greater than 180 km."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        expl = "No buses in dataset."
        return True, expl
    condition = buses["distance_km"] <= 180
    truth = not condition.any()
    if truth:
        expl = "All buses have distance > 180 km."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} bus(es) violate this rule (distance <= 180)."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle is a truck, then its fuel used is greater than 40 liters."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        expl = "No trucks in dataset."
        return True, expl
    condition = trucks["fuel_used_l"] <= 40
    truth = not condition.any()
    if truth:
        expl = "All trucks use > 40 liters."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} truck(s) violate this rule (fuel <= 40)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most vehicles have an average speed greater than 50 kph."""
    condition = df["avg_speed_kph"] > 50
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} vehicles have speed > 50 kph (>50%)."
    else:
        expl = f"{count} out of {total} vehicles have speed > 50 kph (<=50%)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All vehicles with a distance less than 100 km have a fuel used less than 20 liters."""
    condition = (df["distance_km"] < 100) & (df["fuel_used_l"] >= 20)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with distance < 100 km use < 20 liters."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate this rule (distance < 100 but fuel >= 20)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a van, then its average speed is greater than 45 kph."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        expl = "No vans in dataset."
        return True, expl
    condition = vans["avg_speed_kph"] <= 45
    truth = not condition.any()
    if truth:
        expl = "All vans have speed > 45 kph."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} van(s) violate this rule (speed <= 45)."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one vehicle with an average speed greater than 65 kph."""
    condition = df["avg_speed_kph"] > 65
    truth = condition.any()
    if truth:
        expl = "At least one vehicle has speed > 65 kph."
    else:
        expl = "No vehicle has speed > 65 kph."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All vehicles with a delay greater than 20 minutes have a distance greater than 150 km."""
    condition = (df["delay_minutes"] > 20) & (df["distance_km"] <= 150)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with delay > 20 minutes have distance > 150 km."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate this rule (delay > 20 but distance <= 150)."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a vehicle is a bus, then its delay is greater than 10 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        expl = "No buses in dataset."
        return True, expl
    condition = buses["delay_minutes"] <= 10
    truth = not condition.any()
    if truth:
        expl = "All buses have delay > 10 minutes."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} bus(es) violate this rule (delay <= 10)."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most vehicles have a distance greater than 100 km."""
    condition = df["distance_km"] > 100
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} vehicles have distance > 100 km (>50%)."
    else:
        expl = f"{count} out of {total} vehicles have distance > 100 km (<=50%)."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All vehicles with a fuel used less than 20 liters have a distance less than 150 km."""
    condition = (df["fuel_used_l"] < 20) & (df["distance_km"] >= 150)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with fuel < 20 liters have distance < 150 km."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate this rule (fuel < 20 but distance >= 150)."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a vehicle is a truck, then its distance is less than 150 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        expl = "No trucks in dataset."
        return True, expl
    condition = trucks["distance_km"] >= 150
    truth = not condition.any()
    if truth:
        expl = "All trucks have distance < 150 km."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} truck(s) violate this rule (distance >= 150)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_73.csv")

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
        (16, stmt_16),
        (17, stmt_17),
        (18, stmt_18),
        (19, stmt_19),
        (20, stmt_20)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()