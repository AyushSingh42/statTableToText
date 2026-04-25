import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all households in the rural region, the internet type is either satellite or cable (no DSL or fiber)."""
    rural = df[df["region"] == "rural"]
    valid_internet = rural["internet_type"].isin(["satellite", "cable"])
    truth = valid_internet.all()
    if truth:
        expl = f"All {len(rural)} rural households have satellite or cable internet."
    else:
        viol = rural[~valid_internet]
        expl = f"{len(viol)} rural households have invalid internet types ({', '.join(viol['internet_type'].tolist())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Every urban household has exactly one vehicle."""
    urban = df[df["region"] == "urban"]
    exactly_one_vehicle = urban["vehicle_count"] == 1
    truth = exactly_one_vehicle.all()
    if truth:
        expl = f"All {len(urban)} urban households have exactly one vehicle."
    else:
        viol = urban[~exactly_one_vehicle]
        expl = f"{len(viol)} urban households do not have exactly one vehicle ({', '.join(map(str, viol['vehicle_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All households with a household size of 6 have rent of at least $2.2k."""
    size_6 = df[df["household_size"] == 6]
    rent_min = size_6["rent_k"] >= 2.2
    truth = rent_min.all()
    if truth:
        expl = f"All {len(size_6)} households with size 6 have rent >= 2.2k."
    else:
        viol = size_6[~rent_min]
        expl = f"{len(viol)} households with size 6 have rent < 2.2k ({', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with zero vehicles have a utility cost no greater than $173k."""
    no_vehicles = df[df["vehicle_count"] == 0]
    utility_max = no_vehicles["utility_cost"] <= 173
    truth = utility_max.all()
    if truth:
        expl = f"All {len(no_vehicles)} households with zero vehicles have utility cost <= 173k."
    else:
        viol = no_vehicles[~utility_max]
        expl = f"{len(viol)} households with zero vehicles have utility cost > 173k ({', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Every suburban household has a monthly income of at least $5.2k."""
    suburban = df[df["region"] == "suburban"]
    income_min = suburban["monthly_income_k"] >= 5.2
    truth = income_min.all()
    if truth:
        expl = f"All {len(suburban)} suburban households have income >= 5.2k."
    else:
        viol = suburban[~income_min]
        expl = f"{len(viol)} suburban households have income < 5.2k ({', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All rural households have a monthly income of at most $8.6k."""
    rural = df[df["region"] == "rural"]
    income_max = rural["monthly_income_k"] <= 8.6
    truth = income_max.all()
    if truth:
        expl = f"All {len(rural)} rural households have income <= 8.6k."
    else:
        viol = rural[~income_max]
        expl = f"{len(viol)} rural households have income > 8.6k ({', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For the single household with fiber internet, the vehicle count is exactly one."""
    fiber = df[df["internet_type"] == "fiber"]
    if len(fiber)!= 1:
        truth = False
        expl = f"There are {len(fiber)} households with fiber internet, not exactly one."
        return truth, expl
    vehicle_one = fiber["vehicle_count"] == 1
    truth = vehicle_one.iloc[0] if not fiber.empty else False
    if truth:
        expl = "The single household with fiber internet has exactly one vehicle."
    else:
        expl = f"The household with fiber internet has {fiber['vehicle_count'].iloc[0]} vehicles, not one."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All households with monthly income exceeding $10k have a utility cost of at least $173k."""
    high_income = df[df["monthly_income_k"] > 10]
    utility_min = high_income["utility_cost"] >= 173
    truth = utility_min.all()
    if truth:
        expl = f"All {len(high_income)} households with income > 10k have utility cost >= 173k."
    else:
        viol = high_income[~utility_min]
        expl = f"{len(viol)} households with income > 10k have utility cost < 173k ({', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All households with two vehicles have a utility cost of at least $132.5k."""
    two_vehicles = df[df["vehicle_count"] == 2]
    utility_min = two_vehicles["utility_cost"] >= 132.5
    truth = utility_min.all()
    if truth:
        expl = f"All {len(two_vehicles)} households with two vehicles have utility cost >= 132.5k."
    else:
        viol = two_vehicles[~utility_min]
        expl = f"{len(viol)} households with two vehicles have utility cost < 132.5k ({', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_4.csv")

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