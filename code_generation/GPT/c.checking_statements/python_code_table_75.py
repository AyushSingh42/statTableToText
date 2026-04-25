import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 5-star hotels have an average nightly rate of at least $135.5."""
    five_star = df[df["star_level"] == 5]
    condition = five_star["avg_nightly_rate"] >= 135.5
    truth = condition.all()
    if truth:
        expl = f"All {len(five_star)} five-star hotels meet the rate requirement."
    else:
        viol = five_star[~condition]
        expl = f"{len(viol)} five-star hotels violate the rate requirement (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hotels with a cancellation rate below 9% have an occupancy rate of at least 74.5%."""
    low_cancellation = df[df["cancellation_rate"] < 9]
    condition = low_cancellation["occupancy_rate"] >= 74.5
    truth = condition.all()
    if truth:
        expl = f"All {len(low_cancellation)} hotels with low cancellation rates meet the occupancy requirement."
    else:
        viol = low_cancellation[~condition]
        expl = f"{len(viol)} hotels with low cancellation rates violate the occupancy requirement (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hotels with staff counts of 35 or more have a cancellation rate of 15.5% or lower."""
    high_staff = df[df["staff_count"] >= 35]
    condition = high_staff["cancellation_rate"] <= 15.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} hotels with high staff counts meet the cancellation rate requirement."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} hotels with high staff counts violate the cancellation rate requirement (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. The two Boston hotels both have average nightly rates of $159.0 or higher."""
    boston = df[df["city"] == "boston"]
    condition = boston["avg_nightly_rate"] >= 159.0
    truth = condition.all()
    if truth:
        expl = f"All {len(boston)} Boston hotels meet the rate requirement."
    else:
        viol = boston[~condition]
        expl = f"{len(viol)} Boston hotels violate the rate requirement (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. In Phoenix, hotel occupancy rates range from 68.6% to 74.5%."""
    phoenix = df[df["city"] == "phoenix"]
    min_occ = phoenix["occupancy_rate"].min()
    max_occ = phoenix["occupancy_rate"].max()
    truth = min_occ >= 68.6 and max_occ <= 74.5
    if truth:
        expl = f"Phoenix hotels' occupancy rates range from {min_occ:.1f}% to {max_occ:.1f}%."
    else:
        expl = f"Phoenix hotels' occupancy rates range from {min_occ:.1f}% to {max_occ:.1f}%, which does not match the specified range."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. The only hotels with occupancy rates below 70% are located in Portland, Austin, and Miami."""
    low_occ = df[df["occupancy_rate"] < 70]
    valid_cities = {"portland", "austin", "miami"}
    actual_cities = set(low_occ["city"].str.lower())
    truth = actual_cities.issubset(valid_cities) and len(actual_cities) > 0
    if truth:
        expl = f"All {len(low_occ)} hotels with low occupancy are in Portland, Austin, or Miami."
    else:
        invalid_cities = actual_cities - valid_cities
        expl = f"{len(low_occ)} hotels with low occupancy are in {', '.join(actual_cities)}, but only {', '.join(valid_cities)} are allowed."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Hotels with average nightly rates above $200 have cancellation rates of at least 11%."""
    high_rate = df[df["avg_nightly_rate"] > 200]
    condition = high_rate["cancellation_rate"] >= 11
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rate)} hotels with high rates meet the cancellation rate requirement."
    else:
        viol = high_rate[~condition]
        expl = f"{len(viol)} hotels with high rates violate the cancellation rate requirement (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All 3-star hotels have staff counts between 26 and 39."""
    three_star = df[df["star_level"] == 3]
    condition = three_star["staff_count"].between(26, 39, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(three_star)} three-star hotels meet the staff count requirement."
    else:
        viol = three_star[~condition]
        expl = f"{len(viol)} three-star hotels violate the staff count requirement (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_75.csv")

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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()