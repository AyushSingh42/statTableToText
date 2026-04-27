import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All west region stores have monthly sales of at least 111.0 k."""
    west = df[df["region"] == "west"]
    condition = west["monthly_sales_k"] >= 111.0
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west region stores have monthly sales >= 111.0 k."
    else:
        viol = west[~condition]
        values = ", ".join(map(str, viol["monthly_sales_k"].tolist()))
        expl = f"{len(viol)} west region store(s) violate the rule (monthly_sales_k: {values})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All east region stores have customer satisfaction of at least 3.8."""
    east = df[df["region"] == "east"]
    condition = east["customer_satisfaction"] >= 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east region stores have customer satisfaction >= 3.8."
    else:
        viol = east[~condition]
        values = ", ".join(map(str, viol["customer_satisfaction"].tolist()))
        expl = f"{len(viol)} east region store(s) violate the rule (customer_satisfaction: {values})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All stores with a staff count of at least 25 have an average basket size no more than 54.7."""
    staff_ge_25 = df[df["staff_count"] >= 25]
    condition = staff_ge_25["avg_basket_size"] <= 54.7
    truth = condition.all()
    if truth:
        expl = f"All {len(staff_ge_25)} stores with staff_count >= 25 have avg_basket_size <= 54.7."
    else:
        viol = staff_ge_25[~condition]
        values = ", ".join(map(str, viol["avg_basket_size"].tolist()))
        expl = f"{len(viol)} store(s) with staff_count >= 25 violate the rule (avg_basket_size: {values})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with an average basket size greater than 60 have customer satisfaction of at least 3.9."""
    basket_gt_60 = df[df["avg_basket_size"] > 60]
    condition = basket_gt_60["customer_satisfaction"] >= 3.9
    truth = condition.all()
    if truth:
        expl = f"All {len(basket_gt_60)} stores with avg_basket_size > 60 have customer_satisfaction >= 3.9."
    else:
        viol = basket_gt_60[~condition]
        values = ", ".join(map(str, viol["customer_satisfaction"].tolist()))
        expl = f"{len(viol)} store(s) with avg_basket_size > 60 violate the rule (customer_satisfaction: {values})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with monthly sales greater than 150 k have a staff count no more than 18."""
    sales_gt_150 = df[df["monthly_sales_k"] > 150]
    condition = sales_gt_150["staff_count"] <= 18
    truth = condition.all()
    if truth:
        expl = f"All {len(sales_gt_150)} stores with monthly_sales_k > 150 have staff_count <= 18."
    else:
        viol = sales_gt_150[~condition]
        values = ", ".join(map(str, viol["staff_count"].tolist()))
        expl = f"{len(viol)} store(s) with monthly_sales_k > 150 violate the rule (staff_count: {values})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with at least 2600 transactions have monthly sales of at least 162.9 k."""
    trans_ge_2600 = df[df["transactions"] >= 2600]
    condition = trans_ge_2600["monthly_sales_k"] >= 162.9
    truth = condition.all()
    if truth:
        expl = f"All {len(trans_ge_2600)} stores with transactions >= 2600 have monthly_sales_k >= 162.9 k."
    else:
        viol = trans_ge_2600[~condition]
        values = ", ".join(map(str, viol["monthly_sales_k"].tolist()))
        expl = f"{len(viol)} store(s) with transactions >= 2600 violate the rule (monthly_sales_k: {values})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All north region stores have monthly sales of at least 110.1 k."""
    north = df[df["region"] == "north"]
    condition = north["monthly_sales_k"] >= 110.1
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north region stores have monthly_sales_k >= 110.1 k."
    else:
        viol = north[~condition]
        values = ", ".join(map(str, viol["monthly_sales_k"].tolist()))
        expl = f"{len(viol)} north region store(s) violate the rule (monthly_sales_k: {values})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All south region stores have an average basket size of at least 59.9."""
    south = df[df["region"] == "south"]
    condition = south["avg_basket_size"] >= 59.9
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south region stores have avg_basket_size >= 59.9."
    else:
        viol = south[~condition]
        values = ", ".join(map(str, viol["avg_basket_size"].tolist()))
        expl = f"{len(viol)} south region store(s) violate the rule (avg_basket_size: {values})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_72.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()