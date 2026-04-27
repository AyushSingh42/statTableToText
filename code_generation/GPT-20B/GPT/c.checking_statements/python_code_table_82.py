import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All north region stores have staff counts of at most 18."""
    north = df[df["region"] == "north"]
    condition = north["staff_count"] <= 18
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores have staff counts ≤ 18."
    else:
        viol = north[~condition]
        expl = f"{len(viol)} north store(s) violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All west region stores have staff counts of no more than 24."""
    west = df[df["region"] == "west"]
    condition = west["staff_count"] <= 24
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores have staff counts ≤ 24."
    else:
        viol = west[~condition]
        expl = f"{len(viol)} west store(s) violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All stores with monthly sales greater than $170k have average basket sizes of at most 60.2."""
    high_sales = df[df["monthly_sales_k"] > 170]
    condition = high_sales["avg_basket_size"] <= 60.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high‑sales stores have avg basket size ≤ 60.2."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} high‑sales store(s) violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with staff counts of at least 24 have monthly sales of at least $157k."""
    many_staff = df[df["staff_count"] >= 24]
    condition = many_staff["monthly_sales_k"] >= 157
    truth = condition.all()
    if truth:
        expl = f"All {len(many_staff)} stores with ≥24 staff have monthly sales ≥ 157k."
    else:
        viol = many_staff[~condition]
        expl = f"{len(viol)} store(s) with ≥24 staff violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with an average basket size of at least 62 have monthly sales of at least $102.9k."""
    big_basket = df[df["avg_basket_size"] >= 62]
    condition = big_basket["monthly_sales_k"] >= 102.9
    truth = condition.all()
    if truth:
        expl = f"All {len(big_basket)} stores with avg basket ≥ 62 have monthly sales ≥ 102.9k."
    else:
        viol = big_basket[~condition]
        expl = f"{len(viol)} store(s) with avg basket ≥ 62 violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All east region stores have customer satisfaction scores of at least 4.0."""
    east = df[df["region"] == "east"]
    condition = east["customer_satisfaction"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have customer satisfaction ≥ 4.0."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east store(s) violate the rule (customer satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with monthly sales exceeding $150k have at least 13 staff members."""
    high_sales = df[df["monthly_sales_k"] > 150]
    condition = high_sales["staff_count"] >= 13
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} stores with monthly sales > 150k have ≥ 13 staff."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} store(s) with monthly sales > 150k violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All stores with at least 2500 transactions have monthly sales of at least $99.8k."""
    many_trans = df[df["transactions"] >= 2500]
    condition = many_trans["monthly_sales_k"] >= 99.8
    truth = condition.all()
    if truth:
        expl = f"All {len(many_trans)} stores with ≥ 2500 transactions have monthly sales ≥ 99.8k."
    else:
        viol = many_trans[~condition]
        expl = f"{len(viol)} store(s) with ≥ 2500 transactions violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_82.csv")

    # Convert columns to numeric where possible
    for col in df.columns:
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