import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all households with rent ≤ 1.0 k, utility cost is at least 180 k."""
    subset = df[df["rent_k"] <= 1.0]
    if subset.empty:
        return True, "No households with rent ≤ 1.0 k, so the rule holds vacuously."
    condition = subset["utility_cost"] >= 180.0
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with rent ≤ 1.0 k have utility cost ≥ 180 k."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost']))})."

def stmt_2(df: pd.DataFrame):
    """2. For all households with no vehicles, utility cost is at least 172.2 k."""
    subset = df[df["vehicle_count"] == 0]
    if subset.empty:
        return True, "No households with zero vehicles, so the rule holds vacuously."
    condition = subset["utility_cost"] >= 172.2
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with no vehicles have utility cost ≥ 172.2 k."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost']))})."

def stmt_3(df: pd.DataFrame):
    """3. For all households with size ≥ 6, rent is at most 1.9 k."""
    subset = df[df["household_size"] >= 6]
    if subset.empty:
        return True, "No households with size ≥ 6, so the rule holds vacuously."
    condition = subset["rent_k"] <= 1.9
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with size ≥ 6 have rent ≤ 1.9 k."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (rents: {', '.join(map(str, viol['rent_k']))})."

def stmt_4(df: pd.DataFrame):
    """4. All urban households have internet type either fiber or satellite."""
    subset = df[df["region"] == "urban"]
    if subset.empty:
        return True, "No urban households, so the rule holds vacuously."
    condition = subset["internet_type"].isin(["fiber", "satellite"])
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} urban households use fiber or satellite internet."
    viol = subset[~condition]
    return False, f"{len(viol)} urban households violate the rule (internet types: {', '.join(map(str, viol['internet_type']))})."

def stmt_5(df: pd.DataFrame):
    """5. All rural households have rent of at least 1.5 k."""
    subset = df[df["region"] == "rural"]
    if subset.empty:
        return True, "No rural households, so the rule holds vacuously."
    condition = subset["rent_k"] >= 1.5
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} rural households have rent ≥ 1.5 k."
    viol = subset[~condition]
    return False, f"{len(viol)} rural households violate the rule (rents: {', '.join(map(str, viol['rent_k']))})."

def stmt_6(df: pd.DataFrame):
    """6. All households with monthly income > 10 k have utility cost greater than 115 k."""
    subset = df[df["monthly_income_k"] > 10.0]
    if subset.empty:
        return True, "No households with monthly income > 10 k, so the rule holds vacuously."
    condition = subset["utility_cost"] > 115.0
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with income > 10 k have utility cost > 115 k."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (utility costs: {', '.join(map(str, viol['utility_cost']))})."

def stmt_7(df: pd.DataFrame):
    """7. All cable‑connected households have at least 2 vehicles."""
    subset = df[df["internet_type"] == "cable"]
    if subset.empty:
        return True, "No cable‑connected households, so the rule holds vacuously."
    condition = subset["vehicle_count"] >= 2
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} cable‑connected households have at least 2 vehicles."
    viol = subset[~condition]
    return False, f"{len(viol)} cable‑connected households violate the rule (vehicle counts: {', '.join(map(str, viol['vehicle_count']))})."

def stmt_8(df: pd.DataFrame):
    """8. All households with size 1 have monthly income ≤ 5.3 k."""
    subset = df[df["household_size"] == 1]
    if subset.empty:
        return True, "No households with size 1, so the rule holds vacuously."
    condition = subset["monthly_income_k"] <= 5.3
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with size 1 have monthly income ≤ 5.3 k."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (monthly incomes: {', '.join(map(str, viol['monthly_income_k']))})."

def stmt_9(df: pd.DataFrame):
    """9. Most households have utility cost greater than 100 k."""
    total = len(df)
    if total == 0:
        return True, "No households in the dataset, so the rule holds vacuously."
    count = (df["utility_cost"] > 100.0).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        return True, f"{count}/{total} households ({proportion:.2%}) have utility cost > 100 k."
    else:
        return False, f"Only {count}/{total} households ({proportion:.2%}) have utility cost > 100 k, which is not a majority."

def main():
    df = pd.read_csv("../inference_generation/tables/table_54.csv")

    # Convert numeric columns safely
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