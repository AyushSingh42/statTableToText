import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles with a distance greater than 200 km have an average speed greater than 60 kph."""
    subset = df[df["distance_km"] > 200]
    condition = subset["avg_speed_kph"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} vehicles with distance >200 km have avg_speed >60 kph."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} vehicles violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a van, then its fuel used is less than 40 liters."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["fuel_used_l"] < 40
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans use less than 40 liters."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one truck with a delay of less than 10 minutes."""
    exists = ((df["vehicle_type"] == "truck") & (df["delay_minutes"] < 10)).any()
    if exists:
        expl = "At least one truck has delay <10 minutes."
    else:
        expl = "No truck with delay <10 minutes found."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All buses have a distance greater than 100 km."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["distance_km"] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have distance >100 km."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If the weather is clear, then the vehicle type is either a truck or a van."""
    clear = df[df["weather"] == "clear"]
    condition = clear["vehicle_type"].isin(["truck", "van"])
    truth = condition.all()
    if truth:
        expl = f"All {len(clear)} clear-weather vehicles are trucks or vans."
    else:
        viol = clear[~condition]
        expl = f"{len(viol)} clear-weather vehicles violate the rule (type: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All vehicles with an average speed greater than 65 kph have a distance greater than 150 km."""
    subset = df[df["avg_speed_kph"] > 65]
    condition = subset["distance_km"] > 150
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} vehicles with avg_speed >65 kph have distance >150 km."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} vehicles violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most vehicles have a delay greater than 10 minutes."""
    total = len(df)
    count = (df["delay_minutes"] > 10).sum()
    truth = count > total / 2
    percent = count / total * 100
    if truth:
        expl = f"{percent:.1f}% of vehicles have delay >10 minutes."
    else:
        expl = f"Only {percent:.1f}% of vehicles have delay >10 minutes."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a bus, then its average speed is greater than 55 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["avg_speed_kph"] > 55
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have avg_speed >55 kph."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one van with a distance less than 150 km and an average speed less than 55 kph."""
    exists = ((df["vehicle_type"] == "van") &
              (df["distance_km"] < 150) &
              (df["avg_speed_kph"] < 55)).any()
    if exists:
        expl = "At least one van satisfies distance <150 km and avg_speed <55 kph."
    else:
        expl = "No van satisfies both conditions."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All trucks have a fuel used greater than 10 liters."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["fuel_used_l"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks use >10 liters."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If the weather is rainy, then the vehicle type is either a bus or a van."""
    rainy = df[df["weather"] == "rainy"]
    condition = rainy["vehicle_type"].isin(["bus", "van"])
    truth = condition.all()
    if truth:
        expl = f"All {len(rainy)} rainy-weather vehicles are buses or vans."
    else:
        viol = rainy[~condition]
        expl = f"{len(viol)} rainy-weather vehicles violate the rule (type: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All vehicles with a distance less than 120 km have a delay less than 20 minutes."""
    subset = df[df["distance_km"] < 120]
    condition = subset["delay_minutes"] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} vehicles with distance <120 km have delay <20 minutes."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} vehicles violate the rule (delay: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most trucks have a distance greater than 120 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    total = len(trucks)
    count = (trucks["distance_km"] > 120).sum()
    truth = count > total / 2
    percent = count / total * 100 if total > 0 else 0
    if truth:
        expl = f"{percent:.1f}% of trucks have distance >120 km."
    else:
        expl = f"Only {percent:.1f}% of trucks have distance >120 km."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a truck, then its average speed is greater than 50 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"] > 50
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have avg_speed >50 kph."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one bus with a fuel used greater than 20 liters and a distance greater than 200 km."""
    exists = ((df["vehicle_type"] == "bus") &
              (df["fuel_used_l"] > 20) &
              (df["distance_km"] > 200)).any()
    if exists:
        expl = "At least one bus satisfies fuel_used >20 liters and distance >200 km."
    else:
        expl = "No bus satisfies both conditions."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. All vehicles with an average speed less than 55 kph have a distance less than 180 km."""
    subset = df[df["avg_speed_kph"] < 55]
    condition = subset["distance_km"] < 180
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} vehicles with avg_speed <55 kph have distance <180 km."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} vehicles violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_33.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()