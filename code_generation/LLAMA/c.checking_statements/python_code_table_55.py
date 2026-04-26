import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Austin have an average nightly rate greater than $150."""
    austin_hotels = df[df["city"] == "austin"]
    condition = austin_hotels["avg_nightly_rate"] > 150
    truth = condition.all()
    if truth:
        expl = f"All {len(austin_hotels)} Austin hotels have nightly rates > $150."
    else:
        viol = austin_hotels[~condition]
        expl = f"{len(viol)} Austin hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Seattle, then its staff count is less than 40."""
    seattle_hotels = df[df["city"] == "seattle"]
    if len(seattle_hotels) == 0:
        return True, "No hotels in Seattle."
    condition = seattle_hotels["staff_count"] < 40
    truth = condition.all()
    if truth:
        expl = f"All {len(seattle_hotels)} Seattle hotels have staff counts < 40."
    else:
        viol = seattle_hotels[~condition]
        expl = f"{len(viol)} Seattle hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one hotel in Dallas with an occupancy rate greater than 85%."""
    dallas_hotels = df[df["city"] == "dallas"]
    condition = dallas_hotels["occupancy_rate"] > 85
    truth = condition.any()
    if truth:
        expl = f"At least one Dallas hotel has occupancy rate > 85%."
    else:
        expl = f"No Dallas hotels have occupancy rate > 85%."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with a star level of 5 have an average nightly rate greater than $200."""
    five_star_hotels = df[df["star_level"] == 5]
    if len(five_star_hotels) == 0:
        return True, "No 5-star hotels."
    condition = five_star_hotels["avg_nightly_rate"] > 200
    truth = condition.all()
    if truth:
        expl = f"All {len(five_star_hotels)} 5-star hotels have nightly rates > $200."
    else:
        viol = five_star_hotels[~condition]
        expl = f"{len(viol)} 5-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel has a cancellation rate less than 10%, then its occupancy rate is greater than 70%."""
    filtered = df[df["cancellation_rate"] < 10]
    if len(filtered) == 0:
        return True, "No hotels with cancellation rate < 10%."
    condition = filtered["occupancy_rate"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} hotels with cancellation rate < 10% have occupancy rate > 70%."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} hotels with cancellation rate < 10% violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most hotels in the dataset have a staff count greater than 30."""
    condition = df["staff_count"] > 30
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of hotels have staff count > 30."
    else:
        expl = f"Less than half ({count}/{total}) of hotels have staff count > 30."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels in Boston have a star level of either 3 or 5."""
    boston_hotels = df[df["city"] == "boston"]
    if len(boston_hotels) == 0:
        return True, "No hotels in Boston."
    condition = (boston_hotels["star_level"] == 3) | (boston_hotels["star_level"] == 5)
    truth = condition.all()
    if truth:
        expl = f"All {len(boston_hotels)} Boston hotels have star level 3 or 5."
    else:
        viol = boston_hotels[~condition]
        expl = f"{len(viol)} Boston hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Miami, then its occupancy rate is less than 70%."""
    miami_hotels = df[df["city"] == "miami"]
    if len(miami_hotels) == 0:
        return True, "No hotels in Miami."
    condition = miami_hotels["occupancy_rate"] < 70
    truth = condition.all()
    if truth:
        expl = f"All {len(miami_hotels)} Miami hotels have occupancy rate < 70%."
    else:
        viol = miami_hotels[~condition]
        expl = f"{len(viol)} Miami hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one hotel in Austin with a bookings per month count greater than 800."""
    austin_hotels = df[df["city"] == "austin"]
    condition = austin_hotels["bookings_month"] > 800
    truth = condition.any()
    if truth:
        expl = f"At least one Austin hotel has bookings/month > 800."
    else:
        expl = f"No Austin hotels have bookings/month > 800."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All hotels with a star level of 4 have an average nightly rate greater than $180."""
    four_star_hotels = df[df["star_level"] == 4]
    if len(four_star_hotels) == 0:
        return True, "No 4-star hotels."
    condition = four_star_hotels["avg_nightly_rate"] > 180
    truth = condition.all()
    if truth:
        expl = f"All {len(four_star_hotels)} 4-star hotels have nightly rates > $180."
    else:
        viol = four_star_hotels[~condition]
        expl = f"{len(viol)} 4-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel has an occupancy rate greater than 80%, then its cancellation rate is less than 12%."""
    filtered = df[df["occupancy_rate"] > 80]
    if len(filtered) == 0:
        return True, "No hotels with occupancy rate > 80%."
    condition = filtered["cancellation_rate"] < 12
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} hotels with occupancy rate > 80% have cancellation rate < 12%."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} hotels with occupancy rate > 80% violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels in Dallas have an average nightly rate greater than $170."""
    dallas_hotels = df[df["city"] == "dallas"]
    if len(dallas_hotels) == 0:
        return True, "No hotels in Dallas."
    condition = dallas_hotels["avg_nightly_rate"] > 170
    truth = condition.all()
    if truth:
        expl = f"All {len(dallas_hotels)} Dallas hotels have nightly rates > $170."
    else:
        viol = dallas_hotels[~condition]
        expl = f"{len(viol)} Dallas hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. There exists at least one hotel in Seattle with a staff count greater than 40."""
    seattle_hotels = df[df["city"] == "seattle"]
    condition = seattle_hotels["staff_count"] > 40
    truth = condition.any()
    if truth:
        expl = f"At least one Seattle hotel has staff count > 40."
    else:
        expl = f"No Seattle hotels have staff count > 40."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel has a star level of 3, then its average nightly rate is less than $220."""
    three_star_hotels = df[df["star_level"] == 3]
    if len(three_star_hotels) == 0:
        return True, "No 3-star hotels."
    condition = three_star_hotels["avg_nightly_rate"] < 220
    truth = condition.all()
    if truth:
        expl = f"All {len(three_star_hotels)} 3-star hotels have nightly rates < $220."
    else:
        viol = three_star_hotels[~condition]
        expl = f"{len(viol)} 3-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most hotels in the dataset have an occupancy rate greater than 70%."""
    condition = df["occupancy_rate"] > 70
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of hotels have occupancy rate > 70%."
    else:
        expl = f"Less than half ({count}/{total}) of hotels have occupancy rate > 70%."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All hotels with a bookings per month count greater than 700 have a staff count greater than 25."""
    filtered = df[df["bookings_month"] > 700]
    if len(filtered) == 0:
        return True, "No hotels with bookings/month > 700."
    condition = filtered["staff_count"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} hotels with bookings/month > 700 have staff count > 25."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} hotels with bookings/month > 700 violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel is in Austin, then its star level is either 3, 4, or 5."""
    austin_hotels = df[df["city"] == "austin"]
    if len(austin_hotels) == 0:
        return True, "No hotels in Austin."
    condition = (austin_hotels["star_level"] == 3) | (austin_hotels["star_level"] == 4) | (austin_hotels["star_level"] == 5)
    truth = condition.all()
    if truth:
        expl = f"All {len(austin_hotels)} Austin hotels have star level 3, 4, or 5."
    else:
        viol = austin_hotels[~condition]
        expl = f"{len(viol)} Austin hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_55.csv")

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