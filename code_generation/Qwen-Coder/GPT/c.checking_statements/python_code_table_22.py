import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All east region stores have an average basket size greater than 66."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["avg_basket_size"] > 66
    truth = condition.all()
    if truth:
        expl = f"All {len(east_stores)} east region stores have avg basket size > 66."
    else:
        viol = east_stores[~condition]
        expl = f"{len(viol)} east region stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All west region stores have customer satisfaction of 4.5 or lower."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["customer_satisfaction"] <= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west region stores have customer satisfaction <= 4.5."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west region stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All north region stores have monthly sales below 135 thousand."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["monthly_sales_k"] < 135
    truth = condition.all()
    if truth:
        expl = f"All {len(north_stores)} north region stores have monthly sales < 135k."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north region stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All south region stores have a staff count of at least 16."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["staff_count"] >= 16
    truth = condition.all()
    if truth:
        expl = f"All {len(south_stores)} south region stores have staff count >= 16."
    else:
        viol = south_stores[~condition]
        expl = f"{len(viol)} south region stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with an average basket size of at least 67 have monthly sales exceeding 140 thousand."""
    qualifying_stores = df[df["avg_basket_size"] >= 67]
    condition = qualifying_stores["monthly_sales_k"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(qualifying_stores)} stores with avg basket size >= 67 have monthly sales > 140k."
    else:
        viol = qualifying_stores[~condition]
        expl = f"{len(viol)} stores with avg basket size >= 67 violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with a staff count of 24 or more have customer satisfaction of 4.4 or lower."""
    qualifying_stores = df[df["staff_count"] >= 24]
    condition = qualifying_stores["customer_satisfaction"] <= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(qualifying_stores)} stores with staff count >= 24 have customer satisfaction <= 4.4."
    else:
        viol = qualifying_stores[~condition]
        expl = f"{len(viol)} stores with staff count >= 24 violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with 12 or fewer staff members have monthly sales of at most 151.1 thousand."""
    qualifying_stores = df[df["staff_count"] <= 12]
    condition = qualifying_stores["monthly_sales_k"] <= 151.1
    truth = condition.all()
    if truth:
        expl = f"All {len(qualifying_stores)} stores with staff count <= 12 have monthly sales <= 151.1k."
    else:
        viol = qualifying_stores[~condition]
        expl = f"{len(viol)} stores with staff count <= 12 violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All stores with transactions fewer than 1500 have an average basket size greater than 59."""
    qualifying_stores = df[df["transactions"] < 1500]
    condition = qualifying_stores["avg_basket_size"] > 59
    truth = condition.all()
    if truth:
        expl = f"All {len(qualifying_stores)} stores with transactions < 1500 have avg basket size > 59."
    else:
        viol = qualifying_stores[~condition]
        expl = f"{len(viol)} stores with transactions < 1500 violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_22.csv")

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