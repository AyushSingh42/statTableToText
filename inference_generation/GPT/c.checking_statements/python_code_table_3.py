import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All trucks have an average speed of at least 59.6 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"] >= 59.6
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks meet the speed requirement."
    else:
        viol = trucks[~condition]
        ids = ", ".join(map(str, viol["route_id"].tolist()))
        speeds = ", ".join(map(str, viol["avg_speed_kph"].tolist()))
        expl = f"{len(viol)} trucks violate the rule (route_id: {ids}; speeds: {speeds})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All vans have an average speed between 52.0 kph and 57.2 kph."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["avg_speed_kph"].between(52.0, 57.2, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans are within the speed range."
    else:
        viol = vans[~condition]
        ids = ", ".join(map(str, viol["route_id"].tolist()))
        speeds = ", ".join(map(str, viol["avg_speed_kph"].tolist()))
        expl = f"{len(viol)} vans violate the rule (route_id: {ids}; speeds: {speeds})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All buses have an average speed between 46.9 kph and 49.7 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["avg_speed_kph"].between(46.9, 49.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses are within the speed range."
    else:
        viol = buses[~condition]
        ids = ", ".join(map(str, viol["route_id"].tolist()))
        speeds = ", ".join(map(str, viol["avg_speed_kph"].tolist()))
        expl = f"{len(viol)} buses violate the rule (route_id: {ids}; speeds: {speeds})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All trucks consume at least 0.210 liters of fuel per kilometer."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["fuel_used_l"] >= 0.210
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks meet the fuel consumption minimum."
    else:
        viol = trucks[~condition]
        ids = ", ".join(map(str, viol["route_id"].tolist()))
        fuels = ", ".join(map(str, viol["fuel_used_l"].tolist()))
        expl = f"{len(viol)} trucks violate the rule (route_id: {ids}; fuel_used_l: {fuels})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All vans consume less than 0.13 liters of fuel per kilometer."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["fuel_used_l"] < 0.13
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans satisfy the fuel consumption limit."
    else:
        viol = vans[~condition]
        ids = ", ".join(map(str, viol["route_id"].tolist()))
        fuels = ", ".join(map(str, viol["fuel_used_l"].tolist()))
        expl = f"{len(viol)} vans violate the rule (route_id: {ids}; fuel_used_l: {fuels})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All buses have fuel consumption per kilometer between 0.199 L/km and 0.203 L/km."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["fuel_used_l"].between(0.199, 0.203, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(buses)} buses are within the fuel consumption range."
    else:
        viol = buses[~condition]
        ids = ", ".join(map(str, viol["route_id"].tolist()))
        fuels = ", ".join(map(str, viol["fuel_used_l"].tolist()))
        expl = f"{len(viol)} buses violate the rule (route_id: {ids}; fuel_used_l: {fuels})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All routes in clear weather have a delay of at most 14 minutes."""
    clear = df[df["weather"] == "clear"]
    condition = clear["delay_minutes"] <= 14
    truth = condition.all()
    if truth:
        expl = f"All {len(clear)} clear-weather routes meet the delay limit."
    else:
        viol = clear[~condition]
        ids = ", ".join(map(str, viol["route_id"].tolist()))
        delays = ", ".join(map(str, viol["delay_minutes"].tolist()))
        expl = f"{len(viol)} clear-weather routes violate the rule (route_id: {ids}; delays: {delays})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All windy routes have a delay of at least 21 minutes."""
    windy = df[df["weather"] == "windy"]
    condition = windy["delay_minutes"] >= 21
    truth = condition.all()
    if truth:
        expl = f"All {len(windy)} windy routes meet the delay minimum."
    else:
        viol = windy[~condition]
        ids = ", ".join(map(str, viol["route_id"].tolist()))
        delays = ", ".join(map(str, viol["delay_minutes"].tolist()))
        expl = f"{len(viol)} windy routes violate the rule (route_id: {ids}; delays: {delays})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_3.csv")
    # Convert possible string identifiers to integers
    if df["route_id"].dtype == object:
        df["route_id"] = pd.to_numeric(df["route_id"], errors="coerce").astype("Int64")
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