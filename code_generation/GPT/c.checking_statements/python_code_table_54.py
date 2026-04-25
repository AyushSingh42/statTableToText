import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all households with rent ≤ 1.0 k, utility cost is at least 180 k."""
    condition = (df["rent_k"] <= 1.0) & (df["utility_cost"] >= 180.0)
    truth = condition.all()
    if truth:
        expl = "All households with rent ≤ 1.0 k have utility cost ≥ 180 k."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} households violate the rule (rent, utility_cost): {[(r, u) for r, u in zip(viol['rent_k'], viol['utility_cost'])]}."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all households with no vehicles, utility cost is at least 172.2 k."""
    condition = (df["vehicle_count"] == 0) & (df["utility_cost"] >= 172.2)
    truth = condition.all()
    if truth:
        expl = "All households with no vehicles have utility cost ≥ 172.2 k."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} households violate the rule (vehicle_count, utility_cost): {[(v, u) for v, u in zip(viol['vehicle_count'], viol['utility_cost'])]}."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all households with size ≥ 6, rent is at most 1.9 k."""
    condition = (df["household_size"] >= 6) & (df["rent_k"] <= 1.9)
    truth = condition.all()
    if truth:
        expl = "All households with size ≥ 6 have rent ≤ 1.9 k."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} households violate the rule (size, rent): {[(s, r) for s, r in zip(viol['household_size'], viol['rent_k'])]}."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All urban households have internet type either fiber or satellite."""
    urban = df[df["region"] == "urban"]
    valid_internet = urban["internet_type"].isin(["fiber", "satellite"])
    truth = valid_internet.all()
    if truth:
        expl = "All urban households have internet type fiber or satellite."
    else:
        viol = urban[~valid_internet]
        expl = f"{len(viol)} urban households violate the rule (internet_type): {list(viol['internet_type'])}."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All rural households have rent of at least 1.5 k."""
    rural = df[df["region"] == "rural"]
    condition = rural["rent_k"] >= 1.5
    truth = condition.all()
    if truth:
        expl = "All rural households have rent ≥ 1.5 k."
    else:
        viol = rural[~condition]
        expl = f"{len(viol)} rural households violate the rule (rent): {list(viol['rent_k'])}."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with monthly income > 10 k have utility cost greater than 115 k."""
    condition = (df["monthly_income_k"] > 10.0) & (df["utility_cost"] > 115.0)
    truth = condition.all()
    if truth:
        expl = "All households with income > 10 k have utility cost > 115 k."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} households violate the rule (income, utility_cost): {[(i, u) for i, u in zip(viol['monthly_income_k'], viol['utility_cost'])]}."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All cable-connected households have at least 2 vehicles."""
    cable = df[df["internet_type"] == "cable"]
    condition = cable["vehicle_count"] >= 2
    truth = condition.all()
    if truth:
        expl = "All cable-connected households have at least 2 vehicles."
    else:
        viol = cable[~condition]
        expl = f"{len(viol)} cable-connected households violate the rule (vehicle_count): {list(viol['vehicle_count'])}."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All households with size 1 have monthly income ≤ 5.3 k."""
    size1 = df[df["household_size"] == 1]
    condition = size1["monthly_income_k"] <= 5.3
    truth = condition.all()
    if truth:
        expl = "All households with size 1 have income ≤ 5.3 k."
    else:
        viol = size1[~condition]
        expl = f"{len(viol)} size-1 households violate the rule (income): {list(viol['monthly_income_k'])}."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most households have utility cost greater than 100 k."""
    condition = df["utility_cost"] > 100.0
    count_true = condition.sum()
    total = len(df)
    truth = count_true > total / 2
    if truth:
        expl = f"More than half ({count_true}/{total}) of households have utility cost > 100 k."
    else:
        expl = f"Less than or equal to half ({count_true}/{total}) of households have utility cost > 100 k."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_54.csv")

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
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()