import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All Atlanta hotels have an occupancy rate of at least 84.3%."""
    atlanta = df[df["city"].str.lower() == "atlanta"]
    if atlanta.empty:
        return True, "No Atlanta hotels in the data."
    condition = atlanta["occupancy_rate"] >= 84.3
    truth = condition.all()
    if truth:
        expl = f"All {len(atlanta)} Atlanta hotels meet the occupancy rate requirement."
    else:
        viol = atlanta[~condition]
        expl = f"{len(viol)} Atlanta hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All Denver hotels have an average nightly rate of at least $175.3."""
    denver = df[df["city"].str.lower() == "denver"]
    if denver.empty:
        return True, "No Denver hotels in the data."
    condition = denver["avg_nightly_rate"] >= 175.3
    truth = condition.all()
    if truth:
        expl = f"All {len(denver)} Denver hotels meet the average nightly rate requirement."
    else:
        viol = denver[~condition]
        expl = f"{len(viol)} Denver hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All 5-star hotels have an average nightly rate of at least $175.5."""
    five_star = df[df["star_level"] == 5]
    if five_star.empty:
        return True, "No 5-star hotels in the data."
    condition = five_star["avg_nightly_rate"] >= 175.5
    truth = condition.all()
    if truth:
        expl = f"All {len(five_star)} 5-star hotels meet the average nightly rate requirement."
    else:
        viol = five_star[~condition]
        expl = f"{len(viol)} 5-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All 5-star hotels have a cancellation rate of at least 10.3%."""
    five_star = df[df["star_level"] == 5]
    if five_star.empty:
        return True, "No 5-star hotels in the data."
    condition = five_star["cancellation_rate"] >= 10.3
    truth = condition.all()
    if truth:
        expl = f"All {len(five_star)} 5-star hotels meet the cancellation rate requirement."
    else:
        viol = five_star[~condition]
        expl = f"{len(viol)} 5-star hotels violate the rule (rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All hotels with an average nightly rate above $200 are 5-star."""
    high_rate = df[df["avg_nightly_rate"] > 200]
    if high_rate.empty:
        return True, "No hotels with average nightly rate above $200."
    condition = high_rate["star_level"] == 5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rate)} hotels with rate > $200 are 5-star."
    else:
        viol = high_rate[~condition]
        expl = f"{len(viol)} hotels with rate > $200 are not 5-star (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with at least 950 bookings per month have an average nightly rate of at least $173.9."""
    many_bookings = df[df["bookings_month"] >= 950]
    if many_bookings.empty:
        return True, "No hotels with 950 or more bookings per month."
    condition = many_bookings["avg_nightly_rate"] >= 173.9
    truth = condition.all()
    if truth:
        expl = f"All {len(many_bookings)} hotels with >=950 bookings meet the rate requirement."
    else:
        viol = many_bookings[~condition]
        expl = f"{len(viol)} hotels with >=950 bookings violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All Chicago hotels have a cancellation rate of at least 10.3%."""
    chicago = df[df["city"].str.lower() == "chicago"]
    if chicago.empty:
        return True, "No Chicago hotels in the data."
    condition = chicago["cancellation_rate"] >= 10.3
    truth = condition.all()
    if truth:
        expl = f"All {len(chicago)} Chicago hotels meet the cancellation rate requirement."
    else:
        viol = chicago[~condition]
        expl = f"{len(viol)} Chicago hotels violate the rule (rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All hotels with an occupancy rate of at least 85% are 4-star."""
    high_occ = df[df["occupancy_rate"] >= 85]
    if high_occ.empty:
        return True, "No hotels with occupancy rate >= 85%."
    condition = high_occ["star_level"] == 4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_occ)} hotels with occupancy >= 85% are 4-star."
    else:
        viol = high_occ[~condition]
        expl = f"{len(viol)} hotels with occupancy >= 85% are not 4-star (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All 4-star hotels have a cancellation rate of at most 14.1%."""
    four_star = df[df["star_level"] == 4]
    if four_star.empty:
        return True, "No 4-star hotels in the data."
    condition = four_star["cancellation_rate"] <= 14.1
    truth = condition.all()
    if truth:
        expl = f"All {len(four_star)} 4-star hotels meet the cancellation rate limit."
    else:
        viol = four_star[~condition]
        expl = f"{len(viol)} 4-star hotels violate the rule (rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_95.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col not in ["city", "staff_count", "star_level"]:
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()