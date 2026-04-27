import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Austin have a star level of 5."""
    austin_hotels = df[df['city'] == 'austin']
    if austin_hotels.empty:
        truth = True
        expl = "No hotels in Austin found, so vacuously true."
    else:
        all_five_star = (austin_hotels['star_level'] == 5).all()
        truth = all_five_star
        if all_five_star:
            expl = f"All {len(austin_hotels)} Austin hotels have 5 stars."
        else:
            viol = austin_hotels[austin_hotels['star_level']!= 5]
            expl = f"{len(viol)} Austin hotels do not have 5 stars (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Phoenix, then its star level is 3."""
    phoenix_hotels = df[df['city'] == 'phoenix']
    if phoenix_hotels.empty:
        truth = True
        expl = "No hotels in Phoenix found, so vacuously true."
    else:
        all_three_star = (phoenix_hotels['star_level'] == 3).all()
        truth = all_three_star
        if all_three_star:
            expl = f"All {len(phoenix_hotels)} Phoenix hotels have 3 stars."
        else:
            viol = phoenix_hotels[phoenix_hotels['star_level']!= 3]
            expl = f"{len(viol)} Phoenix hotels do not have 3 stars (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hotels with an occupancy rate greater than 80% have a staff count greater than 30."""
    high_occ = df[df['occupancy_rate'] > 80]
    if high_occ.empty:
        truth = True
        expl = "No hotels with occupancy >80%, so vacuously true."
    else:
        sufficient_staff = (high_occ['staff_count'] > 30).all()
        truth = sufficient_staff
        if sufficient_staff:
            expl = f"All {len(high_occ)} high occupancy hotels have staff >30."
        else:
            viol = high_occ[high_occ['staff_count'] <= 30]
            expl = f"{len(viol)} high occupancy hotels have staff <=30 (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a hotel is in Chicago, then its average nightly rate is less than $200."""
    chicago_hotels = df[df['city'] == 'chicago']
    if chicago_hotels.empty:
        truth = True
        expl = "No hotels in Chicago found, so vacuously true."
    else:
        below_200 = (chicago_hotels['avg_nightly_rate'] < 200).all()
        truth = below_200
        if below_200:
            expl = f"All {len(chicago_hotels)} Chicago hotels have rate < $200."
        else:
            viol = chicago_hotels[chicago_hotels['avg_nightly_rate'] >= 200]
            expl = f"{len(viol)} Chicago hotels have rate >= $200 (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. There exists at least one hotel in Boston with a cancellation rate greater than 14%."""
    boston_hotels = df[df['city'] == 'boston']
    if boston_hotels.empty:
        truth = False
        expl = "No hotels in Boston found."
    else:
        high_cancel = (boston_hotels['cancellation_rate'] > 14).any()
        truth = high_cancel
        if high_cancel:
            viol = boston_hotels[boston_hotels['cancellation_rate'] > 14]
            expl = f"At least one Boston hotel has cancellation rate >14% (rate: {viol.iloc[0]['cancellation_rate']})."
        else:
            expl = f"No Boston hotels have cancellation rate >14% (max: {boston_hotels['cancellation_rate'].max()})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All hotels with a staff count greater than 35 have an occupancy rate greater than 70%."""
    high_staff = df[df['staff_count'] > 35]
    if high_staff.empty:
        truth = True
        expl = "No hotels with staff >35, so vacuously true."
    else:
        high_occ = (high_staff['occupancy_rate'] > 70).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(high_staff)} high staff hotels have occupancy >70%."
        else:
            viol = high_staff[high_staff['occupancy_rate'] <= 70]
            expl = f"{len(viol)} high staff hotels have occupancy <=70% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a hotel is in Austin and has a staff count greater than 30, then its occupancy rate is greater than 70%."""
    austin_high_staff = df[(df['city'] == 'austin') & (df['staff_count'] > 30)]
    if austin_high_staff.empty:
        truth = True
        expl = "No Austin hotels with staff >30, so vacuously true."
    else:
        high_occ = (austin_high_staff['occupancy_rate'] > 70).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(austin_high_staff)} Austin high staff hotels have occupancy >70%."
        else:
            viol = austin_high_staff[austin_high_staff['occupancy_rate'] <= 70]
            expl = f"{len(viol)} Austin high staff hotels have occupancy <=70% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most hotels in the dataset have an occupancy rate greater than 70%."""
    total = len(df)
    high_occ = (df['occupancy_rate'] > 70).sum()
    most = high_occ > total / 2
    truth = most
    if most:
        expl = f"More than half ({high_occ}/{total}) of hotels have occupancy >70%."
    else:
        expl = f"Less than half ({high_occ}/{total}) of hotels have occupancy >70%."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All hotels with an average nightly rate greater than $200 have a star level of 5."""
    high_rate = df[df['avg_nightly_rate'] > 200]
    if high_rate.empty:
        truth = True
        expl = "No hotels with rate >$200, so vacuously true."
    else:
        five_star = (high_rate['star_level'] == 5).all()
        truth = five_star
        if five_star:
            expl = f"All {len(high_rate)} high rate hotels have 5 stars."
        else:
            viol = high_rate[high_rate['star_level']!= 5]
            expl = f"{len(viol)} high rate hotels do not have 5 stars (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a hotel is in Dallas, then its staff count is greater than 35."""
    dallas_hotels = df[df['city'] == 'dallas']
    if dallas_hotels.empty:
        truth = True
        expl = "No hotels in Dallas found, so vacuously true."
    else:
        high_staff = (dallas_hotels['staff_count'] > 35).all()
        truth = high_staff
        if high_staff:
            expl = f"All {len(dallas_hotels)} Dallas hotels have staff >35."
        else:
            viol = dallas_hotels[dallas_hotels['staff_count'] <= 35]
            expl = f"{len(viol)} Dallas hotels have staff <=35 (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. There exists at least one hotel in Chicago with a staff count less than 30."""
    chicago_hotels = df[df['city'] == 'chicago']
    if chicago_hotels.empty:
        truth = False
        expl = "No hotels in Chicago found."
    else:
        low_staff = (chicago_hotels['staff_count'] < 30).any()
        truth = low_staff
        if low_staff:
            viol = chicago_hotels[chicago_hotels['staff_count'] < 30]
            expl = f"At least one Chicago hotel has staff <30 (staff count: {viol.iloc[0]['staff_count']})."
        else:
            expl = f"No Chicago hotels have staff <30 (min: {chicago_hotels['staff_count'].min()})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All hotels with a cancellation rate less than 10% have a staff count greater than 30."""
    low_cancel = df[df['cancellation_rate'] < 10]
    if low_cancel.empty:
        truth = True
        expl = "No hotels with cancellation <10%, so vacuously true."
    else:
        high_staff = (low_cancel['staff_count'] > 30).all()
        truth = high_staff
        if high_staff:
            expl = f"All {len(low_cancel)} low cancellation hotels have staff >30."
        else:
            viol = low_cancel[low_cancel['staff_count'] <= 30]
            expl = f"{len(viol)} low cancellation hotels have staff <=30 (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a hotel is in Boston and has a star level of 5, then its occupancy rate is greater than 80%."""
    boston_five_star = df[(df['city'] == 'boston') & (df['star_level'] == 5)]
    if boston_five_star.empty:
        truth = True
        expl = "No Boston 5-star hotels found, so vacuously true."
    else:
        high_occ = (boston_five_star['occupancy_rate'] > 80).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(boston_five_star)} Boston 5-star hotels have occupancy >80%."
        else:
            viol = boston_five_star[boston_five_star['occupancy_rate'] <= 80]
            expl = f"{len(viol)} Boston 5-star hotels have occupancy <=80% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All hotels with a staff count greater than 40 have an occupancy rate greater than 80%."""
    high_staff = df[df['staff_count'] > 40]
    if high_staff.empty:
        truth = True
        expl = "No hotels with staff >40, so vacuously true."
    else:
        high_occ = (high_staff['occupancy_rate'] > 80).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(high_staff)} high staff hotels have occupancy >80%."
        else:
            viol = high_staff[high_staff['occupancy_rate'] <= 80]
            expl = f"{len(viol)} high staff hotels have occupancy <=80% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a hotel is in Miami, then its star level is 3."""
    miami_hotels = df[df['city'] =='miami']
    if miami_hotels.empty:
        truth = True
        expl = "No hotels in Miami found, so vacuously true."
    else:
        three_star = (miami_hotels['star_level'] == 3).all()
        truth = three_star
        if three_star:
            expl = f"All {len(miami_hotels)} Miami hotels have 3 stars."
        else:
            viol = miami_hotels[miami_hotels['star_level']!= 3]
            expl = f"{len(viol)} Miami hotels do not have 3 stars (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one hotel in Austin with a cancellation rate greater than 15%."""
    austin_hotels = df[df['city'] == 'austin']
    if austin_hotels.empty:
        truth = False
        expl = "No hotels in Austin found."
    else:
        high_cancel = (austin_hotels['cancellation_rate'] > 15).any()
        truth = high_cancel
        if high_cancel:
            viol = austin_hotels[austin_hotels['cancellation_rate'] > 15]
            expl = f"At least one Austin hotel has cancellation rate >15% (rate: {viol.iloc[0]['cancellation_rate']})."
        else:
            expl = f"No Austin hotels have cancellation rate >15% (max: {austin_hotels['cancellation_rate'].max()})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All hotels with an occupancy rate greater than 85% have a staff count less than 30."""
    high_occ = df[df['occupancy_rate'] > 85]
    if high_occ.empty:
        truth = True
        expl = "No hotels with occupancy >85%, so vacuously true."
    else:
        low_staff = (high_occ['staff_count'] < 30).all()
        truth = low_staff
        if low_staff:
            expl = f"All {len(high_occ)} high occupancy hotels have staff <30."
        else:
            viol = high_occ[high_occ['staff_count'] >= 30]
            expl = f"{len(viol)} high occupancy hotels have staff >=30 (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a hotel is in Chicago and has a staff count less than 30, then its occupancy rate is greater than 75%."""
    chicago_low_staff = df[(df['city'] == 'chicago') & (df['staff_count'] < 30)]
    if chicago_low_staff.empty:
        truth = True
        expl = "No Chicago hotels with staff <30, so vacuously true."
    else:
        high_occ = (chicago_low_staff['occupancy_rate'] > 75).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(chicago_low_staff)} Chicago low staff hotels have occupancy >75%."
        else:
            viol = chicago_low_staff[chicago_low_staff['occupancy_rate'] <= 75]
            expl = f"{len(viol)} Chicago low staff hotels have occupancy <=75% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All hotels with a star level of 3 have an average nightly rate less than $170."""
    three_star = df[df['star_level'] == 3]
    if three_star.empty:
        truth = True
        expl = "No 3-star hotels found, so vacuously true."
    else:
        below_170 = (three_star['avg_nightly_rate'] < 170).all()
        truth = below_170
        if below_170:
            expl = f"All {len(three_star)} 3-star hotels have rate < $170."
        else:
            viol = three_star[three_star['avg_nightly_rate'] >= 170]
            expl = f"{len(viol)} 3-star hotels have rate >= $170 (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a hotel is in Phoenix and has a staff count greater than 30, then its occupancy rate is greater than 65%."""
    phoenix_high_staff = df[(df['city'] == 'phoenix') & (df['staff_count'] > 30)]
    if phoenix_high_staff.empty:
        truth = True
        expl = "No Phoenix hotels with staff >30, so vacuously true."
    else:
        high_occ = (phoenix_high_staff['occupancy_rate'] > 65).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(phoenix_high_staff)} Phoenix high staff hotels have occupancy >65%."
        else:
            viol = phoenix_high_staff[phoenix_high_staff['occupancy_rate'] <= 65]
            expl = f"{len(viol)} Phoenix high staff hotels have occupancy <=65% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one hotel in Boston with a staff count greater than 35."""
    boston_hotels = df[df['city'] == 'boston']
    if boston_hotels.empty:
        truth = False
        expl = "No hotels in Boston found."
    else:
        high_staff = (boston_hotels['staff_count'] > 35).any()
        truth = high_staff
        if high_staff:
            viol = boston_hotels[boston_hotels['staff_count'] > 35]
            expl = f"At least one Boston hotel has staff >35 (staff count: {viol.iloc[0]['staff_count']})."
        else:
            expl = f"No Boston hotels have staff >35 (max: {boston_hotels['staff_count'].max()})."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. All hotels with a cancellation rate greater than 12% have a staff count greater than 30."""
    high_cancel = df[df['cancellation_rate'] > 12]
    if high_cancel.empty:
        truth = True
        expl = "No hotels with cancellation >12%, so vacuously true."
    else:
        high_staff = (high_cancel['staff_count'] > 30).all()
        truth = high_staff
        if high_staff:
            expl = f"All {len(high_cancel)} high cancellation hotels have staff >30."
        else:
            viol = high_cancel[high_cancel['staff_count'] <= 30]
            expl = f"{len(viol)} high cancellation hotels have staff <=30 (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_23(df: pd.DataFrame):
    """23. If a hotel is in Dallas and has a staff count greater than 35, then its occupancy rate is greater than 75%."""
    dallas_high_staff = df[(df['city'] == 'dallas') & (df['staff_count'] > 35)]
    if dallas_high_staff.empty:
        truth = True
        expl = "No Dallas hotels with staff >35, so vacuously true."
    else:
        high_occ = (dallas_high_staff['occupancy_rate'] > 75).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(dallas_high_staff)} Dallas high staff hotels have occupancy >75%."
        else:
            viol = dallas_high_staff[dallas_high_staff['occupancy_rate'] <= 75]
            expl = f"{len(viol)} Dallas high staff hotels have occupancy <=75% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_24(df: pd.DataFrame):
    """24. All hotels with an occupancy rate greater than 80% have a star level of 5 or 3."""
    high_occ = df[df['occupancy_rate'] > 80]
    if high_occ.empty:
        truth = True
        expl = "No hotels with occupancy >80%, so vacuously true."
    else:
        correct_stars = ((high_occ['star_level'] == 5) | (high_occ['star_level'] == 3)).all()
        truth = correct_stars
        if correct_stars:
            expl = f"All {len(high_occ)} high occupancy hotels have 5 or 3 stars."
        else:
            viol = high_occ[~((high_occ['star_level'] == 5) | (high_occ['star_level'] == 3))]
            expl = f"{len(viol)} high occupancy hotels do not have 5 or 3 stars (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_25(df: pd.DataFrame):
    """25. If a hotel is in Austin and has a star level of 5, then its occupancy rate is greater than 70%."""
    austin_five_star = df[(df['city'] == 'austin') & (df['star_level'] == 5)]
    if austin_five_star.empty:
        truth = True
        expl = "No Austin 5-star hotels found, so vacuously true."
    else:
        high_occ = (austin_five_star['occupancy_rate'] > 70).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(austin_five_star)} Austin 5-star hotels have occupancy >70%."
        else:
            viol = austin_five_star[austin_five_star['occupancy_rate'] <= 70]
            expl = f"{len(viol)} Austin 5-star hotels have occupancy <=70% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_26(df: pd.DataFrame):
    """26. There exists at least one hotel in Chicago with a cancellation rate less than 10%."""
    chicago_hotels = df[df['city'] == 'chicago']
    if chicago_hotels.empty:
        truth = False
        expl = "No hotels in Chicago found."
    else:
        low_cancel = (chicago_hotels['cancellation_rate'] < 10).any()
        truth = low_cancel
        if low_cancel:
            viol = chicago_hotels[chicago_hotels['cancellation_rate'] < 10]
            expl = f"At least one Chicago hotel has cancellation rate <10% (rate: {viol.iloc[0]['cancellation_rate']})."
        else:
            expl = f"No Chicago hotels have cancellation rate <10% (min: {chicago_hotels['cancellation_rate'].min()})."
    return truth, expl

def stmt_27(df: pd.DataFrame):
    """27. All hotels with a staff count greater than 35 have a star level of 5 or 3."""
    high_staff = df[df['staff_count'] > 35]
    if high_staff.empty:
        truth = True
        expl = "No hotels with staff >35, so vacuously true."
    else:
        correct_stars = ((high_staff['star_level'] == 5) | (high_staff['star_level'] == 3)).all()
        truth = correct_stars
        if correct_stars:
            expl = f"All {len(high_staff)} high staff hotels have 5 or 3 stars."
        else:
            viol = high_staff[~((high_staff['star_level'] == 5) | (high_staff['star_level'] == 3))]
            expl = f"{len(viol)} high staff hotels do not have 5 or 3 stars (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_28(df: pd.DataFrame):
    """28. If a hotel is in Boston and has a staff count greater than 35, then its occupancy rate is greater than 75%."""
    boston_high_staff = df[(df['city'] == 'boston') & (df['staff_count'] > 35)]
    if boston_high_staff.empty:
        truth = True
        expl = "No Boston hotels with staff >35, so vacuously true."
    else:
        high_occ = (boston_high_staff['occupancy_rate'] > 75).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(boston_high_staff)} Boston high staff hotels have occupancy >75%."
        else:
            viol = boston_high_staff[boston_high_staff['occupancy_rate'] <= 75]
            expl = f"{len(viol)} Boston high staff hotels have occupancy <=75% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_29(df: pd.DataFrame):
    """29. All hotels with an average nightly rate greater than $190 have a star level of 5."""
    high_rate = df[df['avg_nightly_rate'] > 190]
    if high_rate.empty:
        truth = True
        expl = "No hotels with rate >$190, so vacuously true."
    else:
        five_star = (high_rate['star_level'] == 5).all()
        truth = five_star
        if five_star:
            expl = f"All {len(high_rate)} high rate hotels have 5 stars."
        else:
            viol = high_rate[high_rate['star_level']!= 5]
            expl = f"{len(viol)} high rate hotels do not have 5 stars (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_30(df: pd.DataFrame):
    """30. If a hotel is in Miami and has a staff count greater than 30, then its occupancy rate is greater than 65%."""
    miami_high_staff = df[(df['city'] =='miami') & (df['staff_count'] > 30)]
    if miami_high_staff.empty:
        truth = True
        expl = "No Miami hotels with staff >30, so vacuously true."
    else:
        high_occ = (miami_high_staff['occupancy_rate'] > 65).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(miami_high_staff)} Miami high staff hotels have occupancy >65%."
        else:
            viol = miami_high_staff[miami_high_staff['occupancy_rate'] <= 65]
            expl = f"{len(viol)} Miami high staff hotels have occupancy <=65% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_31(df: pd.DataFrame):
    """31. There exists at least one hotel in Austin with a staff count greater than 40."""
    austin_hotels = df[df['city'] == 'austin']
    if austin_hotels.empty:
        truth = False
        expl = "No hotels in Austin found."
    else:
        high_staff = (austin_hotels['staff_count'] > 40).any()
        truth = high_staff
        if high_staff:
            viol = austin_hotels[austin_hotels['staff_count'] > 40]
            expl = f"At least one Austin hotel has staff >40 (staff count: {viol.iloc[0]['staff_count']})."
        else:
            expl = f"No Austin hotels have staff >40 (max: {austin_hotels['staff_count'].max()})."
    return truth, expl

def stmt_32(df: pd.DataFrame):
    """32. All hotels with a cancellation rate greater than 13% have a staff count greater than 30."""
    high_cancel = df[df['cancellation_rate'] > 13]
    if high_cancel.empty:
        truth = True
        expl = "No hotels with cancellation >13%, so vacuously true."
    else:
        high_staff = (high_cancel['staff_count'] > 30).all()
        truth = high_staff
        if high_staff:
            expl = f"All {len(high_cancel)} high cancellation hotels have staff >30."
        else:
            viol = high_cancel[high_cancel['staff_count'] <= 30]
            expl = f"{len(viol)} high cancellation hotels have staff <=30 (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_33(df: pd.DataFrame):
    """33. If a hotel is in Chicago and has a star level of 5, then its occupancy rate is greater than 75%."""
    chicago_five_star = df[(df['city'] == 'chicago') & (df['star_level'] == 5)]
    if chicago_five_star.empty:
        truth = True
        expl = "No Chicago 5-star hotels found, so vacuously true."
    else:
        high_occ = (chicago_five_star['occupancy_rate'] > 75).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(chicago_five_star)} Chicago 5-star hotels have occupancy >75%."
        else:
            viol = chicago_five_star[chicago_five_star['occupancy_rate'] <= 75]
            expl = f"{len(viol)} Chicago 5-star hotels have occupancy <=75% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_34(df: pd.DataFrame):
    """34. All hotels with a staff count greater than 40 have a star level of 5."""
    high_staff = df[df['staff_count'] > 40]
    if high_staff.empty:
        truth = True
        expl = "No hotels with staff >40, so vacuously true."
    else:
        five_star = (high_staff['star_level'] == 5).all()
        truth = five_star
        if five_star:
            expl = f"All {len(high_staff)} high staff hotels have 5 stars."
        else:
            viol = high_staff[high_staff['star_level']!= 5]
            expl = f"{len(viol)} high staff hotels do not have 5 stars (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_35(df: pd.DataFrame):
    """35. If a hotel is in Boston and has a star level of 5, then its staff count is greater than 35."""
    boston_five_star = df[(df['city'] == 'boston') & (df['star_level'] == 5)]
    if boston_five_star.empty:
        truth = True
        expl = "No Boston 5-star hotels found, so vacuously true."
    else:
        high_staff = (boston_five_star['staff_count'] > 35).all()
        truth = high_staff
        if high_staff:
            expl = f"All {len(boston_five_star)} Boston 5-star hotels have staff >35."
        else:
            viol = boston_five_star[boston_five_star['staff_count'] <= 35]
            expl = f"{len(viol)} Boston 5-star hotels have staff <=35 (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_36(df: pd.DataFrame):
    """36. There exists at least one hotel in Phoenix with a cancellation rate greater than 12%."""
    phoenix_hotels = df[df['city'] == 'phoenix']
    if phoenix_hotels.empty:
        truth = False
        expl = "No hotels in Phoenix found."
    else:
        high_cancel = (phoenix_hotels['cancellation_rate'] > 12).any()
        truth = high_cancel
        if high_cancel:
            viol = phoenix_hotels[phoenix_hotels['cancellation_rate'] > 12]
            expl = f"At least one Phoenix hotel has cancellation rate >12% (rate: {viol.iloc[0]['cancellation_rate']})."
        else:
            expl = f"No Phoenix hotels have cancellation rate >12% (max: {phoenix_hotels['cancellation_rate'].max()})."
    return truth, expl

def stmt_37(df: pd.DataFrame):
    """37. All hotels with an occupancy rate greater than 85% have a star level of 5."""
    high_occ = df[df['occupancy_rate'] > 85]
    if high_occ.empty:
        truth = True
        expl = "No hotels with occupancy >85%, so vacuously true."
    else:
        five_star = (high_occ['star_level'] == 5).all()
        truth = five_star
        if five_star:
            expl = f"All {len(high_occ)} high occupancy hotels have 5 stars."
        else:
            viol = high_occ[high_occ['star_level']!= 5]
            expl = f"{len(viol)} high occupancy hotels do not have 5 stars (star levels: {', '.join(map(str, viol['star_level'].tolist()))})."
    return truth, expl

def stmt_38(df: pd.DataFrame):
    """38. If a hotel is in Dallas and has a star level of 3, then its occupancy rate is greater than 75%."""
    dallas_three_star = df[(df['city'] == 'dallas') & (df['star_level'] == 3)]
    if dallas_three_star.empty:
        truth = True
        expl = "No Dallas 3-star hotels found, so vacuously true."
    else:
        high_occ = (dallas_three_star['occupancy_rate'] > 75).all()
        truth = high_occ
        if high_occ:
            expl = f"All {len(dallas_three_star)} Dallas 3-star hotels have occupancy >75%."
        else:
            viol = dallas_three_star[dallas_three_star['occupancy_rate'] <= 75]
            expl = f"{len(viol)} Dallas 3-star hotels have occupancy <=75% (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_39(df: pd.DataFrame):
    """39. All hotels with a staff count greater than 35 have an average nightly rate greater than $140."""
    high_staff = df[df['staff_count'] > 35]
    if high_staff.empty:
        truth = True
        expl = "No hotels with staff >35, so vacuously true."
    else:
        high_rate = (high_staff['avg_nightly_rate'] > 140).all()
        truth = high