import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all stores in the west region, customer satisfaction is at least 3.6."""
    west = df[df["region"] == "west"]
    condition = west["customer_satisfaction"] >= 3.6
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores have customer satisfaction ≥ 3.6."
    else:
        viol = west[~condition]
        expl = f"{len(viol)} west store(s) violate the rule (satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store's average basket size is at least 63, its monthly sales are at least $163.5k."""
    cond = df["avg_basket_size"] >= 63
    subset = df[cond]
    truth = subset["monthly_sales_k"].ge(163.5).all()
    if truth:
        expl = f"All {len(subset)} stores with avg basket size ≥ 63 have monthly sales ≥ $163.5k."
    else:
        viol = subset[~subset["monthly_sales_k"].ge(163.5)]
        expl = f"{len(viol)} store(s) violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all stores with more than 2500 transactions, the average basket size is at least 50.2."""
    cond = df["transactions"] > 2500
    subset = df[cond]
    truth = subset["avg_basket_size"].ge(50.2).all()
    if truth:
        expl = f"All {len(subset)} stores with >2500 transactions have avg basket size ≥ 50.2."
    else:
        viol = subset[~subset["avg_basket_size"].ge(50.2)]
        expl = f"{len(viol)} store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Every north region store has customer satisfaction of at least 4.6."""
    north = df[df["region"] == "north"]
    truth = north["customer_satisfaction"].ge(4.6).all()
    if truth:
        expl = f"All {len(north)} north stores have customer satisfaction ≥ 4.6."
    else:
        viol = north[~north["customer_satisfaction"].ge(4.6)]
        expl = f"{len(viol)} north store(s) violate the rule (satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store's customer satisfaction is at least 4.6, its monthly sales are no more than $162.8k."""
    cond = df["customer_satisfaction"] >= 4.6
    subset = df[cond]
    truth = subset["monthly_sales_k"].le(162.8).all()
    if truth:
        expl = f"All {len(subset)} stores with satisfaction ≥ 4.6 have monthly sales ≤ $162.8k."
    else:
        viol = subset[~subset["monthly_sales_k"].le(162.8)]
        expl = f"{len(viol)} store(s) violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most stores have an average basket size greater than 50."""
    total = len(df)
    count_gt_50 = df["avg_basket_size"].gt(50).sum()
    proportion = count_gt_50 / total
    truth = proportion > 0.5
    percent = round(proportion * 100, 1)
    if truth:
        expl = f"{count_gt_50} out of {total} stores have avg basket size > 50 ({percent}%)."
    else:
        expl = f"Only {count_gt_50} out of {total} stores have avg basket size > 50 ({percent}%)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every west region store records monthly sales of at least $77.7k."""
    west = df[df["region"] == "west"]
    truth = west["monthly_sales_k"].ge(77.7).all()
    if truth:
        expl = f"All {len(west)} west stores have monthly sales ≥ $77.7k."
    else:
        viol = west[~west["monthly_sales_k"].ge(77.7)]
        expl = f"{len(viol)} west store(s) violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store's average basket size is at least 60, its customer satisfaction is at most 4.4."""
    cond = df["avg_basket_size"] >= 60
    subset = df[cond]
    truth = subset["customer_satisfaction"].le(4.4).all()
    if truth:
        expl = f"All {len(subset)} stores with avg basket size ≥ 60 have satisfaction ≤ 4.4."
    else:
        viol = subset[~subset["customer_satisfaction"].le(4.4)]
        expl = f"{len(viol)} store(s) violate the rule (satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All south region stores have an average basket size between 50.2 and 55.4."""
    south = df[df["region"] == "south"]
    condition = south["avg_basket_size"].between(50.2, 55.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores have avg basket size between 50.2 and 55.4."
    else:
        viol = south[~condition]
        expl = f"{len(viol)} south store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_32.csv")

    # Convert numeric columns safely
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
        (9, stmt_9),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()