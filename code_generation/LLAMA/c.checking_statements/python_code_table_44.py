import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with monthly income greater than 8k have a household size greater than 3."""
    condition = (df["monthly_income_k"] > 8) & (df["household_size"] <= 3)
    truth = not condition.any()
    if truth:
        expl = "All households with income > 8k have household size > 3."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income > 8k but size <= 3)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their utility cost is greater than 140."""
    condition = (df["region"] == "rural") & (df["utility_cost"] <= 140)
    truth = not condition.any()
    if truth:
        expl = "All rural households have utility cost > 140."
    else:
        viol = df[condition]
        expl = f"{len(viol)} rural households violate the rule (utility cost <= 140)."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in the suburban region with a monthly income greater than 10k."""
    condition = (df["region"] == "suburban") & (df["monthly_income_k"] > 10)
    truth = condition.any()
    if truth:
        expl = "At least one suburban household has income > 10k."
    else:
        expl = "No suburban household has income > 10k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a vehicle count greater than 2 have a monthly income greater than 4k."""
    condition = (df["vehicle_count"] > 2) & (df["monthly_income_k"] <= 4)
    truth = not condition.any()
    if truth:
        expl = "All households with >2 vehicles have income > 4k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (vehicles > 2 but income <= 4k)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a household size greater than 5, then their rent is greater than 1.5k."""
    condition = (df["household_size"] > 5) & (df["rent_k"] <= 1.5)
    truth = not condition.any()
    if truth:
        expl = "All households with size > 5 have rent > 1.5k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size > 5 but rent <= 1.5k)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most households in the table have a household size less than or equal to 5."""
    total = len(df)
    condition = df["household_size"] <= 5
    count_leq5 = condition.sum()
    truth = count_leq5 > total / 2
    if truth:
        expl = f"More than half ({count_leq5}/{total}) of households have size <= 5."
    else:
        expl = f"Less than half ({count_leq5}/{total}) of households have size <= 5."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with internet type 'fiber' have a monthly income greater than 3k."""
    condition = (df["internet_type"] == "fiber") & (df["monthly_income_k"] <= 3)
    truth = not condition.any()
    if truth:
        expl = "All fiber households have income > 3k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} fiber households violate the rule (income <= 3k)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household is in an urban region, then their household size is greater than or equal to 3."""
    condition = (df["region"] == "urban") & (df["household_size"] < 3)
    truth = not condition.any()
    if truth:
        expl = "All urban households have size >= 3."
    else:
        viol = df[condition]
        expl = f"{len(viol)} urban households violate the rule (size < 3)."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in the rural region with a vehicle count of 0."""
    condition = (df["region"] == "rural") & (df["vehicle_count"] == 0)
    truth = condition.any()
    if truth:
        expl = "At least one rural household has 0 vehicles."
    else:
        expl = "No rural household has 0 vehicles."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All households with a monthly income less than or equal to 4k have a household size less than or equal to 5."""
    condition = (df["monthly_income_k"] <= 4) & (df["household_size"] > 5)
    truth = not condition.any()
    if truth:
        expl = "All households with income <= 4k have size <= 5."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income <= 4k but size > 5)."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household has a household size of 2, then their monthly income is greater than 5k."""
    condition = (df["household_size"] == 2) & (df["monthly_income_k"] <= 5)
    truth = not condition.any()
    if truth:
        expl = "All households with size 2 have income > 5k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size = 2 but income <= 5k)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All households with internet type'satellite' have a household size less than or equal to 6."""
    condition = (df["internet_type"] == "satellite") & (df["household_size"] > 6)
    truth = not condition.any()
    if truth:
        expl = "All satellite households have size <= 6."
    else:
        viol = df[condition]
        expl = f"{len(viol)} satellite households violate the rule (size > 6)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most households in the table have a utility cost greater than 100."""
    total = len(df)
    condition = df["utility_cost"] > 100
    count_gt100 = condition.sum()
    truth = count_gt100 > total / 2
    if truth:
        expl = f"More than half ({count_gt100}/{total}) of households have utility cost > 100."
    else:
        expl = f"Less than half ({count_gt100}/{total}) of households have utility cost > 100."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household is in a suburban region, then their rent is greater than 1k."""
    condition = (df["region"] == "suburban") & (df["rent_k"] <= 1)
    truth = not condition.any()
    if truth:
        expl = "All suburban households have rent > 1k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} suburban households violate the rule (rent <= 1k)."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household in the urban region with a monthly income less than 5k."""
    condition = (df["region"] == "urban") & (df["monthly_income_k"] < 5)
    truth = condition.any()
    if truth:
        expl = "At least one urban household has income < 5k."
    else:
        expl = "No urban household has income < 5k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All households with a vehicle count of 1 have a monthly income greater than 3k."""
    condition = (df["vehicle_count"] == 1) & (df["monthly_income_k"] <= 3)
    truth = not condition.any()
    if truth:
        expl = "All households with 1 vehicle have income > 3k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (1 vehicle but income <= 3k)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_44.csv")

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
        (16, stmt_16)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()