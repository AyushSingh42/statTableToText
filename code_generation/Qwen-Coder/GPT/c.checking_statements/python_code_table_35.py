import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all 5-star hotels, occupancy_rate is at least 66.1%."""
    five_star = df[df["star_level"] == 5]
    if five_star.empty:
        truth = True
        expl = "No 5-star hotels in dataset."
    else:
        condition = five_star["occupancy_rate"] >= 66.1
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star)} 5-star hotels meet occupancy rate requirement."
        else:
            viol = five_star[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all hotels in Dallas, avg_nightly_rate is at least $199.5."""
    dallas = df[df["city"] == "dallas"]
    if dallas.empty:
        truth = True
        expl = "No hotels in Dallas in dataset."
    else:
        condition = dallas["avg_nightly_rate"] >= 199.5
        truth = condition.all()
        if truth:
            expl = f"All {len(dallas)} Dallas hotels meet average nightly rate requirement."
        else:
            viol = dallas[~condition]
            expl = f"{len(viol)} Dallas hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all Denver hotels, avg_nightly_rate does not exceed $160.5."""
    denver = df[df["city"] == "denver"]
    if denver.empty:
        truth = True
        expl = "No hotels in Denver in dataset."
    else:
        condition = denver["avg_nightly_rate"] <= 160.5
        truth = condition.all()
        if truth:
            expl = f"All {len(denver)} Denver hotels meet maximum average nightly rate requirement."
        else:
            viol = denver[~condition]
            expl = f"{len(viol)} Denver hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all 3-star hotels, cancellation_rate is at most 15.3%."""
    three_star = df[df["star_level"] == 3]
    if three_star.empty:
        truth = True
        expl = "No 3-star hotels in dataset."
    else:
        condition = three_star["cancellation_rate"] <= 15.3
        truth = condition.all()
        if truth:
            expl = f"All {len(three_star)} 3-star hotels meet cancellation rate requirement."
        else:
            viol = three_star[~condition]
            expl = f"{len(viol)} 3-star hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all hotels with staff_count of at least 40, avg_nightly_rate is at least $135.6."""
    large_staff = df[df["staff_count"] >= 40]
    if large_staff.empty:
        truth = True
        expl = "No hotels with staff count >= 40 in dataset."
    else:
        condition = large_staff["avg_nightly_rate"] >= 135.6
        truth = condition.all()
        if truth:
            expl = f"All {len(large_staff)} hotels with large staff meet average nightly rate requirement."
        else:
            viol = large_staff[~condition]
            expl = f"{len(viol)} hotels with large staff violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all hotels with avg_nightly_rate exceeding $200, occupancy_rate is at least 70.4%."""
    high_rate = df[df["avg_nightly_rate"] > 200]
    if high_rate.empty:
        truth = True
        expl = "No hotels with average nightly rate > $200 in dataset."
    else:
        condition = high_rate["occupancy_rate"] >= 70.4
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rate)} hotels with high rate meet occupancy rate requirement."
        else:
            viol = high_rate[~condition]
            expl = f"{len(viol)} hotels with high rate violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all Chicago hotels, bookings_month is at least 815."""
    chicago = df[df["city"] == "chicago"]
    if chicago.empty:
        truth = True
        expl = "No hotels in Chicago in dataset."
    else:
        condition = chicago["bookings_month"] >= 815
        truth = condition.all()
        if truth:
            expl = f"All {len(chicago)} Chicago hotels meet booking requirement."
        else:
            viol = chicago[~condition]
            expl = f"{len(viol)} Chicago hotels violate the rule (bookings: {', '.join(map(str, viol['bookings_month'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most hotels have occupancy_rate greater than 70%."""
    condition = df["occupancy_rate"] > 70
    count_above = condition.sum()
    total = len(df)
    truth = count_above > total / 2
    if truth:
        expl = f"{count_above} out of {total} hotels have occupancy rate > 70%."
    else:
        expl = f"{count_above} out of {total} hotels have occupancy rate > 70%, which is not more than half."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_35.csv")

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