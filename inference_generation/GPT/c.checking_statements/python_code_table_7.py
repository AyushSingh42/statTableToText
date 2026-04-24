import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def convert_numeric(df: pd.DataFrame) -> pd.DataFrame:
    # Attempt to convert known numeric columns that may be stored as strings
    numeric_cols = ["occupancy_rate", "avg_nightly_rate", "bookings_month",
                    "cancellation_rate", "staff_count", "star_level"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

def stmt_1(df: pd.DataFrame):
    """1. All 5-star hotels have an occupancy rate greater than 85%."""
    subset = df[df["star_level"] == 5]
    condition = subset["occupancy_rate"] > 85
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} 5‑star hotels satisfy occupancy_rate > 85%."
    else:
        viol = subset[~condition]
        expl = (f"{len(viol)} 5‑star hotels violate the rule "
                f"(occupancy_rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))}).")
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All 3-star hotels have an average nightly rate of at most $133.4."""
    subset = df[df["star_level"] == 3]
    condition = subset["avg_nightly_rate"] <= 133.4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} 3‑star hotels satisfy avg_nightly_rate ≤ 133.4."
    else:
        viol = subset[~condition]
        expl = (f"{len(viol)} 3‑star hotels violate the rule "
                f"(rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))}).")
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hotels with an occupancy rate above 80% have an average nightly rate of at least $176.5."""
    subset = df[df["occupancy_rate"] > 80]
    condition = subset["avg_nightly_rate"] >= 176.5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} hotels with occupancy_rate > 80% satisfy avg_nightly_rate ≥ 176.5."
    else:
        viol = subset[~condition]
        expl = (f"{len(viol)} hotels violate the rule "
                f"(occupancy_rate, avg_nightly_rate): {', '.join([f'({o}, {r})' for o, r in zip(viol['occupancy_rate'], viol['avg_nightly_rate'])])}.")
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with a cancellation rate greater than 14% have an average nightly rate of at least $185."""
    subset = df[df["cancellation_rate"] > 14]
    condition = subset["avg_nightly_rate"] >= 185
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} hotels with cancellation_rate > 14% satisfy avg_nightly_rate ≥ 185."
    else:
        viol = subset[~condition]
        expl = (f"{len(viol)} hotels violate the rule "
                f"(cancellation_rate, avg_nightly_rate): {', '.join([f'({c}, {r})' for c, r in zip(viol['cancellation_rate'], viol['avg_nightly_rate'])])}.")
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most hotels have an occupancy rate above 70%."""
    total = len(df)
    above = (df["occupancy_rate"] > 70).sum()
    truth = above > total / 2
    expl = f"{above} out of {total} hotels ({above/total:.1%}) have occupancy_rate > 70%."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All 5-star hotels have a cancellation rate greater than 13%."""
    subset = df[df["star_level"] == 5]
    condition = subset["cancellation_rate"] > 13
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} 5‑star hotels satisfy cancellation_rate > 13%."
    else:
        viol = subset[~condition]
        expl = (f"{len(viol)} 5‑star hotels violate the rule "
                f"(cancellation_rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))}).")
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels with an average nightly rate of at most $128.8 have a staff count less than 30."""
    subset = df[df["avg_nightly_rate"] <= 128.8]
    condition = subset["staff_count"] < 30
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} hotels with avg_nightly_rate ≤ 128.8 have staff_count < 30."
    else:
        viol = subset[~condition]
        expl = (f"{len(viol)} hotels violate the rule "
                f"(staff_counts: {', '.join(map(str, viol['staff_count'].tolist()))}).")
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All 4-star hotels have a cancellation rate between 10.7% and 15%."""
    subset = df[df["star_level"] == 4]
    condition = subset["cancellation_rate"].between(10.7, 15, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} 4‑star hotels satisfy 10.7% ≤ cancellation_rate ≤ 15%."
    else:
        viol = subset[~condition]
        expl = (f"{len(viol)} 4‑star hotels violate the rule "
                f"(cancellation_rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))}).")
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All hotels with fewer than 700 bookings per month have an occupancy rate below 70%."""
    subset = df[df["bookings_month"] < 700]
    condition = subset["occupancy_rate"] < 70
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} hotels with bookings_month < 700 satisfy occupancy_rate < 70%."
    else:
        viol = subset[~condition]
        expl = (f"{len(viol)} hotels violate the rule "
                f"(bookings_month, occupancy_rate): {', '.join([f'({b}, {o})' for b, o in zip(viol['bookings_month'], viol['occupancy_rate'])])}.")
    return truth, expl

def main():
    df = pd.read_csv("tables/table_7.csv")
    df = convert_numeric(df)

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