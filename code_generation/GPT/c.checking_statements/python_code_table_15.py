import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 5-star hotels have an occupancy rate of at least 67.2%."""
    five_star = df[df["star_level"] == 5]
    if five_star.empty:
        truth = True
        expl = "No 5-star hotels in dataset."
    else:
        condition = five_star["occupancy_rate"] >= 67.2
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star)} 5-star hotels meet the occupancy requirement."
        else:
            viol = five_star[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hotels with a cancellation rate above 14% have an average nightly rate of no more than $214.5."""
    high_cancellation = df[df["cancellation_rate"] > 14]
    if high_cancellation.empty:
        truth = True
        expl = "No hotels with cancellation rate above 14%."
    else:
        condition = high_cancellation["avg_nightly_rate"] <= 214.5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_cancellation)} hotels with high cancellation rates meet the rate limit."
        else:
            viol = high_cancellation[~condition]
            expl = f"{len(viol)} hotels with high cancellation rates exceed the rate limit (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All Seattle hotels have an average nightly rate of $126.0 or less."""
    seattle_hotels = df[df["city"] == "seattle"]
    if seattle_hotels.empty:
        truth = True
        expl = "No Seattle hotels in dataset."
    else:
        condition = seattle_hotels["avg_nightly_rate"] <= 126.0
        truth = condition.all()
        if truth:
            expl = f"All {len(seattle_hotels)} Seattle hotels meet the rate limit."
        else:
            viol = seattle_hotels[~condition]
            expl = f"{len(viol)} Seattle hotels exceed the rate limit (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with at least 45 staff members have an occupancy rate of at least 72.2%."""
    many_staff = df[df["staff_count"] >= 45]
    if many_staff.empty:
        truth = True
        expl = "No hotels with at least 45 staff members."
    else:
        condition = many_staff["occupancy_rate"] >= 72.2
        truth = condition.all()
        if truth:
            expl = f"All {len(many_staff)} hotels with sufficient staff meet the occupancy requirement."
        else:
            viol = many_staff[~condition]
            expl = f"{len(viol)} hotels with sufficient staff fall below the occupancy requirement (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All 3-star hotels have an average nightly rate of no more than $141.4."""
    three_star = df[df["star_level"] == 3]
    if three_star.empty:
        truth = True
        expl = "No 3-star hotels in dataset."
    else:
        condition = three_star["avg_nightly_rate"] <= 141.4
        truth = condition.all()
        if truth:
            expl = f"All {len(three_star)} 3-star hotels meet the rate limit."
        else:
            viol = three_star[~condition]
            expl = f"{len(viol)} 3-star hotels exceed the rate limit (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with more than 900 bookings per month have an occupancy rate of at least 84.3%."""
    many_bookings = df[df["bookings_month"] > 900]
    if many_bookings.empty:
        truth = True
        expl = "No hotels with more than 900 bookings/month."
    else:
        condition = many_bookings["occupancy_rate"] >= 84.3
        truth = condition.all()
        if truth:
            expl = f"All {len(many_bookings)} hotels with high bookings meet the occupancy requirement."
        else:
            viol = many_bookings[~condition]
            expl = f"{len(viol)} hotels with high bookings fall below the occupancy requirement (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels with an average nightly rate of $200 or more have a star level of at least 4."""
    high_rate = df[df["avg_nightly_rate"] >= 200]
    if high_rate.empty:
        truth = True
        expl = "No hotels with average nightly rate of $200 or more."
    else:
        condition = high_rate["star_level"] >= 4
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rate)} hotels with high rates meet the star level requirement."
        else:
            viol = high_rate[~condition]
            expl = f"{len(viol)} hotels with high rates fall below the star level requirement (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most hotels have a cancellation rate greater than 10%."""
    total_hotels = len(df)
    high_cancellation = df[df["cancellation_rate"] > 10]
    count_high = len(high_cancellation)
    truth = count_high > total_hotels / 2
    expl = f"{count_high} out of {total_hotels} hotels have cancellation rate > 10%, which {'is' if truth else 'is not'} more than half."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All Chicago hotels have at least 38 staff members."""
    chicago_hotels = df[df["city"] == "chicago"]
    if chicago_hotels.empty:
        truth = True
        expl = "No Chicago hotels in dataset."
    else:
        condition = chicago_hotels["staff_count"] >= 38
        truth = condition.all()
        if truth:
            expl = f"All {len(chicago_hotels)} Chicago hotels meet the staff requirement."
        else:
            viol = chicago_hotels[~condition]
            expl = f"{len(viol)} Chicago hotels fall below the staff requirement (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
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
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()