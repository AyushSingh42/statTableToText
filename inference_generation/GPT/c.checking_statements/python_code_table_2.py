import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def convert_numeric(df: pd.DataFrame) -> pd.DataFrame:
    # columns that should be numeric
    num_cols = ["store_id", "monthly_sales_k", "transactions", "avg_basket_size", "staff_count", "customer_satisfaction"]
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

def stmt_1(df: pd.DataFrame):
    """All west region stores have customer satisfaction of 3.9 or lower."""
    west = df[df["region"] == "west"]
    condition = west["customer_satisfaction"] <= 3.9
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores satisfy the condition."
    else:
        viol = west[~condition]
        ids = ", ".join(map(str, viol["store_id"].tolist()))
        expl = f"{len(viol)} west store(s) violate the rule (store_id(s): {ids})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """All east region stores have an average basket size of at least 58.3."""
    east = df[df["region"] == "east"]
    condition = east["avg_basket_size"] >= 58.3
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores satisfy the condition."
    else:
        viol = east[~condition]
        ids = ", ".join(map(str, viol["store_id"].tolist()))
        expl = f"{len(viol)} east store(s) violate the rule (store_id(s): {ids})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """All south region stores have monthly sales of $110.8k or less."""
    south = df[df["region"] == "south"]
    condition = south["monthly_sales_k"] <= 110.8
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores satisfy the condition."
    else:
        viol = south[~condition]
        ids = ", ".join(map(str, viol["store_id"].tolist()))
        expl = f"{len(viol)} south store(s) violate the rule (store_id(s): {ids})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """Stores with at least 20 staff members have monthly sales of at least $143.2k."""
    staff = df[df["staff_count"] >= 20]
    condition = staff["monthly_sales_k"] >= 143.2
    truth = condition.all()
    if truth:
        expl = f"All {len(staff)} stores with ≥20 staff meet the sales threshold."
    else:
        viol = staff[~condition]
        ids = ", ".join(map(str, viol["store_id"].tolist()))
        expl = f"{len(viol)} store(s) with ≥20 staff violate the rule (store_id(s): {ids})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """Stores with an average basket size greater than 60 have customer satisfaction of at least 4.4."""
    basket = df[df["avg_basket_size"] > 60]
    condition = basket["customer_satisfaction"] >= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(basket)} stores with basket size >60 satisfy the condition."
    else:
        viol = basket[~condition]
        ids = ", ".join(map(str, viol["store_id"].tolist()))
        expl = f"{len(viol)} store(s) with basket size >60 violate the rule (store_id(s): {ids})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """Stores with more than 2400 transactions have monthly sales of at least $157.6k."""
    trans = df[df["transactions"] > 2400]
    condition = trans["monthly_sales_k"] >= 157.6
    truth = condition.all()
    if truth:
        expl = f"All {len(trans)} stores with >2400 transactions meet the sales threshold."
    else:
        viol = trans[~condition]
        ids = ", ".join(map(str, viol["store_id"].tolist()))
        expl = f"{len(viol)} store(s) with >2400 transactions violate the rule (store_id(s): {ids})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """Most stores (12 of 15) have a customer satisfaction rating of 4.0 or higher."""
    total = len(df)
    high_sat = df[df["customer_satisfaction"] >= 4.0]
    count = len(high_sat)
    truth = count >= 12 and total == 15
    if truth:
        expl = f"{count} of {total} stores have satisfaction ≥4.0, meeting the 12‑of‑15 requirement."
    else:
        expl = f"Only {count} of {total} stores have satisfaction ≥4.0; requirement not met."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """If a store is in the north region, then its monthly sales are at least $128.4k."""
    north = df[df["region"] == "north"]
    condition = north["monthly_sales_k"] >= 128.4
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores have sales ≥128.4k."
    else:
        viol = north[~condition]
        ids = ", ".join(map(str, viol["store_id"].tolist()))
        expl = f"{len(viol)} north store(s) violate the rule (store_id(s): {ids})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """If a store’s customer satisfaction is 4.5 or higher, then the store is located in the north or east region."""
    high_sat = df[df["customer_satisfaction"] >= 4.5]
    condition = high_sat["region"].isin(["north", "east"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sat)} high‑satisfaction stores are in north or east."
    else:
        viol = high_sat[~condition]
        ids = ", ".join(map(str, viol["store_id"].tolist()))
        expl = f"{len(viol)} high‑satisfaction store(s) violate the rule (store_id(s): {ids})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_2.csv")
    df = convert_numeric(df)

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