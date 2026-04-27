import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles with a distance greater than 200 km have an average speed greater than 60 kph."""
    subset = df[df["distance_km"] > 200]
    if subset.empty:
        return True, "No vehicles with distance >200 km, so the statement holds vacuously."
    condition = subset["avg_speed_kph"] > 60
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vehicles with distance >200 km have avg_speed >60 kph."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} vehicles violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a bus, then its fuel used is less than 50 liters."""
    subset = df[df["vehicle_type"] == "bus"]
    if subset.empty:
        return True, "No buses in the data, so the statement holds vacuously."
    condition = subset["fuel_used_l"] < 50
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} buses have fuel_used <50 liters."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} buses violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one truck with a delay of less than 12 minutes."""
    subset = df[(df["vehicle_type"] == "truck") & (df["delay_minutes"] < 12)]
    truth = not subset.empty
    if truth:
        return True, f"Found {len(subset)} truck(s) with delay <12 minutes."
    else:
        return False, "No truck with delay <12 minutes found."

def stmt_4(df: pd.DataFrame):
    """4. All vans with a distance less than 120 km have an average speed greater than 50 kph."""
    subset = df[(df["vehicle_type"] == "van") & (df["distance_km"] < 120)]
    if subset.empty:
        return True, "No vans with distance <120 km, so the statement holds vacuously."
    condition = subset["avg_speed_kph"] > 50
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vans with distance <120 km have avg_speed >50 kph."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} vans violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle is a truck, then its average speed is less than 60 kph."""
    subset = df[df["vehicle_type"] == "truck"]
    if subset.empty:
        return True, "No trucks in the data, so the statement holds vacuously."
    condition = subset["avg_speed_kph"] < 60
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} trucks have avg_speed <60 kph."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} trucks violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."

def stmt_6(df: pd.DataFrame):
    """6. Most vehicles have a delay of less than 20 minutes."""
    total = len(df)
    count = (df["delay_minutes"] < 20).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% ({count}/{total}) of vehicles have delay <20 minutes."
    else:
        return False, f"{proportion*100:.1f}% ({count}/{total}) of vehicles have delay <20 minutes, which is not a majority."

def stmt_7(df: pd.DataFrame):
    """7. All vehicles with a distance greater than 180 km have a fuel used greater than 30 liters."""
    subset = df[df["distance_km"] > 180]
    if subset.empty:
        return True, "No vehicles with distance >180 km, so the statement holds vacuously."
    condition = subset["fuel_used_l"] > 30
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vehicles with distance >180 km have fuel_used >30 liters."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} vehicles violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a van, then its distance is greater than 100 km."""
    subset = df[df["vehicle_type"] == "van"]
    if subset.empty:
        return True, "No vans in the data, so the statement holds vacuously."
    condition = subset["distance_km"] > 100
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vans have distance >100 km."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} vans violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one vehicle with a delay of less than 5 minutes."""
    subset = df[df["delay_minutes"] < 5]
    truth = not subset.empty
    if truth:
        return True, f"Found {len(subset)} vehicle(s) with delay <5 minutes."
    else:
        return False, "No vehicle with delay <5 minutes found."

def stmt_10(df: pd.DataFrame):
    """10. All buses have a distance greater than 180 km."""
    subset = df[df["vehicle_type"] == "bus"]
    if subset.empty:
        return True, "No buses in the data, so the statement holds vacuously."
    condition = subset["distance_km"] > 180
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} buses have distance >180 km."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} buses violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle is a truck, then its fuel used is greater than 40 liters."""
    subset = df[df["vehicle_type"] == "truck"]
    if subset.empty:
        return True, "No trucks in the data, so the statement holds vacuously."
    condition = subset["fuel_used_l"] > 40
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} trucks have fuel_used >40 liters."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} trucks violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."

def stmt_12(df: pd.DataFrame):
    """12. Most vehicles have an average speed greater than 50 kph."""
    total = len(df)
    count = (df["avg_speed_kph"] > 50).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% ({count}/{total}) of vehicles have avg_speed >50 kph."
    else:
        return False, f"{proportion*100:.1f}% ({count}/{total}) of vehicles have avg_speed >50 kph, which is not a majority."

def stmt_13(df: pd.DataFrame):
    """13. All vehicles with a distance less than 100 km have a fuel used less than 20 liters."""
    subset = df[df["distance_km"] < 100]
    if subset.empty:
        return True, "No vehicles with distance <100 km, so the statement holds vacuously."
    condition = subset["fuel_used_l"] < 20
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vehicles with distance <100 km have fuel_used <20 liters."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} vehicles violate the rule (fuel_used: {', '.join(map(str, viol['fuel_used_l'].tolist()))})."

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a van, then its average speed is greater than 45 kph."""
    subset = df[df["vehicle_type"] == "van"]
    if subset.empty:
        return True, "No vans in the data, so the statement holds vacuously."
    condition = subset["avg_speed_kph"] > 45
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vans have avg_speed >45 kph."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} vans violate the rule (avg_speed: {', '.join(map(str, viol['avg_speed_kph'].tolist()))})."

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one vehicle with an average speed greater than 65 kph."""
    subset = df[df["avg_speed_kph"] > 65]
    truth = not subset.empty
    if truth:
        return True, f"Found {len(subset)} vehicle(s) with avg_speed >65 kph."
    else:
        return False, "No vehicle with avg_speed >65 kph found."

def stmt_16(df: pd.DataFrame):
    """16. All vehicles with a delay greater than 20 minutes have a distance greater than 150 km."""
    subset = df[df["delay_minutes"] > 20]
    if subset.empty:
        return True, "No vehicles with delay >20 minutes, so the statement holds vacuously."
    condition = subset["distance_km"] > 150
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vehicles with delay >20 minutes have distance >150 km."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} vehicles violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."

def stmt_17(df: pd.DataFrame):
    """17. If a vehicle is a bus, then its delay is greater than 10 minutes."""
    subset = df[df["vehicle_type"] == "bus"]
    if subset.empty:
        return True, "No buses in the data, so the statement holds vacuously."
    condition = subset["delay_minutes"] > 10
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} buses have delay >10 minutes."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} buses violate the rule (delay: {', '.join(map(str, viol['delay_minutes'].tolist()))})."

def stmt_18(df: pd.DataFrame):
    """18. Most vehicles have a distance greater than 100 km."""
    total = len(df)
    count = (df["distance_km"] > 100).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% ({count}/{total}) of vehicles have distance >100 km."
    else:
        return False, f"{proportion*100:.1f}% ({count}/{total}) of vehicles have distance >100 km, which is not a majority."

def stmt_19(df: pd.DataFrame):
    """19. All vehicles with a fuel used less than 20 liters have a distance less than 150 km."""
    subset = df[df["fuel_used_l"] < 20]
    if subset.empty:
        return True, "No vehicles with fuel_used <20 liters, so the statement holds vacuously."
    condition = subset["distance_km"] < 150
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} vehicles with fuel_used <20 liters have distance <150 km."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} vehicles violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."

def stmt_20(df: pd.DataFrame):
    """20. If a vehicle is a truck, then its distance is less than 150 km."""
    subset = df[df["vehicle_type"] == "truck"]
    if subset.empty:
        return True, "No trucks in the data, so the statement holds vacuously."
    condition = subset["distance_km"] < 150
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} trucks have distance <150 km."
    else:
        viol = subset[~condition]
        return False, f"{len(viol)} trucks violate the rule (distance: {', '.join(map(str, viol['distance_km'].tolist()))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_73.csv")

    # Convert numeric columns safely.
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
        (20, stmt_20),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()