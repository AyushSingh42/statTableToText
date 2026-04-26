import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the west region have monthly sales greater than $100k, except for store B062001."""
    west_stores = df[df["region"] == "west"]
    condition = (west_stores["monthly_sales_k"] > 100) | (west_stores["store_id"] == "B062001")
    truth = condition.all()
    if truth:
        expl = f"All west region stores meet the criteria (except B062001)."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All stores with staff count greater than 20 have customer satisfaction greater than 3.9."""
    high_staff = df[df["staff_count"] > 20]
    condition = high_staff["customer_satisfaction"] > 3.9
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} high-staff stores have satisfaction > 3.9."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} high-staff stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a store is in the east region, then its average basket size is greater than 60."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["avg_basket_size"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(east_stores)} east stores have avg basket > 60."
    else:
        viol = east_stores[~condition]
        expl = f"{len(viol)} east stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one store in the south region with transactions greater than 2500."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["transactions"] > 2500
    truth = condition.any()
    if truth:
        expl = f"At least one south store has transactions > 2500."
    else:
        expl = f"No south stores have transactions > 2500."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with monthly sales greater than $150k have staff count greater than 15."""
    high_sales = df[df["monthly_sales_k"] > 150]
    condition = high_sales["staff_count"] > 15
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high-sales stores have staff > 15."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} high-sales stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a store is in the north region, then its average basket size is less than 60, except for store B062014."""
    north_stores = df[df["region"] == "north"]
    condition = (north_stores["avg_basket_size"] < 60) | (north_stores["store_id"] == "B062014")
    truth = condition.all()
    if truth:
        expl = f"All north stores meet the criteria (except B062014)."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most stores in the west region have customer satisfaction less than 4.1."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["customer_satisfaction"] < 4.1
    satisfied_count = condition.sum()
    total_count = len(west_stores)
    truth = satisfied_count > total_count / 2
    if truth:
        expl = f"More than half ({satisfied_count}/{total_count}) of west stores have satisfaction < 4.1."
    else:
        expl = f"Less than half ({satisfied_count}/{total_count}) of west stores have satisfaction < 4.1."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All stores with staff count less than 15 have monthly sales less than $120k."""
    low_staff = df[df["staff_count"] < 15]
    condition = low_staff["monthly_sales_k"] < 120
    truth = condition.all()
    if truth:
        expl = f"All {len(low_staff)} low-staff stores have sales < 120k."
    else:
        viol = low_staff[~condition]
        expl = f"{len(viol)} low-staff stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a store has transactions greater than 2000, then its average basket size is greater than 55."""
    high_trans = df[df["transactions"] > 2000]
    condition = high_trans["avg_basket_size"] > 55
    truth = condition.all()
    if truth:
        expl = f"All {len(high_trans)} high-transaction stores have avg basket > 55."
    else:
        viol = high_trans[~condition]
        expl = f"{len(viol)} high-transaction stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one store in the east region with customer satisfaction greater than 4.1."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["customer_satisfaction"] > 4.1
    truth = condition.any()
    if truth:
        expl = f"At least one east store has satisfaction > 4.1."
    else:
        expl = f"No east stores have satisfaction > 4.1."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All stores with monthly sales less than $100k have staff count less than 20."""
    low_sales = df[df["monthly_sales_k"] < 100]
    condition = low_sales["staff_count"] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sales)} low-sales stores have staff < 20."
    else:
        viol = low_sales[~condition]
        expl = f"{len(viol)} low-sales stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a store is in the south region, then its monthly sales are greater than $100k, except for store B062009."""
    south_stores = df[df["region"] == "south"]
    condition = (south_stores["monthly_sales_k"] > 100) | (south_stores["store_id"] == "B062009")
    truth = condition.all()
    if truth:
        expl = f"All south stores meet the criteria (except B062009)."
    else:
        viol = south_stores[~condition]
        expl = f"{len(viol)} south stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most stores in the east region have monthly sales greater than $150k."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["monthly_sales_k"] > 150
    satisfied_count = condition.sum()
    total_count = len(east_stores)
    truth = satisfied_count > total_count / 2
    if truth:
        expl = f"More than half ({satisfied_count}/{total_count}) of east stores have sales > 150k."
    else:
        expl = f"Less than half ({satisfied_count}/{total_count}) of east stores have sales > 150k."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All stores with average basket size greater than 65 have customer satisfaction less than 4.0."""
    high_basket = df[df["avg_basket_size"] > 65]
    condition = high_basket["customer_satisfaction"] < 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(high_basket)} high-basket stores have satisfaction < 4.0."
    else:
        viol = high_basket[~condition]
        expl = f"{len(viol)} high-basket stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a store has staff count greater than 20, then its monthly sales are greater than $120k."""
    high_staff = df[df["staff_count"] > 20]
    condition = high_staff["monthly_sales_k"] > 120
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} high-staff stores have sales > 120k."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} high-staff stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one store in the north region with customer satisfaction greater than 4.7."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["customer_satisfaction"] > 4.7
    truth = condition.any()
    if truth:
        expl = f"At least one north store has satisfaction > 4.7."
    else:
        expl = f"No north stores have satisfaction > 4.7."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All stores with transactions less than 2000 have monthly sales less than $120k."""
    low_trans = df[df["transactions"] < 2000]
    condition = low_trans["monthly_sales_k"] < 120
    truth = condition.all()
    if truth:
        expl = f"All {len(low_trans)} low-transaction stores have sales < 120k."
    else:
        viol = low_trans[~condition]
        expl = f"{len(viol)} low-transaction stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a store is in the west region, then its staff count is greater than 10, except for store B062005."""
    west_stores = df[df["region"] == "west"]
    condition = (west_stores["staff_count"] > 10) | (west_stores["store_id"] == "B062005")
    truth = condition.all()
    if truth:
        expl = f"All west stores meet the criteria (except B062005)."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_62.csv")

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
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
        (18, stmt_18)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()