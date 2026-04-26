import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles with an average speed greater than 62 kph have a fuel usage less than 25 liters."""
    condition = (df['avg_speed_kph'] > 62) & (df['fuel_used_l'] >= 25)
    truth = not condition.any()
    if truth:
        expl = "No vehicle with avg speed > 62 kph has fuel usage >= 25 liters."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate the rule: {viol[['route_id', 'avg_speed_kph', 'fuel_used_l']].to_dict('records')}"
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a truck, then its average speed is greater than 52 kph."""
    trucks = df[df['vehicle_type'] == 'truck']
    if trucks.empty:
        truth = True
        expl = "No trucks in dataset."
    else:
        condition = trucks['avg_speed_kph'] <= 52
        truth = not condition.any()
        if truth:
            expl = f"All {len(trucks)} trucks have avg speed > 52 kph."
        else:
            viol = trucks[condition]
            expl = f"{len(viol)} truck(s) violate the rule: {viol[['route_id', 'avg_speed_kph']].to_dict('records')}"
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All buses with a distance greater than 200 km have an average speed greater than 53 kph."""
    buses = df[(df['vehicle_type'] == 'bus') & (df['distance_km'] > 200)]
    if buses.empty:
        truth = True
        expl = "No buses with distance > 200 km."
    else:
        condition = buses['avg_speed_kph'] <= 53
        truth = not condition.any()
        if truth:
            expl = f"All {len(buses)} buses with distance > 200 km have avg speed > 53 kph."
        else:
            viol = buses[condition]
            expl = f"{len(viol)} bus(es) violate the rule: {viol[['route_id', 'distance_km', 'avg_speed_kph']].to_dict('records')}"
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one van with a fuel usage greater than 32 liters."""
    vans = df[(df['vehicle_type'] == 'van') & (df['fuel_used_l'] > 32)]
    truth = len(vans) > 0
    if truth:
        expl = f"Found {len(vans)} van(s) with fuel usage > 32 liters."
    else:
        expl = "No vans found with fuel usage > 32 liters."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle is a bus, then its delay is less than 27 minutes."""
    buses = df[df['vehicle_type'] == 'bus']
    if buses.empty:
        truth = True
        expl = "No buses in dataset."
    else:
        condition = buses['delay_minutes'] >= 27
        truth = not condition.any()
        if truth:
            expl = f"All {len(buses)} buses have delay < 27 minutes."
        else:
            viol = buses[condition]
            expl = f"{len(viol)} bus(es) violate the rule: {viol[['route_id', 'delay_minutes']].to_dict('records')}"
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All vehicles with a distance less than 150 km have a fuel usage greater than 30 liters."""
    condition = (df['distance_km'] < 150) & (df['fuel_used_l'] <= 30)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with distance < 150 km have fuel usage > 30 liters."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate the rule: {viol[['route_id', 'distance_km', 'fuel_used_l']].to_dict('records')}"
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most vehicles have a delay less than 10 minutes."""
    total = len(df)
    condition = df['delay_minutes'] >= 10
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"Less than half ({count}/{total}) of vehicles have delay >= 10 minutes."
    else:
        expl = f"Half or more ({total-count}/{total}) of vehicles have delay < 10 minutes."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a truck, then its distance is greater than 90 km."""
    trucks = df[df['vehicle_type'] == 'truck']
    if trucks.empty:
        truth = True
        expl = "No trucks in dataset."
    else:
        condition = trucks['distance_km'] <= 90
        truth = not condition.any()
        if truth:
            expl = f"All {len(trucks)} trucks have distance > 90 km."
        else:
            viol = trucks[condition]
            expl = f"{len(viol)} truck(s) violate the rule: {viol[['route_id', 'distance_km']].to_dict('records')}"
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All vehicles with an average speed greater than 60 kph have a fuel usage less than 40 liters."""
    condition = (df['avg_speed_kph'] > 60) & (df['fuel_used_l'] >= 40)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with avg speed > 60 kph have fuel usage < 40 liters."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate the rule: {viol[['route_id', 'avg_speed_kph', 'fuel_used_l']].to_dict('records')}"
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one bus with an average speed greater than 64 kph."""
    buses = df[(df['vehicle_type'] == 'bus') & (df['avg_speed_kph'] > 64)]
    truth = len(buses) > 0
    if truth:
        expl = f"Found {len(buses)} bus(es) with avg speed > 64 kph."
    else:
        expl = "No buses found with avg speed > 64 kph."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle is a van, then its average speed is greater than 48 kph."""
    vans = df[df['vehicle_type'] == 'van']
    if vans.empty:
        truth = True
        expl = "No vans in dataset."
    else:
        condition = vans['avg_speed_kph'] <= 48
        truth = not condition.any()
        if truth:
            expl = f"All {len(vans)} vans have avg speed > 48 kph."
        else:
            viol = vans[condition]
            expl = f"{len(viol)} van(s) violate the rule: {viol[['route_id', 'avg_speed_kph']].to_dict('records')}"
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All vehicles with a fuel usage less than 20 liters have an average speed greater than 60 kph."""
    condition = (df['fuel_used_l'] < 20) & (df['avg_speed_kph'] <= 60)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with fuel usage < 20 liters have avg speed > 60 kph."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate the rule: {viol[['route_id', 'fuel_used_l', 'avg_speed_kph']].to_dict('records')}"
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most vehicles have an average speed greater than 50 kph."""
    total = len(df)
    condition = df['avg_speed_kph'] <= 50
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"Less than half ({count}/{total}) of vehicles have avg speed <= 50 kph."
    else:
        expl = f"Half or more ({total-count}/{total}) of vehicles have avg speed > 50 kph."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a bus, then its distance is greater than 100 km."""
    buses = df[df['vehicle_type'] == 'bus']
    if buses.empty:
        truth = True
        expl = "No buses in dataset."
    else:
        condition = buses['distance_km'] <= 100
        truth = not condition.any()
        if truth:
            expl = f"All {len(buses)} buses have distance > 100 km."
        else:
            viol = buses[condition]
            expl = f"{len(viol)} bus(es) violate the rule: {viol[['route_id', 'distance_km']].to_dict('records')}"
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All vehicles with a delay greater than 20 minutes have a weather condition of rain."""
    condition = (df['delay_minutes'] > 20) & (df['weather']!= 'rain')
    truth = not condition.any()
    if truth:
        expl = "All vehicles with delay > 20 minutes have weather = rain."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate the rule: {viol[['route_id', 'delay_minutes', 'weather']].to_dict('records')}"
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one truck with a fuel usage less than 10 liters."""
    trucks = df[(df['vehicle_type'] == 'truck') & (df['fuel_used_l'] < 10)]
    truth = len(trucks) > 0
    if truth:
        expl = f"Found {len(trucks)} truck(s) with fuel usage < 10 liters."
    else:
        expl = "No trucks found with fuel usage < 10 liters."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_13.csv")

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
        (16, stmt_16)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()