import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 5-star hotels have an average nightly rate of at least $135.5."""
    five_star = df[df["star_level"] == 5]
    if five_star.empty:
        return True, "No 5-star hotels present; statement holds vacuously."
    condition = five_star["avg_nightly_rate"] >= 135.5
    truth = condition.all()
    if truth:
        expl = f"All {len(five_star)} 5-star hotels meet the rate requirement."
    else:
        viol = five_star[~condition]
        viol_ids = viol["hotel_id"].tolist()
        viol_rates = viol["avg_nightly_rate"].tolist()
        expl = f"{len(viol)} 5-star hotel(s) violate the rule (IDs: {', '.join(map(str, viol_ids))}, rates: {', '.join(map(str, viol_rates))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hotels with a cancellation rate below 9% have an occupancy rate of at least 74.5%."""
    low_cancel = df[df["cancellation_rate"] < 9]
    if low_cancel.empty:
        return True, "No hotels with cancellation rate below 9%; statement holds vacuously."
    condition = low_cancel["occupancy_rate"] >= 74.5
    truth = condition.all()
    if truth:
        expl = f"All {len(low_cancel)} hotels with cancellation rate < 9% have occupancy >= 74.5%."
    else:
        viol = low_cancel[~condition]
        viol_ids = viol["hotel_id"].tolist()
        viol_occ = viol["occupancy_rate"].tolist()
        expl = f"{len(viol)} hotel(s) violate the rule (IDs: {', '.join(map(str, viol_ids))}, occupancy: {', '.join(map(str, viol_occ))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hotels with staff counts of 35 or more have a cancellation rate of 15.5% or lower."""
    high_staff = df[df["staff_count"] >= 35]
    if high_staff.empty:
        return True, "No hotels with staff count >= 35; statement holds vacuously."
    condition = high_staff["cancellation_rate"] <= 15.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} hotels with staff >= 35 have cancellation rate <= 15.5%."
    else:
        viol = high_staff[~condition]
        viol_ids = viol["hotel_id"].tolist()
        viol_cr = viol["cancellation_rate"].tolist()
        expl = f"{len(viol)} hotel(s) violate the rule (IDs: {', '.join(map(str, viol_ids))}, cancellation rates: {', '.join(map(str, viol_cr))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. The two Boston hotels both have average nightly rates of $159.0 or higher."""
    boston = df[df["city"].str.lower() == "boston"]
    if len(boston)!= 2:
        return False, f"Expected 2 Boston hotels, found {len(boston)}."
    condition = boston["avg_nightly_rate"] >= 159.0
    truth = condition.all()
    if truth:
        expl = "Both Boston hotels meet the rate requirement."
    else:
        viol = boston[~condition]
        viol_ids = viol["hotel_id"].tolist()
        viol_rates = viol["avg_nightly_rate"].tolist()
        expl = f"{len(viol)} Boston hotel(s) violate the rule (IDs: {', '.join(map(str, viol_ids))}, rates: {', '.join(map(str, viol_rates))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. In Phoenix, hotel occupancy rates range from 68.6% to 74.5%."""
    phoenix = df[df["city"].str.lower() == "phoenix"]
    if phoenix.empty:
        return False, "No Phoenix hotels found."
    min_occ = phoenix["occupancy_rate"].min()
    max_occ = phoenix["occupancy_rate"].max()
    truth = (min_occ >= 68.6) and (max_occ <= 74.5)
    if truth:
        expl = f"Phoenix hotels occupancy rates range from {min_occ}% to {max_occ}%."
    else:
        viol = phoenix[(phoenix["occupancy_rate"] < 68.6) | (phoenix["occupancy_rate"] > 74.5)]
        viol_ids = viol["hotel_id"].tolist()
        viol_occ = viol["occupancy_rate"].tolist()
        expl = f"Occupancy rates out of range for hotel(s) (IDs: {', '.join(map(str, viol_ids))}, rates: {', '.join(map(str, viol_occ))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. The only hotels with occupancy rates below 70% are located in Portland, Austin, and Miami."""
    low_occ = df[df["occupancy_rate"] < 70]
    if low_occ.empty:
        return True, "No hotels with occupancy < 70%; statement holds vacuously."
    cities = set(low_occ["city"].str.lower())
    allowed = {"portland", "austin", "miami"}
    truth = cities.issubset(allowed)
    if truth:
        expl = f"All hotels with occupancy < 70% are in {', '.join(sorted(allowed))}."
    else:
        viol = low_occ[~low_occ["city"].str.lower().isin(allowed)]
        viol_ids = viol["hotel_id"].tolist()
        viol_cities = viol["city"].tolist()
        expl = f"Hotels with occupancy < 70% in disallowed cities: IDs {', '.join(map(str, viol_ids))} (cities: {', '.join(viol_cities)})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Hotels with average nightly rates above $200 have cancellation rates of at least 11%."""
    high_rate = df[df["avg_nightly_rate"] > 200]
    if high_rate.empty:
        return True, "No hotels with avg nightly rate > $200; statement holds vacuously."
    condition = high_rate["cancellation_rate"] >= 11
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rate)} hotels with rate > $200 have cancellation rate >= 11%."
    else:
        viol = high_rate[~condition]
        viol_ids = viol["hotel_id"].tolist()
        viol_cr = viol["cancellation_rate"].tolist()
        expl = f"{len(viol)} hotel(s) violate the rule (IDs: {', '.join(map(str, viol_ids))}, cancellation rates: {', '.join(map(str, viol_cr))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All 3-star hotels have staff counts between 26 and 39."""
    three_star = df[df["star_level"] == 3]
    if three_star.empty:
        return True, "No 3-star hotels; statement holds vacuously."
    condition = three_star["staff_count"].between(26, 39, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(three_star)} 3-star hotels have staff counts between 26 and 39."
    else:
        viol = three_star[~condition]
        viol_ids = viol["hotel_id"].tolist()
        viol_staff = viol["staff_count"].tolist()
        expl = f"{len(viol)} 3-star hotel(s) violate the rule (IDs: {', '.join(map(str, viol_ids))}, staff counts: {', '.join(map(str, viol_staff))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_75.csv")
    # Convert numeric columns safely
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")
    checks = [
        (1, stmt_1),
        (2, stmt_2),
        (3, stmt_3),
        (4, stmt_4),
        (5, stmt_5),
        (6, stmt_6),
        (7, stmt_7),
        (8, stmt_8),
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()