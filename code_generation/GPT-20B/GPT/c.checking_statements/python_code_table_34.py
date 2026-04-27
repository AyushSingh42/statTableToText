import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all households with utility cost greater than 200, vehicle count is at least 1."""
    subset = df[df["utility_cost"] > 200]
    condition = subset["vehicle_count"] >= 1
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with utility cost > 200 have vehicle count >= 1."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (vehicle counts: {', '.join(map(str, viol['vehicle_count'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Every rural household uses either cable or satellite internet."""
    subset = df[df["region"] == "rural"]
    condition = subset["internet_type"].isin(["cable", "satellite"])
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} rural households use cable or satellite internet."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} rural households violate the rule (internet types: {', '.join(map(str, viol['internet_type'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. No urban household uses satellite internet."""
    subset = df[df["region"] == "urban"]
    condition = subset["internet_type"]!= "satellite"
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} urban households do not use satellite internet."
    else:
        viol = subset[subset["internet_type"] == "satellite"]
        expl = f"{len(viol)} urban households violate the rule (satellite internet)."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all households with monthly income of at least $10 k, rent is at least $2.2 k."""
    subset = df[df["monthly_income_k"] >= 10]
    condition = subset["rent_k"] >= 2.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with income >= 10k have rent >= 2.2k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households violate the rule (rent: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Every satellite‑internet household pays rent of at least $2.2 k."""
    subset = df[df["internet_type"] == "satellite"]
    condition = subset["rent_k"] >= 2.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} satellite‑internet households have rent >= 2.2k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} satellite‑internet households violate the rule (rent: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all households with six members, rent does not exceed $2.7 k."""
    subset = df[df["household_size"] == 6]
    condition = subset["rent_k"] <= 2.7
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with 6 members have rent <= 2.7k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} households with 6 members violate the rule (rent: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All cable‑internet households have utility cost no greater than $217.6."""
    subset = df[df["internet_type"] == "cable"]
    condition = subset["utility_cost"] <= 217.6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} cable‑internet households have utility cost <= 217.6."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} cable‑internet households violate the rule (utility cost: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_34.csv")

    # Convert numeric columns where possible
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