import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All trucks have an average speed between 46.4 and 62.4 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"].between(46.4, 62.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have speeds between 46.4 and 62.4 kph."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the speed range (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All buses have a delay between 12 and 25 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["delay_minutes"].between(12, 25, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses have delays between 12 and 25 minutes."
    else:
        viol = buses[~condition]
        expl = f"{len(viol)} buses violate the delay range (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All vans have a delay between 3 and 20 minutes."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["delay_minutes"].between(3, 20, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans have delays between 3 and 20 minutes."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans violate the delay range (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a truck travels in clear weather, its delay does not exceed 17 minutes."""
    trucks_clear = df[(df["vehicle_type"] == "truck") & (df["weather"] == "clear")]
    condition = trucks_clear["delay_minutes"] <= 17
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks_clear)} clear-weather trucks have delays ≤ 17 minutes."
    else:
        viol = trucks_clear[~condition]
        expl = f"{len(viol)} clear-weather trucks exceed 17-minute delay (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a bus travels in rain, its delay is at least 12 minutes."""
    buses_rain = df[(df["vehicle_type"] == "bus") & (df["weather"] == "rain")]
    condition = buses_rain["delay_minutes"] >= 12
    truth = condition.all()
    if truth:
        expl = f"All {len(buses_rain)} rainy-weather buses have delays ≥ 12 minutes."
    else:
        viol = buses_rain[~condition]
        expl = f"{len(viol)} rainy-weather buses have delays < 12 minutes (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. There exists a van that used less than 22 liters of fuel."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["fuel_used_l"] < 22
    truth = condition.any()
    if truth:
        found = vans[condition].iloc[0]
        expl = f"A van (ID: {found['route_id']}) used {found['fuel_used_l']} liters, which is less than 22."
    else:
        expl = "No van used less than 22 liters of fuel."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most routes (13 out of 15) have a delay greater than 10 minutes."""
    total_routes = len(df)
    delay_gt_10 = df["delay_minutes"] > 10
    count_gt_10 = delay_gt_10.sum()
    truth = count_gt_10 >= 13
    if truth:
        expl = f"{count_gt_10} out of {total_routes} routes have delays > 10 minutes (≥13 as required)."
    else:
        expl = f"{count_gt_10} out of {total_routes} routes have delays > 10 minutes (<13 required)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_23.csv")

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
        (7, stmt_7)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()