import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores with 12 or fewer staff members have an average basket size of at least 52.4."""
    condition = df[df["staff_count"] <= 12]["avg_basket_size"] >= 52.4
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['staff_count'] <= 12])} stores with 12 or fewer staff have avg basket size >= 52.4."
    else:
        viol = df[(df["staff_count"] <= 12) & (df["avg_basket_size"] < 52.4)]
        expl = f"{len(viol)} stores violate the rule (staff: {', '.join(map(str, viol['staff_count'].tolist()))}, basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All stores with a customer satisfaction rating of 4.7 have at least 2,444 transactions."""
    condition = df[df["customer_satisfaction"] == 4.7]["transactions"] >= 2444
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['customer_satisfaction'] == 4.7])} stores with CS rating 4.7 have >= 2444 transactions."
    else:
        viol = df[(df["customer_satisfaction"] == 4.7) & (df["transactions"] < 2444)]
        expl = f"{len(viol)} stores violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All stores with an average basket size greater than 60 have monthly sales of no more than $124.8k."""
    condition = df[df["avg_basket_size"] > 60]["monthly_sales_k"] <= 124.8
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['avg_basket_size'] > 60])} stores with avg basket > 60 have monthly sales <= 124.8k."
    else:
        viol = df[(df["avg_basket_size"] > 60) & (df["monthly_sales_k"] > 124.8)]
        expl = f"{len(viol)} stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with monthly sales under $100k have staff counts of 22 or fewer."""
    condition = df[df["monthly_sales_k"] < 100]["staff_count"] <= 22
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['monthly_sales_k'] < 100])} stores with sales < 100k have staff count <= 22."
    else:
        viol = df[(df["monthly_sales_k"] < 100) & (df["staff_count"] > 22)]
        expl = f"{len(viol)} stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with 25 staff members have a customer satisfaction rating of at least 3.9."""
    condition = df[df["staff_count"] == 25]["customer_satisfaction"] >= 3.9
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['staff_count'] == 25])} stores with 25 staff have CS rating >= 3.9."
    else:
        viol = df[(df["staff_count"] == 25) & (df["customer_satisfaction"] < 3.9)]
        expl = f"{len(viol)} stores violate the rule (CS ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with an average basket size under 50 have monthly sales exceeding $156k."""
    condition = df[df["avg_basket_size"] < 50]["monthly_sales_k"] > 156
    truth = condition.all()
    if truth:
        expl = f"All {len(df[df['avg_basket_size'] < 50])} stores with avg basket < 50 have sales > 156k."
    else:
        viol = df[(df["avg_basket_size"] < 50) & (df["monthly_sales_k"] <= 156)]
        expl = f"{len(viol)} stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All east region stores have average basket sizes between 53.0 and 58.8."""
    east_stores = df[df["region"] == "east"]
    condition = (east_stores["avg_basket_size"] >= 53.0) & (east_stores["avg_basket_size"] <= 58.8)
    truth = condition.all()
    if truth:
        expl = f"All {len(east_stores)} east region stores have avg basket size between 53.0 and 58.8."
    else:
        viol = east_stores[~condition]
        expl = f"{len(viol)} east stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one west region store with a customer satisfaction rating of 4.3."""
    west_stores = df[df["region"] == "west"]
    has_rating_43 = (west_stores["customer_satisfaction"] == 4.3).any()
    truth = has_rating_43
    if truth:
        expl = f"At least one west store has CS rating 4.3."
    else:
        expl = f"No west store has CS rating 4.3."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_2.csv")

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