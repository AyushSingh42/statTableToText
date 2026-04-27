import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Denver have an average nightly rate greater than $140."""
    subset = df[df["city"] == "denver"]
    condition = subset["avg_nightly_rate"] > 140
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} Denver hotels have avg nightly rate > $140."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} Denver hotels violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Austin, then its occupancy rate is greater than 73%."""
    subset = df[df["city"] == "austin"]
    condition = subset["occupancy_rate"] > 73
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} Austin hotels have occupancy rate > 73%."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} Austin hotels violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one hotel in Portland with a staff count less than 30."""
    subset = df[(df["city"] == "portland") & (df["staff_count"] < 30)]
    truth = not subset.empty
    if truth:
        ids = subset["hotel_id"].tolist()
        expl = f"Found {len(subset)} Portland hotel(s) with staff count < 30 (IDs: {', '.join(ids)})."
    else:
        expl = "No Portland hotel with staff count < 30 found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with a star level of 5 have an average nightly rate greater than $150."""
    subset = df[df["star_level"] == 5]
    condition = subset["avg_nightly_rate"] > 150
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} star-5 hotels have avg nightly rate > $150."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} star-5 hotels violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel has a cancellation rate less than 12%, then its occupancy rate is greater than 75%."""
    subset = df[df["cancellation_rate"] < 12]
    condition = subset["occupancy_rate"] > 75
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} hotels with cancellation rate < 12% have occupancy rate > 75%."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} hotels with cancellation rate < 12% violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most hotels in the dataset have a staff count greater than 30."""
    subset = df[df["staff_count"] > 30]
    truth = len(subset) > len(df) / 2
    if truth:
        expl = f"{len(subset)} out of {len(df)} hotels have staff count > 30 (majority)."
    else:
        expl = f"Only {len(subset)} out of {len(df)} hotels have staff count > 30 (not majority)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels in Chicago with a star level of 3 have an occupancy rate greater than 72%."""
    subset = df[(df["city"] == "chicago") & (df["star_level"] == 3)]
    condition = subset["occupancy_rate"] > 72
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} Chicago star-3 hotels have occupancy rate > 72%."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} Chicago star-3 hotels violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Phoenix, then its average nightly rate is greater than $200."""
    subset = df[df["city"] == "phoenix"]
    condition = subset["avg_nightly_rate"] > 200
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} Phoenix hotels have avg nightly rate > $200."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} Phoenix hotels violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one hotel in Dallas with a staff count less than 40 and a star level of 5."""
    subset = df[(df["city"] == "dallas") & (df["staff_count"] < 40) & (df["star_level"] == 5)]
    truth = not subset.empty
    if truth:
        ids = subset["hotel_id"].tolist()
        expl = f"Found {len(subset)} Dallas hotel(s) with staff < 40 and star 5 (IDs: {', '.join(ids)})."
    else:
        expl = "No Dallas hotel with staff < 40 and star 5 found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All hotels with an occupancy rate greater than 85% have a staff count less than 45."""
    subset = df[df["occupancy_rate"] > 85]
    condition = subset["staff_count"] < 45
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} hotels with occupancy > 85% have staff count < 45."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} hotels with occupancy > 85% violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel has a star level of 3, then its average nightly rate is less than $170."""
    subset = df[df["star_level"] == 3]
    condition = subset["avg_nightly_rate"] < 170
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} star-3 hotels have avg nightly rate < $170."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} star-3 hotels violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most hotels in the dataset have an occupancy rate greater than 70%."""
    subset = df[df["occupancy_rate"] > 70]
    truth = len(subset) > len(df) / 2
    if truth:
        expl = f"{len(subset)} out of {len(df)} hotels have occupancy rate > 70% (majority)."
    else:
        expl = f"Only {len(subset)} out of {len(df)} hotels have occupancy rate > 70% (not majority)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All hotels in Boston have a star level of 5."""
    subset = df[df["city"] == "boston"]
    condition = subset["star_level"] == 5
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} Boston hotels have star level 5."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} Boston hotels violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel is in Denver and has a star level of 3, then its occupancy rate is greater than 70%."""
    subset = df[(df["city"] == "denver") & (df["star_level"] == 3)]
    condition = subset["occupancy_rate"] > 70
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} Denver star-3 hotels have occupancy rate > 70%."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} Denver star-3 hotels violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one hotel in Chicago with a staff count less than 25 and a star level of 5."""
    subset = df[(df["city"] == "chicago") & (df["staff_count"] < 25) & (df["star_level"] == 5)]
    truth = not subset.empty
    if truth:
        ids = subset["hotel_id"].tolist()
        expl = f"Found {len(subset)} Chicago hotel(s) with staff < 25 and star 5 (IDs: {', '.join(ids)})."
    else:
        expl = "No Chicago hotel with staff < 25 and star 5 found."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All hotels with a cancellation rate greater than 14% have an occupancy rate less than 80%."""
    subset = df[df["cancellation_rate"] > 14]
    condition = subset["occupancy_rate"] < 80
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} hotels with cancellation > 14% have occupancy rate < 80%."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} hotels with cancellation > 14% violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel has an average nightly rate greater than $220, then its star level is 5 or 3."""
    subset = df[df["avg_nightly_rate"] > 220]
    condition = subset["star_level"].isin([5, 3])
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} hotels with avg nightly rate > $220 have star level 5 or 3."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} hotels with avg nightly rate > $220 violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most hotels in the dataset have a cancellation rate less than 15%."""
    subset = df[df["cancellation_rate"] < 15]
    truth = len(subset) > len(df) / 2
    if truth:
        expl = f"{len(subset)} out of {len(df)} hotels have cancellation rate < 15% (majority)."
    else:
        expl = f"Only {len(subset)} out of {len(df)} hotels have cancellation rate < 15% (not majority)."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All hotels in Austin with a star level of 3 have an occupancy rate greater than 73%."""
    subset = df[(df["city"] == "austin") & (df["star_level"] == 3)]
    condition = subset["occupancy_rate"] > 73
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} Austin star-3 hotels have occupancy rate > 73%."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} Austin star-3 hotels violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a hotel is in Dallas and has a star level of 5, then its occupancy rate is greater than 75%."""
    subset = df[(df["city"] == "dallas") & (df["star_level"] == 5)]
    condition = subset["occupancy_rate"] > 75
    truth = condition.all() if not subset.empty else True
    if truth:
        expl = f"All {len(subset)} Dallas star-5 hotels have occupancy rate > 75%."
    else:
        viol = subset[~condition]
        ids = viol["hotel_id"].tolist()
        expl = f"{len(viol)} Dallas star-5 hotels violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one hotel in Portland with a staff count greater than 40 and a star level of 3."""
    subset = df[(df["city"] == "portland") & (df["staff_count"] > 40) & (df["star_level"] == 3)]
    truth = not subset.empty
    if truth:
        ids = subset["hotel_id"].tolist()
        expl = f"Found {len(subset)} Portland hotel(s) with staff > 40 and star 3 (IDs: {', '.join(ids)})."
    else:
        expl = "No Portland hotel with staff > 40 and star 3 found."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_35.csv")
    # Ensure city names are lowercase for consistency
    df["city"] = df["city"].str.lower()
    # Convert numeric columns
    for col in df.columns:
        if col not in ["hotel_id", "city"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    checks = [
        (1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5),
        (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10),
        (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15),
        (16, stmt_16), (17, stmt_17), (18, stmt_18), (19, stmt_19), (20, stmt_20), (21, stmt_21)
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()