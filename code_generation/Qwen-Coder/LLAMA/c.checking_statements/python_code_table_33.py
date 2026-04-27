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
        expl = f"{len(viol)} vehicle(s) violate the rule (distance > 200 km but avg speed <= 60 kph)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a van, then its fuel used is less than 40 liters."""
    condition = (df["vehicle_type"] == "van") & (df["fuel_used_l"] >= 40)
    truth = not condition.any()
    if truth:
        expl = "All vans use < 40 liters of fuel."
    else:
        viol = df[condition]
        expl = f"{len(viol)} van(s) violate the rule (use >= 40 liters)."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one truck with a delay of less than 10 minutes."""
    condition = (df["vehicle_type"] == "truck") & (df["delay_minutes"] < 10)
    truth = condition.any()
    if truth:
        expl = "At least one truck has delay < 10 minutes."
    else:
        expl = "No truck has delay < 10 minutes."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All buses have a distance greater than 100 km."""
    condition = (df["vehicle_type"] == "bus") & (df["distance_km"] <= 100)
    truth = not condition.any()
    if truth:
        expl = "All buses travel > 100 km."
    else:
        viol = df[condition]
        expl = f"{len(viol)} bus(es) violate the rule (distance <= 100 km)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If the weather is clear, then the vehicle type is either a truck or a van."""
    condition = (df["weather"] == "clear") & (~df["vehicle_type"].isin(["truck", "van"]))
    truth = not condition.any()
    if truth:
        expl = "All vehicles in clear weather are either trucks or vans."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) in clear weather are neither trucks nor vans."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All vehicles with an average speed greater than 65 kph have a distance greater than 150 km."""
    condition = (df["avg_speed_kph"] > 65) & (df["distance_km"] <= 150)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with avg speed > 65 kph travel > 150 km."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (avg speed > 65 kph but distance <= 150 km)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most vehicles have a delay greater than 10 minutes."""
    total = len(df)
    condition = df["delay_minutes"] > 10
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of vehicles have delay > 10 minutes."
    else:
        expl = f"Less than half ({count}/{total}) of vehicles have delay > 10 minutes."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a bus, then its average speed is greater than 55 kph."""
    condition = (df["vehicle_type"] == "bus") & (df["avg_speed_kph"] <= 55)
    truth = not condition.any()
    if truth:
        expl = "All buses have avg speed > 55 kph."
    else:
        viol = df[condition]
        expl = f"{len(viol)} bus(es) violate the rule (avg speed <= 55 kph)."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one van with a distance less than 150 km and an average speed less than 55 kph."""
    condition = (df["vehicle_type"] == "van") & (df["distance_km"] < 150) & (df["avg_speed_kph"] < 55)
    truth = condition.any()
    if truth:
        expl = "At least one van has distance < 150 km and avg speed < 55 kph."
    else:
        expl = "No van satisfies both conditions."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All trucks have a fuel used greater than 10 liters."""
    condition = (df["vehicle_type"] == "truck") & (df["fuel_used_l"] <= 10)
    truth = not condition.any()
    if truth:
        expl = "All trucks use > 10 liters of fuel."
    else:
        viol = df[condition]
        expl = f"{len(viol)} truck(s) violate the rule (use <= 10 liters)."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If the weather is rainy, then the vehicle type is either a bus or a van."""
    condition = (df["weather"] == "rainy") & (~df["vehicle_type"].isin(["bus", "van"]))
    truth = not condition.any()
    if truth:
        expl = "All vehicles in rainy weather are either buses or vans."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) in rainy weather are neither buses nor vans."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All vehicles with a distance less than 120 km have a delay less than 20 minutes."""
    condition = (df["distance_km"] < 120) & (df["delay_minutes"] >= 20)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with distance < 120 km have delay < 20 minutes."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (distance < 120 km but delay >= 20 minutes)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most trucks have a distance greater than 120 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    total = len(trucks)
    condition = trucks["distance_km"] > 120
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of trucks travel > 120 km."
    else:
        expl = f"Less than half ({count}/{total}) of trucks travel > 120 km."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a truck, then its average speed is greater than 50 kph."""
    condition = (df["vehicle_type"] == "truck") & (df["avg_speed_kph"] <= 50)
    truth = not condition.any()
    if truth:
        expl = "All trucks have avg speed > 50 kph."
    else:
        viol = df[condition]
        expl = f"{len(viol)} truck(s) violate the rule (avg speed <= 50 kph)."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one bus with a fuel used greater than 20 liters and a distance greater than 200 km."""
    condition = (df["vehicle_type"] == "bus") & (df["fuel_used_l"] > 20) & (df["distance_km"] > 200)
    truth = condition.any()
    if truth:
        expl = "At least one bus has fuel > 20 liters and distance > 200 km."
    else:
        expl = "No bus satisfies both conditions."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All vehicles with an average speed less than 55 kph have a distance less than 180 km."""
    condition = (df["avg_speed_kph"] < 55) & (df["distance_km"] >= 180)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with avg speed < 55 kph travel < 180 km."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicle(s) violate the rule (avg speed < 55 kph but distance >= 180 km)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_33.csv")

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