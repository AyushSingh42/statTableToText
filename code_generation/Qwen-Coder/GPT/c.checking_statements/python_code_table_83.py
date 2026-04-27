import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vans have an average speed of at least 49.1 kph."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["avg_speed_kph"] >= 49.1
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans have average speed >= 49.1 kph."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All trucks have a delay of at least 20 minutes."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["delay_minutes"] >= 20
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have delay >= 20 minutes."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All buses have a delay of at most 22 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["delay_minutes"] <= 22
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have delay <= 22 minutes."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All routes longer than 220 km have an average speed of at least 47.8 kph."""
    long_routes = df[df["distance_km"] > 220]
    condition = long_routes["avg_speed_kph"] >= 47.8
    truth = condition.all()
    if truth:
        expl = f"All {len(long_routes)} long routes have average speed >= 47.8 kph."
    else:
        viol = long_routes[~condition]
        expl = f"{len(viol)} long routes violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All vans use no more than 39.0 L of fuel."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["fuel_used_l"] <= 39.0
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans use fuel <= 39.0 L."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All rainy routes have an average speed of at most 65.6 kph."""
    rainy = df[df["weather"] == "rain"]
    condition = rainy["avg_speed_kph"] <= 65.6
    truth = condition.all()
    if truth:
        expl = f"All {len(rainy)} rainy routes have average speed <= 65.6 kph."
    else:
        viol = rainy[~condition]
        expl = f"{len(viol)} rainy routes violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All routes with a delay of at least 25 minutes involve either a van or a truck (no bus)."""
    delayed = df[df["delay_minutes"] >= 25]
    # Filter out buses
    non_buses = delayed[delayed["vehicle_type"]!= "bus"]
    # Check if all remaining are either van or truck
    valid_types = non_buses["vehicle_type"].isin(["van", "truck"])
    truth = valid_types.all()
    if truth:
        expl = f"All {len(delayed)} delayed routes involve van or truck (no bus)."
    else:
        viol = delayed[~valid_types]
        expl = f"{len(viol)} delayed routes involve invalid vehicle type (types: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists a bus route (R083010) whose fuel consumption per kilometer is about 0.48 L/km, the highest among all routes."""
    # Calculate fuel per km for all routes
    df["fuel_per_km"] = df["fuel_used_l"] / df["distance_km"]
    # Get the bus route R083010
    bus_route = df[(df["route_id"] == "R083010") & (df["vehicle_type"] == "bus")]
    if len(bus_route) == 0:
        return False, "Bus route R083010 does not exist."
    fuel_per_km_val = bus_route.iloc[0]["fuel_per_km"]
    max_fuel_per_km = df["fuel_per_km"].max()
    truth = abs(fuel_per_km_val - 0.48) < 0.01 and abs(fuel_per_km_val - max_fuel_per_km) < 0.01
    if truth:
        expl = f"Bus route R083010 has fuel consumption of 0.48 L/km which is the highest among all routes."
    else:
        expl = f"Either bus route R083010 doesn't have 0.48 L/km fuel consumption or it's not the maximum."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_83.csv")

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