import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than 9k have a household size greater than 1."""
    condition = (df["monthly_income_k"] > 9) & (df["household_size"] <= 1)
    truth = not condition.any()
    if truth:
        expl = "No household with income >9k has household size <=1."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income: {', '.join(map(str, viol['monthly_income_k'].tolist()))}, size: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their utility cost is greater than 114.9."""
    condition = (df["region"] == "rural") & (df["utility_cost"] <= 114.9)
    truth = not condition.any()
    if truth:
        expl = "All rural households have utility cost >114.9."
    else:
        viol = df[condition]
        expl = f"{len(viol)} rural households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in the urban region with a monthly income less than 4k."""
    condition = (df["region"] == "urban") & (df["monthly_income_k"] < 4)
    truth = condition.any()
    if truth:
        expl = "At least one urban household has income <4k."
    else:
        expl = "No urban household has income <4k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a household size greater than 5 have a monthly income greater than 6k."""
    condition = (df["household_size"] > 5) & (df["monthly_income_k"] <= 6)
    truth = not condition.any()
    if truth:
        expl = "All households with size >5 have income >6k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size: {', '.join(map(str, viol['household_size'].tolist()))}, income: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count greater than 2, then their monthly income is greater than 5k."""
    condition = (df["vehicle_count"] > 2) & (df["monthly_income_k"] <= 5)
    truth = not condition.any()
    if truth:
        expl = "All households with >2 vehicles have income >5k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (vehicles: {', '.join(map(str, viol['vehicle_count'].tolist()))}, income: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most households have a household size greater than 2."""
    total = len(df)
    condition = df["household_size"] > 2
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of households have size >2."
    else:
        expl = f"Less than half ({count}/{total}) of households have size >2."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with a monthly income less than 8k have a rent less than or equal to 2.2k."""
    condition = (df["monthly_income_k"] < 8) & (df["rent_k"] > 2.2)
    truth = not condition.any()
    if truth:
        expl = "All households with income <8k have rent <=2.2k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income: {', '.join(map(str, viol['monthly_income_k'].tolist()))}, rent: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household is in a suburban region, then their internet type is either fiber or satellite."""
    condition = (df["region"] == "suburban") & (~df["internet_type"].isin(["fiber", "satellite"]))
    truth = not condition.any()
    if truth:
        expl = "All suburban households have internet type fiber or satellite."
    else:
        viol = df[condition]
        expl = f"{len(viol)} suburban households violate the rule (internet types: {', '.join(map(str, viol['internet_type'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in the rural region with a monthly income greater than 10k."""
    condition = (df["region"] == "rural") & (df["monthly_income_k"] > 10)
    truth = condition.any()
    if truth:
        expl = "At least one rural household has income >10k."
    else:
        expl = "No rural household has income >10k."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All households with a utility cost greater than 178 have a household size greater than 3."""
    condition = (df["utility_cost"] > 178) & (df["household_size"] <= 3)
    truth = not condition.any()
    if truth:
        expl = "All households with utility cost >178 have size >3."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (utility cost: {', '.join(map(str, viol['utility_cost'].tolist()))}, size: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household has a monthly income greater than 9k, then their household size is greater than 2."""
    condition = (df["monthly_income_k"] > 9) & (df["household_size"] <= 2)
    truth = not condition.any()
    if truth:
        expl = "All households with income >9k have size >2."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income: {', '.join(map(str, viol['monthly_income_k'].tolist()))}, size: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most households have a utility cost greater than 114.9."""
    total = len(df)
    condition = df["utility_cost"] > 114.9
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of households have utility cost >114.9."
    else:
        expl = f"Less than half ({count}/{total}) of households have utility cost >114.9."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All households with a vehicle count greater than 1 have a monthly income greater than 5k."""
    condition = (df["vehicle_count"] > 1) & (df["monthly_income_k"] <= 5)
    truth = not condition.any()
    if truth:
        expl = "All households with >1 vehicle have income >5k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (vehicles: {', '.join(map(str, viol['vehicle_count'].tolist()))}, income: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household is in an urban region, then their rent is less than or equal to 2.2k."""
    condition = (df["region"] == "urban") & (df["rent_k"] > 2.2)
    truth = not condition.any()
    if truth:
        expl = "All urban households have rent <=2.2k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} urban households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household in the suburban region with a monthly income less than 6k."""
    condition = (df["region"] == "suburban") & (df["monthly_income_k"] < 6)
    truth = condition.any()
    if truth:
        expl = "At least one suburban household has income <6k."
    else:
        expl = "No suburban household has income <6k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All households with a household size greater than 4 have a monthly income greater than 5k."""
    condition = (df["household_size"] > 4) & (df["monthly_income_k"] <= 5)
    truth = not condition.any()
    if truth:
        expl = "All households with size >4 have income >5k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size: {', '.join(map(str, viol['household_size'].tolist()))}, income: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a household has a monthly income less than 8k, then their utility cost is greater than 90."""
    condition = (df["monthly_income_k"] < 8) & (df["utility_cost"] <= 90)
    truth = not condition.any()
    if truth:
        expl = "All households with income <8k have utility cost >90."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income: {', '.join(map(str, viol['monthly_income_k'].tolist()))}, utility cost: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_94.csv")

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
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()