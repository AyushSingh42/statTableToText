import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All east region stores have an average basket size greater than 66."""
    east = df[df["region"] == "east"]
    condition = east["avg_basket_size"] > 66
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have avg basket size > 66."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east store(s) violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All west region stores have customer satisfaction of 4.5 or lower."""
    west = df[df["region"] == "west"]
    condition = west["customer_satisfaction"] <= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores have customer satisfaction <= 4.5."
    else:
        viol = west[~condition]
        expl = f"{len(viol)} west store(s) violate the rule (customer satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All north region stores have monthly sales below 135 thousand."""
    north = df[df["region"] == "north"]
    condition = north["monthly_sales_k"] < 135
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores have monthly sales < 135k."
    else:
        viol = north[~condition]
        expl = f"{len(viol)} north store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All south region stores have a staff count of at least 16."""
    south = df[df["region"] == "south"]
    condition = south["staff_count"] >= 16
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores have staff count >= 16."
    else:
        viol = south[~condition]
        expl = f"{len(viol)} south store(s) violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with an average basket size of at least 67 have monthly sales exceeding 140 thousand."""
    cond = df["avg_basket_size"] >= 67
    subset = df[cond]
    condition = subset["monthly_sales_k"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} stores with avg basket size >= 67 have monthly sales > 140k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with a staff count of 24 or more have customer satisfaction of 4.4 or lower."""
    cond = df["staff_count"] >= 24
    subset = df[cond]
    condition = subset["customer_satisfaction"] <= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} stores with staff count >= 24 have customer satisfaction <= 4.4."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} store(s) violate the rule (customer satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with 12 or fewer staff members have monthly sales of at most 151.1 thousand."""
    cond = df["staff_count"] <= 12
    subset = df[cond]
    condition = subset["monthly_sales_k"] <= 151.1
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} stores with staff count <= 12 have monthly sales <= 151.1k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All stores with transactions fewer than 1500 have an average basket size greater than 59."""
    cond = df["transactions"] < 1500
    subset = df[cond]
    condition = subset["avg_basket_size"] > 59
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} stores with transactions < 1500 have avg basket size > 59."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_22.csv")

    # Convert numeric columns where possible
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