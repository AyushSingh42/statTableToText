import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all households in the rural region, the internet type is either satellite or cable (no DSL or fiber)."""
    rural = df[df["region"] == "rural"]
    condition = rural["internet_type"].isin(["satellite", "cable"])
    truth = condition.all()
    if truth:
        expl = f"All {len(rural)} rural households have internet type satellite or cable."
    else:
        viol = rural[~condition]
        viol_types = viol["internet_type"].unique()
        expl = f"{len(viol)} rural households violate the rule (internet types: {', '.join(map(str, viol_types))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Every urban household has exactly one vehicle."""
    urban = df[df["region"] == "urban"]
    condition = urban["vehicle_count"] == 1
    truth = condition.all()
    if truth:
        expl = f"All {len(urban)} urban households have exactly one vehicle."
    else:
        viol = urban[~condition]
        expl = f"{len(viol)} urban households violate the rule (vehicle counts: {', '.join(map(str, viol['vehicle_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All households with a household size of 6 have rent of at least $2.2k."""
    size6 = df[df["household_size"] == 6]
    condition = size6["rent_k"] >= 2.2
    truth = condition.all()
    if truth:
        expl = f"All {len(size6)} households of size 6 have rent ≥ 2.2k."
    else:
        viol = size6[~condition]
        rents = viol["rent_k"].tolist()
        expl = f"{len(viol)} households of size 6 violate the rule (rents: {', '.join(map(str, rents))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with zero vehicles have a utility cost no greater than $173k."""
    zero_veh = df[df["vehicle_count"] == 0]
    condition = zero_veh["utility_cost"] <= 173
    truth = condition.all()
    if truth:
        expl = f"All {len(zero_veh)} zero‑vehicle households have utility cost ≤ 173k."
    else:
        viol = zero_veh[~condition]
        costs = viol["utility_cost"].tolist()
        expl = f"{len(viol)} zero‑vehicle households violate the rule (utility costs: {', '.join(map(str, costs))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Every suburban household has a monthly income of at least $5.2k."""
    sub = df[df["region"] == "suburban"]
    condition = sub["monthly_income_k"] >= 5.2
    truth = condition.all()
    if truth:
        expl = f"All {len(sub)} suburban households have monthly income ≥ 5.2k."
    else:
        viol = sub[~condition]
        incomes = viol["monthly_income_k"].tolist()
        expl = f"{len(viol)} suburban households violate the rule (incomes: {', '.join(map(str, incomes))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All rural households have a monthly income of at most $8.6k."""
    rural = df[df["region"] == "rural"]
    condition = rural["monthly_income_k"] <= 8.6
    truth = condition.all()
    if truth:
        expl = f"All {len(rural)} rural households have monthly income ≤ 8.6k."
    else:
        viol = rural[~condition]
        incomes = viol["monthly_income_k"].tolist()
        expl = f"{len(viol)} rural households violate the rule (incomes: {', '.join(map(str, incomes))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For the single household with fiber internet, the vehicle count is exactly one."""
    fiber = df[df["internet_type"] == "fiber"]
    count = len(fiber)
    if count == 1 and fiber.iloc[0]["vehicle_count"] == 1:
        truth = True
        expl = "The single fiber household has exactly one vehicle."
    else:
        truth = False
        if count == 0:
            expl = "No household with fiber internet found."
        elif count > 1:
            expl = f"Multiple ({count}) households with fiber internet found."
        else:
            expl = f"Fiber household has vehicle count {fiber.iloc[0]['vehicle_count']} (expected 1)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All households with monthly income exceeding $10k have a utility cost of at least $173k."""
    high_inc = df[df["monthly_income_k"] > 10]
    condition = high_inc["utility_cost"] >= 173
    truth = condition.all()
    if truth:
        expl = f"All {len(high_inc)} households with income > 10k have utility cost ≥ 173k."
    else:
        viol = high_inc[~condition]
        costs = viol["utility_cost"].tolist()
        expl = f"{len(viol)} high‑income households violate the rule (utility costs: {', '.join(map(str, costs))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All households with two vehicles have a utility cost of at least $132.5k."""
    two_veh = df[df["vehicle_count"] == 2]
    condition = two_veh["utility_cost"] >= 132.5
    truth = condition.all()
    if truth:
        expl = f"All {len(two_veh)} two‑vehicle households have utility cost ≥ 132.5k."
    else:
        viol = two_veh[~condition]
        costs = viol["utility_cost"].tolist()
        expl = f"{len(viol)} two‑vehicle households violate the rule (utility costs: {', '.join(map(str, costs))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_4.csv")

    # Convert numeric columns
    numeric_cols = ["household_size", "monthly_income_k", "rent_k", "utility_cost", "vehicle_count"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

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