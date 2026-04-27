import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the north region have monthly sales greater than or equal to $110k."""
    north = df[df["region"] == "north"]
    condition = north["monthly_sales_k"] >= 110
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores meet the sales threshold."
    else:
        viol = north[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} north stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the west region, then its staff count is less than or equal to 25."""
    west = df[df["region"] == "west"]
    condition = west["staff_count"] <= 25
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores have staff_count <= 25."
    else:
        viol = west[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} west stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the east region with customer satisfaction less than 4.0."""
    east = df[df["region"] == "east"]
    condition = east["customer_satisfaction"] < 4.0
    truth = condition.any()
    if truth:
        viol = east[condition]
        ids = viol["store_id"].tolist()
        expl = f"Found {len(viol)} east stores with cs < 4.0 (store_ids: {', '.join(ids)})."
    else:
        expl = "No east store has customer satisfaction < 4.0."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all stores with transactions greater than 2500, their average basket size is less than or equal to 55."""
    high_tx = df[df["transactions"] > 2500]
    condition = high_tx["avg_basket_size"] <= 55
    truth = condition.all()
    if truth:
        expl = f"All {len(high_tx)} high-transaction stores have avg_basket_size <= 55."
    else:
        viol = high_tx[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} high-transaction stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with staff count greater than 20 have monthly sales greater than or equal to $120k."""
    high_staff = df[df["staff_count"] > 20]
    condition = high_staff["monthly_sales_k"] >= 120
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} high-staff stores have monthly_sales_k >= 120."
    else:
        viol = high_staff[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} high-staff stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a store is in the south region, then its average basket size is greater than 59."""
    south = df[df["region"] == "south"]
    condition = south["avg_basket_size"] > 59
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores have avg_basket_size > 59."
    else:
        viol = south[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} south stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most stores in the data have customer satisfaction greater than 4.0."""
    proportion = (df["customer_satisfaction"] > 4.0).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of stores have cs > 4.0."
    else:
        expl = f"Only {proportion*100:.1f}% of stores have cs > 4.0."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all stores with monthly sales less than $100k, their transactions are less than 2200."""
    low_sales = df[df["monthly_sales_k"] < 100]
    condition = low_sales["transactions"] < 2200
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sales)} low-sales stores have transactions < 2200."
    else:
        viol = low_sales[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} low-sales stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the west region with staff count less than 12."""
    west = df[df["region"] == "west"]
    condition = west["staff_count"] < 12
    truth = condition.any()
    if truth:
        viol = west[condition]
        ids = viol["store_id"].tolist()
        expl = f"Found {len(viol)} west stores with staff_count < 12 (store_ids: {', '.join(ids)})."
    else:
        expl = "No west store has staff_count < 12."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a store is in the north region, then its monthly sales are greater than or equal to $110k or its transactions are greater than 2000."""
    north = df[df["region"] == "north"]
    condition = (north["monthly_sales_k"] >= 110) | (north["transactions"] > 2000)
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores satisfy the condition."
    else:
        viol = north[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} north stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All stores with average basket size greater than 60 have staff count less than or equal to 12."""
    high_basket = df[df["avg_basket_size"] > 60]
    condition = high_basket["staff_count"] <= 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_basket)} high-basket stores have staff_count <= 12."
    else:
        viol = high_basket[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} high-basket stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all stores with customer satisfaction greater than 4.4, their monthly sales are greater than or equal to $140k."""
    high_cs = df[df["customer_satisfaction"] > 4.4]
    condition = high_cs["monthly_sales_k"] >= 140
    truth = condition.all()
    if truth:
        expl = f"All {len(high_cs)} high-cs stores have monthly_sales_k >= 140."
    else:
        viol = high_cs[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} high-cs stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a store is in the east region, then its transactions are greater than 2000 or its average basket size is greater than 54."""
    east = df[df["region"] == "east"]
    condition = (east["transactions"] > 2000) | (east["avg_basket_size"] > 54)
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores satisfy the condition."
    else:
        viol = east[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} east stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one store in the south region with customer satisfaction less than 4.0."""
    south = df[df["region"] == "south"]
    condition = south["customer_satisfaction"] < 4.0
    truth = condition.any()
    if truth:
        viol = south[condition]
        ids = viol["store_id"].tolist()
        expl = f"Found {len(viol)} south stores with cs < 4.0 (store_ids: {', '.join(ids)})."
    else:
        expl = "No south store has customer satisfaction < 4.0."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most stores in the data have staff count greater than 10."""
    proportion = (df["staff_count"] > 10).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of stores have staff_count > 10."
    else:
        expl = f"Only {proportion*100:.1f}% of stores have staff_count > 10."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. For all stores with monthly sales greater than $160k, their transactions are greater than 2500."""
    high_sales = df[df["monthly_sales_k"] > 160]
    condition = high_sales["transactions"] > 2500
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high-sales stores have transactions > 2500."
    else:
        viol = high_sales[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} high-sales stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a store is in the west region, then its monthly sales are greater than or equal to $110k or its average basket size is greater than 51."""
    west = df[df["region"] == "west"]
    condition = (west["monthly_sales_k"] >= 110) | (west["avg_basket_size"] > 51)
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores satisfy the condition."
    else:
        viol = west[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} west stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All stores with transactions less than 2000 have monthly sales less than $120k."""
    low_tx = df[df["transactions"] < 2000]
    condition = low_tx["monthly_sales_k"] < 120
    truth = condition.all()
    if truth:
        expl = f"All {len(low_tx)} low-transaction stores have monthly_sales_k < 120."
    else:
        viol = low_tx[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} low-transaction stores violate the rule (store_ids: {', '.join(ids)})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. There exists at least one store in the north region with customer satisfaction less than 4.0."""
    north = df[df["region"] == "north"]
    condition = north["customer_satisfaction"] < 4.0
    truth = condition.any()
    if truth:
        viol = north[condition]
        ids = viol["store_id"].tolist()
        expl = f"Found {len(viol)} north stores with cs < 4.0 (store_ids: {', '.join(ids)})."
    else:
        expl = "No north store has customer satisfaction < 4.0."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_72.csv")

    # Convert numeric columns
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
        (19, stmt_19),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()