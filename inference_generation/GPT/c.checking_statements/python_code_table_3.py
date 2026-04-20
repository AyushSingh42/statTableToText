import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. Most truck routes (4 out of 5) have an average speed above 60 kph, with only one truck route averaging 59.6 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    total = len(trucks)
    high = trucks[trucks["avg_speed_kph"] > 60]
    low = trucks[trucks["avg_speed_kph"] <= 60]
    truth = (total == 5) and (len(high) == 4) and (len(low) == 1) and (abs(low["avg_speed_kph"].iloc[0] - 59.6) < 1e-3)
    if truth:
        expl = f"Exactly 5 truck routes: 4 >60 kph, 1 = {low['avg_speed_kph'].iloc[0]:.1f} kph."
    else:
        expl = f"Truck count={total}, >60 kph={len(high)}, ≤60 kph={len(low)} (values: {low['avg_speed_kph'].tolist()})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All bus routes have average speeds below 50 kph, ranging from 46.9 to 49.7 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        return False, "No bus records found."
    min_speed = buses["avg_speed_kph"].min()
    max_speed = buses["avg_speed_kph"].max()
    truth = (max_speed < 50) and (min_speed >= 46.9) and (max_speed <= 49.7)
    if truth:
        expl = f"Bus speeds span {min_speed:.1f}–{max_speed:.1f} kph, all <50."
    else:
        expl = f"Bus speed range is {min_speed:.1f}–{max_speed:.1f} kph (expected 46.9–49.7 and <50)."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every route that experienced rain recorded a delay of at least 7 minutes."""
    rainy = df[df["weather"] == "rain"]
    if rainy.empty:
        return False, "No rainy records to evaluate."
    truth = (rainy["delay_minutes"] >= 7).all()
    if truth:
        expl = f"All {len(rainy)} rainy routes have delay ≥7 min."
    else:
        viol = rainy[rainy["delay_minutes"] < 7]
        expl = f"{len(viol)} rainy routes violate (delays: {viol['delay_minutes'].tolist()})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Vans consistently show the lowest fuel consumption per kilometer, with values between 0.11 and 0.12 L/km, lower than any bus or truck route."""
    df = df.copy()
    df["fuel_per_km"] = df["fuel_used_l"] / df["distance_km"]
    vans = df[df["vehicle_type"] == "van"]
    others = df[df["vehicle_type"].isin(["bus", "truck"])]
    if vans.empty or others.empty:
        return False, "Missing van or other vehicle records."
    van_min, van_max = vans["fuel_per_km"].min(), vans["fuel_per_km"].max()
    truth = (van_min >= 0.11) and (van_max <= 0.12) and (van_max < others["fuel_per_km"].min())
    if truth:
        expl = f"Van consumption 0.11–0.12 L/km; next lowest (bus/truck) is {others['fuel_per_km'].min():.3f} L/km."
    else:
        viol = vans[(vans["fuel_per_km"] < 0.11) | (vans["fuel_per_km"] > 0.12)]
        expl = f"Van values out of range: {viol['fuel_per_km'].tolist()}, or not lowest (min others {others['fuel_per_km'].min():.3f})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Clear weather occurs only on truck and van routes; no bus route in the data was recorded under clear conditions."""
    clear = df[df["weather"] == "clear"]
    if clear.empty:
        return False, "No clear‑weather records to evaluate."
    allowed = set(["truck", "van"])
    truth = clear["vehicle_type"].isin(list(allowed)).all() and (df[(df["weather"] == "clear") & (df["vehicle_type"] == "bus")].empty)
    if truth:
        expl = f"All {len(clear)} clear routes are {set(clear['vehicle_type'].unique())}."
    else:
        bad = clear[~clear["vehicle_type"].isin(list(allowed))]
        expl = f"{len(bad)} clear routes have disallowed types: {bad['vehicle_type'].tolist()}."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. The longest route (R013, 231.4 km) is a truck route in windy weather and also has the highest fuel usage (49.5 L) and the greatest delay (27 minutes) among all records."""
    longest = df.loc[df["distance_km"].idxmax()]
    max_fuel = df["fuel_used_l"].max()
    max_delay = df["delay_minutes"].max()
    truth = (
        longest["route_id"] == "R013"
        and abs(longest["distance_km"] - 231.4) < 1e-3
        and longest["vehicle_type"] == "truck"
        and longest["weather"] == "windy"
        and abs(longest["fuel_used_l"] - 49.5) < 1e-3
        and longest["fuel_used_l"] == max_fuel
        and longest["delay_minutes"] == max_delay
        and max_delay == 27
    )
    if truth:
        expl = "Record matches all specified attributes."
    else:
        details = []
        if longest["route_id"]!= "R013":
            details.append(f"route_id={longest['route_id']}")
        if abs(longest["distance_km"] - 231.4) >= 1e-3:
            details.append(f"distance={longest['distance_km']}")
        if longest["vehicle_type"]!= "truck":
            details.append(f"vehicle_type={longest['vehicle_type']}")
        if longest["weather"]!= "windy":
            details.append(f"weather={longest['weather']}")
        if abs(longest["fuel_used_l"] - 49.5) >= 1e-3:
            details.append(f"fuel_used={longest['fuel_used_l']}")
        if longest["delay_minutes"]!= 27:
            details.append(f"delay={longest['delay_minutes']}")
        expl = "Mismatches: " + "; ".join(details)
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All truck routes use more than 39 L of fuel, which is higher than any van (≤12 L) or bus (≤31.4 L) route."""
    trucks = df[df["vehicle_type"] == "truck"]
    vans = df[df["vehicle_type"] == "van"]
    buses = df[df["vehicle_type"] == "bus"]
    if trucks.empty or vans.empty or buses.empty:
        return False, "Missing one of the vehicle categories."
    truth = (
        (trucks["fuel_used_l"] > 39).all()
        and (vans["fuel_used_l"] <= 12).all()
        and (buses["fuel_used_l"] <= 31.4).all()
        and (trucks["fuel_used_l"].min() > vans["fuel_used_l"].max())
        and (trucks["fuel_used_l"].min() > buses["fuel_used_l"].max())
    )
    if truth:
        expl = f"Truck min fuel {trucks['fuel_used_l'].min():.1f}>39; van max {vans['fuel_used_l'].max():.1f}≤12; bus max {buses['fuel_used_l'].max():.1f}≤31.4."
    else:
        viol = []
        if not (trucks["fuel_used_l"] > 39).all():
            viol.append(f"truck fuel ≤39 ({trucks[trucks['fuel_used_l'] <= 39]['fuel_used_l'].tolist()})")
        if not (vans["fuel_used_l"] <= 12).all():
            viol.append(f"van fuel >12 ({vans[vans['fuel_used_l'] > 12]['fuel_used_l'].tolist()})")
        if not (buses["fuel_used_l"] <= 31.4).all():
            viol.append(f"bus fuel >31.4 ({buses[buses['fuel_used_l'] > 31.4]['fuel_used_l'].tolist()})")
        expl = "; ".join(viol)
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most windy routes (2 out of 3) are truck routes, indicating trucks are more frequently affected by windy conditions in this dataset."""
    windy = df[df["weather"] == "windy"]
    total = len(windy)
    truck_windy = windy[windy["vehicle_type"] == "truck"]
    truth = (total == 3) and (len(truck_windy) == 2)
    if truth:
        expl = f"3 windy routes, 2 are trucks."
    else:
        expl = f"Windy total={total}, truck windy={len(truck_windy)}."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_3.csv")
    # Convert any numeric columns stored as strings to proper numeric types
    for col in ["distance_km", "avg_speed_kph", "fuel_used_l", "delay_minutes"]:
        if df[col].dtype == object:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    # Example of converting a turn/route number string to integer
    if "route_id" in df.columns:
        df["route_num"] = df["route_id"].str.extract(r"(\d+)").astype(int)
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