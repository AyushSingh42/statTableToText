

import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. Trucks have higher fuel consumption per kilometer compared to vans and buses."""
    trucks = df[df['vehicle_type'] == 'truck']
    vans = df[df['vehicle_type'] == 'van']
    buses = df[df['vehicle_type'] == 'bus']
    truck_fuel_per_km = trucks['fuel_used_l'] / trucks['distance_km']
    van_fuel_per_km = vans['fuel_used_l'] / vans['distance_km']
    bus_fuel_per_km = buses['fuel_used_l'] / buses['distance_km']
    truck_avg = truck_fuel_per_km.mean()
    van_avg = van_fuel_per_km.mean() if not vans.empty else float('inf')
    bus_avg = bus_fuel_per_km.mean() if not buses.empty else float('inf')
    truth = (truck_avg > van_avg) and (truck_avg > bus_avg)
    parts = []
    if vans.empty:
        parts.append("no van routes")
    else:
        parts.append(f"van average fuel per km: {van_avg:.2f}")
    if buses.empty:
        parts.append("no bus routes")
    else:
        parts.append(f"bus average fuel per km: {bus_avg:.2f}")
    expl = f"Truck's average fuel per km ({truck_avg:.2f}) is {'higher than' if truth else 'not higher than'} {', '.join(parts)}."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Routes with windy weather conditions have higher average delays than routes with rainy or clear conditions."""
    windy = df[df['weather'] == 'windy']
    rainy = df[df['weather'] == 'rainy']
    clear = df[df['weather'] == 'clear']
    windy_avg = windy['delay_minutes'].mean()
    rainy_avg = rainy['delay_minutes'].mean()
    clear_avg = clear['delay_minutes'].mean()
    truth = (windy_avg > rainy_avg) and (windy_avg > clear_avg)
    expl = f"Windy average delay ({windy_avg:.2f}) is {'higher than' if truth else 'not higher than'} rainy ({rainy_avg:.2f}) and clear ({clear_avg:.2f})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all vehicle types, fuel_used_l is approximately proportional to distance_km, with consistent fuel efficiency rates per category."""
    vehicle_types = df['vehicle_type'].unique()
    results = []
    for vtype in vehicle_types:
        subset = df[df['vehicle_type'] == vtype]
        if subset.empty or len(subset) < 2:
            continue
        corr = subset['distance_km'].corr(subset['fuel_used_l'])
        if corr < 0.9:
            results.append((vtype, corr))
    if not results:
        truth = True
        expl = "All vehicle types have high correlation (>=0.9) between distance_km and fuel_used_l."
    else:
        truth = False
        expl = f"Vehicle types {', '.join([v for v, _ in results])} have lower correlation ({', '.join([f'{c:.2f}' for _, c in results])}) between distance_km and fuel_used_l."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a route has vehicle type truck and weather is windy, then delay_minutes exceeds 24."""
    condition = (df['vehicle_type'] == 'truck') & (df['weather'] == 'windy')
    subset = df[condition]
    truth = subset['delay_minutes'].gt(24).all()
    if truth:
        expl = f"All {len(subset)} truck routes in windy weather have delay_minutes >24."
    else:
        viol = subset[~subset['delay_minutes'].gt(24)]
        expl = f"{len(viol)} violations found: {', '.join(map(str, viol['delay_minutes'].tolist()))}."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Van routes with average speeds above 55 kph have fuel_used_l less than or equal to 12 liters."""
    vans = df[df['vehicle_type'] == 'van']
    condition = vans['avg_speed_kph'] > 55
    subset = vans[condition]
    truth = subset['fuel_used_l'].le(12).all()
    if truth:
        expl = f"All {len(subset)} van routes with speed >55 have fuel_used_l <=12."
    else:
        viol = subset[~subset['fuel_used_l'].le(12)]
        expl = f"{len(viol)} violations found: {', '.join(map(str, viol['fuel_used_l'].tolist()))}."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All routes with delay_minutes exceeding 20 are associated with windy weather conditions."""
    subset = df[df['delay_minutes'] > 20]
    truth = subset['weather'].eq('windy').all()
    if truth:
        expl = f"All {len(subset)} routes with delay >20 have windy weather."
    else:
        viol = subset[~subset['weather'].eq('windy')]
        expl = f"{len(viol)} violations found: weather {', '.join(viol['weather'].unique())}."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Buses operating in cloudy weather have lower fuel_used_l compared to buses operating in windy weather."""
    buses_cloudy = df[(df['vehicle_type'] == 'bus') & (df['weather'] == 'cloudy')]
    buses_windy = df[(df['vehicle_type'] == 'bus') & (df['weather'] == 'windy')]
    if buses_cloudy.empty or buses_windy.empty:
        truth = buses_cloudy.empty or buses_windy.empty
        expl = "No data for one or both conditions."
    else:
        avg_cloudy = buses_cloudy['fuel_used_l'].mean()
        avg_windy = buses_windy['fuel_used_l'].mean()
        truth = avg_cloudy < avg_windy
        expl = f"Cloudy buses avg fuel: {avg_cloudy:.2f}, windy buses avg fuel: {avg_windy:.2f}. {'Lower' if truth else 'Not lower'}."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For every vehicle type, routes with distance_km exceeding 150 km have fuel_used_l greater than 25 liters."""
    vehicle_types = df['vehicle_type'].unique()
    violations = []
    for vtype in vehicle_types:
        subset = df[df['vehicle_type'] == vtype]
        condition = subset['distance_km'] > 150
        viol = subset[condition & (subset['fuel_used_l'] <= 25)]
        if not viol.empty:
            violations.append((vtype, len(viol)))
    truth = len(violations) == 0
    if truth:
        expl = "All vehicle types meet the condition."
    else:
        expl = f"Violations found in {', '.join([f'{v} ({c})' for v, c in violations])} vehicle types."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a route has vehicle type van and weather is clear, then delay_minutes is less than 7."""
    condition = (df['vehicle_type'] == 'van') & (df['weather'] == 'clear')
    subset = df[condition]
    truth = subset['delay_minutes'].lt(7).all()
    if truth:
        expl = f"All {len(subset)} van routes in clear weather have delay <7."
    else:
        viol = subset[~subset['delay_minutes'].lt(7)]
        expl = f"{len(viol)} violations found: {', '.join(map(str, viol['delay_minutes'].tolist()))}."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Truck routes are the only ones with distance_km exceeding 200 km, and these routes have the highest fuel_used_l and delay_minutes among all vehicle types."""
    non_truck_long = df[(df['vehicle_type']!= 'truck') & (df['distance_km'] > 200)]
    part1 = non_truck_long.empty
    truck_long = df[(df['vehicle_type'] == 'truck') & (df['distance_km'] > 200)]
    if truck_long.empty:
        part2 = True
        expl_part2 = "No truck routes with distance >200."
    else:
        other_routes = df[df['vehicle_type']!= 'truck']
        max_fuel = other_routes['fuel_used_l'].max()
        max_delay = other_routes['delay_minutes'].max()
        part2_fuel = truck_long['fuel_used_l'].min() > max_fuel
        part2_delay = truck_long['delay_minutes'].min() > max_delay
        part2 = part2_fuel and part2_delay
        expl_part2 = f"Truck routes have min fuel {truck_long['fuel_used_l'].min()} > {max_fuel} and min delay {truck_long['delay_minutes'].min()} > {max_delay}."
    truth = part1 and part2
    expl = f"Only trucks have distance >200: {part1}. Truck routes have highest fuel and delay: {part2}. {expl_part2}"
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. In rainy weather conditions, bus routes experience higher delays than van routes."""
    rainy_buses = df[(df['weather'] == 'rainy') & (df['vehicle_type'] == 'bus')]
    rainy_vans = df[(df['weather'] == 'rainy') & (df['vehicle_type'] == 'van')]
    if rainy_buses.empty or rainy_vans.empty:
        truth = rainy_buses.empty and rainy_vans.empty
        expl = "No data for one or both vehicle types in rainy weather."
    else:
        avg_bus = rainy_buses['delay_minutes'].mean()
        avg_van = rainy_vans['delay_minutes'].mean()
        truth = avg_bus > avg_van
        expl = f"Rainy bus avg delay: {avg_bus:.2f}, van avg delay: {avg_van:.2f}. {'Higher' if truth else 'Not higher'}."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Routes with vehicle type bus and weather conditions other than clear have delay_minutes between 17 and 21."""
    condition = (df['vehicle_type'] == 'bus') & (df['weather']!= 'clear')
    subset = df[condition]
    truth = subset['delay_minutes'].between(17, 21, inclusive='both').all()
    if truth:
        expl = f"All {len(subset)} bus routes in non-clear weather have delays between 17-21."
    else:
        viol = subset[~subset['delay_minutes'].between(17, 21, inclusive='both')]
        expl = f"{len(viol)} violations found: {', '.join(map(str, viol['delay_minutes'].tolist()))}."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. For all vehicle types except trucks in clear weather, average speed decreases as delay_minutes increases."""
    excluded = (df['vehicle_type'] == 'truck') & (df['weather'] == 'clear')
    included = df[~excluded]
    groups = included.groupby(['vehicle_type', 'weather'])
    violations = []
    for name, group in groups:
        if len(group) < 2:
            continue
        corr = group['avg_speed_kph'].corr(group['delay_minutes'])
        if corr >= 0:
            violations.append(name)
    truth = len(violations) == 0
    if truth:
        expl = "All groups except trucks in clear weather have negative correlation between speed and delay."
    else:
        expl = f"Violations in groups {', '.join(violations)} have non-negative correlation."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Van routes with distance_km below 100 km have both the highest average speeds and the lowest fuel_used_l among all vehicle types."""
    vans_short = df[(df['vehicle_type'] == 'van') & (df['distance_km'] < 100)]
    if vans_short.empty:
        truth = True
        expl = "No van routes with distance <100 km."
        return truth, expl
    short_routes = df[df['distance_km'] < 100]
    groups = short_routes.groupby('vehicle_type')
    speed_dict = {}
    fuel_dict = {}
    for name, group in groups:
        speed_dict[name] = group['avg_speed_kph'].mean()
        fuel_dict[name] = group['fuel_used_l'].mean()
    van_speed = speed_dict.get('van', 0)
    van_fuel = fuel_dict.get('van', float('inf'))
    max_speed = max(speed_dict.values())
    min_fuel = min(fuel_dict.values())
    truth = (van_speed == max_speed) and (van_fuel == min_fuel)
    expl = f"Van avg speed: {van_speed}, max speed: {max_speed}; van fuel: {van_fuel}, min fuel: {min_fuel}. {'True' if truth else 'False'}."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a route has vehicle type bus and weather is cloudy, then delay_minutes is between 18 and 19."""
    condition = (df['vehicle_type'] == 'bus') & (df['weather'] == 'cloudy')
    subset = df[condition]
    truth = subset['delay_minutes'].between(18, 19, inclusive='both').all()
    if truth:
        expl = f"All {len(subset)} bus routes in cloudy weather have delays between 18-19."
    else:
        viol = subset[~subset['delay_minutes'].between(18, 19, inclusive='both')]
        expl = f"{len(viol)} violations found: {', '.join(map(str, viol['delay_minutes'].tolist()))}."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_3.csv")
    df['distance_km'] = pd.to_numeric(df['distance_km'], errors='coerce')
    df['fuel_used_l'] = pd.to_numeric(df['fuel_used_l'], errors='coerce')
    df['delay_minutes'] = pd.to_numeric(df['delay_minutes'], errors='coerce')
    df['avg_speed_kph'] = pd.to_numeric(df['avg_speed_kph'], errors='coerce')
    checks = [
        (1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5),
        (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10),
        (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()