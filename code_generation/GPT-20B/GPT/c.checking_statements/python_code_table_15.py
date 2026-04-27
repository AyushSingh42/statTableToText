import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 5‑star hotels have an occupancy rate of at least 67.2 %."""
    five_star = df[df["star_level"] == 5]
    condition = five_star["occupancy_rate"] >= 67.2
    truth = condition.all()
    if truth:
        expl = f"All {len(five_star)} 5‑star hotels meet the occupancy requirement."
    else:
        viol = five_star[~condition]
        expl = f"{len(viol)} 5‑star hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hotels with a cancellation rate above 14 % have an average nightly rate of no more than $214.5."""
    high_cancel = df[df["cancellation_rate"] > 14]
    condition = high_cancel["avg_nightly_rate"] <= 214.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_cancel)} hotels with cancellation >14% have avg nightly rate ≤ $214.5."
    else:
        viol = high_cancel[~condition]
        expl = f"{len(viol)} hotels violate the rule (avg nightly rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All Seattle hotels have an average nightly rate of $126.0 or less."""
    seattle = df[df["city"] == "seattle"]
    condition = seattle["avg_nightly_rate"] <= 126.0
    truth = condition.all()
    if truth:
        expl = f"All {len(seattle)} Seattle hotels have avg nightly rate ≤ $126.0."
    else:
        viol = seattle[~condition]
        expl = f"{len(viol)} Seattle hotels violate the rule (avg nightly rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with at least 45 staff members have an occupancy rate of at least 72.2 %."""
    many_staff = df[df["staff_count"] >= 45]
    condition = many_staff["occupancy_rate"] >= 72.2
    truth = condition.all()
    if truth:
        expl = f"All {len(many_staff)} hotels with ≥45 staff meet the occupancy requirement."
    else:
        viol = many_staff[~condition]
        expl = f"{len(viol)} hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All 3‑star hotels have an average nightly rate of no more than $141.4."""
    three_star = df[df["star_level"] == 3]
    condition = three_star["avg_nightly_rate"] <= 141.4
    truth = condition.all()
    if truth:
        expl = f"All {len(three_star)} 3‑star hotels have avg nightly rate ≤ $141.4."
    else:
        viol = three_star[~condition]
        expl = f"{len(viol)} 3‑star hotels violate the rule (avg nightly rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with more than 900 bookings per month have an occupancy rate of at least 84.3 %."""
    high_bookings = df[df["bookings_month"] > 900]
    condition = high_bookings["occupancy_rate"] >= 84.3
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bookings)} hotels with >900 bookings/month meet the occupancy requirement."
    else:
        viol = high_bookings[~condition]
        expl = f"{len(viol)} hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels with an average nightly rate of $200 or more have a star level of at least 4."""
    high_rate = df[df["avg_nightly_rate"] >= 200]
    condition = high_rate["star_level"] >= 4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rate)} hotels with avg nightly rate ≥ $200 have star level ≥ 4."
    else:
        viol = high_rate[~condition]
        expl = f"{len(viol)} hotels violate the rule (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most hotels have a cancellation rate greater than 10 %."""
    total = len(df)
    high_cancel = df[df["cancellation_rate"] > 10]
    proportion = len(high_cancel) / total
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of hotels have cancellation rate >10%."
    else:
        expl = f"Only {proportion*100:.1f}% of hotels have cancellation rate >10%."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All Chicago hotels have at least 38 staff members."""
    chicago = df[df["city"] == "chicago"]
    condition = chicago["staff_count"] >= 38
    truth = condition.all()
    if truth:
        expl = f"All {len(chicago)} Chicago hotels have ≥38 staff members."
    else:
        viol = chicago[~condition]
        expl = f"{len(viol)} Chicago hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_15.csv")

    # Ensure city is string and lowercased for case‑insensitive matching
    df["city"] = df["city"].astype(str).str.lower()

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()