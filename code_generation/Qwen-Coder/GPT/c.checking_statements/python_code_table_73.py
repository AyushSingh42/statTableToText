import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All trucks have avg_speed_kph at least 45.6."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"] >= 45.6
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have avg_speed_kph >= 45.6."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All buses have delay_minutes no more than 26."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["delay_minutes"] <= 26
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have delay_minutes <= 26."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All vans have avg_speed_kph at least 47.2."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["avg_speed_kph"] >= 47.2
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans have avg_speed_kph >= 47.2."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All routes longer than 200 km are operated by vans or buses (no trucks)."""
    long_routes = df[df["distance_km"] > 200]
    valid_types = long_routes["vehicle_type"].isin(["van", "bus"])
    truth = valid_types.all()
    if truth:
        expl = f"All {len(long_routes)} long routes are operated by vans or buses."
    else:
        viol = long_routes[~valid_types]
        expl = f"{len(viol)} long routes are operated by trucks (types: {', '.join(viol['vehicle_type'].tolist())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All clear-weather routes have avg_speed_kph at least 57.4."""
    clear_weather = df[df["weather"] == "clear"]
    condition = clear_weather["avg_speed_kph"] >= 57.4
    truth = condition.all()
    if truth:
        expl = f"All {len(clear_weather)} clear-weather routes have avg_speed_kph >= 57.4."
    else:
        viol = clear_weather[~condition]
        expl = f"{len(viol)} clear-weather routes violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All windy routes have avg_speed_kph at most 60.7."""
    windy = df[df["weather"] == "windy"]
    condition = windy["avg_speed_kph"] <= 60.7
    truth = condition.all()
    if truth:
        expl = f"All {len(windy)} windy routes have avg_speed_kph <= 60.7."
    else:
        viol = windy[~condition]
        expl = f"{len(viol)} windy routes violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All routes with fuel_used_l greater than 45 L are either a bus or a truck."""
    high_fuel = df[df["fuel_used_l"] > 45]
    valid_types = high_fuel["vehicle_type"].isin(["bus", "truck"])
    truth = valid_types.all()
    if truth:
        expl = f"All {len(high_fuel)} high-fuel routes are operated by buses or trucks."
    else:
        viol = high_fuel[~valid_types]
        expl = f"{len(viol)} high-fuel routes are operated by vans (types: {', '.join(viol['vehicle_type'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All trucks travel a distance between 85.1 km and 121.5 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["distance_km"].between(85.1, 121.5, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks travel between 85.1 km and 121.5 km."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the distance range (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()