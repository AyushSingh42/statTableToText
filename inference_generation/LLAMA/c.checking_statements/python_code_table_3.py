import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All truck routes have higher average speeds than van routes."""
    truck_routes = df[df["vehicle_type"] == "truck"]
    van_routes = df[df["vehicle_type"] == "van"]
    truck_avg_speeds = truck_routes["avg_speed_kph"]
    van_avg_speeds = van_routes["avg_speed_kph"]
    truth = (truck_avg_speeds > van_avg_speeds).all()
    if truth:
        expl = f"All {len(truck_routes)} truck routes have higher average speeds than van routes."
    else:
        viol = truck_routes[truck_avg_speeds <= van_avg_speeds]
        expl = f"{len(viol)} truck routes violate the rule (avg speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If the weather is clear, then the delay minutes are less than 15."""
    clear_weather = df[df["weather"] == "clear"]
    truth = (clear_weather["delay_minutes"] < 15).all()
    if truth:
        expl = f"All {len(clear_weather)} routes with clear weather have delay minutes less than 15."
    else:
        viol = clear_weather[clear_weather["delay_minutes"] >= 15]
        expl = f"{len(viol)} routes with clear weather violate the rule (delay minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every bus route with a distance greater than 150 km has an average speed less than 50 kph."""
    bus_routes = df[df["vehicle_type"] == "bus"]
    long_bus_routes = bus_routes[bus_routes["distance_km"] > 150]
    truth = (long_bus_routes["avg_speed_kph"] < 50).all()
    if truth:
        expl = f"All {len(long_bus_routes)} bus routes with distance greater than 150 km have average speed less than 50 kph."
    else:
        viol = long_bus_routes[long_bus_routes["avg_speed_kph"] >= 50]
        expl = f"{len(viol)} bus routes with distance greater than 150 km violate the rule (avg speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. The maximum fuel used by a van is less than the minimum fuel used by a truck."""
    van_routes = df[df["vehicle_type"] == "van"]
    truck_routes = df[df["vehicle_type"] == "truck"]
    max_van_fuel = van_routes["fuel_used_l"].max()
    min_truck_fuel = truck_routes["fuel_used_l"].min()
    truth = max_van_fuel < min_truck_fuel
    if truth:
        expl = f"The maximum fuel used by a van ({max_van_fuel} liters) is less than the minimum fuel used by a truck ({min_truck_fuel} liters)."
    else:
        expl = f"The maximum fuel used by a van ({max_van_fuel} liters) is not less than the minimum fuel used by a truck ({min_truck_fuel} liters)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All routes with a delay of more than 20 minutes have a weather condition of either rain or windy."""
    delayed_routes = df[df["delay_minutes"] > 20]
    truth = delayed_routes["weather"].isin(["rain", "windy"]).all()
    if truth:
        expl = f"All {len(delayed_routes)} routes with delay more than 20 minutes have weather condition of either rain or windy."
    else:
        viol = delayed_routes[~delayed_routes["weather"].isin(["rain", "windy"])]
        expl = f"{len(viol)} routes with delay more than 20 minutes violate the rule (weather conditions: {', '.join(map(str, viol['weather'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a route has a distance less than 100 km, then the fuel used is less than 15 liters."""
    short_routes = df[df["distance_km"] < 100]
    truth = (short_routes["fuel_used_l"] < 15).all()
    if truth:
        expl = f"All {len(short_routes)} routes with distance less than 100 km have fuel used less than 15 liters."
    else:
        viol = short_routes[short_routes["fuel_used_l"] >= 15]
        expl = f"{len(viol)} routes with distance less than 100 km violate the rule (fuel used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. The average speed of truck routes is higher than the average speed of bus routes."""
    truck_routes = df[df["vehicle_type"] == "truck"]
    bus_routes = df[df["vehicle_type"] == "bus"]
    truck_avg_speed = truck_routes["avg_speed_kph"].mean()
    bus_avg_speed = bus_routes["avg_speed_kph"].mean()
    truth = truck_avg_speed > bus_avg_speed
    if truth:
        expl = f"The average speed of truck routes ({truck_avg_speed} kph) is higher than the average speed of bus routes ({bus_avg_speed} kph)."
    else:
        expl = f"The average speed of truck routes ({truck_avg_speed} kph) is not higher than the average speed of bus routes ({bus_avg_speed} kph)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All routes with a weather condition of cloudy have a delay of more than 10 minutes."""
    cloudy_routes = df[df["weather"] == "cloudy"]
    truth = (cloudy_routes["delay_minutes"] > 10).all()
    if truth:
        expl = f"All {len(cloudy_routes)} routes with weather condition of cloudy have delay more than 10 minutes."
    else:
        viol = cloudy_routes[cloudy_routes["delay_minutes"] <= 10]
        expl = f"{len(viol)} routes with weather condition of cloudy violate the rule (delay minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Every route with an average speed greater than 60 kph has a distance greater than 150 km."""
    fast_routes = df[df["avg_speed_kph"] > 60]
    truth = (fast_routes["distance_km"] > 150).all()
    if truth:
        expl = f"All {len(fast_routes)} routes with average speed greater than 60 kph have distance greater than 150 km."
    else:
        viol = fast_routes[fast_routes["distance_km"] <= 150]
        expl = f"{len(viol)} routes with average speed greater than 60 kph violate the rule (distances: {', '.join(map(str, viol['distance_km'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a route has a fuel used of more than 40 liters, then the vehicle type is a truck."""
    high_fuel_routes = df[df["fuel_used_l"] > 40]
    truth = high_fuel_routes["vehicle_type"].isin(["truck"]).all()
    if truth:
        expl = f"All {len(high_fuel_routes)} routes with fuel used more than 40 liters have vehicle type of truck."
    else:
        viol = high_fuel_routes[~high_fuel_routes["vehicle_type"].isin(["truck"])]
        expl = f"{len(viol)} routes with fuel used more than 40 liters violate the rule (vehicle types: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. The minimum distance traveled by a bus is greater than the maximum distance traveled by a van."""
    bus_routes = df[df["vehicle_type"] == "bus"]
    van_routes = df[df["vehicle_type"] == "van"]
    min_bus_distance = bus_routes["distance_km"].min()
    max_van_distance = van_routes["distance_km"].max()
    truth = min_bus_distance > max_van_distance
    if truth:
        expl = f"The minimum distance traveled by a bus ({min_bus_distance} km) is greater than the maximum distance traveled by a van ({max_van_distance} km)."
    else:
        expl = f"The minimum distance traveled by a bus ({min_bus_distance} km) is not greater than the maximum distance traveled by a van ({max_van_distance} km)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All routes with a delay of less than 10 minutes have a weather condition of clear."""
    short_delay_routes = df[df["delay_minutes"] < 10]
    truth = short_delay_routes["weather"].isin(["clear"]).all()
    if truth:
        expl = f"All {len(short_delay_routes)} routes with delay less than 10 minutes have weather condition of clear."
    else:
        viol = short_delay_routes[~short_delay_routes["weather"].isin(["clear"])]
        expl = f"{len(viol)} routes with delay less than 10 minutes violate the rule (weather conditions: {', '.join(map(str, viol['weather'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Every truck route with a distance less than 200 km has an average speed greater than 60 kph."""
    truck_routes = df[df["vehicle_type"] == "truck"]
    short_truck_routes = truck_routes[truck_routes["distance_km"] < 200]
    truth = (short_truck_routes["avg_speed_kph"] > 60).all()
    if truth:
        expl = f"All {len(short_truck_routes)} truck routes with distance less than 200 km have average speed greater than 60 kph."
    else:
        viol = short_truck_routes[short_truck_routes["avg_speed_kph"] <= 60]
        expl = f"{len(viol)} truck routes with distance less than 200 km violate the rule (avg speeds: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a route has a weather condition of rain, then the delay minutes are greater than 5 minutes."""
    rainy_routes = df[df["weather"] == "rain"]
    truth = (rainy_routes["delay_minutes"] > 5).all()
    if truth:
        expl = f"All {len(rainy_routes)} routes with weather condition of rain have delay minutes greater than 5 minutes."
    else:
        viol = rainy_routes[rainy_routes["delay_minutes"] <= 5]
        expl = f"{len(viol)} routes with weather condition of rain violate the rule (delay minutes: {', '.join(map(str, viol['delay_minutes'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All routes with an average speed less than 50 kph have a vehicle type of bus."""
    slow_routes = df[df["avg_speed_kph"] < 50]
    truth = slow_routes["vehicle_type"].isin(["bus"]).all()
    if truth:
        expl = f"All {len(slow_routes)} routes with average speed less than 50 kph have vehicle type of bus."
    else:
        viol = slow_routes[~slow_routes["vehicle_type"].isin(["bus"])]
        expl = f"{len(viol)} routes with average speed less than 50 kph violate the rule (vehicle types: {', '.join(map(str, viol['vehicle_type'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_3.csv")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10), (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()