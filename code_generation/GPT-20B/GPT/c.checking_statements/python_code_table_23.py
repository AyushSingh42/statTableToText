import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All trucks have an average speed between 46.4 and 62.4 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"].between(46.4, 62.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have avg_speed_kph between 46.4 and 62.4."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (avg_speed_kph: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All buses have a delay between 12 and 25 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["delay_minutes"].between(12, 25, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have delay_minutes between 12 and 25."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (delay_minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All vans have a delay between 3 and 20 minutes."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["delay_minutes"].between(3, 20, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans have delay_minutes between 3 and 20."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (delay_minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a truck travels in clear weather, its delay does not exceed 17 minutes."""
    trucks_clear = df[(df["vehicle_type"] == "truck") & (df["weather"] == "clear")]
    condition = trucks_clear["delay_minutes"] <= 17
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks_clear)} clear-weather trucks have delay_minutes <= 17."
    else:
        viol = trucks_clear[~condition]
        expl = f"{len(viol)} clear-weather trucks violate the rule (delay_minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a bus travels in rain, its delay is at least 12 minutes."""
    buses_rain = df[(df["vehicle_type"] == "bus") & (df["weather"] == "rain")]
    condition = buses_rain["delay_minutes"] >= 12
    truth = condition.all()
    if truth:
        expl = f"All {len(buses_rain)} rain-traveling buses have delay_minutes >= 12."
    else:
        viol = buses_rain[~condition]
        expl = f"{len(viol)} rain-traveling buses violate the rule (delay_minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. There exists a van that used less than 22 liters of fuel."""
    vans = df[df["vehicle_type"] == "van"]
    exists = (vans["fuel_used_l"] < 22).any()
    if exists:
        viol = vans[vans["fuel_used_l"] < 22]
        expl = f"Found {len(viol)} van(s) with fuel_used_l < 22 (values: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    else:
        expl = "No van found with fuel_used_l < 22."
    return exists, expl

def stmt_7(df: pd.DataFrame):
    """7. Most routes (13 out of 15) have a delay greater than 10 minutes."""
    total_routes = df["route_id"].nunique()
    routes_gt10 = df[df["delay_minutes"] > 10]["route_id"].nunique()
    truth = (total_routes == 15) and (routes_gt10 == 13)
    if truth:
        expl = f"Total routes: 15, routes with delay >10: 13."
    else:
        expl = f"Total routes: {total_routes}, routes with delay >10: {routes_gt10}."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_23.csv")

    # Convert likely numeric columns safely.
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()