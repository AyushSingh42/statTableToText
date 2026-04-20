import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All trucks have an average speed of over 60 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(trucks)} trucks have an average speed of over 60 kph."
    else:
        viol = trucks[~condition]
        expl = f"{len(viol)} trucks violate the rule (average speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. There exists at least one van that traveled less than 100 km."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["distance_km"] < 100
    truth = condition.any()
    if truth:
        expl = f"There are {len(vans[condition])} vans that traveled less than 100 km."
    else:
        expl = "No vans traveled less than 100 km."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Most buses experienced delays of over 15 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["delay_minutes"] > 15
    truth = len(buses[condition]) > len(buses) / 2
    if truth:
        expl = f"{len(buses[condition])} buses experienced delays of over 15 minutes, which is more than half of all buses."
    else:
        expl = f"{len(buses[condition])} buses experienced delays of over 15 minutes, which is not more than half of all buses."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If the weather was clear, then the average delay was less than 12 minutes."""
    clear_weather = df[df["weather"] == "clear"]
    condition = clear_weather["delay_minutes"] < 12
    truth = condition.all()
    if truth:
        expl = f"All {len(clear_weather)} vehicles with clear weather had an average delay of less than 12 minutes."
    else:
        viol = clear_weather[~condition]
        expl = f"{len(viol)} vehicles with clear weather violate the rule (average delays: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All vehicles that traveled over 200 km were trucks."""
    long_distance = df[df["distance_km"] > 200]
    condition = long_distance["vehicle_type"] == "truck"
    truth = condition.all()
    if truth:
        expl = f"All {len(long_distance)} vehicles that traveled over 200 km were trucks."
    else:
        viol = long_distance[~condition]
        expl = f"{len(viol)} vehicles that traveled over 200 km were not trucks (vehicle types: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. There exists at least one bus that used over 30 liters of fuel."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["fuel_used_l"] > 30
    truth = condition.any()
    if truth:
        expl = f"There are {len(buses[condition])} buses that used over 30 liters of fuel."
    else:
        expl = "No buses used over 30 liters of fuel."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most vans had an average speed of over 53 kph."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["avg_speed_kph"] > 53
    truth = len(vans[condition]) > len(vans) / 2
    if truth:
        expl = f"{len(vans[condition])} vans had an average speed of over 53 kph, which is more than half of all vans."
    else:
        expl = f"{len(vans[condition])} vans had an average speed of over 53 kph, which is not more than half of all vans."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If the weather was windy, then the average fuel used was over 40 liters."""
    windy_weather = df[df["weather"] == "windy"]
    condition = windy_weather["fuel_used_l"] > 40
    truth = condition.all()
    if truth:
        expl = f"All {len(windy_weather)} vehicles with windy weather had an average fuel used of over 40 liters."
    else:
        viol = windy_weather[~condition]
        expl = f"{len(viol)} vehicles with windy weather violate the rule (average fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All vehicles that experienced delays of less than 10 minutes were vans."""
    short_delay = df[df["delay_minutes"] < 10]
    condition = short_delay["vehicle_type"] == "van"
    truth = condition.all()
    if truth:
        expl = f"All {len(short_delay)} vehicles that experienced delays of less than 10 minutes were vans."
    else:
        viol = short_delay[~condition]
        expl = f"{len(viol)} vehicles that experienced delays of less than 10 minutes were not vans (vehicle types: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_3.csv")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()