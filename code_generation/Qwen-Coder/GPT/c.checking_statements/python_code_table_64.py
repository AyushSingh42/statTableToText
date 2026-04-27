import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all urban households with household size 1, monthly income is between $4.4k and $9.2k."""
    urban_size1 = df[(df["region"] == "urban") & (df["household_size"] == 1)]
    condition = urban_size1["monthly_income_k"].between(4.4, 9.2, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(urban_size1)} urban households with size 1 have income between $4.4k and $9.2k."
    else:
        viol = urban_size1[~condition]
        expl = f"{len(viol)} urban households with size 1 violate the income range (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All rural households have rent of $2.9k or less."""
    rural = df[df["region"] == "rural"]
    condition = rural["rent_k"] <= 2.9
    truth = condition.all()
    if truth:
        expl = f"All {len(rural)} rural households have rent ≤ $2.9k."
    else:
        viol = rural[~condition]
        expl = f"{len(viol)} rural households have rent > $2.9k (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All households with zero vehicles have utility cost of at least $84.8."""
    no_vehicle = df[df["vehicle_count"] == 0]
    condition = no_vehicle["utility_cost"] >= 84.8
    truth = condition.all()
    if truth:
        expl = f"All {len(no_vehicle)} households with zero vehicles have utility cost ≥ $84.8."
    else:
        viol = no_vehicle[~condition]
        expl = f"{len(viol)} households with zero vehicles have utility cost < $84.8 (costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All fiber internet households have rent of $2.4k or less."""
    fiber = df[df["internet_type"] == "fiber"]
    condition = fiber["rent_k"] <= 2.4
    truth = condition.all()
    if truth:
        expl = f"All {len(fiber)} fiber internet households have rent ≤ $2.4k."
    else:
        viol = fiber[~condition]
        expl = f"{len(viol)} fiber internet households have rent > $2.4k (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most households have utility cost greater than $100."""
    condition = df["utility_cost"] > 100
    count_gt = condition.sum()
    total = len(df)
    truth = count_gt > total / 2
    if truth:
        expl = f"{count_gt} out of {total} households have utility cost > $100 (more than half)."
    else:
        expl = f"{count_gt} out of {total} households have utility cost > $100 (not more than half)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with six or more members have rent of $2.4k or less."""
    large_households = df[df["household_size"] >= 6]
    condition = large_households["rent_k"] <= 2.4
    truth = condition.all()
    if truth:
        expl = f"All {len(large_households)} households with 6+ members have rent ≤ $2.4k."
    else:
        viol = large_households[~condition]
        expl = f"{len(viol)} households with 6+ members have rent > $2.4k (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All satellite internet households have utility cost of at least $99.6."""
    satellite = df[df["internet_type"] == "satellite"]
    condition = satellite["utility_cost"] >= 99.6
    truth = condition.all()
    if truth:
        expl = f"All {len(satellite)} satellite internet households have utility cost ≥ $99.6."
    else:
        viol = satellite[~condition]
        expl = f"{len(viol)} satellite internet households have utility cost < $99.6 (costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All urban households have at most three vehicles."""
    urban = df[df["region"] == "urban"]
    condition = urban["vehicle_count"] <= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(urban)} urban households have at most 3 vehicles."
    else:
        viol = urban[~condition]
        expl = f"{len(viol)} urban households have more than 3 vehicles (counts: {', '.join(map(str, viol['vehicle_count'].tolist()))})."
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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()