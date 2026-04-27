import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. If a hotel's occupancy rate exceeds 80%, then its star level is at least 4."""
    high_occ = df[df["occupancy_rate"] > 80]
    if high_occ.empty:
        return True, "No hotels exceed 80% occupancy, so the condition holds vacuously."
    violations = high_occ[high_occ["star_level"] < 4]
    truth = violations.empty
    if truth:
        expl = f"All {len(high_occ)} hotels with >80% occupancy have star level >=4."
    else:
        viol = violations
        expl = f"{len(viol)} hotels violate the rule: {viol[['hotel_id','city','occupancy_rate','star_level']].to_dict(orient='records')}."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hotels with a cancellation rate below 10% have an average nightly rate above $160."""
    low_cancel = df[df["cancellation_rate"] < 10]
    if low_cancel.empty:
        return True, "No hotels have cancellation rate below 10%, so the condition holds vacuously."
    violations = low_cancel[low_cancel["avg_nightly_rate"] <= 160]
    truth = violations.empty
    if truth:
        expl = f"All {len(low_cancel)} hotels with cancellation rate <10% have avg nightly rate >$160."
    else:
        viol = violations
        expl = f"{len(viol)} hotels violate the rule: {viol[['hotel_id','city','cancellation_rate','avg_nightly_rate']].to_dict(orient='records')}."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. In each city that has hotels with different star levels (Denver and Austin), the higher‑star hotel has a higher average nightly rate than the lower‑star hotel."""
    cities = df.groupby("city")["star_level"].nunique()
    multi_star_cities = cities[cities > 1].index.tolist()
    if not multi_star_cities:
        return True, "No city has hotels with different star levels, so the condition holds vacuously."
    failures = []
    for city in multi_star_cities:
        city_df = df[df["city"] == city]
        max_star = city_df["star_level"].max()
        min_star = city_df["star_level"].min()
        max_rate = city_df[city_df["star_level"] == max_star]["avg_nightly_rate"].max()
        min_rate = city_df[city_df["star_level"] == min_star]["avg_nightly_rate"].min()
        if max_rate <= min_rate:
            failures.append({"city": city, "max_star": max_star, "min_star": min_star,
                             "max_rate": max_rate, "min_rate": min_rate})
    truth = not failures
    if truth:
        expl = f"All {len(multi_star_cities)} cities with multiple star levels satisfy the rule."
    else:
        expl = f"Cities failing the rule: {failures}."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hotels with bookings_month greater than 900 have occupancy rates above 75%."""
    high_bookings = df[df["bookings_month"] > 900]
    if high_bookings.empty:
        return True, "No hotels have bookings_month >900, so the condition holds vacuously."
    violations = high_bookings[high_bookings["occupancy_rate"] <= 75]
    truth = violations.empty
    if truth:
        expl = f"All {len(high_bookings)} hotels with bookings_month >900 have occupancy >75%."
    else:
        viol = violations
        expl = f"{len(viol)} hotels violate the rule: {viol[['hotel_id','city','bookings_month','occupancy_rate']].to_dict(orient='records')}."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. The 4‑star hotel in Denver has both a higher average nightly rate ($164.7) and a higher occupancy rate (75.8%) than the 3‑star Denver hotel ($119.5, 72.2%)."""
    den4 = df[(df["city"] == "Denver") & (df["star_level"] == 4)]
    den3 = df[(df["city"] == "Denver") & (df["star_level"] == 3)]
    if den4.empty or den3.empty:
        return False, f"Required Denver hotels not found: 4-star present={not den4.empty}, 3-star present={not den3.empty}."
    # Use first row if multiple
    den4_row = den4.iloc[0]
    den3_row = den3.iloc[0]
    cond_rate = den4_row["avg_nightly_rate"] > 164.7
    cond_occ = den4_row["occupancy_rate"] > 75.8
    cond_rate3 = den3_row["avg_nightly_rate"] == 119.5
    cond_occ3 = den3_row["occupancy_rate"] == 72.2
    truth = cond_rate and cond_occ and cond_rate3 and cond_occ3
    if truth:
        expl = ("4-star Denver hotel meets the specified rates and occupancy, and 3-star Denver hotel matches the given values.")
    else:
        expl = (f"4-star Denver rates/occ: {den4_row['avg_nightly_rate']}, {den4_row['occupancy_rate']}; "
                f"3-star Denver rates/occ: {den3_row['avg_nightly_rate']}, {den3_row['occupancy_rate']}.")
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Among 3‑star hotels, the highest occupancy rate is 78.8% (Portland) and the lowest is 68.0% (Seattle)."""
    three_star = df[df["star_level"] == 3]
    if three_star.empty:
        return False, "No 3-star hotels in dataset."
    max_occ = three_star["occupancy_rate"].max()
    min_occ = three_star["occupancy_rate"].min()
    max_city = three_star[three_star["occupancy_rate"] == max_occ]["city"].iloc[0]
    min_city = three_star[three_star["occupancy_rate"] == min_occ]["city"].iloc[0]
    truth = (round(max_occ,1) == 78.8 and max_city == "Portland" and
             round(min_occ,1) == 68.0 and min_city == "Seattle")
    if truth:
        expl = f"Max occupancy 78.8% in Portland, min 68.0% in Seattle."
    else:
        expl = (f"Computed max {max_occ}% in {max_city}, min {min_occ}% in {min_city}.")
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. The range of occupancy rates for 4‑star hotels spans from 65.0% (Austin) to 86.6% (Dallas)."""
    four_star = df[df["star_level"] == 4]
    if four_star.empty:
        return False, "No 4-star hotels in dataset."
    min_occ = four_star["occupancy_rate"].min()
    max_occ = four_star["occupancy_rate"].max()
    min_city = four_star[four_star["occupancy_rate"] == min_occ]["city"].iloc[0]
    max_city = four_star[four_star["occupancy_rate"] == max_occ]["city"].iloc[0]
    truth = (round(min_occ,1) == 65.0 and min_city == "Austin" and
             round(max_occ,1) == 86.6 and max_city == "Dallas")
    if truth:
        expl = f"Min 65.0% in Austin, max 86.6% in Dallas."
    else:
        expl = (f"Computed min {min_occ}% in {min_city}, max {max_occ}% in {max_city}.")
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_65.csv")
    # Convert numeric columns safely
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')
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