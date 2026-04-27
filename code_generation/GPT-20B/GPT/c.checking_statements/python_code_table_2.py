import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores with 12 or fewer staff members have an average basket size of at least 52.4."""
    subset = df[df["staff_count"] <= 12]
    if subset.empty:
        return True, "No stores have 12 or fewer staff members."
    condition = subset["avg_basket_size"] >= 52.4
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} stores with <=12 staff have avg basket size >= 52.4."
    viol = subset[~condition]
    return False, f"{len(viol)} store(s) violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. All stores with a customer satisfaction rating of 4.7 have at least 2,444 transactions."""
    subset = df[df["customer_satisfaction"] == 4.7]
    if subset.empty:
        return True, "No stores have a customer satisfaction rating of 4.7."
    condition = subset["transactions"] >= 2444
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} stores with rating 4.7 have >= 2444 transactions."
    viol = subset[~condition]
    return False, f"{len(viol)} store(s) violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. All stores with an average basket size greater than 60 have monthly sales of no more than $124.8k."""
    subset = df[df["avg_basket_size"] > 60]
    if subset.empty:
        return True, "No stores have avg basket size > 60."
    condition = subset["monthly_sales_k"] <= 124.8
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} stores with avg basket size > 60 have monthly sales <= 124.8k."
    viol = subset[~condition]
    return False, f"{len(viol)} store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."

def stmt_4(df: pd.DataFrame):
    """4. All stores with monthly sales under $100k have staff counts of 22 or fewer."""
    subset = df[df["monthly_sales_k"] < 100]
    if subset.empty:
        return True, "No stores have monthly sales under $100k."
    condition = subset["staff_count"] <= 22
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} stores with monthly sales < 100k have staff <= 22."
    viol = subset[~condition]
    return False, f"{len(viol)} store(s) violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."

def stmt_5(df: pd.DataFrame):
    """5. All stores with 25 staff members have a customer satisfaction rating of at least 3.9."""
    subset = df[df["staff_count"] == 25]
    if subset.empty:
        return True, "No stores have exactly 25 staff members."
    condition = subset["customer_satisfaction"] >= 3.9
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} stores with 25 staff have rating >= 3.9."
    viol = subset[~condition]
    return False, f"{len(viol)} store(s) violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."

def stmt_6(df: pd.DataFrame):
    """6. All stores with an average basket size under 50 have monthly sales exceeding $156k."""
    subset = df[df["avg_basket_size"] < 50]
    if subset.empty:
        return True, "No stores have avg basket size < 50."
    condition = subset["monthly_sales_k"] > 156
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} stores with avg basket size < 50 have monthly sales > 156k."
    viol = subset[~condition]
    return False, f"{len(viol)} store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."

def stmt_7(df: pd.DataFrame):
    """7. All east region stores have average basket sizes between 53.0 and 58.8."""
    subset = df[df["region"] == "east"]
    if subset.empty:
        return True, "No east region stores."
    condition = subset["avg_basket_size"].between(53.0, 58.8, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} east region stores have avg basket size between 53.0 and 58.8."
    viol = subset[~condition]
    return False, f"{len(viol)} east region store(s) violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one west region store with a customer satisfaction rating of 4.3."""
    subset = df[(df["region"] == "west") & (df["customer_satisfaction"] == 4.3)]
    truth = not subset.empty
    if truth:
        return True, f"Found {len(subset)} west region store(s) with rating 4.3."
    else:
        return False, "No west region store has a customer satisfaction rating of 4.3."

def main():
    df = pd.read_csv("../inference_generation/tables/table_2.csv")

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