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
        truth = True
        expl = "No rural households in dataset."
    else:
        sat_used = rural["internet_type"] == "satellite"
        truth = sat_used.all()
        if truth:
            expl = f"All {len(rural)} rural households use satellite internet."
        else:
            viol = rural[~sat_used]
            expl = f"{len(viol)} rural households do not use satellite internet."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All households with rent less than or equal to $0.8k have fiber internet."""
    low_rent = df[df["rent_k"] <= 0.8]
    if low_rent.empty:
        truth = True
        expl = "No households with rent <= $0.8k."
    else:
        fiber = low_rent["internet_type"] == "fiber"
        truth = fiber.all()
        if truth:
            expl = f"All {len(low_rent)} low-rent households have fiber internet."
        else:
            viol = low_rent[~fiber]
            expl = f"{len(viol)} low-rent households do not have fiber internet."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All single-person households have an internet type other than fiber."""
    single = df[df["household_size"] == 1]
    if single.empty:
        truth = True
        expl = "No single-person households in dataset."
    else:
        not_fiber = single["internet_type"]!= "fiber"
        truth = not_fiber.all()
        if truth:
            expl = f"All {len(single)} single-person households do not have fiber internet."
        else:
            viol = single[~not_fiber]
            expl = f"{len(viol)} single-person households have fiber internet."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All urban households have a utility cost of at least $84.4."""
    urban = df[df["region"] == "urban"]
    if urban.empty:
        truth = True
        expl = "No urban households in dataset."
    else:
        min_utility = urban["utility_cost"] >= 84.4
        truth = min_utility.all()
        if truth:
            expl = f"All {len(urban)} urban households have utility cost >= $84.4."
        else:
            viol = urban[~min_utility]
            expl = f"{len(viol)} urban households have utility cost < $84.4."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All households with a monthly income of $9k or more have rent of at least $2.0k."""
    high_income = df[df["monthly_income_k"] >= 9.0]
    if high_income.empty:
        truth = True
        expl = "No households with income >= $9k."
    else:
        min_rent = high_income["rent_k"] >= 2.0
        truth = min_rent.all()
        if truth:
            expl = f"All {len(high_income)} high-income households have rent >= $2.0k."
        else:
            viol = high_income[~min_rent]
            expl = f"{len(viol)} high-income households have rent < $2.0k."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All households with a size of six persons have rent of $1.8k or less."""
    size_six = df[df["household_size"] == 6]
    if size_six.empty:
        truth = True
        expl = "No six-person households in dataset."
    else:
        max_rent = size_six["rent_k"] <= 1.8
        truth = max_rent.all()
        if truth:
            expl = f"All {len(size_six)} six-person households have rent <= $1.8k."
        else:
            viol = size_six[~max_rent]
            expl = f"{len(viol)} six-person households have rent > $1.8k."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with satellite internet are not located in urban areas."""
    sat_users = df[df["internet_type"] == "satellite"]
    if sat_users.empty:
        truth = True
        expl = "No households with satellite internet."
    else:
        not_urban = sat_users["region"]!= "urban"
        truth = not_urban.all()
        if truth:
            expl = f"All {len(sat_users)} satellite users are not in urban areas."
        else:
            viol = sat_users[~not_urban]
            expl = f"{len(viol)} satellite users are in urban areas."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All households with a size of five or more persons have at most two vehicles."""
    large_households = df[df["household_size"] >= 5]
    if large_households.empty:
        truth = True
        expl = "No households with size >= 5."
    else:
        max_vehicles = large_households["vehicle_count"] <= 2
        truth = max_vehicles.all()
        if truth:
            expl = f"All {len(large_households)} large households have at most 2 vehicles."
        else:
            viol = large_households[~max_vehicles]
            expl = f"{len(viol)} large households have more than 2 vehicles."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_24.csv")

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