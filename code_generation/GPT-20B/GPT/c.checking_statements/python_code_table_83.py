import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vans have an average speed of at least 49.1 kph."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        return True, "No vans in the data, vacuously true."
    condition = vans["avg_speed_kph"] >= 49.1
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans have avg_speed_kph >= 49.1."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (avg_speed_kph: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All trucks have a delay of at least 20 minutes."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        return True, "No trucks in the data, vacuously true."
    condition = trucks["delay_minutes"] >= 20
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have delay_minutes >= 20."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (delay_minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All buses have a delay of at most 22 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        return True, "No buses in the data, vacuously true."
    condition = buses["delay_minutes"] <= 22
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have delay_minutes <= 22."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (delay_minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All routes longer than 220 km have an average speed of at least 47.8 kph."""
    long_routes = df[df["distance_km"] > 220]
    if long_routes.empty:
        return True, "No routes longer than 220 km, vacuously true."
    condition = long_routes["avg_speed_kph"] >= 47.8
    truth = condition.all()
    if truth:
        expl = f"All {len(long_routes)} routes >220 km have avg_speed_kph >= 47.8."
    else:
        viol = long_routes[~condition]
        expl = f"{len(viol)} routes violate the rule (avg_speed_kph: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All vans use no more than 39.0 L of fuel."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        return True, "No vans in the data, vacuously true."
    condition = vans["fuel_used_l"] <= 39.0
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans use <= 39.0 L of fuel."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (fuel_used_l: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All rainy routes have an average speed of at most 65.6 kph."""
    rainy = df[df["weather"] == "rain"]
    if rainy.empty:
        return True, "No rainy routes in the data, vacuously true."
    condition = rainy["avg_speed_kph"] <= 65.6
    truth = condition.all()
    if truth:
        expl = f"All {len(rainy)} rainy routes have avg_speed_kph <= 65.6."
    else:
        viol = rainy[~condition]
        expl = f"{len(viol)} rainy routes violate the rule (avg_speed_kph: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All routes with a delay of at least 25 minutes involve either a van or a truck (no bus)."""
    delayed = df[df["delay_minutes"] >= 25]
    if delayed.empty:
        return True, "No routes with delay >= 25 minutes, vacuously true."
    condition = delayed["vehicle_type"].isin(["van", "truck"])
    truth = condition.all()
    if truth:
        expl = f"All {len(delayed)} routes with delay >= 25 minutes are vans or trucks."
    else:
        viol = delayed[~condition]
        expl = f"{len(viol)} routes violate the rule (vehicle_type: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists a bus route (R083010) whose fuel consumption per kilometer is about 0.48 L/km, the highest among all routes."""
    target = df[df["route_id"] == "R083010"]
    if target.empty:
        return False, "Route R083010 not found."
    target = target.iloc[0]
    if target["vehicle_type"]!= "bus":
        return False, "Route R083010 is not a bus."
    consumption = target["fuel_used_l"] / target["distance_km"]
    # Check approximate 0.48 within tolerance 0.01
    if abs(consumption - 0.48) > 0.01:
        return False, f"Fuel consumption per km is {consumption:.4f} L/km, not about 0.48."
    # Compute max consumption among all routes
    df["consumption_per_km"] = df["fuel_used_l"] / df["distance_km"]
    max_consumption = df["consumption_per_km"].max()
    if consumption < max_consumption - 1e-6:
        return False, f"Consumption {consumption:.4f} L/km is not the highest (max is {max_consumption:.4f})."
    return True, f"Route R083010 has consumption {consumption:.4f} L/km, which is about 0.48 and the highest."

def main():
    df = pd.read_csv("../inference_generation/tables/table_83.csv")

    # Convert numeric columns safely
    for col in ["distance_km", "avg_speed_kph", "fuel_used_l", "delay_minutes"]:
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