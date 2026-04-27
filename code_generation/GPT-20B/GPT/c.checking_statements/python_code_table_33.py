import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all vans, average speed is at least 48.7 kph."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["avg_speed_kph"] >= 48.7
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans have avg_speed >= 48.7 kph."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All buses have delay of at least 13 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["delay_minutes"] >= 13
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have delay >= 13 minutes."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (delay: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All trucks use at least 10.1 liters of fuel."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["fuel_used_l"] >= 10.1
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks use >= 10.1 liters of fuel."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All rainy routes have average speed of at least 48.7 kph."""
    rainy = df[df["weather"] == "rainy"]
    condition = rainy["avg_speed_kph"] >= 48.7
    truth = condition.all()
    if truth:
        expl = f"All {len(rainy)} rainy routes have avg_speed >= 48.7 kph."
    else:
        viol = rainy[~condition]
        expl = f"{len(viol)} rainy routes violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All routes longer than 200 km have average speed of at least 52.5 kph."""
    long_routes = df[df["distance_km"] > 200]
    condition = long_routes["avg_speed_kph"] >= 52.5
    truth = condition.all()
    if truth:
        expl = f"All {len(long_routes)} routes >200 km have avg_speed >= 52.5 kph."
    else:
        viol = long_routes[~condition]
        expl = f"{len(viol)} long routes violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All clear-weather routes have delay of no more than 14 minutes."""
    clear = df[df["weather"] == "clear"]
    condition = clear["delay_minutes"] <= 14
    truth = condition.all()
    if truth:
        expl = f"All {len(clear)} clear-weather routes have delay <= 14 minutes."
    else:
        viol = clear[~condition]
        expl = f"{len(viol)} clear-weather routes violate the rule (delay: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All routes with average speed greater than 60 kph use at most 40.3 liters of fuel."""
    fast = df[df["avg_speed_kph"] > 60]
    condition = fast["fuel_used_l"] <= 40.3
    truth = condition.all()
    if truth:
        expl = f"All {len(fast)} routes with avg_speed > 60 kph use <= 40.3 liters of fuel."
    else:
        viol = fast[~condition]
        expl = f"{len(viol)} fast routes violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All routes with delay of at least 24 minutes occur under rainy weather."""
    delayed = df[df["delay_minutes"] >= 24]
    condition = delayed["weather"] == "rainy"
    truth = condition.all()
    if truth:
        expl = f"All {len(delayed)} routes with delay >= 24 minutes occur under rainy weather."
    else:
        viol = delayed[~condition]
        expl = f"{len(viol)} delayed routes violate the rule (weather: {', '.join(map(str, viol['weather'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_33.csv")

    # Convert numeric columns
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()