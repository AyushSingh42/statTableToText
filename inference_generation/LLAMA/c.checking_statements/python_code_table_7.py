import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels with a star level of 5 have an occupancy rate above 85%."""
    hotels = df[df["star_level"] == 5]
    condition = hotels["occupancy_rate"] > 85
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with a star level of 5 have an occupancy rate above 85%."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with a star level of 5 violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel has an occupancy rate above 80%, then its average nightly rate is above 150."""
    hotels = df[df["occupancy_rate"] > 80]
    condition = hotels["avg_nightly_rate"] > 150
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with an occupancy rate above 80% have an average nightly rate above 150."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with an occupancy rate above 80% violate the rule (average nightly rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every hotel with a staff count above 40 has a star level of 4 or 5."""
    hotels = df[df["staff_count"] > 40]
    condition = hotels["star_level"].isin([4, 5])
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with a staff count above 40 have a star level of 4 or 5."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with a staff count above 40 violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Hotels in cities with high occupancy rates (above 80%) tend to have higher average nightly rates (above 150)."""
    cities = df.groupby("city")["occupancy_rate"].mean()
    high_occupancy_cities = cities[cities > 80].index
    hotels = df[df["city"].isin(high_occupancy_cities)]
    condition = hotels["avg_nightly_rate"] > 150
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels in cities with high occupancy rates have an average nightly rate above 150."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels in cities with high occupancy rates violate the rule (average nightly rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All hotels with a cancellation rate above 12% have an occupancy rate above 75%."""
    hotels = df[df["cancellation_rate"] > 12]
    condition = hotels["occupancy_rate"] > 75
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with a cancellation rate above 12% have an occupancy rate above 75%."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with a cancellation rate above 12% violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a hotel has a star level of 3, then its staff count is below 35."""
    hotels = df[df["star_level"] == 3]
    condition = hotels["staff_count"] < 35
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with a star level of 3 have a staff count below 35."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with a star level of 3 violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Hotels with a high occupancy rate (above 80%) and a low cancellation rate (below 10%) tend to have a high average nightly rate (above 180)."""
    hotels = df[(df["occupancy_rate"] > 80) & (df["cancellation_rate"] < 10)]
    condition = hotels["avg_nightly_rate"] > 180
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with a high occupancy rate and a low cancellation rate have an average nightly rate above 180."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with a high occupancy rate and a low cancellation rate violate the rule (average nightly rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Every hotel with a staff count below 30 has a star level of 3."""
    hotels = df[df["staff_count"] < 30]
    condition = hotels["star_level"] == 3
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with a staff count below 30 have a star level of 3."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with a staff count below 30 violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a hotel has an average nightly rate above 200, then its occupancy rate is above 80%."""
    hotels = df[df["avg_nightly_rate"] > 200]
    condition = hotels["occupancy_rate"] > 80
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with an average nightly rate above 200 have an occupancy rate above 80%."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with an average nightly rate above 200 violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Hotels in cities with low occupancy rates (below 75%) tend to have lower average nightly rates (below 140)."""
    cities = df.groupby("city")["occupancy_rate"].mean()
    low_occupancy_cities = cities[cities < 75].index
    hotels = df[df["city"].isin(low_occupancy_cities)]
    condition = hotels["avg_nightly_rate"] < 140
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels in cities with low occupancy rates have an average nightly rate below 140."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels in cities with low occupancy rates violate the rule (average nightly rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All hotels with a star level of 4 or 5 have an average nightly rate above 160."""
    hotels = df[df["star_level"].isin([4, 5])]
    condition = hotels["avg_nightly_rate"] > 160
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with a star level of 4 or 5 have an average nightly rate above 160."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with a star level of 4 or 5 violate the rule (average nightly rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a hotel has a cancellation rate below 10%, then its occupancy rate is above 75%."""
    hotels = df[df["cancellation_rate"] < 10]
    condition = hotels["occupancy_rate"] > 75
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with a cancellation rate below 10% have an occupancy rate above 75%."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with a cancellation rate below 10% violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Every hotel with a staff count above 35 has a star level of 4 or 5."""
    hotels = df[df["staff_count"] > 35]
    condition = hotels["star_level"].isin([4, 5])
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with a staff count above 35 have a star level of 4 or 5."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with a staff count above 35 violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Hotels with a high occupancy rate (above 80%) and a high staff count (above 35) tend to have a high average nightly rate (above 180)."""
    hotels = df[(df["occupancy_rate"] > 80) & (df["staff_count"] > 35)]
    condition = hotels["avg_nightly_rate"] > 180
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with a high occupancy rate and a high staff count have an average nightly rate above 180."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with a high occupancy rate and a high staff count violate the rule (average nightly rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a hotel has an occupancy rate above 85%, then its cancellation rate is below 12%."""
    hotels = df[df["occupancy_rate"] > 85]
    condition = hotels["cancellation_rate"] < 12
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels)} hotels with an occupancy rate above 85% have a cancellation rate below 12%."
    else:
        viol = hotels[~condition]
        expl = f"{len(viol)} hotels with an occupancy rate above 85% violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_7.csv")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10), (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()