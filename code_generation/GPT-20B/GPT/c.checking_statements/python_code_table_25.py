import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels with a cancellation rate of 14% or higher are located in Austin."""
    high_cancel = df[df["cancellation_rate"] >= 14]
    violations = high_cancel[high_cancel["city"]!= "austin"]
    truth = violations.empty
    if truth:
        expl = f"All {len(high_cancel)} hotels with cancellation_rate >= 14 are in Austin."
    else:
        expl = f"{len(violations)} hotels violate the rule (cities: {', '.join(violations['city'].unique())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Every hotel with an occupancy rate above 85% is a 5-star hotel."""
    high_occ = df[df["occupancy_rate"] > 85]
    violations = high_occ[high_occ["star_level"]!= 5]
    truth = violations.empty
    if truth:
        expl = f"All {len(high_occ)} hotels with occupancy_rate > 85 are 5-star."
    else:
        expl = f"{len(violations)} hotels violate the rule (star levels: {', '.join(map(str, violations['star_level'].unique()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Hotels that have 25 or fewer staff members are all 5-star hotels."""
    small_staff = df[df["staff_count"] <= 25]
    violations = small_staff[small_staff["star_level"]!= 5]
    truth = violations.empty
    if truth:
        expl = f"All {len(small_staff)} hotels with staff_count <= 25 are 5-star."
    else:
        expl = f"{len(violations)} hotels violate the rule (star levels: {', '.join(map(str, violations['star_level'].unique()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. In Miami, the 5-star hotel has a lower average nightly rate ($120.0) than the 4-star hotel ($179.8)."""
    miami = df[df["city"] == "miami"]
    five_star = miami[(miami["star_level"] == 5) & (miami["avg_nightly_rate"] == 120.0)]
    four_star = miami[(miami["star_level"] == 4) & (miami["avg_nightly_rate"] == 179.8)]
    truth = not five_star.empty and not four_star.empty and (120.0 < 179.8)
    if truth:
        expl = "Both required hotels exist in Miami and 120.0 < 179.8."
    else:
        missing = []
        if five_star.empty:
            missing.append("5-star hotel with $120.0")
        if four_star.empty:
            missing.append("4-star hotel with $179.8")
        expl = f"Missing: {', '.join(missing)}." if missing else "Condition not satisfied."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. The hotel with the highest average nightly rate ($222.0) is a 3-star hotel in Denver."""
    max_row = df.loc[df["avg_nightly_rate"].idxmax()]
    truth = (max_row["avg_nightly_rate"] == 222.0 and
             max_row["star_level"] == 3 and
             max_row["city"] == "denver")
    if truth:
        expl = f"Hotel {max_row['hotel_id']} has $222.0, 3-star, in Denver."
    else:
        expl = f"Highest rate is ${max_row['avg_nightly_rate']}, star {max_row['star_level']}, city {max_row['city']}."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Every 4-star hotel has an average nightly rate between $145.1 and $213.4."""
    four_star = df[df["star_level"] == 4]
    violations = four_star[~four_star["avg_nightly_rate"].between(145.1, 213.4, inclusive="both")]
    truth = violations.empty
    if truth:
        expl = f"All {len(four_star)} 4-star hotels have rates within the range."
    else:
        expl = f"{len(violations)} 4-star hotels violate the rate range."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All Austin hotels have cancellation rates of at least 11.7%."""
    austin = df[df["city"] == "austin"]
    violations = austin[austin["cancellation_rate"] < 11.7]
    truth = violations.empty
    if truth:
        expl = f"All {len(austin)} Austin hotels have cancellation_rate >= 11.7%."
    else:
        expl = f"{len(violations)} Austin hotels violate the rule (rates: {', '.join(map(str, violations['cancellation_rate'].unique()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Every hotel with an average nightly rate of $130 or less is a 5-star hotel."""
    low_rate = df[df["avg_nightly_rate"] <= 130]
    violations = low_rate[low_rate["star_level"]!= 5]
    truth = violations.empty
    if truth:
        expl = f"All {len(low_rate)} hotels with avg_nightly_rate <= 130 are 5-star."
    else:
        expl = f"{len(violations)} hotels violate the rule (star levels: {', '.join(map(str, violations['star_level'].unique()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_25.csv")

    # Convert numeric columns where possible
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()