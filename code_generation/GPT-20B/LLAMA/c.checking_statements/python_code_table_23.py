import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles with a distance greater than 200 km have an average speed less than 60 kph."""
    mask = df["distance_km"] > 200
    if mask.any():
        condition = df.loc[mask, "avg_speed_kph"] < 60
        truth = condition.all()
        if truth:
            expl = f"All {mask.sum()} vehicles with distance >200 km have avg_speed <60 kph."
        else:
            viol = df.loc[mask & ~condition]
            expl = f"{len(viol)} vehicles violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph']))})."
    else:
        truth = True
        expl = "No vehicles with distance >200 km, so the statement holds vacuously."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a truck, then its fuel used is greater than 30 liters."""
    trucks = df[df["vehicle_type"] == "truck"]
    if not trucks.empty:
        condition = trucks["fuel_used_l"] > 30
        truth = condition.all()
        if truth:
            expl = f"All {len(trucks)} trucks have fuel_used >30 liters."
        else:
            viol = trucks[~condition]
            expl = f"{len(viol)} trucks violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l']))})."
    else:
        truth = True
        expl = "No trucks present, so the statement holds vacuously."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one bus with a delay of less than 15 minutes."""
    condition = (df["vehicle_type"] == "bus") & (df["delay_minutes"] < 15)
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"Found {count} bus(es) with delay <15 minutes."
    else:
        expl = "No bus with delay <15 minutes found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All vans have a distance greater than 100 km."""
    vans = df[df["vehicle_type"] == "van"]
    if not vans.empty:
        condition = vans["distance_km"] > 100
        truth = condition.all()
        if truth:
            expl = f"All {len(vans)} vans have distance >100 km."
        else:
            viol = vans[~condition]
            expl = f"{len(viol)} van(s) violate the rule (distance: {', '.join(map(str, viol['distance_km']))})."
    else:
        truth = True
        expl = "No vans present, so the statement holds vacuously."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle is a bus, then its average speed is greater than 50 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    if not buses.empty:
        condition = buses["avg_speed_kph"] > 50
        truth = condition.all()
        if truth:
            expl = f"All {len(buses)} buses have avg_speed >50 kph."
        else:
            viol = buses[~condition]
            expl = f"{len(viol)} bus(es) violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph']))})."
    else:
        truth = True
        expl = "No buses present, so the statement holds vacuously."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most vehicles have a delay of less than 20 minutes."""
    condition = df["delay_minutes"] < 20
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of vehicles have delay <20 minutes."
    else:
        expl = f"Only {proportion*100:.1f}% of vehicles have delay <20 minutes."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All vehicles with a distance less than 150 km have an average speed greater than 50 kph."""
    mask = df["distance_km"] < 150
    if mask.any():
        condition = df.loc[mask, "avg_speed_kph"] > 50
        truth = condition.all()
        if truth:
            expl = f"All {mask.sum()} vehicles with distance <150 km have avg_speed >50 kph."
        else:
            viol = df.loc[mask & ~condition]
            expl = f"{len(viol)} vehicles violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph']))})."
    else:
        truth = True
        expl = "No vehicles with distance <150 km, so the statement holds vacuously."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a truck, then its distance is less than 250 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    if not trucks.empty:
        condition = trucks["distance_km"] < 250
        truth = condition.all()
        if truth:
            expl = f"All {len(trucks)} trucks have distance <250 km."
        else:
            viol = trucks[~condition]
            expl = f"{len(viol)} truck(s) violate the rule (distance: {', '.join(map(str, viol['distance_km']))})."
    else:
        truth = True
        expl = "No trucks present, so the statement holds vacuously."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one vehicle with a fuel used of less than 10 liters."""
    condition = df["fuel_used_l"] < 10
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"Found {count} vehicle(s) with fuel_used <10 liters."
    else:
        expl = "No vehicle with fuel_used <10 liters found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All vehicles with an average speed greater than 60 kph have a distance less than 200 km."""
    mask = df["avg_speed_kph"] > 60
    if mask.any():
        condition = df.loc[mask, "distance_km"] < 200
        truth = condition.all()
        if truth:
            expl = f"All {mask.sum()} vehicles with avg_speed >60 kph have distance <200 km."
        else:
            viol = df.loc[mask & ~condition]
            expl = f"{len(viol)} vehicle(s) violate the rule (distance: {', '.join(map(str, viol['distance_km']))})."
    else:
        truth = True
        expl = "No vehicles with avg_speed >60 kph, so the statement holds vacuously."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle is a van, then its fuel used is greater than 20 liters."""
    vans = df[df["vehicle_type"] == "van"]
    if not vans.empty:
        condition = vans["fuel_used_l"] > 20
        truth = condition.all()
        if truth:
            expl = f"All {len(vans)} vans have fuel_used >20 liters."
        else:
            viol = vans[~condition]
            expl = f"{len(viol)} van(s) violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l']))})."
    else:
        truth = True
        expl = "No vans present, so the statement holds vacuously."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most vehicles have an average speed less than 60 kph."""
    condition = df["avg_speed_kph"] < 60
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of vehicles have avg_speed <60 kph."
    else:
        expl = f"Only {proportion*100:.1f}% of vehicles have avg_speed <60 kph."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All buses have a distance greater than 120 km."""
    buses = df[df["vehicle_type"] == "bus"]
    if not buses.empty:
        condition = buses["distance_km"] > 120
        truth = condition.all()
        if truth:
            expl = f"All {len(buses)} buses have distance >120 km."
        else:
            viol = buses[~condition]
            expl = f"{len(viol)} bus(es) violate the rule (distance: {', '.join(map(str, viol['distance_km']))})."
    else:
        truth = True
        expl = "No buses present, so the statement holds vacuously."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a truck, then its delay is greater than 10 minutes."""
    trucks = df[df["vehicle_type"] == "truck"]
    if not trucks.empty:
        condition = trucks["delay_minutes"] > 10
        truth = condition.all()
        if truth:
            expl = f"All {len(trucks)} trucks have delay >10 minutes."
        else:
            viol = trucks[~condition]
            expl = f"{len(viol)} truck(s) violate the rule (delay: {', '.join(map(str, viol['delay_minutes']))})."
    else:
        truth = True
        expl = "No trucks present, so the statement holds vacuously."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one vehicle with a delay of less than 5 minutes."""
    condition = df["delay_minutes"] < 5
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"Found {count} vehicle(s) with delay <5 minutes."
    else:
        expl = "No vehicle with delay <5 minutes found."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All vehicles with a distance greater than 150 km have a fuel used greater than 15 liters."""
    mask = df["distance_km"] > 150
    if mask.any():
        condition = df.loc[mask, "fuel_used_l"] > 15
        truth = condition.all()
        if truth:
            expl = f"All {mask.sum()} vehicles with distance >150 km have fuel_used >15 liters."
        else:
            viol = df.loc[mask & ~condition]
            expl = f"{len(viol)} vehicle(s) violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l']))})."
    else:
        truth = True
        expl = "No vehicles with distance >150 km, so the statement holds vacuously."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a vehicle is a bus, then its fuel used is less than 50 liters."""
    buses = df[df["vehicle_type"] == "bus"]
    if not buses.empty:
        condition = buses["fuel_used_l"] < 50
        truth = condition.all()
        if truth:
            expl = f"All {len(buses)} buses have fuel_used <50 liters."
        else:
            viol = buses[~condition]
            expl = f"{len(viol)} bus(es) violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l']))})."
    else:
        truth = True
        expl = "No buses present, so the statement holds vacuously."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_23.csv")

    # Convert numeric columns safely, keep vehicle_type as string
    for col in df.columns:
        if col!= "vehicle_type":
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