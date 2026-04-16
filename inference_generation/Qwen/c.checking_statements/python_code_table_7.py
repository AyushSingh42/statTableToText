

import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels with a star level of 5 have an average nightly rate exceeding $190 and staff counts above 40."""
    star_5 = df[df['star_level'] == 5]
    condition = (star_5['avg_nightly_rate'] > 190) & (star_5['staff_count'] > 40)
    truth = condition.all()
    if truth:
        expl = f"All {len(star_5)} 5-star hotels meet the criteria."
    else:
        viol = star_5[~condition]
        expl = f"{len(viol)} hotels violate the rule (avg_nightly_rate: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))}, staff_count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel has an occupancy rate above 80%, its cancellation rate is strictly greater than 12%."""
    high_occupancy = df[df['occupancy_rate'] > 80]
    condition = high_occupancy['cancellation_rate'] > 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_occupancy)} hotels with occupancy >80% have cancellation rate >12%."
    else:
        viol = high_occupancy[~condition]
        expl = f"{len(viol)} hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For star level 3 hotels, cancellation rates are consistently below 11%, with the highest being 10.8% in Denver."""
    star_3 = df[df['star_level'] == 3]
    condition = star_3['cancellation_rate'] < 11
    truth_condition = condition.all()
    max_cancellation = star_3['cancellation_rate'].max()
    max_row = star_3[star_3['cancellation_rate'] == max_cancellation]
    city_with_max = max_row['city'].iloc[0] if not max_row.empty else None
    if truth_condition and max_cancellation == 10.8 and city_with_max == 'Denver':
        expl = f"All {len(star_3)} 3-star hotels have cancellation rates below 11%, with the highest {max_cancellation}% in {city_with_max}."
        truth = True
    else:
        viol = star_3[~condition]
        expl = f"{len(viol)} hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))}). Max cancellation rate is {max_cancellation}% in {city_with_max} instead of Denver."
        truth = False
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Every hotel with an average nightly rate exceeding $180 has an occupancy rate above 80%, except Miami (HT006), which has 81.7%."""
    high_rate = df[df['avg_nightly_rate'] > 180]
    exception_row = high_rate[(high_rate['hotel_id'] == 'HT006') & (high_rate['city'] == 'Miami') & (high_rate['occupancy_rate'] == 81.7)]
    others = high_rate[~((high_rate['hotel_id'] == 'HT006') & (high_rate['city'] == 'Miami') & (high_rate['occupancy_rate'] == 81.7))]
    condition = others['occupancy_rate'] > 80
    truth = condition.all() and not exception_row.empty
    if truth:
        expl = f"All hotels with avg_nightly_rate > $180 except HT006 in Miami meet occupancy >80%."
    else:
        viol = others[~condition]
        expl = f"{len(viol)} hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Hotels with both high occupancy (>80%) and high average nightly rates (>180) exhibit cancellation rates exceeding 13%."""
    high_occupancy_and_rate = df[(df['occupancy_rate'] > 80) & (df['avg_nightly_rate'] > 180)]
    condition = high_occupancy_and_rate['cancellation_rate'] > 13
    truth = condition.all()
    if truth:
        expl = f"All {len(high_occupancy_and_rate)} hotels meet cancellation rate >13%."
    else:
        viol = high_occupancy_and_rate[~condition]
        expl = f"{len(viol)} hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a hotel’s staff count exceeds 40, its star level is at least 4, and its average nightly rate is above $170."""
    high_staff = df[df['staff_count'] > 40]
    condition = (high_staff['star_level'] >= 4) & (high_staff['avg_nightly_rate'] > 170)
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} hotels with staff_count >40 meet the criteria."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} hotels violate the rule (star_level: {', '.join(map(str, viol['star_level'].tolist()))}, avg_nightly_rate: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All cities with average nightly rates above $190 belong to hotels with star levels of 5 and are located in Boston or Chicago."""
    high_rate = df[df['avg_nightly_rate'] > 190]
    condition = (high_rate['star_level'] == 5) & high_rate['city'].isin(['Boston', 'Chicago'])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rate)} hotels with avg_nightly_rate >$190 are 5-star in Boston or Chicago."
    else:
        viol = high_rate[~condition]
        expl = f"{len(viol)} hotels violate the rule (star_level: {', '.join(map(str, viol['star_level'].tolist()))}, cities: {', '.join(map(str, viol['city'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For star level 4 hotels, occupancy rates above 80% correlate with staff counts exceeding 35."""
    star_4_high_occupancy = df[(df['star_level'] == 4) & (df['occupancy_rate'] > 80)]
    condition = star_4_high_occupancy['staff_count'] > 35
    truth = condition.all()
    if truth:
        expl = f"All {len(star_4_high_occupancy)} star 4 hotels with occupancy >80% have staff_count >35."
    else:
        viol = star_4_high_occupancy[~condition]
        expl = f"{len(viol)} hotels violate the rule (staff_count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. The cancellation rate is inversely related to occupancy rate only in star level 3 hotels, where lower occupancy coincides with lower cancellation rates."""
    star_3 = df[df['star_level'] == 3]
    corr = star_3['occupancy_rate'].corr(star_3['cancellation_rate'])
    truth = corr < 0
    if truth:
        expl = f"Star level 3 hotels have a negative correlation ({corr:.2f}) between occupancy rate and cancellation rate."
    else:
        expl = f"Star level 3 hotels do not have a negative correlation ({corr:.2f}) between occupancy rate and cancellation rate."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a hotel’s cancellation rate is below 9.6%, its occupancy rate is strictly less than 70%, as seen in Detroit (HT014)."""
    low_cancellation = df[df['cancellation_rate'] < 9.6]
    condition = low_cancellation['occupancy_rate'] < 70
    truth = condition.all()
    detroit_hotel = df[(df['hotel_id'] == 'HT014') & (df['city'] == 'Detroit')]
    detroit_condition = detroit_hotel['cancellation_rate'] < 9.6 and detroit_hotel['occupancy_rate'] < 70
    if truth and not detroit_hotel.empty and detroit_condition:
        expl = f"All hotels with cancellation rate <9.6% have occupancy <70%, including HT014 in Detroit."
        truth = True
    else:
        viol = low_cancellation[~condition]
        expl = f"{len(viol)} hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))}). HT014 in Detroit may not meet the condition."
        truth = False
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Among star level 4 hotels, those with occupancy rates above 80% have bookings per month exceeding 900, while those below 80% have fewer than 850 bookings."""
    star_4 = df[df['star_level'] == 4]
    high_occupancy = star_4[star_4['occupancy_rate'] > 80]
    low_occupancy = star_4[star_4['occupancy_rate'] <= 80]
    condition_high = high_occupancy['bookings_month'] > 900
    condition_low = low_occupancy['bookings_month'] < 850
    truth_high = condition_high.all()
    truth_low = condition_low.all()
    truth = truth_high and truth_low
    if truth:
        expl = f"All star 4 hotels with occupancy >80% have bookings >900 and those <=80% have <850."
    else:
        viol_high = high_occupancy[~condition_high]
        viol_low = low_occupancy[~condition_low]
        expl = f"{len(viol_high)} hotels with high occupancy violate the rule (bookings_month: {', '.join(map(str, viol_high['bookings_month'].tolist()))}), {len(viol_low)} hotels with low occupancy violate the rule (bookings_month: {', '.join(map(str, viol_low['bookings_month'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Every hotel with a star level of 5 has a cancellation rate exceeding 13%, whereas star level 3 hotels have cancellation rates below 11%."""
    star_5 = df[df['star_level'] == 5]
    star_3 = df[df['star_level'] == 3]
    condition_5 = star_5['cancellation_rate'] > 13
    condition_3 = star_3['cancellation_rate'] < 11
    truth_5 = condition_5.all()
    truth_3 = condition_3.all()
    truth = truth_5 and truth_3
    if truth:
        expl = f"All 5-star hotels have cancellation rate >13% and all 3-star hotels have cancellation rate <11%."
    else:
        viol_5 = star_5[~condition_5]
        viol_3 = star_3[~condition_3]
        expl = f"{len(viol_5)} 5-star hotels violate the rule (cancellation rates: {', '.join(map(str, viol_5['cancellation_rate'].tolist()))}), {len(viol_3)} 3-star hotels violate the rule (cancellation rates: {', '.join(map(str, viol_3['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. For hotels in cities with average nightly rates between $130–$140, cancellation rates are consistently between 10.5%–11.4%."""
    hotels_in_range = df[(df['avg_nightly_rate'] >= 130) & (df['avg_nightly_rate'] <= 140)]
    condition = (hotels_in_range['cancellation_rate'] >= 10.5) & (hotels_in_range['cancellation_rate'] <= 11.4)
    truth = condition.all()
    if truth:
        expl = f"All {len(hotels_in_range)} hotels in the $130–$140 range have cancellation rates between 10.5%–11.4%."
    else:
        viol = hotels_in_range[~condition]
        expl = f"{len(viol)} hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel’s staff count is below 30, its star level is strictly less than 4, and its average nightly rate is below $130."""
    low_staff = df[df['staff_count'] < 30]
    condition = (low_staff['star_level'] < 4) & (low_staff['avg_nightly_rate'] < 130)
    truth = condition.all()
    if truth:
        expl = f"All {len(low_staff)} hotels with staff_count <30 meet the criteria."
    else:
        viol = low_staff[~condition]
        expl = f"{len(viol)} hotels violate the rule (star_level: {', '.join(map(str, viol['star_level'].tolist()))}, avg_nightly_rate: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. The top three hotels by bookings per month (Boston, Chicago, Seattle) all have star levels of 4 or 5 and occupancy rates above 80%."""
    top_hotels = df.sort_values(by='bookings_month', ascending=False).head(3)
    condition = (top_hotels['city'].isin(['Boston', 'Chicago', 'Seattle'])) & \
                (top_hotels['star_level'].isin([4,5])) & \
                (top_hotels['occupancy_rate'] > 80)
    truth = condition.all()
    if truth:
        expl = f"The top 3 hotels by bookings_month meet the criteria."
    else:
        viol = top_hotels[~condition]
        expl = f"{len(viol)} hotels violate the rule (cities: {', '.join(map(str, viol['city'].tolist()))}, star_levels: {', '.join(map(str, viol['star_level'].tolist()))}, occupancy_rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_7.csv")
    df['occupancy_rate'] = pd.to_numeric(df['occupancy_rate'].str.replace('%', ''), errors='coerce')
    df['cancellation_rate'] = pd.to_numeric(df['cancellation_rate'].str.replace('%', ''), errors='coerce')
    df['avg_nightly_rate'] = pd.to_numeric(df['avg_nightly_rate'].str.replace('$', '').str.replace(',', ''), errors='coerce')
    df['staff_count'] = pd.to_numeric(df['staff_count'], errors='coerce').astype(int)
    df['star_level'] = pd.to_numeric(df['star_level'], errors='coerce').astype(int)
    df['bookings_month'] = pd.to_numeric(df['bookings_month'], errors='coerce').astype(int)
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
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()