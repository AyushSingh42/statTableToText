import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 5-star hotels have an occupancy rate of at least 71.6%."""
    five_star = df[df["star_level"] == 5]
    condition = five_star["occupancy_rate"] >= 71.6
    truth = condition.all()
    if truth:
        expl = f"All {len(five_star)} 5-star hotels meet the occupancy rate requirement."
    else:
        viol = five_star[~condition]
        expl = f"{len(viol)} 5-star hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All 5-star hotels have a staff count of no more than 40."""
    five_star = df[df["star_level"] == 5]
    condition = five_star["staff_count"] <= 40
    truth = condition.all()
    if truth:
        expl = f"All {len(five_star)} 5-star hotels meet the staff count limit."
    else:
        viol = five_star[~condition]
        expl = f"{len(viol)} 5-star hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All 3-star hotels have an average nightly rate of at least $115.6."""
    three_star = df[df["star_level"] == 3]
    condition = three_star["avg_nightly_rate"] >= 115.6
    truth = condition.all()
    if truth:
        expl = f"All {len(three_star)} 3-star hotels meet the minimum nightly rate."
    else:
        viol = three_star[~condition]
        expl = f"{len(viol)} 3-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All Phoenix hotels have an occupancy rate of at least 71.6%."""
    phoenix = df[df["city"] == "phoenix"]
    condition = phoenix["occupancy_rate"] >= 71.6
    truth = condition.all()
    if truth:
        expl = f"All {len(phoenix)} Phoenix hotels meet the occupancy rate requirement."
    else:
        viol = phoenix[~condition]
        expl = f"{len(viol)} Phoenix hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All Miami hotels have a cancellation rate of no more than 12.4%."""
    miami = df[df["city"] == "miami"]
    condition = miami["cancellation_rate"] <= 12.4
    truth = condition.all()
    if truth:
        expl = f"All {len(miami)} Miami hotels meet the cancellation rate limit."
    else:
        viol = miami[~condition]
        expl = f"{len(viol)} Miami hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. There exists at least one 5-star hotel with an average nightly rate below $140."""
    five_star = df[df["star_level"] == 5]
    condition = five_star["avg_nightly_rate"] < 140
    truth = condition.any()
    if truth:
        expl = f"At least one 5-star hotel ({len(five_star[condition])}) has an average nightly rate below $140."
    else:
        expl = f"No 5-star hotels have an average nightly rate below $140."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most hotels have a cancellation rate greater than 9%."""
    condition = df["cancellation_rate"] > 9
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} hotels have a cancellation rate over 9% (more than half)."
    else:
        expl = f"{count} out of {total} hotels have a cancellation rate over 9% (less than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All hotels with an average nightly rate of $140 or less are either 3-star or 5-star."""
    filtered = df[df["avg_nightly_rate"] <= 140]
    condition = (filtered["star_level"] == 3) | (filtered["star_level"] == 5)
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} hotels with rate ≤ $140 are 3-star or 5-star."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} hotels with rate ≤ $140 are not 3-star or 5-star (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()