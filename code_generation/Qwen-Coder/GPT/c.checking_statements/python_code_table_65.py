import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. If a hotel's occupancy rate exceeds 80%, then its star level is at least 4."""
    condition = df["occupancy_rate"] > 80
    filtered = df[condition]
    if filtered.empty:
        expl = "No hotels exceed 80% occupancy rate."
        return True, expl
    valid = (filtered["star_level"] >= 4).all()
    if valid:
        expl = f"All {len(filtered)} hotels with >80% occupancy are 4-star or higher."
    else:
        viol = filtered[~(filtered["star_level"] >= 4)]
        expl = f"{len(viol)} hotels with >80% occupancy are not 4-star or higher."
    return valid, expl

def stmt_2(df: pd.DataFrame):
    """2. All hotels with a cancellation rate below 10% have an average nightly rate above $160."""
    condition = df["cancellation_rate"] < 10
    filtered = df[condition]
    if filtered.empty:
        expl = "No hotels have cancellation rate below 10%."
        return True, expl
    valid = (filtered["avg_nightly_rate"] > 160).all()
    if valid:
        expl = f"All {len(filtered)} hotels with <10% cancellation rate have >$160 avg nightly rate."
    else:
        viol = filtered[~(filtered["avg_nightly_rate"] > 160)]
        expl = f"{len(viol)} hotels with <10% cancellation rate have <=$160 avg nightly rate."
    return valid, expl

def stmt_3(df: pd.DataFrame):
    """3. In each city that has hotels with different star levels (Denver and Austin), the higher-star hotel has a higher average nightly rate than the lower-star hotel."""
    cities = ["denver", "austin"]
    valid = True
    expls = []
    for city in cities:
        city_data = df[df["city"].str.lower() == city]
        if city_data.empty:
            continue
        star_levels = sorted(city_data["star_level"].unique())
        if len(star_levels) < 2:
            continue
        # Get max and min star level hotels
        max_star = max(star_levels)
        min_star = min(star_levels)
        max_star_hotel = city_data[city_data["star_level"] == max_star].iloc[0]
        min_star_hotel = city_data[city_data["star_level"] == min_star].iloc[0]
        if max_star_hotel["avg_nightly_rate"] > min_star_hotel["avg_nightly_rate"]:
            expls.append(f"In {city.title()}, {max_star}-star hotel has higher rate than {min_star}-star.")
        else:
            valid = False
            expls.append(f"In {city.title()}, {max_star}-star hotel does not have higher rate than {min_star}-star.")
    if not expls:
        expl = "No cities with multiple star levels found."
        return True, expl
    return valid, "; ".join(expls)

def stmt_4(df: pd.DataFrame):
    """4. All hotels with bookings_month greater than 900 have occupancy rates above 75%."""
    condition = df["bookings_month"] > 900
    filtered = df[condition]
    if filtered.empty:
        expl = "No hotels have bookings_month > 900."
        return True, expl
    valid = (filtered["occupancy_rate"] > 75).all()
    if valid:
        expl = f"All {len(filtered)} hotels with >900 bookings/month have >75% occupancy."
    else:
        viol = filtered[~(filtered["occupancy_rate"] > 75)]
        expl = f"{len(viol)} hotels with >900 bookings/month have <=75% occupancy."
    return valid, expl

def stmt_5(df: pd.DataFrame):
    """5. The 4-star hotel in Denver has both a higher average nightly rate ($164.7) and a higher occupancy rate (75.8%) than the 3-star Denver hotel ($119.5, 72.2%)."""
    denver_hotels = df[df["city"].str.lower() == "denver"]
    if len(denver_hotels) < 2:
        expl = "Not enough Denver hotels to compare."
        return False, expl
    four_star = denver_hotels[denver_hotels["star_level"] == 4]
    three_star = denver_hotels[denver_hotels["star_level"] == 3]
    if four_star.empty or three_star.empty:
        expl = "Missing 3-star or 4-star hotel in Denver."
        return False, expl
    four_star = four_star.iloc[0]
    three_star = three_star.iloc[0]
    rate_check = four_star["avg_nightly_rate"] > three_star["avg_nightly_rate"]
    occupancy_check = four_star["occupancy_rate"] > three_star["occupancy_rate"]
    if rate_check and occupancy_check:
        expl = f"4-star Denver hotel ({four_star['avg_nightly_rate']}, {four_star['occupancy_rate']}%) > 3-star ({three_star['avg_nightly_rate']}, {three_star['occupancy_rate']}%)."
        return True, expl
    else:
        expl = f"4-star Denver hotel ({four_star['avg_nightly_rate']}, {four_star['occupancy_rate']}%) not better than 3-star ({three_star['avg_nightly_rate']}, {three_star['occupancy_rate']}%)."
        return False, expl

def stmt_6(df: pd.DataFrame):
    """6. Among 3-star hotels, the highest occupancy rate is 78.8% (Portland) and the lowest is 68.0% (Seattle)."""
    three_star = df[df["star_level"] == 3]
    if three_star.empty:
        expl = "No 3-star hotels found."
        return False, expl
    max_occ = three_star["occupancy_rate"].max()
    min_occ = three_star["occupancy_rate"].min()
    max_city = three_star[three_star["occupancy_rate"] == max_occ]["city"].iloc[0]
    min_city = three_star[three_star["occupancy_rate"] == min_occ]["city"].iloc[0]
    if max_occ == 78.8 and min_occ == 68.0 and max_city.lower() == "portland" and min_city.lower() == "seattle":
        expl = f"Highest 3-star occupancy is 78.8% in Portland, lowest is 68.0% in Seattle."
        return True, expl
    else:
        expl = f"Highest 3-star occupancy is {max_occ}% in {max_city}, lowest is {min_occ}% in {min_city}."
        return False, expl

def stmt_7(df: pd.DataFrame):
    """7. The range of occupancy rates for 4-star hotels spans from 65.0% (Austin) to 86.6% (Dallas)."""
    four_star = df[df["star_level"] == 4]
    if four_star.empty:
        expl = "No 4-star hotels found."
        return False, expl
    min_occ = four_star["occupancy_rate"].min()
    max_occ = four_star["occupancy_rate"].max()
    min_city = four_star[four_star["occupancy_rate"] == min_occ]["city"].iloc[0]
    max_city = four_star[four_star["occupancy_rate"] == max_occ]["city"].iloc[0]
    if min_occ == 65.0 and max_occ == 86.6 and min_city.lower() == "austin" and max_city.lower() == "dallas":
        expl = f"4-star occupancy range is 65.0% in Austin to 86.6% in Dallas."
        return True, expl
    else:
        expl = f"4-star occupancy range is {min_occ}% in {min_city} to {max_occ}% in {max_city}."
        return False, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_65.csv")

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