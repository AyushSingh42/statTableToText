import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All bus routes have a delay of 21 minutes or less."""
    bus_routes = df[df["vehicle_type"] == "bus"]
    condition = bus_routes["delay_minutes"] <= 21
    truth = condition.all()
    if truth:
        expl = f"All {len(bus_routes)} bus routes have delays ≤ 21 minutes."
    else:
        viol = bus_routes[~condition]
        expl = f"{len(viol)} bus routes violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All truck routes have a delay between 11 and 19 minutes inclusive."""
    truck_routes = df[df["vehicle_type"] == "truck"]
    condition = truck_routes["delay_minutes"].between(11, 19, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(truck_routes)} truck routes have delays between 11-19 minutes."
    else:
        viol = truck_routes[~condition]
        expl = f"{len(viol)} truck routes violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For routes longer than 200 km, fuel used does not exceed 44.6 liters."""
    long_routes = df[df["distance_km"] > 200]
    condition = long_routes["fuel_used_l"] <= 44.6
    truth = condition.all()
    if truth:
        expl = f"All {len(long_routes)} long routes use ≤ 44.6 liters of fuel."
    else:
        viol = long_routes[~condition]
        expl = f"{len(viol)} long routes violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All rainy-weather routes have an average speed of at most 61.2 kph."""
    rainy_routes = df[df["weather"] == "rain"]
    condition = rainy_routes["avg_speed_kph"] <= 61.2
    truth = condition.all()
    if truth:
        expl = f"All {len(rainy_routes)} rainy routes have speeds ≤ 61.2 kph."
    else:
        viol = rainy_routes[~condition]
        expl = f"{len(viol)} rainy routes violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a route is a truck and its distance is less than 70 km, then its fuel consumption per kilometer exceeds 0.5 L/km."""
    truck_short = df[(df["vehicle_type"] == "truck") & (df["distance_km"] < 70)]
    if len(truck_short) == 0:
        return True, "No truck routes under 70 km to check."
    fuel_per_km = truck_short["fuel_used_l"] / truck_short["distance_km"]
    condition = fuel_per_km > 0.5
    truth = condition.all()
    if truth:
        expl = f"All {len(truck_short)} short truck routes have fuel consumption > 0.5 L/km."
    else:
        viol = truck_short[~condition]
        expl = f"{len(viol)} short truck routes violate the rule (fuel per km: {', '.join(map(str, (viol['fuel_used_l']/viol['distance_km']).tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For routes shorter than 100 km, the average speed is at least 51.5 kph."""
    short_routes = df[df["distance_km"] < 100]
    condition = short_routes["avg_speed_kph"] >= 51.5
    truth = condition.all()
    if truth:
        expl = f"All {len(short_routes)} short routes have speeds ≥ 51.5 kph."
    else:
        viol = short_routes[~condition]
        expl = f"{len(viol)} short routes violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Cloudy-weather routes have a delay of no more than 19 minutes."""
    cloudy_routes = df[df["weather"] == "cloudy"]
    condition = cloudy_routes["delay_minutes"] <= 19
    truth = condition.all()
    if truth:
        expl = f"All {len(cloudy_routes)} cloudy routes have delays ≤ 19 minutes."
    else:
        viol = cloudy_routes[~condition]
        expl = f"{len(viol)} cloudy routes violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. The route with the lowest fuel consumption per kilometer is a van covering 228.0 km with only 11.6 liters of fuel (≈0.051 L/km)."""
    df["fuel_per_km"] = df["fuel_used_l"] / df["distance_km"]
    min_fuel_route = df.loc[df["fuel_per_km"].idxmin()]
    expected_route = df[(df["vehicle_type"] == "van") & (df["distance_km"] == 228.0) & (df["fuel_used_l"] == 11.6)]
    if len(expected_route) == 0:
        return False, "No van route matches the specified criteria."
    expected_fuel_per_km = 11.6 / 228.0
    actual_min_fuel_per_km = min_fuel_route["fuel_per_km"]
    truth = abs(actual_min_fuel_per_km - expected_fuel_per_km) < 0.001
    if truth:
        expl = f"The route with lowest fuel consumption per km ({actual_min_fuel_per_km:.3f} L/km) is indeed the van with 228 km and 11.6 L fuel."
    else:
        expl = f"The route with lowest fuel consumption per km ({actual_min_fuel_per_km:.3f} L/km) is not the specified van route (expected ~{expected_fuel_per_km:.3f} L/km)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_3.csv")

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