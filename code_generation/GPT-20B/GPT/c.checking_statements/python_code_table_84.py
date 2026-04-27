import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with three vehicles have a monthly income of at least $8.3 k."""
    mask = df["vehicle_count"] == 3
    condition = df.loc[mask, "monthly_income_k"] >= 8.3
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} households with 3 vehicles have income ≥ 8.3 k."
    else:
        viol = df.loc[mask & ~condition]
        incomes = viol["monthly_income_k"].tolist()
        expl = f"{len(viol)} households with 3 vehicles violate the rule (incomes: {', '.join(map(str, incomes))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Every household that uses fiber internet has a utility cost no greater than $183.2."""
    mask = df["internet_type"] == "fiber"
    condition = df.loc[mask, "utility_cost"] <= 183.2
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} fiber households have utility cost ≤ 183.2."
    else:
        viol = df.loc[mask & ~condition]
        costs = viol["utility_cost"].tolist()
        expl = f"{len(viol)} fiber households violate the rule (utility costs: {', '.join(map(str, costs))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every rural household has a monthly income of at least $3.2 k."""
    mask = df["region"] == "rural"
    condition = df.loc[mask, "monthly_income_k"] >= 3.2
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} rural households have income ≥ 3.2 k."
    else:
        viol = df.loc[mask & ~condition]
        incomes = viol["monthly_income_k"].tolist()
        expl = f"{len(viol)} rural households violate the rule (incomes: {', '.join(map(str, incomes))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All suburban households have at most two vehicles."""
    mask = df["region"] == "suburban"
    condition = df.loc[mask, "vehicle_count"] <= 2
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} suburban households have ≤ 2 vehicles."
    else:
        viol = df.loc[mask & ~condition]
        counts = viol["vehicle_count"].tolist()
        expl = f"{len(viol)} suburban households violate the rule (vehicle counts: {', '.join(map(str, counts))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Every urban household pays rent of at least $0.8 k."""
    mask = df["region"] == "urban"
    condition = df.loc[mask, "rent_k"] >= 0.8
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} urban households have rent ≥ 0.8 k."
    else:
        viol = df.loc[mask & ~condition]
        rents = viol["rent_k"].tolist()
        expl = f"{len(viol)} urban households violate the rule (rents: {', '.join(map(str, rents))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All one‑person households have a monthly income between $5.4 k and $6.9 k."""
    mask = df["household_size"] == 1
    condition = df.loc[mask, "monthly_income_k"].between(5.4, 6.9, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} one‑person households have income between 5.4 k and 6.9 k."
    else:
        viol = df.loc[mask & ~condition]
        incomes = viol["monthly_income_k"].tolist()
        expl = f"{len(viol)} one‑person households violate the rule (incomes: {', '.join(map(str, incomes))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every household with no vehicles pays rent of at most $2.4 k."""
    mask = df["vehicle_count"] == 0
    condition = df.loc[mask, "rent_k"] <= 2.4
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} vehicle‑free households have rent ≤ 2.4 k."
    else:
        viol = df.loc[mask & ~condition]
        rents = viol["rent_k"].tolist()
        expl = f"{len(viol)} vehicle‑free households violate the rule (rents: {', '.join(map(str, rents))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All DSL households have a monthly income of at least $9.7 k."""
    mask = df["internet_type"] == "dsl"
    condition = df.loc[mask, "monthly_income_k"] >= 9.7
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} DSL households have income ≥ 9.7 k."
    else:
        viol = df.loc[mask & ~condition]
        incomes = viol["monthly_income_k"].tolist()
        expl = f"{len(viol)} DSL households violate the rule (incomes: {', '.join(map(str, incomes))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Any household with a utility cost exceeding $200 k pays rent of at least $2.8 k."""
    mask = df["utility_cost"] > 200
    condition = df.loc[mask, "rent_k"] >= 2.8
    truth = condition.all()
    if truth:
        expl = f"All {mask.sum()} households with utility cost > 200 have rent ≥ 2.8 k."
    else:
        viol = df.loc[mask & ~condition]
        rents = viol["rent_k"].tolist()
        expl = f"{len(viol)} households with utility cost > 200 violate the rule (rents: {', '.join(map(str, rents))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_84.csv")

    # Convert numeric columns safely
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()