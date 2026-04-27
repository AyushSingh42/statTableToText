import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with monthly income greater than 10k have a household size greater than or equal to 3."""
    high_income = df[df["monthly_income_k"] > 10]
    condition = high_income["household_size"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(high_income)} households with income >10k have size >=3."
    else:
        viol = high_income[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their monthly income is less than or equal to 11.1k."""
    rural = df[df["region"] == "rural"]
    condition = rural["monthly_income_k"] <= 11.1
    truth = condition.all()
    if truth:
        expl = f"All {len(rural)} rural households have income <=11.1k."
    else:
        viol = rural[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} rural households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in the urban region with a monthly income less than 5k."""
    urban = df[df["region"] == "urban"]
    exists = (urban["monthly_income_k"] < 5).any()
    if exists:
        ids = urban[urban["monthly_income_k"] < 5]["household_id"].tolist()
        expl = f"Found {len(ids)} urban households with income <5k (ids: {', '.join(ids)})."
    else:
        expl = "No urban household has income <5k."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. For all households with a household size greater than or equal to 5, their rent is less than or equal to 2.8k."""
    large_size = df[df["household_size"] >= 5]
    condition = large_size["rent_k"] <= 2.8
    truth = condition.all()
    if truth:
        expl = f"All {len(large_size)} households with size >=5 have rent <=2.8k."
    else:
        viol = large_size[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count greater than 0, then their internet type is not satellite."""
    with_vehicle = df[df["vehicle_count"] > 0]
    condition = with_vehicle["internet_type"]!= "satellite"
    truth = condition.all()
    if truth:
        expl = f"All {len(with_vehicle)} households with vehicle count >0 have non-satellite internet."
    else:
        viol = with_vehicle[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with a utility cost greater than 190 have an internet type of either cable or fiber."""
    high_util = df[df["utility_cost"] > 190]
    condition = high_util["internet_type"].isin(["cable", "fiber"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_util)} households with utility cost >190 have cable or fiber internet."
    else:
        viol = high_util[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all households with a monthly income less than 6k, their household size is greater than or equal to 4."""
    low_income = df[df["monthly_income_k"] < 6]
    condition = low_income["household_size"] >= 4
    truth = condition.all()
    if truth:
        expl = f"All {len(low_income)} households with income <6k have size >=4."
    else:
        viol = low_income[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one household in the suburban region with a monthly income greater than 10k."""
    suburban = df[df["region"] == "suburban"]
    exists = (suburban["monthly_income_k"] > 10).any()
    if exists:
        ids = suburban[suburban["monthly_income_k"] > 10]["household_id"].tolist()
        expl = f"Found {len(ids)} suburban households with income >10k (ids: {', '.join(ids)})."
    else:
        expl = "No suburban household has income >10k."
    return exists, expl

def stmt_9(df: pd.DataFrame):
    """9. If a household has a household size of 1, then their monthly income is less than 7k."""
    size_one = df[df["household_size"] == 1]
    condition = size_one["monthly_income_k"] < 7
    truth = condition.all()
    if truth:
        expl = f"All {len(size_one)} households with size 1 have income <7k."
    else:
        viol = size_one[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Most households have a vehicle count greater than or equal to 2."""
    count_ge2 = (df["vehicle_count"] >= 2).sum()
    truth = count_ge2 > len(df) / 2
    if truth:
        expl = f"{count_ge2} out of {len(df)} households have vehicle count >=2."
    else:
        expl = f"Only {count_ge2} out of {len(df)} households have vehicle count >=2."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. For all households with a rent less than 2k, their household size is greater than or equal to 4."""
    low_rent = df[df["rent_k"] < 2]
    condition = low_rent["household_size"] >= 4
    truth = condition.all()
    if truth:
        expl = f"All {len(low_rent)} households with rent <2k have size >=4."
    else:
        viol = low_rent[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a household is in an urban region, then their utility cost is greater than 120."""
    urban = df[df["region"] == "urban"]
    condition = urban["utility_cost"] > 120
    truth = condition.all()
    if truth:
        expl = f"All {len(urban)} urban households have utility cost >120."
    else:
        viol = urban[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} urban households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All households with a monthly income greater than 10.8k have a household size greater than or equal to 3."""
    high_income = df[df["monthly_income_k"] > 10.8]
    condition = high_income["household_size"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(high_income)} households with income >10.8k have size >=3."
    else:
        viol = high_income[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one household in the rural region with a utility cost less than 100."""
    rural = df[df["region"] == "rural"]
    exists = (rural["utility_cost"] < 100).any()
    if exists:
        ids = rural[rural["utility_cost"] < 100]["household_id"].tolist()
        expl = f"Found {len(ids)} rural households with utility cost <100 (ids: {', '.join(ids)})."
    else:
        expl = "No rural household has utility cost <100."
    return exists, expl

def stmt_15(df: pd.DataFrame):
    """15. For all households with an internet type of fiber, their household size is greater than or equal to 3."""
    fiber = df[df["internet_type"] == "fiber"]
    condition = fiber["household_size"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(fiber)} fiber households have size >=3."
    else:
        viol = fiber[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} fiber households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a household has a household size of 6, then their monthly income is less than 11k."""
    size_six = df[df["household_size"] == 6]
    condition = size_six["monthly_income_k"] < 11
    truth = condition.all()
    if truth:
        expl = f"All {len(size_six)} households with size 6 have income <11k."
    else:
        viol = size_six[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. Most households have a utility cost greater than 100."""
    count_gt100 = (df["utility_cost"] > 100).sum()
    truth = count_gt100 > len(df) / 2
    if truth:
        expl = f"{count_gt100} out of {len(df)} households have utility cost >100."
    else:
        expl = f"Only {count_gt100} out of {len(df)} households have utility cost >100."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. For all households with a vehicle count of 0, their internet type is satellite."""
    zero_vehicle = df[df["vehicle_count"] == 0]
    condition = zero_vehicle["internet_type"] == "satellite"
    truth = condition.all()
    if truth:
        expl = f"All {len(zero_vehicle)} households with vehicle count 0 have satellite internet."
    else:
        viol = zero_vehicle[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. If a household is in a suburban region, then their monthly income is less than 11k."""
    suburban = df[df["region"] == "suburban"]
    condition = suburban["monthly_income_k"] < 11
    truth = condition.all()
    if truth:
        expl = f"All {len(suburban)} suburban households have income <11k."
    else:
        viol = suburban[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} suburban households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. All households with a rent greater than 2.5k have a household size greater than or equal to 3."""
    high_rent = df[df["rent_k"] > 2.5]
    condition = high_rent["household_size"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rent)} households with rent >2.5k have size >=3."
    else:
        viol = high_rent[~condition]
        ids = viol["household_id"].tolist()
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(ids)})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_14.csv")

    # Convert numeric columns where possible
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
        (19, stmt_19),
        (20, stmt_20),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()