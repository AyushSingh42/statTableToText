import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All west region stores have monthly sales of at least 111.0 k."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["monthly_sales_k"] >= 111.0
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west region stores meet the minimum sales requirement."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west region stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All east region stores have customer satisfaction of at least 3.8."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["customer_satisfaction"] >= 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(east_stores)} east region stores meet the minimum satisfaction requirement."
    else:
        viol = east_stores[~condition]
        expl = f"{len(viol)} east region stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All stores with a staff count of at least 25 have an average basket size no more than 54.7."""
    high_staff = df[df["staff_count"] >= 25]
    condition = high_staff["avg_basket_size"] <= 54.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} high-staff stores meet the maximum basket size limit."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} high-staff stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with an average basket size greater than 60 have customer satisfaction of at least 3.9."""
    large_basket = df[df["avg_basket_size"] > 60]
    condition = large_basket["customer_satisfaction"] >= 3.9
    truth = condition.all()
    if truth:
        expl = f"All {len(large_basket)} large-basket stores meet the minimum satisfaction requirement."
    else:
        viol = large_basket[~condition]
        expl = f"{len(viol)} large-basket stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with monthly sales greater than 150 k have a staff count no more than 18."""
    high_sales = df[df["monthly_sales_k"] > 150]
    condition = high_sales["staff_count"] <= 18
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high-sales stores meet the maximum staff count limit."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} high-sales stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with at least 2600 transactions have monthly sales of at least 162.9 k."""
    many_transactions = df[df["transactions"] >= 2600]
    condition = many_transactions["monthly_sales_k"] >= 162.9
    truth = condition.all()
    if truth:
        expl = f"All {len(many_transactions)} high-transaction stores meet the minimum sales requirement."
    else:
        viol = many_transactions[~condition]
        expl = f"{len(viol)} high-transaction stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All north region stores have monthly sales of at least 110.1 k."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["monthly_sales_k"] >= 110.1
    truth = condition.all()
    if truth:
        expl = f"All {len(north_stores)} north region stores meet the minimum sales requirement."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north region stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All south region stores have an average basket size of at least 59.9."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["avg_basket_size"] >= 59.9
    truth = condition.all()
    if truth:
        expl = f"All {len(south_stores)} south region stores meet the minimum basket size requirement."
    else:
        viol = south_stores[~condition]
        expl = f"{len(viol)} south region stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_72.csv")

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