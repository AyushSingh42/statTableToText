import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than $10k have a household size greater than 2."""
    subset = df[df["monthly_income_k"] > 10]
    condition = subset["household_size"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income >10k have size >2."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is located in an urban region, then their monthly income is greater than $2k."""
    urban = df[df["region"] == "urban"]
    condition = urban["monthly_income_k"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(urban)} urban households have income >2k."
    else:
        viol = urban[~condition]
        expl = f"{len(viol)} urban households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in a rural region with a monthly income greater than $9k."""
    exists = ((df["region"] == "rural") & (df["monthly_income_k"] > 9)).any()
    truth = exists
    if truth:
        count = df[(df["region"] == "rural") & (df["monthly_income_k"] > 9)].shape[0]
        expl = f"{count} rural household(s) have income >9k."
    else:
        expl = "No rural household has income >9k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a household size greater than 5 have a monthly income greater than $8k."""
    subset = df[df["household_size"] > 5]
    condition = subset["monthly_income_k"] > 8
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size >5 have income >8k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count greater than 1, then their monthly income is greater than $4k."""
    subset = df[df["vehicle_count"] > 1]
    condition = subset["monthly_income_k"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with vehicle count >1 have income >4k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most households have a utility cost greater than $150."""
    proportion = (df["utility_cost"] > 150).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of households have utility cost >150."
    else:
        expl = f"Only {proportion*100:.1f}% of households have utility cost >150."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with a monthly income less than $4k have a household size less than 4."""
    subset = df[df["monthly_income_k"] < 4]
    condition = subset["household_size"] < 4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income <4k have size <4."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household is located in a suburban region, then their internet type is not fiber."""
    subset = df[df["region"] == "suburban"]
    condition = subset["internet_type"]!= "fiber"
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} suburban households have internet type not fiber."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} suburban households violate the rule (internet types: {', '.join(map(str, viol['internet_type'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in an urban region with a rent less than $1.5k."""
    exists = ((df["region"] == "urban") & (df["rent_k"] < 1.5)).any()
    truth = exists
    if truth:
        count = df[(df["region"] == "urban") & (df["rent_k"] < 1.5)].shape[0]
        expl = f"{count} urban household(s) have rent <1.5k."
    else:
        expl = "No urban household has rent <1.5k."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All households with a household size less than 3 have a monthly income greater than $3k."""
    subset = df[df["household_size"] < 3]
    condition = subset["monthly_income_k"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size <3 have income >3k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household has a monthly income greater than $9k, then their household size is greater than 2."""
    subset = df[df["monthly_income_k"] > 9]
    condition = subset["household_size"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income >9k have size >2."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most households have a monthly income less than $12k."""
    proportion = (df["monthly_income_k"] < 12).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of households have income <12k."
    else:
        expl = f"Only {proportion*100:.1f}% of households have income <12k."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All households with a utility cost less than $200 have a household size less than 5."""
    subset = df[df["utility_cost"] < 200]
    condition = subset["household_size"] < 5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with utility cost <200 have size <5."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household is located in a rural region, then their vehicle count is less than 3."""
    subset = df[df["region"] == "rural"]
    condition = subset["vehicle_count"] < 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} rural households have vehicle count <3."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} rural households violate the rule (vehicle counts: {', '.join(map(str, viol['vehicle_count'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household in a suburban region with a monthly income greater than $9k."""
    exists = ((df["region"] == "suburban") & (df["monthly_income_k"] > 9)).any()
    truth = exists
    if truth:
        count = df[(df["region"] == "suburban") & (df["monthly_income_k"] > 9)].shape[0]
        expl = f"{count} suburban household(s) have income >9k."
    else:
        expl = "No suburban household has income >9k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All households with a rent greater than $2k have a household size greater than 3."""
    subset = df[df["rent_k"] > 2]
    condition = subset["household_size"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with rent >2k have size >3."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a household has a monthly income less than $3k, then their household size is less than 4."""
    subset = df[df["monthly_income_k"] < 3]
    condition = subset["household_size"] < 4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income <3k have size <4."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most households have a household size less than 6."""
    proportion = (df["household_size"] < 6).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of households have size <6."
    else:
        expl = f"Only {proportion*100:.1f}% of households have size <6."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_34.csv")

    # Convert numeric columns
    numeric_cols = ["household_size", "monthly_income_k", "rent_k", "utility_cost", "vehicle_count"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    # Ensure vehicle_count is integer if possible
    df["vehicle_count"] = df["vehicle_count"].astype('Int64')

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()