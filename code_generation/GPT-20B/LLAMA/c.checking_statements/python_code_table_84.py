import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with a monthly income greater than 9k have a household size greater than 1."""
    subset = df[df["monthly_income_k"] > 9]
    if subset.empty:
        return True, "No households with income >9k, vacuously true."
    condition = subset["household_size"] > 1
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with income >9k have size >1."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. If a household is in a rural region, then their monthly income is less than 11k."""
    subset = df[df["region"] == "rural"]
    if subset.empty:
        return True, "No rural households, vacuously true."
    condition = subset["monthly_income_k"] < 11
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} rural households have income <11k."
    viol = subset[~condition]
    return False, f"{len(viol)} rural households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in a suburban region with a monthly income greater than 9k and a household size of 4."""
    matches = df[(df["region"] == "suburban") & (df["monthly_income_k"] > 9) & (df["household_size"] == 4)]
    if not matches.empty:
        ids = matches["household_id"].tolist()
        return True, f"Found {len(matches)} matching household(s): {', '.join(ids)}."
    return False, "No matching household found."

def stmt_4(df: pd.DataFrame):
    """4. All households with a rent greater than 2.5k have a monthly income greater than 5k."""
    subset = df[df["rent_k"] > 2.5]
    if subset.empty:
        return True, "No households with rent >2.5k, vacuously true."
    condition = subset["monthly_income_k"] > 5
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with rent >2.5k have income >5k."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count of 2, then their monthly income is greater than 5k."""
    subset = df[df["vehicle_count"] == 2]
    if subset.empty:
        return True, "No households with vehicle count 2, vacuously true."
    condition = subset["monthly_income_k"] > 5
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with 2 vehicles have income >5k."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."

def stmt_6(df: pd.DataFrame):
    """6. Most households have a utility cost greater than 150."""
    proportion = (df["utility_cost"] > 150).mean()
    truth = proportion > 0.5
    pct = proportion * 100
    if truth:
        return True, f"{pct:.1f}% of households have utility cost >150."
    return False, f"{pct:.1f}% of households have utility cost >150, which is not a majority."

def stmt_7(df: pd.DataFrame):
    """7. All households with a household size of 1 have a monthly income greater than 5k."""
    subset = df[df["household_size"] == 1]
    if subset.empty:
        return True, "No households with size 1, vacuously true."
    condition = subset["monthly_income_k"] > 5
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with size 1 have income >5k."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."

def stmt_8(df: pd.DataFrame):
    """8. If a household has an internet type of fiber, then their monthly income is greater than 4k."""
    subset = df[df["internet_type"] == "fiber"]
    if subset.empty:
        return True, "No fiber households, vacuously true."
    condition = subset["monthly_income_k"] > 4
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} fiber households have income >4k."
    viol = subset[~condition]
    return False, f"{len(viol)} fiber households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in an urban region with a monthly income greater than 6k and a household size of 1."""
    matches = df[(df["region"] == "urban") & (df["monthly_income_k"] > 6) & (df["household_size"] == 1)]
    if not matches.empty:
        ids = matches["household_id"].tolist()
        return True, f"Found {len(matches)} matching household(s): {', '.join(ids)}."
    return False, "No matching household found."

def stmt_10(df: pd.DataFrame):
    """10. All households with a monthly income less than 6k have a household size less than 4."""
    subset = df[df["monthly_income_k"] < 6]
    if subset.empty:
        return True, "No households with income <6k, vacuously true."
    condition = subset["household_size"] < 4
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with income <6k have size <4."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."

def stmt_11(df: pd.DataFrame):
    """11. If a household is in a suburban region, then their rent is greater than 1k."""
    subset = df[df["region"] == "suburban"]
    if subset.empty:
        return True, "No suburban households, vacuously true."
    condition = subset["rent_k"] > 1
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} suburban households have rent >1k."
    viol = subset[~condition]
    return False, f"{len(viol)} suburban households violate the rule (rents: {', '.join(map(str, viol['rent_k'].tolist()))})."

def stmt_12(df: pd.DataFrame):
    """12. Most households have a monthly income less than 10k."""
    proportion = (df["monthly_income_k"] < 10).mean()
    truth = proportion > 0.5
    pct = proportion * 100
    if truth:
        return True, f"{pct:.1f}% of households have income <10k."
    return False, f"{pct:.1f}% of households have income <10k, which is not a majority."

def stmt_13(df: pd.DataFrame):
    """13. All households with a vehicle count of 0 have a household size of 2 or 5."""
    subset = df[df["vehicle_count"] == 0]
    if subset.empty:
        return True, "No households with vehicle count 0, vacuously true."
    condition = subset["household_size"].isin([2,5])
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with 0 vehicles have size 2 or 5."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."

def stmt_14(df: pd.DataFrame):
    """14. If a household has a utility cost less than 200, then their household size is less than 4."""
    subset = df[df["utility_cost"] < 200]
    if subset.empty:
        return True, "No households with utility cost <200, vacuously true."
    condition = subset["household_size"] < 4
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with utility cost <200 have size <4."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household in a rural region with a monthly income greater than 8k and a household size of 2."""
    matches = df[(df["region"] == "rural") & (df["monthly_income_k"] > 8) & (df["household_size"] == 2)]
    if not matches.empty:
        ids = matches["household_id"].tolist()
        return True, f"Found {len(matches)} matching household(s): {', '.join(ids)}."
    return False, "No matching household found."

def stmt_16(df: pd.DataFrame):
    """16. All households with an internet type of satellite have a household size of 1 or 4."""
    subset = df[df["internet_type"] == "satellite"]
    if subset.empty:
        return True, "No satellite households, vacuously true."
    condition = subset["household_size"].isin([1,4])
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} satellite households have size 1 or 4."
    viol = subset[~condition]
    return False, f"{len(viol)} satellite households violate the rule (sizes: {', '.join(map(str, viol['household_size'].tolist()))})."

def stmt_17(df: pd.DataFrame):
    """17. If a household has a rent less than 2k, then their monthly income is less than 7k."""
    subset = df[df["rent_k"] < 2]
    if subset.empty:
        return True, "No households with rent <2k, vacuously true."
    condition = subset["monthly_income_k"] < 7
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} households with rent <2k have income <7k."
    viol = subset[~condition]
    return False, f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_84.csv")

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
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()