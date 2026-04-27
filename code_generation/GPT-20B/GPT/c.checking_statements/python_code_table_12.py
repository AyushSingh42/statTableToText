import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All south stores have monthly sales of at least $118.8k."""
    south = df[df["region"] == "south"]
    condition = south["monthly_sales_k"] >= 118.8
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores have sales ≥ 118.8k."
    else:
        viol = south[~condition]
        ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} south store(s) violate the rule (store_ids: {ids})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All north stores have monthly sales between $82.5k and $146.7k."""
    north = df[df["region"] == "north"]
    condition = north["monthly_sales_k"].between(82.5, 146.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores have sales between 82.5k and 146.7k."
    else:
        viol = north[~condition]
        ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} north store(s) violate the rule (store_ids: {ids})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All east stores have an average basket size of at least 49.2."""
    east = df[df["region"] == "east"]
    condition = east["avg_basket_size"] >= 49.2
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have avg basket size ≥ 49.2."
    else:
        viol = east[~condition]
        ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} east store(s) violate the rule (store_ids: {ids})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All west stores have a staff count of at least 16."""
    west = df[df["region"] == "west"]
    condition = west["staff_count"] >= 16
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores have staff count ≥ 16."
    else:
        viol = west[~condition]
        ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} west store(s) violate the rule (store_ids: {ids})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most stores have a customer satisfaction rating of at least 4.1."""
    total = len(df)
    good = df[df["customer_satisfaction"] >= 4.1]
    proportion = len(good) / total
    truth = proportion > 0.5
    if truth:
        expl = f"{len(good)}/{total} stores (>{proportion*100:.1f}%) have satisfaction ≥ 4.1."
    else:
        bad = df[df["customer_satisfaction"] < 4.1]
        ids = ", ".join(bad["store_id"])
        expl = f"Only {len(good)}/{total} stores (>{proportion*100:.1f}%) have satisfaction ≥ 4.1. Violators: {ids}."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with monthly sales greater than $138.5k have more than 1500 transactions."""
    high_sales = df[df["monthly_sales_k"] > 138.5]
    condition = high_sales["transactions"] > 1500
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high‑sales stores have >1500 transactions."
    else:
        viol = high_sales[~condition]
        ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} high‑sales store(s) violate the rule (store_ids: {ids})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a store has a staff count of at least 25, then its average basket size is at least 49.2."""
    large_staff = df[df["staff_count"] >= 25]
    condition = large_staff["avg_basket_size"] >= 49.2
    truth = condition.all()
    if truth:
        expl = f"All {len(large_staff)} stores with staff ≥25 have avg basket size ≥49.2."
    else:
        viol = large_staff[~condition]
        ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} store(s) with staff ≥25 violate the rule (store_ids: {ids})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All stores with a customer satisfaction rating of 4.6 have an average basket size of at least 49.2."""
    cs_46 = df[df["customer_satisfaction"] == 4.6]
    condition = cs_46["avg_basket_size"] >= 49.2
    truth = condition.all()
    if truth:
        expl = f"All {len(cs_46)} stores with satisfaction 4.6 have avg basket size ≥49.2."
    else:
        viol = cs_46[~condition]
        ids = ", ".join(viol["store_id"])
        expl = f"{len(viol)} store(s) with satisfaction 4.6 violate the rule (store_ids: {ids})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_12.csv")

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