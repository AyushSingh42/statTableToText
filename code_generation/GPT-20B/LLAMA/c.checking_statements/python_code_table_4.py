import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than 10k have a household size greater than 1."""
    subset = df[df["monthly_income_k"] > 10]
    condition = subset["household_size"] > 1
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income >10k have size >1."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their utility cost is greater than 100."""
    subset = df[df["region"] == "rural"]
    condition = subset["utility_cost"] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} rural households have utility cost >100."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} rural households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All households with a vehicle count of 2 have a monthly income greater than 5k."""
    subset = df[df["vehicle_count"] == 2]
    condition = subset["monthly_income_k"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with 2 vehicles have income >5k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one household in a suburban region with a monthly income greater than 11k."""
    exists = ((df["region"] == "suburban") & (df["monthly_income_k"] > 11)).any()
    truth = exists
    if truth:
        expl = "At least one suburban household has income >11k."
    else:
        expl = "No suburban household has income >11k."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a household size of 6, then their monthly income is less than 12k."""
    subset = df[df["household_size"] == 6]
    condition = subset["monthly_income_k"] < 12
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size 6 have income <12k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with a monthly income less than 4k have a household size less than 6."""
    subset = df[df["monthly_income_k"] < 4]
    condition = subset["household_size"] < 6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income <4k have size <6."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most households in the data have a household size of 3 or more."""
    count = (df["household_size"] >= 3).sum()
    truth = count >= 0.5 * len(df)
    if truth:
        expl = f"{count} out of {len(df)} households have size >=3."
    else:
        expl = f"Only {count} out of {len(df)} households have size >=3."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household has a vehicle count of 0, then their monthly income is greater than 5k."""
    subset = df[df["vehicle_count"] == 0]
    condition = subset["monthly_income_k"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with 0 vehicles have income >5k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All households with a monthly income greater than 9k have a rent cost less than 3k."""
    subset = df[df["monthly_income_k"] > 9]
    condition = subset["rent_k"] < 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income >9k have rent <3k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one household in an urban region with a monthly income greater than 10k."""
    exists = ((df["region"] == "urban") & (df["monthly_income_k"] > 10)).any()
    truth = exists
    if truth:
        expl = "At least one urban household has income >10k."
    else:
        expl = "No urban household has income >10k."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household has a household size of 1, then their monthly income is greater than 10k."""
    subset = df[df["household_size"] == 1]
    condition = subset["monthly_income_k"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size 1 have income >10k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All households with a utility cost greater than 200 have a household size greater than 2."""
    subset = df[df["utility_cost"] > 200]
    condition = subset["household_size"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with utility >200 have size >2."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most households in the data have a utility cost greater than 100."""
    count = (df["utility_cost"] > 100).sum()
    truth = count >= 0.5 * len(df)
    if truth:
        expl = f"{count} out of {len(df)} households have utility >100."
    else:
        expl = f"Only {count} out of {len(df)} households have utility >100."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household is in a rural region, then their internet type is not fiber."""
    subset = df[df["region"] == "rural"]
    condition = subset["internet_type"]!= "fiber"
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} rural households have internet type not fiber."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} rural households violate the rule (internet types: {', '.join(map(str, viol['internet_type'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All households with a monthly income less than 6k have a household size greater than 2."""
    subset = df[df["monthly_income_k"] < 6]
    condition = subset["household_size"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income <6k have size >2."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one household in a suburban region with a vehicle count of 2."""
    exists = ((df["region"] == "suburban") & (df["vehicle_count"] == 2)).any()
    truth = exists
    if truth:
        expl = "At least one suburban household has vehicle count 2."
    else:
        expl = "No suburban household has vehicle count 2."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a household has a household size of 5, then their monthly income is greater than 3k."""
    subset = df[df["household_size"] == 5]
    condition = subset["monthly_income_k"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size 5 have income >3k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_4.csv")

    # Convert numeric columns
    numeric_cols = ["monthly_income_k", "rent_k", "utility_cost", "vehicle_count", "household_size"]
    for col in numeric_cols:
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()