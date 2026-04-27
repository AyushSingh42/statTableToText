import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles that traveled in the rain had a delay of 10 minutes or more, except for one bus that had a delay of 6 minutes."""
    rain_df = df[df['weather'] == 'rain']
    buses_rain = rain_df[rain_df['vehicle_type'] == 'bus']
    other_rain = rain_df[(rain_df['vehicle_type']!= 'bus') | (rain_df['delay_minutes']!= 6)]
    
    # Check if all non-bus rain vehicles have delay >= 10
    condition = other_rain['delay_minutes'] >= 10
    # Check if exactly one bus has delay = 6
    bus_delay_6 = buses_rain[buses_rain['delay_minutes'] == 6]
    
    truth = condition.all() and len(bus_delay_6) == 1
    if truth:
        expl = "All rain vehicles except one bus (with 6 min delay) had delay >= 10."
    else:
        expl = "Either some rain vehicles had delay < 10 or multiple buses had delay = 6."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All buses that traveled in the wind had an average speed of 55 kph or more."""
    wind_buses = df[(df['weather'] == 'wind') & (df['vehicle_type'] == 'bus')]
    condition = wind_buses['avg_speed_kph'] >= 55
    truth = condition.all()
    if truth:
        expl = f"All {len(wind_buses)} wind buses had avg speed >= 55 kph."
    else:
        viol = wind_buses[~condition]
        expl = f"{len(viol)} wind buses violated the rule (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a vehicle traveled in the clear weather, then its fuel used was 12.5 liters or less."""
    clear_df = df[df['weather'] == 'clear']
    condition = clear_df['fuel_used_l'] <= 12.5
    truth = condition.all()
    if truth:
        expl = f"All {len(clear_df)} clear weather vehicles used <= 12.5L fuel."
    else:
        viol = clear_df[~condition]
        expl = f"{len(viol)} clear weather vehicles used > 12.5L fuel (amounts: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one truck that traveled in the rain and had a delay of 11 minutes."""
    trucks_rain = df[(df['vehicle_type'] == 'truck') & (df['weather'] == 'rain') & (df['delay_minutes'] == 11)]
    truth = len(trucks_rain) >= 1
    if truth:
        expl = f"Found {len(trucks_rain)} truck(s) in rain with 11 min delay."
    else:
        expl = "No truck found in rain with 11 min delay."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All vans had a distance traveled of 200 km or less."""
    vans = df[df['vehicle_type'] == 'van']
    condition = vans['distance_km'] <= 200
    truth = condition.all()
    if truth:
        expl = f"All {len(vans)} vans traveled <= 200 km."
    else:
        viol = vans[~condition]
        expl = f"{len(viol)} vans traveled > 200 km (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a vehicle had a delay of 15 minutes or more, then it was a bus."""
    delayed_15_plus = df[df['delay_minutes'] >= 15]
    condition = delayed_15_plus['vehicle_type'] == 'bus'
    truth = condition.all()
    if truth:
        expl = f"All {len(delayed_15_plus)} vehicles with delay >= 15 were buses."
    else:
        viol = delayed_15_plus[~condition]
        expl = f"{len(viol)} non-buses had delay >= 15 (types: {', '.join(viol['vehicle_type'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most vehicles that traveled in the rain had a fuel used of 30 liters or more."""
    rain_df = df[df['weather'] == 'rain']
    condition = rain_df['fuel_used_l'] >= 30
    count_30_plus = condition.sum()
    total_rain = len(rain_df)
    truth = count_30_plus > total_rain / 2
    if truth:
        expl = f"More than half ({count_30_plus}/{total_rain}) of rain vehicles used >= 30L fuel."
    else:
        expl = f"Less than half ({count_30_plus}/{total_rain}) of rain vehicles used >= 30L fuel."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All buses that had a distance traveled of 180 km or more had an average speed of 56 kph or more."""
    buses_long = df[(df['vehicle_type'] == 'bus') & (df['distance_km'] >= 180)]
    condition = buses_long['avg_speed_kph'] >= 56
    truth = condition.all()
    if truth:
        expl = f"All {len(buses_long)} long-distance buses had avg speed >= 56 kph."
    else:
        viol = buses_long[~condition]
        expl = f"{len(viol)} long-distance buses had speed < 56 kph (speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a vehicle had an average speed of 60 kph or more, then it was a van."""
    fast = df[df['avg_speed_kph'] >= 60]
    condition = fast['vehicle_type'] == 'van'
    truth = condition.all()
    if truth:
        expl = f"All {len(fast)} fast vehicles were vans."
    else:
        viol = fast[~condition]
        expl = f"{len(viol)} non-vans had speed >= 60 (types: {', '.join(viol['vehicle_type'].tolist())})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one bus that traveled in the wind and had a fuel used of 12.2 liters."""
    wind_buses = df[(df['weather'] == 'wind') & (df['vehicle_type'] == 'bus') & (df['fuel_used_l'] == 12.2)]
    truth = len(wind_buses) >= 1
    if truth:
        expl = f"Found {len(wind_buses)} wind bus(es) with 12.2L fuel."
    else:
        expl = "No wind bus found with 12.2L fuel."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All trucks that traveled in the clear weather had a distance traveled of 200 km or less."""
    clear_trucks = df[(df['weather'] == 'clear') & (df['vehicle_type'] == 'truck')]
    condition = clear_trucks['distance_km'] <= 200
    truth = condition.all()
    if truth:
        expl = f"All {len(clear_trucks)} clear weather trucks traveled <= 200 km."
    else:
        viol = clear_trucks[~condition]
        expl = f"{len(viol)} clear weather trucks traveled > 200 km (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a vehicle had a delay of 10 minutes or less, then it was a bus."""
    low_delay = df[df['delay_minutes'] <= 10]
    condition = low_delay['vehicle_type'] == 'bus'
    truth = condition.all()
    if truth:
        expl = f"All {len(low_delay)} low-delay vehicles were buses."
    else:
        viol = low_delay[~condition]
        expl = f"{len(viol)} non-buses had delay <= 10 (types: {', '.join(viol['vehicle_type'].tolist())})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All vehicles that had a fuel used of 40 liters or more had a distance traveled of 200 km or less."""
    high_fuel = df[df['fuel_used_l'] >= 40]
    condition = high_fuel['distance_km'] <= 200
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fuel)} high-fuel vehicles traveled <= 200 km."
    else:
        viol = high_fuel[~condition]
        expl = f"{len(viol)} high-fuel vehicles traveled > 200 km (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Most vehicles that traveled in the wind had a delay of 15 minutes or less."""
    wind_df = df[df['weather'] == 'wind']
    condition = wind_df['delay_minutes'] <= 15
    count_15_or_less = condition.sum()
    total_wind = len(wind_df)
    truth = count_15_or_less > total_wind / 2
    if truth:
        expl = f"More than half ({count_15_or_less}/{total_wind}) of wind vehicles had delay <= 15."
    else:
        expl = f"Less than half ({count_15_or_less}/{total_wind}) of wind vehicles had delay <= 15."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a vehicle had a distance traveled of 150 km or less, then it was a van."""
    short_distance = df[df['distance_km'] <= 150]
    condition = short_distance['vehicle_type'] == 'van'
    truth = condition.all()
    if truth:
        expl = f"All {len(short_distance)} short-distance vehicles were vans."
    else:
        viol = short_distance[~condition]
        expl = f"{len(viol)} non-vans traveled <= 150 km (types: {', '.join(viol['vehicle_type'].tolist())})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one truck that traveled in the rain and had a fuel used of 24.6 liters."""
    rain_trucks = df[(df['vehicle_type'] == 'truck') & (df['weather'] == 'rain') & (df['fuel_used_l'] == 24.6)]
    truth = len(rain_trucks) >= 1
    if truth:
        expl = f"Found {len(rain_trucks)} rain truck(s) with 24.6L fuel."
    else:
        expl = "No rain truck found with 24.6L fuel."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All buses that had a delay of 10 minutes or less had a distance traveled of 200 km or more."""
    buses_low_delay = df[(df['vehicle_type'] == 'bus') & (df['delay_minutes'] <= 10)]
    condition = buses_low_delay['distance_km'] >= 200
    truth = condition.all()
    if truth:
        expl = f"All {len(buses_low_delay)} low-delay buses traveled >= 200 km."
    else:
        viol = buses_low_delay[~condition]
        expl = f"{len(viol)} low-delay buses traveled < 200 km (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a vehicle had an average speed of 50 kph or less, then it was a truck."""
    slow = df[df['avg_speed_kph'] <= 50]
    condition = slow['vehicle_type'] == 'truck'
    truth = condition.all()
    if truth:
        expl = f"All {len(slow)} slow vehicles were trucks."
    else:
        viol = slow[~condition]
        expl = f"{len(viol)} non-trucks had speed <= 50 (types: {', '.join(viol['vehicle_type'].tolist())})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All vehicles that traveled in the rain had a fuel used of 10 liters or more."""
    rain_df = df[df['weather'] == 'rain']
    condition = rain_df['fuel_used_l'] >= 10
    truth = condition.all()
    if truth:
        expl = f"All {len(rain_df)} rain vehicles used >= 10L fuel."
    else:
        viol = rain_df[~condition]
        expl = f"{len(viol)} rain vehicles used < 10L fuel (amounts: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. Most vehicles that had a distance traveled of 200 km or more had an average speed of 55 kph or more."""
    long_distance = df[df['distance_km'] >= 200]
    condition = long_distance['avg_speed_kph'] >= 55
    count_fast = condition.sum()
    total_long = len(long_distance)
    truth = count_fast > total_long / 2
    if truth:
        expl = f"More than half ({count_fast}/{total_long}) of long-distance vehicles had speed >= 55 kph."
    else:
        expl = f"Less than half ({count_fast}/{total_long}) of long-distance vehicles had speed >= 55 kph."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_93.csv")

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
        (17, stmt_17),
        (18, stmt_18),
        (19, stmt_19),
        (20, stmt_20)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()