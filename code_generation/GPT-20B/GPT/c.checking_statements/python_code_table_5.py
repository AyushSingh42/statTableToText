import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 5-star hotels in Phoenix have occupancy rates above 84%."""
    mask = (df["star_level"] == 5) & (df["city"].str.lower() == "phoenix")
    subset = df[mask]
    if subset.empty:
        return True, "No 5-star hotels in Phoenix to evaluate."
    condition = subset["occupancy_rate"] > 84.0
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} 5-star Phoenix hotels have occupancy > 84%."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} 5-star Phoenix hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hotels with an average nightly rate above $210 have occupancy rates at most 84.0%."""
    mask = df["avg_nightly_rate"] > 210.0
    subset = df[mask]
    if subset.empty:
        return True, "No hotels with avg nightly rate > $210 to evaluate."
    condition = subset["occupancy_rate"] <= 84.0
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} hotels with avg nightly rate > $210 have occupancy <= 84%."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} hotels violate the rule (occupancy: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a hotel is located in Phoenix, its average nightly rate is below $130."""
    mask = df["city"].str.lower() == "phoenix"
    subset = df[mask]
    if subset.empty:
        return True, "No hotels in Phoenix to evaluate."
    condition = subset["avg_nightly_rate"] < 130.0
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} Phoenix hotels have avg nightly rate < $130."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} Phoenix hotels violate the rule (avg nightly rate: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists a 5-star hotel with a cancellation rate below 9% (the Atlanta hotel with 8.1%)."""
    mask = (df["star_level"] == 5) & (df["cancellation_rate"] < 9.0)
    subset = df[mask]
    truth = not subset.empty
    if truth:
        hotels = subset["hotel_id"].tolist()
        expl = f"Found {len(subset)} 5-star hotel(s) with cancellation rate < 9%: {', '.join(hotels)}."
    else:
        expl = "No 5-star hotel has a cancellation rate below 9%."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All hotels with occupancy rates above 85% are 5-star hotels located in Phoenix or Atlanta."""
    mask = df["occupancy_rate"] > 85.0
    subset = df[mask]
    if subset.empty:
        return True, "No hotels with occupancy > 85% to evaluate."
    condition = (subset["star_level"] == 5) & (subset["city"].str.lower().isin(["phoenix", "atlanta"]))
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} hotels with occupancy > 85% are 5-star in Phoenix or Atlanta."
    else:
        viol = subset[~condition]
        viol_info = viol.apply(lambda row: f"{row['hotel_id']} ({row['city']}, star {row['star_level']})", axis=1).tolist()
        expl = f"{len(viol)} hotels violate the rule: {', '.join(viol_info)}."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All Atlanta hotels have cancellation rates below 14%."""
    mask = df["city"].str.lower() == "atlanta"
    subset = df[mask]
    if subset.empty:
        return True, "No Atlanta hotels to evaluate."
    condition = subset["cancellation_rate"] < 14.0
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} Atlanta hotels have cancellation rate < 14%."
    else:
        viol = subset[~condition]
        viol_info = viol.apply(lambda row: f"{row['hotel_id']} (cancellation {row['cancellation_rate']}%)", axis=1).tolist()
        expl = f"{len(viol)} Atlanta hotels violate the rule: {', '.join(viol_info)}."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Among 3-star hotels, the Portland hotel has the lowest average nightly rate."""
    mask = df["star_level"] == 3
    subset = df[mask]
    if subset.empty:
        return True, "No 3-star hotels to evaluate."
    min_rate = subset["avg_nightly_rate"].min()
    portland = subset[subset["city"].str.lower() == "portland"]
    if portland.empty:
        return False, "No Portland hotel among 3-star hotels."
    portland_rate = portland["avg_nightly_rate"].iloc[0]
    truth = portland_rate == min_rate
    if truth:
        expl = f"Portland's avg nightly rate (${portland_rate}) is the lowest among 3-star hotels (${min_rate})."
    else:
        expl = f"Portland's avg nightly rate (${portland_rate}) is not the lowest (${min_rate})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_5.csv")

    # Convert numeric columns
    numeric_cols = ["occupancy_rate", "avg_nightly_rate", "bookings_month",
                    "cancellation_rate", "staff_count", "star_level"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    checks = [
        (1, stmt_1),
        (2, stmt_2),
        (3, stmt_3),
        (4, stmt_4),
        (5, stmt_5),
        (6, stmt_6),
        (7, stmt_7),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()