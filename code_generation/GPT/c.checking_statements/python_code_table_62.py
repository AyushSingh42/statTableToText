import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All east region stores have customer satisfaction of at least 3.7."""
    east_stores = df[df["region"] == "east"]
    if east_stores.empty:
        truth = True
        expl = "No east region stores found."
    else:
        condition = east_stores["customer_satisfaction"] >= 3.7
        truth = condition.all()
        if truth:
            expl = f"All {len(east_stores)} east region stores satisfy the condition."
        else:
            viol = east_stores[~condition]
            expl = f"{len(viol)} east region stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All stores with staff count of at least 20 have average basket size of at most 63.4."""
    high_staff = df[df["staff_count"] >= 20]
    if high_staff.empty:
        truth = True
        expl = "No stores with staff count >= 20 found."
    else:
        condition = high_staff["avg_basket_size"] <= 63.4
        truth = condition.all()
        if truth:
            expl = f"All {len(high_staff)} high staff count stores satisfy the condition."
        else:
            viol = high_staff[~condition]
            expl = f"{len(viol)} high staff count stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All stores with monthly sales exceeding $150k have customer satisfaction of at least 4.0."""
    high_sales = df[df["monthly_sales_k"] > 150]
    if high_sales.empty:
        truth = True
        expl = "No stores with monthly sales > 150k found."
    else:
        condition = high_sales["customer_satisfaction"] >= 4.0
        truth = condition.all()
        if truth:
            expl = f"All {len(high_sales)} high sales stores satisfy the condition."
        else:
            viol = high_sales[~condition]
            expl = f"{len(viol)} high sales stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with average basket size greater than 60 have monthly sales of at least $78.1k."""
    high_basket = df[df["avg_basket_size"] > 60]
    if high_basket.empty:
        truth = True
        expl = "No stores with avg basket size > 60 found."
    else:
        condition = high_basket["monthly_sales_k"] >= 78.1
        truth = condition.all()
        if truth:
            expl = f"All {len(high_basket)} high basket size stores satisfy the condition."
        else:
            viol = high_basket[~condition]
            expl = f"{len(viol)} high basket size stores violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with customer satisfaction of at least 4.5 are located in the north region."""
    high_satisfaction = df[df["customer_satisfaction"] >= 4.5]
    if high_satisfaction.empty:
        truth = True
        expl = "No stores with satisfaction >= 4.5 found."
    else:
        condition = high_satisfaction["region"] == "north"
        truth = condition.all()
        if truth:
            expl = f"All {len(high_satisfaction)} high satisfaction stores are in north region."
        else:
            viol = high_satisfaction[~condition]
            expl = f"{len(viol)} high satisfaction stores are not in north region (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All north region stores have staff count of at most 20."""
    north_stores = df[df["region"] == "north"]
    if north_stores.empty:
        truth = True
        expl = "No north region stores found."
    else:
        condition = north_stores["staff_count"] <= 20
        truth = condition.all()
        if truth:
            expl = f"All {len(north_stores)} north region stores satisfy the condition."
        else:
            viol = north_stores[~condition]
            expl = f"{len(viol)} north region stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All south region stores have monthly sales of at least $107.4k."""
    south_stores = df[df["region"] == "south"]
    if south_stores.empty:
        truth = True
        expl = "No south region stores found."
    else:
        condition = south_stores["monthly_sales_k"] >= 107.4
        truth = condition.all()
        if truth:
            expl = f"All {len(south_stores)} south region stores satisfy the condition."
        else:
            viol = south_stores[~condition]
            expl = f"{len(viol)} south region stores violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All stores with more than 2000 transactions have average basket size of at least 55.0."""
    many_transactions = df[df["transactions"] > 2000]
    if many_transactions.empty:
        truth = True
        expl = "No stores with transactions > 2000 found."
    else:
        condition = many_transactions["avg_basket_size"] >= 55.0
        truth = condition.all()
        if truth:
            expl = f"All {len(many_transactions)} high transaction stores satisfy the condition."
        else:
            viol = many_transactions[~condition]
            expl = f"{len(viol)} high transaction stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_62.csv")

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