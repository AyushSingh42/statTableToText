import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 5-star hotels have a staff count of at least 25."""
    five_star = df[df["star_level"] == 5]
    condition = five_star["staff_count"] >= 25
    truth = condition.all()
    if truth:
        expl = f"All {len(five_star)} 5-star hotels have staff count >= 25."
    else:
        viol = five_star[~condition]
        expl = f"{len(viol)} 5-star hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hotels with occupancy rate above 85% have an average nightly rate of at least $193.2."""
    high_occ = df[df["occupancy_rate"] > 85]
    condition = high_occ["avg_nightly_rate"] >= 193.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_occ)} hotels with occupancy >85% have avg nightly rate >= $193.2."
    else:
        viol = high_occ[~condition]
        expl = f"{len(viol)} hotels violate the rule (avg rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All Boston hotels are 5-star."""
    boston = df[df["city"].str.lower() == "boston"]
    condition = boston["star_level"] == 5
    truth = condition.all()
    if truth:
        expl = f"All {len(boston)} Boston hotels are 5-star."
    else:
        viol = boston[~condition]
        expl = f"{len(viol)} Boston hotels are not 5-star (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with staff count greater than 40 have an occupancy rate below 69%."""
    high_staff = df[df["staff_count"] > 40]
    condition = high_staff["occupancy_rate"] < 69
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} hotels with staff >40 have occupancy <69%."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All 3-star hotels have a cancellation rate of at most 12.5%."""
    three_star = df[df["star_level"] == 3]
    condition = three_star["cancellation_rate"] <= 12.5
    truth = condition.all()
    if truth:
        expl = f"All {len(three_star)} 3-star hotels have cancellation rate <= 12.5%."
    else:
        viol = three_star[~condition]
        expl = f"{len(viol)} 3-star hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All Phoenix hotels have an average nightly rate of at least $146.6."""
    phoenix = df[df["city"].str.lower() == "phoenix"]
    condition = phoenix["avg_nightly_rate"] >= 146.6
    truth = condition.all()
    if truth:
        expl = f"All {len(phoenix)} Phoenix hotels have avg nightly rate >= $146.6."
    else:
        viol = phoenix[~condition]
        expl = f"{len(viol)} Phoenix hotels violate the rule (avg rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most hotels have an occupancy rate above 70%."""
    high_occ = df["occupancy_rate"] > 70
    proportion = high_occ.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of hotels have occupancy >70%."
    else:
        expl = f"Only {proportion*100:.1f}% of hotels have occupancy >70%."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All 4-star hotels have a staff count of at most 38."""
    four_star = df[df["star_level"] == 4]
    condition = four_star["staff_count"] <= 38
    truth = condition.all()
    if truth:
        expl = f"All {len(four_star)} 4-star hotels have staff count <= 38."
    else:
        viol = four_star[~condition]
        expl = f"{len(viol)} 4-star hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All Dallas hotels have an occupancy rate of at least 78.8%."""
    dallas = df[df["city"].str.lower() == "dallas"]
    condition = dallas["occupancy_rate"] >= 78.8
    truth = condition.all()
    if truth:
        expl = f"All {len(dallas)} Dallas hotels have occupancy >= 78.8%."
    else:
        viol = dallas[~condition]
        expl = f"{len(viol)} Dallas hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_45.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col not in ["hotel_id", "city"]:
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