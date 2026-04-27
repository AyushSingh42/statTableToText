import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles that traveled in windy weather had an average speed of less than 60 kph."""
    windy = df[df["weather"] == "windy"]
    if windy.empty:
        truth = True
        expl = "No vehicles traveled in windy weather."
    else:
        condition = windy["avg_speed_kph"] < 60
        truth = condition.all()
        if truth:
            expl = f"All {len(windy)} vehicles in windy weather had speed < 60 kph."
        else:
            viol = windy[~condition]
            expl = f"{len(viol)} vehicles in windy weather violated the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a bus, then its fuel used is greater than 10 liters."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        truth = True
        expl = "No buses in dataset."
    else:
        condition = buses["fuel_used_l"] > 10
        truth = condition.all()
        if truth:
            expl = f"All {len(buses)} buses had fuel > 10 liters."
        else:
            viol = buses[~condition]
            expl = f"{len(viol)} buses violated the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one truck that traveled a distance of more than 160 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        truth = False
        expl = "No trucks in dataset."
    else:
        condition = trucks["distance_km"] > 160
        truth = condition.any()
        if truth:
            expl = f"At least one truck ({trucks[condition]['route_id'].iloc[0]}) traveled > 160 km."
        else:
            expl = f"No trucks traveled > 160 km."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All vehicles that had a delay of less than 10 minutes had an average speed of greater than 50 kph."""
    delays = df[df["delay_minutes"] < 10]
    if delays.empty:
        truth = True
        expl = "No vehicles had delay < 10 minutes."
    else:
        condition = delays["avg_speed_kph"] > 50
        truth = condition.all()
        if truth:
            expl = f"All {len(delays)} vehicles with delay < 10 min had speed > 50 kph."
        else:
            viol = delays[~condition]
            expl = f"{len(viol)} vehicles with delay < 10 min violated the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle is a van, then its distance traveled is less than 200 km."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        truth = True
        expl = "No vans in dataset."
    else:
        condition = vans["distance_km"] < 200
        truth = condition.all()
        if truth:
            expl = f"All {len(vans)} vans traveled < 200 km."
        else:
            viol = vans[~condition]
            expl = f"{len(viol)} vans violated the rule (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most vehicles that traveled in clear weather had an average speed of greater than 55 kph."""
    clear = df[df["weather"] == "clear"]
    if clear.empty:
        truth = True
        expl = "No vehicles traveled in clear weather."
    else:
        condition = clear["avg_speed_kph"] > 55
        count_true = condition.sum()
        total = len(clear)
        truth = count_true > total / 2
        if truth:
            expl = f"Most ({count_true}/{total}) vehicles in clear weather had speed > 55 kph."
        else:
            expl = f"Only {count_true}/{total} vehicles in clear weather had speed > 55 kph."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All buses that traveled a distance of more than 200 km had a fuel used of greater than 25 liters."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        truth = True
        expl = "No buses in dataset."
    else:
        filtered = buses[buses["distance_km"] > 200]
        if filtered.empty:
            truth = True
            expl = "No buses traveled > 200 km."
        else:
            condition = filtered["fuel_used_l"] > 25
            truth = condition.all()
            if truth:
                expl = f"All {len(filtered)} buses with distance > 200 km had fuel > 25 liters."
            else:
                viol = filtered[~condition]
                expl = f"{len(viol)} buses with distance > 200 km violated the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle had a delay of more than 20 minutes, then its average speed was less than 55 kph."""
    delays = df[df["delay_minutes"] > 20]
    if delays.empty:
        truth = True
        expl = "No vehicles had delay > 20 minutes."
    else:
        condition = delays["avg_speed_kph"] < 55
        truth = condition.all()
        if truth:
            expl = f"All {len(delays)} vehicles with delay > 20 min had speed < 55 kph."
        else:
            viol = delays[~condition]
            expl = f"{len(viol)} vehicles with delay > 20 min violated the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one bus that traveled in rainy weather and had a fuel used of more than 30 liters."""
    buses_rainy = df[(df["vehicle_type"] == "bus") & (df["weather"] == "rain")]
    if buses_rainy.empty:
        truth = False
        expl = "No buses traveled in rainy weather."
    else:
        condition = buses_rainy["fuel_used_l"] > 30
        truth = condition.any()
        if truth:
            expl = f"At least one bus in rainy weather had fuel > 30 liters."
        else:
            expl = f"No buses in rainy weather had fuel > 30 liters."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All trucks that had an average speed of greater than 55 kph had a distance traveled of less than 180 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        truth = True
        expl = "No trucks in dataset."
    else:
        filtered = trucks[trucks["avg_speed_kph"] > 55]
        if filtered.empty:
            truth = True
            expl = "No trucks had speed > 55 kph."
        else:
            condition = filtered["distance_km"] < 180
            truth = condition.all()
            if truth:
                expl = f"All {len(filtered)} trucks with speed > 55 kph had distance < 180 km."
            else:
                viol = filtered[~condition]
                expl = f"{len(viol)} trucks with speed > 55 kph violated the rule (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle had a fuel used of less than 15 liters, then its distance traveled was less than 150 km."""
    fuels = df[df["fuel_used_l"] < 15]
    if fuels.empty:
        truth = True
        expl = "No vehicles had fuel < 15 liters."
    else:
        condition = fuels["distance_km"] < 150
        truth = condition.all()
        if truth:
            expl = f"All {len(fuels)} vehicles with fuel < 15 liters had distance < 150 km."
        else:
            viol = fuels[~condition]
            expl = f"{len(viol)} vehicles with fuel < 15 liters violated the rule (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most vehicles that had a delay of more than 15 minutes had a fuel used of greater than 20 liters."""
    delays = df[df["delay_minutes"] > 15]
    if delays.empty:
        truth = True
        expl = "No vehicles had delay > 15 minutes."
    else:
        condition = delays["fuel_used_l"] > 20
        count_true = condition.sum()
        total = len(delays)
        truth = count_true > total / 2
        if truth:
            expl = f"Most ({count_true}/{total}) vehicles with delay > 15 min had fuel > 20 liters."
        else:
            expl = f"Only {count_true}/{total} vehicles with delay > 15 min had fuel > 20 liters."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All vehicles that traveled in cloudy weather had a delay of more than 10 minutes."""
    cloudy = df[df["weather"] == "cloudy"]
    if cloudy.empty:
        truth = True
        expl = "No vehicles traveled in cloudy weather."
    else:
        condition = cloudy["delay_minutes"] > 10
        truth = condition.all()
        if truth:
            expl = f"All {len(cloudy)} vehicles in cloudy weather had delay > 10 minutes."
        else:
            viol = cloudy[~condition]
            expl = f"{len(viol)} vehicles in cloudy weather violated the rule (delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a truck, then its average speed is less than 60 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        truth = True
        expl = "No trucks in dataset."
    else:
        condition = trucks["avg_speed_kph"] < 60
        truth = condition.all()
        if truth:
            expl = f"All {len(trucks)} trucks had speed < 60 kph."
        else:
            viol = trucks[~condition]
            expl = f"{len(viol)} trucks violated the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one van that had a fuel used of more than 35 liters and traveled a distance of less than 100 km."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        truth = False
        expl = "No vans in dataset."
    else:
        condition = (vans["fuel_used_l"] > 35) & (vans["distance_km"] < 100)
        truth = condition.any()
        if truth:
            expl = f"At least one van had fuel > 35 liters and distance < 100 km."
        else:
            expl = f"No vans met both criteria."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All buses that had an average speed of greater than 60 kph had a distance traveled of less than 150 km."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        truth = True
        expl = "No buses in dataset."
    else:
        filtered = buses[buses["avg_speed_kph"] > 60]
        if filtered.empty:
            truth = True
            expl = "No buses had speed > 60 kph."
        else:
            condition = filtered["distance_km"] < 150
            truth = condition.all()
            if truth:
                expl = f"All {len(filtered)} buses with speed > 60 kph had distance < 150 km."
            else:
                viol = filtered[~condition]
                expl = f"{len(viol)} buses with speed > 60 kph violated the rule (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a vehicle had a delay of less than 5 minutes, then its average speed was greater than 50 kph."""
    delays = df[df["delay_minutes"] < 5]
    if delays.empty:
        truth = True
        expl = "No vehicles had delay < 5 minutes."
    else:
        condition = delays["avg_speed_kph"] > 50
        truth = condition.all()
        if truth:
            expl = f"All {len(delays)} vehicles with delay < 5 min had speed > 50 kph."
        else:
            viol = delays[~condition]
            expl = f"{len(viol)} vehicles with delay < 5 min violated the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_43.csv")

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
        (8, stmt_8),
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()