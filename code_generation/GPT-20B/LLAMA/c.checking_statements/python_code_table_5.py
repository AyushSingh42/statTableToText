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
        return True, "No Phoenix hotels to evaluate."
    cond = phx["occupancy_rate"] > 70
    truth = cond.all()
    if truth:
        expl = f"All {len(phx)} Phoenix hotels have occupancy > 70%."
    else:
        viol = phx[~cond]
        expl = f"{len(viol)} Phoenix hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Atlanta, then its cancellation rate is greater than 10%."""
    atl = df[df["city"].str.lower() == "atlanta"]
    if atl.empty:
        return True, "No Atlanta hotels to evaluate."
    cond = atl["cancellation_rate"] > 10
    truth = cond.all()
    if truth:
        expl = f"All {len(atl)} Atlanta hotels have cancellation rate > 10%."
    else:
        viol = atl[~cond]
        expl = f"{len(viol)} Atlanta hotels violate the rule (cancellation: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hotels with a star level of 5 have an occupancy rate greater than 80%."""
    five_star = df[df["star_level"] == 5]
    if five_star.empty:
        return True, "No star level 5 hotels to evaluate."
    cond = five_star["occupancy_rate"] > 80
    truth = cond.all()
    if truth:
        expl = f"All {len(five_star)} star 5 hotels have occupancy > 80%."
    else:
        viol = five_star[~cond]
        expl = f"{len(viol)} star 5 hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one hotel in Chicago with a staff count greater than 40."""
    chicago = df[df["city"].str.lower() == "chicago"]
    exists = (chicago["staff_count"] > 40).any()
    if exists:
        expl = f"At least one Chicago hotel has staff count > 40."
    else:
        expl = "No Chicago hotel has staff count > 40."
    return exists, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel has a star level of 4, then its average nightly rate is less than $220."""
    four_star = df[df["star_level"] == 4]
    if four_star.empty:
        return True, "No star level 4 hotels to evaluate."
    cond = four_star["avg_nightly_rate"] < 220
    truth = cond.all()
    if truth:
        expl = f"All {len(four_star)} star 4 hotels have avg nightly rate < $220."
    else:
        viol = four_star[~cond]
        expl = f"{len(viol)} star 4 hotels violate the rule (avg rate: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with a bookings month greater than 900 have a staff count greater than 30."""
    high_book = df[df["bookings_month"] > 900]
    if high_book.empty:
        return True, "No hotels with bookings month > 900 to evaluate."
    cond = high_book["staff_count"] > 30
    truth = cond.all()
    if truth:
        expl = f"All {len(high_book)} hotels with bookings month > 900 have staff count > 30."
    else:
        viol = high_book[~cond]
        expl = f"{len(viol)} hotels violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most hotels in the dataset have an occupancy rate greater than 70%."""
    total = len(df)
    if total == 0:
        return True, "No hotels in dataset."
    count = (df["occupancy_rate"] > 70).sum()
    proportion = count / total
    truth = proportion > 0.5
    expl = f"{proportion*100:.1f}% of hotels have occupancy > 70% (threshold 50%)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Denver, then its average nightly rate is greater than $140."""
    den = df[df["city"].str.lower() == "denver"]
    if den.empty:
        return True, "No Denver hotels to evaluate."
    cond = den["avg_nightly_rate"] > 140
    truth = cond.all()
    if truth:
        expl = f"All {len(den)} Denver hotels have avg nightly rate > $140."
    else:
        viol = den[~cond]
        expl = f"{len(viol)} Denver hotels violate the rule (avg rate: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All hotels with a star level of 3 have a staff count less than 45."""
    three_star = df[df["star_level"] == 3]
    if three_star.empty:
        return True, "No star level 3 hotels to evaluate."
    cond = three_star["staff_count"] < 45
    truth = cond.all()
    if truth:
        expl = f"All {len(three_star)} star 3 hotels have staff count < 45."
    else:
        viol = three_star[~cond]
        expl = f"{len(viol)} star 3 hotels violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one hotel in Atlanta with a star level of 5 and an occupancy rate greater than 85%."""
    atl = df[(df["city"].str.lower() == "atlanta") & (df["star_level"] == 5) & (df["occupancy_rate"] > 85)]
    exists = not atl.empty
    if exists:
        expl = f"At least one Atlanta hotel meets the criteria."
    else:
        expl = "No Atlanta hotel meets the criteria."
    return exists, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel has a staff count greater than 40, then its star level is 5."""
    high_staff = df[df["staff_count"] > 40]
    if high_staff.empty:
        return True, "No hotels with staff count > 40 to evaluate."
    cond = high_staff["star_level"] == 5
    truth = cond.all()
    if truth:
        expl = f"All {len(high_staff)} hotels with staff count > 40 have star level 5."
    else:
        viol = high_staff[~cond]
        expl = f"{len(viol)} hotels violate the rule (star level: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels in Boston have a star level of 4."""
    bos = df[df["city"].str.lower() == "boston"]
    if bos.empty:
        return True, "No Boston hotels to evaluate."
    cond = bos["star_level"] == 4
    truth = cond.all()
    if truth:
        expl = f"All {len(bos)} Boston hotels have star level 4."
    else:
        viol = bos[~cond]
        expl = f"{len(viol)} Boston hotels violate the rule (star level: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a hotel is in Phoenix, then its cancellation rate is less than 15%."""
    phx = df[df["city"].str.lower() == "phoenix"]
    if phx.empty:
        return True, "No Phoenix hotels to evaluate."
    cond = phx["cancellation_rate"] < 15
    truth = cond.all()
    if truth:
        expl = f"All {len(phx)} Phoenix hotels have cancellation rate < 15%."
    else:
        viol = phx[~cond]
        expl = f"{len(viol)} Phoenix hotels violate the rule (cancellation: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All hotels with an occupancy rate greater than 85% have a star level of 5."""
    high_occ = df[df["occupancy_rate"] > 85]
    if high_occ.empty:
        return True, "No hotels with occupancy > 85% to evaluate."
    cond = high_occ["star_level"] == 5
    truth = cond.all()
    if truth:
        expl = f"All {len(high_occ)} hotels with occupancy > 85% have star level 5."
    else:
        viol = high_occ[~cond]
        expl = f"{len(viol)} hotels violate the rule (star level: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most hotels in the dataset have a staff count greater than 30."""
    total = len(df)
    if total == 0:
        return True, "No hotels in dataset."
    count = (df["staff_count"] > 30).sum()
    proportion = count / total
    truth = proportion > 0.5
    expl = f"{proportion*100:.1f}% of hotels have staff count > 30 (threshold 50%)."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a hotel has a bookings month greater than 800, then its occupancy rate is greater than 70%."""
    high_book = df[df["bookings_month"] > 800]
    if high_book.empty:
        return True, "No hotels with bookings month > 800 to evaluate."
    cond = high_book["occupancy_rate"] > 70
    truth = cond.all()
    if truth:
        expl = f"All {len(high_book)} hotels with bookings month > 800 have occupancy > 70%."
    else:
        viol = high_book[~cond]
        expl = f"{len(viol)} hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. There exists at least one hotel in Chicago with a star level of 5 and an occupancy rate greater than 80%."""
    chicago = df[(df["city"].str.lower() == "chicago") & (df["star_level"] == 5) & (df["occupancy_rate"] > 80)]
    exists = not chicago.empty
    if exists:
        expl = f"At least one Chicago hotel meets the criteria."
    else:
        expl = "No Chicago hotel meets the criteria."
    return exists, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_5.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()