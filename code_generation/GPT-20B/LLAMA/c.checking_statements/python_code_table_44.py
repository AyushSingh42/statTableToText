import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with monthly income greater than 8k have a household size greater than 3."""
    subset = df[df["monthly_income_k"] > 8]
    condition = subset["household_size"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income > 8k have size > 3."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their utility cost is greater than 140."""
    subset = df[df["region"] == "rural"]
    condition = subset["utility_cost"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} rural households have utility cost > 140."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} rural households violate the rule (costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in the suburban region with a monthly income greater than 10k."""
    exists = ((df["region"] == "suburban") & (df["monthly_income_k"] > 10)).any()
    truth = exists
    if truth:
        expl = "At least one suburban household has income > 10k."
    else:
        expl = "No suburban household has income > 10k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a vehicle count greater than 2 have a monthly income greater than 4k."""
    subset = df[df["vehicle_count"] > 2]
    condition = subset["monthly_income_k"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with vehicle count > 2 have income > 4k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a household size greater than 5, then their rent is greater than 1.5k."""
    subset = df[df["household_size"] > 5]
    condition = subset["rent_k"] > 1.5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size > 5 have rent > 1.5k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most households in the table have a household size less than or equal to 5."""
    total = len(df)
    count = (df["household_size"] <= 5).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of households have size <= 5."
    else:
        expl = f"Only {proportion*100:.1f}% of households have size <= 5."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with internet type 'fiber' have a monthly income greater than 3k."""
    subset = df[df["internet_type"] == "fiber"]
    condition = subset["monthly_income_k"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} fiber households have income > 3k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} fiber households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household is in an urban region, then their household size is greater than or equal to 3."""
    subset = df[df["region"] == "urban"]
    condition = subset["household_size"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} urban households have size >= 3."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} urban households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in the rural region with a vehicle count of 0."""
    exists = ((df["region"] == "rural") & (df["vehicle_count"] == 0)).any()
    truth = exists
    if truth:
        expl = "At least one rural household has vehicle count 0."
    else:
        expl = "No rural household has vehicle count 0."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All households with a monthly income less than or equal to 4k have a household size less than or equal to 5."""
    subset = df[df["monthly_income_k"] <= 4]
    condition = subset["household_size"] <= 5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income <= 4k have size <= 5."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household has a household size of 2, then their monthly income is greater than 5k."""
    subset = df[df["household_size"] == 2]
    condition = subset["monthly_income_k"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size 2 have income > 5k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All households with internet type'satellite' have a household size less than or equal to 6."""
    subset = df[df["internet_type"] == "satellite"]
    condition = subset["household_size"] <= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} satellite households have size <= 6."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} satellite households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most households in the table have a utility cost greater than 100."""
    total = len(df)
    count = (df["utility_cost"] > 100).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of households have utility cost > 100."
    else:
        expl = f"Only {proportion*100:.1f}% of households have utility cost > 100."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household is in a suburban region, then their rent is greater than 1k."""
    subset = df[df["region"] == "suburban"]
    condition = subset["rent_k"] > 1
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} suburban households have rent > 1k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} suburban households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household in the urban region with a monthly income less than 5k."""
    exists = ((df["region"] == "urban") & (df["monthly_income_k"] < 5)).any()
    truth = exists
    if truth:
        expl = "At least one urban household has income < 5k."
    else:
        expl = "No urban household has income < 5k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All households with a vehicle count of 1 have a monthly income greater than 3k."""
    subset = df[df["vehicle_count"] == 1]
    condition = subset["monthly_income_k"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with vehicle count 1 have income > 3k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_44.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()