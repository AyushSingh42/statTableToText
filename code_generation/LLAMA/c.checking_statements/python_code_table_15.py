import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Atlanta have an average nightly rate greater than $110."""
    atlanta_hotels = df[df["city"] == "atlanta"]
    if atlanta_hotels.empty:
        truth = True
        expl = "No hotels in Atlanta found, so vacuously true."
    else:
        condition = atlanta_hotels["avg_nightly_rate"] > 110
        truth = condition.all()
        if truth:
            expl = f"All {len(atlanta_hotels)} Atlanta hotels have rates > $110."
        else:
            viol = atlanta_hotels[~condition]
            expl = f"{len(viol)} Atlanta hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Seattle, then its occupancy rate is greater than 78%."""
    seattle_hotels = df[df["city"] == "seattle"]
    if seattle_hotels.empty:
        truth = True
        expl = "No hotels in Seattle found, so vacuously true."
    else:
        condition = seattle_hotels["occupancy_rate"] > 78
        truth = condition.all()
        if truth:
            expl = f"All {len(seattle_hotels)} Seattle hotels have occupancy > 78%."
        else:
            viol = seattle_hotels[~condition]
            expl = f"{len(viol)} Seattle hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hotels with a star level of 5 have an occupancy rate greater than 72%."""
    five_star_hotels = df[df["star_level"] == 5]
    if five_star_hotels.empty:
        truth = True
        expl = "No 5-star hotels found, so vacuously true."
    else:
        condition = five_star_hotels["occupancy_rate"] > 72
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star_hotels)} 5-star hotels have occupancy > 72%."
        else:
            viol = five_star_hotels[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one hotel in Dallas with an occupancy rate less than 85%."""
    dallas_hotels = df[df["city"] == "dallas"]
    if dallas_hotels.empty:
        truth = False
        expl = "No hotels in Dallas found."
    else:
        condition = dallas_hotels["occupancy_rate"] < 85
        truth = condition.any()
        if truth:
            viol = dallas_hotels[condition]
            expl = f"At least one Dallas hotel ({len(viol)} out of {len(dallas_hotels)}) has occupancy < 85%."
        else:
            expl = f"All {len(dallas_hotels)} Dallas hotels have occupancy >= 85%."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel has a staff count greater than 40, then its occupancy rate is greater than 83%."""
    high_staff_hotels = df[df["staff_count"] > 40]
    if high_staff_hotels.empty:
        truth = True
        expl = "No hotels with staff > 40 found, so vacuously true."
    else:
        condition = high_staff_hotels["occupancy_rate"] > 83
        truth = condition.all()
        if truth:
            expl = f"All {len(high_staff_hotels)} hotels with staff > 40 have occupancy > 83%."
        else:
            viol = high_staff_hotels[~condition]
            expl = f"{len(viol)} hotels with staff > 40 violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with a cancellation rate greater than 14% have a star level less than 5."""
    high_cancel_hotels = df[df["cancellation_rate"] > 14]
    if high_cancel_hotels.empty:
        truth = True
        expl = "No hotels with cancellation rate > 14% found, so vacuously true."
    else:
        condition = high_cancel_hotels["star_level"] < 5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_cancel_hotels)} hotels with cancellation rate > 14% have star level < 5."
        else:
            viol = high_cancel_hotels[~condition]
            expl = f"{len(viol)} hotels with cancellation rate > 14% violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a hotel is in Portland, then its average nightly rate is less than $225."""
    portland_hotels = df[df["city"] == "portland"]
    if portland_hotels.empty:
        truth = True
        expl = "No hotels in Portland found, so vacuously true."
    else:
        condition = portland_hotels["avg_nightly_rate"] < 225
        truth = condition.all()
        if truth:
            expl = f"All {len(portland_hotels)} Portland hotels have rates < $225."
        else:
            viol = portland_hotels[~condition]
            expl = f"{len(viol)} Portland hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most hotels in the dataset have an occupancy rate greater than 70%."""
    condition = df["occupancy_rate"] > 70
    total = len(df)
    satisfied = condition.sum()
    truth = satisfied > total / 2
    expl = f"{satisfied} out of {total} hotels have occupancy > 70%. {'Most' if truth else 'Not most'}."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All hotels with a bookings month greater than 800 have an occupancy rate greater than 75%."""
    high_bookings_hotels = df[df["bookings_month"] > 800]
    if high_bookings_hotels.empty:
        truth = True
        expl = "No hotels with bookings_month > 800 found, so vacuously true."
    else:
        condition = high_bookings_hotels["occupancy_rate"] > 75
        truth = condition.all()
        if truth:
            expl = f"All {len(high_bookings_hotels)} hotels with bookings_month > 800 have occupancy > 75%."
        else:
            viol = high_bookings_hotels[~condition]
            expl = f"{len(viol)} hotels with bookings_month > 800 violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a hotel has a star level of 4, then its average nightly rate is less than $215."""
    four_star_hotels = df[df["star_level"] == 4]
    if four_star_hotels.empty:
        truth = True
        expl = "No 4-star hotels found, so vacuously true."
    else:
        condition = four_star_hotels["avg_nightly_rate"] < 215
        truth = condition.all()
        if truth:
            expl = f"All {len(four_star_hotels)} 4-star hotels have rates < $215."
        else:
            viol = four_star_hotels[~condition]
            expl = f"{len(viol)} 4-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. There exists at least one hotel in Chicago with a staff count greater than 45."""
    chicago_hotels = df[df["city"] == "chicago"]
    if chicago_hotels.empty:
        truth = False
        expl = "No hotels in Chicago found."
    else:
        condition = chicago_hotels["staff_count"] > 45
        truth = condition.any()
        if truth:
            viol = chicago_hotels[condition]
            expl = f"At least one Chicago hotel ({len(viol)} out of {len(chicago_hotels)}) has staff > 45."
        else:
            expl = f"All {len(chicago_hotels)} Chicago hotels have staff <= 45."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels with an occupancy rate greater than 85% have a star level greater than 3."""
    high_occupancy_hotels = df[df["occupancy_rate"] > 85]
    if high_occupancy_hotels.empty:
        truth = True
        expl = "No hotels with occupancy > 85% found, so vacuously true."
    else:
        condition = high_occupancy_hotels["star_level"] > 3
        truth = condition.all()
        if truth:
            expl = f"All {len(high_occupancy_hotels)} hotels with occupancy > 85% have star level > 3."
        else:
            viol = high_occupancy_hotels[~condition]
            expl = f"{len(viol)} hotels with occupancy > 85% violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a hotel is in Miami, then its occupancy rate is greater than 80%."""
    miami_hotels = df[df["city"] == "miami"]
    if miami_hotels.empty:
        truth = True
        expl = "No hotels in Miami found, so vacuously true."
    else:
        condition = miami_hotels["occupancy_rate"] > 80
        truth = condition.all()
        if truth:
            expl = f"All {len(miami_hotels)} Miami hotels have occupancy > 80%."
        else:
            viol = miami_hotels[~condition]
            expl = f"{len(viol)} Miami hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All hotels with a cancellation rate less than 10% have a staff count less than 30."""
    low_cancel_hotels = df[df["cancellation_rate"] < 10]
    if low_cancel_hotels.empty:
        truth = True
        expl = "No hotels with cancellation rate < 10% found, so vacuously true."
    else:
        condition = low_cancel_hotels["staff_count"] < 30
        truth = condition.all()
        if truth:
            expl = f"All {len(low_cancel_hotels)} hotels with cancellation rate < 10% have staff < 30."
        else:
            viol = low_cancel_hotels[~condition]
            expl = f"{len(viol)} hotels with cancellation rate < 10% violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most hotels in the dataset have a staff count less than 40."""
    condition = df["staff_count"] < 40
    total = len(df)
    satisfied = condition.sum()
    truth = satisfied > total / 2
    expl = f"{satisfied} out of {total} hotels have staff < 40. {'Most' if truth else 'Not most'}."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a hotel has an average nightly rate greater than $200, then its star level is greater than 3."""
    high_rate_hotels = df[df["avg_nightly_rate"] > 200]
    if high_rate_hotels.empty:
        truth = True
        expl = "No hotels with rate > $200 found, so vacuously true."
    else:
        condition = high_rate_hotels["star_level"] > 3
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rate_hotels)} hotels with rate > $200 have star level > 3."
        else:
            viol = high_rate_hotels[~condition]
            expl = f"{len(viol)} hotels with rate > $200 violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. There exists at least one hotel in Boston with an occupancy rate greater than 80%."""
    boston_hotels = df[df["city"] == "boston"]
    if boston_hotels.empty:
        truth = False
        expl = "No hotels in Boston found."
    else:
        condition = boston_hotels["occupancy_rate"] > 80
        truth = condition.any()
        if truth:
            viol = boston_hotels[condition]
            expl = f"At least one Boston hotel ({len(viol)} out of {len(boston_hotels)}) has occupancy > 80%."
        else:
            expl = f"All {len(boston_hotels)} Boston hotels have occupancy <= 80%."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All hotels with a bookings month less than 700 have a star level less than 5."""
    low_bookings_hotels = df[df["bookings_month"] < 700]
    if low_bookings_hotels.empty:
        truth = True
        expl = "No hotels with bookings_month < 700 found, so vacuously true."
    else:
        condition = low_bookings_hotels["star_level"] < 5
        truth = condition.all()
        if truth:
            expl = f"All {len(low_bookings_hotels)} hotels with bookings_month < 700 have star level < 5."
        else:
            viol = low_bookings_hotels[~condition]
            expl = f"{len(viol)} hotels with bookings_month < 700 violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. If a hotel has a staff count less than 25, then its occupancy rate is less than 85%."""
    low_staff_hotels = df[df["staff_count"] < 25]
    if low_staff_hotels.empty:
        truth = True
        expl = "No hotels with staff < 25 found, so vacuously true."
    else:
        condition = low_staff_hotels["occupancy_rate"] < 85
        truth = condition.all()
        if truth:
            expl = f"All {len(low_staff_hotels)} hotels with staff < 25 have occupancy < 85%."
        else:
            viol = low_staff_hotels[~condition]
            expl = f"{len(viol)} hotels with staff < 25 violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_15.csv")

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
        (19, stmt_19)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()