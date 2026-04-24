import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # Convert numeric columns that may be stored as strings to proper numeric types
    numeric_cols = ["household_size", "monthly_income_k", "rent_k", "utility_cost", "vehicle_count"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    # Standardise region and internet_type strings to lower case for reliable comparison
    df["region"] = df["region"].str.lower()
    df["internet_type"] = df["internet_type"].str.lower()
    return df

def stmt_1(df: pd.DataFrame):
    """1. For all urban households, the internet type is either fiber or cable."""
    urban = df[df["region"] == "urban"]
    allowed = {"fiber", "cable"}
    condition = urban["internet_type"].isin(allowed)
    truth = condition.all()
    if truth:
        expl = f"All {len(urban)} urban households have internet type fiber or cable."
    else:
        viol = urban[~condition]
        expl = f"{len(viol)} urban households violate the rule (internet types: {', '.join(viol['internet_type'].unique())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all rural households, the internet type is either DSL or satellite."""
    rural = df[df["region"] == "rural"]
    allowed = {"dsl", "satellite"}
    condition = rural["internet_type"].isin(allowed)
    truth = condition.all()
    if truth:
        expl = f"All {len(rural)} rural households have internet type DSL or satellite."
    else:
        viol = rural[~condition]
        expl = f"{len(viol)} rural households violate the rule (internet types: {', '.join(viol['internet_type'].unique())})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a household has zero vehicles, it is located in an urban region."""
    zero_veh = df[df["vehicle_count"] == 0]
    condition = zero_veh["region"] == "urban"
    truth = condition.all()
    if truth:
        expl = f"All {len(zero_veh)} households with zero vehicles are urban."
    else:
        viol = zero_veh[~condition]
        expl = f"{len(viol)} households with zero vehicles are not urban (regions: {', '.join(viol['region'].unique())})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a household's internet type is satellite, then it is in a rural region."""
    satellite = df[df["internet_type"] == "satellite"]
    condition = satellite["region"] == "rural"
    truth = condition.all()
    if truth:
        expl = f"All {len(satellite)} satellite‑internet households are rural."
    else:
        viol = satellite[~condition]
        expl = f"{len(viol)} satellite‑internet households are not rural (regions: {', '.join(viol['region'].unique())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If household size is at least 5, then utility cost exceeds $150."""
    large = df[df["household_size"] >= 5]
    condition = large["utility_cost"] > 150
    truth = condition.all()
    if truth:
        expl = f"All {len(large)} households with size ≥5 have utility cost > $150."
    else:
        viol = large[~condition]
        expl = f"{len(viol)} households with size ≥5 have utility cost ≤ $150 (costs: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If rent cost is at most $1.0 k, then the household is in a rural region."""
    cheap = df[df["rent_k"] <= 1.0]
    condition = cheap["region"] == "rural"
    truth = condition.all()
    if truth:
        expl = f"All {len(cheap)} households with rent ≤ $1.0k are rural."
    else:
        viol = cheap[~condition]
        expl = f"{len(viol)} households with rent ≤ $1.0k are not rural (regions: {', '.join(viol['region'].unique())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most households have an internet type of fiber or cable."""
    allowed = {"fiber", "cable"}
    count_allowed = df["internet_type"].isin(allowed).sum()
    total = len(df)
    truth = count_allowed > total / 2
    expl = f"{count_allowed} out of {total} households ({count_allowed/total:.1%}) have fiber or cable."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most households own at least one vehicle."""
    count_one_plus = (df["vehicle_count"] >= 1).sum()
    total = len(df)
    truth = count_one_plus > total / 2
    expl = f"{count_one_plus} out of {total} households ({count_one_plus/total:.1%}) own ≥1 vehicle."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a household's monthly income exceeds $8 k, its internet type is fiber or cable."""
    rich = df[df["monthly_income_k"] > 8]
    allowed = {"fiber", "cable"}
    condition = rich["internet_type"].isin(allowed)
    truth = condition.all()
    if truth:
        expl = f"All {len(rich)} households with income > $8k have fiber or cable internet."
    else:
        viol = rich[~condition]
        expl = f"{len(viol)} high‑income households violate the rule (internet types: {', '.join(viol['internet_type'].unique())})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a household has three or more vehicles, it is located in a suburban or rural region."""
    many_veh = df[df["vehicle_count"] >= 3]
    allowed_regions = {"suburban", "rural"}
    condition = many_veh["region"].isin(allowed_regions)
    truth = condition.all()
    if truth:
        expl = f"All {len(many_veh)} households with ≥3 vehicles are in suburban or rural regions."
    else:
        viol = many_veh[~condition]
        expl = f"{len(viol)} households with ≥3 vehicles are not in suburban/rural (regions: {', '.join(viol['region'].unique())})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_5.csv")
    df = clean_dataframe(df)

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()