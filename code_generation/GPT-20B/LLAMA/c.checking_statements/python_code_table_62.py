import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the west region have monthly sales greater than $100k, except for store B062001."""
    west = df[(df["region"] == "west") & (df["store_id"]!= "B062001")]
    condition = west["monthly_sales_k"] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores (excluding B062001) have sales > 100k."
    else:
        viol = west[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} west store(s) violate the rule: {ids}."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All stores with staff count greater than 20 have customer satisfaction greater than 3.9."""
    staff_gt20 = df[df["staff_count"] > 20]
    condition = staff_gt20["customer_satisfaction"] > 3.9
    truth = condition.all()
    if truth:
        expl = f"All {len(staff_gt20)} stores with staff > 20 have CS > 3.9."
    else:
        viol = staff_gt20[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} store(s) violate the rule: {ids}."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a store is in the east region, then its average basket size is greater than 60."""
    east = df[df["region"] == "east"]
    condition = east["avg_basket_size"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have avg basket size > 60."
    else:
        viol = east[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} east store(s) violate the rule: {ids}."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one store in the south region with transactions greater than 2500."""
    south = df[df["region"] == "south"]
    exists = (south["transactions"] > 2500).any()
    if exists:
        ids = south[south["transactions"] > 2500]["store_id"].tolist()
        expl = f"Store(s) {ids} satisfy the condition."
    else:
        expl = "No south store has transactions > 2500."
    return exists, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with monthly sales greater than $150k have staff count greater than 15."""
    sales_gt150 = df[df["monthly_sales_k"] > 150]
    condition = sales_gt150["staff_count"] > 15
    truth = condition.all()
    if truth:
        expl = f"All {len(sales_gt150)} stores with sales > 150k have staff > 15."
    else:
        viol = sales_gt150[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} store(s) violate the rule: {ids}."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a store is in the north region, then its average basket size is less than 60, except for store B062014."""
    north = df[(df["region"] == "north") & (df["store_id"]!= "B062014")]
    condition = north["avg_basket_size"] < 60
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores (excluding B062014) have avg basket size < 60."
    else:
        viol = north[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} north store(s) violate the rule: {ids}."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most stores in the west region have customer satisfaction less than 4.1."""
    west = df[df["region"] == "west"]
    count = len(west)
    if count == 0:
        truth = True
        expl = "No west stores to evaluate."
    else:
        satisfied = (west["customer_satisfaction"] < 4.1).sum()
        truth = satisfied > count / 2
        if truth:
            expl = f"{satisfied}/{count} west stores have CS < 4.1 (majority)."
        else:
            expl = f"{satisfied}/{count} west stores have CS < 4.1 (not majority)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All stores with monthly sales less than $100k have staff count less than 20."""
    sales_lt100 = df[df["monthly_sales_k"] < 100]
    condition = sales_lt100["staff_count"] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(sales_lt100)} stores with sales < 100k have staff < 20."
    else:
        viol = sales_lt100[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} store(s) violate the rule: {ids}."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a store has transactions greater than 2000, then its average basket size is greater than 55."""
    trans_gt2000 = df[df["transactions"] > 2000]
    condition = trans_gt2000["avg_basket_size"] > 55
    truth = condition.all()
    if truth:
        expl = f"All {len(trans_gt2000)} stores with transactions > 2000 have avg basket size > 55."
    else:
        viol = trans_gt2000[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} store(s) violate the rule: {ids}."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one store in the east region with customer satisfaction greater than 4.1."""
    east = df[df["region"] == "east"]
    exists = (east["customer_satisfaction"] > 4.1).any()
    if exists:
        ids = east[east["customer_satisfaction"] > 4.1]["store_id"].tolist()
        expl = f"Store(s) {ids} satisfy the condition."
    else:
        expl = "No east store has customer satisfaction > 4.1."
    return exists, expl

def stmt_11(df: pd.DataFrame):
    """11. All stores with monthly sales less than $100k have staff count less than 20."""
    # Same as stmt_8
    return stmt_8(df)

def stmt_12(df: pd.DataFrame):
    """12. If a store is in the south region, then its monthly sales are greater than $100k, except for store B062009."""
    south = df[(df["region"] == "south") & (df["store_id"]!= "B062009")]
    condition = south["monthly_sales_k"] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores (excluding B062009) have sales > 100k."
    else:
        viol = south[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} south store(s) violate the rule: {ids}."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most stores in the east region have monthly sales greater than $150k."""
    east = df[df["region"] == "east"]
    count = len(east)
    if count == 0:
        truth = True
        expl = "No east stores to evaluate."
    else:
        satisfied = (east["monthly_sales_k"] > 150).sum()
        truth = satisfied > count / 2
        if truth:
            expl = f"{satisfied}/{count} east stores have sales > 150k (majority)."
        else:
            expl = f"{satisfied}/{count} east stores have sales > 150k (not majority)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All stores with average basket size greater than 65 have customer satisfaction less than 4.0."""
    basket_gt65 = df[df["avg_basket_size"] > 65]
    condition = basket_gt65["customer_satisfaction"] < 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(basket_gt65)} stores with basket size > 65 have CS < 4.0."
    else:
        viol = basket_gt65[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} store(s) violate the rule: {ids}."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a store has staff count greater than 20, then its monthly sales are greater than $120k."""
    staff_gt20 = df[df["staff_count"] > 20]
    condition = staff_gt20["monthly_sales_k"] > 120
    truth = condition.all()
    if truth:
        expl = f"All {len(staff_gt20)} stores with staff > 20 have sales > 120k."
    else:
        viol = staff_gt20[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} store(s) violate the rule: {ids}."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one store in the north region with customer satisfaction greater than 4.7."""
    north = df[df["region"] == "north"]
    exists = (north["customer_satisfaction"] > 4.7).any()
    if exists:
        ids = north[north["customer_satisfaction"] > 4.7]["store_id"].tolist()
        expl = f"Store(s) {ids} satisfy the condition."
    else:
        expl = "No north store has customer satisfaction > 4.7."
    return exists, expl

def stmt_17(df: pd.DataFrame):
    """17. All stores with transactions less than 2000 have monthly sales less than $120k."""
    trans_lt2000 = df[df["transactions"] < 2000]
    condition = trans_lt2000["monthly_sales_k"] < 120
    truth = condition.all()
    if truth:
        expl = f"All {len(trans_lt2000)} stores with transactions < 2000 have sales < 120k."
    else:
        viol = trans_lt2000[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} store(s) violate the rule: {ids}."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a store is in the west region, then its staff count is greater than 10, except for store B062005."""
    west = df[(df["region"] == "west") & (df["store_id"]!= "B062005")]
    condition = west["staff_count"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores (excluding B062005) have staff > 10."
    else:
        viol = west[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} west store(s) violate the rule: {ids}."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_62.csv")

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