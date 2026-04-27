import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all bus routes, average speed is between 46.5 and 64.4 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["avg_speed_kph"].between(46.5, 64.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} bus routes have avg_speed between 46.5 and 64.4 kph."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} bus route(s) violate the rule (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all truck routes, average speed is between 52.4 and 65.7 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"].between(52.4, 65.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} truck routes have avg_speed between 52.4 and 65.7 kph."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} truck route(s) violate the rule (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all van routes, average speed is between 48.7 and 61.3 kph."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["avg_speed_kph"].between(48.7, 61.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} van routes have avg_speed between 48.7 and 61.3 kph."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} van route(s) violate the rule (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All routes with delay greater than 20 minutes are either bus or van, and none are trucks."""
    delayed = df[df["delay_minutes"] > 20]
    condition = delayed["vehicle_type"].isin(["bus", "van"])
    truth = condition.all()
    if truth:
        expl = f"All {len(delayed)} delayed routes are bus or van."
    else:
        viol = delayed[~condition]
        expl = f"{len(viol)} delayed route(s) are not bus or van (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all routes with clear weather, average speed is between 46.5 and 61.3 kph."""
    clear = df[df["weather"] == "clear"]
    condition = clear["avg_speed_kph"].between(46.5, 61.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(clear)} clear-weather routes have avg_speed between 46.5 and 61.3 kph."
    else:
        viol = clear[~condition]
        expl = f"{len(viol)} clear-weather route(s) violate the rule (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all routes with rainy weather, average speed is between 48.7 and 64.4 kph."""
    rainy = df[df["weather"] == "rainy"]
    condition = rainy["avg_speed_kph"].between(48.7, 64.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(rainy)} rainy-weather routes have avg_speed between 48.7 and 64.4 kph."
    else:
        viol = rainy[~condition]
        expl = f"{len(viol)} rainy-weather route(s) violate the rule (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all routes with cloudy weather, average speed is between 50.9 and 65.7 kph."""
    cloudy = df[df["weather"] == "cloudy"]
    condition = cloudy["avg_speed_kph"].between(50.9, 65.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(cloudy)} cloudy-weather routes have avg_speed between 50.9 and 65.7 kph."
    else:
        viol = cloudy[~condition]
        expl = f"{len(viol)} cloudy-weather route(s) violate the rule (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. The route with the highest fuel consumption per kilometer is the truck route R013010 (37.5 L over 93.3 km, about 0.40 L/km)."""
    df = df.copy()
    df["fuel_per_km"] = df["fuel_used_l"] / df["distance_km"]
    max_row = df.loc[df["fuel_per_km"].idxmax()]
    truth = (
        max_row["route_id"] == "R013010"
        and max_row["vehicle_type"] == "truck"
        and abs(max_row["fuel_per_km"] - 0.40) < 0.01
    )
    if truth:
        expl = f"Route {max_row['route_id']} has the highest consumption of {max_row['fuel_per_km']:.3f} L/km."
    else:
        expl = (
            f"Highest consumption route is {max_row['route_id']} "
            f"({max_row['fuel_per_km']:.3f} L/km, vehicle: {max_row['vehicle_type']}). "
            f"Expected R013010 with ~0.40 L/km."
        )
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_13.csv")

    # Convert numeric columns
    numeric_cols = ["distance_km", "avg_speed_kph", "fuel_used_l", "delay_minutes"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Normalize weather strings to lowercase
    df["weather"] = df["weather"].str.lower()

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