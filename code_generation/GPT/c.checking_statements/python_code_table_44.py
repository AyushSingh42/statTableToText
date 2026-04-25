import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with monthly income greater than $8 k have at least one vehicle."""
    condition = (df["monthly_income_k"] > 8) & (df["vehicle_count"] < 1)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "No households with income >$8k lack a vehicle."
    else:
        expl = f"{len(violations)} households with income >$8k lack a vehicle."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All urban households have rent of at least $1.2 k."""
    condition = (df["region"] == "urban") & (df["rent_k"] < 1.2)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All urban households have rent >= $1.2k."
    else:
        expl = f"{len(violations)} urban households have rent < $1.2k."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All households with a household size of 6 have rent of at least $2.0 k."""
    condition = (df["household_size"] == 6) & (df["rent_k"] < 2.0)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All households with size 6 have rent >= $2.0k."
    else:
        expl = f"{len(violations)} households with size 6 have rent < $2.0k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with utility cost above $200 k have rent of at most $2.0 k."""
    condition = (df["utility_cost"] > 200) & (df["rent_k"] > 2.0)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All households with utility cost >$200k have rent <= $2.0k."
    else:
        expl = f"{len(violations)} households with utility cost >$200k have rent > $2.0k."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All satellite‑internet households have utility cost of at least $134.7 k."""
    condition = (df["internet_type"] == "satellite") & (df["utility_cost"] < 134.7)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All satellite-internet households have utility cost >= $134.7k."
    else:
        expl = f"{len(violations)} satellite-internet households have utility cost < $134.7k."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with vehicle count of 3 have rent of at least $1.2 k."""
    condition = (df["vehicle_count"] == 3) & (df["rent_k"] < 1.2)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All households with 3 vehicles have rent >= $1.2k."
    else:
        expl = f"{len(violations)} households with 3 vehicles have rent < $1.2k."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with rent of $2.5 k or more have utility cost of at most $150.9 k."""
    condition = (df["rent_k"] >= 2.5) & (df["utility_cost"] > 150.9)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All households with rent >= $2.5k have utility cost <= $150.9k."
    else:
        expl = f"{len(violations)} households with rent >= $2.5k have utility cost > $150.9k."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists a rural household with zero vehicles that uses fiber internet."""
    condition = (df["region"] == "rural") & (df["vehicle_count"] == 0) & (df["internet_type"] == "fiber")
    matches = df[condition]
    truth = len(matches) > 0
    if truth:
        expl = f"There is 1 rural household with 0 vehicles using fiber internet."
    else:
        expl = "No rural household with 0 vehicles uses fiber internet."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_44.csv")

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