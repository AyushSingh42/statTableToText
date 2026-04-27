import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 5-star hotels in Phoenix have occupancy rates above 84%."""
    phx_5star = df[(df['city'] == 'phoenix') & (df['star_level'] == 5)]
    if phx_5star.empty:
        truth = True
        expl = "No 5-star hotels in Phoenix found in dataset."
    else:
        condition = phx_5star['occupancy_rate'] > 84
        truth = condition.all()
        if truth:
            expl = f"All {len(phx_5star)} 5-star Phoenix hotels have occupancy > 84%."
        else:
            viol = phx_5star[~condition]
            expl = f"{len(viol)} 5-star Phoenix hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hotels with an average nightly rate above $210 have occupancy rates at most 84.0%."""
    high_rate = df[df['avg_nightly_rate'] > 210]
    if high_rate.empty:
        truth = True
        expl = "No hotels with avg nightly rate > $210 found in dataset."
    else:
        condition = high_rate['occupancy_rate'] <= 84.0
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rate)} hotels with rate > $210 have occupancy <= 84%."
        else:
            viol = high_rate[~condition]
            expl = f"{len(viol)} hotels with rate > $210 violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a hotel is located in Phoenix, its average nightly rate is below $130."""
    phx_hotels = df[df['city'] == 'phoenix']
    if phx_hotels.empty:
        truth = True
        expl = "No hotels in Phoenix found in dataset."
    else:
        condition = phx_hotels['avg_nightly_rate'] < 130
        truth = condition.all()
        if truth:
            expl = f"All {len(phx_hotels)} Phoenix hotels have rate < $130."
        else:
            viol = phx_hotels[~condition]
            expl = f"{len(viol)} Phoenix hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists a 5-star hotel with a cancellation rate below 9%."""
    five_star = df[df['star_level'] == 5]
    if five_star.empty:
        truth = False
        expl = "No 5-star hotels found in dataset."
    else:
        condition = five_star['cancellation_rate'] < 9
        if condition.any():
            truth = True
            valid_hotel = five_star[condition].iloc[0]
            expl = f"Found 5-star hotel {valid_hotel['hotel_id']} with cancellation rate {valid_hotel['cancellation_rate']}%."
        else:
            truth = False
            expl = "No 5-star hotels with cancellation rate < 9% found."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All hotels with occupancy rates above 85% are 5-star hotels located in Phoenix or Atlanta."""
    high_occ = df[df['occupancy_rate'] > 85]
    if high_occ.empty:
        truth = True
        expl = "No hotels with occupancy > 85% found in dataset."
    else:
        condition = ((high_occ['star_level'] == 5) &
                     ((high_occ['city'] == 'phoenix') | (high_occ['city'] == 'atlanta')))
        truth = condition.all()
        if truth:
            expl = f"All {len(high_occ)} hotels with occupancy > 85% are 5-star Phoenix/Atlanta hotels."
        else:
            viol = high_occ[~condition]
            expl = f"{len(viol)} hotels with occupancy > 85% violate the rule (cities: {', '.join(viol['city'].tolist())}, star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All Atlanta hotels have cancellation rates below 14%."""
    atlanta_hotels = df[df['city'] == 'atlanta']
    if atlanta_hotels.empty:
        truth = True
        expl = "No hotels in Atlanta found in dataset."
    else:
        condition = atlanta_hotels['cancellation_rate'] < 14
        truth = condition.all()
        if truth:
            expl = f"All {len(atlanta_hotels)} Atlanta hotels have cancellation rate < 14%."
        else:
            viol = atlanta_hotels[~condition]
            expl = f"{len(viol)} Atlanta hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Among 3-star hotels, the Portland hotel has the lowest average nightly rate."""
    three_star = df[(df['star_level'] == 3) & (df['city'] == 'portland')]
    if three_star.empty:
        truth = False
        expl = "No 3-star Portland hotels found in dataset."
    else:
        other_three_stars = df[(df['star_level'] == 3) & (df['city']!= 'portland')]
        if other_three_stars.empty:
            truth = True
            expl = "Only one 3-star hotel in dataset; it's Portland."
        else:
            portland_rate = three_star['avg_nightly_rate'].iloc[0]
            min_other_rate = other_three_stars['avg_nightly_rate'].min()
            truth = portland_rate < min_other_rate
            if truth:
                expl = f"Portland 3-star hotel ({portland_rate}) has lower rate than minimum of others ({min_other_rate})."
            else:
                expl = f"Portland 3-star hotel ({portland_rate}) does not have the lowest rate among 3-star hotels."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_5.csv")

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
        (7, stmt_7)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()