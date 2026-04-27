import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than 9k have a household size greater than 1."""
    subset = df[df["monthly_income_k"] > 9]
    condition = subset["household_size"] > 1
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income > 9k have size > 1."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their utility cost is greater than 114.9."""
    subset = df[df["region"] == "rural"]
    condition = subset["utility_cost"] > 114.9
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} rural households have utility cost > 114.9."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} rural households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in the urban region with a monthly income less than 4k."""
    exists = ((df["region"] == "urban") & (df["monthly_income_k"] < 4)).any()
    truth = exists
    if truth:
        count = df[(df["region"] == "urban") & (df["monthly_income_k"] < 4)].shape[0]
        expl = f"Found {count} urban household(s) with income < 4k."
    else:
        expl = "No urban household with income < 4k found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a household size greater than 5 have a monthly income greater than 6k."""
    subset = df[df["household_size"] > 5]
    condition = subset["monthly_income_k"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size > 5 have income > 6k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count greater than 2, then their monthly income is greater than 5k."""
    subset = df[df["vehicle_count"] > 2]
    condition = subset["monthly_income_k"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with vehicle count > 2 have income > 5k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most households have a household size greater than 2."""
    condition = df["household_size"] > 2
    proportion = condition.mean()
    truth = proportion > 0.5
    expl = f"{proportion*100:.1f}% of households have size > 2."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with a monthly income less than 8k have a rent less than or equal to 2.2k."""
    subset = df[df["monthly_income_k"] < 8]
    condition = subset["rent_k"] <= 2.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income < 8k have rent <= 2.2k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household is in a suburban region, then their internet type is either fiber or satellite."""
    subset = df[df["region"] == "suburban"]
    condition = subset["internet_type"].isin(["fiber", "satellite"])
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} suburban households use fiber or satellite."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} suburban households violate the rule (internet types: {', '.join(map(str, viol['internet_type'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in the rural region with a monthly income greater than 10k."""
    exists = ((df["region"] == "rural") & (df["monthly_income_k"] > 10)).any()
    truth = exists
    if truth:
        count = df[(df["region"] == "rural") & (df["monthly_income_k"] > 10)].shape[0]
        expl = f"Found {count} rural household(s) with income > 10k."
    else:
        expl = "No rural household with income > 10k found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All households with a utility cost greater than 178 have a household size greater than 3."""
    subset = df[df["utility_cost"] > 178]
    condition = subset["household_size"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with utility cost > 178 have size > 3."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household has a monthly income greater than 9k, then their household size is greater than 2."""
    subset = df[df["monthly_income_k"] > 9]
    condition = subset["household_size"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income > 9k have size > 2."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most households have a utility cost greater than 114.9."""
    condition = df["utility_cost"] > 114.9
    proportion = condition.mean()
    truth = proportion > 0.5
    expl = f"{proportion*100:.1f}% of households have utility cost > 114.9."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All households with a vehicle count greater than 1 have a monthly income greater than 5k."""
    subset = df[df["vehicle_count"] > 1]
    condition = subset["monthly_income_k"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with vehicle count > 1 have income > 5k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household is in an urban region, then their rent is less than or equal to 2.2k."""
    subset = df[df["region"] == "urban"]
    condition = subset["rent_k"] <= 2.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} urban households have rent <= 2.2k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} urban households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household in the suburban region with a monthly income less than 6k."""
    exists = ((df["region"] == "suburban") & (df["monthly_income_k"] < 6)).any()
    truth = exists
    if truth:
        count = df[(df["region"] == "suburban") & (df["monthly_income_k"] < 6)].shape[0]
        expl = f"Found {count} suburban household(s) with income < 6k."
    else:
        expl = "No suburban household with income < 6k found."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All households with a household size greater than 4 have a monthly income greater than 5k."""
    subset = df[df["household_size"] > 4]
    condition = subset["monthly_income_k"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size > 4 have income > 5k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a household has a monthly income less than 8k, then their utility cost is greater than 90."""
    subset = df[df["monthly_income_k"] < 8]
    condition = subset["utility_cost"] > 90
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income < 8k have utility cost > 90."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_94.csv")

    # Convert numeric columns
    numeric_cols = ["household_size", "monthly_income_k", "rent_k", "utility_cost", "vehicle_count"]
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