import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than 10k have a household size greater than or equal to 2."""
    high_income = df[df["monthly_income_k"] > 10]
    condition = high_income["household_size"] >= 2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_income)} households with income >10k have size >=2."
    else:
        viol = high_income[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their monthly income is less than or equal to 11.5k."""
    rural = df[df["region"] == "rural"]
    condition = rural["monthly_income_k"] <= 11.5
    truth = condition.all()
    if truth:
        expl = f"All {len(rural)} rural households have income <=11.5k."
    else:
        viol = rural[~condition]
        expl = f"{len(viol)} rural households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in a suburban region with a monthly income less than 6k."""
    suburban = df[df["region"] == "suburban"]
    exists = (suburban["monthly_income_k"] < 6).any()
    if exists:
        viol = suburban[suburban["monthly_income_k"] < 6]
        expl = f"Found {len(viol)} suburban households with income <6k."
    else:
        expl = "No suburban household has income <6k."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a household size greater than or equal to 6 have a monthly income greater than or equal to 8.6k."""
    large_size = df[df["household_size"] >= 6]
    condition = large_size["monthly_income_k"] >= 8.6
    truth = condition.all()
    if truth:
        expl = f"All {len(large_size)} households with size >=6 have income >=8.6k."
    else:
        viol = large_size[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count greater than or equal to 3, then their monthly income is greater than or equal to 9.3k."""
    many_vehicles = df[df["vehicle_count"] >= 3]
    condition = many_vehicles["monthly_income_k"] >= 9.3
    truth = condition.all()
    if truth:
        expl = f"All {len(many_vehicles)} households with vehicle_count >=3 have income >=9.3k."
    else:
        viol = many_vehicles[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most households in the data have a utility cost greater than 100."""
    total = len(df)
    count = (df["utility_cost"] > 100).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count}/{total} households have utility cost >100."
    else:
        expl = f"Only {count}/{total} households have utility cost >100."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with a monthly income less than 6k have a household size less than or equal to 3."""
    low_income = df[df["monthly_income_k"] < 6]
    condition = low_income["household_size"] <= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(low_income)} households with income <6k have size <=3."
    else:
        viol = low_income[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household is in an urban region, then their household size is less than or equal to 3."""
    urban = df[df["region"] == "urban"]
    condition = urban["household_size"] <= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(urban)} urban households have size <=3."
    else:
        viol = urban[~condition]
        expl = f"{len(viol)} urban households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in a rural region with a monthly income less than 5k."""
    rural = df[df["region"] == "rural"]
    exists = (rural["monthly_income_k"] < 5).any()
    if exists:
        viol = rural[rural["monthly_income_k"] < 5]
        expl = f"Found {len(viol)} rural households with income <5k."
    else:
        expl = "No rural household has income <5k."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All households with a rent greater than 2k have a monthly income greater than or equal to 8.8k."""
    high_rent = df[df["rent_k"] > 2]
    condition = high_rent["monthly_income_k"] >= 8.8
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rent)} households with rent >2k have income >=8.8k."
    else:
        viol = high_rent[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household has a household size greater than or equal to 5, then their vehicle count is greater than or equal to 2."""
    large_size = df[df["household_size"] >= 5]
    condition = large_size["vehicle_count"] >= 2
    truth = condition.all()
    if truth:
        expl = f"All {len(large_size)} households with size >=5 have vehicle_count >=2."
    else:
        viol = large_size[~condition]
        expl = f"{len(viol)} households violate the rule (vehicle_counts: {', '.join(map(str, viol['vehicle_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most households in the data have a household size greater than or equal to 2."""
    total = len(df)
    count = (df["household_size"] >= 2).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count}/{total} households have size >=2."
    else:
        expl = f"Only {count}/{total} households have size >=2."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All households with a utility cost greater than 150 have a household size greater than or equal to 4."""
    high_util = df[df["utility_cost"] > 150]
    condition = high_util["household_size"] >= 4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_util)} households with utility_cost >150 have size >=4."
    else:
        viol = high_util[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household has a monthly income greater than 10k, then their internet type is not satellite."""
    high_income = df[df["monthly_income_k"] > 10]
    condition = high_income["internet_type"]!= "satellite"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_income)} households with income >10k have internet_type!= satellite."
    else:
        viol = high_income[~condition]
        expl = f"{len(viol)} households violate the rule (internet_types: {', '.join(map(str, viol['internet_type'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household in a suburban region with a monthly income greater than 9k and a household size greater than or equal to 5."""
    suburban = df[df["region"] == "suburban"]
    exists = ((suburban["monthly_income_k"] > 9) & (suburban["household_size"] >= 5)).any()
    if exists:
        viol = suburban[(suburban["monthly_income_k"] > 9) & (suburban["household_size"] >= 5)]
        expl = f"Found {len(viol)} suburban households with income >9k and size >=5."
    else:
        expl = "No suburban household satisfies income >9k and size >=5."
    return exists, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_54.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()