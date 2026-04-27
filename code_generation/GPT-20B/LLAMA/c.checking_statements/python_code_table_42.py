import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the east region have a customer satisfaction rating of 4.0 or higher."""
    east = df[df["region"] == "east"]
    condition = east["customer_satisfaction"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have satisfaction >= 4.0."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east store(s) violate the rule (satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the south region, then its average basket size is greater than 60."""
    south = df[df["region"] == "south"]
    condition = south["avg_basket_size"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores have avg basket size > 60."
    else:
        viol = south[~condition]
        expl = f"{len(viol)} south store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the west region with a staff count of 20 or more."""
    west = df[df["region"] == "west"]
    exists = (west["staff_count"] >= 20).any()
    if exists:
        count = west[west["staff_count"] >= 20].shape[0]
        expl = f"Found {count} west store(s) with staff count >= 20."
    else:
        expl = "No west store has staff count >= 20."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with a monthly sales value of $150k or more have a transaction count of 1800 or less."""
    high_sales = df[df["monthly_sales_k"] >= 150]
    condition = high_sales["transactions"] <= 1800
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high‑sales stores have transactions <= 1800."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} high‑sales store(s) violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store has a staff count of 15 or less, then its customer satisfaction rating is 4.5 or higher."""
    low_staff = df[df["staff_count"] <= 15]
    condition = low_staff["customer_satisfaction"] >= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(low_staff)} low‑staff stores have satisfaction >= 4.5."
    else:
        viol = low_staff[~condition]
        expl = f"{len(viol)} low‑staff store(s) violate the rule (satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most stores in the east region have a monthly sales value of $120k or less."""
    east = df[df["region"] == "east"]
    if east.empty:
        return False, "No east stores to evaluate."
    proportion = (east["monthly_sales_k"] <= 120).mean()
    truth = proportion > 0.5
    expl = f"{proportion*100:.1f}% of east stores have monthly sales <= 120k."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with an average basket size of 65 or more have a customer satisfaction rating of 4.0 or higher."""
    large_basket = df[df["avg_basket_size"] >= 65]
    condition = large_basket["customer_satisfaction"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(large_basket)} large‑basket stores have satisfaction >= 4.0."
    else:
        viol = large_basket[~condition]
        expl = f"{len(viol)} large‑basket store(s) violate the rule (satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store is in the west region, then its staff count is 18 or more."""
    west = df[df["region"] == "west"]
    condition = west["staff_count"] >= 18
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores have staff count >= 18."
    else:
        viol = west[~condition]
        expl = f"{len(viol)} west store(s) violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the east region with a transaction count of 2700 or more."""
    east = df[df["region"] == "east"]
    exists = (east["transactions"] >= 2700).any()
    if exists:
        count = east[east["transactions"] >= 2700].shape[0]
        expl = f"Found {count} east store(s) with transactions >= 2700."
    else:
        expl = "No east store has transactions >= 2700."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All stores with a customer satisfaction rating of 4.8 or higher have an average basket size of 60 or more."""
    high_sat = df[df["customer_satisfaction"] >= 4.8]
    condition = high_sat["avg_basket_size"] >= 60
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sat)} high‑sat stores have avg basket size >= 60."
    else:
        viol = high_sat[~condition]
        expl = f"{len(viol)} high‑sat store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a store has a monthly sales value of $100k or less, then its staff count is 15 or more."""
    low_sales = df[df["monthly_sales_k"] <= 100]
    condition = low_sales["staff_count"] >= 15
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sales)} low‑sales stores have staff count >= 15."
    else:
        viol = low_sales[~condition]
        expl = f"{len(viol)} low‑sales store(s) violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most stores in the south region have a customer satisfaction rating of 4.7 or higher."""
    south = df[df["region"] == "south"]
    if south.empty:
        return False, "No south stores to evaluate."
    proportion = (south["customer_satisfaction"] >= 4.7).mean()
    truth = proportion > 0.5
    expl = f"{proportion*100:.1f}% of south stores have satisfaction >= 4.7."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All stores with a staff count of 20 or more have a monthly sales value of $150k or less."""
    high_staff = df[df["staff_count"] >= 20]
    condition = high_staff["monthly_sales_k"] <= 150
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} high‑staff stores have monthly sales <= 150k."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} high‑staff store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a store is in the east region, then its average basket size is 55 or more."""
    east = df[df["region"] == "east"]
    condition = east["avg_basket_size"] >= 55
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have avg basket size >= 55."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the west region with a customer satisfaction rating of 3.6 or less."""
    west = df[df["region"] == "west"]
    exists = (west["customer_satisfaction"] <= 3.6).any()
    if exists:
        count = west[west["customer_satisfaction"] <= 3.6].shape[0]
        expl = f"Found {count} west store(s) with satisfaction <= 3.6."
    else:
        expl = "No west store has satisfaction <= 3.6."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. All stores with a transaction count of 2000 or more have a staff count of 11 or more."""
    high_trans = df[df["transactions"] >= 2000]
    condition = high_trans["staff_count"] >= 11
    truth = condition.all()
    if truth:
        expl = f"All {len(high_trans)} high‑transaction stores have staff count >= 11."
    else:
        viol = high_trans[~condition]
        expl = f"{len(viol)} high‑transaction store(s) violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a store has an average basket size of 50 or less, then its staff count is 20 or more."""
    small_basket = df[df["avg_basket_size"] <= 50]
    condition = small_basket["staff_count"] >= 20
    truth = condition.all()
    if truth:
        expl = f"All {len(small_basket)} small‑basket stores have staff count >= 20."
    else:
        viol = small_basket[~condition]
        expl = f"{len(viol)} small‑basket store(s) violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_42.csv")

    # Convert numeric columns safely.
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
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()