import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All trucks have an average speed of at most 64.6 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        return True, "No trucks in dataset."
    condition = trucks["avg_speed_kph"] <= 64.6
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have average speed <= 64.6 kph."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All vans use at least 24.9 liters of fuel on their routes."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        return True, "No vans in dataset."
    condition = vans["fuel_used_l"] >= 24.9
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans use >= 24.9 liters of fuel."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All buses experience a delay of at least 20 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        return True, "No buses in dataset."
    condition = buses["delay_minutes"] >= 20
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have delay >= 20 minutes."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All routes recorded in rain have an average speed of at most 61.0 kph."""
    rainy = df[df["weather"] == "rain"]
    if rainy.empty:
        return True, "No rainy routes in dataset."
    condition = rainy["avg_speed_kph"] <= 61.0
    truth = condition.all()
    if truth:
        expl = f"All {len(rainy)} rainy routes have average speed <= 61.0 kph."
    else:
        viol = rainy[~condition]
        expl = f"{len(viol)} rainy routes violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All windy routes have an average speed of at least 51.9 kph."""
    windy = df[df["weather"] == "windy"]
    if windy.empty:
        return True, "No windy routes in dataset."
    condition = windy["avg_speed_kph"] >= 51.9
    truth = condition.all()
    if truth:
        expl = f"All {len(windy)} windy routes have average speed >= 51.9 kph."
    else:
        viol = windy[~condition]
        expl = f"{len(viol)} windy routes violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All vans travel a distance of at least 74.9 km."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        return True, "No vans in dataset."
    condition = vans["distance_km"] >= 74.9
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans travel >= 74.9 km."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All trucks use no more than 27.2 liters of fuel."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        return True, "No trucks in dataset."
    condition = trucks["fuel_used_l"] <= 27.2
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks use <= 27.2 liters of fuel."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All routes longer than 200 km involve either a van or a truck."""
    long_routes = df[df["distance_km"] > 200]
    if long_routes.empty:
        return True, "No routes longer than 200 km in dataset."
    valid_types = ["van", "truck"]
    condition = long_routes["vehicle_type"].isin(valid_types)
    truth = condition.all()
    if truth:
        expl = f"All {len(long_routes)} long routes involve a van or truck."
    else:
        viol = long_routes[~condition]
        expl = f"{len(viol)} long routes do not involve a van or truck (types: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Any route with an average speed of 62 kph or higher uses a van or a truck."""
    fast_routes = df[df["avg_speed_kph"] >= 62]
    if fast_routes.empty:
        return True, "No routes with average speed >= 62 kph in dataset."
    valid_types = ["van", "truck"]
    condition = fast_routes["vehicle_type"].isin(valid_types)
    truth = condition.all()
    if truth:
        expl = f"All {len(fast_routes)} fast routes involve a van or truck."
    else:
        viol = fast_routes[~condition]
        expl = f"{len(viol)} fast routes do not involve a van or truck (types: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All routes that used more than 40 liters of fuel were vans."""
    high_fuel = df[df["fuel_used_l"] > 40]
    if high_fuel.empty:
        return True, "No routes with fuel usage > 40 liters in dataset."
    condition = high_fuel["vehicle_type"] == "van"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fuel)} high-fuel routes are vans."
    else:
        viol = high_fuel[~condition]
        expl = f"{len(viol)} high-fuel routes are not vans (types: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
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
        (10, stmt_10)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()