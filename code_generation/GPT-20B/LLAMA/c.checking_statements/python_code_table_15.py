import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Atlanta have an average nightly rate greater than $110."""
    atlanta = df[df["city"].str.lower() == "atlanta"]
    condition = atlanta["avg_nightly_rate"] > 110
    truth = condition.all()
    if truth:
        expl = f"All {len(atlanta)} Atlanta hotels have avg nightly rate > 110."
    else:
        viol = atlanta[~condition]
        expl = f"{len(viol)} Atlanta hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Seattle, then its occupancy rate is greater than 78%."""
    seattle = df[df["city"].str.lower() == "seattle"]
    condition = seattle["occupancy_rate"] > 78
    truth = condition.all()
    if truth:
        expl = f"All {len(seattle)} Seattle hotels have occupancy rate > 78%."
    else:
        viol = seattle[~condition]
        expl = f"{len(viol)} Seattle hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hotels with a star level of 5 have an occupancy rate greater than 72%."""
    five_star = df[df["star_level"] == 5]
    condition = five_star["occupancy_rate"] > 72
    truth = condition.all()
    if truth:
        expl = f"All {len(five_star)} star-5 hotels have occupancy rate > 72%."
    else:
        viol = five_star[~condition]
        expl = f"{len(viol)} star-5 hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one hotel in Dallas with an occupancy rate less than 85%."""
    dallas = df[(df["city"].str.lower() == "dallas") & (df["occupancy_rate"] < 85)]
    truth = not dallas.empty
    if truth:
        expl = f"Found {len(dallas)} Dallas hotel(s) with occupancy rate < 85%."
    else:
        expl = "No Dallas hotel has occupancy rate < 85%."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel has a staff count greater than 40, then its occupancy rate is greater than 83%."""
    high_staff = df[df["staff_count"] > 40]
    condition = high_staff["occupancy_rate"] > 83
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} hotels with staff > 40 have occupancy rate > 83%."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} hotels with staff > 40 violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with a cancellation rate greater than 14% have a star level less than 5."""
    high_cancel = df[df["cancellation_rate"] > 14]
    condition = high_cancel["star_level"] < 5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_cancel)} hotels with cancellation > 14% have star level < 5."
    else:
        viol = high_cancel[~condition]
        expl = f"{len(viol)} hotels with cancellation > 14% violate the rule (star level: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a hotel is in Portland, then its average nightly rate is less than $225."""
    portland = df[df["city"].str.lower() == "portland"]
    condition = portland["avg_nightly_rate"] < 225
    truth = condition.all()
    if truth:
        expl = f"All {len(portland)} Portland hotels have avg nightly rate < 225."
    else:
        viol = portland[~condition]
        expl = f"{len(viol)} Portland hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most hotels in the dataset have an occupancy rate greater than 70%."""
    total = len(df)
    count = (df["occupancy_rate"] > 70).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} hotels have occupancy > 70%."
    else:
        expl = f"Only {count} out of {total} hotels have occupancy > 70%."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All hotels with a bookings month greater than 800 have an occupancy rate greater than 75%."""
    high_bookings = df[df["bookings_month"] > 800]
    condition = high_bookings["occupancy_rate"] > 75
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bookings)} hotels with bookings > 800 have occupancy > 75%."
    else:
        viol = high_bookings[~condition]
        expl = f"{len(viol)} hotels with bookings > 800 violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a hotel has a star level of 4, then its average nightly rate is less than $215."""
    four_star = df[df["star_level"] == 4]
    condition = four_star["avg_nightly_rate"] < 215
    truth = condition.all()
    if truth:
        expl = f"All {len(four_star)} star-4 hotels have avg nightly rate < 215."
    else:
        viol = four_star[~condition]
        expl = f"{len(viol)} star-4 hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. There exists at least one hotel in Chicago with a staff count greater than 45."""
    chicago = df[(df["city"].str.lower() == "chicago") & (df["staff_count"] > 45)]
    truth = not chicago.empty
    if truth:
        expl = f"Found {len(chicago)} Chicago hotel(s) with staff > 45."
    else:
        expl = "No Chicago hotel has staff > 45."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels with an occupancy rate greater than 85% have a star level greater than 3."""
    high_occ = df[df["occupancy_rate"] > 85]
    condition = high_occ["star_level"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(high_occ)} hotels with occupancy > 85% have star level > 3."
    else:
        viol = high_occ[~condition]
        expl = f"{len(viol)} hotels with occupancy > 85% violate the rule (star level: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a hotel is in Miami, then its occupancy rate is greater than 80%."""
    miami = df[df["city"].str.lower() == "miami"]
    condition = miami["occupancy_rate"] > 80
    truth = condition.all()
    if truth:
        expl = f"All {len(miami)} Miami hotels have occupancy > 80%."
    else:
        viol = miami[~condition]
        expl = f"{len(viol)} Miami hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All hotels with a cancellation rate less than 10% have a staff count less than 30."""
    low_cancel = df[df["cancellation_rate"] < 10]
    condition = low_cancel["staff_count"] < 30
    truth = condition.all()
    if truth:
        expl = f"All {len(low_cancel)} hotels with cancellation < 10% have staff < 30."
    else:
        viol = low_cancel[~condition]
        expl = f"{len(viol)} hotels with cancellation < 10% violate the rule (staff: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most hotels in the dataset have a staff count less than 40."""
    total = len(df)
    count = (df["staff_count"] < 40).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} hotels have staff < 40."
    else:
        expl = f"Only {count} out of {total} hotels have staff < 40."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a hotel has an average nightly rate greater than $200, then its star level is greater than 3."""
    high_rate = df[df["avg_nightly_rate"] > 200]
    condition = high_rate["star_level"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rate)} hotels with rate > 200 have star level > 3."
    else:
        viol = high_rate[~condition]
        expl = f"{len(viol)} hotels with rate > 200 violate the rule (star level: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. There exists at least one hotel in Boston with an occupancy rate greater than 80%."""
    boston = df[(df["city"].str.lower() == "boston") & (df["occupancy_rate"] > 80)]
    truth = not boston.empty
    if truth:
        expl = f"Found {len(boston)} Boston hotel(s) with occupancy > 80%."
    else:
        expl = "No Boston hotel has occupancy > 80%."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All hotels with a bookings month less than 700 have a star level less than 5."""
    low_bookings = df[df["bookings_month"] < 700]
    condition = low_bookings["star_level"] < 5
    truth = condition.all()
    if truth:
        expl = f"All {len(low_bookings)} hotels with bookings < 700 have star level < 5."
    else:
        viol = low_bookings[~condition]
        expl = f"{len(viol)} hotels with bookings < 700 violate the rule (star level: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. If a hotel has a staff count less than 25, then its occupancy rate is less than 85%."""
    low_staff = df[df["staff_count"] < 25]
    condition = low_staff["occupancy_rate"] < 85
    truth = condition.all()
    if truth:
        expl = f"All {len(low_staff)} hotels with staff < 25 have occupancy < 85%."
    else:
        viol = low_staff[~condition]
        expl = f"{len(viol)} hotels with staff < 25 violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_15.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()