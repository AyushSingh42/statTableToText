import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hotels in Denver have an average nightly rate greater than $170."""
    denver = df[df["city"] == "denver"]
    if denver.empty:
        return True, "No hotels in Denver, statement vacuously true."
    condition = denver["avg_nightly_rate"] > 170
    truth = condition.all()
    if truth:
        return True, f"All {len(denver)} Denver hotels have avg nightly rate >170."
    else:
        viol = denver[~condition]
        return False, f"{len(viol)} Denver hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate']))})."

def stmt_2(df: pd.DataFrame):
    """2. If a hotel is in Atlanta, then its occupancy rate is greater than 84%."""
    atlanta = df[df["city"] == "atlanta"]
    if atlanta.empty:
        return True, "No hotels in Atlanta, statement vacuously true."
    condition = atlanta["occupancy_rate"] > 84
    truth = condition.all()
    if truth:
        return True, f"All {len(atlanta)} Atlanta hotels have occupancy >84%."
    else:
        viol = atlanta[~condition]
        return False, f"{len(viol)} Atlanta hotels violate the rule (occupancies: {', '.join(map(str, viol['occupancy_rate']))})."

def stmt_3(df: pd.DataFrame):
    """3. All hotels with a star level of 5 have an average nightly rate greater than $175."""
    star5 = df[df["star_level"] == 5]
    if star5.empty:
        return True, "No star level 5 hotels, statement vacuously true."
    condition = star5["avg_nightly_rate"] > 175
    truth = condition.all()
    if truth:
        return True, f"All {len(star5)} star 5 hotels have avg nightly rate >175."
    else:
        viol = star5[~condition]
        return False, f"{len(viol)} star 5 hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate']))})."

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one hotel in Phoenix with a cancellation rate greater than 15%."""
    phoenix = df[df["city"] == "phoenix"]
    condition = phoenix["cancellation_rate"] > 15
    truth = condition.any()
    if truth:
        count = phoenix[condition].shape[0]
        return True, f"{count} Phoenix hotel(s) have cancellation rate >15%."
    else:
        return False, "No Phoenix hotel has cancellation rate >15%."

def stmt_5(df: pd.DataFrame):
    """5. If a hotel is in Chicago, then its staff count is less than 40."""
    chicago = df[df["city"] == "chicago"]
    if chicago.empty:
        return True, "No hotels in Chicago, statement vacuously true."
    condition = chicago["staff_count"] < 40
    truth = condition.all()
    if truth:
        return True, f"All {len(chicago)} Chicago hotels have staff count <40."
    else:
        viol = chicago[~condition]
        return False, f"{len(viol)} Chicago hotels violate the rule (staff counts: {', '.join(map(str, viol['staff_count']))})."

def stmt_6(df: pd.DataFrame):
    """6. All hotels with an occupancy rate greater than 85% have a star level of 4 or 5."""
    high_occ = df[df["occupancy_rate"] > 85]
    if high_occ.empty:
        return True, "No hotels with occupancy >85%, statement vacuously true."
    condition = high_occ["star_level"].isin([4,5])
    truth = condition.all()
    if truth:
        return True, f"All {len(high_occ)} hotels with occupancy >85% have star level 4 or 5."
    else:
        viol = high_occ[~condition]
        return False, f"{len(viol)} hotels with occupancy >85% violate the rule (star levels: {', '.join(map(str, viol['star_level']))})."

def stmt_7(df: pd.DataFrame):
    """7. Most hotels in the dataset have an average nightly rate greater than $150."""
    condition = df["avg_nightly_rate"] > 150
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% of hotels have avg nightly rate >150."
    else:
        return False, f"Only {proportion*100:.1f}% of hotels have avg nightly rate >150."

def stmt_8(df: pd.DataFrame):
    """8. If a hotel is in Boston, then its occupancy rate is less than 80%."""
    boston = df[df["city"] == "boston"]
    if boston.empty:
        return True, "No hotels in Boston, statement vacuously true."
    condition = boston["occupancy_rate"] < 80
    truth = condition.all()
    if truth:
        return True, f"All {len(boston)} Boston hotels have occupancy <80%."
    else:
        viol = boston[~condition]
        return False, f"{len(viol)} Boston hotels violate the rule (occupancies: {', '.join(map(str, viol['occupancy_rate']))})."

def stmt_9(df: pd.DataFrame):
    """9. All hotels with a staff count greater than 40 have a star level of 4."""
    high_staff = df[df["staff_count"] > 40]
    if high_staff.empty:
        return True, "No hotels with staff count >40, statement vacuously true."
    condition = high_staff["star_level"] == 4
    truth = condition.all()
    if truth:
        return True, f"All {len(high_staff)} hotels with staff >40 have star level 4."
    else:
        viol = high_staff[~condition]
        return False, f"{len(viol)} hotels with staff >40 violate the rule (star levels: {', '.join(map(str, viol['star_level']))})."

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one hotel in Atlanta with an occupancy rate greater than 87%."""
    atlanta = df[df["city"] == "atlanta"]
    condition = atlanta["occupancy_rate"] > 87
    truth = condition.any()
    if truth:
        count = atlanta[condition].shape[0]
        return True, f"{count} Atlanta hotel(s) have occupancy >87%."
    else:
        return False, "No Atlanta hotel has occupancy >87%."

def stmt_11(df: pd.DataFrame):
    """11. If a hotel has a star level of 3, then its average nightly rate is less than $190."""
    star3 = df[df["star_level"] == 3]
    if star3.empty:
        return True, "No star level 3 hotels, statement vacuously true."
    condition = star3["avg_nightly_rate"] < 190
    truth = condition.all()
    if truth:
        return True, f"All {len(star3)} star 3 hotels have avg nightly rate <190."
    else:
        viol = star3[~condition]
        return False, f"{len(viol)} star 3 hotels violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate']))})."

def stmt_12(df: pd.DataFrame):
    """12. All hotels with a cancellation rate less than 10% have a star level of 4."""
    low_cancel = df[df["cancellation_rate"] < 10]
    if low_cancel.empty:
        return True, "No hotels with cancellation rate <10%, statement vacuously true."
    condition = low_cancel["star_level"] == 4
    truth = condition.all()
    if truth:
        return True, f"All {len(low_cancel)} hotels with cancellation <10% have star level 4."
    else:
        viol = low_cancel[~condition]
        return False, f"{len(viol)} hotels with cancellation <10% violate the rule (star levels: {', '.join(map(str, viol['star_level']))})."

def stmt_13(df: pd.DataFrame):
    """13. Most hotels in the dataset have a staff count greater than 30."""
    condition = df["staff_count"] > 30
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% of hotels have staff count >30."
    else:
        return False, f"Only {proportion*100:.1f}% of hotels have staff count >30."

def stmt_14(df: pd.DataFrame):
    """14. If a hotel is in Denver, then its cancellation rate is less than 10%."""
    denver = df[df["city"] == "denver"]
    if denver.empty:
        return True, "No hotels in Denver, statement vacuously true."
    condition = denver["cancellation_rate"] < 10
    truth = condition.all()
    if truth:
        return True, f"All {len(denver)} Denver hotels have cancellation rate <10%."
    else:
        viol = denver[~condition]
        return False, f"{len(viol)} Denver hotels violate the rule (cancellation rates: {', '.join(map(str, viol['cancellation_rate']))})."

def stmt_15(df: pd.DataFrame):
    """15. All hotels with an occupancy rate greater than 80% have an average nightly rate greater than $120."""
    high_occ = df[df["occupancy_rate"] > 80]
    if high_occ.empty:
        return True, "No hotels with occupancy >80%, statement vacuously true."
    condition = high_occ["avg_nightly_rate"] > 120
    truth = condition.all()
    if truth:
        return True, f"All {len(high_occ)} hotels with occupancy >80% have avg nightly rate >120."
    else:
        viol = high_occ[~condition]
        return False, f"{len(viol)} hotels with occupancy >80% violate the rule (rates: {', '.join(map(str, viol['avg_nightly_rate']))})."

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one hotel in Phoenix with a staff count greater than 40."""
    phoenix = df[df["city"] == "phoenix"]
    condition = phoenix["staff_count"] > 40
    truth = condition.any()
    if truth:
        count = phoenix[condition].shape[0]
        return True, f"{count} Phoenix hotel(s) have staff count >40."
    else:
        return False, "No Phoenix hotel has staff count >40."

def stmt_17(df: pd.DataFrame):
    """17. If a hotel has a star level of 5, then its occupancy rate is greater than 75%."""
    star5 = df[df["star_level"] == 5]
    if star5.empty:
        return True, "No star level 5 hotels, statement vacuously true."
    condition = star5["occupancy_rate"] > 75
    truth = condition.all()
    if truth:
        return True, f"All {len(star5)} star 5 hotels have occupancy >75%."
    else:
        viol = star5[~condition]
        return False, f"{len(viol)} star 5 hotels violate the rule (occupancies: {', '.join(map(str, viol['occupancy_rate']))})."

def stmt_18(df: pd.DataFrame):
    """18. All hotels with an average nightly rate greater than $200 have a star level of 5."""
    high_rate = df[df["avg_nightly_rate"] > 200]
    if high_rate.empty:
        return True, "No hotels with avg nightly rate >200, statement vacuously true."
    condition = high_rate["star_level"] == 5
    truth = condition.all()
    if truth:
        return True, f"All {len(high_rate)} hotels with avg nightly rate >200 have star level 5."
    else:
        viol = high_rate[~condition]
        return False, f"{len(viol)} hotels with avg nightly rate >200 violate the rule (star levels: {', '.join(map(str, viol['star_level']))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_95.csv")

    # Convert numeric columns safely
    for col in df.columns:
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
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
        (18, stmt_18),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()