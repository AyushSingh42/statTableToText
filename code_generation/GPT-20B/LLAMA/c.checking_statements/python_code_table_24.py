import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with monthly income greater than 9k have a household size greater than 1."""
    subset = df[df["monthly_income_k"] > 9]
    condition = subset["household_size"] > 1
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income >9k have size >1."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a suburban region, then their utility cost is less than 200."""
    subset = df[df["region"] == "suburban"]
    condition = subset["utility_cost"] < 200
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} suburban households have utility cost <200."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} suburban households violate the rule (costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in an urban region with a vehicle count of 0."""
    exists = ((df["region"] == "urban") & (df["vehicle_count"] == 0)).any()
    if exists:
        count = df[(df["region"] == "urban") & (df["vehicle_count"] == 0)].shape[0]
        expl = f"Found {count} urban household(s) with vehicle count 0."
    else:
        expl = "No urban household with vehicle count 0 found."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. For all households with a household size greater than 5, their monthly income is greater than 7k."""
    subset = df[df["household_size"] > 5]
    condition = subset["monthly_income_k"] > 7
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size >5 have income >7k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a fiber internet type, then their monthly income is greater than 3k."""
    subset = df[df["internet_type"] == "fiber"]
    condition = subset["monthly_income_k"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} fiber households have income >3k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} fiber households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with a monthly income less than 4k have a household size greater than 4."""
    subset = df[df["monthly_income_k"] < 4]
    condition = subset["household_size"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income <4k have size >4."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most households in the data have a vehicle count greater than 0."""
    total = len(df)
    count_gt0 = (df["vehicle_count"] > 0).sum()
    proportion = count_gt0 / total
    truth = proportion > 0.5
    expl = f"{proportion*100:.1f}% of households have vehicle count >0 ({count_gt0}/{total})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household is in a rural region, then their monthly income is less than 9k."""
    subset = df[df["region"] == "rural"]
    condition = subset["monthly_income_k"] < 9
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} rural households have income <9k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} rural households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. For all households with a utility cost greater than 150, their household size is greater than 2."""
    subset = df[df["utility_cost"] > 150]
    condition = subset["household_size"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with utility cost >150 have size >2."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one household in a suburban region with a monthly income greater than 10k."""
    exists = ((df["region"] == "suburban") & (df["monthly_income_k"] > 10)).any()
    if exists:
        count = df[(df["region"] == "suburban") & (df["monthly_income_k"] > 10)].shape[0]
        expl = f"Found {count} suburban household(s) with income >10k."
    else:
        expl = "No suburban household with income >10k found."
    return exists, expl

def stmt_11(df: pd.DataFrame):
    """11. All households with a household size of 1 have a monthly income greater than 6k."""
    subset = df[df["household_size"] == 1]
    condition = subset["monthly_income_k"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size 1 have income >6k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a household has a satellite internet type, then their household size is less than 6."""
    subset = df[df["internet_type"] == "satellite"]
    condition = subset["household_size"] < 6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} satellite households have size <6."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} satellite households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. For all households with a monthly income greater than 8k, their rent is greater than 1k."""
    subset = df[df["monthly_income_k"] > 8]
    condition = subset["rent_k"] > 1
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income >8k have rent >1k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Most households in the data have a monthly income greater than 5k."""
    total = len(df)
    count_gt5 = (df["monthly_income_k"] > 5).sum()
    proportion = count_gt5 / total
    truth = proportion > 0.5
    expl = f"{proportion*100:.1f}% of households have income >5k ({count_gt5}/{total})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a household is in an urban region, then their utility cost is greater than 80."""
    subset = df[df["region"] == "urban"]
    condition = subset["utility_cost"] > 80
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} urban households have utility cost >80."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} urban households violate the rule (costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one household with a vehicle count of 3."""
    exists = (df["vehicle_count"] == 3).any()
    if exists:
        count = df[df["vehicle_count"] == 3].shape[0]
        expl = f"Found {count} household(s) with vehicle count 3."
    else:
        expl = "No household with vehicle count 3 found."
    return exists, expl

def stmt_17(df: pd.DataFrame):
    """17. All households with a household size greater than 3 have a monthly income greater than 4k."""
    subset = df[df["household_size"] > 3]
    condition = subset["monthly_income_k"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size >3 have income >4k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_24.csv")

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