import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels with a cancellation rate of 14% or higher are located in Austin."""
    high_cancellation = df[df['cancellation_rate'] >= 14.0]
    all_austin = high_cancellation['city'].eq('austin').all()
    if all_austin:
        expl = f"All {len(high_cancellation)} hotels with cancellation rate >= 14% are in Austin."
    else:
        non_austin = high_cancellation[high_cancellation['city']!= 'austin']
        expl = f"{len(non_austin)} hotels with cancellation rate >= 14% are not in Austin ({', '.join(non_austin['city'].unique())})."
    return all_austin, expl

def stmt_2(df: pd.DataFrame):
    """2. Every hotel with an occupancy rate above 85% is a 5-star hotel."""
    high_occupancy = df[df['occupancy_rate'] > 85.0]
    all_five_star = high_occupancy['star_level'].eq(5).all()
    if all_five_star:
        expl = f"All {len(high_occupancy)} hotels with occupancy > 85% are 5-star."
    else:
        non_five_star = high_occupancy[high_occupancy['star_level']!= 5]
        expl = f"{len(non_five_star)} hotels with occupancy > 85% are not 5-star (star levels: {', '.join(map(str, non_five_star['star_level'].unique()))})."
    return all_five_star, expl

def stmt_3(df: pd.DataFrame):
    """3. Hotels that have 25 or fewer staff members are all 5-star hotels."""
    low_staff = df[df['staff_count'] <= 25]
    all_five_star = low_staff['star_level'].eq(5).all()
    if all_five_star:
        expl = f"All {len(low_staff)} hotels with <= 25 staff members are 5-star."
    else:
        non_five_star = low_staff[low_staff['star_level']!= 5]
        expl = f"{len(non_five_star)} hotels with <= 25 staff members are not 5-star (star levels: {', '.join(map(str, non_five_star['star_level'].unique()))})."
    return all_five_star, expl

def stmt_4(df: pd.DataFrame):
    """4. In Miami, the 5-star hotel has a lower average nightly rate ($120.0) than the 4-star hotel ($179.8)."""
    miami_hotels = df[df['city'] =='miami']
    five_star = miami_hotels[miami_hotels['star_level'] == 5]
    four_star = miami_hotels[miami_hotels['star_level'] == 4]
    if len(five_star) == 1 and len(four_star) == 1:
        five_rate = five_star['avg_nightly_rate'].iloc[0]
        four_rate = four_star['avg_nightly_rate'].iloc[0]
        truth = five_rate < four_rate
        expl = f"5-star hotel rate (${five_rate:.1f}) < 4-star hotel rate (${four_rate:.1f}): {'TRUE' if truth else 'FALSE'}"
    else:
        expl = "Not exactly one 5-star and one 4-star hotel in Miami."
        truth = False
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. The hotel with the highest average nightly rate ($222.0) is a 3-star hotel in Denver."""
    max_rate = df['avg_nightly_rate'].max()
    max_hotel = df[df['avg_nightly_rate'] == max_rate]
    if len(max_hotel) == 1:
        hotel = max_hotel.iloc[0]
        truth = (hotel['avg_nightly_rate'] == 222.0) and (hotel['star_level'] == 3) and (hotel['city'] == 'denver')
        expl = f"Highest rate hotel is 3-star in Denver with rate ${max_rate}: {'TRUE' if truth else 'FALSE'}"
    else:
        expl = "Multiple hotels with maximum rate."
        truth = False
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Every 4-star hotel has an average nightly rate between $145.1 and $213.4."""
    four_star = df[df['star_level'] == 4]
    within_range = four_star['avg_nightly_rate'].between(145.1, 213.4, inclusive='both').all()
    if within_range:
        expl = f"All {len(four_star)} 4-star hotels have rates between $145.1 and $213.4."
    else:
        out_of_range = four_star[~four_star['avg_nightly_rate'].between(145.1, 213.4, inclusive='both')]
        expl = f"{len(out_of_range)} 4-star hotels have rates outside $145.1-$213.4 (rates: {', '.join(map(str, out_of_range['avg_nightly_rate'].tolist()))})."
    return within_range, expl

def stmt_7(df: pd.DataFrame):
    """7. All Austin hotels have cancellation rates of at least 11.7%."""
    austin_hotels = df[df['city'] == 'austin']
    all_at_least_11_7 = austin_hotels['cancellation_rate'] >= 11.7
    truth = all_at_least_11_7.all()
    if truth:
        expl = f"All {len(austin_hotels)} Austin hotels have cancellation rate >= 11.7%."
    else:
        below = austin_hotels[~all_at_least_11_7]
        expl = f"{len(below)} Austin hotels have cancellation rate < 11.7% (rates: {', '.join(map(str, below['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Every hotel with an average nightly rate of $130 or less is a 5-star hotel."""
    low_rate = df[df['avg_nightly_rate'] <= 130.0]
    all_five_star = low_rate['star_level'].eq(5).all()
    if all_five_star:
        expl = f"All {len(low_rate)} hotels with rate <= $130 are 5-star."
    else:
        non_five_star = low_rate[low_rate['star_level']!= 5]
        expl = f"{len(non_five_star)} hotels with rate <= $130 are not 5-star (star levels: {', '.join(map(str, non_five_star['star_level'].unique()))})."
    return all_five_star, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_25.csv")

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