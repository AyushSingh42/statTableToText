import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All rural households use satellite internet."""
    rural = df[df["region"] == "rural"]
    if rural.empty:
        return True, "No rural households to check."
    condition = rural["internet_type"] == "satellite"
    truth = condition.all()
    if truth:
        return True, f"All {len(rural)} rural households use satellite internet."
    viol = rural[~condition]
    ids = viol["household_id"].tolist()
    return False, f"{len(viol)} rural households do not use satellite internet (IDs: {', '.join(ids)})."

def stmt_2(df: pd.DataFrame):
    """2. All households with rent less than or equal to $0.8k have fiber internet."""
    low_rent = df[df["rent_k"] <= 0.8]
    if low_rent.empty:
        return True, "No households with rent <= 0.8k to check."
    condition = low_rent["internet_type"] == "fiber"
    truth = condition.all()
    if truth:
        return True, f"All {len(low_rent)} households with rent <= 0.8k have fiber internet."
    viol = low_rent[~condition]
    ids = viol["household_id"].tolist()
    return False, f"{len(viol)} households with rent <= 0.8k do not have fiber internet (IDs: {', '.join(ids)})."

def stmt_3(df: pd.DataFrame):
    """3. All single-person households have an internet type other than fiber."""
    single = df[df["household_size"] == 1]
    if single.empty:
        return True, "No single-person households to check."
    condition = single["internet_type"]!= "fiber"
    truth = condition.all()
    if truth:
        return True, f"All {len(single)} single-person households have non-fiber internet."
    viol = single[~condition]
    ids = viol["household_id"].tolist()
    return False, f"{len(viol)} single-person households have fiber internet (IDs: {', '.join(ids)})."

def stmt_4(df: pd.DataFrame):
    """4. All urban households have a utility cost of at least $84.4."""
    urban = df[df["region"] == "urban"]
    if urban.empty:
        return True, "No urban households to check."
    condition = urban["utility_cost"] >= 84.4
    truth = condition.all()
    if truth:
        return True, f"All {len(urban)} urban households have utility cost >= 84.4."
    viol = urban[~condition]
    ids = viol["household_id"].tolist()
    return False, f"{len(viol)} urban households have utility cost < 84.4 (IDs: {', '.join(ids)})."

def stmt_5(df: pd.DataFrame):
    """5. All households with a monthly income of $9k or more have rent of at least $2.0k."""
    high_income = df[df["monthly_income_k"] >= 9]
    if high_income.empty:
        return True, "No households with monthly income >= 9k to check."
    condition = high_income["rent_k"] >= 2.0
    truth = condition.all()
    if truth:
        return True, f"All {len(high_income)} households with income >= 9k have rent >= 2.0k."
    viol = high_income[~condition]
    ids = viol["household_id"].tolist()
    return False, f"{len(viol)} households with income >= 9k have rent < 2.0k (IDs: {', '.join(ids)})."

def stmt_6(df: pd.DataFrame):
    """6. All households with a size of six persons have rent of $1.8k or less."""
    size_six = df[df["household_size"] == 6]
    if size_six.empty:
        return True, "No households of size 6 to check."
    condition = size_six["rent_k"] <= 1.8
    truth = condition.all()
    if truth:
        return True, f"All {len(size_six)} households of size 6 have rent <= 1.8k."
    viol = size_six[~condition]
    ids = viol["household_id"].tolist()
    return False, f"{len(viol)} households of size 6 have rent > 1.8k (IDs: {', '.join(ids)})."

def stmt_7(df: pd.DataFrame):
    """7. All households with satellite internet are not located in urban areas."""
    sat = df[df["internet_type"] == "satellite"]
    if sat.empty:
        return True, "No households with satellite internet to check."
    condition = sat["region"]!= "urban"
    truth = condition.all()
    if truth:
        return True, f"All {len(sat)} satellite households are not in urban areas."
    viol = sat[~condition]
    ids = viol["household_id"].tolist()
    return False, f"{len(viol)} satellite households are in urban areas (IDs: {', '.join(ids)})."

def stmt_8(df: pd.DataFrame):
    """8. All households with a size of five or more persons have at most two vehicles."""
    large = df[df["household_size"] >= 5]
    if large.empty:
        return True, "No households with size >= 5 to check."
    condition = large["vehicle_count"] <= 2
    truth = condition.all()
    if truth:
        return True, f"All {len(large)} households with size >= 5 have <= 2 vehicles."
    viol = large[~condition]
    ids = viol["household_id"].tolist()
    return False, f"{len(viol)} households with size >= 5 have > 2 vehicles (IDs: {', '.join(ids)})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_24.csv")

    # Convert numeric columns safely
    numeric_cols = ["household_size", "monthly_income_k", "rent_k", "utility_cost", "vehicle_count"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

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