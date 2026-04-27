import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All bus routes have a delay of 21 minutes or less."""
    bus = df[df["vehicle_type"] == "bus"]
    condition = bus["delay_minutes"] <= 21
    truth = condition.all()
    if truth:
        expl = f"All {len(bus)} bus routes have delay <= 21 minutes."
    else:
        viol = bus[~condition]
        expl = f"{len(viol)} bus routes violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All truck routes have a delay between 11 and 19 minutes inclusive."""
    truck = df[df["vehicle_type"] == "truck"]
    condition = truck["delay_minutes"].between(11, 19, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(truck)} truck routes have delay between 11 and 19 minutes."
    else:
        viol = truck[~condition]
        expl = f"{len(viol)} truck routes violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For routes longer than 200 km, fuel used does not exceed 44.6 liters."""
    long_routes = df[df["distance_km"] > 200]
    if long_routes.empty:
        return True, "No routes longer than 200 km; rule vacuously satisfied."
    condition = long_routes["fuel_used_l"] <= 44.6
    truth = condition.all()
    if truth:
        expl = f"All {len(long_routes)} routes >200 km use <= 44.6 liters."
    else:
        viol = long_routes[~condition]
        expl = f"{len(viol)} routes >200 km exceed 44.6 liters (fuel: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All rainy-weather routes have an average speed of at most 61.2 kph."""
    rain = df[df["weather"] == "rain"]
    condition = rain["avg_speed_kph"] <= 61.2
    truth = condition.all()
    if truth:
        expl = f"All {len(rain)} rainy routes have avg speed <= 61.2 kph."
    else:
        viol = rain[~condition]
        expl = f"{len(viol)} rainy routes violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a route is a truck and its distance is less than 70 km, then its fuel consumption per kilometer exceeds 0.5 L/km."""
    subset = df[(df["vehicle_type"] == "truck") & (df["distance_km"] < 70)]
    if subset.empty:
        return True, "No truck routes with distance <70 km; rule vacuously satisfied."
    fuel_per_km = subset["fuel_used_l"] / subset["distance_km"]
    condition = fuel_per_km > 0.5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} truck routes <70 km have fuel per km > 0.5 L/km."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} truck routes <70 km violate the rule (fuel per km: {', '.join(map(lambda x: f'{x:.3f}', (viol['fuel_used_l'] / viol['distance_km']).tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For routes shorter than 100 km, the average speed is at least 51.5 kph."""
    short = df[df["distance_km"] < 100]
    if short.empty:
        return True, "No routes shorter than 100 km; rule vacuously satisfied."
    condition = short["avg_speed_kph"] >= 51.5
    truth = condition.all()
    if truth:
        expl = f"All {len(short)} routes <100 km have avg speed >= 51.5 kph."
    else:
        viol = short[~condition]
        expl = f"{len(viol)} routes <100 km violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Cloudy-weather routes have a delay of no more than 19 minutes."""
    cloudy = df[df["weather"] == "cloudy"]
    condition = cloudy["delay_minutes"] <= 19
    truth = condition.all()
    if truth:
        expl = f"All {len(cloudy)} cloudy routes have delay <= 19 minutes."
    else:
        viol = cloudy[~condition]
        expl = f"{len(viol)} cloudy routes violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. The route with the lowest fuel consumption per kilometer is a van covering 228.0 km with only 11.6 liters of fuel (≈0.051 L/km)."""
    df = df.copy()
    df["fuel_per_km"] = df["fuel_used_l"] / df["distance_km"]
    min_fuel_per_km = df["fuel_per_km"].min()
    min_rows = df[df["fuel_per_km"] == min_fuel_per_km]
    # Check if any row matches the specified van
    match = min_rows[
        (min_rows["vehicle_type"] == "van") &
        (min_rows["distance_km"] == 228.0) &
        (min_rows["fuel_used_l"] == 11.6)
    ]
    truth = not match.empty
    if truth:
        expl = f"The route with lowest fuel per km is a van (228.0 km, 11.6 L, {min_fuel_per_km:.3f} L/km)."
    else:
        # Provide details of the actual min route(s)
        details = min_rows[["route_id", "vehicle_type", "distance_km", "fuel_used_l", "fuel_per_km"]]
        expl = f"The route(s) with lowest fuel per km: {details.to_dict(orient='records')}. None matches the specified van."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_3.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()