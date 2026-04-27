import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All Austin hotels have an average nightly rate of at least $149.2."""
    austin_hotels = df[df["city"].str.lower() == "austin"]
    condition = austin_hotels["avg_nightly_rate"] >= 149.2
    truth = condition.all()
    if truth:
        expl = f"All {len(austin_hotels)} Austin hotels meet the rate requirement."
    else:
        viol = austin_hotels[~condition]
        expl = f"{len(viol)} Austin hotels violate the rate requirement (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All Dallas hotels have an occupancy rate of at least 70.7%."""
    dallas_hotels = df[df["city"].str.lower() == "dallas"]
    condition = dallas_hotels["occupancy_rate"] >= 70.7
    truth = condition.all()
    if truth:
        expl = f"All {len(dallas_hotels)} Dallas hotels meet the occupancy requirement."
    else:
        viol = dallas_hotels[~condition]
        expl = f"{len(viol)} Dallas hotels violate the occupancy requirement (rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All Seattle hotels have an average nightly rate of at least $154.0."""
    seattle_hotels = df[df["city"].str.lower() == "seattle"]
    condition = seattle_hotels["avg_nightly_rate"] >= 154.0
    truth = condition.all()
    if truth:
        expl = f"All {len(seattle_hotels)} Seattle hotels meet the rate requirement."
    else:
        viol = seattle_hotels[~condition]
        expl = f"{len(viol)} Seattle hotels violate the rate requirement (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All 5-star hotels have a cancellation rate of no more than 15.1%."""
    five_star_hotels = df[df["star_level"] == 5]
    condition = five_star_hotels["cancellation_rate"] <= 15.1
    truth = condition.all()
    if truth:
        expl = f"All {len(five_star_hotels)} 5-star hotels meet the cancellation rate requirement."
    else:
        viol = five_star_hotels[~condition]
        expl = f"{len(viol)} 5-star hotels violate the cancellation rate requirement (rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All 4-star hotels have an average nightly rate between $149.2 and $211.0."""
    four_star_hotels = df[df["star_level"] == 4]
    condition = df["avg_nightly_rate"].between(149.2, 211.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(four_star_hotels)} 4-star hotels meet the rate requirement."
    else:
        viol = four_star_hotels[~condition]
        expl = f"{len(viol)} 4-star hotels violate the rate requirement (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with bookings between 690 and 700 have occupancy rates between 72.5% and 77.5%."""
    filtered_hotels = df[(df["bookings_month"] >= 690) & (df["bookings_month"] <= 700)]
    condition = df["occupancy_rate"].between(72.5, 77.5, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered_hotels)} hotels with bookings between 690 and 700 meet the occupancy requirement."
    else:
        viol = filtered_hotels[~condition]
        expl = f"{len(viol)} hotels with bookings between 690 and 700 violate the occupancy requirement (rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All 3-star hotels have an average nightly rate of at most $214.4."""
    three_star_hotels = df[df["star_level"] == 3]
    condition = three_star_hotels["avg_nightly_rate"] <= 214.4
    truth = condition.all()
    if truth:
        expl = f"All {len(three_star_hotels)} 3-star hotels meet the rate requirement."
    else:
        viol = three_star_hotels[~condition]
        expl = f"{len(viol)} 3-star hotels violate the rate requirement (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists a hotel with an occupancy rate below 70%, and it is located in Miami."""
    miami_hotels = df[df["city"].str.lower() == "miami"]
    condition = miami_hotels["occupancy_rate"] < 70
    truth = condition.any()
    if truth:
        viol = miami_hotels[condition]
        expl = f"There is at least one Miami hotel with occupancy rate below 70% (rate: {viol.iloc[0]['occupancy_rate']})."
    else:
        expl = "No Miami hotel has occupancy rate below 70%."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_55.csv")

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