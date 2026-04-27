import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All north stores have an average basket size of at least 61.2."""
    north = df[df["region"] == "north"]
    condition = north["avg_basket_size"] >= 61.2
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores have avg basket size >= 61.2."
    else:
        viol = north[~condition]
        ids = viol["store_id"].tolist()
        sizes = viol["avg_basket_size"].tolist()
        expl = f"{len(viol)} north store(s) violate the rule (store_id: {', '.join(map(str, ids))}, sizes: {', '.join(map(str, sizes))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All stores with monthly sales over 160 k have customer satisfaction of at most 4.2."""
    high_sales = df[df["monthly_sales_k"] > 160]
    condition = high_sales["customer_satisfaction"] <= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} stores with monthly sales > 160k have customer satisfaction <= 4.2."
    else:
        viol = high_sales[~condition]
        ids = viol["store_id"].tolist()
        sats = viol["customer_satisfaction"].tolist()
        expl = f"{len(viol)} store(s) violate the rule (store_id: {', '.join(map(str, ids))}, satisfaction: {', '.join(map(str, sats))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All stores with an average basket size of at least 65 have monthly sales of at least 148.2 k."""
    high_basket = df[df["avg_basket_size"] >= 65]
    condition = high_basket["monthly_sales_k"] >= 148.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_basket)} stores with avg basket size >= 65 have monthly sales >= 148.2k."
    else:
        viol = high_basket[~condition]
        ids = viol["store_id"].tolist()
        sales = viol["monthly_sales_k"].tolist()
        expl = f"{len(viol)} store(s) violate the rule (store_id: {', '.join(map(str, ids))}, sales: {', '.join(map(str, sales))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All east‑region stores have monthly sales of no more than 148.2 k."""
    east = df[df["region"] == "east"]
    condition = east["monthly_sales_k"] <= 148.2
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east-region stores have monthly sales <= 148.2k."
    else:
        viol = east[~condition]
        ids = viol["store_id"].tolist()
        sales = viol["monthly_sales_k"].tolist()
        expl = f"{len(viol)} east-region store(s) violate the rule (store_id: {', '.join(map(str, ids))}, sales: {', '.join(map(str, sales))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All west‑region stores have monthly sales of at least 129.0 k."""
    west = df[df["region"] == "west"]
    condition = west["monthly_sales_k"] >= 129.0
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west-region stores have monthly sales >= 129.0k."
    else:
        viol = west[~condition]
        ids = viol["store_id"].tolist()
        sales = viol["monthly_sales_k"].tolist()
        expl = f"{len(viol)} west-region store(s) violate the rule (store_id: {', '.join(map(str, ids))}, sales: {', '.join(map(str, sales))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with more than 2 500 transactions have customer satisfaction of at least 4.0."""
    high_tx = df[df["transactions"] > 2500]
    condition = high_tx["customer_satisfaction"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(high_tx)} stores with >2500 transactions have customer satisfaction >= 4.0."
    else:
        viol = high_tx[~condition]
        ids = viol["store_id"].tolist()
        sats = viol["customer_satisfaction"].tolist()
        expl = f"{len(viol)} store(s) violate the rule (store_id: {', '.join(map(str, ids))}, satisfaction: {', '.join(map(str, sats))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with a staff count of 12 or fewer have an average basket size of at most 61.2."""
    small_staff = df[df["staff_count"] <= 12]
    condition = small_staff["avg_basket_size"] <= 61.2
    truth = condition.all()
    if truth:
        expl = f"All {len(small_staff)} stores with staff_count <= 12 have avg basket size <= 61.2."
    else:
        viol = small_staff[~condition]
        ids = viol["store_id"].tolist()
        sizes = viol["avg_basket_size"].tolist()
        expl = f"{len(viol)} store(s) violate the rule (store_id: {', '.join(map(str, ids))}, sizes: {', '.join(map(str, sizes))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one south‑region store whose customer satisfaction is 4.5 or higher."""
    south = df[df["region"] == "south"]
    condition = south["customer_satisfaction"] >= 4.5
    truth = condition.any()
    if truth:
        ids = south[condition]["store_id"].tolist()
        expl = f"At least one south-region store satisfies the rule (store_id: {', '.join(map(str, ids))})."
    else:
        expl = "No south-region store satisfies the rule."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_52.csv")

    # Convert numeric columns safely
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

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