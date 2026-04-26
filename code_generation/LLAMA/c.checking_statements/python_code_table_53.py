import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles that traveled in clear weather had an average speed greater than 45 kph."""
    clear_weather = df[df["weather"] == "clear"]
    if clear_weather.empty:
        truth = True
        expl = "No vehicles traveled in clear weather."
    else:
        condition = clear_weather["avg_speed_kph"] > 45
        truth = condition.all()
        if truth:
            expl = f"All {len(clear_weather)} vehicles in clear weather exceeded 45 kph."
        else:
            viol = clear_weather[~condition]
            expl = f"{len(viol)} vehicles in clear weather did not exceed 45 kph."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a van, then its fuel used is less than 20 liters."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        truth = True
        expl = "No vans in dataset."
    else:
        condition = vans["fuel_used_l"] < 20
        truth = condition.all()
        if truth:
            expl = f"All {len(vans)} vans used less than 20 liters."
        else:
            viol = vans[~condition]
            expl = f"{len(viol)} vans used 20 liters or more."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one bus that traveled a distance greater than 180 km."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        truth = False
        expl = "No buses in dataset."
    else:
        condition = buses["distance_km"] > 180
        truth = condition.any()
        if truth:
            expl = f"At least one bus traveled over 180 km."
        else:
            expl = f"No buses traveled over 180 km."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All trucks that traveled in windy weather had a delay of less than 17 minutes."""
    trucks_windy = df[(df["vehicle_type"] == "truck") & (df["weather"] == "windy")]
    if trucks_windy.empty:
        truth = True
        expl = "No trucks traveled in windy weather."
    else:
        condition = trucks_windy["delay_minutes"] < 17
        truth = condition.all()
        if truth:
            expl = f"All {len(trucks_windy)} trucks in windy weather had delays under 17 minutes."
        else:
            viol = trucks_windy[~condition]
            expl = f"{len(viol)} trucks in windy weather had delays of 17 minutes or more."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle is a bus, then its average speed is greater than 51 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        truth = True
        expl = "No buses in dataset."
    else:
        condition = buses["avg_speed_kph"] > 51
        truth = condition.all()
        if truth:
            expl = f"All {len(buses)} buses exceeded 51 kph."
        else:
            viol = buses[~condition]
            expl = f"{len(viol)} buses did not exceed 51 kph."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most vehicles that traveled in rain had a delay of less than 22 minutes."""
    rainy = df[df["weather"] == "rain"]
    if rainy.empty:
        truth = True
        expl = "No vehicles traveled in rain."
    else:
        condition = rainy["delay_minutes"] < 22
        count_less = condition.sum()
        total = len(rainy)
        truth = count_less > total / 2
        if truth:
            expl = f"More than half ({count_less}/{total}) of rainy vehicles had delays under 22 minutes."
        else:
            expl = f"Less than half ({count_less}/{total}) of rainy vehicles had delays under 22 minutes."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All vehicles with a distance traveled greater than 200 km had an average speed greater than 50 kph."""
    long_distance = df[df["distance_km"] > 200]
    if long_distance.empty:
        truth = True
        expl = "No vehicles traveled over 200 km."
    else:
        condition = long_distance["avg_speed_kph"] > 50
        truth = condition.all()
        if truth:
            expl = f"All {len(long_distance)} vehicles over 200 km exceeded 50 kph."
        else:
            viol = long_distance[~condition]
            expl = f"{len(viol)} vehicles over 200 km did not exceed 50 kph."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a truck, then its fuel used is greater than 13 liters."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        truth = True
        expl = "No trucks in dataset."
    else:
        condition = trucks["fuel_used_l"] > 13
        truth = condition.all()
        if truth:
            expl = f"All {len(trucks)} trucks used more than 13 liters."
        else:
            viol = trucks[~condition]
            expl = f"{len(viol)} trucks used 13 liters or less."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one van that traveled a distance less than 70 km."""
    vans = df[df["vehicle_type"] == "van"]
    if vans.empty:
        truth = False
        expl = "No vans in dataset."
    else:
        condition = vans["distance_km"] < 70
        truth = condition.any()
        if truth:
            expl = f"At least one van traveled under 70 km."
        else:
            expl = f"No vans traveled under 70 km."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All buses that traveled in clear weather had a fuel used greater than 20 liters."""
    buses_clear = df[(df["vehicle_type"] == "bus") & (df["weather"] == "clear")]
    if buses_clear.empty:
        truth = True
        expl = "No buses traveled in clear weather."
    else:
        condition = buses_clear["fuel_used_l"] > 20
        truth = condition.all()
        if truth:
            expl = f"All {len(buses_clear)} buses in clear weather used more than 20 liters."
        else:
            viol = buses_clear[~condition]
            expl = f"{len(viol)} buses in clear weather used 20 liters or less."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle's average speed is greater than 60 kph, then its delay is less than 15 minutes."""
    fast = df[df["avg_speed_kph"] > 60]
    if fast.empty:
        truth = True
        expl = "No vehicles exceeded 60 kph."
    else:
        condition = fast["delay_minutes"] < 15
        truth = condition.all()
        if truth:
            expl = f"All {len(fast)} fast vehicles had delays under 15 minutes."
        else:
            viol = fast[~condition]
            expl = f"{len(viol)} fast vehicles had delays of 15 minutes or more."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most vehicles that traveled in clear weather had an average speed greater than 50 kph."""
    clear = df[df["weather"] == "clear"]
    if clear.empty:
        truth = True
        expl = "No vehicles traveled in clear weather."
    else:
        condition = clear["avg_speed_kph"] > 50
        count_fast = condition.sum()
        total = len(clear)
        truth = count_fast > total / 2
        if truth:
            expl = f"More than half ({count_fast}/{total}) of clear weather vehicles exceeded 50 kph."
        else:
            expl = f"Less than half ({count_fast}/{total}) of clear weather vehicles exceeded 50 kph."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All vehicles with a delay of less than 10 minutes had an average speed greater than 45 kph."""
    short_delay = df[df["delay_minutes"] < 10]
    if short_delay.empty:
        truth = True
        expl = "No vehicles had delays under 10 minutes."
    else:
        condition = short_delay["avg_speed_kph"] > 45
        truth = condition.all()
        if truth:
            expl = f"All {len(short_delay)} vehicles with short delays exceeded 45 kph."
        else:
            viol = short_delay[~condition]
            expl = f"{len(viol)} vehicles with short delays did not exceed 45 kph."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a bus, then its distance traveled is greater than 70 km."""
    buses = df[df["vehicle_type"] == "bus"]
    if buses.empty:
        truth = True
        expl = "No buses in dataset."
    else:
        condition = buses["distance_km"] > 70
        truth = condition.all()
        if truth:
            expl = f"All {len(buses)} buses traveled over 70 km."
        else:
            viol = buses[~condition]
            expl = f"{len(viol)} buses traveled 70 km or less."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one truck that traveled a distance greater than 220 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    if trucks.empty:
        truth = False
        expl = "No trucks in dataset."
    else:
        condition = trucks["distance_km"] > 220
        truth = condition.any()
        if truth:
            expl = f"At least one truck traveled over 220 km."
        else:
            expl = f"No trucks traveled over 220 km."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All vans that traveled in rain had a fuel used less than 20 liters."""
    vans_rain = df[(df["vehicle_type"] == "van") & (df["weather"] == "rain")]
    if vans_rain.empty:
        truth = True
        expl = "No vans traveled in rain."
    else:
        condition = vans_rain["fuel_used_l"] < 20
        truth = condition.all()
        if truth:
            expl = f"All {len(vans_rain)} vans in rain used less than 20 liters."
        else:
            viol = vans_rain[~condition]
            expl = f"{len(viol)} vans in rain used 20 liters or more."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a vehicle's fuel used is greater than 30 liters, then its distance traveled is greater than 150 km."""
    high_fuel = df[df["fuel_used_l"] > 30]
    if high_fuel.empty:
        truth = True
        expl = "No vehicles used more than 30 liters."
    else:
        condition = high_fuel["distance_km"] > 150
        truth = condition.all()
        if truth:
            expl = f"All {len(high_fuel)} vehicles with high fuel use traveled over 150 km."
        else:
            viol = high_fuel[~condition]
            expl = f"{len(viol)} vehicles with high fuel use traveled 150 km or less."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most vehicles that traveled in rain had a fuel used greater than 15 liters."""
    rainy = df[df["weather"] == "rain"]
    if rainy.empty:
        truth = True
        expl = "No vehicles traveled in rain."
    else:
        condition = rainy["fuel_used_l"] > 15
        count_high = condition.sum()
        total = len(rainy)
        truth = count_high > total / 2
        if truth:
            expl = f"More than half ({count_high}/{total}) of rainy vehicles used more than 15 liters."
        else:
            expl = f"Less than half ({count_high}/{total}) of rainy vehicles used more than 15 liters."
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
        (18, stmt_18)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()