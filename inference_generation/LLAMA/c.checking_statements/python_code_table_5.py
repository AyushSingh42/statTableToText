import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income above 8k reside in either urban or suburban regions."""
    high_income = df[df["monthly_income_k"] > 8]
    condition = high_income["region"].isin(["urban", "suburban"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_income)} households with income above 8k reside in urban or suburban regions."
    else:
        viol = high_income[~condition]
        expl = f"{len(viol)} households violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household has a vehicle count of 2, then their utility cost is always above 150."""
    two_vehicles = df[df["vehicle_count"] == 2]
    condition = two_vehicles["utility_cost"] > 150
    truth = condition.all()
    if truth:
        expl = f"All {len(two_vehicles)} households with 2 vehicles have utility cost above 150."
    else:
        viol = two_vehicles[~condition]
        expl = f"{len(viol)} households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every household with a household size of 5 or more resides in either suburban or rural regions."""
    large_households = df[df["household_size"] >= 5]
    condition = large_households["region"].isin(["suburban", "rural"])
    truth = condition.all()
    if truth:
        expl = f"All {len(large_households)} large households reside in suburban or rural regions."
    else:
        viol = large_households[~condition]
        expl = f"{len(viol)} households violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a rent above 2k have a monthly income above 6k."""
    high_rent = df[df["rent_k"] > 2]
    condition = high_rent["monthly_income_k"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rent)} households with rent above 2k have income above 6k."
    else:
        viol = high_rent[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a household size of 1, then their internet type is always either fiber or dsl."""
    single_person = df[df["household_size"] == 1]
    condition = single_person["internet_type"].isin(["fiber", "dsl"])
    truth = condition.all()
    if truth:
        expl = f"All {len(single_person)} single-person households have fiber or dsl internet."
    else:
        viol = single_person[~condition]
        expl = f"{len(viol)} households violate the rule (internet types: {', '.join(map(str, viol['internet_type'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with a utility cost above 200 reside in either suburban or rural regions."""
    high_utility = df[df["utility_cost"] > 200]
    condition = high_utility["region"].isin(["suburban", "rural"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_utility)} households with utility cost above 200 reside in suburban or rural regions."
    else:
        viol = high_utility[~condition]
        expl = f"{len(viol)} households violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every household with a vehicle count of 3 or more resides in either suburban or rural regions."""
    many_vehicles = df[df["vehicle_count"] >= 3]
    condition = many_vehicles["region"].isin(["suburban", "rural"])
    truth = condition.all()
    if truth:
        expl = f"All {len(many_vehicles)} households with 3 or more vehicles reside in suburban or rural regions."
    else:
        viol = many_vehicles[~condition]
        expl = f"{len(viol)} households violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household has a monthly income above 7k, then their household size is always 2 or more."""
    high_income = df[df["monthly_income_k"] > 7]
    condition = high_income["household_size"] >= 2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_income)} households with income above 7k have size 2 or more."
    else:
        viol = high_income[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All households with a rent below 1.5k reside in rural regions."""
    low_rent = df[df["rent_k"] < 1.5]
    condition = low_rent["region"] == "rural"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_rent)} households with rent below 1.5k reside in rural regions."
    else:
        viol = low_rent[~condition]
        expl = f"{len(viol)} households violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Every household with a household size of 4 or more has a monthly income above 6k."""
    large_households = df[df["household_size"] >= 4]
    condition = large_households["monthly_income_k"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(large_households)} large households have income above 6k."
    else:
        viol = large_households[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household has a utility cost above 180, then their household size is always 3 or more."""
    high_utility = df[df["utility_cost"] > 180]
    condition = high_utility["household_size"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(high_utility)} households with utility cost above 180 have size 3 or more."
    else:
        viol = high_utility[~condition]
        expl = f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All households with a vehicle count of 1 or less reside in either urban or rural regions."""
    few_vehicles = df[df["vehicle_count"] <= 1]
    condition = few_vehicles["region"].isin(["urban", "rural"])
    truth = condition.all()
    if truth:
        expl = f"All {len(few_vehicles)} households with 1 or fewer vehicles reside in urban or rural regions."
    else:
        viol = few_vehicles[~condition]
        expl = f"{len(viol)} households violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Every household with a monthly income below 5k resides in either rural or urban regions."""
    low_income = df[df["monthly_income_k"] < 5]
    condition = low_income["region"].isin(["rural", "urban"])
    truth = condition.all()
    if truth:
        expl = f"All {len(low_income)} households with income below 5k reside in rural or urban regions."
    else:
        viol = low_income[~condition]
        expl = f"{len(viol)} households violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household has a household size of 2, then their rent is always below 2.5k."""
    small_households = df[df["household_size"] == 2]
    condition = small_households["rent_k"] < 2.5
    truth = condition.all()
    if truth:
        expl = f"All {len(small_households)} small households have rent below 2.5k."
    else:
        viol = small_households[~condition]
        expl = f"{len(viol)} households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All households with a utility cost below 120 reside in rural regions."""
    low_utility = df[df["utility_cost"] < 120]
    condition = low_utility["region"] == "rural"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_utility)} households with utility cost below 120 reside in rural regions."
    else:
        viol = low_utility[~condition]
        expl = f"{len(viol)} households violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_5.csv")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10), (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()