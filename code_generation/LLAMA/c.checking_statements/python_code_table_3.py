import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All vehicles with a distance greater than 200 km have an average speed less than 60 kph."""
    condition = (df["distance_km"] > 200) & (df["avg_speed_kph"] >= 60)
    truth = not condition.any()
    if truth:
        expl = "No vehicles with distance > 200 km have avg speed >= 60 kph."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (distance > 200 km and avg speed >= 60 kph)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a vehicle is a bus, then its fuel used is greater than 30 liters."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["fuel_used_l"] <= 30
    truth = not condition.any()
    if truth:
        expl = "All buses have fuel used > 30 liters."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} buses violate the rule (fuel used <= 30 liters)."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one truck with a delay of less than 15 minutes."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["delay_minutes"] < 15
    truth = condition.any()
    if truth:
        expl = "At least one truck has delay < 15 minutes."
    else:
        expl = "No trucks have delay < 15 minutes."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All vans with a distance less than 100 km have an average speed greater than 60 kph."""
    vans = df[df["vehicle_type"] == "van"]
    condition = (vans["distance_km"] < 100) & (vans["avg_speed_kph"] <= 60)
    truth = not condition.any()
    if truth:
        expl = "All vans with distance < 100 km have avg speed > 60 kph."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} vans violate the rule (distance < 100 km and avg speed <= 60 kph)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a vehicle is a truck, then its average speed is less than 62 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"] >= 62
    truth = not condition.any()
    if truth:
        expl = "All trucks have avg speed < 62 kph."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} trucks violate the rule (avg speed >= 62 kph)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most vehicles have a delay of less than 20 minutes."""
    total = len(df)
    condition = df["delay_minutes"] >= 20
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"Less than half ({count}/{total}) of vehicles have delay >= 20 minutes."
    else:
        expl = f"Half or more ({count}/{total}) of vehicles have delay >= 20 minutes."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All buses with a distance greater than 150 km have a fuel used greater than 40 liters."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = (buses["distance_km"] > 150) & (buses["fuel_used_l"] <= 40)
    truth = not condition.any()
    if truth:
        expl = "All buses with distance > 150 km have fuel used > 40 liters."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} buses violate the rule (distance > 150 km and fuel used <= 40 liters)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a vehicle is a van, then its fuel used is less than 50 liters."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["fuel_used_l"] >= 50
    truth = not condition.any()
    if truth:
        expl = "All vans have fuel used < 50 liters."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} vans violate the rule (fuel used >= 50 liters)."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one bus with a delay of less than 10 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["delay_minutes"] < 10
    truth = condition.any()
    if truth:
        expl = "At least one bus has delay < 10 minutes."
    else:
        expl = "No buses have delay < 10 minutes."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All vehicles with a distance less than 150 km have an average speed greater than 50 kph."""
    condition = (df["distance_km"] < 150) & (df["avg_speed_kph"] <= 50)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with distance < 150 km have avg speed > 50 kph."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (distance < 150 km and avg speed <= 50 kph)."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a vehicle is a truck, then its distance is greater than 150 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["distance_km"] <= 150
    truth = not condition.any()
    if truth:
        expl = "All trucks have distance > 150 km."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} trucks violate the rule (distance <= 150 km)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most vehicles have an average speed greater than 55 kph."""
    total = len(df)
    condition = df["avg_speed_kph"] <= 55
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"Less than half ({count}/{total}) of vehicles have avg speed <= 55 kph."
    else:
        expl = f"Half or more ({count}/{total}) of vehicles have avg speed <= 55 kph."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All vans with a distance greater than 200 km have an average speed greater than 60 kph."""
    vans = df[df["vehicle_type"] == "van"]
    condition = (vans["distance_km"] > 200) & (vans["avg_speed_kph"] <= 60)
    truth = not condition.any()
    if truth:
        expl = "All vans with distance > 200 km have avg speed > 60 kph."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} vans violate the rule (distance > 200 km and avg speed <= 60 kph)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a vehicle is a bus, then its distance is greater than 100 km."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["distance_km"] <= 100
    truth = not condition.any()
    if truth:
        expl = "All buses have distance > 100 km."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} buses violate the rule (distance <= 100 km)."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one van with a delay of greater than 25 minutes."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["delay_minutes"] > 25
    truth = condition.any()
    if truth:
        expl = "At least one van has delay > 25 minutes."
    else:
        expl = "No vans have delay > 25 minutes."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All vehicles with a fuel used greater than 40 liters have a distance greater than 150 km."""
    condition = (df["fuel_used_l"] > 40) & (df["distance_km"] <= 150)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with fuel used > 40 liters have distance > 150 km."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (fuel used > 40 liters and distance <= 150 km)."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a vehicle is a truck, then its fuel used is greater than 30 liters."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["fuel_used_l"] <= 30
    truth = not condition.any()
    if truth:
        expl = "All trucks have fuel used > 30 liters."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} trucks violate the rule (fuel used <= 30 liters)."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most vehicles have a fuel used less than 50 liters."""
    total = len(df)
    condition = df["fuel_used_l"] >= 50
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"Less than half ({count}/{total}) of vehicles have fuel used >= 50 liters."
    else:
        expl = f"Half or more ({count}/{total}) of vehicles have fuel used >= 50 liters."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All buses with a distance less than 150 km have an average speed greater than 60 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = (buses["distance_km"] < 150) & (buses["avg_speed_kph"] <= 60)
    truth = not condition.any()
    if truth:
        expl = "All buses with distance < 150 km have avg speed > 60 kph."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} buses violate the rule (distance < 150 km and avg speed <= 60 kph)."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a vehicle is a van, then its distance is less than 250 km."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["distance_km"] >= 250
    truth = not condition.any()
    if truth:
        expl = "All vans have distance < 250 km."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} vans violate the rule (distance >= 250 km)."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one truck with a fuel used less than 40 liters."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["fuel_used_l"] < 40
    truth = condition.any()
    if truth:
        expl = "At least one truck has fuel used < 40 liters."
    else:
        expl = "No trucks have fuel used < 40 liters."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. All vehicles with an average speed greater than 60 kph have a distance less than 250 km."""
    condition = (df["avg_speed_kph"] > 60) & (df["distance_km"] >= 250)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with avg speed > 60 kph have distance < 250 km."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (avg speed > 60 kph and distance >= 250 km)."
    return truth, expl

def stmt_23(df: pd.DataFrame):
    """23. If a vehicle is a bus, then its average speed is less than 65 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["avg_speed_kph"] >= 65
    truth = not condition.any()
    if truth:
        expl = "All buses have avg speed < 65 kph."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} buses violate the rule (avg speed >= 65 kph)."
    return truth, expl

def stmt_24(df: pd.DataFrame):
    """24. Most vehicles have a distance greater than 100 km."""
    total = len(df)
    condition = df["distance_km"] <= 100
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"Less than half ({count}/{total}) of vehicles have distance <= 100 km."
    else:
        expl = f"Half or more ({count}/{total}) of vehicles have distance <= 100 km."
    return truth, expl

def stmt_25(df: pd.DataFrame):
    """25. All vans with a fuel used less than 20 liters have a distance greater than 200 km."""
    vans = df[df["vehicle_type"] == "van"]
    condition = (vans["fuel_used_l"] < 20) & (vans["distance_km"] <= 200)
    truth = not condition.any()
    if truth:
        expl = "All vans with fuel used < 20 liters have distance > 200 km."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} vans violate the rule (fuel used < 20 liters and distance <= 200 km)."
    return truth, expl

def stmt_26(df: pd.DataFrame):
    """26. If a vehicle is a truck, then its delay is greater than 10 minutes."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["delay_minutes"] <= 10
    truth = not condition.any()
    if truth:
        expl = "All trucks have delay > 10 minutes."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} trucks violate the rule (delay <= 10 minutes)."
    return truth, expl

def stmt_27(df: pd.DataFrame):
    """27. There exists at least one bus with a fuel used greater than 45 liters."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["fuel_used_l"] > 45
    truth = condition.any()
    if truth:
        expl = "At least one bus has fuel used > 45 liters."
    else:
        expl = "No buses have fuel used > 45 liters."
    return truth, expl

def stmt_28(df: pd.DataFrame):
    """28. All vehicles with a distance greater than 200 km have a fuel used less than 50 liters."""
    condition = (df["distance_km"] > 200) & (df["fuel_used_l"] >= 50)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with distance > 200 km have fuel used < 50 liters."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (distance > 200 km and fuel used >= 50 liters)."
    return truth, expl

def stmt_29(df: pd.DataFrame):
    """29. If a vehicle is a van, then its average speed is greater than 50 kph."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["avg_speed_kph"] <= 50
    truth = not condition.any()
    if truth:
        expl = "All vans have avg speed > 50 kph."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} vans violate the rule (avg speed <= 50 kph)."
    return truth, expl

def stmt_30(df: pd.DataFrame):
    """30. Most vehicles have a delay less than 25 minutes."""
    total = len(df)
    condition = df["delay_minutes"] >= 25
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"Less than half ({count}/{total}) of vehicles have delay >= 25 minutes."
    else:
        expl = f"Half or more ({count}/{total}) of vehicles have delay >= 25 minutes."
    return truth, expl

def stmt_31(df: pd.DataFrame):
    """31. All buses with an average speed less than 60 kph have a distance greater than 200 km."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = (buses["avg_speed_kph"] < 60) & (buses["distance_km"] <= 200)
    truth = not condition.any()
    if truth:
        expl = "All buses with avg speed < 60 kph have distance > 200 km."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} buses violate the rule (avg speed < 60 kph and distance <= 200 km)."
    return truth, expl

def stmt_32(df: pd.DataFrame):
    """32. If a vehicle is a truck, then its distance is less than 250 km."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["distance_km"] >= 250
    truth = not condition.any()
    if truth:
        expl = "All trucks have distance < 250 km."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} trucks violate the rule (distance >= 250 km)."
    return truth, expl

def stmt_33(df: pd.DataFrame):
    """33. There exists at least one van with a fuel used greater than 40 liters."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["fuel_used_l"] > 40
    truth = condition.any()
    if truth:
        expl = "At least one van has fuel used > 40 liters."
    else:
        expl = "No vans have fuel used > 40 liters."
    return truth, expl

def stmt_34(df: pd.DataFrame):
    """34. All vehicles with a fuel used less than 30 liters have a distance less than 200 km."""
    condition = (df["fuel_used_l"] < 30) & (df["distance_km"] >= 200)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with fuel used < 30 liters have distance < 200 km."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (fuel used < 30 liters and distance >= 200 km)."
    return truth, expl

def stmt_35(df: pd.DataFrame):
    """35. If a vehicle is a bus, then its delay is less than 25 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["delay_minutes"] >= 25
    truth = not condition.any()
    if truth:
        expl = "All buses have delay < 25 minutes."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} buses violate the rule (delay >= 25 minutes)."
    return truth, expl

def stmt_36(df: pd.DataFrame):
    """36. Most vehicles have an average speed less than 65 kph."""
    total = len(df)
    condition = df["avg_speed_kph"] >= 65
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"Less than half ({count}/{total}) of vehicles have avg speed >= 65 kph."
    else:
        expl = f"Half or more ({count}/{total}) of vehicles have avg speed >= 65 kph."
    return truth, expl

def stmt_37(df: pd.DataFrame):
    """37. All vans with a distance greater than 150 km have a fuel used less than 50 liters."""
    vans = df[df["vehicle_type"] == "van"]
    condition = (vans["distance_km"] > 150) & (vans["fuel_used_l"] >= 50)
    truth = not condition.any()
    if truth:
        expl = "All vans with distance > 150 km have fuel used < 50 liters."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} vans violate the rule (distance > 150 km and fuel used >= 50 liters)."
    return truth, expl

def stmt_38(df: pd.DataFrame):
    """38. If a vehicle is a truck, then its average speed is greater than 50 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"] <= 50
    truth = not condition.any()
    if truth:
        expl = "All trucks have avg speed > 50 kph."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} trucks violate the rule (avg speed <= 50 kph)."
    return truth, expl

def stmt_39(df: pd.DataFrame):
    """39. There exists at least one bus with a distance less than 150 km."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["distance_km"] < 150
    truth = condition.any()
    if truth:
        expl = "At least one bus has distance < 150 km."
    else:
        expl = "No buses have distance < 150 km."
    return truth, expl

def stmt_40(df: pd.DataFrame):
    """40. All vehicles with an average speed greater than 55 kph have a fuel used less than 50 liters."""
    condition = (df["avg_speed_kph"] > 55) & (df["fuel_used_l"] >= 50)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with avg speed > 55 kph have fuel used < 50 liters."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (avg speed > 55 kph and fuel used >= 50 liters)."
    return truth, expl

def stmt_41(df: pd.DataFrame):
    """41. If a vehicle is a van, then its delay is greater than 15 minutes."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["delay_minutes"] <= 15
    truth = not condition.any()
    if truth:
        expl = "All vans have delay > 15 minutes."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} vans violate the rule (delay <= 15 minutes)."
    return truth, expl

def stmt_42(df: pd.DataFrame):
    """42. Most vehicles have a distance less than 250 km."""
    total = len(df)
    condition = df["distance_km"] >= 250
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"Less than half ({count}/{total}) of vehicles have distance >= 250 km."
    else:
        expl = f"Half or more ({count}/{total}) of vehicles have distance >= 250 km."
    return truth, expl

def stmt_43(df: pd.DataFrame):
    """43. All buses with a fuel used greater than 40 liters have an average speed less than 65 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = (buses["fuel_used_l"] > 40) & (buses["avg_speed_kph"] >= 65)
    truth = not condition.any()
    if truth:
        expl = "All buses with fuel used > 40 liters have avg speed < 65 kph."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} buses violate the rule (fuel used > 40 liters and avg speed >= 65 kph)."
    return truth, expl

def stmt_44(df: pd.DataFrame):
    """44. If a vehicle is a truck, then its fuel used is less than 50 liters."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["fuel_used_l"] >= 50
    truth = not condition.any()
    if truth:
        expl = "All trucks have fuel used < 50 liters."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} trucks violate the rule (fuel used >= 50 liters)."
    return truth, expl

def stmt_45(df: pd.DataFrame):
    """45. There exists at least one van with an average speed less than 60 kph."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["avg_speed_kph"] < 60
    truth = condition.any()
    if truth:
        expl = "At least one van has avg speed < 60 kph."
    else:
        expl = "No vans have avg speed < 60 kph."
    return truth, expl

def stmt_46(df: pd.DataFrame):
    """46. All vehicles with a distance less than 200 km have a fuel used less than 50 liters."""
    condition = (df["distance_km"] < 200) & (df["fuel_used_l"] >= 50)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with distance < 200 km have fuel used < 50 liters."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (distance < 200 km and fuel used >= 50 liters)."
    return truth, expl

def stmt_47(df: pd.DataFrame):
    """47. If a vehicle is a bus, then its average speed is greater than 50 kph."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["avg_speed_kph"] <= 50
    truth = not condition.any()
    if truth:
        expl = "All buses have avg speed > 50 kph."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} buses violate the rule (avg speed <= 50 kph)."
    return truth, expl

def stmt_48(df: pd.DataFrame):
    """48. Most vehicles have a fuel used greater than 20 liters."""
    total = len(df)
    condition = df["fuel_used_l"] <= 20
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"Less than half ({count}/{total}) of vehicles have fuel used <= 20 liters."
    else:
        expl = f"Half or more ({count}/{total}) of vehicles have fuel used <= 20 liters."
    return truth, expl

def stmt_49(df: pd.DataFrame):
    """49. All vans with an average speed greater than 60 kph have a distance greater than 100 km."""
    vans = df[df["vehicle_type"] == "van"]
    condition = (vans["avg_speed_kph"] > 60) & (vans["distance_km"] <= 100)
    truth = not condition.any()
    if truth:
        expl = "All vans with avg speed > 60 kph have distance > 100 km."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} vans violate the rule (avg speed > 60 kph and distance <= 100 km)."
    return truth, expl

def stmt_50(df: pd.DataFrame):
    """50. If a vehicle is a truck, then its delay is less than 30 minutes."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["delay_minutes"] >= 30
    truth = not condition.any()
    if truth:
        expl = "All trucks have delay < 30 minutes."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} trucks violate the rule (delay >= 30 minutes)."
    return truth, expl

def stmt_51(df: pd.DataFrame):
    """51. There exists at least one bus with a fuel used less than 40 liters."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["fuel_used_l"] < 40
    truth = condition.any()
    if truth:
        expl = "At least one bus has fuel used < 40 liters."
    else:
        expl = "No buses have fuel used < 40 liters."
    return truth, expl

def stmt_52(df: pd.DataFrame):
    """52. All vehicles with a fuel used greater than 30 liters have a distance greater than 100 km."""
    condition = (df["fuel_used_l"] > 30) & (df["distance_km"] <= 100)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with fuel used > 30 liters have distance > 100 km."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (fuel used > 30 liters and distance <= 100 km)."
    return truth, expl

def stmt_53(df: pd.DataFrame):
    """53. If a vehicle is a van, then its distance is greater than 50 km."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["distance_km"] <= 50
    truth = not condition.any()
    if truth:
        expl = "All vans have distance > 50 km."
    else:
        viol = vans[condition]
        expl = f"{len(viol)} vans violate the rule (distance <= 50 km)."
    return truth, expl

def stmt_54(df: pd.DataFrame):
    """54. Most vehicles have an average speed greater than 50 kph."""
    total = len(df)
    condition = df["avg_speed_kph"] <= 50
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl = f"Less than half ({count}/{total}) of vehicles have avg speed <= 50 kph."
    else:
        expl = f"Half or more ({count}/{total}) of vehicles have avg speed <= 50 kph."
    return truth, expl

def stmt_55(df: pd.DataFrame):
    """55. All buses with a distance greater than 200 km have a delay less than 25 minutes."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = (buses["distance_km"] > 200) & (buses["delay_minutes"] >= 25)
    truth = not condition.any()
    if truth:
        expl = "All buses with distance > 200 km have delay < 25 minutes."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} buses violate the rule (distance > 200 km and delay >= 25 minutes)."
    return truth, expl

def stmt_56(df: pd.DataFrame):
    """56. If a vehicle is a truck, then its average speed is less than 65 kph."""
    trucks = df[df["vehicle_type"] == "truck"]
    condition = trucks["avg_speed_kph"] >= 65
    truth = not condition.any()
    if truth:
        expl = "All trucks have avg speed < 65 kph."
    else:
        viol = trucks[condition]
        expl = f"{len(viol)} trucks violate the rule (avg speed >= 65 kph)."
    return truth, expl

def stmt_57(df: pd.DataFrame):
    """57. There exists at least one van with a fuel used greater than 30 liters."""
    vans = df[df["vehicle_type"] == "van"]
    condition = vans["fuel_used_l"] > 30
    truth = condition.any()
    if truth:
        expl = "At least one van has fuel used > 30 liters."
    else:
        expl = "No vans have fuel used > 30 liters."
    return truth, expl

def stmt_58(df: pd.DataFrame):
    """58. All vehicles with an average speed less than 60 kph have a fuel used greater than 20 liters."""
    condition = (df["avg_speed_kph"] < 60) & (df["fuel_used_l"] <= 20)
    truth = not condition.any()
    if truth:
        expl = "All vehicles with avg speed < 60 kph have fuel used > 20 liters."
    else:
        viol = df[condition]
        expl = f"{len(viol)} vehicles violate the rule (avg speed < 60 kph and fuel used <= 20 liters)."
    return truth, expl

def stmt_59(df: pd.DataFrame):
    """59. If a vehicle is a bus, then its distance is less than 300 km."""
    buses = df[df["vehicle_type"] == "bus"]
    condition = buses["distance_km"] >= 300
    truth = not condition.any()
    if truth:
        expl = "All buses have distance < 300 km."
    else:
        viol = buses[condition]
        expl = f"{len(viol)} buses violate the rule (distance >= 300 km)."
    return truth, expl

def stmt_60(df: pd.DataFrame):
    """60. Most vehicles have a delay greater than 10 minutes."""
    total = len(df)
    condition = df["delay_minutes"] <= 10
    count = condition.sum()
    truth = count < total / 2
    if truth:
        expl