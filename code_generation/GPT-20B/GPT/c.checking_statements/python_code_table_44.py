import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with monthly income greater than $8 k have at least one vehicle."""
    subset = df[df["monthly_income_k"] > 8]
    condition = subset["vehicle_count"] >= 1
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income > 8k have at least one vehicle."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (vehicle counts: {', '.join(map(str, viol['vehicle_count'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All urban households have rent of at least $1.2 k."""
    subset = df[df["region"] == "urban"]
    condition = subset["rent_k"] >= 1.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} urban households have rent >= 1.2k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} urban households violate the rule (rent values: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All households with a household size of 6 have rent of at least $2.0 k."""
    subset = df[df["household_size"] == 6]
    condition = subset["rent_k"] >= 2.0
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with size 6 have rent >= 2.0k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (rent values: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with utility cost above $200 k have rent of at most $2.0 k."""
    subset = df[df["utility_cost"] > 200]
    condition = subset["rent_k"] <= 2.0
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with utility cost > 200k have rent <= 2.0k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (rent values: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All satellite‑internet households have utility cost of at least $134.7 k."""
    subset = df[df["internet_type"] == "satellite"]
    condition = subset["utility_cost"] >= 134.7
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} satellite‑internet households have utility cost >= 134.7k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with vehicle count of 3 have rent of at least $1.2 k."""
    subset = df[df["vehicle_count"] == 3]
    condition = subset["rent_k"] >= 1.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with 3 vehicles have rent >= 1.2k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (rent values: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with rent of $2.5 k or more have utility cost of at most $150.9 k."""
    subset = df[df["rent_k"] >= 2.5]
    condition = subset["utility_cost"] <= 150.9
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with rent >= 2.5k have utility cost <= 150.9k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists a rural household with zero vehicles that uses fiber internet."""
    condition = (df["region"] == "rural") & (df["vehicle_count"] == 0) & (df["internet_type"] == "fiber")
    truth = condition.any()
    if truth:
        expl = "Such a household exists."
    else:
        expl = "No such household found."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_44.csv")

    # Convert numeric columns
    numeric_cols = ["monthly_income_k", "rent_k", "utility_cost", "household_size", "vehicle_count"]
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()