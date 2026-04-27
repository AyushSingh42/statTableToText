import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All trucks have an average speed of at most 64.6 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"] <= 64.6
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks satisfy avg_speed_kph <= 64.6."
    else:
        viol = trucks[~condition]
        viol_info = ", ".join(f"{r['route_id']}({r['avg_speed_kph']})" for _, r in viol.iterrows())
        expl = f"{len(viol)} trucks violate the rule: {viol_info}."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All vans use at least 24.9 liters of fuel on their routes."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["fuel_used_l"] >= 24.9
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans use at least 24.9 liters."
    else:
        viol = vans[~condition]
        viol_info = ", ".join(f"{r['route_id']}({r['fuel_used_l']})" for _, r in viol.iterrows())
        expl = f"{len(viol)} vans violate the rule: {viol_info}."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All buses experience a delay of at least 20 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["delay_minutes"] >= 20
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have delay >= 20 minutes."
    else:
        viol = buses[~condition]
        viol_info = ", ".join(f"{r['route_id']}({r['delay_minutes']})" for _, r in viol.iterrows())
        expl = f"{len(viol)} buses violate the rule: {viol_info}."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All routes recorded in rain have an average speed of at most 61.0 kph."""
    rain = df[df["weather"] == "rain"]
    condition = rain["avg_speed_kph"] <= 61.0
    truth = condition.all()
    if truth:
        expl = f"All {len(rain)} rain routes satisfy avg_speed_kph <= 61.0."
    else:
        viol = rain[~condition]
        viol_info = ", ".join(f"{r['route_id']}({r['avg_speed_kph']})" for _, r in viol.iterrows())
        expl = f"{len(viol)} rain routes violate the rule: {viol_info}."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All windy routes have an average speed of at least 51.9 kph."""
    windy = df[df["weather"] == "windy"]
    condition = windy["avg_speed_kph"] >= 51.9
    truth = condition.all()
    if truth:
        expl = f"All {len(windy)} windy routes satisfy avg_speed_kph >= 51.9."
    else:
        viol = windy[~condition]
        viol_info = ", ".join(f"{r['route_id']}({r['avg_speed_kph']})" for _, r in viol.iterrows())
        expl = f"{len(viol)} windy routes violate the rule: {viol_info}."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All vans travel a distance of at least 74.9 km."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["distance_km"] >= 74.9
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans travel >= 74.9 km."
    else:
        viol = vans[~condition]
        viol_info = ", ".join(f"{r['route_id']}({r['distance_km']})" for _, r in viol.iterrows())
        expl = f"{len(viol)} vans violate the rule: {viol_info}."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All trucks use no more than 27.2 liters of fuel."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["fuel_used_l"] <= 27.2
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks use <= 27.2 liters."
    else:
        viol = trucks[~condition]
        viol_info = ", ".join(f"{r['route_id']}({r['fuel_used_l']})" for _, r in viol.iterrows())
        expl = f"{len(viol)} trucks violate the rule: {viol_info}."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All routes longer than 200 km involve either a van or a truck."""
    long = df[df["distance_km"] > 200]
    condition = long["vehicle_type"].isin(["van", "truck"])
    truth = condition.all()
    if truth:
        expl = f"All {len(long)} routes >200 km involve a van or truck."
    else:
        viol = long[~condition]
        viol_info = ", ".join(f"{r['route_id']}({r['vehicle_type']})" for _, r in viol.iterrows())
        expl = f"{len(viol)} routes >200 km violate the rule: {viol_info}."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Any route with an average speed of 62 kph or higher uses a van or a truck."""
    fast = df[df["avg_speed_kph"] >= 62]
    condition = fast["vehicle_type"].isin(["van", "truck"])
    truth = condition.all()
    if truth:
        expl = f"All {len(fast)} routes with avg_speed >= 62 use a van or truck."
    else:
        viol = fast[~condition]
        viol_info = ", ".join(f"{r['route_id']}({r['vehicle_type']})" for _, r in viol.iterrows())
        expl = f"{len(viol)} fast routes violate the rule: {viol_info}."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All routes that used more than 40 liters of fuel were vans."""
    high_fuel = df[df["fuel_used_l"] > 40]
    condition = high_fuel["vehicle_type"] == "van"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fuel)} routes with fuel >40 liters are vans."
    else:
        viol = high_fuel[~condition]
        viol_info = ", ".join(f"{r['route_id']}({r['vehicle_type']})" for _, r in viol.iterrows())
        expl = f"{len(viol)} high-fuel routes violate the rule: {viol_info}."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_63.csv")

    # Convert numeric columns safely
    for col in ["distance_km", "avg_speed_kph", "fuel_used_l", "delay_minutes"]:
        if col in df.columns:
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
        (9, stmt_9),
        (10, stmt_10),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()