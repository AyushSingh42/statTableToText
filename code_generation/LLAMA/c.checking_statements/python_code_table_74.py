import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than $9k have a household size greater than 1."""
    condition = (df["monthly_income_k"] > 9) & (df["household_size"] <= 1)
    truth = not condition.any()
    if truth:
        expl = "No household with income >$9k has household size <= 1."
    else:
        viol = df[condition]
        expl = f"{len(viol)} households violate the rule (income >9, size <=1)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their monthly income is less than or equal to $10.5k."""
    rural = df[df["region"] == "rural"]
    condition = rural["monthly_income_k"] > 10.5
    truth = not condition.any()
    if truth:
        expl = "All rural households have income <= $10.5k."
    else:
        viol = rural[condition]
        expl = f"{len(viol)} rural households violate the rule (income > 10.5)."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in the urban region with a monthly income less than $6k."""
    urban = df[df["region"] == "urban"]
    condition = urban["monthly_income_k"] < 6
    truth = condition.any()
    if truth:
        expl = "At least one urban household has income < $6k."
    else:
        expl = "No urban household has income < $6k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all households with a household size greater than 4, their monthly income is less than or equal to $10.5k."""
    large_households = df[df["household_size"] > 4]
    condition = large_households["monthly_income_k"] > 10.5
    truth = not condition.any()
    if truth:
        expl = "All households with size > 4 have income <= $10.5k."
    else:
        viol = large_households[condition]
        expl = f"{len(viol)} large households violate the rule (size >4, income > 10.5)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count greater than 1, then their monthly income is greater than or equal to $4.9k."""
    many_vehicles = df[df["vehicle_count"] > 1]
    condition = many_vehicles["monthly_income_k"] < 4.9
    truth = not condition.any()
    if truth:
        expl = "All households with >1 vehicle have income >= $4.9k."
    else:
        viol = many_vehicles[condition]
        expl = f"{len(viol)} households with >1 vehicle violate the rule (income < 4.9)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with a utility cost greater than $200 have a household size greater than 1."""
    high_utility = df[df["utility_cost"] > 200]
    condition = high_utility["household_size"] <= 1
    truth = not condition.any()
    if truth:
        expl = "All households with utility > $200 have household size > 1."
    else:
        viol = high_utility[condition]
        expl = f"{len(viol)} households with utility > 200 have size <= 1."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a household has an internet type of fiber, then their monthly income is greater than or equal to $4.9k."""
    fiber = df[df["internet_type"] == "fiber"]
    condition = fiber["monthly_income_k"] < 4.9
    truth = not condition.any()
    if truth:
        expl = "All fiber households have income >= $4.9k."
    else:
        viol = fiber[condition]
        expl = f"{len(viol)} fiber households violate the rule (income < 4.9)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one household in the suburban region with a monthly income greater than $9k."""
    suburban = df[df["region"] == "suburban"]
    condition = suburban["monthly_income_k"] > 9
    truth = condition.any()
    if truth:
        expl = "At least one suburban household has income > $9k."
    else:
        expl = "No suburban household has income > $9k."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. For all households with a rent greater than $2k, their household size is greater than 1."""
    high_rent = df[df["rent_k"] > 2]
    condition = high_rent["household_size"] <= 1
    truth = not condition.any()
    if truth:
        expl = "All households with rent > $2k have household size > 1."
    else:
        viol = high_rent[condition]
        expl = f"{len(viol)} households with rent > 2 have size <= 1."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a household is in the urban region, then their utility cost is greater than or equal to $84.1."""
    urban = df[df["region"] == "urban"]
    condition = urban["utility_cost"] < 84.1
    truth = not condition.any()
    if truth:
        expl = "All urban households have utility cost >= $84.1."
    else:
        viol = urban[condition]
        expl = f"{len(viol)} urban households violate the rule (utility < 84.1)."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Most households have a household size greater than 1."""
    total = len(df)
    large = len(df[df["household_size"] > 1])
    truth = large > total / 2
    if truth:
        expl = f"{large} out of {total} households have size > 1 (majority)."
    else:
        expl = f"{large} out of {total} households have size > 1 (not majority)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All households with a monthly income less than $6k have a household size greater than 1."""
    low_income = df[df["monthly_income_k"] < 6]
    condition = low_income["household_size"] <= 1
    truth = not condition.any()
    if truth:
        expl = "All households with income < $6k have household size > 1."
    else:
        viol = low_income[condition]
        expl = f"{len(viol)} low-income households have size <= 1."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a household has a vehicle count of 0, then their monthly income is greater than or equal to $9k."""
    no_vehicle = df[df["vehicle_count"] == 0]
    condition = no_vehicle["monthly_income_k"] < 9
    truth = not condition.any()
    if truth:
        expl = "All households with 0 vehicles have income >= $9k."
    else:
        viol = no_vehicle[condition]
        expl = f"{len(viol)} households with 0 vehicles violate the rule (income < 9)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one household in the rural region with a monthly income greater than $9k."""
    rural = df[df["region"] == "rural"]
    condition = rural["monthly_income_k"] > 9
    truth = condition.any()
    if truth:
        expl = "At least one rural household has income > $9k."
    else:
        expl = "No rural household has income > $9k."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. For all households with an internet type of satellite, their monthly income is less than or equal to $10.9k."""
    satellite = df[df["internet_type"] == "satellite"]
    condition = satellite["monthly_income_k"] > 10.9
    truth = not condition.any()
    if truth:
        expl = "All satellite households have income <= $10.9k."
    else:
        viol = satellite[condition]
        expl = f"{len(viol)} satellite households violate the rule (income > 10.9)."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a household has a household size of 1, then their monthly income is greater than or equal to $6.4k."""
    single = df[df["household_size"] == 1]
    condition = single["monthly_income_k"] < 6.4
    truth = not condition.any()
    if truth:
        expl = "All single-person households have income >= $6.4k."
    else:
        viol = single[condition]
        expl = f"{len(viol)} single-person households violate the rule (income < 6.4)."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All households with a utility cost less than $150 have a household size of 1 or 2."""
    low_utility = df[df["utility_cost"] < 150]
    condition = ~low_utility["household_size"].isin([1, 2])
    truth = not condition.any()
    if truth:
        expl = "All households with utility < $150 have household size 1 or 2."
    else:
        viol = low_utility[condition]
        expl = f"{len(viol)} households with utility < 150 have size!= 1 or 2."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a household is in the suburban region, then their utility cost is greater than or equal to $85.1."""
    suburban = df[df["region"] == "suburban"]
    condition = suburban["utility_cost"] < 85.1
    truth = not condition.any()
    if truth:
        expl = "All suburban households have utility cost >= $85.1."
    else:
        viol = suburban[condition]
        expl = f"{len(viol)} suburban households violate the rule (utility < 85.1)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_74.csv")

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