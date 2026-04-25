import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All trips have an average speed between 45.7 kph and 65.7 kph."""
    condition = df["avg_speed_kph"].between(45.7, 65.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(df)} trips have average speeds between 45.7 and 65.7 kph."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} trips violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For every van, the distance traveled is at least 65 km and the fuel used is between 17.1 L and 20.2 L."""
    vans = df[df["vehicle_type"] == "van"]
    cond_dist = vans["distance_km"] >= 65
    cond_fuel = vans["fuel_used_l"].between(17.1, 20.2, inclusive="both")
    condition = cond_dist & cond_fuel
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans meet the criteria (distance ≥ 65 km and fuel used between 17.1 L and 20.2 L)."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (distances: {', '.join(map(str, viol['distance_km'].tolist()))}, fuels: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All trucks have an average speed below 62 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"] < 62
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have average speeds below 62 kph."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All rainy trips experience a delay of at least 3 minutes."""
    rainy = df[df["weather"] == "rain"]
    condition = rainy["delay_minutes"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(rainy)} rainy trips have delays of at least 3 minutes."
    else:
        viol = rainy[~condition]
        expl = f"{len(viol)} rainy trips violate the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a trip is longer than 200 km, its average speed lies between 49.8 kph and 64.4 kph."""
    long_trips = df[df["distance_km"] > 200]
    condition = long_trips["avg_speed_kph"].between(49.8, 64.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(long_trips)} long trips (over 200 km) have average speeds between 49.8 and 64.4 kph."
    else:
        viol = long_trips[~condition]
        expl = f"{len(viol)} long trips violate the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Every trip shorter than 70 km is made by a van."""
    short_trips = df[df["distance_km"] < 70]
    condition = short_trips["vehicle_type"] == "van"
    truth = condition.all()
    if truth:
        expl = f"All {len(short_trips)} short trips (under 70 km) are made by vans."
    else:
        viol = short_trips[~condition]
        expl = f"{len(viol)} short trips are not made by vans (vehicle types: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All trucks consume less than 0.30 L of fuel per kilometre."""
    trucks = df[df["vehicle_type"] == "truck"]
    consumption = trucks["fuel_used_l"] / trucks["distance_km"]
    condition = consumption < 0.30
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks consume less than 0.30 L/km."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks consume 0.30 L/km or more (consumptions: {', '.join(map(str, (viol['fuel_used_l']/viol['distance_km']).tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one van whose delay is under 10 minutes."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["delay_minutes"] < 10
    truth = condition.any()
    if truth:
        expl = f"At least one van has a delay under 10 minutes."
    else:
        expl = f"No van has a delay under 10 minutes."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_53.csv")

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