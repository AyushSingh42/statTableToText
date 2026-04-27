import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Phoenix have an occupancy rate greater than 70%."""
    phx = df[df["city"].str.lower() == "phoenix"]
    if phx.empty:
        truth = True
        expl = "No hotels in Phoenix, statement vacuously true."
    else:
        cond = phx["occupancy_rate"] > 70
        truth = cond.all()
        if truth:
            expl = f"All {len(phx)} hotels in Phoenix have occupancy >70%."
        else:
            viol = phx[~cond]
            expl = f"{len(viol)} hotels in Phoenix violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Phoenix, then its cancellation rate is less than 15%."""
    phx = df[df["city"].str.lower() == "phoenix"]
    if phx.empty:
        truth = True
        expl = "No hotels in Phoenix, statement vacuously true."
    else:
        cond = phx["cancellation_rate"] < 15
        truth = cond.all()
        if truth:
            expl = f"All {len(phx)} hotels in Phoenix have cancellation rate <15%."
        else:
            viol = phx[~cond]
            expl = f"{len(viol)} hotels in Phoenix violate the rule (cancellation: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one hotel in Miami with a star level of 3."""
    miami = df[(df["city"].str.lower() == "miami") & (df["star_level"] == 3)]
    truth = not miami.empty
    if truth:
        ids = miami["hotel_id"].tolist()
        expl = f"Found {len(ids)} hotel(s) in Miami with star level 3: {', '.join(ids)}."
    else:
        expl = "No hotel in Miami has star level 3."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with an average nightly rate greater than $200 have a staff count greater than 30."""
    high_rate = df[df["avg_nightly_rate"] > 200]
    if high_rate.empty:
        truth = True
        expl = "No hotels with avg nightly rate >$200, statement vacuously true."
    else:
        cond = high_rate["staff_count"] > 30
        truth = cond.all()
        if truth:
            expl = f"All {len(high_rate)} hotels with avg nightly rate >$200 have staff count >30."
        else:
            viol = high_rate[~cond]
            expl = f"{len(viol)} hotels with avg nightly rate >$200 violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel is in Austin, then its occupancy rate is greater than 65%."""
    austin = df[df["city"].str.lower() == "austin"]
    if austin.empty:
        truth = True
        expl = "No hotels in Austin, statement vacuously true."
    else:
        cond = austin["occupancy_rate"] > 65
        truth = cond.all()
        if truth:
            expl = f"All {len(austin)} hotels in Austin have occupancy rate >65%."
        else:
            viol = austin[~cond]
            expl = f"{len(viol)} hotels in Austin violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most hotels have an occupancy rate greater than 70%."""
    total = len(df)
    if total == 0:
        truth = True
        expl = "No hotels in dataset, statement vacuously true."
    else:
        count = (df["occupancy_rate"] > 70).sum()
        proportion = count / total
        truth = proportion > 0.5
        percent = round(proportion * 100, 1)
        if truth:
            expl = f"{count} out of {total} hotels have occupancy >70% ({percent}%)."
        else:
            expl = f"Only {count} out of {total} hotels have occupancy >70% ({percent}%)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels with a star level of 5 have an occupancy rate greater than 80%."""
    five_star = df[df["star_level"] == 5]
    if five_star.empty:
        truth = True
        expl = "No star level 5 hotels, statement vacuously true."
    else:
        cond = five_star["occupancy_rate"] > 80
        truth = cond.all()
        if truth:
            expl = f"All {len(five_star)} star level 5 hotels have occupancy >80%."
        else:
            viol = five_star[~cond]
            expl = f"{len(viol)} star level 5 hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Chicago, then its average nightly rate is less than $150."""
    chicago = df[df["city"].str.lower() == "chicago"]
    if chicago.empty:
        truth = True
        expl = "No hotels in Chicago, statement vacuously true."
    else:
        cond = chicago["avg_nightly_rate"] < 150
        truth = cond.all()
        if truth:
            expl = f"All {len(chicago)} hotels in Chicago have avg nightly rate <150."
        else:
            viol = chicago[~cond]
            expl = f"{len(viol)} hotels in Chicago violate the rule (avg nightly rate: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one hotel in Portland with a staff count greater than 35."""
    portland = df[(df["city"].str.lower() == "portland") & (df["staff_count"] > 35)]
    truth = not portland.empty
    if truth:
        ids = portland["hotel_id"].tolist()
        expl = f"Found {len(ids)} hotel(s) in Portland with staff count >35: {', '.join(ids)}."
    else:
        expl = "No hotel in Portland has staff count >35."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All hotels with a cancellation rate less than 10% have an occupancy rate greater than 75%."""
    low_cancel = df[df["cancellation_rate"] < 10]
    if low_cancel.empty:
        truth = True
        expl = "No hotels with cancellation rate <10%, statement vacuously true."
    else:
        cond = low_cancel["occupancy_rate"] > 75
        truth = cond.all()
        if truth:
            expl = f"All {len(low_cancel)} hotels with cancellation rate <10% have occupancy >75%."
        else:
            viol = low_cancel[~cond]
            expl = f"{len(viol)} hotels with cancellation rate <10% violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel is in Seattle, then its staff count is less than 30."""
    seattle = df[df["city"].str.lower() == "seattle"]
    if seattle.empty:
        truth = True
        expl = "No hotels in Seattle, statement vacuously true."
    else:
        cond = seattle["staff_count"] < 30
        truth = cond.all()
        if truth:
            expl = f"All {len(seattle)} hotels in Seattle have staff count <30."
        else:
            viol = seattle[~cond]
            expl = f"{len(viol)} hotels in Seattle violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels with an average nightly rate less than $120 have a star level of 3."""
    low_rate = df[df["avg_nightly_rate"] < 120]
    if low_rate.empty:
        truth = True
        expl = "No hotels with avg nightly rate <120, statement vacuously true."
    else:
        cond = low_rate["star_level"] == 3
        truth = cond.all()
        if truth:
            expl = f"All {len(low_rate)} hotels with avg nightly rate <120 have star level 3."
        else:
            viol = low_rate[~cond]
            expl = f"{len(viol)} hotels with avg nightly rate <120 violate the rule (star level: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most hotels in Phoenix have a staff count greater than 30."""
    phx = df[df["city"].str.lower() == "phoenix"]
    total = len(phx)
    if total == 0:
        truth = True
        expl = "No hotels in Phoenix, statement vacuously true."
    else:
        count = (phx["staff_count"] > 30).sum()
        proportion = count / total
        truth = proportion > 0.5
        percent = round(proportion * 100, 1)
        if truth:
            expl = f"{count} out of {total} Phoenix hotels have staff count >30 ({percent}%)."
        else:
            expl = f"Only {count} out of {total} Phoenix hotels have staff count >30 ({percent}%)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel is in Atlanta, then its occupancy rate is less than 70%."""
    atlanta = df[df["city"].str.lower() == "atlanta"]
    if atlanta.empty:
        truth = True
        expl = "No hotels in Atlanta, statement vacuously true."
    else:
        cond = atlanta["occupancy_rate"] < 70
        truth = cond.all()
        if truth:
            expl = f"All {len(atlanta)} hotels in Atlanta have occupancy rate <70%."
        else:
            viol = atlanta[~cond]
            expl = f"{len(viol)} hotels in Atlanta violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one hotel in Austin with a star level of 5."""
    austin5 = df[(df["city"].str.lower() == "austin") & (df["star_level"] == 5)]
    truth = not austin5.empty
    if truth:
        ids = austin5["hotel_id"].tolist()
        expl = f"Found {len(ids)} hotel(s) in Austin with star level 5: {', '.join(ids)}."
    else:
        expl = "No hotel in Austin has star level 5."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All hotels with a staff count greater than 40 have an occupancy rate greater than 80%."""
    high_staff = df[df["staff_count"] > 40]
    if high_staff.empty:
        truth = True
        expl = "No hotels with staff count >40, statement vacuously true."
    else:
        cond = high_staff["occupancy_rate"] > 80
        truth = cond.all()
        if truth:
            expl = f"All {len(high_staff)} hotels with staff count >40 have occupancy >80%."
        else:
            viol = high_staff[~cond]
            expl = f"{len(viol)} hotels with staff count >40 violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel is in Denver, then its average nightly rate is greater than $180."""
    denver = df[df["city"].str.lower() == "denver"]
    if denver.empty:
        truth = True
        expl = "No hotels in Denver, statement vacuously true."
    else:
        cond = denver["avg_nightly_rate"] > 180
        truth = cond.all()
        if truth:
            expl = f"All {len(denver)} hotels in Denver have avg nightly rate >180."
        else:
            viol = denver[~cond]
            expl = f"{len(viol)} hotels in Denver violate the rule (avg nightly rate: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All hotels with a cancellation rate greater than 12% have a staff count greater than 25."""
    high_cancel = df[df["cancellation_rate"] > 12]
    if high_cancel.empty:
        truth = True
        expl = "No hotels with cancellation rate >12%, statement vacuously true."
    else:
        cond = high_cancel["staff_count"] > 25
        truth = cond.all()
        if truth:
            expl = f"All {len(high_cancel)} hotels with cancellation rate >12% have staff count >25."
        else:
            viol = high_cancel[~cond]
            expl = f"{len(viol)} hotels with cancellation rate >12% violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. Most hotels have a staff count greater than 25."""
    total = len(df)
    if total == 0:
        truth = True
        expl = "No hotels in dataset, statement vacuously true."
    else:
        count = (df["staff_count"] > 25).sum()
        proportion = count / total
        truth = proportion > 0.5
        percent = round(proportion * 100, 1)
        if truth:
            expl = f"{count} out of {total} hotels have staff count >25 ({percent}%)."
        else:
            expl = f"Only {count} out of {total} hotels have staff count >25 ({percent}%)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_85.csv")

    # Convert numeric columns
    numeric_cols = ["occupancy_rate", "avg_nightly_rate", "bookings_month",
                    "cancellation_rate", "staff_count", "star_level"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

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