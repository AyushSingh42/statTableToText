import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with three vehicles have a monthly income of at least $8.3 k."""
    condition = df[df["vehicle_count"] == 3]["monthly_income_k"] >= 8.3
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['vehicle_count'] == 3])} households with three vehicles meet the income requirement."
    else:
        viol = df[(df["vehicle_count"] == 3) & (df["monthly_income_k"] < 8.3)]
        expl = f"{len(viol)} households with three vehicles violate the rule (income: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Every household that uses fiber internet has a utility cost no greater than $183.2."""
    condition = df[df["internet_type"] == "fiber"]["utility_cost"] <= 183.2
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['internet_type'] == 'fiber'])} fiber households meet the utility cost limit."
    else:
        viol = df[(df["internet_type"] == "fiber") & (df["utility_cost"] > 183.2)]
        expl = f"{len(viol)} fiber households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every rural household has a monthly income of at least $3.2 k."""
    condition = df[df["region"] == "rural"]["monthly_income_k"] >= 3.2
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['region'] == 'rural'])} rural households meet the income requirement."
    else:
        viol = df[(df["region"] == "rural") & (df["monthly_income_k"] < 3.2)]
        expl = f"{len(viol)} rural households violate the rule (income: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All suburban households have at most two vehicles."""
    condition = df[df["region"] == "suburban"]["vehicle_count"] <= 2
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['region'] =='suburban'])} suburban households have at most two vehicles."
    else:
        viol = df[(df["region"] == "suburban") & (df["vehicle_count"] > 2)]
        expl = f"{len(viol)} suburban households violate the rule (vehicle counts: {', '.join(map(str, viol['vehicle_count'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Every urban household pays rent of at least $0.8 k."""
    condition = df[df["region"] == "urban"]["rent_k"] >= 0.8
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['region'] == 'urban'])} urban households meet the rent requirement."
    else:
        viol = df[(df["region"] == "urban") & (df["rent_k"] < 0.8)]
        expl = f"{len(viol)} urban households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All one-person households have a monthly income between $5.4 k and $6.9 k."""
    condition = (df[df["household_size"] == 1]["monthly_income_k"] >= 5.4) & (df[df["household_size"] == 1]["monthly_income_k"] <= 6.9)
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['household_size'] == 1])} one-person households meet the income range."
    else:
        viol = df[(df["household_size"] == 1) & ((df["monthly_income_k"] < 5.4) | (df["monthly_income_k"] > 6.9))]
        expl = f"{len(viol)} one-person households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every household with no vehicles pays rent of at most $2.4 k."""
    condition = df[df["vehicle_count"] == 0]["rent_k"] <= 2.4
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['vehicle_count'] == 0])} zero-vehicle households meet the rent limit."
    else:
        viol = df[(df["vehicle_count"] == 0) & (df["rent_k"] > 2.4)]
        expl = f"{len(viol)} zero-vehicle households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All DSL households have a monthly income of at least $9.7 k."""
    condition = df[df["internet_type"] == "dsl"]["monthly_income_k"] >= 9.7
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['internet_type'] == 'dsl'])} DSL households meet the income requirement."
    else:
        viol = df[(df["internet_type"] == "dsl") & (df["monthly_income_k"] < 9.7)]
        expl = f"{len(viol)} DSL households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Any household with a utility cost exceeding $200 k pays rent of at least $2.8 k."""
    condition = (df[df["utility_cost"] > 200]["rent_k"] >= 2.8) | (df[df["utility_cost"] <= 200].index.tolist())
    truth = condition.all()
    if truth:
        expl = f"All households with utility cost over $200k meet the rent requirement."
    else:
        viol = df[(df["utility_cost"] > 200) & (df["rent_k"] < 2.8)]
        expl = f"{len(viol)} high-utility households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_84.csv")

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