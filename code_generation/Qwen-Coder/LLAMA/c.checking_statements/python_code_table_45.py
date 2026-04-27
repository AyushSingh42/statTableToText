import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Austin have an average nightly rate greater than $120."""
    austin_hotels = df[df["city"] == "austin"]
    if austin_hotels.empty:
        truth = True
        expl = "No hotels in Austin found."
    else:
        condition = austin_hotels["avg_nightly_rate"] > 120
        truth = condition.all()
        if truth:
            expl = f"All {len(austin_hotels)} Austin hotels have rates > $120."
        else:
            viol = austin_hotels[~condition]
            expl = f"{len(viol)} Austin hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Boston, then its occupancy rate is greater than 69%."""
    boston_hotels = df[df["city"] == "boston"]
    if boston_hotels.empty:
        truth = True
        expl = "No hotels in Boston found."
    else:
        condition = boston_hotels["occupancy_rate"] > 69
        truth = condition.all()
        if truth:
            expl = f"All {len(boston_hotels)} Boston hotels have occupancy > 69%."
        else:
            viol = boston_hotels[~condition]
            expl = f"{len(viol)} Boston hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one hotel in Phoenix with a cancellation rate less than 9%."""
    phoenix_hotels = df[df["city"] == "phoenix"]
    if phoenix_hotels.empty:
        truth = False
        expl = "No hotels in Phoenix found."
    else:
        condition = phoenix_hotels["cancellation_rate"] < 9
        truth = condition.any()
        if truth:
            expl = f"At least one Phoenix hotel has cancellation rate < 9%."
        else:
            expl = f"No Phoenix hotels have cancellation rate < 9%."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with a staff count greater than 35 have a star level of 5."""
    high_staff = df[df["staff_count"] > 35]
    if high_staff.empty:
        truth = True
        expl = "No hotels with staff count > 35 found."
    else:
        condition = high_staff["star_level"] == 5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_staff)} hotels with staff > 35 have star level 5."
        else:
            viol = high_staff[~condition]
            expl = f"{len(viol)} hotels with staff > 35 do not have star level 5 (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel is in Dallas, then its average nightly rate is less than $210."""
    dallas_hotels = df[df["city"] == "dallas"]
    if dallas_hotels.empty:
        truth = True
        expl = "No hotels in Dallas found."
    else:
        condition = dallas_hotels["avg_nightly_rate"] < 210
        truth = condition.all()
        if truth:
            expl = f"All {len(dallas_hotels)} Dallas hotels have rates < $210."
        else:
            viol = dallas_hotels[~condition]
            expl = f"{len(viol)} Dallas hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most hotels have an occupancy rate greater than 70%."""
    condition = df["occupancy_rate"] > 70
    total = len(df)
    satisfied = condition.sum()
    truth = satisfied > total / 2
    if truth:
        expl = f"More than half ({satisfied}/{total}) of hotels have occupancy > 70%."
    else:
        expl = f"Less than half ({satisfied}/{total}) of hotels have occupancy > 70%."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels with a star level of 3 have an average nightly rate less than $185."""
    star3_hotels = df[df["star_level"] == 3]
    if star3_hotels.empty:
        truth = True
        expl = "No hotels with star level 3 found."
    else:
        condition = star3_hotels["avg_nightly_rate"] < 185
        truth = condition.all()
        if truth:
            expl = f"All {len(star3_hotels)} star level 3 hotels have rates < $185."
        else:
            viol = star3_hotels[~condition]
            expl = f"{len(viol)} star level 3 hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel has a bookings month greater than 800, then its cancellation rate is less than 12%."""
    high_bookings = df[df["bookings_month"] > 800]
    if high_bookings.empty:
        truth = True
        expl = "No hotels with bookings month > 800 found."
    else:
        condition = high_bookings["cancellation_rate"] < 12
        truth = condition.all()
        if truth:
            expl = f"All {len(high_bookings)} hotels with bookings > 800 have cancellation rate < 12%."
        else:
            viol = high_bookings[~condition]
            expl = f"{len(viol)} hotels with bookings > 800 violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one hotel in Seattle with a staff count less than 25."""
    seattle_hotels = df[df["city"] == "seattle"]
    if seattle_hotels.empty:
        truth = False
        expl = "No hotels in Seattle found."
    else:
        condition = seattle_hotels["staff_count"] < 25
        truth = condition.any()
        if truth:
            expl = f"At least one Seattle hotel has staff count < 25."
        else:
            expl = f"No Seattle hotels have staff count < 25."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All hotels with an occupancy rate greater than 85% have a star level of 4 or 5."""
    high_occupancy = df[df["occupancy_rate"] > 85]
    if high_occupancy.empty:
        truth = True
        expl = "No hotels with occupancy > 85% found."
    else:
        condition = (high_occupancy["star_level"] == 4) | (high_occupancy["star_level"] == 5)
        truth = condition.all()
        if truth:
            expl = f"All {len(high_occupancy)} hotels with occupancy > 85% have star level 4 or 5."
        else:
            viol = high_occupancy[~condition]
            expl = f"{len(viol)} hotels with occupancy > 85% do not have star level 4 or 5 (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel is in Atlanta, then its average nightly rate is less than $185."""
    atlanta_hotels = df[df["city"] == "atlanta"]
    if atlanta_hotels.empty:
        truth = True
        expl = "No hotels in Atlanta found."
    else:
        condition = atlanta_hotels["avg_nightly_rate"] < 185
        truth = condition.all()
        if truth:
            expl = f"All {len(atlanta_hotels)} Atlanta hotels have rates < $185."
        else:
            viol = atlanta_hotels[~condition]
            expl = f"{len(viol)} Atlanta hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most hotels have a bookings month greater than 700."""
    condition = df["bookings_month"] > 700
    total = len(df)
    satisfied = condition.sum()
    truth = satisfied > total / 2
    if truth:
        expl = f"More than half ({satisfied}/{total}) of hotels have bookings > 700."
    else:
        expl = f"Less than half ({satisfied}/{total}) of hotels have bookings > 700."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All hotels with a star level of 5 have an average nightly rate greater than $138."""
    star5_hotels = df[df["star_level"] == 5]
    if star5_hotels.empty:
        truth = True
        expl = "No hotels with star level 5 found."
    else:
        condition = star5_hotels["avg_nightly_rate"] > 138
        truth = condition.all()
        if truth:
            expl = f"All {len(star5_hotels)} star level 5 hotels have rates > $138."
        else:
            viol = star5_hotels[~condition]
            expl = f"{len(viol)} star level 5 hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel has a cancellation rate less than 10%, then its staff count is less than 38."""
    low_cancellation = df[df["cancellation_rate"] < 10]
    if low_cancellation.empty:
        truth = True
        expl = "No hotels with cancellation rate < 10% found."
    else:
        condition = low_cancellation["staff_count"] < 38
        truth = condition.all()
        if truth:
            expl = f"All {len(low_cancellation)} hotels with cancellation rate < 10% have staff count < 38."
        else:
            viol = low_cancellation[~condition]
            expl = f"{len(viol)} hotels with cancellation rate < 10% violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one hotel in Austin with an occupancy rate greater than 85%."""
    austin_hotels = df[df["city"] == "austin"]
    if austin_hotels.empty:
        truth = False
        expl = "No hotels in Austin found."
    else:
        condition = austin_hotels["occupancy_rate"] > 85
        truth = condition.any()
        if truth:
            expl = f"At least one Austin hotel has occupancy > 85%."
        else:
            expl = f"No Austin hotels have occupancy > 85%."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All hotels with a staff count greater than 40 have an occupancy rate greater than 78%."""
    high_staff = df[df["staff_count"] > 40]
    if high_staff.empty:
        truth = True
        expl = "No hotels with staff count > 40 found."
    else:
        condition = high_staff["occupancy_rate"] > 78
        truth = condition.all()
        if truth:
            expl = f"All {len(high_staff)} hotels with staff > 40 have occupancy > 78%."
        else:
            viol = high_staff[~condition]
            expl = f"{len(viol)} hotels with staff > 40 violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel is in Chicago, then its average nightly rate is greater than $200."""
    chicago_hotels = df[df["city"] == "chicago"]
    if chicago_hotels.empty:
        truth = True
        expl = "No hotels in Chicago found."
    else:
        condition = chicago_hotels["avg_nightly_rate"] > 200
        truth = condition.all()
        if truth:
            expl = f"All {len(chicago_hotels)} Chicago hotels have rates > $200."
        else:
            viol = chicago_hotels[~condition]
            expl = f"{len(viol)} Chicago hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most hotels have an average nightly rate greater than $140."""
    condition = df["avg_nightly_rate"] > 140
    total = len(df)
    satisfied = condition.sum()
    truth = satisfied > total / 2
    if truth:
        expl = f"More than half ({satisfied}/{total}) of hotels have rates > $140."
    else:
        expl = f"Less than half ({satisfied}/{total}) of hotels have rates > $140."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All hotels with a bookings month greater than 850 have a cancellation rate less than 11%."""
    high_bookings = df[df["bookings_month"] > 850]
    if high_bookings.empty:
        truth = True
        expl = "No hotels with bookings month > 850 found."
    else:
        condition = high_bookings["cancellation_rate"] < 11
        truth = condition.all()
        if truth:
            expl = f"All {len(high_bookings)} hotels with bookings > 850 have cancellation rate < 11%."
        else:
            viol = high_bookings[~condition]
            expl = f"{len(viol)} hotels with bookings > 850 violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_45.csv")

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