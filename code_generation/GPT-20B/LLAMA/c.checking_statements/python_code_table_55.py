import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Austin have an average nightly rate greater than $150."""
    austin = df[df["city"] == "austin"]
    condition = austin["avg_nightly_rate"] > 150
    truth = condition.all()
    if truth:
        expl = f"All {len(austin)} Austin hotels have avg nightly rate > 150."
    else:
        viol = austin[~condition]
        expl = f"{len(viol)} Austin hotels violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Seattle, then its staff count is less than 40."""
    seattle = df[df["city"] == "seattle"]
    condition = seattle["staff_count"] < 40
    truth = condition.all()
    if truth:
        expl = f"All {len(seattle)} Seattle hotels have staff count < 40."
    else:
        viol = seattle[~condition]
        expl = f"{len(viol)} Seattle hotels violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one hotel in Dallas with an occupancy rate greater than 85%."""
    matches = df[(df["city"] == "dallas") & (df["occupancy_rate"] > 85)]
    truth = not matches.empty
    if truth:
        expl = f"Found {len(matches)} Dallas hotel(s) with occupancy rate > 85%."
    else:
        expl = "No Dallas hotel has occupancy rate > 85%."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with a star level of 5 have an average nightly rate greater than $200."""
    star5 = df[df["star_level"] == 5]
    condition = star5["avg_nightly_rate"] > 200
    truth = condition.all()
    if truth:
        expl = f"All {len(star5)} star-5 hotels have avg nightly rate > 200."
    else:
        viol = star5[~condition]
        expl = f"{len(viol)} star-5 hotels violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel has a cancellation rate less than 10%, then its occupancy rate is greater than 70%."""
    low_cancel = df[df["cancellation_rate"] < 10]
    condition = low_cancel["occupancy_rate"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(low_cancel)} hotels with cancellation rate < 10% have occupancy rate > 70%."
    else:
        viol = low_cancel[~condition]
        expl = f"{len(viol)} hotels with cancellation rate < 10% violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most hotels in the dataset have a staff count greater than 30."""
    total = len(df)
    count = (df["staff_count"] > 30).sum()
    percent = count / total * 100
    truth = percent > 50
    if truth:
        expl = f"{percent:.1f}% of hotels have staff count > 30 ({count}/{total})."
    else:
        expl = f"{percent:.1f}% of hotels have staff count > 30 ({count}/{total}), which is not a majority."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels in Boston have a star level of either 3 or 5."""
    boston = df[df["city"] == "boston"]
    condition = boston["star_level"].isin([3, 5])
    truth = condition.all()
    if truth:
        expl = f"All {len(boston)} Boston hotels have star level 3 or 5."
    else:
        viol = boston[~condition]
        expl = f"{len(viol)} Boston hotels violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Miami, then its occupancy rate is less than 70%."""
    miami = df[df["city"] == "miami"]
    condition = miami["occupancy_rate"] < 70
    truth = condition.all()
    if truth:
        expl = f"All {len(miami)} Miami hotels have occupancy rate < 70%."
    else:
        viol = miami[~condition]
        expl = f"{len(viol)} Miami hotels violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one hotel in Austin with a bookings per month count greater than 800."""
    matches = df[(df["city"] == "austin") & (df["bookings_month"] > 800)]
    truth = not matches.empty
    if truth:
        expl = f"Found {len(matches)} Austin hotel(s) with bookings per month > 800."
    else:
        expl = "No Austin hotel has bookings per month > 800."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All hotels with a star level of 4 have an average nightly rate greater than $180."""
    star4 = df[df["star_level"] == 4]
    condition = star4["avg_nightly_rate"] > 180
    truth = condition.all()
    if truth:
        expl = f"All {len(star4)} star-4 hotels have avg nightly rate > 180."
    else:
        viol = star4[~condition]
        expl = f"{len(viol)} star-4 hotels violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel has an occupancy rate greater than 80%, then its cancellation rate is less than 12%."""
    high_occ = df[df["occupancy_rate"] > 80]
    condition = high_occ["cancellation_rate"] < 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_occ)} hotels with occupancy > 80% have cancellation rate < 12%."
    else:
        viol = high_occ[~condition]
        expl = f"{len(viol)} hotels with occupancy > 80% violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels in Dallas have an average nightly rate greater than $170."""
    dallas = df[df["city"] == "dallas"]
    condition = dallas["avg_nightly_rate"] > 170
    truth = condition.all()
    if truth:
        expl = f"All {len(dallas)} Dallas hotels have avg nightly rate > 170."
    else:
        viol = dallas[~condition]
        expl = f"{len(viol)} Dallas hotels violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. There exists at least one hotel in Seattle with a staff count greater than 40."""
    matches = df[(df["city"] == "seattle") & (df["staff_count"] > 40)]
    truth = not matches.empty
    if truth:
        expl = f"Found {len(matches)} Seattle hotel(s) with staff count > 40."
    else:
        expl = "No Seattle hotel has staff count > 40."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel has a star level of 3, then its average nightly rate is less than $220."""
    star3 = df[df["star_level"] == 3]
    condition = star3["avg_nightly_rate"] < 220
    truth = condition.all()
    if truth:
        expl = f"All {len(star3)} star-3 hotels have avg nightly rate < 220."
    else:
        viol = star3[~condition]
        expl = f"{len(viol)} star-3 hotels violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most hotels in the dataset have an occupancy rate greater than 70%."""
    total = len(df)
    count = (df["occupancy_rate"] > 70).sum()
    percent = count / total * 100
    truth = percent > 50
    if truth:
        expl = f"{percent:.1f}% of hotels have occupancy rate > 70% ({count}/{total})."
    else:
        expl = f"{percent:.1f}% of hotels have occupancy rate > 70% ({count}/{total}), which is not a majority."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All hotels with a bookings per month count greater than 700 have a staff count greater than 25."""
    high_book = df[df["bookings_month"] > 700]
    condition = high_book["staff_count"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(high_book)} hotels with bookings > 700 have staff count > 25."
    else:
        viol = high_book[~condition]
        expl = f"{len(viol)} hotels with bookings > 700 violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel is in Austin, then its star level is either 3, 4, or 5."""
    austin = df[df["city"] == "austin"]
    condition = austin["star_level"].isin([3, 4, 5])
    truth = condition.all()
    if truth:
        expl = f"All {len(austin)} Austin hotels have star level 3, 4, or 5."
    else:
        viol = austin[~condition]
        expl = f"{len(viol)} Austin hotels violate the rule (hotel_ids: {', '.join(map(str, viol['hotel_id']))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_55.csv")

    # Convert numeric columns
    numeric_cols = ["occupancy_rate", "avg_nightly_rate", "bookings_month",
                    "cancellation_rate", "staff_count", "star_level"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()