import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles that traveled in the rain had a delay of 10 minutes or more, except for one bus that had a delay of 6 minutes."""
    rain = df[df["weather"] == "rain"]
    condition = (rain["delay_minutes"] >= 10) | ((rain["vehicle_type"] == "bus") & (rain["delay_minutes"] == 6))
    violations = rain[~condition]
    bus6 = rain[(rain["vehicle_type"] == "bus") & (rain["delay_minutes"] == 6)]
    truth = violations.empty and len(bus6) == 1
    if truth:
        expl = f"All {len(rain)} rain vehicles satisfy the rule; exactly one bus has delay 6."
    else:
        viol_ids = violations["route_id"].tolist()
        expl = f"{len(violations)} rain vehicles violate the rule (ids: {', '.join(viol_ids)})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All buses that traveled in the wind had an average speed of 55 kph or more."""
    buses_wind = df[(df["vehicle_type"] == "bus") & (df["weather"] == "wind")]
    truth = (buses_wind["avg_speed_kph"] >= 55).all()
    if truth:
        expl = f"All {len(buses_wind)} wind buses have avg speed ≥55."
    else:
        viol = buses_wind[buses_wind["avg_speed_kph"] < 55]
        expl = f"{len(viol)} wind buses violate the rule (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a vehicle traveled in the clear weather, then its fuel used was 12.5 liters or less."""
    clear = df[df["weather"] == "clear"]
    truth = (clear["fuel_used_l"] <= 12.5).all()
    if truth:
        expl = f"All {len(clear)} clear vehicles use ≤12.5 L."
    else:
        viol = clear[clear["fuel_used_l"] > 12.5]
        expl = f"{len(viol)} clear vehicles exceed 12.5 L (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one truck that traveled in the rain and had a delay of 11 minutes."""
    exists = ((df["vehicle_type"] == "truck") & (df["weather"] == "rain") & (df["delay_minutes"] == 11)).any()
    if exists:
        expl = "At least one truck meets the criteria."
    else:
        expl = "No truck satisfies the criteria."
    return exists, expl

def stmt_5(df: pd.DataFrame):
    """5. All vans had a distance traveled of 200 km or less."""
    vans = df[df["vehicle_type"] == "van"]
    truth = (vans["distance_km"] <= 200).all()
    if truth:
        expl = f"All {len(vans)} vans travel ≤200 km."
    else:
        viol = vans[vans["distance_km"] > 200]
        expl = f"{len(viol)} vans exceed 200 km (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a vehicle had a delay of 15 minutes or more, then it was a bus."""
    delay_ge15 = df[df["delay_minutes"] >= 15]
    truth = (delay_ge15["vehicle_type"] == "bus").all()
    if truth:
        expl = f"All {len(delay_ge15)} vehicles with delay ≥15 are buses."
    else:
        viol = delay_ge15[delay_ge15["vehicle_type"]!= "bus"]
        expl = f"{len(viol)} vehicles with delay ≥15 are not buses (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most vehicles that traveled in the rain had a fuel used of 30 liters or more."""
    rain = df[df["weather"] == "rain"]
    fuel_ge30 = rain["fuel_used_l"] >= 30
    truth = fuel_ge30.sum() > len(rain) / 2
    if truth:
        expl = f"{fuel_ge30.sum()} of {len(rain)} rain vehicles use ≥30 L."
    else:
        expl = f"Only {fuel_ge30.sum()} of {len(rain)} rain vehicles use ≥30 L."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All buses that had a distance traveled of 180 km or more had an average speed of 56 kph or more."""
    buses_dist_ge180 = df[(df["vehicle_type"] == "bus") & (df["distance_km"] >= 180)]
    truth = (buses_dist_ge180["avg_speed_kph"] >= 56).all()
    if truth:
        expl = f"All {len(buses_dist_ge180)} buses with distance ≥180 km have avg speed ≥56."
    else:
        viol = buses_dist_ge180[buses_dist_ge180["avg_speed_kph"] < 56]
        expl = f"{len(viol)} buses violate the rule (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a vehicle had an average speed of 60 kph or more, then it was a van."""
    speed_ge60 = df[df["avg_speed_kph"] >= 60]
    truth = (speed_ge60["vehicle_type"] == "van").all()
    if truth:
        expl = f"All {len(speed_ge60)} vehicles with speed ≥60 are vans."
    else:
        viol = speed_ge60[speed_ge60["vehicle_type"]!= "van"]
        expl = f"{len(viol)} vehicles with speed ≥60 are not vans (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one bus that traveled in the wind and had a fuel used of 12.2 liters."""
    exists = ((df["vehicle_type"] == "bus") & (df["weather"] == "wind") & (df["fuel_used_l"] == 12.2)).any()
    if exists:
        expl = "At least one bus meets the criteria."
    else:
        expl = "No bus satisfies the criteria."
    return exists, expl

def stmt_11(df: pd.DataFrame):
    """11. All trucks that traveled in the clear weather had a distance traveled of 200 km or less."""
    trucks_clear = df[(df["vehicle_type"] == "truck") & (df["weather"] == "clear")]
    truth = (trucks_clear["distance_km"] <= 200).all()
    if truth:
        expl = f"All {len(trucks_clear)} clear trucks travel ≤200 km."
    else:
        viol = trucks_clear[trucks_clear["distance_km"] > 200]
        expl = f"{len(viol)} clear trucks exceed 200 km (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a vehicle had a delay of 10 minutes or less, then it was a bus."""
    delay_le10 = df[df["delay_minutes"] <= 10]
    truth = (delay_le10["vehicle_type"] == "bus").all()
    if truth:
        expl = f"All {len(delay_le10)} vehicles with delay ≤10 are buses."
    else:
        viol = delay_le10[delay_le10["vehicle_type"]!= "bus"]
        expl = f"{len(viol)} vehicles with delay ≤10 are not buses (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All vehicles that had a fuel used of 40 liters or more had a distance traveled of 200 km or less."""
    fuel_ge40 = df[df["fuel_used_l"] >= 40]
    truth = (fuel_ge40["distance_km"] <= 200).all()
    if truth:
        expl = f"All {len(fuel_ge40)} vehicles with fuel ≥40 L travel ≤200 km."
    else:
        viol = fuel_ge40[fuel_ge40["distance_km"] > 200]
        expl = f"{len(viol)} vehicles with fuel ≥40 L exceed 200 km (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Most vehicles that traveled in the wind had a delay of 15 minutes or less."""
    wind = df[df["weather"] == "wind"]
    delay_le15 = wind["delay_minutes"] <= 15
    truth = delay_le15.sum() > len(wind) / 2
    if truth:
        expl = f"{delay_le15.sum()} of {len(wind)} wind vehicles have delay ≤15."
    else:
        expl = f"Only {delay_le15.sum()} of {len(wind)} wind vehicles have delay ≤15."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a vehicle had a distance traveled of 150 km or less, then it was a van."""
    dist_le150 = df[df["distance_km"] <= 150]
    truth = (dist_le150["vehicle_type"] == "van").all()
    if truth:
        expl = f"All {len(dist_le150)} vehicles with distance ≤150 are vans."
    else:
        viol = dist_le150[dist_le150["vehicle_type"]!= "van"]
        expl = f"{len(viol)} vehicles with distance ≤150 are not vans (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one truck that traveled in the rain and had a fuel used of 24.6 liters."""
    exists = ((df["vehicle_type"] == "truck") & (df["weather"] == "rain") & (df["fuel_used_l"] == 24.6)).any()
    if exists:
        expl = "At least one truck meets the criteria."
    else:
        expl = "No truck satisfies the criteria."
    return exists, expl

def stmt_17(df: pd.DataFrame):
    """17. All buses that had a delay of 10 minutes or less had a distance traveled of 200 km or more."""
    buses_delay_le10 = df[(df["vehicle_type"] == "bus") & (df["delay_minutes"] <= 10)]
    truth = (buses_delay_le10["distance_km"] >= 200).all()
    if truth:
        expl = f"All {len(buses_delay_le10)} buses with delay ≤10 travel ≥200 km."
    else:
        viol = buses_delay_le10[buses_delay_le10["distance_km"] < 200]
        expl = f"{len(viol)} buses violate the rule (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a vehicle had an average speed of 50 kph or less, then it was a truck."""
    speed_le50 = df[df["avg_speed_kph"] <= 50]
    truth = (speed_le50["vehicle_type"] == "truck").all()
    if truth:
        expl = f"All {len(speed_le50)} vehicles with speed ≤50 are trucks."
    else:
        viol = speed_le50[speed_le50["vehicle_type"]!= "truck"]
        expl = f"{len(viol)} vehicles with speed ≤50 are not trucks (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All vehicles that traveled in the rain had a fuel used of 10 liters or more."""
    rain = df[df["weather"] == "rain"]
    truth = (rain["fuel_used_l"] >= 10).all()
    if truth:
        expl = f"All {len(rain)} rain vehicles use ≥10 L."
    else:
        viol = rain[rain["fuel_used_l"] < 10]
        expl = f"{len(viol)} rain vehicles use <10 L (ids: {', '.join(viol['route_id'])})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. Most vehicles that had a distance traveled of 200 km or more had an average speed of 55 kph or more."""
    dist_ge200 = df[df["distance_km"] >= 200]
    speed_ge55 = dist_ge200["avg_speed_kph"] >= 55
    truth = speed_ge55.sum() > len(dist_ge200) / 2
    if truth:
        expl = f"{speed_ge55.sum()} of {len(dist_ge200)} vehicles with distance ≥200 have speed ≥55."
    else:
        expl = f"Only {speed_ge55.sum()} of {len(dist_ge200)} vehicles with distance ≥200 have speed ≥55."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_93.csv")

    # Convert numeric columns safely
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors="coerce")
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
        (17, stmt_17),
        (18, stmt_18),
        (19, stmt_19),
        (20, stmt_20),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()