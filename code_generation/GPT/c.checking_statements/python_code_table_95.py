import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All Atlanta hotels have an occupancy rate of at least 84.3%."""
    atlanta_hotels = df[df["city"] == "atlanta"]
    if atlanta_hotels.empty:
        truth = True
        expl = "No Atlanta hotels in dataset."
    else:
        condition = atlanta_hotels["occupancy_rate"] >= 84.3
        truth = condition.all()
        if truth:
            expl = f"All {len(atlanta_hotels)} Atlanta hotels meet the occupancy rate requirement."
        else:
            viol = atlanta_hotels[~condition]
            expl = f"{len(viol)} Atlanta hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All Denver hotels have an average nightly rate of at least $175.3."""
    denver_hotels = df[df["city"] == "denver"]
    if denver_hotels.empty:
        truth = True
        expl = "No Denver hotels in dataset."
    else:
        condition = denver_hotels["avg_nightly_rate"] >= 175.3
        truth = condition.all()
        if truth:
            expl = f"All {len(denver_hotels)} Denver hotels meet the average nightly rate requirement."
        else:
            viol = denver_hotels[~condition]
            expl = f"{len(viol)} Denver hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All 5-star hotels have an average nightly rate of at least $175.5."""
    five_star_hotels = df[df["star_level"] == 5]
    if five_star_hotels.empty:
        truth = True
        expl = "No 5-star hotels in dataset."
    else:
        condition = five_star_hotels["avg_nightly_rate"] >= 175.5
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star_hotels)} 5-star hotels meet the average nightly rate requirement."
        else:
            viol = five_star_hotels[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All 5-star hotels have a cancellation rate of at least 10.3%."""
    five_star_hotels = df[df["star_level"] == 5]
    if five_star_hotels.empty:
        truth = True
        expl = "No 5-star hotels in dataset."
    else:
        condition = five_star_hotels["cancellation_rate"] >= 10.3
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star_hotels)} 5-star hotels meet the cancellation rate requirement."
        else:
            viol = five_star_hotels[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All hotels with an average nightly rate above $200 are 5-star."""
    high_rate_hotels = df[df["avg_nightly_rate"] > 200]
    if high_rate_hotels.empty:
        truth = True
        expl = "No hotels with average nightly rate above $200 in dataset."
    else:
        condition = high_rate_hotels["star_level"] == 5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rate_hotels)} hotels with rate above $200 are 5-star."
        else:
            viol = high_rate_hotels[~condition]
            expl = f"{len(viol)} hotels with rate above $200 are not 5-star (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with at least 950 bookings per month have an average nightly rate of at least $173.9."""
    high_booking_hotels = df[df["bookings_month"] >= 950]
    if high_booking_hotels.empty:
        truth = True
        expl = "No hotels with at least 950 bookings/month in dataset."
    else:
        condition = high_booking_hotels["avg_nightly_rate"] >= 173.9
        truth = condition.all()
        if truth:
            expl = f"All {len(high_booking_hotels)} hotels with at least 950 bookings/month meet the rate requirement."
        else:
            viol = high_booking_hotels[~condition]
            expl = f"{len(viol)} hotels with at least 950 bookings/month violate the rate requirement (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All Chicago hotels have a cancellation rate of at least 10.3%."""
    chicago_hotels = df[df["city"] == "chicago"]
    if chicago_hotels.empty:
        truth = True
        expl = "No Chicago hotels in dataset."
    else:
        condition = chicago_hotels["cancellation_rate"] >= 10.3
        truth = condition.all()
        if truth:
            expl = f"All {len(chicago_hotels)} Chicago hotels meet the cancellation rate requirement."
        else:
            viol = chicago_hotels[~condition]
            expl = f"{len(viol)} Chicago hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All hotels with an occupancy rate of at least 85% are 4-star."""
    high_occupancy_hotels = df[df["occupancy_rate"] >= 85]
    if high_occupancy_hotels.empty:
        truth = True
        expl = "No hotels with occupancy rate at least 85% in dataset."
    else:
        condition = high_occupancy_hotels["star_level"] == 4
        truth = condition.all()
        if truth:
            expl = f"All {len(high_occupancy_hotels)} hotels with occupancy rate at least 85% are 4-star."
        else:
            viol = high_occupancy_hotels[~condition]
            expl = f"{len(viol)} hotels with occupancy rate at least 85% are not 4-star (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All 4-star hotels have a cancellation rate of at most 14.1%."""
    four_star_hotels = df[df["star_level"] == 4]
    if four_star_hotels.empty:
        truth = True
        expl = "No 4-star hotels in dataset."
    else:
        condition = four_star_hotels["cancellation_rate"] <= 14.1
        truth = condition.all()
        if truth:
            expl = f"All {len(four_star_hotels)} 4-star hotels meet the cancellation rate requirement."
        else:
            viol = four_star_hotels[~condition]
            expl = f"{len(viol)} 4-star hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_95.csv")

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
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()