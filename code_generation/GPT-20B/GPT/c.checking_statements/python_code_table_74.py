import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all households in the rural region, the internet type is not satellite."""
    rural = df[df["region"] == "rural"]
    condition = rural["internet_type"]!= "satellite"
    truth = condition.all()
    if truth:
        expl = f"All {len(rural)} rural households have internet type not satellite."
    else:
        viol = rural[~condition]
        expl = f"{len(viol)} rural households violate the rule (internet types: {', '.join(map(str, viol['internet_type'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all households in the urban region, the internet type is not DSL."""
    urban = df[df["region"] == "urban"]
    condition = urban["internet_type"]!= "dsl"
    truth = condition.all()
    if truth:
        expl = f"All {len(urban)} urban households have internet type not DSL."
    else:
        viol = urban[~condition]
        expl = f"{len(viol)} urban households violate the rule (internet types: {', '.join(map(str, viol['internet_type'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all households with a rent of $0.8k, the utility cost is at least $143.4k."""
    rent_08 = df[df["rent_k"] == 0.8]
    if rent_08.empty:
        truth = True
        expl = "No households with rent 0.8k, so the statement holds vacuously."
    else:
        condition = rent_08["utility_cost"] >= 143.4
        truth = condition.all()
        if truth:
            expl = f"All {len(rent_08)} households with rent 0.8k have utility cost >= 143.4k."
        else:
            viol = rent_08[~condition]
            expl = f"{len(viol)} households with rent 0.8k violate the rule (utility costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with internet type fiber have rent of $2.5k or less."""
    fiber = df[df["internet_type"] == "fiber"]
    condition = fiber["rent_k"] <= 2.5
    truth = condition.all()
    if truth:
        expl = f"All {len(fiber)} fiber households have rent <= 2.5k."
    else:
        viol = fiber[~condition]
        expl = f"{len(viol)} fiber households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all households with a household size of 1, monthly income is at least $6.4k."""
    size1 = df[df["household_size"] == 1]
    condition = size1["monthly_income_k"] >= 6.4
    truth = condition.all()
    if truth:
        expl = f"All {len(size1)} households with size 1 have monthly income >= 6.4k."
    else:
        viol = size1[~condition]
        expl = f"{len(viol)} households with size 1 violate the rule (monthly incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with vehicle count of 0 have rent of at least $1.4k."""
    zero_veh = df[df["vehicle_count"] == 0]
    condition = zero_veh["rent_k"] >= 1.4
    truth = condition.all()
    if truth:
        expl = f"All {len(zero_veh)} households with 0 vehicles have rent >= 1.4k."
    else:
        viol = zero_veh[~condition]
        expl = f"{len(viol)} households with 0 vehicles violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all households with a household size of 5 or more, monthly income does not exceed $10.2k."""
    size5plus = df[df["household_size"] >= 5]
    condition = size5plus["monthly_income_k"] <= 10.2
    truth = condition.all()
    if truth:
        expl = f"All {len(size5plus)} households with size >=5 have monthly income <= 10.2k."
    else:
        viol = size5plus[~condition]
        expl = f"{len(viol)} households with size >=5 violate the rule (monthly incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_74.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()