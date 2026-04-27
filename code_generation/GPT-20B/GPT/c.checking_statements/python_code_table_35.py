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
        return True, "No 5-star hotels present; condition holds vacuously."
    condition = five_star["occupancy_rate"] >= 66.1
    truth = condition.all()
    if truth:
        return True, f"All {len(five_star)} 5-star hotels meet the occupancy rate requirement."
    viol = five_star[~condition]
    return False, f"{len(viol)} 5-star hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. For all hotels in Dallas, avg_nightly_rate is at least $199.5."""
    dallas = df[df["city"].str.lower() == "dallas"]
    if dallas.empty:
        return True, "No Dallas hotels present; condition holds vacuously."
    condition = dallas["avg_nightly_rate"] >= 199.5
    truth = condition.all()
    if truth:
        return True, f"All {len(dallas)} Dallas hotels meet the avg nightly rate requirement."
    viol = dallas[~condition]
    return False, f"{len(viol)} Dallas hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. For all Denver hotels, avg_nightly_rate does not exceed $160.5."""
    denver = df[df["city"].str.lower() == "denver"]
    if denver.empty:
        return True, "No Denver hotels present; condition holds vacuously."
    condition = denver["avg_nightly_rate"] <= 160.5
    truth = condition.all()
    if truth:
        return True, f"All {len(denver)} Denver hotels meet the avg nightly rate upper bound."
    viol = denver[~condition]
    return False, f"{len(viol)} Denver hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."

def stmt_4(df: pd.DataFrame):
    """4. For all 3-star hotels, cancellation_rate is at most 15.3%."""
    three_star = df[df["star_level"] == 3]
    if three_star.empty:
        return True, "No 3-star hotels present; condition holds vacuously."
    condition = three_star["cancellation_rate"] <= 15.3
    truth = condition.all()
    if truth:
        return True, f"All {len(three_star)} 3-star hotels meet the cancellation rate requirement."
    viol = three_star[~condition]
    return False, f"{len(viol)} 3-star hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."

def stmt_5(df: pd.DataFrame):
    """5. For all hotels with staff_count of at least 40, avg_nightly_rate is at least $135.6."""
    staff_ge_40 = df[df["staff_count"] >= 40]
    if staff_ge_40.empty:
        return True, "No hotels with staff_count >= 40; condition holds vacuously."
    condition = staff_ge_40["avg_nightly_rate"] >= 135.6
    truth = condition.all()
    if truth:
        return True, f"All {len(staff_ge_40)} hotels with staff_count >= 40 meet the avg nightly rate requirement."
    viol = staff_ge_40[~condition]
    return False, f"{len(viol)} hotels with staff_count >= 40 violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."

def stmt_6(df: pd.DataFrame):
    """6. For all hotels with avg_nightly_rate exceeding $200, occupancy_rate is at least 70.4%."""
    high_rate = df[df["avg_nightly_rate"] > 200]
    if high_rate.empty:
        return True, "No hotels with avg_nightly_rate > 200; condition holds vacuously."
    condition = high_rate["occupancy_rate"] >= 70.4
    truth = condition.all()
    if truth:
        return True, f"All {len(high_rate)} hotels with avg_nightly_rate > 200 meet the occupancy rate requirement."
    viol = high_rate[~condition]
    return False, f"{len(viol)} hotels with avg_nightly_rate > 200 violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."

def stmt_7(df: pd.DataFrame):
    """7. For all Chicago hotels, bookings_month is at least 815."""
    chicago = df[df["city"].str.lower() == "chicago"]
    if chicago.empty:
        return True, "No Chicago hotels present; condition holds vacuously."
    condition = chicago["bookings_month"] >= 815
    truth = condition.all()
    if truth:
        return True, f"All {len(chicago)} Chicago hotels meet the bookings_month requirement."
    viol = chicago[~condition]
    return False, f"{len(viol)} Chicago hotels violate the rule (bookings_month: {', '.join(map(str, viol['bookings_month'].tolist()))})."

def stmt_8(df: pd.DataFrame):
    """8. Most hotels have occupancy_rate greater than 70%."""
    if df.empty:
        return True, "No hotels in dataset; condition holds vacuously."
    count_gt_70 = (df["occupancy_rate"] > 70).sum()
    total = len(df)
    proportion = count_gt_70 / total
    truth = proportion > 0.5
    if truth:
        return True, f"{count_gt_70} out of {total} hotels ({proportion:.2%}) have occupancy_rate > 70%."
    else:
        return False, f"Only {count_gt_70} out of {total} hotels ({proportion:.2%}) have occupancy_rate > 70%."

def main():
    df = pd.read_csv("../inference_generation/tables/table_35.csv")

    # Convert numeric columns where possible
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')

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