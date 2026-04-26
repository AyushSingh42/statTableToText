import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Denver have an average nightly rate greater than $170."""
    denver_hotels = df[df["city"] == "denver"]
    if denver_hotels.empty:
        truth = True
        expl = "No hotels in Denver found."
    else:
        condition = denver_hotels["avg_nightly_rate"] > 170
        truth = condition.all()
        if truth:
            expl = f"All {len(denver_hotels)} Denver hotels have rates > $170."
        else:
            viol = denver_hotels[~condition]
            expl = f"{len(viol)} Denver hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Atlanta, then its occupancy rate is greater than 84%."""
    atlanta_hotels = df[df["city"] == "atlanta"]
    if atlanta_hotels.empty:
        truth = True
        expl = "No hotels in Atlanta found."
    else:
        condition = atlanta_hotels["occupancy_rate"] > 84
        truth = condition.all()
        if truth:
            expl = f"All {len(atlanta_hotels)} Atlanta hotels have occupancy > 84%."
        else:
            viol = atlanta_hotels[~condition]
            expl = f"{len(viol)} Atlanta hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hotels with a star level of 5 have an average nightly rate greater than $175."""
    five_star_hotels = df[df["star_level"] == 5]
    if five_star_hotels.empty:
        truth = True
        expl = "No 5-star hotels found."
    else:
        condition = five_star_hotels["avg_nightly_rate"] > 175
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star_hotels)} 5-star hotels have rates > $175."
        else:
            viol = five_star_hotels[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one hotel in Phoenix with a cancellation rate greater than 15%."""
    phoenix_hotels = df[df["city"] == "phoenix"]
    if phoenix_hotels.empty:
        truth = False
        expl = "No hotels in Phoenix found."
    else:
        condition = phoenix_hotels["cancellation_rate"] > 15
        truth = condition.any()
        if truth:
            viol = phoenix_hotels[condition]
            expl = f"At least one Phoenix hotel ({viol.iloc[0]['hotel_id']}) has cancellation rate > 15%."
        else:
            expl = f"No Phoenix hotels have cancellation rate > 15%."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel is in Chicago, then its staff count is less than 40."""
    chicago_hotels = df[df["city"] == "chicago"]
    if chicago_hotels.empty:
        truth = True
        expl = "No hotels in Chicago found."
    else:
        condition = chicago_hotels["staff_count"] < 40
        truth = condition.all()
        if truth:
            expl = f"All {len(chicago_hotels)} Chicago hotels have staff < 40."
        else:
            viol = chicago_hotels[~condition]
            expl = f"{len(viol)} Chicago hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with an occupancy rate greater than 85% have a star level of 4 or 5."""
    high_occ_hotels = df[df["occupancy_rate"] > 85]
    if high_occ_hotels.empty:
        truth = True
        expl = "No hotels with occupancy > 85% found."
    else:
        condition = (high_occ_hotels["star_level"] == 4) | (high_occ_hotels["star_level"] == 5)
        truth = condition.all()
        if truth:
            expl = f"All {len(high_occ_hotels)} high-occupancy hotels have star level 4 or 5."
        else:
            viol = high_occ_hotels[~condition]
            expl = f"{len(viol)} high-occupancy hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most hotels in the dataset have an average nightly rate greater than $150."""
    condition = df["avg_nightly_rate"] > 150
    count_above = condition.sum()
    total = len(df)
    truth = count_above > total / 2
    if truth:
        expl = f"{count_above} out of {total} hotels have rates > $150 (more than half)."
    else:
        expl = f"{count_above} out of {total} hotels have rates > $150 (not more than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Boston, then its occupancy rate is less than 80%."""
    boston_hotels = df[df["city"] == "boston"]
    if boston_hotels.empty:
        truth = True
        expl = "No hotels in Boston found."
    else:
        condition = boston_hotels["occupancy_rate"] < 80
        truth = condition.all()
        if truth:
            expl = f"All {len(boston_hotels)} Boston hotels have occupancy < 80%."
        else:
            viol = boston_hotels[~condition]
            expl = f"{len(viol)} Boston hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All hotels with a staff count greater than 40 have a star level of 4."""
    high_staff_hotels = df[df["staff_count"] > 40]
    if high_staff_hotels.empty:
        truth = True
        expl = "No hotels with staff > 40 found."
    else:
        condition = high_staff_hotels["star_level"] == 4
        truth = condition.all()
        if truth:
            expl = f"All {len(high_staff_hotels)} high-staff hotels have star level 4."
        else:
            viol = high_staff_hotels[~condition]
            expl = f"{len(viol)} high-staff hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one hotel in Atlanta with an occupancy rate greater than 87%."""
    atlanta_hotels = df[df["city"] == "atlanta"]
    if atlanta_hotels.empty:
        truth = False
        expl = "No hotels in Atlanta found."
    else:
        condition = atlanta_hotels["occupancy_rate"] > 87
        truth = condition.any()
        if truth:
            viol = atlanta_hotels[condition]
            expl = f"At least one Atlanta hotel ({viol.iloc[0]['hotel_id']}) has occupancy > 87%."
        else:
            expl = f"No Atlanta hotels have occupancy > 87%."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel has a star level of 3, then its average nightly rate is less than $190."""
    three_star_hotels = df[df["star_level"] == 3]
    if three_star_hotels.empty:
        truth = True
        expl = "No 3-star hotels found."
    else:
        condition = three_star_hotels["avg_nightly_rate"] < 190
        truth = condition.all()
        if truth:
            expl = f"All {len(three_star_hotels)} 3-star hotels have rates < $190."
        else:
            viol = three_star_hotels[~condition]
            expl = f"{len(viol)} 3-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels with a cancellation rate less than 10% have a star level of 4."""
    low_cancel_hotels = df[df["cancellation_rate"] < 10]
    if low_cancel_hotels.empty:
        truth = True
        expl = "No hotels with cancellation rate < 10% found."
    else:
        condition = low_cancel_hotels["star_level"] == 4
        truth = condition.all()
        if truth:
            expl = f"All {len(low_cancel_hotels)} low-cancellation hotels have star level 4."
        else:
            viol = low_cancel_hotels[~condition]
            expl = f"{len(viol)} low-cancellation hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most hotels in the dataset have a staff count greater than 30."""
    condition = df["staff_count"] > 30
    count_above = condition.sum()
    total = len(df)
    truth = count_above > total / 2
    if truth:
        expl = f"{count_above} out of {total} hotels have staff > 30 (more than half)."
    else:
        expl = f"{count_above} out of {total} hotels have staff > 30 (not more than half)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel is in Denver, then its cancellation rate is less than 10%."""
    denver_hotels = df[df["city"] == "denver"]
    if denver_hotels.empty:
        truth = True
        expl = "No hotels in Denver found."
    else:
        condition = denver_hotels["cancellation_rate"] < 10
        truth = condition.all()
        if truth:
            expl = f"All {len(denver_hotels)} Denver hotels have cancellation rate < 10%."
        else:
            viol = denver_hotels[~condition]
            expl = f"{len(viol)} Denver hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All hotels with an occupancy rate greater than 80% have an average nightly rate greater than $120."""
    high_occ_hotels = df[df["occupancy_rate"] > 80]
    if high_occ_hotels.empty:
        truth = True
        expl = "No hotels with occupancy > 80% found."
    else:
        condition = high_occ_hotels["avg_nightly_rate"] > 120
        truth = condition.all()
        if truth:
            expl = f"All {len(high_occ_hotels)} high-occupancy hotels have rates > $120."
        else:
            viol = high_occ_hotels[~condition]
            expl = f"{len(viol)} high-occupancy hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one hotel in Phoenix with a staff count greater than 40."""
    phoenix_hotels = df[df["city"] == "phoenix"]
    if phoenix_hotels.empty:
        truth = False
        expl = "No hotels in Phoenix found."
    else:
        condition = phoenix_hotels["staff_count"] > 40
        truth = condition.any()
        if truth:
            viol = phoenix_hotels[condition]
            expl = f"At least one Phoenix hotel ({viol.iloc[0]['hotel_id']}) has staff > 40."
        else:
            expl = f"No Phoenix hotels have staff > 40."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel has a star level of 5, then its occupancy rate is greater than 75%."""
    five_star_hotels = df[df["star_level"] == 5]
    if five_star_hotels.empty:
        truth = True
        expl = "No 5-star hotels found."
    else:
        condition = five_star_hotels["occupancy_rate"] > 75
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star_hotels)} 5-star hotels have occupancy > 75%."
        else:
            viol = five_star_hotels[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All hotels with an average nightly rate greater than $200 have a star level of 5."""
    high_rate_hotels = df[df["avg_nightly_rate"] > 200]
    if high_rate_hotels.empty:
        truth = True
        expl = "No hotels with rate > $200 found."
    else:
        condition = high_rate_hotels["star_level"] == 5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rate_hotels)} high-rate hotels have star level 5."
        else:
            viol = high_rate_hotels[~condition]
            expl = f"{len(viol)} high-rate hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
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
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
        (18, stmt_18)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()