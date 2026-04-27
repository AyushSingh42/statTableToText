import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the north region have monthly sales less than 180 thousand."""
    north = df[df["region"] == "north"]
    condition = north["monthly_sales_k"] < 180
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores have monthly sales < 180k."
    else:
        viol = north[~condition]
        expl = f"{len(viol)} north store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the south region, then its customer satisfaction is less than or equal to 4.5."""
    south = df[df["region"] == "south"]
    condition = south["customer_satisfaction"] <= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores have customer satisfaction ≤ 4.5."
    else:
        viol = south[~condition]
        expl = f"{len(viol)} south store(s) violate the rule (customer satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the west region with a staff count greater than 20."""
    west = df[df["region"] == "west"]
    exists = ((west["staff_count"] > 20).any())
    truth = exists
    if truth:
        count = west[west["staff_count"] > 20].shape[0]
        expl = f"Found {count} west store(s) with staff count > 20."
    else:
        expl = "No west store has staff count > 20."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with a staff count greater than 15 have a customer satisfaction less than or equal to 4.5."""
    high_staff = df[df["staff_count"] > 15]
    condition = high_staff["customer_satisfaction"] <= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} stores with staff > 15 have customer satisfaction ≤ 4.5."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} store(s) violate the rule (customer satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store has a monthly sales greater than 160 thousand, then its transactions are greater than 2400."""
    high_sales = df[df["monthly_sales_k"] > 160]
    condition = high_sales["transactions"] > 2400
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} stores with monthly sales > 160k have transactions > 2400."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} store(s) violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most stores have an average basket size between 50 and 65."""
    condition = df["avg_basket_size"].between(50, 65, inclusive="both")
    majority = condition.sum() > 0.5 * len(df)
    truth = majority
    if truth:
        expl = f"{condition.sum()} out of {len(df)} stores have avg basket size between 50 and 65."
    else:
        expl = f"Only {condition.sum()} out of {len(df)} stores have avg basket size between 50 and 65."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with a customer satisfaction greater than 4.2 have a staff count greater than 10."""
    high_cs = df[df["customer_satisfaction"] > 4.2]
    condition = high_cs["staff_count"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(high_cs)} stores with customer satisfaction > 4.2 have staff count > 10."
    else:
        viol = high_cs[~condition]
        expl = f"{len(viol)} store(s) violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store is in the east region, then its monthly sales are less than 180 thousand."""
    east = df[df["region"] == "east"]
    condition = east["monthly_sales_k"] < 180
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have monthly sales < 180k."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the west region with a customer satisfaction greater than 4.5."""
    west = df[df["region"] == "west"]
    exists = ((west["customer_satisfaction"] > 4.5).any())
    truth = exists
    if truth:
        count = west[west["customer_satisfaction"] > 4.5].shape[0]
        expl = f"Found {count} west store(s) with customer satisfaction > 4.5."
    else:
        expl = "No west store has customer satisfaction > 4.5."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All stores with a transactions greater than 2500 have a staff count greater than 12."""
    high_trans = df[df["transactions"] > 2500]
    condition = high_trans["staff_count"] > 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_trans)} stores with transactions > 2500 have staff count > 12."
    else:
        viol = high_trans[~condition]
        expl = f"{len(viol)} store(s) violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a store has a staff count greater than 18, then its customer satisfaction is less than or equal to 4.5."""
    high_staff = df[df["staff_count"] > 18]
    condition = high_staff["customer_satisfaction"] <= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} stores with staff count > 18 have customer satisfaction ≤ 4.5."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} store(s) violate the rule (customer satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most stores in the south region have a monthly sales greater than 100 thousand."""
    south = df[df["region"] == "south"]
    condition = south["monthly_sales_k"] > 100
    majority = condition.sum() > 0.5 * len(south)
    truth = majority
    if truth:
        expl = f"{condition.sum()} out of {len(south)} south stores have monthly sales > 100k."
    else:
        expl = f"Only {condition.sum()} out of {len(south)} south stores have monthly sales > 100k."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All stores with a monthly sales less than 120 thousand have a staff count less than 16."""
    low_sales = df[df["monthly_sales_k"] < 120]
    condition = low_sales["staff_count"] < 16
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sales)} stores with monthly sales < 120k have staff count < 16."
    else:
        viol = low_sales[~condition]
        expl = f"{len(viol)} store(s) violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a store is in the north region, then its transactions are greater than 2000."""
    north = df[df["region"] == "north"]
    condition = north["transactions"] > 2000
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores have transactions > 2000."
    else:
        viol = north[~condition]
        expl = f"{len(viol)} north store(s) violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the south region with a staff count greater than 20."""
    south = df[df["region"] == "south"]
    exists = ((south["staff_count"] > 20).any())
    truth = exists
    if truth:
        count = south[south["staff_count"] > 20].shape[0]
        expl = f"Found {count} south store(s) with staff count > 20."
    else:
        expl = "No south store has staff count > 20."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All stores with a customer satisfaction less than 4.0 have a staff count greater than 12."""
    low_cs = df[df["customer_satisfaction"] < 4.0]
    condition = low_cs["staff_count"] > 12
    truth = condition.all()
    if truth:
        expl = f"All {len(low_cs)} stores with customer satisfaction < 4.0 have staff count > 12."
    else:
        viol = low_cs[~condition]
        expl = f"{len(viol)} store(s) violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a store has a transactions less than 2200, then its average basket size is greater than 60."""
    low_trans = df[df["transactions"] < 2200]
    condition = low_trans["avg_basket_size"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(low_trans)} stores with transactions < 2200 have avg basket size > 60."
    else:
        viol = low_trans[~condition]
        expl = f"{len(viol)} store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most stores in the west region have a monthly sales greater than 120 thousand."""
    west = df[df["region"] == "west"]
    condition = west["monthly_sales_k"] > 120
    majority = condition.sum() > 0.5 * len(west)
    truth = majority
    if truth:
        expl = f"{condition.sum()} out of {len(west)} west stores have monthly sales > 120k."
    else:
        expl = f"Only {condition.sum()} out of {len(west)} west stores have monthly sales > 120k."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_82.csv")

    # Convert numeric columns safely
    for col in ["monthly_sales_k", "transactions", "avg_basket_size", "staff_count", "customer_satisfaction"]:
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