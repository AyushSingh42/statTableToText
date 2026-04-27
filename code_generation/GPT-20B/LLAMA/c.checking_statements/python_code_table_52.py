import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the south region have monthly sales greater than $130k or less than $92k."""
    south = df[df["region"] == "south"]
    cond = (south["monthly_sales_k"] > 130) | (south["monthly_sales_k"] < 92)
    truth = cond.all()
    if truth:
        expl = f"All {len(south)} south stores satisfy the sales condition."
    else:
        viol = south[~cond]
        expl = f"{len(viol)} south stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the north region, then its customer satisfaction is greater than or equal to 4.2."""
    north = df[df["region"] == "north"]
    cond = north["customer_satisfaction"] >= 4.2
    truth = cond.all()
    if truth:
        expl = f"All {len(north)} north stores have customer satisfaction >= 4.2."
    else:
        viol = north[~cond]
        expl = f"{len(viol)} north stores violate the rule (satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the east region with customer satisfaction less than 4.0."""
    east = df[df["region"] == "east"]
    exists = (east["customer_satisfaction"] < 4.0).any()
    if exists:
        viol = east[east["customer_satisfaction"] < 4.0]
        expl = f"Found {len(viol)} east store(s) with satisfaction < 4.0 (ids: {', '.join(map(str, viol['store_id'].tolist()))})."
    else:
        expl = "No east store has satisfaction < 4.0."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with staff count greater than 20 have monthly sales greater than $158k."""
    high_staff = df[df["staff_count"] > 20]
    cond = high_staff["monthly_sales_k"] > 158
    truth = cond.all()
    if truth:
        expl = f"All {len(high_staff)} stores with staff > 20 have sales > 158k."
    else:
        viol = high_staff[~cond]
        expl = f"{len(viol)} store(s) with staff > 20 violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store is in the west region, then its average basket size is greater than 58k."""
    west = df[df["region"] == "west"]
    cond = west["avg_basket_size"] > 58
    truth = cond.all()
    if truth:
        expl = f"All {len(west)} west stores have avg basket size > 58k."
    else:
        viol = west[~cond]
        expl = f"{len(viol)} west store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most stores have transactions greater than 2000."""
    total = len(df)
    count = (df["transactions"] > 2000).sum()
    proportion = count / total if total > 0 else 0
    truth = proportion > 0.5
    expl = f"{count} out of {total} stores have transactions > 2000 ({proportion*100:.1f}%)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with customer satisfaction greater than 4.5 have staff count less than 18."""
    high_satis = df[df["customer_satisfaction"] > 4.5]
    cond = high_satis["staff_count"] < 18
    truth = cond.all()
    if truth:
        expl = f"All {len(high_satis)} stores with satisfaction > 4.5 have staff < 18."
    else:
        viol = high_satis[~cond]
        expl = f"{len(viol)} store(s) with satisfaction > 4.5 violate the rule (staff: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store is in the south region, then its average basket size is less than 65k."""
    south = df[df["region"] == "south"]
    cond = south["avg_basket_size"] < 65
    truth = cond.all()
    if truth:
        expl = f"All {len(south)} south stores have avg basket size < 65k."
    else:
        viol = south[~cond]
        expl = f"{len(viol)} south store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the north region with monthly sales greater than $166k."""
    north = df[df["region"] == "north"]
    exists = (north["monthly_sales_k"] > 166).any()
    if exists:
        viol = north[north["monthly_sales_k"] > 166]
        expl = f"Found {len(viol)} north store(s) with sales > 166k (ids: {', '.join(map(str, viol['store_id'].tolist()))})."
    else:
        expl = "No north store has sales > 166k."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All stores with average basket size greater than 64k have customer satisfaction greater than or equal to 4.2."""
    high_basket = df[df["avg_basket_size"] > 64]
    cond = high_basket["customer_satisfaction"] >= 4.2
    truth = cond.all()
    if truth:
        expl = f"All {len(high_basket)} stores with avg basket size > 64k have satisfaction >= 4.2."
    else:
        viol = high_basket[~cond]
        expl = f"{len(viol)} store(s) with avg basket size > 64k violate the rule (satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a store has transactions less than 1800, then its staff count is less than 18."""
    low_trans = df[df["transactions"] < 1800]
    cond = low_trans["staff_count"] < 18
    truth = cond.all()
    if truth:
        expl = f"All {len(low_trans)} stores with transactions < 1800 have staff < 18."
    else:
        viol = low_trans[~cond]
        expl = f"{len(viol)} store(s) with transactions < 1800 violate the rule (staff: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most stores in the east region have customer satisfaction greater than 4.4."""
    east = df[df["region"] == "east"]
    total = len(east)
    count = (east["customer_satisfaction"] > 4.4).sum()
    proportion = count / total if total > 0 else 0
    truth = proportion > 0.5
    expl = f"{count} out of {total} east stores have satisfaction > 4.4 ({proportion*100:.1f}%)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All stores with staff count less than 15 have monthly sales less than $150k."""
    low_staff = df[df["staff_count"] < 15]
    cond = low_staff["monthly_sales_k"] < 150
    truth = cond.all()
    if truth:
        expl = f"All {len(low_staff)} stores with staff < 15 have sales < 150k."
    else:
        viol = low_staff[~cond]
        expl = f"{len(viol)} store(s) with staff < 15 violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a store is in the west region, then its customer satisfaction is greater than or equal to 4.1."""
    west = df[df["region"] == "west"]
    cond = west["customer_satisfaction"] >= 4.1
    truth = cond.all()
    if truth:
        expl = f"All {len(west)} west stores have satisfaction >= 4.1."
    else:
        viol = west[~cond]
        expl = f"{len(viol)} west store(s) violate the rule (satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the south region with staff count greater than 25."""
    south = df[df["region"] == "south"]
    exists = (south["staff_count"] > 25).any()
    if exists:
        viol = south[south["staff_count"] > 25]
        expl = f"Found {len(viol)} south store(s) with staff > 25 (ids: {', '.join(map(str, viol['store_id'].tolist()))})."
    else:
        expl = "No south store has staff > 25."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. All stores with monthly sales greater than $160k have transactions greater than 1500."""
    high_sales = df[df["monthly_sales_k"] > 160]
    cond = high_sales["transactions"] > 1500
    truth = cond.all()
    if truth:
        expl = f"All {len(high_sales)} stores with sales > 160k have transactions > 1500."
    else:
        viol = high_sales[~cond]
        expl = f"{len(viol)} store(s) with sales > 160k violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a store has average basket size less than 60k, then its staff count is less than 20."""
    low_basket = df[df["avg_basket_size"] < 60]
    cond = low_basket["staff_count"] < 20
    truth = cond.all()
    if truth:
        expl = f"All {len(low_basket)} stores with avg basket size < 60k have staff < 20."
    else:
        viol = low_basket[~cond]
        expl = f"{len(viol)} store(s) with avg basket size < 60k violate the rule (staff: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most stores have monthly sales less than $170k."""
    total = len(df)
    count = (df["monthly_sales_k"] < 170).sum()
    proportion = count / total if total > 0 else 0
    truth = proportion > 0.5
    expl = f"{count} out of {total} stores have sales < 170k ({proportion*100:.1f}%)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_52.csv")

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
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
        (18, stmt_18),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()