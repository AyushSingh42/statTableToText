import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Phoenix have an occupancy rate greater than 70%."""
    phx_hotels = df[df["city"].str.lower() == "phoenix"]
    if phx_hotels.empty:
        truth = True
        expl = "No hotels in Phoenix found."
    else:
        condition = phx_hotels["occupancy_rate"] > 70
        truth = condition.all()
        if truth:
            expl = f"All {len(phx_hotels)} Phoenix hotels have occupancy > 70%."
        else:
            viol = phx_hotels[~condition]
            expl = f"{len(viol)} Phoenix hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Atlanta, then its cancellation rate is greater than 10%."""
    atlanta_hotels = df[df["city"].str.lower() == "atlanta"]
    if atlanta_hotels.empty:
        truth = True
        expl = "No hotels in Atlanta found."
    else:
        condition = atlanta_hotels["cancellation_rate"] > 10
        truth = condition.all()
        if truth:
            expl = f"All {len(atlanta_hotels)} Atlanta hotels have cancellation rate > 10%."
        else:
            viol = atlanta_hotels[~condition]
            expl = f"{len(viol)} Atlanta hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hotels with a star level of 5 have an occupancy rate greater than 80%."""
    five_star_hotels = df[df["star_level"] == 5]
    if five_star_hotels.empty:
        truth = True
        expl = "No 5-star hotels found."
    else:
        condition = five_star_hotels["occupancy_rate"] > 80
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star_hotels)} 5-star hotels have occupancy > 80%."
        else:
            viol = five_star_hotels[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one hotel in Chicago with a staff count greater than 40."""
    chicago_hotels = df[df["city"].str.lower() == "chicago"]
    if chicago_hotels.empty:
        truth = False
        expl = "No hotels in Chicago found."
    else:
        condition = chicago_hotels["staff_count"] > 40
        truth = condition.any()
        if truth:
            expl = f"At least one Chicago hotel has staff count > 40."
        else:
            expl = f"No Chicago hotels have staff count > 40."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel has a star level of 4, then its average nightly rate is less than $220."""
    four_star_hotels = df[df["star_level"] == 4]
    if four_star_hotels.empty:
        truth = True
        expl = "No 4-star hotels found."
    else:
        condition = four_star_hotels["avg_nightly_rate"] < 220
        truth = condition.all()
        if truth:
            expl = f"All {len(four_star_hotels)} 4-star hotels have nightly rate < $220."
        else:
            viol = four_star_hotels[~condition]
            expl = f"{len(viol)} 4-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with a bookings month greater than 900 have a staff count greater than 30."""
    high_bookings_hotels = df[df["bookings_month"] > 900]
    if high_bookings_hotels.empty:
        truth = True
        expl = "No hotels with bookings_month > 900 found."
    else:
        condition = high_bookings_hotels["staff_count"] > 30
        truth = condition.all()
        if truth:
            expl = f"All {len(high_bookings_hotels)} high-bookings hotels have staff count > 30."
        else:
            viol = high_bookings_hotels[~condition]
            expl = f"{len(viol)} high-bookings hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most hotels in the dataset have an occupancy rate greater than 70%."""
    condition = df["occupancy_rate"] > 70
    total = len(df)
    satisfied = condition.sum()
    truth = satisfied > total / 2
    if truth:
        expl = f"More than half ({satisfied}/{total}) of hotels have occupancy > 70%."
    else:
        expl = f"Less than half ({satisfied}/{total}) of hotels have occupancy > 70%."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Denver, then its average nightly rate is greater than $140."""
    denver_hotels = df[df["city"].str.lower() == "denver"]
    if denver_hotels.empty:
        truth = True
        expl = "No hotels in Denver found."
    else:
        condition = denver_hotels["avg_nightly_rate"] > 140
        truth = condition.all()
        if truth:
            expl = f"All {len(denver_hotels)} Denver hotels have nightly rate > $140."
        else:
            viol = denver_hotels[~condition]
            expl = f"{len(viol)} Denver hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All hotels with a star level of 3 have a staff count less than 45."""
    three_star_hotels = df[df["star_level"] == 3]
    if three_star_hotels.empty:
        truth = True
        expl = "No 3-star hotels found."
    else:
        condition = three_star_hotels["staff_count"] < 45
        truth = condition.all()
        if truth:
            expl = f"All {len(three_star_hotels)} 3-star hotels have staff count < 45."
        else:
            viol = three_star_hotels[~condition]
            expl = f"{len(viol)} 3-star hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one hotel in Atlanta with a star level of 5 and an occupancy rate greater than 85%."""
    atlanta_hotels = df[(df["city"].str.lower() == "atlanta") & (df["star_level"] == 5)]
    if atlanta_hotels.empty:
        truth = False
        expl = "No 5-star hotels in Atlanta found."
    else:
        condition = atlanta_hotels["occupancy_rate"] > 85
        truth = condition.any()
        if truth:
            expl = f"At least one Atlanta 5-star hotel has occupancy > 85%."
        else:
            expl = f"No Atlanta 5-star hotels have occupancy > 85%."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel has a staff count greater than 40, then its star level is 5."""
    high_staff_hotels = df[df["staff_count"] > 40]
    if high_staff_hotels.empty:
        truth = True
        expl = "No hotels with staff count > 40 found."
    else:
        condition = high_staff_hotels["star_level"] == 5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_staff_hotels)} high-staff hotels have star level 5."
        else:
            viol = high_staff_hotels[~condition]
            expl = f"{len(viol)} high-staff hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels in Boston have a star level of 4."""
    boston_hotels = df[df["city"].str.lower() == "boston"]
    if boston_hotels.empty:
        truth = True
        expl = "No hotels in Boston found."
    else:
        condition = boston_hotels["star_level"] == 4
        truth = condition.all()
        if truth:
            expl = f"All {len(boston_hotels)} Boston hotels have star level 4."
        else:
            viol = boston_hotels[~condition]
            expl = f"{len(viol)} Boston hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a hotel is in Phoenix, then its cancellation rate is less than 15%."""
    phx_hotels = df[df["city"].str.lower() == "phoenix"]
    if phx_hotels.empty:
        truth = True
        expl = "No hotels in Phoenix found."
    else:
        condition = phx_hotels["cancellation_rate"] < 15
        truth = condition.all()
        if truth:
            expl = f"All {len(phx_hotels)} Phoenix hotels have cancellation rate < 15%."
        else:
            viol = phx_hotels[~condition]
            expl = f"{len(viol)} Phoenix hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All hotels with an occupancy rate greater than 85% have a star level of 5."""
    high_occ_hotels = df[df["occupancy_rate"] > 85]
    if high_occ_hotels.empty:
        truth = True
        expl = "No hotels with occupancy > 85% found."
    else:
        condition = high_occ_hotels["star_level"] == 5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_occ_hotels)} high-occupancy hotels have star level 5."
        else:
            viol = high_occ_hotels[~condition]
            expl = f"{len(viol)} high-occupancy hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most hotels in the dataset have a staff count greater than 30."""
    condition = df["staff_count"] > 30
    total = len(df)
    satisfied = condition.sum()
    truth = satisfied > total / 2
    if truth:
        expl = f"More than half ({satisfied}/{total}) of hotels have staff count > 30."
    else:
        expl = f"Less than half ({satisfied}/{total}) of hotels have staff count > 30."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a hotel has a bookings month greater than 800, then its occupancy rate is greater than 70%."""
    high_bookings_hotels = df[df["bookings_month"] > 800]
    if high_bookings_hotels.empty:
        truth = True
        expl = "No hotels with bookings_month > 800 found."
    else:
        condition = high_bookings_hotels["occupancy_rate"] > 70
        truth = condition.all()
        if truth:
            expl = f"All {len(high_bookings_hotels)} high-bookings hotels have occupancy > 70%."
        else:
            viol = high_bookings_hotels[~condition]
            expl = f"{len(viol)} high-bookings hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. There exists at least one hotel in Chicago with a star level of 5 and an occupancy rate greater than 80%."""
    chicago_hotels = df[(df["city"].str.lower() == "chicago") & (df["star_level"] == 5)]
    if chicago_hotels.empty:
        truth = False
        expl = "No 5-star hotels in Chicago found."
    else:
        condition = chicago_hotels["occupancy_rate"] > 80
        truth = condition.any()
        if truth:
            expl = f"At least one Chicago 5-star hotel has occupancy > 80%."
        else:
            expl = f"No Chicago 5-star hotels have occupancy > 80%."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_5.csv")

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