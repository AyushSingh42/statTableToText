import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Austin have an average nightly rate greater than $120."""
    austin = df[df["city"] == "austin"]
    if austin.empty:
        truth = True
        expl = "No Austin hotels in data; vacuously true."
    else:
        condition = austin["avg_nightly_rate"] > 120
        truth = condition.all()
        if truth:
            expl = f"All {len(austin)} Austin hotels have avg nightly rate > $120."
        else:
            viol = austin[~condition]
            expl = f"{len(viol)} Austin hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Boston, then its occupancy rate is greater than 69%."""
    boston = df[df["city"] == "boston"]
    if boston.empty:
        truth = True
        expl = "No Boston hotels in data; vacuously true."
    else:
        condition = boston["occupancy_rate"] > 69
        truth = condition.all()
        if truth:
            expl = f"All {len(boston)} Boston hotels have occupancy rate > 69%."
        else:
            viol = boston[~condition]
            expl = f"{len(viol)} Boston hotels violate the rule (rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one hotel in Phoenix with a cancellation rate less than 9%."""
    phoenix = df[(df["city"] == "phoenix") & (df["cancellation_rate"] < 9)]
    truth = not phoenix.empty
    if truth:
        expl = f"Found {len(phoenix)} Phoenix hotel(s) with cancellation rate < 9%."
    else:
        expl = "No Phoenix hotel with cancellation rate < 9% found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with a staff count greater than 35 have a star level of 5."""
    staff_gt_35 = df[df["staff_count"] > 35]
    if staff_gt_35.empty:
        truth = True
        expl = "No hotels with staff count > 35; vacuously true."
    else:
        condition = staff_gt_35["star_level"] == 5
        truth = condition.all()
        if truth:
            expl = f"All {len(staff_gt_35)} hotels with staff > 35 have star level 5."
        else:
            viol = staff_gt_35[~condition]
            expl = f"{len(viol)} hotels with staff > 35 violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel is in Dallas, then its average nightly rate is less than $210."""
    dallas = df[df["city"] == "dallas"]
    if dallas.empty:
        truth = True
        expl = "No Dallas hotels in data; vacuously true."
    else:
        condition = dallas["avg_nightly_rate"] < 210
        truth = condition.all()
        if truth:
            expl = f"All {len(dallas)} Dallas hotels have avg nightly rate < $210."
        else:
            viol = dallas[~condition]
            expl = f"{len(viol)} Dallas hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most hotels have an occupancy rate greater than 70%."""
    total = len(df)
    count = (df["occupancy_rate"] > 70).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} hotels have occupancy rate > 70%."
    else:
        expl = f"Only {count} out of {total} hotels have occupancy rate > 70%."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels with a star level of 3 have an average nightly rate less than $185."""
    star3 = df[df["star_level"] == 3]
    if star3.empty:
        truth = True
        expl = "No star level 3 hotels; vacuously true."
    else:
        condition = star3["avg_nightly_rate"] < 185
        truth = condition.all()
        if truth:
            expl = f"All {len(star3)} star level 3 hotels have avg nightly rate < $185."
        else:
            viol = star3[~condition]
            expl = f"{len(viol)} star level 3 hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel has a bookings month greater than 800, then its cancellation rate is less than 12%."""
    bm_gt_800 = df[df["bookings_month"] > 800]
    if bm_gt_800.empty:
        truth = True
        expl = "No hotels with bookings month > 800; vacuously true."
    else:
        condition = bm_gt_800["cancellation_rate"] < 12
        truth = condition.all()
        if truth:
            expl = f"All {len(bm_gt_800)} hotels with bookings month > 800 have cancellation rate < 12%."
        else:
            viol = bm_gt_800[~condition]
            expl = f"{len(viol)} hotels with bookings month > 800 violate the rule (rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one hotel in Seattle with a staff count less than 25."""
    seattle = df[(df["city"] == "seattle") & (df["staff_count"] < 25)]
    truth = not seattle.empty
    if truth:
        expl = f"Found {len(seattle)} Seattle hotel(s) with staff count < 25."
    else:
        expl = "No Seattle hotel with staff count < 25 found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All hotels with an occupancy rate greater than 85% have a star level of 4 or 5."""
    occ_gt_85 = df[df["occupancy_rate"] > 85]
    if occ_gt_85.empty:
        truth = True
        expl = "No hotels with occupancy rate > 85%; vacuously true."
    else:
        condition = occ_gt_85["star_level"].isin([4,5])
        truth = condition.all()
        if truth:
            expl = f"All {len(occ_gt_85)} hotels with occupancy rate > 85% have star level 4 or 5."
        else:
            viol = occ_gt_85[~condition]
            expl = f"{len(viol)} hotels with occupancy rate > 85% violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel is in Atlanta, then its average nightly rate is less than $185."""
    atlanta = df[df["city"] == "atlanta"]
    if atlanta.empty:
        truth = True
        expl = "No Atlanta hotels in data; vacuously true."
    else:
        condition = atlanta["avg_nightly_rate"] < 185
        truth = condition.all()
        if truth:
            expl = f"All {len(atlanta)} Atlanta hotels have avg nightly rate < $185."
        else:
            viol = atlanta[~condition]
            expl = f"{len(viol)} Atlanta hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most hotels have a bookings month greater than 700."""
    total = len(df)
    count = (df["bookings_month"] > 700).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} hotels have bookings month > 700."
    else:
        expl = f"Only {count} out of {total} hotels have bookings month > 700."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All hotels with a star level of 5 have an average nightly rate greater than $138."""
    star5 = df[df["star_level"] == 5]
    if star5.empty:
        truth = True
        expl = "No star level 5 hotels; vacuously true."
    else:
        condition = star5["avg_nightly_rate"] > 138
        truth = condition.all()
        if truth:
            expl = f"All {len(star5)} star level 5 hotels have avg nightly rate > $138."
        else:
            viol = star5[~condition]
            expl = f"{len(viol)} star level 5 hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel has a cancellation rate less than 10%, then its staff count is less than 38."""
    cr_lt_10 = df[df["cancellation_rate"] < 10]
    if cr_lt_10.empty:
        truth = True
        expl = "No hotels with cancellation rate < 10%; vacuously true."
    else:
        condition = cr_lt_10["staff_count"] < 38
        truth = condition.all()
        if truth:
            expl = f"All {len(cr_lt_10)} hotels with cancellation rate < 10% have staff count < 38."
        else:
            viol = cr_lt_10[~condition]
            expl = f"{len(viol)} hotels with cancellation rate < 10% violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one hotel in Austin with an occupancy rate greater than 85%."""
    austin_gt_85 = df[(df["city"] == "austin") & (df["occupancy_rate"] > 85)]
    truth = not austin_gt_85.empty
    if truth:
        expl = f"Found {len(austin_gt_85)} Austin hotel(s) with occupancy rate > 85%."
    else:
        expl = "No Austin hotel with occupancy rate > 85% found."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All hotels with a staff count greater than 40 have an occupancy rate greater than 78%."""
    staff_gt_40 = df[df["staff_count"] > 40]
    if staff_gt_40.empty:
        truth = True
        expl = "No hotels with staff count > 40; vacuously true."
    else:
        condition = staff_gt_40["occupancy_rate"] > 78
        truth = condition.all()
        if truth:
            expl = f"All {len(staff_gt_40)} hotels with staff > 40 have occupancy rate > 78%."
        else:
            viol = staff_gt_40[~condition]
            expl = f"{len(viol)} hotels with staff > 40 violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel is in Chicago, then its average nightly rate is greater than $200."""
    chicago = df[df["city"] == "chicago"]
    if chicago.empty:
        truth = True
        expl = "No Chicago hotels in data; vacuously true."
    else:
        condition = chicago["avg_nightly_rate"] > 200
        truth = condition.all()
        if truth:
            expl = f"All {len(chicago)} Chicago hotels have avg nightly rate > $200."
        else:
            viol = chicago[~condition]
            expl = f"{len(viol)} Chicago hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most hotels have an average nightly rate greater than $140."""
    total = len(df)
    count = (df["avg_nightly_rate"] > 140).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} hotels have avg nightly rate > $140."
    else:
        expl = f"Only {count} out of {total} hotels have avg nightly rate > $140."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All hotels with a bookings month greater than 850 have a cancellation rate less than 11%."""
    bm_gt_850 = df[df["bookings_month"] > 850]
    if bm_gt_850.empty:
        truth = True
        expl = "No hotels with bookings month > 850; vacuously true."
    else:
        condition = bm_gt_850["cancellation_rate"] < 11
        truth = condition.all()
        if truth:
            expl = f"All {len(bm_gt_850)} hotels with bookings month > 850 have cancellation rate < 11%."
        else:
            viol = bm_gt_850[~condition]
            expl = f"{len(viol)} hotels with bookings month > 850 violate the rule (rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_45.csv")

    # Convert numeric columns safely
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')

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