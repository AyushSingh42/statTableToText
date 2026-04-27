import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All north stores have an average basket size of at least 61.2."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["avg_basket_size"] >= 61.2
    truth = condition.all()
    if truth:
        expl = f"All {len(north_stores)} north stores have avg basket size >= 61.2."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All stores with monthly sales over 160 k have customer satisfaction of at most 4.2."""
    high_sales = df[df["monthly_sales_k"] > 160]
    condition = high_sales["customer_satisfaction"] <= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high-sales stores have customer satisfaction <= 4.2."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} high-sales stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All stores with an average basket size of at least 65 have monthly sales of at least 148.2 k."""
    high_basket = df[df["avg_basket_size"] >= 65]
    condition = high_basket["monthly_sales_k"] >= 148.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_basket)} high-basket stores have monthly sales >= 148.2 k."
    else:
        viol = high_basket[~condition]
        expl = f"{len(viol)} high-basket stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All east-region stores have monthly sales of no more than 148.2 k."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["monthly_sales_k"] <= 148.2
    truth = condition.all()
    if truth:
        expl = f"All {len(east_stores)} east stores have monthly sales <= 148.2 k."
    else:
        viol = east_stores[~condition]
        expl = f"{len(viol)} east stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All west-region stores have monthly sales of at least 129.0 k."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["monthly_sales_k"] >= 129.0
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west stores have monthly sales >= 129.0 k."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with more than 2 500 transactions have customer satisfaction of at least 4.0."""
    many_transactions = df[df["transactions"] > 2500]
    condition = many_transactions["customer_satisfaction"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(many_transactions)} high-transaction stores have customer satisfaction >= 4.0."
    else:
        viol = many_transactions[~condition]
        expl = f"{len(viol)} high-transaction stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with a staff count of 12 or fewer have an average basket size of at most 61.2."""
    few_staff = df[df["staff_count"] <= 12]
    condition = few_staff["avg_basket_size"] <= 61.2
    truth = condition.all()
    if truth:
        expl = f"All {len(few_staff)} low-staff stores have avg basket size <= 61.2."
    else:
        viol = few_staff[~condition]
        expl = f"{len(viol)} low-staff stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one south-region store whose customer satisfaction is 4.5 or higher."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["customer_satisfaction"] >= 4.5
    truth = condition.any()
    if truth:
        viol = south_stores[condition]
        expl = f"At least one south store has satisfaction >= 4.5 (e.g., {viol.iloc[0]['store_id']} with {viol.iloc[0]['customer_satisfaction']})."
    else:
        expl = f"No south store has satisfaction >= 4.5."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_52.csv")

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