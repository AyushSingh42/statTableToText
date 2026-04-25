import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all bus routes, average speed is between 46.5 and 64.4 kph."""
    bus_routes = df[df["vehicle_type"] == "bus"]
    condition = bus_routes["avg_speed_kph"].between(46.5, 64.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(bus_routes)} bus routes have speeds between 46.5 and 64.4 kph."
    else:
        viol = bus_routes[~condition]
        expl = f"{len(viol)} bus routes violate the speed range (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all truck routes, average speed is between 52.4 and 65.7 kph."""
    truck_routes = df[df["vehicle_type"] == "truck"]
    condition = truck_routes["avg_speed_kph"].between(52.4, 65.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(truck_routes)} truck routes have speeds between 52.4 and 65.7 kph."
    else:
        viol = truck_routes[~condition]
        expl = f"{len(viol)} truck routes violate the speed range (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all van routes, average speed is between 48.7 and 61.3 kph."""
    van_routes = df[df["vehicle_type"] == "van"]
    condition = van_routes["avg_speed_kph"].between(48.7, 61.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(van_routes)} van routes have speeds between 48.7 and 61.3 kph."
    else:
        viol = van_routes[~condition]
        expl = f"{len(viol)} van routes violate the speed range (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All routes with delay greater than 20 minutes are either bus or van, and none are trucks."""
    delayed_routes = df[df["delay_minutes"] > 20]
    valid_types = delayed_routes["vehicle_type"].isin(["bus", "van"])
    truth = valid_types.all()
    if truth:
        expl = f"All {len(delayed_routes)} delayed routes are either bus or van."
    else:
        invalid = delayed_routes[~valid_types]
        expl = f"{len(invalid)} delayed routes are not bus or van (types: {', '.join(invalid['vehicle_type'].tolist())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all routes with clear weather, average speed is between 46.5 and 61.3 kph."""
    clear_routes = df[df["weather"] == "clear"]
    condition = clear_routes["avg_speed_kph"].between(46.5, 61.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(clear_routes)} clear weather routes have speeds between 46.5 and 61.3 kph."
    else:
        viol = clear_routes[~condition]
        expl = f"{len(viol)} clear weather routes violate the speed range (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all routes with rainy weather, average speed is between 48.7 and 64.4 kph."""
    rainy_routes = df[df["weather"] == "rainy"]
    condition = rainy_routes["avg_speed_kph"].between(48.7, 64.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(rainy_routes)} rainy weather routes have speeds between 48.7 and 64.4 kph."
    else:
        viol = rainy_routes[~condition]
        expl = f"{len(viol)} rainy weather routes violate the speed range (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all routes with cloudy weather, average speed is between 50.9 and 65.7 kph."""
    cloudy_routes = df[df["weather"] == "cloudy"]
    condition = cloudy_routes["avg_speed_kph"].between(50.9, 65.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(cloudy_routes)} cloudy weather routes have speeds between 50.9 and 65.7 kph."
    else:
        viol = cloudy_routes[~condition]
        expl = f"{len(viol)} cloudy weather routes violate the speed range (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. The route with the highest fuel consumption per kilometer is the truck route R013010 (37.5 L over 93.3 km, about 0.40 L/km)."""
    df["fuel_consumption_per_km"] = df["fuel_used_l"] / df["distance_km"]
    max_fuel_route = df.loc[df["fuel_consumption_per_km"].idxmax()]
    expected_route_id = "R013010"
    expected_fuel_consumption = 0.40
    truth = (max_fuel_route["route_id"] == expected_route_id) and (abs(max_fuel_route["fuel_consumption_per_km"] - expected_fuel_consumption) < 0.001)
    if truth:
        expl = f"The route with highest fuel consumption is indeed {expected_route_id} with consumption of {max_fuel_route['fuel_consumption_per_km']:.2f} L/km."
    else:
        expl = f"The route with highest fuel consumption is {max_fuel_route['route_id']} with consumption of {max_fuel_route['fuel_consumption_per_km']:.2f} L/km, not {expected_route_id}."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_13.csv")

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