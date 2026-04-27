import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Denver have an average nightly rate greater than $140."""
    denver_hotels = df[df["city"] == "denver"]
    if denver_hotels.empty:
        truth = True
        expl = "No hotels in Denver found."
    else:
        condition = denver_hotels["avg_nightly_rate"] > 140
        truth = condition.all()
        if truth:
            expl = f"All {len(denver_hotels)} Denver hotels have rates > $140."
        else:
            viol = denver_hotels[~condition]
            expl = f"{len(viol)} Denver hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Austin, then its occupancy rate is greater than 73%."""
    austin_hotels = df[df["city"] == "austin"]
    if austin_hotels.empty:
        truth = True
        expl = "No hotels in Austin found."
    else:
        condition = austin_hotels["occupancy_rate"] > 73
        truth = condition.all()
        if truth:
            expl = f"All {len(austin_hotels)} Austin hotels have occupancy > 73%."
        else:
            viol = austin_hotels[~condition]
            expl = f"{len(viol)} Austin hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one hotel in Portland with a staff count less than 30."""
    portland_hotels = df[df["city"] == "portland"]
    if portland_hotels.empty:
        truth = False
        expl = "No hotels in Portland found."
    else:
        condition = portland_hotels["staff_count"] < 30
        truth = condition.any()
        if truth:
            viol = portland_hotels[condition]
            expl = f"At least one Portland hotel ({viol.iloc[0]['hotel_id']}) has staff < 30."
        else:
            expl = f"No Portland hotels have staff < 30."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with a star level of 5 have an average nightly rate greater than $150."""
    five_star_hotels = df[df["star_level"] == 5]
    if five_star_hotels.empty:
        truth = True
        expl = "No 5-star hotels found."
    else:
        condition = five_star_hotels["avg_nightly_rate"] > 150
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star_hotels)} 5-star hotels have rates > $150."
        else:
            viol = five_star_hotels[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel has a cancellation rate less than 12%, then its occupancy rate is greater than 75%."""
    filtered = df[df["cancellation_rate"] < 12]
    if filtered.empty:
        truth = True
        expl = "No hotels with cancellation rate < 12% found."
    else:
        condition = filtered["occupancy_rate"] > 75
        truth = condition.all()
        if truth:
            expl = f"All {len(filtered)} hotels with cancellation < 12% have occupancy > 75%."
        else:
            viol = filtered[~condition]
            expl = f"{len(viol)} hotels with cancellation < 12% violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most hotels in the dataset have a staff count greater than 30."""
    condition = df["staff_count"] > 30
    total = len(df)
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} hotels have staff > 30 (more than half)."
    else:
        expl = f"{count} out of {total} hotels have staff > 30 (not more than half)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels in Chicago with a star level of 3 have an occupancy rate greater than 72%."""
    chicago_three_stars = df[(df["city"] == "chicago") & (df["star_level"] == 3)]
    if chicago_three_stars.empty:
        truth = True
        expl = "No Chicago 3-star hotels found."
    else:
        condition = chicago_three_stars["occupancy_rate"] > 72
        truth = condition.all()
        if truth:
            expl = f"All {len(chicago_three_stars)} Chicago 3-star hotels have occupancy > 72%."
        else:
            viol = chicago_three_stars[~condition]
            expl = f"{len(viol)} Chicago 3-star hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Phoenix, then its average nightly rate is greater than $200."""
    phoenix_hotels = df[df["city"] == "phoenix"]
    if phoenix_hotels.empty:
        truth = True
        expl = "No hotels in Phoenix found."
    else:
        condition = phoenix_hotels["avg_nightly_rate"] > 200
        truth = condition.all()
        if truth:
            expl = f"All {len(phoenix_hotels)} Phoenix hotels have rates > $200."
        else:
            viol = phoenix_hotels[~condition]
            expl = f"{len(viol)} Phoenix hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one hotel in Dallas with a staff count less than 40 and a star level of 5."""
    dallas_five_stars = df[(df["city"] == "dallas") & (df["star_level"] == 5)]
    if dallas_five_stars.empty:
        truth = False
        expl = "No Dallas 5-star hotels found."
    else:
        condition = (dallas_five_stars["staff_count"] < 40)
        truth = condition.any()
        if truth:
            viol = dallas_five_stars[condition]
            expl = f"At least one Dallas 5-star hotel ({viol.iloc[0]['hotel_id']}) has staff < 40."
        else:
            expl = f"No Dallas 5-star hotels have staff < 40."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All hotels with an occupancy rate greater than 85% have a staff count less than 45."""
    high_occ_hotels = df[df["occupancy_rate"] > 85]
    if high_occ_hotels.empty:
        truth = True
        expl = "No hotels with occupancy > 85% found."
    else:
        condition = high_occ_hotels["staff_count"] < 45
        truth = condition.all()
        if truth:
            expl = f"All {len(high_occ_hotels)} hotels with occupancy > 85% have staff < 45."
        else:
            viol = high_occ_hotels[~condition]
            expl = f"{len(viol)} hotels with occupancy > 85% violate the rule (staff: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel has a star level of 3, then its average nightly rate is less than $170."""
    three_star_hotels = df[df["star_level"] == 3]
    if three_star_hotels.empty:
        truth = True
        expl = "No 3-star hotels found."
    else:
        condition = three_star_hotels["avg_nightly_rate"] < 170
        truth = condition.all()
        if truth:
            expl = f"All {len(three_star_hotels)} 3-star hotels have rates < $170."
        else:
            viol = three_star_hotels[~condition]
            expl = f"{len(viol)} 3-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most hotels in the dataset have an occupancy rate greater than 70%."""
    condition = df["occupancy_rate"] > 70
    total = len(df)
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} hotels have occupancy > 70% (more than half)."
    else:
        expl = f"{count} out of {total} hotels have occupancy > 70% (not more than half)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All hotels in Boston have a star level of 5."""
    boston_hotels = df[df["city"] == "boston"]
    if boston_hotels.empty:
        truth = True
        expl = "No hotels in Boston found."
    else:
        condition = boston_hotels["star_level"] == 5
        truth = condition.all()
        if truth:
            expl = f"All {len(boston_hotels)} Boston hotels have star level 5."
        else:
            viol = boston_hotels[~condition]
            expl = f"{len(viol)} Boston hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel is in Denver and has a star level of 3, then its occupancy rate is greater than 70%."""
    denver_three_stars = df[(df["city"] == "denver") & (df["star_level"] == 3)]
    if denver_three_stars.empty:
        truth = True
        expl = "No Denver 3-star hotels found."
    else:
        condition = denver_three_stars["occupancy_rate"] > 70
        truth = condition.all()
        if truth:
            expl = f"All {len(denver_three_stars)} Denver 3-star hotels have occupancy > 70%."
        else:
            viol = denver_three_stars[~condition]
            expl = f"{len(viol)} Denver 3-star hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one hotel in Chicago with a staff count less than 25 and a star level of 5."""
    chicago_five_stars = df[(df["city"] == "chicago") & (df["star_level"] == 5)]
    if chicago_five_stars.empty:
        truth = False
        expl = "No Chicago 5-star hotels found."
    else:
        condition = (chicago_five_stars["staff_count"] < 25)
        truth = condition.any()
        if truth:
            viol = chicago_five_stars[condition]
            expl = f"At least one Chicago 5-star hotel ({viol.iloc[0]['hotel_id']}) has staff < 25."
        else:
            expl = f"No Chicago 5-star hotels have staff < 25."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All hotels with a cancellation rate greater than 14% have an occupancy rate less than 80%."""
    high_cancel_hotels = df[df["cancellation_rate"] > 14]
    if high_cancel_hotels.empty:
        truth = True
        expl = "No hotels with cancellation rate > 14% found."
    else:
        condition = high_cancel_hotels["occupancy_rate"] < 80
        truth = condition.all()
        if truth:
            expl = f"All {len(high_cancel_hotels)} hotels with cancellation > 14% have occupancy < 80%."
        else:
            viol = high_cancel_hotels[~condition]
            expl = f"{len(viol)} hotels with cancellation > 14% violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel has an average nightly rate greater than $220, then its star level is 5 or 3."""
    high_rate_hotels = df[df["avg_nightly_rate"] > 220]
    if high_rate_hotels.empty:
        truth = True
        expl = "No hotels with rate > $220 found."
    else:
        condition = (high_rate_hotels["star_level"] == 5) | (high_rate_hotels["star_level"] == 3)
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rate_hotels)} hotels with rate > $220 have star level 3 or 5."
        else:
            viol = high_rate_hotels[~condition]
            expl = f"{len(viol)} hotels with rate > $220 violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most hotels in the dataset have a cancellation rate less than 15%."""
    condition = df["cancellation_rate"] < 15
    total = len(df)
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} hotels have cancellation < 15% (more than half)."
    else:
        expl = f"{count} out of {total} hotels have cancellation < 15% (not more than half)."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All hotels in Austin with a star level of 3 have an occupancy rate greater than 73%."""
    austin_three_stars = df[(df["city"] == "austin") & (df["star_level"] == 3)]
    if austin_three_stars.empty:
        truth = True
        expl = "No Austin 3-star hotels found."
    else:
        condition = austin_three_stars["occupancy_rate"] > 73
        truth = condition.all()
        if truth:
            expl = f"All {len(austin_three_stars)} Austin 3-star hotels have occupancy > 73%."
        else:
            viol = austin_three_stars[~condition]
            expl = f"{len(viol)} Austin 3-star hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a hotel is in Dallas and has a star level of 5, then its occupancy rate is greater than 75%."""
    dallas_five_stars = df[(df["city"] == "dallas") & (df["star_level"] == 5)]
    if dallas_five_stars.empty:
        truth = True
        expl = "No Dallas 5-star hotels found."
    else:
        condition = dallas_five_stars["occupancy_rate"] > 75
        truth = condition.all()
        if truth:
            expl = f"All {len(dallas_five_stars)} Dallas 5-star hotels have occupancy > 75%."
        else:
            viol = dallas_five_stars[~condition]
            expl = f"{len(viol)} Dallas 5-star hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one hotel in Portland with a staff count greater than 40 and a star level of 3."""
    portland_three_stars = df[(df["city"] == "portland") & (df["star_level"] == 3)]
    if portland_three_stars.empty:
        truth = False
        expl = "No Portland 3-star hotels found."
    else:
        condition = (portland_three_stars["staff_count"] > 40)
        truth = condition.any()
        if truth:
            viol = portland_three_stars[condition]
            expl = f"At least one Portland 3-star hotel ({viol.iloc[0]['hotel_id']}) has staff > 40."
        else:
            expl = f"No Portland 3-star hotels have staff > 40."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_35.csv")

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
        (19, stmt_19),
        (20, stmt_20),
        (21, stmt_21)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()