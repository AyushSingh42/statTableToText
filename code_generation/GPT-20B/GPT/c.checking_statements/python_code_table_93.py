import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vans have an average speed of at least 52.7 kph."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["avg_speed_kph"] >= 52.7
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans have avg_speed_kph >= 52.7."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the rule (avg_speed_kph: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All trucks have an average speed of at most 58.9 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"] <= 58.9
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have avg_speed_kph <= 58.9."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (avg_speed_kph: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All bus routes have an average speed between 51.5 and 57.6 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["avg_speed_kph"].between(51.5, 57.6, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have avg_speed_kph between 51.5 and 57.6."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the rule (avg_speed_kph: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All clear-weather routes use a truck."""
    clear = df[df["weather"] == "clear"]
    condition = clear["vehicle_type"] == "truck"
    truth = condition.all()
    if truth:
        expl = f"All {len(clear)} clear-weather routes use a truck."
    else:
        viol = clear[~condition]
        expl = f"{len(viol)} clear-weather routes do not use a truck (vehicle_type: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a route’s distance is under 100 km, the vehicle type is van."""
    under_100 = df[df["distance_km"] < 100]
    condition = under_100["vehicle_type"] == "van"
    truth = condition.all()
    if truth:
        expl = f"All {len(under_100)} routes with distance < 100 km use a van."
    else:
        viol = under_100[~condition]
        expl = f"{len(viol)} routes with distance < 100 km do not use a van (vehicle_type: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If average speed exceeds 60 kph, the vehicle type is van."""
    over_60 = df[df["avg_speed_kph"] > 60]
    condition = over_60["vehicle_type"] == "van"
    truth = condition.all()
    if truth:
        expl = f"All {len(over_60)} routes with avg_speed_kph > 60 use a van."
    else:
        viol = over_60[~condition]
        expl = f"{len(viol)} routes with avg_speed_kph > 60 do not use a van (vehicle_type: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All windy-weather bus routes have a delay of 15 minutes or less."""
    windy_bus = df[(df["weather"] == "windy") & (df["vehicle_type"] == "bus")]
    condition = windy_bus["delay_minutes"] <= 15
    truth = condition.all()
    if truth:
        expl = f"All {len(windy_bus)} windy-weather bus routes have delay <= 15 minutes."
    else:
        viol = windy_bus[~condition]
        expl = f"{len(viol)} windy-weather bus routes violate the rule (delay_minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All rain-weather bus routes have a delay of at least 6 minutes."""
    rain_bus = df[(df["weather"] == "rain") & (df["vehicle_type"] == "bus")]
    condition = rain_bus["delay_minutes"] >= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(rain_bus)} rain-weather bus routes have delay >= 6 minutes."
    else:
        viol = rain_bus[~condition]
        expl = f"{len(viol)} rain-weather bus routes violate the rule (delay_minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All routes with distance greater than 200 km use at least 13.2 L of fuel."""
    over_200 = df[df["distance_km"] > 200]
    condition = over_200["fuel_used_l"] >= 13.2
    truth = condition.all()
    if truth:
        expl = f"All {len(over_200)} routes with distance > 200 km use at least 13.2 L of fuel."
    else:
        viol = over_200[~condition]
        expl = f"{len(viol)} routes with distance > 200 km use less than 13.2 L of fuel (fuel_used_l: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_93.csv")

    # Convert numeric columns safely
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
        (8, stmt_8),
        (9, stmt_9),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()