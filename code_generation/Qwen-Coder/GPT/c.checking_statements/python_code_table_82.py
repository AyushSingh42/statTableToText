import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All north region stores have staff counts of at most 18."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["staff_count"] <= 18
    truth = condition.all()
    if truth:
        expl = f"All {len(north_stores)} north region stores have staff count <= 18."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north region stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All west region stores have staff counts of no more than 24."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["staff_count"] <= 24
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west region stores have staff count <= 24."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west region stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All stores with monthly sales greater than $170k have average basket sizes of at most 60.2."""
    high_sales = df[df["monthly_sales_k"] > 170]
    condition = high_sales["avg_basket_size"] <= 60.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high-sales stores have avg basket size <= 60.2."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} high-sales stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with staff counts of at least 24 have monthly sales of at least $157k."""
    high_staff = df[df["staff_count"] >= 24]
    condition = high_staff["monthly_sales_k"] >= 157
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} high-staff stores have monthly sales >= 157k."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} high-staff stores violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with an average basket size of at least 62 have monthly sales of at least $102.9k."""
    high_basket = df[df["avg_basket_size"] >= 62]
    condition = high_basket["monthly_sales_k"] >= 102.9
    truth = condition.all()
    if truth:
        expl = f"All {len(high_basket)} high-basket stores have monthly sales >= 102.9k."
    else:
        viol = high_basket[~condition]
        expl = f"{len(viol)} high-basket stores violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All east region stores have customer satisfaction scores of at least 4.0."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["customer_satisfaction"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(east_stores)} east region stores have customer satisfaction >= 4.0."
    else:
        viol = east_stores[~condition]
        expl = f"{len(viol)} east region stores violate the rule (satisfaction scores: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with monthly sales exceeding $150k have at least 13 staff members."""
    high_sales = df[df["monthly_sales_k"] > 150]
    condition = high_sales["staff_count"] >= 13
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high-sales stores have staff count >= 13."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} high-sales stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All stores with at least 2500 transactions have monthly sales of at least $99.8k."""
    high_transactions = df[df["transactions"] >= 2500]
    condition = high_transactions["monthly_sales_k"] >= 99.8
    truth = condition.all()
    if truth:
        expl = f"All {len(high_transactions)} high-transaction stores have monthly sales >= 99.8k."
    else:
        viol = high_transactions[~condition]
        expl = f"{len(viol)} high-transaction stores violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_82.csv")

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