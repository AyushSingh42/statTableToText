import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with monthly income greater than 10k have a household size greater than or equal to 3."""
    condition = (df['monthly_income_k'] > 10) & (df['household_size'] < 3)
    truth = not condition.any()
    if truth:
        expl = "No household with income > 10k has household size < 3."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income > 10k but size < 3)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their monthly income is less than or equal to 11.1k."""
    rural = df[df['region'] == 'rural']
    condition = rural['monthly_income_k'] > 11.1
    truth = not condition.any()
    if truth:
        expl = "All rural households have income <= 11.1k."
    else:
        viol = rural[condition]
        expl = f"{len(viol)} rural households violate the rule (income > 11.1k)."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in the urban region with a monthly income less than 5k."""
    urban = df[df['region'] == 'urban']
    condition = urban['monthly_income_k'] < 5
    truth = condition.any()
    if truth:
        expl = "At least one urban household has income < 5k."
    else:
        expl = "No urban household has income < 5k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all households with a household size greater than or equal to 5, their rent is less than or equal to 2.8k."""
    condition = (df['household_size'] >= 5) & (df['rent_k'] > 2.8)
    truth = not condition.any()
    if truth:
        expl = "All households with size >= 5 have rent <= 2.8k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size >= 5 but rent > 2.8k)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count greater than 0, then their internet type is not satellite."""
    condition = (df['vehicle_count'] > 0) & (df['internet_type'] =='satellite')
    truth = not condition.any()
    if truth:
        expl = "All households with vehicles do not use satellite internet."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (have vehicles but use satellite internet)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with a utility cost greater than 190 have an internet type of either cable or fiber."""
    condition = (df['utility_cost'] > 190) & (~df['internet_type'].isin(['cable', 'fiber']))
    truth = not condition.any()
    if truth:
        expl = "All households with utility cost > 190 use cable or fiber internet."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (utility > 190 but not cable/fiber)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all households with a monthly income less than 6k, their household size is greater than or equal to 4."""
    condition = (df['monthly_income_k'] < 6) & (df['household_size'] < 4)
    truth = not condition.any()
    if truth:
        expl = "All households with income < 6k have size >= 4."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income < 6k but size < 4)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one household in the suburban region with a monthly income greater than 10k."""
    suburban = df[df['region'] =='suburban']
    condition = suburban['monthly_income_k'] > 10
    truth = condition.any()
    if truth:
        expl = "At least one suburban household has income > 10k."
    else:
        expl = "No suburban household has income > 10k."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a household has a household size of 1, then their monthly income is less than 7k."""
    condition = (df['household_size'] == 1) & (df['monthly_income_k'] >= 7)
    truth = not condition.any()
    if truth:
        expl = "All households with size 1 have income < 7k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size=1 but income >= 7k)."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Most households have a vehicle count greater than or equal to 2."""
    condition = df['vehicle_count'] >= 2
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of households have 2+ vehicles."
    else:
        expl = f"Less than half ({count}/{total}) of households have 2+ vehicles."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. For all households with a rent less than 2k, their household size is greater than or equal to 4."""
    condition = (df['rent_k'] < 2) & (df['household_size'] < 4)
    truth = not condition.any()
    if truth:
        expl = "All households with rent < 2k have size >= 4."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (rent < 2k but size < 4)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a household is in an urban region, then their utility cost is greater than 120."""
    urban = df[df['region'] == 'urban']
    condition = urban['utility_cost'] <= 120
    truth = not condition.any()
    if truth:
        expl = "All urban households have utility cost > 120."
    else:
        viol = urban[condition]
        expl = f"{len(viol)} urban households violate the rule (utility cost <= 120)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All households with a monthly income greater than 10.8k have a household size greater than or equal to 3."""
    condition = (df['monthly_income_k'] > 10.8) & (df['household_size'] < 3)
    truth = not condition.any()
    if truth:
        expl = "No household with income > 10.8k has household size < 3."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income > 10.8k but size < 3)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one household in the rural region with a utility cost less than 100."""
    rural = df[df['region'] == 'rural']
    condition = rural['utility_cost'] < 100
    truth = condition.any()
    if truth:
        expl = "At least one rural household has utility cost < 100."
    else:
        expl = "No rural household has utility cost < 100."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. For all households with an internet type of fiber, their household size is greater than or equal to 3."""
    condition = (df['internet_type'] == 'fiber') & (df['household_size'] < 3)
    truth = not condition.any()
    if truth:
        expl = "All households with fiber internet have size >= 3."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (fiber internet but size < 3)."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a household has a household size of 6, then their monthly income is less than 11k."""
    condition = (df['household_size'] == 6) & (df['monthly_income_k'] >= 11)
    truth = not condition.any()
    if truth:
        expl = "All households with size 6 have income < 11k."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (size=6 but income >= 11k)."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. Most households have a utility cost greater than 100."""
    condition = df['utility_cost'] > 100
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of households have utility cost > 100."
    else:
        expl = f"Less than half ({count}/{total}) of households have utility cost > 100."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. For all households with a vehicle count of 0, their internet type is satellite."""
    condition = (df['vehicle_count'] == 0) & (df['internet_type']!='satellite')
    truth = not condition.any()
    if truth:
        expl = "All households with no vehicles use satellite internet."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (no vehicles but not satellite internet)."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. If a household is in a suburban region, then their monthly income is less than 11k."""
    suburban = df[df['region'] =='suburban']
    condition = suburban['monthly_income_k'] >= 11
    truth = not condition.any()
    if truth:
        expl = "All suburban households have income < 11k."
    else:
        viol = suburban[condition]
        expl = f"{len(viol)} suburban households violate the rule (income >= 11k)."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. All households with a rent greater than 2.5k have a household size greater than or equal to 3."""
    condition = (df['rent_k'] > 2.5) & (df['household_size'] < 3)
    truth = not condition.any()
    if truth:
        expl = "No household with rent > 2.5k has household size < 3."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (rent > 2.5k but size < 3)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_14.csv")

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
        (20, stmt_20)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()