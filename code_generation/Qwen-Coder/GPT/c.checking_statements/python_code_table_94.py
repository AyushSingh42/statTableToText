import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All rural households have rent_k ≤ 2.8."""
    rural = df[df["region"] == "rural"]
    condition = rural["rent_k"] <= 2.8
    truth = condition.all()
    if truth:
        expl = f"All {len(rural)} rural households have rent_k ≤ 2.8."
    else:
        viol = rural[~condition]
        expl = f"{len(viol)} rural households violate the rule (rent_k: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All urban households have utility_cost ≥ 131.4."""
    urban = df[df["region"] == "urban"]
    condition = urban["utility_cost"] >= 131.4
    truth = condition.all()
    if truth:
        expl = f"All {len(urban)} urban households have utility_cost ≥ 131.4."
    else:
        viol = urban[~condition]
        expl = f"{len(viol)} urban households violate the rule (utility_cost: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All households with monthly_income_k ≥ 10 have rent_k ≥ 2.1."""
    high_income = df[df["monthly_income_k"] >= 10]
    condition = high_income["rent_k"] >= 2.1
    truth = condition.all()
    if truth:
        expl = f"All {len(high_income)} high-income households have rent_k ≥ 2.1."
    else:
        viol = high_income[~condition]
        expl = f"{len(viol)} high-income households violate the rule (rent_k: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All suburban households have utility_cost ≤ 178.3."""
    suburban = df[df["region"] == "suburban"]
    condition = suburban["utility_cost"] <= 178.3
    truth = condition.all()
    if truth:
        expl = f"All {len(suburban)} suburban households have utility_cost ≤ 178.3."
    else:
        viol = suburban[~condition]
        expl = f"{len(viol)} suburban households violate the rule (utility_cost: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All households with satellite internet have rent_k ≤ 2.4."""
    satellite = df[df["internet_type"] == "satellite"]
    condition = satellite["rent_k"] <= 2.4
    truth = condition.all()
    if truth:
        expl = f"All {len(satellite)} satellite internet households have rent_k ≤ 2.4."
    else:
        viol = satellite[~condition]
        expl = f"{len(viol)} satellite internet households violate the rule (rent_k: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with zero vehicles have monthly_income_k ≥ 4.5."""
    no_vehicle = df[df["vehicle_count"] == 0]
    condition = no_vehicle["monthly_income_k"] >= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(no_vehicle)} zero-vehicle households have monthly_income_k ≥ 4.5."
    else:
        viol = no_vehicle[~condition]
        expl = f"{len(viol)} zero-vehicle households violate the rule (monthly_income_k: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with household_size ≥ 5 have utility_cost ≥ 108.4."""
    large_household = df[df["household_size"] >= 5]
    condition = large_household["utility_cost"] >= 108.4
    truth = condition.all()
    if truth:
        expl = f"All {len(large_household)} large households have utility_cost ≥ 108.4."
    else:
        viol = large_household[~condition]
        expl = f"{len(viol)} large households violate the rule (utility_cost: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most households have vehicle_count ≤ 2."""
    total = len(df)
    condition = df["vehicle_count"] <= 2
    satisfied = condition.sum()
    truth = satisfied > total / 2
    expl = f"{satisfied} out of {total} households have vehicle_count ≤ 2. {'This is more than half.' if truth else 'This is not more than half.'}"
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_94.csv")

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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()