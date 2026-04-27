import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than 10k have a household size greater than or equal to 2."""
    condition = (df["monthly_income_k"] > 10) & (df["household_size"] < 2)
    truth = not condition.any()
    if truth:
        expl = "No households with income >10k have household size <2."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income: {', '.join(map(str, viol['monthly_income_k'].tolist()))}, size: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their monthly income is less than or equal to 11.5k."""
    condition = (df["region"] == "rural") & (df["monthly_income_k"] > 11.5)
    truth = not condition.any()
    if truth:
        expl = "All rural households have income <=11.5k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} rural households violate the rule (income: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in a suburban region with a monthly income less than 6k."""
    condition = (df["region"] == "suburban") & (df["monthly_income_k"] < 6)
    truth = condition.any()
    if truth:
        expl = "At least one suburban household has income <6k."
    else:
        expl = "No suburban households have income <6k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a household size greater than or equal to 6 have a monthly income greater than or equal to 8.6k."""
    condition = (df["household_size"] >= 6) & (df["monthly_income_k"] < 8.6)
    truth = not condition.any()
    if truth:
        expl = "All households with size >=6 have income >=8.6k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size: {', '.join(map(str, viol['household_size'].tolist()))}, income: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count greater than or equal to 3, then their monthly income is greater than or equal to 9.3k."""
    condition = (df["vehicle_count"] >= 3) & (df["monthly_income_k"] < 9.3)
    truth = not condition.any()
    if truth:
        expl = "All households with 3+ vehicles have income >=9.3k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (vehicles: {', '.join(map(str, viol['vehicle_count'].tolist()))}, income: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most households in the data have a utility cost greater than 100."""
    condition = df["utility_cost"] > 100
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of households have utility cost >100."
    else:
        expl = f"Less than half ({count}/{total}) of households have utility cost >100."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with a monthly income less than 6k have a household size less than or equal to 3."""
    condition = (df["monthly_income_k"] < 6) & (df["household_size"] > 3)
    truth = not condition.any()
    if truth:
        expl = "All households with income <6k have size <=3."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income: {', '.join(map(str, viol['monthly_income_k'].tolist()))}, size: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household is in an urban region, then their household size is less than or equal to 3."""
    condition = (df["region"] == "urban") & (df["household_size"] > 3)
    truth = not condition.any()
    if truth:
        expl = "All urban households have size <=3."
    else:
        viol = df[condition]
        expl = f"{len(viol)} urban households violate the rule (size: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in a rural region with a monthly income less than 5k."""
    condition = (df["region"] == "rural") & (df["monthly_income_k"] < 5)
    truth = condition.any()
    if truth:
        expl = "At least one rural household has income <5k."
    else:
        expl = "No rural households have income <5k."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All households with a rent greater than 2k have a monthly income greater than or equal to 8.8k."""
    condition = (df["rent_k"] > 2) & (df["monthly_income_k"] < 8.8)
    truth = not condition.any()
    if truth:
        expl = "All households with rent >2k have income >=8.8k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (rent: {', '.join(map(str, viol['rent_k'].tolist()))}, income: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household has a household size greater than or equal to 5, then their vehicle count is greater than or equal to 2."""
    condition = (df["household_size"] >= 5) & (df["vehicle_count"] < 2)
    truth = not condition.any()
    if truth:
        expl = "All households with size >=5 have vehicle count >=2."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size: {', '.join(map(str, viol['household_size'].tolist()))}, vehicles: {', '.join(map(str, viol['vehicle_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most households in the data have a household size greater than or equal to 2."""
    condition = df["household_size"] >= 2
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of households have size >=2."
    else:
        expl = f"Less than half ({count}/{total}) of households have size >=2."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All households with a utility cost greater than 150 have a household size greater than or equal to 4."""
    condition = (df["utility_cost"] > 150) & (df["household_size"] < 4)
    truth = not condition.any()
    if truth:
        expl = "All households with utility cost >150 have size >=4."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (utility cost: {', '.join(map(str, viol['utility_cost'].tolist()))}, size: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household has a monthly income greater than 10k, then their internet type is not satellite."""
    condition = (df["monthly_income_k"] > 10) & (df["internet_type"] == "satellite")
    truth = not condition.any()
    if truth:
        expl = "All households with income >10k do not use satellite internet."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income: {', '.join(map(str, viol['monthly_income_k'].tolist()))}, internet: {', '.join(map(str, viol['internet_type'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household in a suburban region with a monthly income greater than 9k and a household size greater than or equal to 5."""
    condition = (df["region"] == "suburban") & (df["monthly_income_k"] > 9) & (df["household_size"] >= 5)
    truth = condition.any()
    if truth:
        expl = "At least one suburban household has income >9k and size >=5."
    else:
        expl = "No suburban households satisfy both conditions."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_54.csv")

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
        (8, stmt_8),
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()