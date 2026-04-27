import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles with a distance greater than 200 km have an average speed less than 65 kph."""
    condition = (df['distance_km'] > 200) & (df['avg_speed_kph'] >= 65)
    truth = not condition.any()
    if truth:
        expl = "No vehicles with distance > 200 km have avg speed >= 65 kph."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (distance > 200 km and avg speed >= 65 kph)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a truck, then its fuel used is less than 30 liters."""
    trucks = df[df['vehicle_type'] == 'truck']
    if trucks.empty:
        truth = True
        expl = "No trucks in dataset."
    else:
        condition = trucks['fuel_used_l'] >= 30
        truth = not condition.any()
        if truth:
            expl = f"All {len(trucks)} trucks have fuel used < 30 liters."
        else:
            viol = trucks[condition]
            expl = f"{len(viol)} trucks violate the rule (fuel used >= 30 liters)."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one van with a delay of less than 5 minutes."""
    vans = df[df['vehicle_type'] == 'van']
    if vans.empty:
        truth = False
        expl = "No vans in dataset."
    else:
        condition = vans['delay_minutes'] < 5
        truth = condition.any()
        if truth:
            expl = "At least one van has delay < 5 minutes."
        else:
            expl = "No vans have delay < 5 minutes."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All buses have a distance less than 150 km."""
    buses = df[df['vehicle_type'] == 'bus']
    if buses.empty:
        truth = True
        expl = "No buses in dataset."
    else:
        condition = buses['distance_km'] >= 150
        truth = not condition.any()
        if truth:
            expl = f"All {len(buses)} buses have distance < 150 km."
        else:
            viol = buses[condition]
            expl = f"{len(viol)} buses violate the rule (distance >= 150 km)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle is a van, then its average speed is less than 60 kph."""
    vans = df[df['vehicle_type'] == 'van']
    if vans.empty:
        truth = True
        expl = "No vans in dataset."
    else:
        condition = vans['avg_speed_kph'] >= 60
        truth = not condition.any()
        if truth:
            expl = f"All {len(vans)} vans have avg speed < 60 kph."
        else:
            viol = vans[condition]
            expl = f"{len(viol)} vans violate the rule (avg speed >= 60 kph)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most vehicles have a delay greater than 15 minutes."""
    total = len(df)
    condition = df['delay_minutes'] <= 15
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"More than half ({total - count}/{total}) of vehicles have delay > 15 minutes."
    else:
        expl = f"Half or fewer ({count}/{total}) of vehicles have delay > 15 minutes."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All vehicles with a distance less than 100 km have a fuel used greater than 10 liters."""
    condition = (df['distance_km'] < 100) & (df['fuel_used_l'] <= 10)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with distance < 100 km have fuel used > 10 liters."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (distance < 100 km and fuel used <= 10 liters)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a truck, then its average speed is less than 55 kph."""
    trucks = df[df['vehicle_type'] == 'truck']
    if trucks.empty:
        truth = True
        expl = "No trucks in dataset."
    else:
        condition = trucks['avg_speed_kph'] >= 55
        truth = not condition.any()
        if truth:
            expl = f"All {len(trucks)} trucks have avg speed < 55 kph."
        else:
            viol = trucks[condition]
            expl = f"{len(viol)} trucks violate the rule (avg speed >= 55 kph)."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one bus with a fuel used less than 10 liters."""
    buses = df[df['vehicle_type'] == 'bus']
    if buses.empty:
        truth = False
        expl = "No buses in dataset."
    else:
        condition = buses['fuel_used_l'] < 10
        truth = condition.any()
        if truth:
            expl = "At least one bus has fuel used < 10 liters."
        else:
            expl = "No buses have fuel used < 10 liters."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All vehicles with a distance greater than 150 km have a delay greater than 10 minutes."""
    condition = (df['distance_km'] > 150) & (df['delay_minutes'] <= 10)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with distance > 150 km have delay > 10 minutes."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (distance > 150 km and delay <= 10 minutes)."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle is a van, then its distance is less than 250 km."""
    vans = df[df['vehicle_type'] == 'van']
    if vans.empty:
        truth = True
        expl = "No vans in dataset."
    else:
        condition = vans['distance_km'] >= 250
        truth = not condition.any()
        if truth:
            expl = f"All {len(vans)} vans have distance < 250 km."
        else:
            viol = vans[condition]
            expl = f"{len(viol)} vans violate the rule (distance >= 250 km)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most trucks have a distance greater than 150 km."""
    trucks = df[df['vehicle_type'] == 'truck']
    if trucks.empty:
        truth = False
        expl = "No trucks in dataset."
    else:
        total = len(trucks)
        condition = trucks['distance_km'] <= 150
        count = condition.sum()
        truth = count < total / 2
        if truth:
            expl = f"More than half ({total - count}/{total}) of trucks have distance > 150 km."
        else:
            expl = f"Half or fewer ({count}/{total}) of trucks have distance > 150 km."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All vehicles with an average speed greater than 60 kph have a fuel used greater than 20 liters."""
    condition = (df['avg_speed_kph'] > 60) & (df['fuel_used_l'] <= 20)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with avg speed > 60 kph have fuel used > 20 liters."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (avg speed > 60 kph and fuel used <= 20 liters)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a bus, then its delay is greater than 15 minutes."""
    buses = df[df['vehicle_type'] == 'bus']
    if buses.empty:
        truth = True
        expl = "No buses in dataset."
    else:
        condition = buses['delay_minutes'] <= 15
        truth = not condition.any()
        if truth:
            expl = f"All {len(buses)} buses have delay > 15 minutes."
        else:
            viol = buses[condition]
            expl = f"{len(viol)} buses violate the rule (delay <= 15 minutes)."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one truck with a delay less than 15 minutes."""
    trucks = df[df['vehicle_type'] == 'truck']
    if trucks.empty:
        truth = False
        expl = "No trucks in dataset."
    else:
        condition = trucks['delay_minutes'] < 15
        truth = condition.any()
        if truth:
            expl = "At least one truck has delay < 15 minutes."
        else:
            expl = "No trucks have delay < 15 minutes."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All vehicles with a distance less than 200 km have an average speed less than 65 kph."""
    condition = (df['distance_km'] < 200) & (df['avg_speed_kph'] >= 65)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with distance < 200 km have avg speed < 65 kph."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (distance < 200 km and avg speed >= 65 kph)."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a vehicle is a van, then its fuel used is greater than 20 liters."""
    vans = df[df['vehicle_type'] == 'van']
    if vans.empty:
        truth = True
        expl = "No vans in dataset."
    else:
        condition = vans['fuel_used_l'] <= 20
        truth = not condition.any()
        if truth:
            expl = f"All {len(vans)} vans have fuel used > 20 liters."
        else:
            viol = vans[condition]
            expl = f"{len(viol)} vans violate the rule (fuel used <= 20 liters)."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most vehicles have an average speed less than 60 kph."""
    total = len(df)
    condition = df['avg_speed_kph'] >= 60
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"More than half ({total - count}/{total}) of vehicles have avg speed < 60 kph."
    else:
        expl = f"Half or fewer ({count}/{total}) of vehicles have avg speed < 60 kph."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All buses have a fuel used less than 40 liters."""
    buses = df[df['vehicle_type'] == 'bus']
    if buses.empty:
        truth = True
        expl = "No buses in dataset."
    else:
        condition = buses['fuel_used_l'] >= 40
        truth = not condition.any()
        if truth:
            expl = f"All {len(buses)} buses have fuel used < 40 liters."
        else:
            viol = buses[condition]
            expl = f"{len(viol)} buses violate the rule (fuel used >= 40 liters)."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a vehicle is a truck, then its distance is greater than 100 km."""
    trucks = df[df['vehicle_type'] == 'truck']
    if trucks.empty:
        truth = True
        expl = "No trucks in dataset."
    else:
        condition = trucks['distance_km'] <= 100
        truth = not condition.any()
        if truth:
            expl = f"All {len(trucks)} trucks have distance > 100 km."
        else:
            viol = trucks[condition]
            expl = f"{len(viol)} trucks violate the rule (distance <= 100 km)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_63.csv")

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