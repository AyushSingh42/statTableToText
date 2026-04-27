import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All south stores have monthly sales of at least $118.8k."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["monthly_sales_k"] >= 118.8
    truth = condition.all()
    if truth:
        expl = f"All {len(south_stores)} south stores meet the minimum sales requirement."
    else:
        viol = south_stores[~condition]
        expl = f"{len(viol)} south stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All north stores have monthly sales between $82.5k and $146.7k."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["monthly_sales_k"].between(82.5, 146.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(north_stores)} north stores meet the sales range requirement."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All east stores have an average basket size of at least 49.2."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["avg_basket_size"] >= 49.2
    truth = condition.all()
    if truth:
        expl = f"All {len(east_stores)} east stores meet the minimum basket size requirement."
    else:
        viol = east_stores[~condition]
        expl = f"{len(viol)} east stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All west stores have a staff count of at least 16."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["staff_count"] >= 16
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west stores meet the minimum staff count requirement."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most stores have a customer satisfaction rating of at least 4.1."""
    condition = df["customer_satisfaction"] >= 4.1
    satisfied_count = condition.sum()
    total_count = len(df)
    truth = satisfied_count > total_count / 2
    if truth:
        expl = f"{satisfied_count} out of {total_count} stores satisfy the requirement (>50% satisfied)."
    else:
        expl = f"{satisfied_count} out of {total_count} stores satisfy the requirement (≤50% satisfied)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with monthly sales greater than $138.5k have more than 1500 transactions."""
    high_sales_stores = df[df["monthly_sales_k"] > 138.5]
    condition = high_sales_stores["transactions"] > 1500
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales_stores)} high-sales stores meet the transaction threshold."
    else:
        viol = high_sales_stores[~condition]
        expl = f"{len(viol)} high-sales stores violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a store has a staff count of at least 25, then its average basket size is at least 49.2."""
    qualifying_stores = df[df["staff_count"] >= 25]
    condition = qualifying_stores["avg_basket_size"] >= 49.2
    truth = condition.all()
    if truth:
        expl = f"All {len(qualifying_stores)} high-staff stores meet the basket size requirement."
    else:
        viol = qualifying_stores[~condition]
        expl = f"{len(viol)} high-staff stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All stores with a customer satisfaction rating of 4.6 have an average basket size of at least 49.2."""
    high_satisfaction_stores = df[df["customer_satisfaction"] == 4.6]
    condition = high_satisfaction_stores["avg_basket_size"] >= 49.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_satisfaction_stores)} high-satisfaction stores meet the basket size requirement."
    else:
        viol = high_satisfaction_stores[~condition]
        expl = f"{len(viol)} high-satisfaction stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_12.csv")

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