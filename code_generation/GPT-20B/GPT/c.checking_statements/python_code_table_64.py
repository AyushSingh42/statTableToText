import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all urban households with household size 1, monthly income is between $4.4k and $9.2k."""
    subset = df[(df["region"] == "urban") & (df["household_size"] == 1)]
    if subset.empty:
        return True, "No urban households with size 1 to evaluate."
    condition = subset["monthly_income_k"].between(4.4, 9.2, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} urban households with size 1 have income between 4.4k and 9.2k."
    else:
        viol = subset[~condition]
        viol_ids = viol["household_id"].tolist()
        viol_incomes = viol["monthly_income_k"].tolist()
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(map(str, viol_ids))}, incomes: {', '.join(map(str, viol_incomes))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All rural households have rent of $2.9k or less."""
    subset = df[df["region"] == "rural"]
    if subset.empty:
        return True, "No rural households to evaluate."
    condition = subset["rent_k"] <= 2.9
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} rural households have rent <= 2.9k."
    else:
        viol = subset[~condition]
        viol_ids = viol["household_id"].tolist()
        viol_rents = viol["rent_k"].tolist()
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(map(str, viol_ids))}, rents: {', '.join(map(str, viol_rents))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All households with zero vehicles have utility cost of at least $84.8."""
    subset = df[df["vehicle_count"] == 0]
    if subset.empty:
        return True, "No households with zero vehicles to evaluate."
    condition = subset["utility_cost"] >= 84.8
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with zero vehicles have utility cost >= 84.8."
    else:
        viol = subset[~condition]
        viol_ids = viol["household_id"].tolist()
        viol_utils = viol["utility_cost"].tolist()
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(map(str, viol_ids))}, utilities: {', '.join(map(str, viol_utils))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All fiber internet households have rent of $2.4k or less."""
    subset = df[df["internet_type"] == "fiber"]
    if subset.empty:
        return True, "No fiber internet households to evaluate."
    condition = subset["rent_k"] <= 2.4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} fiber internet households have rent <= 2.4k."
    else:
        viol = subset[~condition]
        viol_ids = viol["household_id"].tolist()
        viol_rents = viol["rent_k"].tolist()
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(map(str, viol_ids))}, rents: {', '.join(map(str, viol_rents))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most households have utility cost greater than $100."""
    if df.empty:
        return True, "No households to evaluate."
    proportion = (df["utility_cost"] > 100).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of households have utility cost > 100."
    else:
        expl = f"Only {proportion*100:.1f}% of households have utility cost > 100."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with six or more members have rent of $2.4k or less."""
    subset = df[df["household_size"] >= 6]
    if subset.empty:
        return True, "No households with six or more members to evaluate."
    condition = subset["rent_k"] <= 2.4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} households with 6+ members have rent <= 2.4k."
    else:
        viol = subset[~condition]
        viol_ids = viol["household_id"].tolist()
        viol_rents = viol["rent_k"].tolist()
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(map(str, viol_ids))}, rents: {', '.join(map(str, viol_rents))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All satellite internet households have utility cost of at least $99.6."""
    subset = df[df["internet_type"] == "satellite"]
    if subset.empty:
        return True, "No satellite internet households to evaluate."
    condition = subset["utility_cost"] >= 99.6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} satellite internet households have utility cost >= 99.6."
    else:
        viol = subset[~condition]
        viol_ids = viol["household_id"].tolist()
        viol_utils = viol["utility_cost"].tolist()
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(map(str, viol_ids))}, utilities: {', '.join(map(str, viol_utils))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All urban households have at most three vehicles."""
    subset = df[df["region"] == "urban"]
    if subset.empty:
        return True, "No urban households to evaluate."
    condition = subset["vehicle_count"] <= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} urban households have <= 3 vehicles."
    else:
        viol = subset[~condition]
        viol_ids = viol["household_id"].tolist()
        viol_vehicles = viol["vehicle_count"].tolist()
        expl = f"{len(viol)} households violate the rule (IDs: {', '.join(map(str, viol_ids))}, vehicles: {', '.join(map(str, viol_vehicles))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_64.csv")

    # Convert numeric columns
    numeric_cols = ["household_size", "monthly_income_k", "rent_k", "utility_cost", "vehicle_count"]
    for col in numeric_cols:
        if col in df.columns:
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