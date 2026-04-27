import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with monthly income greater than 8k have a household size greater than 1."""
    condition = (df["monthly_income_k"] > 8) & (df["household_size"] <= 1)
    truth = not condition.any()
    if truth:
        expl = "No household with income >8k has household size <=1."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income >8k but size <=1)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in an urban region, then their monthly income is greater than 4k."""
    condition = (df["region"] == "urban") & (df["monthly_income_k"] <= 4)
    truth = not condition.any()
    if truth:
        expl = "All urban households have income >4k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} urban households have income <=4k."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in a rural region with a monthly income greater than 8k."""
    condition = (df["region"] == "rural") & (df["monthly_income_k"] > 8)
    truth = condition.any()
    if truth:
        expl = "At least one rural household has income >8k."
    else:
        expl = "No rural household has income >8k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a household size of 1 have a monthly income greater than 4k."""
    condition = (df["household_size"] == 1) & (df["monthly_income_k"] <= 4)
    truth = not condition.any()
    if truth:
        expl = "All households with size=1 have income >4k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households with size=1 have income <=4k."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count of 3, then their monthly income is greater than 6k."""
    condition = (df["vehicle_count"] == 3) & (df["monthly_income_k"] <= 6)
    truth = not condition.any()
    if truth:
        expl = "All households with 3 vehicles have income >6k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households with 3 vehicles have income <=6k."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most households have a utility cost greater than 100."""
    total = len(df)
    condition = df["utility_cost"] > 100
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} households have utility cost >100 (most)."
    else:
        expl = f"{count} out of {total} households have utility cost >100 (not most)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with a monthly income greater than 9k have a rent greater than 1k."""
    condition = (df["monthly_income_k"] > 9) & (df["rent_k"] <= 1)
    truth = not condition.any()
    if truth:
        expl = "All households with income >9k have rent >1k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households with income >9k have rent <=1k."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household has an internet type of fiber, then their monthly income is greater than 5k."""
    condition = (df["internet_type"] == "fiber") & (df["monthly_income_k"] <= 5)
    truth = not condition.any()
    if truth:
        expl = "All fiber households have income >5k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} fiber households have income <=5k."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in a suburban region with a monthly income greater than 9k."""
    condition = (df["region"] == "suburban") & (df["monthly_income_k"] > 9)
    truth = condition.any()
    if truth:
        expl = "At least one suburban household has income >9k."
    else:
        expl = "No suburban household has income >9k."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All households with a household size greater than 5 have a vehicle count greater than 0."""
    condition = (df["household_size"] > 5) & (df["vehicle_count"] == 0)
    truth = not condition.any()
    if truth:
        expl = "All households with size>5 have vehicle count >0."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households with size>5 have vehicle count =0."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household is in a rural region, then their utility cost is less than 200."""
    condition = (df["region"] == "rural") & (df["utility_cost"] >= 200)
    truth = not condition.any()
    if truth:
        expl = "All rural households have utility cost <200."
    else:
        viol = df[condition]
        expl = f"{len(viol)} rural households have utility cost >=200."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most households have a household size greater than 1."""
    total = len(df)
    condition = df["household_size"] > 1
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} households have size >1 (most)."
    else:
        expl = f"{count} out of {total} households have size >1 (not most)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All households with a monthly income less than 5k have a household size greater than 1."""
    condition = (df["monthly_income_k"] < 5) & (df["household_size"] <= 1)
    truth = not condition.any()
    if truth:
        expl = "All households with income <5k have size >1."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households with income <5k have size <=1."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household has a rent greater than 2k, then their monthly income is greater than 8k."""
    condition = (df["rent_k"] > 2) & (df["monthly_income_k"] <= 8)
    truth = not condition.any()
    if truth:
        expl = "All households with rent >2k have income >8k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households with rent >2k have income <=8k."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household with a vehicle count of 3 and a monthly income greater than 8k."""
    condition = (df["vehicle_count"] == 3) & (df["monthly_income_k"] > 8)
    truth = condition.any()
    if truth:
        expl = "At least one household has 3 vehicles and income >8k."
    else:
        expl = "No household has 3 vehicles and income >8k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All households with an internet type of satellite have a monthly income less than 9k."""
    condition = (df["internet_type"] == "satellite") & (df["monthly_income_k"] >= 9)
    truth = not condition.any()
    if truth:
        expl = "All satellite households have income <9k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} satellite households have income >=9k."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a household has a utility cost greater than 150, then their household size is greater than 1."""
    condition = (df["utility_cost"] > 150) & (df["household_size"] <= 1)
    truth = not condition.any()
    if truth:
        expl = "All households with utility cost >150 have size >1."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households with utility cost >150 have size <=1."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most households have a monthly income greater than 5k."""
    total = len(df)
    condition = df["monthly_income_k"] > 5
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} households have income >5k (most)."
    else:
        expl = f"{count} out of {total} households have income >5k (not most)."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All households with a household size of 6 have a monthly income greater than 6k."""
    condition = (df["household_size"] == 6) & (df["monthly_income_k"] <= 6)
    truth = not condition.any()
    if truth:
        expl = "All households with size=6 have income >6k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households with size=6 have income <=6k."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a household is in an urban region, then their utility cost is greater than 80."""
    condition = (df["region"] == "urban") & (df["utility_cost"] <= 80)
    truth = not condition.any()
    if truth:
        expl = "All urban households have utility cost >80."
    else:
        viol = df[condition]
        expl = f"{len(viol)} urban households have utility cost <=80."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one household in a rural region with a household size of 6."""
    condition = (df["region"] == "rural") & (df["household_size"] == 6)
    truth = condition.any()
    if truth:
        expl = "At least one rural household has size=6."
    else:
        expl = "No rural household has size=6."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. All households with a monthly income greater than 10k have a rent greater than 1.5k."""
    condition = (df["monthly_income_k"] > 10) & (df["rent_k"] <= 1.5)
    truth = not condition.any()
    if truth:
        expl = "All households with income >10k have rent >1.5k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households with income >10k have rent <=1.5k."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_64.csv")

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
        (18, stmt_18),
        (19, stmt_19),
        (20, stmt_20),
        (21, stmt_21),
        (22, stmt_22)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()