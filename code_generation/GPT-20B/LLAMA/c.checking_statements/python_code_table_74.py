import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than $9k have a household size greater than 1."""
    cond = df["monthly_income_k"] > 9
    subset = df[cond]
    truth = (subset["household_size"] > 1).all()
    if truth:
        expl = f"All {len(subset)} households with income >9k have size >1."
    else:
        viol = subset[subset["household_size"] <= 1]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their monthly income is less than or equal to $10.5k."""
    cond = df["region"] == "rural"
    subset = df[cond]
    truth = (subset["monthly_income_k"] <= 10.5).all()
    if truth:
        expl = f"All {len(subset)} rural households have income <=10.5k."
    else:
        viol = subset[subset["monthly_income_k"] > 10.5]
        expl = f"{len(viol)} rural households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in the urban region with a monthly income less than $6k."""
    cond = (df["region"] == "urban") & (df["monthly_income_k"] < 6)
    truth = not df[cond].empty
    if truth:
        sample = df[cond].iloc[0]
        expl = f"Found household {sample['household_id']} with income {sample['monthly_income_k']}k."
    else:
        expl = "No urban household with income <6k found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all households with a household size greater than 4, their monthly income is less than or equal to $10.5k."""
    cond = df["household_size"] > 4
    subset = df[cond]
    truth = (subset["monthly_income_k"] <= 10.5).all()
    if truth:
        expl = f"All {len(subset)} households with size >4 have income <=10.5k."
    else:
        viol = subset[subset["monthly_income_k"] > 10.5]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count greater than 1, then their monthly income is greater than or equal to $4.9k."""
    cond = df["vehicle_count"] > 1
    subset = df[cond]
    truth = (subset["monthly_income_k"] >= 4.9).all()
    if truth:
        expl = f"All {len(subset)} households with vehicle count >1 have income >=4.9k."
    else:
        viol = subset[subset["monthly_income_k"] < 4.9]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with a utility cost greater than $200 have a household size greater than 1."""
    cond = df["utility_cost"] > 200
    subset = df[cond]
    truth = (subset["household_size"] > 1).all()
    if truth:
        expl = f"All {len(subset)} households with utility cost >200 have size >1."
    else:
        viol = subset[subset["household_size"] <= 1]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a household has an internet type of fiber, then their monthly income is greater than or equal to $4.9k."""
    cond = df["internet_type"] == "fiber"
    subset = df[cond]
    truth = (subset["monthly_income_k"] >= 4.9).all()
    if truth:
        expl = f"All {len(subset)} fiber households have income >=4.9k."
    else:
        viol = subset[subset["monthly_income_k"] < 4.9]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one household in the suburban region with a monthly income greater than $9k."""
    cond = (df["region"] == "suburban") & (df["monthly_income_k"] > 9)
    truth = not df[cond].empty
    if truth:
        sample = df[cond].iloc[0]
        expl = f"Found household {sample['household_id']} with income {sample['monthly_income_k']}k."
    else:
        expl = "No suburban household with income >9k found."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. For all households with a rent greater than $2k, their household size is greater than 1."""
    cond = df["rent_k"] > 2
    subset = df[cond]
    truth = (subset["household_size"] > 1).all()
    if truth:
        expl = f"All {len(subset)} households with rent >2k have size >1."
    else:
        viol = subset[subset["household_size"] <= 1]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a household is in the urban region, then their utility cost is greater than or equal to $84.1."""
    cond = df["region"] == "urban"
    subset = df[cond]
    truth = (subset["utility_cost"] >= 84.1).all()
    if truth:
        expl = f"All {len(subset)} urban households have utility cost >=84.1."
    else:
        viol = subset[subset["utility_cost"] < 84.1]
        expl = f"{len(viol)} households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Most households have a household size greater than 1."""
    proportion = (df["household_size"] > 1).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of households have size >1."
    else:
        expl = f"Only {proportion*100:.1f}% of households have size >1."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All households with a monthly income less than $6k have a household size greater than 1."""
    cond = df["monthly_income_k"] < 6
    subset = df[cond]
    truth = (subset["household_size"] > 1).all()
    if truth:
        expl = f"All {len(subset)} households with income <6k have size >1."
    else:
        viol = subset[subset["household_size"] <= 1]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a household has a vehicle count of 0, then their monthly income is greater than or equal to $9k."""
    cond = df["vehicle_count"] == 0
    subset = df[cond]
    truth = (subset["monthly_income_k"] >= 9).all()
    if truth:
        expl = f"All {len(subset)} households with vehicle count 0 have income >=9k."
    else:
        viol = subset[subset["monthly_income_k"] < 9]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one household in the rural region with a monthly income greater than $9k."""
    cond = (df["region"] == "rural") & (df["monthly_income_k"] > 9)
    truth = not df[cond].empty
    if truth:
        sample = df[cond].iloc[0]
        expl = f"Found household {sample['household_id']} with income {sample['monthly_income_k']}k."
    else:
        expl = "No rural household with income >9k found."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. For all households with an internet type of satellite, their monthly income is less than or equal to $10.9k."""
    cond = df["internet_type"] == "satellite"
    subset = df[cond]
    truth = (subset["monthly_income_k"] <= 10.9).all()
    if truth:
        expl = f"All {len(subset)} satellite households have income <=10.9k."
    else:
        viol = subset[subset["monthly_income_k"] > 10.9]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a household has a household size of 1, then their monthly income is greater than or equal to $6.4k."""
    cond = df["household_size"] == 1
    subset = df[cond]
    truth = (subset["monthly_income_k"] >= 6.4).all()
    if truth:
        expl = f"All {len(subset)} households with size 1 have income >=6.4k."
    else:
        viol = subset[subset["monthly_income_k"] < 6.4]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All households with a utility cost less than $150 have a household size of 1 or 2."""
    cond = df["utility_cost"] < 150
    subset = df[cond]
    truth = subset["household_size"].isin([1, 2]).all()
    if truth:
        expl = f"All {len(subset)} households with utility cost <150 have size 1 or 2."
    else:
        viol = subset[~subset["household_size"].isin([1, 2])]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a household is in the suburban region, then their utility cost is greater than or equal to $85.1."""
    cond = df["region"] == "suburban"
    subset = df[cond]
    truth = (subset["utility_cost"] >= 85.1).all()
    if truth:
        expl = f"All {len(subset)} suburban households have utility cost >=85.1."
    else:
        viol = subset[subset["utility_cost"] < 85.1]
        expl = f"{len(viol)} households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_74.csv")

    # Convert numeric columns safely
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
        (18, stmt_18),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()