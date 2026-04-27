import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 5‑star hotels have an occupancy rate of at least 71.6 %."""
    df5 = df[df["star_level"] == 5]
    condition = df5["occupancy_rate"] >= 71.6
    truth = condition.all()
    if truth:
        expl = f"All {len(df5)} 5‑star hotels have occupancy rate >= 71.6%."
    else:
        viol = df5[~condition]
        expl = f"{len(viol)} 5‑star hotel(s) violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All 5‑star hotels have a staff count of no more than 40."""
    df5 = df[df["star_level"] == 5]
    condition = df5["staff_count"] <= 40
    truth = condition.all()
    if truth:
        expl = f"All {len(df5)} 5‑star hotels have staff count <= 40."
    else:
        viol = df5[~condition]
        expl = f"{len(viol)} 5‑star hotel(s) violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All 3‑star hotels have an average nightly rate of at least $115.6."""
    df3 = df[df["star_level"] == 3]
    condition = df3["avg_nightly_rate"] >= 115.6
    truth = condition.all()
    if truth:
        expl = f"All {len(df3)} 3‑star hotels have avg nightly rate >= $115.6."
    else:
        viol = df3[~condition]
        expl = f"{len(viol)} 3‑star hotel(s) violate the rule (avg nightly rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All Phoenix hotels have an occupancy rate of at least 71.6 %."""
    df_phoenix = df[df["city"].str.lower() == "phoenix"]
    condition = df_phoenix["occupancy_rate"] >= 71.6
    truth = condition.all()
    if truth:
        expl = f"All {len(df_phoenix)} Phoenix hotel(s) have occupancy rate >= 71.6%."
    else:
        viol = df_phoenix[~condition]
        expl = f"{len(viol)} Phoenix hotel(s) violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All Miami hotels have a cancellation rate of no more than 12.4 %."""
    df_miami = df[df["city"].str.lower() == "miami"]
    condition = df_miami["cancellation_rate"] <= 12.4
    truth = condition.all()
    if truth:
        expl = f"All {len(df_miami)} Miami hotel(s) have cancellation rate <= 12.4%."
    else:
        viol = df_miami[~condition]
        expl = f"{len(viol)} Miami hotel(s) violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. There exists at least one 5‑star hotel with an average nightly rate below $140."""
    df5_low = df[(df["star_level"] == 5) & (df["avg_nightly_rate"] < 140)]
    truth = not df5_low.empty
    if truth:
        expl = f"Found {len(df5_low)} 5‑star hotel(s) with avg nightly rate below $140."
    else:
        expl = "No 5‑star hotel has avg nightly rate below $140."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most hotels have a cancellation rate greater than 9 %."""
    total = len(df)
    count_gt9 = df[df["cancellation_rate"] > 9].shape[0]
    truth = count_gt9 > total / 2
    expl = f"{count_gt9} out of {total} hotels have cancellation rate > 9% ({count_gt9/total*100:.1f}%)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All hotels with an average nightly rate of $140 or less are either 3‑star or 5‑star."""
    df_low = df[df["avg_nightly_rate"] <= 140]
    condition = df_low["star_level"].isin([3, 5])
    truth = condition.all()
    if truth:
        expl = f"All {len(df_low)} hotels with avg nightly rate <= $140 are 3‑star or 5‑star."
    else:
        viol = df_low[~condition]
        expl = f"{len(viol)} hotel(s) with avg nightly rate <= $140 are not 3‑star or 5‑star (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_85.csv")

    # Convert numeric columns safely
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