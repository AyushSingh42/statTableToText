import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All rural households have utility costs of at least $88.0k."""
    rural = df[df["region"] == "rural"]
    condition = rural["utility_cost"] >= 88.0
    truth = condition.all()
    if truth:
        expl = f"All {len(rural)} rural households have utility costs >= $88.0k."
    else:
        viol = rural[~condition]
        expl = f"{len(viol)} rural households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All urban households using satellite internet have utility costs of at least $166.1k."""
    urban_sat = df[(df["region"] == "urban") & (df["internet_type"] == "satellite")]
    condition = urban_sat["utility_cost"] >= 166.1
    truth = condition.all()
    if truth:
        expl = f"All {len(urban_sat)} urban households with satellite internet have utility costs >= $166.1k."
    else:
        viol = urban_sat[~condition]
        expl = f"{len(viol)} urban households with satellite internet violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All households with no vehicles have monthly income of at least $4.5k."""
    no_vehicle = df[df["vehicle_count"] == 0]
    condition = no_vehicle["monthly_income_k"] >= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(no_vehicle)} households with no vehicles have monthly income >= $4.5k."
    else:
        viol = no_vehicle[~condition]
        expl = f"{len(viol)} households with no vehicles violate the rule (monthly incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with six members have monthly income of at most $10.3k."""
    six_members = df[df["household_size"] == 6]
    condition = six_members["monthly_income_k"] <= 10.3
    truth = condition.all()
    if truth:
        expl = f"All {len(six_members)} households with six members have monthly income <= $10.3k."
    else:
        viol = six_members[~condition]
        expl = f"{len(viol)} households with six members violate the rule (monthly incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All suburban households with DSL internet have monthly income of at least $3.4k."""
    suburban_dsl = df[(df["region"] == "suburban") & (df["internet_type"] == "dsl")]
    condition = suburban_dsl["monthly_income_k"] >= 3.4
    truth = condition.all()
    if truth:
        expl = f"All {len(suburban_dsl)} suburban households with DSL internet have monthly income >= $3.4k."
    else:
        viol = suburban_dsl[~condition]
        expl = f"{len(viol)} suburban households with DSL internet violate the rule (monthly incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All urban households pay at least $1.2k in rent."""
    urban = df[df["region"] == "urban"]
    condition = urban["rent_k"] >= 1.2
    truth = condition.all()
    if truth:
        expl = f"All {len(urban)} urban households pay rent >= $1.2k."
    else:
        viol = urban[~condition]
        expl = f"{len(viol)} urban households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with monthly income of at least $11k have utility costs of at most $88.0k."""
    high_income = df[df["monthly_income_k"] >= 11.0]
    condition = high_income["utility_cost"] <= 88.0
    truth = condition.all()
    if truth:
        expl = f"All {len(high_income)} households with monthly income >= $11k have utility costs <= $88.0k."
    else:
        viol = high_income[~condition]
        expl = f"{len(viol)} households with monthly income >= $11k violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
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
        (7, stmt_7)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()