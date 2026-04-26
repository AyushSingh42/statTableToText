import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with monthly income greater than 9k have a household size greater than 1."""
    condition = (df["monthly_income_k"] > 9) & (df["household_size"] <= 1)
    truth = not condition.any()
    if truth:
        expl = "No households with income > 9k have household size <= 1."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income > 9k but size <= 1)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a suburban region, then their utility cost is less than 200."""
    condition = (df["region"] == "suburban") & (df["utility_cost"] >= 200)
    truth = not condition.any()
    if truth:
        expl = "All suburban households have utility cost < 200."
    else:
        viol = df[condition]
        expl = f"{len(viol)} suburban households violate the rule (utility cost >= 200)."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in an urban region with a vehicle count of 0."""
    condition = (df["region"] == "urban") & (df["vehicle_count"] == 0)
    truth = condition.any()
    if truth:
        expl = "At least one urban household has 0 vehicles."
    else:
        expl = "No urban households have 0 vehicles."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all households with a household size greater than 5, their monthly income is greater than 7k."""
    condition = (df["household_size"] > 5) & (df["monthly_income_k"] <= 7)
    truth = not condition.any()
    if truth:
        expl = "All households with size > 5 have income > 7k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size > 5 but income <= 7k)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a fiber internet type, then their monthly income is greater than 3k."""
    condition = (df["internet_type"] == "fiber") & (df["monthly_income_k"] <= 3)
    truth = not condition.any()
    if truth:
        expl = "All fiber households have income > 3k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} fiber households violate the rule (income <= 3k)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with a monthly income less than 4k have a household size greater than 4."""
    condition = (df["monthly_income_k"] < 4) & (df["household_size"] <= 4)
    truth = not condition.any()
    if truth:
        expl = "All households with income < 4k have size > 4."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income < 4k but size <= 4)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most households in the data have a vehicle count greater than 0."""
    total = len(df)
    condition = df["vehicle_count"] > 0
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of households have > 0 vehicles."
    else:
        expl = f"Less than half ({count}/{total}) of households have > 0 vehicles."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household is in a rural region, then their monthly income is less than 9k."""
    condition = (df["region"] == "rural") & (df["monthly_income_k"] >= 9)
    truth = not condition.any()
    if truth:
        expl = "All rural households have income < 9k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} rural households violate the rule (income >= 9k)."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. For all households with a utility cost greater than 150, their household size is greater than 2."""
    condition = (df["utility_cost"] > 150) & (df["household_size"] <= 2)
    truth = not condition.any()
    if truth:
        expl = "All households with utility cost > 150 have size > 2."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (utility cost > 150 but size <= 2)."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one household in a suburban region with a monthly income greater than 10k."""
    condition = (df["region"] == "suburban") & (df["monthly_income_k"] > 10)
    truth = condition.any()
    if truth:
        expl = "At least one suburban household has income > 10k."
    else:
        expl = "No suburban households have income > 10k."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All households with a household size of 1 have a monthly income greater than 6k."""
    condition = (df["household_size"] == 1) & (df["monthly_income_k"] <= 6)
    truth = not condition.any()
    if truth:
        expl = "All households with size 1 have income > 6k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size = 1 but income <= 6k)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a household has a satellite internet type, then their household size is less than 6."""
    condition = (df["internet_type"] == "satellite") & (df["household_size"] >= 6)
    truth = not condition.any()
    if truth:
        expl = "All satellite households have size < 6."
    else:
        viol = df[condition]
        expl = f"{len(viol)} satellite households violate the rule (size >= 6)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. For all households with a monthly income greater than 8k, their rent is greater than 1k."""
    condition = (df["monthly_income_k"] > 8) & (df["rent_k"] <= 1)
    truth = not condition.any()
    if truth:
        expl = "All households with income > 8k have rent > 1k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income > 8k but rent <= 1k)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Most households in the data have a monthly income greater than 5k."""
    total = len(df)
    condition = df["monthly_income_k"] > 5
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of households have income > 5k."
    else:
        expl = f"Less than half ({count}/{total}) of households have income > 5k."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a household is in an urban region, then their utility cost is greater than 80."""
    condition = (df["region"] == "urban") & (df["utility_cost"] <= 80)
    truth = not condition.any()
    if truth:
        expl = "All urban households have utility cost > 80."
    else:
        viol = df[condition]
        expl = f"{len(viol)} urban households violate the rule (utility cost <= 80)."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one household with a vehicle count of 3."""
    condition = df["vehicle_count"] == 3
    truth = condition.any()
    if truth:
        expl = "At least one household has 3 vehicles."
    else:
        expl = "No household has 3 vehicles."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All households with a household size greater than 3 have a monthly income greater than 4k."""
    condition = (df["household_size"] > 3) & (df["monthly_income_k"] <= 4)
    truth = not condition.any()
    if truth:
        expl = "All households with size > 3 have income > 4k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size > 3 but income <= 4k)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_24.csv")

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