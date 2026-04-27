import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than $10k have a household size greater than 2."""
    condition = df[df["monthly_income_k"] > 10]["household_size"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['monthly_income_k'] > 10])} households with income > $10k have household size > 2."
    else:
        viol = df[(df["monthly_income_k"] > 10) & (df["household_size"] <= 2)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is located in an urban region, then their monthly income is greater than $2k."""
    condition = df[df["region"] == "urban"]["monthly_income_k"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['region'] == 'urban'])} urban households have income > $2k."
    else:
        viol = df[(df["region"] == "urban") & (df["monthly_income_k"] <= 2)]
        expl = f"{len(viol)} urban households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in a rural region with a monthly income greater than $9k."""
    condition = df[(df["region"] == "rural") & (df["monthly_income_k"] > 9)]
    truth = len(condition) > 0
    if truth:
        expl = f"There is at least one rural household with income > $9k (ID: {condition.iloc[0]['household_id']})."
    else:
        expl = "No rural households found with income > $9k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a household size greater than 5 have a monthly income greater than $8k."""
    condition = df[df["household_size"] > 5]["monthly_income_k"] > 8
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['household_size'] > 5])} households with size > 5 have income > $8k."
    else:
        viol = df[(df["household_size"] > 5) & (df["monthly_income_k"] <= 8)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count greater than 1, then their monthly income is greater than $4k."""
    condition = df[df["vehicle_count"] > 1]["monthly_income_k"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['vehicle_count'] > 1])} households with >1 vehicle have income > $4k."
    else:
        viol = df[(df["vehicle_count"] > 1) & (df["monthly_income_k"] <= 4)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most households have a utility cost greater than $150."""
    condition = df["utility_cost"] > 150
    truth = condition.sum() > len(df) / 2
    if truth:
        expl = f"More than half ({condition.sum()} out of {len(df)}) of households have utility cost > $150."
    else:
        expl = f"Less than half ({condition.sum()} out of {len(df)}) of households have utility cost > $150."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with a monthly income less than $4k have a household size less than 4."""
    condition = df[df["monthly_income_k"] < 4]["household_size"] < 4
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['monthly_income_k'] < 4])} households with income < $4k have household size < 4."
    else:
        viol = df[(df["monthly_income_k"] < 4) & (df["household_size"] >= 4)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household is located in a suburban region, then their internet type is not fiber."""
    condition = df[df["region"] == "suburban"]["internet_type"]!= "fiber"
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['region'] =='suburban'])} suburban households do not use fiber internet."
    else:
        viol = df[(df["region"] == "suburban") & (df["internet_type"] == "fiber")]
        expl = f"{len(viol)} suburban households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in an urban region with a rent less than $1.5k."""
    condition = df[(df["region"] == "urban") & (df["rent_k"] < 1.5)]
    truth = len(condition) > 0
    if truth:
        expl = f"There is at least one urban household with rent < $1.5k (ID: {condition.iloc[0]['household_id']})."
    else:
        expl = "No urban households found with rent < $1.5k."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All households with a household size less than 3 have a monthly income greater than $3k."""
    condition = df[df["household_size"] < 3]["monthly_income_k"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['household_size'] < 3])} households with size < 3 have income > $3k."
    else:
        viol = df[(df["household_size"] < 3) & (df["monthly_income_k"] <= 3)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household has a monthly income greater than $9k, then their household size is greater than 2."""
    condition = df[df["monthly_income_k"] > 9]["household_size"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['monthly_income_k'] > 9])} households with income > $9k have household size > 2."
    else:
        viol = df[(df["monthly_income_k"] > 9) & (df["household_size"] <= 2)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most households have a monthly income less than $12k."""
    condition = df["monthly_income_k"] < 12
    truth = condition.sum() > len(df) / 2
    if truth:
        expl = f"More than half ({condition.sum()} out of {len(df)}) of households have income < $12k."
    else:
        expl = f"Less than half ({condition.sum()} out of {len(df)}) of households have income < $12k."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All households with a utility cost less than $200 have a household size less than 5."""
    condition = df[df["utility_cost"] < 200]["household_size"] < 5
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['utility_cost'] < 200])} households with utility cost < $200 have household size < 5."
    else:
        viol = df[(df["utility_cost"] < 200) & (df["household_size"] >= 5)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household is located in a rural region, then their vehicle count is less than 3."""
    condition = df[df["region"] == "rural"]["vehicle_count"] < 3
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['region'] == 'rural'])} rural households have vehicle count < 3."
    else:
        viol = df[(df["region"] == "rural") & (df["vehicle_count"] >= 3)]
        expl = f"{len(viol)} rural households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household in a suburban region with a monthly income greater than $9k."""
    condition = df[(df["region"] == "suburban") & (df["monthly_income_k"] > 9)]
    truth = len(condition) > 0
    if truth:
        expl = f"There is at least one suburban household with income > $9k (ID: {condition.iloc[0]['household_id']})."
    else:
        expl = "No suburban households found with income > $9k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All households with a rent greater than $2k have a household size greater than 3."""
    condition = df[df["rent_k"] > 2]["household_size"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['rent_k'] > 2])} households with rent > $2k have household size > 3."
    else:
        viol = df[(df["rent_k"] > 2) & (df["household_size"] <= 3)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a household has a monthly income less than $3k, then their household size is less than 4."""
    condition = df[df["monthly_income_k"] < 3]["household_size"] < 4
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['monthly_income_k'] < 3])} households with income < $3k have household size < 4."
    else:
        viol = df[(df["monthly_income_k"] < 3) & (df["household_size"] >= 4)]
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(viol['household_id'].tolist())})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most households have a household size less than 6."""
    condition = df["household_size"] < 6
    truth = condition.sum() > len(df) / 2
    if truth:
        expl = f"More than half ({condition.sum()} out of {len(df)}) of households have household size < 6."
    else:
        expl = f"Less than half ({condition.sum()} out of {len(df)}) of households have household size < 6."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_34.csv")

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
        (17, stmt_17),
        (18, stmt_18)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()