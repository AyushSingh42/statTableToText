import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all stores in the west region, customer satisfaction is at least 3.6."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["customer_satisfaction"] >= 3.6
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west region stores meet the satisfaction threshold."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west region stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store's average basket size is at least 63, its monthly sales are at least $163.5k."""
    qualifying_stores = df[df["avg_basket_size"] >= 63]
    condition = qualifying_stores["monthly_sales_k"] >= 163.5
    truth = condition.all()
    if truth:
        expl = f"All {len(qualifying_stores)} stores with avg basket size >= 63 meet the sales threshold."
    else:
        viol = qualifying_stores[~condition]
        expl = f"{len(viol)} stores with avg basket size >= 63 violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all stores with more than 2500 transactions, the average basket size is at least 50.2."""
    high_transaction_stores = df[df["transactions"] > 2500]
    condition = high_transaction_stores["avg_basket_size"] >= 50.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_transaction_stores)} high transaction stores meet the basket size threshold."
    else:
        viol = high_transaction_stores[~condition]
        expl = f"{len(viol)} high transaction stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Every north region store has customer satisfaction of at least 4.6."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["customer_satisfaction"] >= 4.6
    truth = condition.all()
    if truth:
        expl = f"All {len(north_stores)} north region stores meet the satisfaction threshold."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north region stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store's customer satisfaction is at least 4.6, its monthly sales are no more than $162.8k."""
    high_satisfaction_stores = df[df["customer_satisfaction"] >= 4.6]
    condition = high_satisfaction_stores["monthly_sales_k"] <= 162.8
    truth = condition.all()
    if truth:
        expl = f"All {len(high_satisfaction_stores)} high satisfaction stores meet the sales cap."
    else:
        viol = high_satisfaction_stores[~condition]
        expl = f"{len(viol)} high satisfaction stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most stores have an average basket size greater than 50."""
    total_stores = len(df)
    qualifying_stores = df[df["avg_basket_size"] > 50]
    proportion = len(qualifying_stores) / total_stores
    truth = proportion > 0.5
    expl = f"{len(qualifying_stores)} out of {total_stores} stores have avg basket size > 50 ({proportion:.2%} of total)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every west region store records monthly sales of at least $77.7k."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["monthly_sales_k"] >= 77.7
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west region stores meet the sales threshold."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west region stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store's average basket size is at least 60, its customer satisfaction is at most 4.4."""
    qualifying_stores = df[df["avg_basket_size"] >= 60]
    condition = qualifying_stores["customer_satisfaction"] <= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(qualifying_stores)} stores with avg basket size >= 60 meet the satisfaction cap."
    else:
        viol = qualifying_stores[~condition]
        expl = f"{len(viol)} stores with avg basket size >= 60 violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All south region stores have an average basket size between 50.2 and 55.4."""
    south_stores = df[df["region"] == "south"]
    condition = (south_stores["avg_basket_size"] >= 50.2) & (south_stores["avg_basket_size"] <= 55.4)
    truth = condition.all()
    if truth:
        expl = f"All {len(south_stores)} south region stores meet the basket size range."
    else:
        viol = south_stores[~condition]
        expl = f"{len(viol)} south region stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_32.csv")

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
        (8, stmt_8),
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()