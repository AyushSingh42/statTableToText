import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Denver have an occupancy rate greater than 70%."""
    denver = df[df["city"].str.lower() == "denver"]
    if denver.empty:
        truth = True
        expl = "No hotels in Denver; statement vacuously true."
    else:
        condition = denver["occupancy_rate"] > 70
        truth = condition.all()
        if truth:
            expl = f"All {len(denver)} hotels in Denver have occupancy >70%."
        else:
            viol = denver[~condition]
            expl = f"{len(viol)} hotels in Denver violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Seattle, then its staff count is less than 35."""
    seattle = df[df["city"].str.lower() == "seattle"]
    if seattle.empty:
        truth = True
        expl = "No hotels in Seattle; statement vacuously true."
    else:
        condition = seattle["staff_count"] < 35
        truth = condition.all()
        if truth:
            expl = f"All {len(seattle)} hotels in Seattle have staff count <35."
        else:
            viol = seattle[~condition]
            expl = f"{len(viol)} hotels in Seattle violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hotels with an average nightly rate greater than $200 have a star level of 4."""
    high_rate = df[df["avg_nightly_rate"] > 200]
    if high_rate.empty:
        truth = True
        expl = "No hotels with avg nightly rate >200; statement vacuously true."
    else:
        condition = high_rate["star_level"] == 4
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rate)} hotels with avg nightly rate >200 have star level 4."
        else:
            viol = high_rate[~condition]
            expl = f"{len(viol)} hotels with avg nightly rate >200 violate the rule (star level: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one hotel in Austin with a star level of 5."""
    austin = df[df["city"].str.lower() == "austin"]
    exists = (austin["star_level"] == 5).any()
    if exists:
        count = austin[austin["star_level"] == 5].shape[0]
        expl = f"Found {count} hotel(s) in Austin with star level 5."
    else:
        expl = "No hotels in Austin with star level 5."
    return exists, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel is in Chicago, then its occupancy rate is greater than 68%."""
    chicago = df[df["city"].str.lower() == "chicago"]
    if chicago.empty:
        truth = True
        expl = "No hotels in Chicago; statement vacuously true."
    else:
        condition = chicago["occupancy_rate"] > 68
        truth = condition.all()
        if truth:
            expl = f"All {len(chicago)} hotels in Chicago have occupancy >68%."
        else:
            viol = chicago[~condition]
            expl = f"{len(viol)} hotels in Chicago violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with a cancellation rate less than 10% have a staff count greater than 35."""
    low_cancel = df[df["cancellation_rate"] < 10]
    if low_cancel.empty:
        truth = True
        expl = "No hotels with cancellation rate <10%; statement vacuously true."
    else:
        condition = low_cancel["staff_count"] > 35
        truth = condition.all()
        if truth:
            expl = f"All {len(low_cancel)} hotels with cancellation rate <10% have staff count >35."
        else:
            viol = low_cancel[~condition]
            expl = f"{len(viol)} hotels with cancellation rate <10% violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most hotels have an occupancy rate greater than 65%."""
    total = len(df)
    if total == 0:
        truth = True
        expl = "No hotels in dataset; statement vacuously true."
    else:
        count = (df["occupancy_rate"] > 65).sum()
        proportion = count / total
        truth = proportion > 0.5
        expl = f"{proportion*100:.1f}% of hotels have occupancy >65%."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Portland, then its average nightly rate is less than $200."""
    portland = df[df["city"].str.lower() == "portland"]
    if portland.empty:
        truth = True
        expl = "No hotels in Portland; statement vacuously true."
    else:
        condition = portland["avg_nightly_rate"] < 200
        truth = condition.all()
        if truth:
            expl = f"All {len(portland)} hotels in Portland have avg nightly rate <200."
        else:
            viol = portland[~condition]
            expl = f"{len(viol)} hotels in Portland violate the rule (avg nightly rate: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All hotels with a bookings month greater than 850 have a star level of 4."""
    high_bookings = df[df["bookings_month"] > 850]
    if high_bookings.empty:
        truth = True
        expl = "No hotels with bookings month >850; statement vacuously true."
    else:
        condition = high_bookings["star_level"] == 4
        truth = condition.all()
        if truth:
            expl = f"All {len(high_bookings)} hotels with bookings month >850 have star level 4."
        else:
            viol = high_bookings[~condition]
            expl = f"{len(viol)} hotels with bookings month >850 violate the rule (star level: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one hotel in Dallas with an occupancy rate greater than 85%."""
    dallas = df[df["city"].str.lower() == "dallas"]
    exists = (dallas["occupancy_rate"] > 85).any()
    if exists:
        count = dallas[dallas["occupancy_rate"] > 85].shape[0]
        expl = f"Found {count} hotel(s) in Dallas with occupancy >85%."
    else:
        expl = "No hotels in Dallas with occupancy >85%."
    return exists, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel is in Miami, then its staff count is less than 30."""
    miami = df[df["city"].str.lower() == "miami"]
    if miami.empty:
        truth = True
        expl = "No hotels in Miami; statement vacuously true."
    else:
        condition = miami["staff_count"] < 30
        truth = condition.all()
        if truth:
            expl = f"All {len(miami)} hotels in Miami have staff count <30."
        else:
            viol = miami[~condition]
            expl = f"{len(viol)} hotels in Miami violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels with a star level of 3 have an average nightly rate less than $220."""
    star3 = df[df["star_level"] == 3]
    if star3.empty:
        truth = True
        expl = "No hotels with star level 3; statement vacuously true."
    else:
        condition = star3["avg_nightly_rate"] < 220
        truth = condition.all()
        if truth:
            expl = f"All {len(star3)} hotels with star level 3 have avg nightly rate <220."
        else:
            viol = star3[~condition]
            expl = f"{len(viol)} hotels with star level 3 violate the rule (avg nightly rate: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most hotels have a staff count less than 40."""
    total = len(df)
    if total == 0:
        truth = True
        expl = "No hotels in dataset; statement vacuously true."
    else:
        count = (df["staff_count"] < 40).sum()
        proportion = count / total
        truth = proportion > 0.5
        expl = f"{proportion*100:.1f}% of hotels have staff count <40."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel is in Austin, then its occupancy rate is greater than 65%."""
    austin = df[df["city"].str.lower() == "austin"]
    if austin.empty:
        truth = True
        expl = "No hotels in Austin; statement vacuously true."
    else:
        condition = austin["occupancy_rate"] > 65
        truth = condition.all()
        if truth:
            expl = f"All {len(austin)} hotels in Austin have occupancy >65%."
        else:
            viol = austin[~condition]
            expl = f"{len(viol)} hotels in Austin violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All hotels with an occupancy rate greater than 80% have a star level of 4 or 5."""
    high_occ = df[df["occupancy_rate"] > 80]
    if high_occ.empty:
        truth = True
        expl = "No hotels with occupancy >80%; statement vacuously true."
    else:
        condition = high_occ["star_level"].isin([4, 5])
        truth = condition.all()
        if truth:
            expl = f"All {len(high_occ)} hotels with occupancy >80% have star level 4 or 5."
        else:
            viol = high_occ[~condition]
            expl = f"{len(viol)} hotels with occupancy >80% violate the rule (star level: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one hotel in Phoenix with an occupancy rate greater than 85%."""
    phoenix = df[df["city"].str.lower() == "phoenix"]
    exists = (phoenix["occupancy_rate"] > 85).any()
    if exists:
        count = phoenix[phoenix["occupancy_rate"] > 85].shape[0]
        expl = f"Found {count} hotel(s) in Phoenix with occupancy >85%."
    else:
        expl = "No hotels in Phoenix with occupancy >85%."
    return exists, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel is in Boston, then its staff count is greater than 35."""
    boston = df[df["city"].str.lower() == "boston"]
    if boston.empty:
        truth = True
        expl = "No hotels in Boston; statement vacuously true."
    else:
        condition = boston["staff_count"] > 35
        truth = condition.all()
        if truth:
            expl = f"All {len(boston)} hotels in Boston have staff count >35."
        else:
            viol = boston[~condition]
            expl = f"{len(viol)} hotels in Boston violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All hotels with a bookings month less than 700 have a star level of 3."""
    low_bookings = df[df["bookings_month"] < 700]
    if low_bookings.empty:
        truth = True
        expl = "No hotels with bookings month <700; statement vacuously true."
    else:
        condition = low_bookings["star_level"] == 3
        truth = condition.all()
        if truth:
            expl = f"All {len(low_bookings)} hotels with bookings month <700 have star level 3."
        else:
            viol = low_bookings[~condition]
            expl = f"{len(viol)} hotels with bookings month <700 violate the rule (star level: {', '.join(map(str, viol