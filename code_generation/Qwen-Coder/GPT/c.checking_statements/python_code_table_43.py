import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all buses, the route distance is at least 66.1 km."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["distance_km"] >= 66.1
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have distance >= 66.1 km."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all buses, the average speed is between 46.5 and 62.3 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["avg_speed_kph"].between(46.5, 62.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have avg speed between 46.5 and 62.3 kph."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all vans, the average speed is between 49.6 and 54.1 kph."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["avg_speed_kph"].between(49.6, 54.1, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans have avg speed between 49.6 and 54.1 kph."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all trucks, the average speed is at least 50.3 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"] >= 50.3
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have avg speed >= 50.3 kph."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all trucks, fuel consumption does not exceed 30.3 liters."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["fuel_used_l"] <= 30.3
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have fuel used <= 30.3 liters."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (fuels: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all routes experiencing rain, the average speed does not exceed 58.6 kph."""
    rainy = df[df["weather"] == "rain"]
    condition = rainy["avg_speed_kph"] <= 58.6
    truth = condition.all()
    if truth:
        expl = f"All {len(rainy)} rainy routes have avg speed <= 58.6 kph."
    else:
        viol = rainy[~condition]
        expl = f"{len(viol)} rainy routes violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all cloudy routes, the delay is at least 12 minutes."""
    cloudy = df[df["weather"] == "cloudy"]
    condition = cloudy["delay_minutes"] >= 12
    truth = condition.all()
    if truth:
        expl = f"All {len(cloudy)} cloudy routes have delay >= 12 minutes."
    else:
        viol = cloudy[~condition]
        expl = f"{len(viol)} cloudy routes violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one bus that used more than 40 liters of fuel."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["fuel_used_l"] > 40
    truth = condition.any()
    if truth:
        viol = buses[condition]
        expl = f"At least one bus ({len(viol)} bus) used more than 40 liters of fuel (fuel: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    else:
        expl = f"No bus used more than 40 liters of fuel."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_43.csv")

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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()