import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than 9k have a household size greater than 1."""
    condition = (df['monthly_income_k'] > 9) & (df['household_size'] <= 1)
    truth = not condition.any()
    if truth:
        expl = "No household with income >9k has household size <=1."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income >9k but size <=1)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their monthly income is less than 11k."""
    condition = (df['region'] == 'rural') & (df['monthly_income_k'] >= 11)
    truth = not condition.any()
    if truth:
        expl = "All rural households have income <11k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} rural households violate the rule (income >=11k)."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in a suburban region with a monthly income greater than 9k and a household size of 4."""
    condition = (df['region'] =='suburban') & (df['monthly_income_k'] > 9) & (df['household_size'] == 4)
    truth = condition.any()
    if truth:
        expl = "At least one suburban household meets criteria (income>9k, size=4)."
    else:
        expl = "No suburban household meets criteria (income>9k, size=4)."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a rent greater than 2.5k have a monthly income greater than 5k."""
    condition = (df['rent_k'] > 2.5) & (df['monthly_income_k'] <= 5)
    truth = not condition.any()
    if truth:
        expl = "All households with rent >2.5k have income >5k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (rent>2.5k but income <=5k)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count of 2, then their monthly income is greater than 5k."""
    condition = (df['vehicle_count'] == 2) & (df['monthly_income_k'] <= 5)
    truth = not condition.any()
    if truth:
        expl = "All households with 2 vehicles have income >5k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (2 vehicles but income <=5k)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most households have a utility cost greater than 150."""
    total = len(df)
    condition = df['utility_cost'] > 150
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of households have utility cost >150."
    else:
        expl = f"Less than half ({count}/{total}) of households have utility cost >150."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with a household size of 1 have a monthly income greater than 5k."""
    condition = (df['household_size'] == 1) & (df['monthly_income_k'] <= 5)
    truth = not condition.any()
    if truth:
        expl = "All households with size=1 have income >5k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size=1 but income <=5k)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household has an internet type of fiber, then their monthly income is greater than 4k."""
    condition = (df['internet_type'] == 'fiber') & (df['monthly_income_k'] <= 4)
    truth = not condition.any()
    if truth:
        expl = "All households with fiber internet have income >4k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (fiber internet but income <=4k)."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in an urban region with a monthly income greater than 6k and a household size of 1."""
    condition = (df['region'] == 'urban') & (df['monthly_income_k'] > 6) & (df['household_size'] == 1)
    truth = condition.any()
    if truth:
        expl = "At least one urban household meets criteria (income>6k, size=1)."
    else:
        expl = "No urban household meets criteria (income>6k, size=1)."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All households with a monthly income less than 6k have a household size less than 4."""
    condition = (df['monthly_income_k'] < 6) & (df['household_size'] >= 4)
    truth = not condition.any()
    if truth:
        expl = "All households with income <6k have size <4."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income <6k but size >=4)."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household is in a suburban region, then their rent is greater than 1k."""
    condition = (df['region'] =='suburban') & (df['rent_k'] <= 1)
    truth = not condition.any()
    if truth:
        expl = "All suburban households have rent >1k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} suburban households violate the rule (rent <=1k)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most households have a monthly income less than 10k."""
    total = len(df)
    condition = df['monthly_income_k'] < 10
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of households have income <10k."
    else:
        expl = f"Less than half ({count}/{total}) of households have income <10k."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All households with a vehicle count of 0 have a household size of 2 or 5."""
    condition = (df['vehicle_count'] == 0) & (~df['household_size'].isin([2, 5]))
    truth = not condition.any()
    if truth:
        expl = "All households with 0 vehicles have size 2 or 5."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (0 vehicles but size!=2,5)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household has a utility cost less than 200, then their household size is less than 4."""
    condition = (df['utility_cost'] < 200) & (df['household_size'] >= 4)
    truth = not condition.any()
    if truth:
        expl = "All households with utility cost <200 have size <4."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (utility <200 but size >=4)."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household in a rural region with a monthly income greater than 8k and a household size of 2."""
    condition = (df['region'] == 'rural') & (df['monthly_income_k'] > 8) & (df['household_size'] == 2)
    truth = condition.any()
    if truth:
        expl = "At least one rural household meets criteria (income>8k, size=2)."
    else:
        expl = "No rural household meets criteria (income>8k, size=2)."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All households with an internet type of satellite have a household size of 1 or 4."""
    condition = (df['internet_type'] =='satellite') & (~df['household_size'].isin([1, 4]))
    truth = not condition.any()
    if truth:
        expl = "All households with satellite internet have size 1 or 4."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (satellite internet but size!=1,4)."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a household has a rent less than 2k, then their monthly income is less than 7k."""
    condition = (df['rent_k'] < 2) & (df['monthly_income_k'] >= 7)
    truth = not condition.any()
    if truth:
        expl = "All households with rent <2k have income <7k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (rent <2k but income >=7k)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_84.csv")

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