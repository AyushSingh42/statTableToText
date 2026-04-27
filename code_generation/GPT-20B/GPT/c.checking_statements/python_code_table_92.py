import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores have an average basket size of at least 48.1 items."""
    condition = df["avg_basket_size"] >= 48.1
    truth = condition.all()
    if truth:
        expl = f"All {len(df)} stores have avg basket size >= 48.1."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Every north‑region store has a customer‑satisfaction rating of at least 3.6."""
    north = df[df["region"] == "north"]
    condition = north["customer_satisfaction"] >= 3.6
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north‑region stores have customer satisfaction >= 3.6."
    else:
        viol = north[~condition]
        expl = f"{len(viol)} north‑region stores violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all stores with monthly sales greater than $150 k, the average basket size is at least 55.0 items."""
    high_sales = df[df["monthly_sales_k"] > 150]
    condition = high_sales["avg_basket_size"] >= 55.0
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} stores with monthly sales > 150k have avg basket size >= 55.0."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with a staff count of 25 or more have a customer‑satisfaction rating of at least 4.5."""
    large_staff = df[df["staff_count"] >= 25]
    condition = large_staff["customer_satisfaction"] >= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(large_staff)} stores with staff count >= 25 have customer satisfaction >= 4.5."
    else:
        viol = large_staff[~condition]
        expl = f"{len(viol)} stores violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Any store whose average basket size exceeds 65 items records monthly sales of at least $110 k."""
    big_basket = df[df["avg_basket_size"] > 65]
    if big_basket.empty:
        truth = True
        expl = "No stores have avg basket size > 65, so the statement holds vacuously."
    else:
        condition = big_basket["monthly_sales_k"] >= 110
        truth = condition.all()
        if truth:
            expl = f"All {len(big_basket)} stores with avg basket size > 65 have monthly sales >= 110k."
        else:
            viol = big_basket[~condition]
            expl = f"{len(viol)} stores violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with more than 2,200 transactions have a customer‑satisfaction rating of no more than 3.7."""
    high_trans = df[df["transactions"] > 2200]
    condition = high_trans["customer_satisfaction"] <= 3.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_trans)} stores with > 2200 transactions have customer satisfaction <= 3.7."
    else:
        viol = high_trans[~condition]
        expl = f"{len(viol)} stores violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every store with a customer‑satisfaction rating of 4.6 or higher achieves monthly sales of at least $110 k."""
    high_satis = df[df["customer_satisfaction"] >= 4.6]
    if high_satis.empty:
        truth = True
        expl = "No stores have customer satisfaction >= 4.6, so the statement holds vacuously."
    else:
        condition = high_satis["monthly_sales_k"] >= 110
        truth = condition.all()
        if truth:
            expl = f"All {len(high_satis)} stores with customer satisfaction >= 4.6 have monthly sales >= 110k."
        else:
            viol = high_satis[~condition]
            expl = f"{len(viol)} stores violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_92.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col not in ["region", "store_id"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    checks = [
        (1, stmt_1),
        (2, stmt_2),
        (3, stmt_3),
        (4, stmt_4),
        (5, stmt_5),
        (6, stmt_6),
        (7, stmt_7),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()