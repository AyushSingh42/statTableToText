import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Denver have an occupancy rate greater than 70%."""
    denver_hotels = df[df["city"] == "denver"]
    if len(denver_hotels) == 0:
        truth = True
        expl = "No hotels in Denver found."
    else:
        condition = denver_hotels["occupancy_rate"] > 70
        truth = condition.all()
        if truth:
            expl = f"All {len(denver_hotels)} Denver hotels have occupancy > 70%."
        else:
            viol = denver_hotels[~condition]
            expl = f"{len(viol)} Denver hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Seattle, then its staff count is less than 35."""
    seattle_hotels = df[df["city"] == "seattle"]
    if len(seattle_hotels) == 0:
        truth = True
        expl = "No hotels in Seattle found."
    else:
        condition = seattle_hotels["staff_count"] < 35
        truth = condition.all()
        if truth:
            expl = f"All {len(seattle_hotels)} Seattle hotels have staff < 35."
        else:
            viol = seattle_hotels[~condition]
            expl = f"{len(viol)} Seattle hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hotels with an average nightly rate greater than $200 have a star level of 4."""
    high_rate_hotels = df[df["avg_nightly_rate"] > 200]
    if len(high_rate_hotels) == 0:
        truth = True
        expl = "No hotels with avg nightly rate > $200 found."
    else:
        condition = high_rate_hotels["star_level"] == 4
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rate_hotels)} high-rate hotels have star level 4."
        else:
            viol = high_rate_hotels[~condition]
            expl = f"{len(viol)} high-rate hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one hotel in Austin with a star level of 5."""
    austin_hotels = df[df["city"] == "austin"]
    if len(austin_hotels) == 0:
        truth = False
        expl = "No hotels in Austin found."
    else:
        has_star_5 = (austin_hotels["star_level"] == 5).any()
        truth = has_star_5
        if truth:
            expl = "At least one Austin hotel has star level 5."
        else:
            expl = f"No Austin hotels have star level 5 (star levels: {', '.join(map(str, austin_hotels['star_level'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel is in Chicago, then its occupancy rate is greater than 68%."""
    chicago_hotels = df[df["city"] == "chicago"]
    if len(chicago_hotels) == 0:
        truth = True
        expl = "No hotels in Chicago found."
    else:
        condition = chicago_hotels["occupancy_rate"] > 68
        truth = condition.all()
        if truth:
            expl = f"All {len(chicago_hotels)} Chicago hotels have occupancy > 68%."
        else:
            viol = chicago_hotels[~condition]
            expl = f"{len(viol)} Chicago hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with a cancellation rate less than 10% have a staff count greater than 35."""
    low_cancel_hotels = df[df["cancellation_rate"] < 10]
    if len(low_cancel_hotels) == 0:
        truth = True
        expl = "No hotels with cancellation rate < 10% found."
    else:
        condition = low_cancel_hotels["staff_count"] > 35
        truth = condition.all()
        if truth:
            expl = f"All {len(low_cancel_hotels)} low-cancellation hotels have staff > 35."
        else:
            viol = low_cancel_hotels[~condition]
            expl = f"{len(viol)} low-cancellation hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most hotels have an occupancy rate greater than 65%."""
    total_hotels = len(df)
    high_occupancy = (df["occupancy_rate"] > 65).sum()
    truth = high_occupancy > total_hotels / 2
    if truth:
        expl = f"{high_occupancy} out of {total_hotels} hotels have occupancy > 65%."
    else:
        expl = f"{high_occupancy} out of {total_hotels} hotels have occupancy > 65% (less than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Portland, then its average nightly rate is less than $200."""
    portland_hotels = df[df["city"] == "portland"]
    if len(portland_hotels) == 0:
        truth = True
        expl = "No hotels in Portland found."
    else:
        condition = portland_hotels["avg_nightly_rate"] < 200
        truth = condition.all()
        if truth:
            expl = f"All {len(portland_hotels)} Portland hotels have avg nightly rate < $200."
        else:
            viol = portland_hotels[~condition]
            expl = f"{len(viol)} Portland hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All hotels with a bookings month greater than 850 have a star level of 4."""
    high_bookings_hotels = df[df["bookings_month"] > 850]
    if len(high_bookings_hotels) == 0:
        truth = True
        expl = "No hotels with bookings month > 850 found."
    else:
        condition = high_bookings_hotels["star_level"] == 4
        truth = condition.all()
        if truth:
            expl = f"All {len(high_bookings_hotels)} high-bookings hotels have star level 4."
        else:
            viol = high_bookings_hotels[~condition]
            expl = f"{len(viol)} high-bookings hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one hotel in Dallas with an occupancy rate greater than 85%."""
    dallas_hotels = df[df["city"] == "dallas"]
    if len(dallas_hotels) == 0:
        truth = False
        expl = "No hotels in Dallas found."
    else:
        has_high_occupancy = (dallas_hotels["occupancy_rate"] > 85).any()
        truth = has_high_occupancy
        if truth:
            expl = "At least one Dallas hotel has occupancy > 85%."
        else:
            expl = f"No Dallas hotels have occupancy > 85% (occupancy rates: {', '.join(map(str, dallas_hotels['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel is in Miami, then its staff count is less than 30."""
    miami_hotels = df[df["city"] == "miami"]
    if len(miami_hotels) == 0:
        truth = True
        expl = "No hotels in Miami found."
    else:
        condition = miami_hotels["staff_count"] < 30
        truth = condition.all()
        if truth:
            expl = f"All {len(miami_hotels)} Miami hotels have staff < 30."
        else:
            viol = miami_hotels[~condition]
            expl = f"{len(viol)} Miami hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels with a star level of 3 have an average nightly rate less than $220."""
    star3_hotels = df[df["star_level"] == 3]
    if len(star3_hotels) == 0:
        truth = True
        expl = "No hotels with star level 3 found."
    else:
        condition = star3_hotels["avg_nightly_rate"] < 220
        truth = condition.all()
        if truth:
            expl = f"All {len(star3_hotels)} 3-star hotels have avg nightly rate < $220."
        else:
            viol = star3_hotels[~condition]
            expl = f"{len(viol)} 3-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most hotels have a staff count less than 40."""
    total_hotels = len(df)
    low_staff = (df["staff_count"] < 40).sum()
    truth = low_staff > total_hotels / 2
    if truth:
        expl = f"{low_staff} out of {total_hotels} hotels have staff < 40."
    else:
        expl = f"{low_staff} out of {total_hotels} hotels have staff < 40 (less than half)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel is in Austin, then its occupancy rate is greater than 65%."""
    austin_hotels = df[df["city"] == "austin"]
    if len(austin_hotels) == 0:
        truth = True
        expl = "No hotels in Austin found."
    else:
        condition = austin_hotels["occupancy_rate"] > 65
        truth = condition.all()
        if truth:
            expl = f"All {len(austin_hotels)} Austin hotels have occupancy > 65%."
        else:
            viol = austin_hotels[~condition]
            expl = f"{len(viol)} Austin hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All hotels with an occupancy rate greater than 80% have a star level of 4 or 5."""
    high_occupancy_hotels = df[df["occupancy_rate"] > 80]
    if len(high_occupancy_hotels) == 0:
        truth = True
        expl = "No hotels with occupancy > 80% found."
    else:
        condition = (high_occupancy_hotels["star_level"] == 4) | (high_occupancy_hotels["star_level"] == 5)
        truth = condition.all()
        if truth:
            expl = f"All {len(high_occupancy_hotels)} high-occupancy hotels have star level 4 or 5."
        else:
            viol = high_occupancy_hotels[~condition]
            expl = f"{len(viol)} high-occupancy hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one hotel in Phoenix with an occupancy rate greater than 85%."""
    phoenix_hotels = df[df["city"] == "phoenix"]
    if len(phoenix_hotels) == 0:
        truth = False
        expl = "No hotels in Phoenix found."
    else:
        has_high_occupancy = (phoenix_hotels["occupancy_rate"] > 85).any()
        truth = has_high_occupancy
        if truth:
            expl = "At least one Phoenix hotel has occupancy > 85%."
        else:
            expl = f"No Phoenix hotels have occupancy > 85% (occupancy rates: {', '.join(map(str, phoenix_hotels['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel is in Boston, then its staff count is greater than 35."""
    boston_hotels = df[df["city"] == "boston"]
    if len(boston_hotels) == 0:
        truth = True
        expl = "No hotels in Boston found."
    else:
        condition = boston_hotels["staff_count"] > 35
        truth = condition.all()
        if truth:
            expl = f"All {len(boston_hotels)} Boston hotels have staff > 35."
        else:
            viol = boston_hotels[~condition]
            expl = f"{len(viol)} Boston hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All hotels with a bookings month less than 700 have a star level of 3."""
    low_bookings_hotels = df[df["bookings_month"] < 700]
    if len(low_bookings_hotels) == 0:
        truth = True
        expl = "No hotels with bookings month < 700 found."
    else:
        condition = low_bookings_hotels["star_level"] == 3
        truth = condition.all()
        if truth:
            expl = f"All {len(low_bookings_hotels)} low-bookings hotels have star level 3."
        else:
            viol = low_bookings_hotels[~condition]
            expl = f"{len(viol)} low-bookings hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. Most hotels have an average nightly rate less than $250."""
    total_hotels = len(df)
    low_rate = (df["avg_nightly_rate"] < 250).sum()
    truth = low_rate > total_hotels / 2
    if truth:
        expl = f"{low_rate} out of {total_hotels} hotels have avg nightly rate < $250."
    else:
        expl = f"{low_rate} out of {total_hotels} hotels have avg nightly rate < $250 (less than half)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_65.csv")

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