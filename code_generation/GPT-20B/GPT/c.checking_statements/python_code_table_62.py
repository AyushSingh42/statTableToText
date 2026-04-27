import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All east region stores have customer satisfaction of at least 3.7."""
    east = df[df["region"] == "east"]
    condition = east["customer_satisfaction"] >= 3.7
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east region stores have satisfaction ≥ 3.7."
    else:
        viol = east[~condition]
        viol_ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} east store(s) violate the rule (store_id: {viol_ids})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All stores with staff count of at least 20 have average basket size of at most 63.4."""
    staff_ge20 = df[df["staff_count"] >= 20]
    condition = staff_ge20["avg_basket_size"] <= 63.4
    truth = condition.all()
    if truth:
        expl = f"All {len(staff_ge20)} stores with staff ≥ 20 have avg basket size ≤ 63.4."
    else:
        viol = staff_ge20[~condition]
        viol_ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} store(s) violate the rule (store_id: {viol_ids})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All stores with monthly sales exceeding $150k have customer satisfaction of at least 4.0."""
    sales_gt150 = df[df["monthly_sales_k"] > 150]
    condition = sales_gt150["customer_satisfaction"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(sales_gt150)} stores with sales > 150k have satisfaction ≥ 4.0."
    else:
        viol = sales_gt150[~condition]
        viol_ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} store(s) violate the rule (store_id: {viol_ids})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with average basket size greater than 60 have monthly sales of at least $78.1k."""
    basket_gt60 = df[df["avg_basket_size"] > 60]
    condition = basket_gt60["monthly_sales_k"] >= 78.1
    truth = condition.all()
    if truth:
        expl = f"All {len(basket_gt60)} stores with avg basket > 60 have sales ≥ 78.1k."
    else:
        viol = basket_gt60[~condition]
        viol_ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} store(s) violate the rule (store_id: {viol_ids})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with customer satisfaction of at least 4.5 are located in the north region."""
    sat_ge45 = df[df["customer_satisfaction"] >= 4.5]
    condition = sat_ge45["region"] == "north"
    truth = condition.all()
    if truth:
        expl = f"All {len(sat_ge45)} stores with satisfaction ≥ 4.5 are in the north region."
    else:
        viol = sat_ge45[~condition]
        viol_ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} store(s) violate the rule (store_id: {viol_ids})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All north region stores have staff count of at most 20."""
    north = df[df["region"] == "north"]
    condition = north["staff_count"] <= 20
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north region stores have staff ≤ 20."
    else:
        viol = north[~condition]
        viol_ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} north store(s) violate the rule (store_id: {viol_ids})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All south region stores have monthly sales of at least $107.4k."""
    south = df[df["region"] == "south"]
    condition = south["monthly_sales_k"] >= 107.4
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south region stores have sales ≥ 107.4k."
    else:
        viol = south[~condition]
        viol_ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} south store(s) violate the rule (store_id: {viol_ids})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All stores with more than 2000 transactions have average basket size of at least 55.0."""
    trans_gt2000 = df[df["transactions"] > 2000]
    condition = trans_gt2000["avg_basket_size"] >= 55.0
    truth = condition.all()
    if truth:
        expl = f"All {len(trans_gt2000)} stores with >2000 transactions have avg basket ≥ 55.0."
    else:
        viol = trans_gt2000[~condition]
        viol_ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} store(s) violate the rule (store_id: {viol_ids})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_62.csv")

    # Convert numeric columns
    numeric_cols = ["monthly_sales_k", "transactions", "avg_basket_size", "staff_count", "customer_satisfaction"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

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