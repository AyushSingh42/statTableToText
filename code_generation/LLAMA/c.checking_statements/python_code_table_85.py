import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Phoenix have an occupancy rate greater than 70%."""
    phx_hotels = df[df["city"] == "phoenix"]
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
    """2. If a hotel is in Phoenix, then its cancellation rate is less than 15%."""
    phx_hotels = df[df["city"] == "phoenix"]
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

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one hotel in Miami with a star level of 3."""
    miami_hotels = df[(df["city"] == "miami") & (df["star_level"] == 3)]
    truth = not miami_hotels.empty
    if truth:
        expl = f"Found {len(miami_hotels)} Miami hotel(s) with star level 3."
    else:
        expl = "No Miami hotel found with star level 3."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with an average nightly rate greater than $200 have a staff count greater than 30."""
    high_rate_hotels = df[df["avg_nightly_rate"] > 200]
    if high_rate_hotels.empty:
        truth = True
        expl = "No hotels with avg nightly rate > $200 found."
    else:
        condition = high_rate_hotels["staff_count"] > 30
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rate_hotels)} high-rate hotels have staff count > 30."
        else:
            viol = high_rate_hotels[~condition]
            expl = f"{len(viol)} high-rate hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel is in Austin, then its occupancy rate is greater than 65%."""
    austin_hotels = df[df["city"] == "austin"]
    if austin_hotels.empty:
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

def stmt_6(df: pd.DataFrame):
    """6. Most hotels have an occupancy rate greater than 70%."""
    total_hotels = len(df)
    high_occupancy = df[df["occupancy_rate"] > 70]
    proportion = len(high_occupancy) / total_hotels if total_hotels > 0 else 0
    truth = proportion > 0.5
    expl = f"{len(high_occupancy)} out of {total_hotels} hotels have occupancy > 70%. Proportion: {proportion:.2%}."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels with a star level of 5 have an occupancy rate greater than 80%."""
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

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Chicago, then its average nightly rate is less than $150."""
    chicago_hotels = df[df["city"] == "chicago"]
    if chicago_hotels.empty:
        truth = True
        expl = "No hotels in Chicago found."
    else:
        condition = chicago_hotels["avg_nightly_rate"] < 150
        truth = condition.all()
        if truth:
            expl = f"All {len(chicago_hotels)} Chicago hotels have avg nightly rate < $150."
        else:
            viol = chicago_hotels[~condition]
            expl = f"{len(viol)} Chicago hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one hotel in Portland with a staff count greater than 35."""
    portland_hotels = df[(df["city"] == "portland") & (df["staff_count"] > 35)]
    truth = not portland_hotels.empty
    if truth:
        expl = f"Found {len(portland_hotels)} Portland hotel(s) with staff count > 35."
    else:
        expl = "No Portland hotel found with staff count > 35."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All hotels with a cancellation rate less than 10% have an occupancy rate greater than 75%."""
    low_cancel_hotels = df[df["cancellation_rate"] < 10]
    if low_cancel_hotels.empty:
        truth = True
        expl = "No hotels with cancellation rate < 10% found."
    else:
        condition = low_cancel_hotels["occupancy_rate"] > 75
        truth = condition.all()
        if truth:
            expl = f"All {len(low_cancel_hotels)} low-cancellation hotels have occupancy > 75%."
        else:
            viol = low_cancel_hotels[~condition]
            expl = f"{len(viol)} low-cancellation hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel is in Seattle, then its staff count is less than 30."""
    seattle_hotels = df[df["city"] == "seattle"]
    if seattle_hotels.empty:
        truth = True
        expl = "No hotels in Seattle found."
    else:
        condition = seattle_hotels["staff_count"] < 30
        truth = condition.all()
        if truth:
            expl = f"All {len(seattle_hotels)} Seattle hotels have staff count < 30."
        else:
            viol = seattle_hotels[~condition]
            expl = f"{len(viol)} Seattle hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels with an average nightly rate less than $120 have a star level of 3."""
    low_rate_hotels = df[df["avg_nightly_rate"] < 120]
    if low_rate_hotels.empty:
        truth = True
        expl = "No hotels with avg nightly rate < $120 found."
    else:
        condition = low_rate_hotels["star_level"] == 3
        truth = condition.all()
        if truth:
            expl = f"All {len(low_rate_hotels)} low-rate hotels have star level 3."
        else:
            viol = low_rate_hotels[~condition]
            expl = f"{len(viol)} low-rate hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most hotels in Phoenix have a staff count greater than 30."""
    phx_hotels = df[df["city"] == "phoenix"]
    if phx_hotels.empty:
        truth = True
        expl = "No hotels in Phoenix found."
    else:
        high_staff_phx = phx_hotels[phx_hotels["staff_count"] > 30]
        proportion = len(high_staff_phx) / len(phx_hotels) if len(phx_hotels) > 0 else 0
        truth = proportion > 0.5
        expl = f"{len(high_staff_phx)} out of {len(phx_hotels)} Phoenix hotels have staff count > 30. Proportion: {proportion:.2%}."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel is in Atlanta, then its occupancy rate is less than 70%."""
    atlanta_hotels = df[df["city"] == "atlanta"]
    if atlanta_hotels.empty:
        truth = True
        expl = "No hotels in Atlanta found."
    else:
        condition = atlanta_hotels["occupancy_rate"] < 70
        truth = condition.all()
        if truth:
            expl = f"All {len(atlanta_hotels)} Atlanta hotels have occupancy < 70%."
        else:
            viol = atlanta_hotels[~condition]
            expl = f"{len(viol)} Atlanta hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one hotel in Austin with a star level of 5."""
    austin_hotels = df[(df["city"] == "austin") & (df["star_level"] == 5)]
    truth = not austin_hotels.empty
    if truth:
        expl = f"Found {len(austin_hotels)} Austin hotel(s) with star level 5."
    else:
        expl = "No Austin hotel found with star level 5."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All hotels with a staff count greater than 40 have an occupancy rate greater than 80%."""
    high_staff_hotels = df[df["staff_count"] > 40]
    if high_staff_hotels.empty:
        truth = True
        expl = "No hotels with staff count > 40 found."
    else:
        condition = high_staff_hotels["occupancy_rate"] > 80
        truth = condition.all()
        if truth:
            expl = f"All {len(high_staff_hotels)} high-staff hotels have occupancy > 80%."
        else:
            viol = high_staff_hotels[~condition]
            expl = f"{len(viol)} high-staff hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel is in Denver, then its average nightly rate is greater than $180."""
    denver_hotels = df[df["city"] == "denver"]
    if denver_hotels.empty:
        truth = True
        expl = "No hotels in Denver found."
    else:
        condition = denver_hotels["avg_nightly_rate"] > 180
        truth = condition.all()
        if truth:
            expl = f"All {len(denver_hotels)} Denver hotels have avg nightly rate > $180."
        else:
            viol = denver_hotels[~condition]
            expl = f"{len(viol)} Denver hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All hotels with a cancellation rate greater than 12% have a staff count greater than 25."""
    high_cancel_hotels = df[df["cancellation_rate"] > 12]
    if high_cancel_hotels.empty:
        truth = True
        expl = "No hotels with cancellation rate > 12% found."
    else:
        condition = high_cancel_hotels["staff_count"] > 25
        truth = condition.all()
        if truth:
            expl = f"All {len(high_cancel_hotels)} high-cancellation hotels have staff count > 25."
        else:
            viol = high_cancel_hotels[~condition]
            expl = f"{len(viol)} high-cancellation hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. Most hotels have a staff count greater than 25."""
    total_hotels = len(df)
    high_staff_hotels = df[df["staff_count"] > 25]
    proportion = len(high_staff_hotels) / total_hotels if total_hotels > 0 else 0
    truth = proportion > 0.5
    expl = f"{len(high_staff_hotels)} out of {total_hotels} hotels have staff count > 25. Proportion: {proportion:.2%}."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_85.csv")

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