import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All south region stores have customer satisfaction of at least 4.7."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["customer_satisfaction"] >= 4.7
    truth = condition.all()
    if truth:
        expl = f"All {len(south_stores)} south region stores meet the satisfaction threshold."
    else:
        viol = south_stores[~condition]
        expl = f"{len(viol)} south region stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All west region stores have a staff count of at least 11."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["staff_count"] >= 11
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west region stores meet the staff count threshold."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west region stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All east region stores have monthly sales between $94.9k and $131.4k."""
    east_stores = df[df["region"] == "east"]
    condition = (east_stores["monthly_sales_k"] >= 94.9) & (east_stores["monthly_sales_k"] <= 131.4)
    truth = condition.all()
    if truth:
        expl = f"All {len(east_stores)} east region stores meet the monthly sales range."
    else:
        viol = east_stores[~condition]
        expl = f"{len(viol)} east region stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with a staff count of 20 or more have an average basket size of at most 65.7."""
    high_staff = df[df["staff_count"] >= 20]
    condition = high_staff["avg_basket_size"] <= 65.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} high-staff stores meet the average basket size limit."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} high-staff stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with a customer satisfaction rating of 4.8 have monthly sales of at least $108.2k."""
    satisfied_stores = df[df["customer_satisfaction"] == 4.8]
    condition = satisfied_stores["monthly_sales_k"] >= 108.2
    truth = condition.all()
    if truth:
        expl = f"All {len(satisfied_stores)} highly satisfied stores meet the monthly sales threshold."
    else:
        viol = satisfied_stores[~condition]
        expl = f"{len(viol)} highly satisfied stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with more than 2500 transactions have an average basket size of at most 66.4."""
    many_transactions = df[df["transactions"] > 2500]
    condition = many_transactions["avg_basket_size"] <= 66.4
    truth = condition.all()
    if truth:
        expl = f"All {len(many_transactions)} high-transaction stores meet the average basket size limit."
    else:
        viol = many_transactions[~condition]
        expl = f"{len(viol)} high-transaction stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most stores have a customer satisfaction rating of at least 4.0."""
    condition = df["customer_satisfaction"] >= 4.0
    satisfied_count = condition.sum()
    total_count = len(df)
    truth = satisfied_count > total_count / 2
    if truth:
        expl = f"{satisfied_count} out of {total_count} stores satisfy the minimum satisfaction level (>50%)."
    else:
        expl = f"{satisfied_count} out of {total_count} stores satisfy the minimum satisfaction level (≤50%)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. West region stores' average basket size ranges from 48.8 to 67.3."""
    west_stores = df[df["region"] == "west"]
    min_val = west_stores["avg_basket_size"].min()
    max_val = west_stores["avg_basket_size"].max()
    truth = (min_val >= 48.8) and (max_val <= 67.3)
    if truth:
        expl = f"West region stores' average basket size ranges from {min_val:.1f} to {max_val:.1f}, within the specified bounds."
    else:
        expl = f"West region stores' average basket size ranges from {min_val:.1f} to {max_val:.1f}, which exceeds the specified bounds."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_42.csv")

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