import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than 10k have a household size greater than 1."""
    condition = df[df["monthly_income_k"] > 10]["household_size"] > 1
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['monthly_income_k'] > 10])} households with income > 10k have household size > 1."
    else:
        viol = df[(df["monthly_income_k"] > 10) & (df["household_size"] <= 1)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their utility cost is greater than 100."""
    condition = df[df["region"] == "rural"]["utility_cost"] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['region'] == 'rural'])} rural households have utility cost > 100."
    else:
        viol = df[(df["region"] == "rural") & (df["utility_cost"] <= 100)]
        expl = f"{len(viol)} rural households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All households with a vehicle count of 2 have a monthly income greater than 5k."""
    condition = df[df["vehicle_count"] == 2]["monthly_income_k"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['vehicle_count'] == 2])} households with 2 vehicles have income > 5k."
    else:
        viol = df[(df["vehicle_count"] == 2) & (df["monthly_income_k"] <= 5)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one household in a suburban region with a monthly income greater than 11k."""
    subset = df[(df["region"] == "suburban") & (df["monthly_income_k"] > 11)]
    truth = len(subset) >= 1
    if truth:
        expl = f"There is at least one suburban household with income > 11k (ID: {subset.iloc[0]['household_id']})."
    else:
        expl = "No suburban household has income > 11k."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a household size of 6, then their monthly income is less than 12k."""
    condition = df[df["household_size"] == 6]["monthly_income_k"] < 12
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['household_size'] == 6])} households with size 6 have income < 12k."
    else:
        viol = df[(df["household_size"] == 6) & (df["monthly_income_k"] >= 12)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with a monthly income less than 4k have a household size less than 6."""
    condition = df[df["monthly_income_k"] < 4]["household_size"] < 6
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['monthly_income_k'] < 4])} households with income < 4k have household size < 6."
    else:
        viol = df[(df["monthly_income_k"] < 4) & (df["household_size"] >= 6)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most households in the data have a household size of 3 or more."""
    count_ge3 = len(df[df["household_size"] >= 3])
    total = len(df)
    truth = count_ge3 > total / 2
    if truth:
        expl = f"{count_ge3} out of {total} households have size >= 3 (more than half)."
    else:
        expl = f"{count_ge3} out of {total} households have size >= 3 (not more than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household has a vehicle count of 0, then their monthly income is greater than 5k."""
    condition = df[df["vehicle_count"] == 0]["monthly_income_k"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['vehicle_count'] == 0])} households with 0 vehicles have income > 5k."
    else:
        viol = df[(df["vehicle_count"] == 0) & (df["monthly_income_k"] <= 5)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All households with a monthly income greater than 9k have a rent cost less than 3k."""
    condition = df[df["monthly_income_k"] > 9]["rent_k"] < 3
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['monthly_income_k'] > 9])} households with income > 9k have rent < 3k."
    else:
        viol = df[(df["monthly_income_k"] > 9) & (df["rent_k"] >= 3)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one household in an urban region with a monthly income greater than 10k."""
    subset = df[(df["region"] == "urban") & (df["monthly_income_k"] > 10)]
    truth = len(subset) >= 1
    if truth:
        expl = f"There is at least one urban household with income > 10k (ID: {subset.iloc[0]['household_id']})."
    else:
        expl = "No urban household has income > 10k."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household has a household size of 1, then their monthly income is greater than 10k."""
    condition = df[df["household_size"] == 1]["monthly_income_k"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['household_size'] == 1])} households with size 1 have income > 10k."
    else:
        viol = df[(df["household_size"] == 1) & (df["monthly_income_k"] <= 10)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All households with a utility cost greater than 200 have a household size greater than 2."""
    condition = df[df["utility_cost"] > 200]["household_size"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['utility_cost'] > 200])} households with utility cost > 200 have household size > 2."
    else:
        viol = df[(df["utility_cost"] > 200) & (df["household_size"] <= 2)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most households in the data have a utility cost greater than 100."""
    count_gt100 = len(df[df["utility_cost"] > 100])
    total = len(df)
    truth = count_gt100 > total / 2
    if truth:
        expl = f"{count_gt100} out of {total} households have utility cost > 100 (more than half)."
    else:
        expl = f"{count_gt100} out of {total} households have utility cost > 100 (not more than half)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household is in a rural region, then their internet type is not fiber."""
    condition = df[df["region"] == "rural"]["internet_type"]!= "fiber"
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['region'] == 'rural'])} rural households do not use fiber internet."
    else:
        viol = df[(df["region"] == "rural") & (df["internet_type"] == "fiber")]
        expl = f"{len(viol)} rural households use fiber internet (violates rule)."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All households with a monthly income less than 6k have a household size greater than 2."""
    condition = df[df["monthly_income_k"] < 6]["household_size"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['monthly_income_k'] < 6])} households with income < 6k have household size > 2."
    else:
        viol = df[(df["monthly_income_k"] < 6) & (df["household_size"] <= 2)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one household in a suburban region with a vehicle count of 2."""
    subset = df[(df["region"] == "suburban") & (df["vehicle_count"] == 2)]
    truth = len(subset) >= 1
    if truth:
        expl = f"There is at least one suburban household with 2 vehicles (ID: {subset.iloc[0]['household_id']})."
    else:
        expl = "No suburban household has 2 vehicles."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a household has a household size of 5, then their monthly income is greater than 3k."""
    condition = df[df["household_size"] == 5]["monthly_income_k"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['household_size'] == 5])} households with size 5 have income > 3k."
    else:
        viol = df[(df["household_size"] == 5) & (df["monthly_income_k"] <= 3)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_4.csv")

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