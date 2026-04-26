import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Austin have an average nightly rate greater than $180."""
    austin_hotels = df[df['city'] == 'austin']
    if austin_hotels.empty:
        truth = True
        expl = "No hotels in Austin found."
    else:
        condition = austin_hotels['avg_nightly_rate'] > 180
        truth = condition.all()
        if truth:
            expl = f"All {len(austin_hotels)} Austin hotels have nightly rates > $180."
        else:
            viol = austin_hotels[~condition]
            expl = f"{len(viol)} Austin hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Austin, then its staff count is greater than or equal to 37."""
    austin_hotels = df[df['city'] == 'austin']
    if austin_hotels.empty:
        truth = True
        expl = "No hotels in Austin found."
    else:
        condition = austin_hotels['staff_count'] >= 37
        truth = condition.all()
        if truth:
            expl = f"All {len(austin_hotels)} Austin hotels have staff count >= 37."
        else:
            viol = austin_hotels[~condition]
            expl = f"{len(viol)} Austin hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one hotel in Atlanta with an occupancy rate greater than 85% and an average nightly rate less than $150."""
    atlanta_hotels = df[df['city'] == 'atlanta']
    if atlanta_hotels.empty:
        truth = False
        expl = "No hotels in Atlanta found."
    else:
        condition = (atlanta_hotels['occupancy_rate'] > 85) & (atlanta_hotels['avg_nightly_rate'] < 150)
        truth = condition.any()
        if truth:
            expl = "At least one Atlanta hotel meets both criteria."
        else:
            expl = "No Atlanta hotels meet both criteria."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with a star level of 5 have an occupancy rate greater than 70%."""
    five_star_hotels = df[df['star_level'] == 5]
    if five_star_hotels.empty:
        truth = True
        expl = "No 5-star hotels found."
    else:
        condition = five_star_hotels['occupancy_rate'] > 70
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star_hotels)} 5-star hotels have occupancy rate > 70%."
        else:
            viol = five_star_hotels[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a hotel has a cancellation rate less than 10%, then its staff count is greater than or equal to 34."""
    condition = (df['cancellation_rate'] < 10) & (df['staff_count'] < 34)
    truth = not condition.any()
    if truth:
        expl = "All hotels with cancellation rate < 10% have staff count >= 34."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (cancellation rate < 10% but staff count < 34)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most hotels have a bookings month greater than 600."""
    condition = df['bookings_month'] > 600
    total = len(df)
    satisfied = condition.sum()
    truth = satisfied > total / 2
    if truth:
        expl = f"More than half ({satisfied}/{total}) of hotels have bookings_month > 600."
    else:
        expl = f"Less than half ({satisfied}/{total}) of hotels have bookings_month > 600."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hotels in Miami have a staff count greater than or equal to 36."""
    miami_hotels = df[df['city'] =='miami']
    if miami_hotels.empty:
        truth = True
        expl = "No hotels in Miami found."
    else:
        condition = miami_hotels['staff_count'] >= 36
        truth = condition.all()
        if truth:
            expl = f"All {len(miami_hotels)} Miami hotels have staff count >= 36."
        else:
            viol = miami_hotels[~condition]
            expl = f"{len(viol)} Miami hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Chicago, then its average nightly rate is greater than $190."""
    chicago_hotels = df[df['city'] == 'chicago']
    if chicago_hotels.empty:
        truth = True
        expl = "No hotels in Chicago found."
    else:
        condition = chicago_hotels['avg_nightly_rate'] > 190
        truth = condition.all()
        if truth:
            expl = f"All {len(chicago_hotels)} Chicago hotels have nightly rate > $190."
        else:
            viol = chicago_hotels[~condition]
            expl = f"{len(viol)} Chicago hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one hotel in Austin with a star level of 3 and an occupancy rate less than 70%."""
    austin_hotels = df[(df['city'] == 'austin') & (df['star_level'] == 3)]
    if austin_hotels.empty:
        truth = False
        expl = "No 3-star hotels in Austin found."
    else:
        condition = austin_hotels['occupancy_rate'] < 70
        truth = condition.any()
        if truth:
            expl = "At least one Austin 3-star hotel has occupancy rate < 70%."
        else:
            expl = "No Austin 3-star hotels have occupancy rate < 70%."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All hotels with an occupancy rate greater than 80% have a staff count greater than or equal to 29."""
    condition = (df['occupancy_rate'] > 80) & (df['staff_count'] < 29)
    truth = not condition.any()
    if truth:
        expl = "All hotels with occupancy rate > 80% have staff count >= 29."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (occupancy rate > 80% but staff count < 29)."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a hotel has a star level of 5, then its average nightly rate is greater than $140."""
    five_star_hotels = df[df['star_level'] == 5]
    if five_star_hotels.empty:
        truth = True
        expl = "No 5-star hotels found."
    else:
        condition = five_star_hotels['avg_nightly_rate'] > 140
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star_hotels)} 5-star hotels have nightly rate > $140."
        else:
            viol = five_star_hotels[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most hotels in Atlanta have an occupancy rate greater than 80%."""
    atlanta_hotels = df[df['city'] == 'atlanta']
    if atlanta_hotels.empty:
        truth = True
        expl = "No hotels in Atlanta found."
    else:
        condition = atlanta_hotels['occupancy_rate'] > 80
        total = len(atlanta_hotels)
        satisfied = condition.sum()
        truth = satisfied > total / 2
        if truth:
            expl = f"More than half ({satisfied}/{total}) of Atlanta hotels have occupancy rate > 80%."
        else:
            expl = f"Less than half ({satisfied}/{total}) of Atlanta hotels have occupancy rate > 80%."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All hotels with a bookings month greater than 900 have a cancellation rate less than 12%."""
    condition = (df['bookings_month'] > 900) & (df['cancellation_rate'] >= 12)
    truth = not condition.any()
    if truth:
        expl = "All hotels with bookings_month > 900 have cancellation rate < 12%."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (bookings_month > 900 but cancellation rate >= 12%)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a hotel is in Boston, then its occupancy rate is greater than 80%."""
    boston_hotels = df[df['city'] == 'boston']
    if boston_hotels.empty:
        truth = True
        expl = "No hotels in Boston found."
    else:
        condition = boston_hotels['occupancy_rate'] > 80
        truth = condition.all()
        if truth:
            expl = f"All {len(boston_hotels)} Boston hotels have occupancy rate > 80%."
        else:
            viol = boston_hotels[~condition]
            expl = f"{len(viol)} Boston hotels violate the rule (occupancy rates: {', '.join(map(str, viol['occupancy_rate'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one hotel in Seattle with a star level of 4 and an average nightly rate less than $150."""
    seattle_hotels = df[(df['city'] =='seattle') & (df['star_level'] == 4)]
    if seattle_hotels.empty:
        truth = False
        expl = "No 4-star hotels in Seattle found."
    else:
        condition = seattle_hotels['avg_nightly_rate'] < 150
        truth = condition.any()
        if truth:
            expl = "At least one Seattle 4-star hotel has nightly rate < $150."
        else:
            expl = "No Seattle 4-star hotels have nightly rate < $150."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All hotels with a staff count greater than or equal to 40 have an occupancy rate greater than 75%."""
    condition = (df['staff_count'] >= 40) & (df['occupancy_rate'] <= 75)
    truth = not condition.any()
    if truth:
        expl = "All hotels with staff count >= 40 have occupancy rate > 75%."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (staff count >= 40 but occupancy rate <= 75%)."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a hotel has an average nightly rate less than $130, then its star level is 5."""
    condition = (df['avg_nightly_rate'] < 130) & (df['star_level']!= 5)
    truth = not condition.any()
    if truth:
        expl = "All hotels with nightly rate < $130 have star level 5."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (nightly rate < $130 but star level!= 5)."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most hotels in Miami have an occupancy rate greater than 80%."""
    miami_hotels = df[df['city'] =='miami']
    if miami_hotels.empty:
        truth = True
        expl = "No hotels in Miami found."
    else:
        condition = miami_hotels['occupancy_rate'] > 80
        total = len(miami_hotels)
        satisfied = condition.sum()
        truth = satisfied > total / 2
        if truth:
            expl = f"More than half ({satisfied}/{total}) of Miami hotels have occupancy rate > 80%."
        else:
            expl = f"Less than half ({satisfied}/{total}) of Miami hotels have occupancy rate > 80%."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All hotels with a cancellation rate less than 9% have a staff count greater than or equal to 31."""
    condition = (df['cancellation_rate'] < 9) & (df['staff_count'] < 31)
    truth = not condition.any()
    if truth:
        expl = "All hotels with cancellation rate < 9% have staff count >= 31."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (cancellation rate < 9% but staff count < 31)."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a hotel is in Dallas, then its average nightly rate is greater than $200."""
    dallas_hotels = df[df['city'] == 'dallas']
    if dallas_hotels.empty:
        truth = True
        expl = "No hotels in Dallas found."
    else:
        condition = dallas_hotels['avg_nightly_rate'] > 200
        truth = condition.all()
        if truth:
            expl = f"All {len(dallas_hotels)} Dallas hotels have nightly rate > $200."
        else:
            viol = dallas_hotels[~condition]
            expl = f"{len(viol)} Dallas hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one hotel in Chicago with a star level of 5 and an occupancy rate greater than 75%."""
    chicago_hotels = df[(df['city'] == 'chicago') & (df['star_level'] == 5)]
    if chicago_hotels.empty:
        truth = False
        expl = "No 5-star hotels in Chicago found."
    else:
        condition = chicago_hotels['occupancy_rate'] > 75
        truth = condition.any()
        if truth:
            expl = "At least one Chicago 5-star hotel has occupancy rate > 75%."
        else:
            expl = "No Chicago 5-star hotels have occupancy rate > 75%."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. All hotels with an occupancy rate greater than 85% have a bookings month greater than 600."""
    condition = (df['occupancy_rate'] > 85) & (df['bookings_month'] <= 600)
    truth = not condition.any()
    if truth:
        expl = "All hotels with occupancy rate > 85% have bookings_month > 600."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (occupancy rate > 85% but bookings_month <= 600)."
    return truth, expl

def stmt_23(df: pd.DataFrame):
    """23. If a hotel has a star level of 3, then its staff count is less than or equal to 40."""
    three_star_hotels = df[df['star_level'] == 3]
    if three_star_hotels.empty:
        truth = True
        expl = "No 3-star hotels found."
    else:
        condition = three_star_hotels['staff_count'] <= 40
        truth = condition.all()
        if truth:
            expl = f"All {len(three_star_hotels)} 3-star hotels have staff count <= 40."
        else:
            viol = three_star_hotels[~condition]
            expl = f"{len(viol)} 3-star hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_24(df: pd.DataFrame):
    """24. Most hotels in Austin have an occupancy rate greater than 70%."""
    austin_hotels = df[df['city'] == 'austin']
    if austin_hotels.empty:
        truth = True
        expl = "No hotels in Austin found."
    else:
        condition = austin_hotels['occupancy_rate'] > 70
        total = len(austin_hotels)
        satisfied = condition.sum()
        truth = satisfied > total / 2
        if truth:
            expl = f"More than half ({satisfied}/{total}) of Austin hotels have occupancy rate > 70%."
        else:
            expl = f"Less than half ({satisfied}/{total}) of Austin hotels have occupancy rate > 70%."
    return truth, expl

def stmt_25(df: pd.DataFrame):
    """25. All hotels with a bookings month greater than 800 have a cancellation rate less than 13%."""
    condition = (df['bookings_month'] > 800) & (df['cancellation_rate'] >= 13)
    truth = not condition.any()
    if truth:
        expl = "All hotels with bookings_month > 800 have cancellation rate < 13%."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (bookings_month > 800 but cancellation rate >= 13%)."
    return truth, expl

def stmt_26(df: pd.DataFrame):
    """26. If a hotel is in Atlanta, then its average nightly rate is less than $200."""
    atlanta_hotels = df[df['city'] == 'atlanta']
    if atlanta_hotels.empty:
        truth = True
        expl = "No hotels in Atlanta found."
    else:
        condition = atlanta_hotels['avg_nightly_rate'] < 200
        truth = condition.all()
        if truth:
            expl = f"All {len(atlanta_hotels)} Atlanta hotels have nightly rate < $200."
        else:
            viol = atlanta_hotels[~condition]
            expl = f"{len(viol)} Atlanta hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_27(df: pd.DataFrame):
    """27. There exists at least one hotel in Boston with a star level of 5 and an occupancy rate greater than 80%."""
    boston_hotels = df[(df['city'] == 'boston') & (df['star_level'] == 5)]
    if boston_hotels.empty:
        truth = False
        expl = "No 5-star hotels in Boston found."
    else:
        condition = boston_hotels['occupancy_rate'] > 80
        truth = condition.any()
        if truth:
            expl = "At least one Boston 5-star hotel has occupancy rate > 80%."
        else:
            expl = "No Boston 5-star hotels have occupancy rate > 80%."
    return truth, expl

def stmt_28(df: pd.DataFrame):
    """28. All hotels with a staff count greater than or equal to 45 have an occupancy rate greater than 80%."""
    condition = (df['staff_count'] >= 45) & (df['occupancy_rate'] <= 80)
    truth = not condition.any()
    if truth:
        expl = "All hotels with staff count >= 45 have occupancy rate > 80%."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (staff count >= 45 but occupancy rate <= 80%)."
    return truth, expl

def stmt_29(df: pd.DataFrame):
    """29. If a hotel has an average nightly rate greater than $220, then its star level is 3."""
    condition = (df['avg_nightly_rate'] > 220) & (df['star_level']!= 3)
    truth = not condition.any()
    if truth:
        expl = "All hotels with nightly rate > $220 have star level 3."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (nightly rate > $220 but star level!= 3)."
    return truth, expl

def stmt_30(df: pd.DataFrame):
    """30. Most hotels in Seattle have an occupancy rate greater than 75%."""
    seattle_hotels = df[df['city'] =='seattle']
    if seattle_hotels.empty:
        truth = True
        expl = "No hotels in Seattle found."
    else:
        condition = seattle_hotels['occupancy_rate'] > 75
        total = len(seattle_hotels)
        satisfied = condition.sum()
        truth = satisfied > total / 2
        if truth:
            expl = f"More than half ({satisfied}/{total}) of Seattle hotels have occupancy rate > 75%."
        else:
            expl = f"Less than half ({satisfied}/{total}) of Seattle hotels have occupancy rate > 75%."
    return truth, expl

def stmt_31(df: pd.DataFrame):
    """31. All hotels with a cancellation rate less than 10% have a bookings month greater than 650."""
    condition = (df['cancellation_rate'] < 10) & (df['bookings_month'] <= 650)
    truth = not condition.any()
    if truth:
        expl = "All hotels with cancellation rate < 10% have bookings_month > 650."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (cancellation rate < 10% but bookings_month <= 650)."
    return truth, expl

def stmt_32(df: pd.DataFrame):
    """32. If a hotel is in Denver, then its average nightly rate is greater than $200."""
    denver_hotels = df[df['city'] == 'denver']
    if denver_hotels.empty:
        truth = True
        expl = "No hotels in Denver found."
    else:
        condition = denver_hotels['avg_nightly_rate'] > 200
        truth = condition.all()
        if truth:
            expl = f"All {len(denver_hotels)} Denver hotels have nightly rate > $200."
        else:
            viol = denver_hotels[~condition]
            expl = f"{len(viol)} Denver hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_33(df: pd.DataFrame):
    """33. There exists at least one hotel in Dallas with a star level of 3 and an occupancy rate greater than 80%."""
    dallas_hotels = df[(df['city'] == 'dallas') & (df['star_level'] == 3)]
    if dallas_hotels.empty:
        truth = False
        expl = "No 3-star hotels in Dallas found."
    else:
        condition = dallas_hotels['occupancy_rate'] > 80
        truth = condition.any()
        if truth:
            expl = "At least one Dallas 3-star hotel has occupancy rate > 80%."
        else:
            expl = "No Dallas 3-star hotels have occupancy rate > 80%."
    return truth, expl

def stmt_34(df: pd.DataFrame):
    """34. All hotels with an occupancy rate greater than 80% have a staff count greater than or equal to 30."""
    condition = (df['occupancy_rate'] > 80) & (df['staff_count'] < 30)
    truth = not condition.any()
    if truth:
        expl = "All hotels with occupancy rate > 80% have staff count >= 30."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (occupancy rate > 80% but staff count < 30)."
    return truth, expl

def stmt_35(df: pd.DataFrame):
    """35. If a hotel has a star level of 5, then its bookings month is greater than 600."""
    five_star_hotels = df[df['star_level'] == 5]
    if five_star_hotels.empty:
        truth = True
        expl = "No 5-star hotels found."
    else:
        condition = five_star_hotels['bookings_month'] > 600
        truth = condition.all()
        if truth:
            expl = f"All {len(five_star_hotels)} 5-star hotels have bookings_month > 600."
        else:
            viol = five_star_hotels[~condition]
            expl = f"{len(viol)} 5-star hotels violate the rule (bookings months: {', '.join(map(str, viol['bookings_month'].tolist()))})."
    return truth, expl

def stmt_36(df: pd.DataFrame):
    """36. Most hotels in Chicago have an occupancy rate greater than 70%."""
    chicago_hotels = df[df['city'] == 'chicago']
    if chicago_hotels.empty:
        truth = True
        expl = "No hotels in Chicago found."
    else:
        condition = chicago_hotels['occupancy_rate'] > 70
        total = len(chicago_hotels)
        satisfied = condition.sum()
        truth = satisfied > total / 2
        if truth:
            expl = f"More than half ({satisfied}/{total}) of Chicago hotels have occupancy rate > 70%."
        else:
            expl = f"Less than half ({satisfied}/{total}) of Chicago hotels have occupancy rate > 70%."
    return truth, expl

def stmt_37(df: pd.DataFrame):
    """37. All hotels with a bookings month greater than 900 have an occupancy rate greater than 75%."""
    condition = (df['bookings_month'] > 900) & (df['occupancy_rate'] <= 75)
    truth = not condition.any()
    if truth:
        expl = "All hotels with bookings_month > 900 have occupancy rate > 75%."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (bookings_month > 900 but occupancy rate <= 75%)."
    return truth, expl

def stmt_38(df: pd.DataFrame):
    """38. If a hotel is in Miami, then its cancellation rate is less than 12%."""
    miami_hotels = df[df['city'] =='miami']
    if miami_hotels.empty:
        truth = True
        expl = "No hotels in Miami found."
    else:
        condition = miami_hotels['cancellation_rate'] < 12
        truth = condition.all()
        if truth:
            expl = f"All {len(miami_hotels)} Miami hotels have cancellation rate < 12%."
        else:
            viol = miami_hotels[~condition]
            expl = f"{len(viol)} Miami hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate'].tolist()))})."
    return truth, expl

def stmt_39(df: pd.DataFrame):
    """39. There exists at least one hotel in Atlanta with a star level of 5 and an average nightly rate less than $150."""
    atlanta_hotels = df[(df['city'] == 'atlanta') & (df['star_level'] == 5)]
    if atlanta_hotels.empty:
        truth = False
        expl = "No 5-star hotels in Atlanta found."
    else:
        condition = atlanta_hotels['avg_nightly_rate'] < 150
        truth = condition.any()
        if truth:
            expl = "At least one Atlanta 5-star hotel has nightly rate < $150."
        else:
            expl = "No Atlanta 5-star hotels have nightly rate < $150."
    return truth, expl

def stmt_40(df: pd.DataFrame):
    """40. All hotels with a staff count greater than or equal to 35 have an occupancy rate greater than 75%."""
    condition = (df['staff_count'] >= 35) & (df['occupancy_rate'] <= 75)
    truth = not condition.any()
    if truth:
        expl = "All hotels with staff count >= 35 have occupancy rate > 75%."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (staff count >= 35 but occupancy rate <= 75%)."
    return truth, expl

def stmt_41(df: pd.DataFrame):
    """41. If a hotel has an average nightly rate less than $140, then its star level is 5."""
    condition = (df['avg_nightly_rate'] < 140) & (df['star_level']!= 5)
    truth = not condition.any()
    if truth:
        expl = "All hotels with nightly rate < $140 have star level 5."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (nightly rate < $140 but star level!= 5)."
    return truth, expl

def stmt_42(df: pd.DataFrame):
    """42. Most hotels in Austin have a bookings month greater than 600."""
    austin_hotels = df[df['city'] == 'austin']
    if austin_hotels.empty:
        truth = True
        expl = "No hotels in Austin found."
    else:
        condition = austin_hotels['bookings_month'] > 600
        total = len(austin_hotels)
        satisfied = condition.sum()
        truth = satisfied > total / 2
        if truth:
            expl = f"More than half ({satisfied}/{total}) of Austin hotels have bookings_month > 600."
        else:
            expl = f"Less than half ({satisfied}/{total}) of Austin hotels have bookings_month > 600."
    return truth, expl

def stmt_43(df: pd.DataFrame):
    """43. All hotels with a cancellation rate less than 9% have a bookings month greater than 700."""
    condition = (df['cancellation_rate'] < 9) & (df['bookings_month'] <= 700)
    truth = not condition.any()
    if truth:
        expl = "All hotels with cancellation rate < 9% have bookings_month > 700."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (cancellation rate < 9% but bookings_month <= 700)."
    return truth, expl

def stmt_44(df: pd.DataFrame):
    """44. If a hotel is in Boston, then its staff count is greater than or equal to 34."""
    boston_hotels = df[df['city'] == 'boston']
    if boston_hotels.empty:
        truth = True
        expl = "No hotels in Boston found."
    else:
        condition = boston_hotels['staff_count'] >= 34
        truth = condition.all()
        if truth:
            expl = f"All {len(boston_hotels)} Boston hotels have staff count >= 34."
        else:
            viol = boston_hotels[~condition]
            expl = f"{len(viol)} Boston hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_45(df: pd.DataFrame):
    """45. There exists at least one hotel in Seattle with a star level of 4 and an occupancy rate greater than 80%."""
    seattle_hotels = df[(df['city'] =='seattle') & (df['star_level'] == 4)]
    if seattle_hotels.empty:
        truth = False
        expl = "No 4-star hotels in Seattle found."
    else:
        condition = seattle_hotels['occupancy_rate'] > 80
        truth = condition.any()
        if truth:
            expl = "At least one Seattle 4-star hotel has occupancy rate > 80%."
        else:
            expl = "No Seattle 4-star hotels have occupancy rate > 80%."
    return truth, expl

def stmt_46(df: pd.DataFrame):
    """46. All hotels with an occupancy rate greater than 85% have a staff count greater than or equal to 32."""
    condition = (df['occupancy_rate'] > 85) & (df['staff_count'] < 32)
    truth = not condition.any()
    if truth:
        expl = "All hotels with occupancy rate > 85% have staff count >= 32."
    else:
        viol = df[condition]
        expl = f"{len(viol)} hotels violate the rule (occupancy rate > 85% but staff count < 32)."
    return truth, expl

def stmt_47(df: pd.DataFrame):
    """47. If a hotel has a star level of 3, then its average nightly rate is greater than $190."""
    three_star_hotels = df[df['star_level'] == 3]
    if three_star_hotels.empty:
        truth = True
        expl = "No 3-star hotels found."
    else:
        condition = three_star_hotels['avg_nightly_rate'] > 190
        truth = condition.all()
        if truth:
            expl = f"All {len(three_star_hotels)} 3-star hotels have nightly rate > $190."
        else:
            viol = three_star_hotels[~condition]
            expl = f"{len(viol)} 3-star hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate'].tolist()))})."
    return truth, expl

def stmt_48(df: pd.DataFrame):
    """48. Most hotels in Miami have a bookings month greater than 700."""
    miami_hotels = df[df['city'] =='miami']
    if miami_hotels.empty:
        truth = True
        expl = "No hotels in Miami found."
    else:
        condition = miami_hotels['bookings_month'] > 700
        total = len(miami_hotels)
        satisfied