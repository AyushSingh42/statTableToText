import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the east region have monthly sales greater than $119k."""
    east = df[df["region"] == "east"]
    condition = east["monthly_sales_k"] > 119
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have monthly sales > 119k."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the north region, then its average basket size is less than $67."""
    north = df[df["region"] == "north"]
    condition = north["avg_basket_size"] < 67
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores have avg basket size < 67."
    else:
        viol = north[~condition]
        expl = f"{len(viol)} north store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the west region with a staff count greater than 19."""
    west = df[df["region"] == "west"]
    exists = not west[west["staff_count"] > 19].empty
    if exists:
        expl = "At least one west store has staff count > 19."
    else:
        expl = "No west store has staff count > 19."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with customer satisfaction greater than 4.5 have monthly sales greater than $90k."""
    high_cs = df[df["customer_satisfaction"] > 4.5]
    condition = high_cs["monthly_sales_k"] > 90
    truth = condition.all()
    if truth:
        expl = f"All {len(high_cs)} high CS stores have monthly sales > 90k."
    else:
        viol = high_cs[~condition]
        expl = f"{len(viol)} high CS store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store is in the south region, then its transactions are less than 2574."""
    south = df[df["region"] == "south"]
    condition = south["transactions"] < 2574
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores have transactions < 2574."
    else:
        viol = south[~condition]
        expl = f"{len(viol)} south store(s) violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most stores have an average basket size greater than $56."""
    total = len(df)
    count = (df["avg_basket_size"] > 56).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} stores have avg basket size > 56, which is a majority."
    else:
        expl = f"Only {count} out of {total} stores have avg basket size > 56."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with staff count greater than 16 have customer satisfaction greater than 4.3."""
    high_staff = df[df["staff_count"] > 16]
    condition = high_staff["customer_satisfaction"] > 4.3
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} high staff stores have CS > 4.3."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} high staff store(s) violate the rule (CS: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store is in the east region, then its staff count is less than 25."""
    east = df[df["region"] == "east"]
    condition = east["staff_count"] < 25
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have staff count < 25."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east store(s) violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the west region with a monthly sales less than $100k and customer satisfaction greater than 4.1."""
    west = df[df["region"] == "west"]
    exists = not west[(west["monthly_sales_k"] < 100) & (west["customer_satisfaction"] > 4.1)].empty
    if exists:
        expl = "At least one west store meets the criteria."
    else:
        expl = "No west store meets the criteria."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All stores with transactions greater than 2495 have an average basket size less than $67."""
    high_trans = df[df["transactions"] > 2495]
    condition = high_trans["avg_basket_size"] < 67
    truth = condition.all()
    if truth:
        expl = f"All {len(high_trans)} high transaction stores have avg basket size < 67."
    else:
        viol = high_trans[~condition]
        expl = f"{len(viol)} high transaction store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a store is in the south region and has a staff count greater than 20, then its customer satisfaction is greater than 4.2."""
    south_high_staff = df[(df["region"] == "south") & (df["staff_count"] > 20)]
    condition = south_high_staff["customer_satisfaction"] > 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(south_high_staff)} south high staff stores have CS > 4.2."
    else:
        viol = south_high_staff[~condition]
        expl = f"{len(viol)} south high staff store(s) violate the rule (CS: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most stores in the west region have a staff count less than 19."""
    west = df[df["region"] == "west"]
    total = len(west)
    count = (west["staff_count"] < 19).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} west stores have staff count < 19, which is a majority."
    else:
        expl = f"Only {count} out of {total} west stores have staff count < 19."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All stores with monthly sales greater than $151k have customer satisfaction greater than 4.5."""
    high_sales = df[df["monthly_sales_k"] > 151]
    condition = high_sales["customer_satisfaction"] > 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high sales stores have CS > 4.5."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} high sales store(s) violate the rule (CS: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a store is in the east region and has a staff count less than 16, then its monthly sales are greater than $119k."""
    east_low_staff = df[(df["region"] == "east") & (df["staff_count"] < 16)]
    condition = east_low_staff["monthly_sales_k"] > 119
    truth = condition.all()
    if truth:
        expl = f"All {len(east_low_staff)} east low staff stores have monthly sales > 119k."
    else:
        viol = east_low_staff[~condition]
        expl = f"{len(viol)} east low staff store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the south region with a staff count greater than 22 and customer satisfaction greater than 4.3."""
    south = df[df["region"] == "south"]
    exists = not south[(south["staff_count"] > 22) & (south["customer_satisfaction"] > 4.3)].empty
    if exists:
        expl = "At least one south store meets the criteria."
    else:
        expl = "No south store meets the criteria."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. All stores with average basket size greater than $62 have transactions greater than 1898."""
    high_basket = df[df["avg_basket_size"] > 62]
    condition = high_basket["transactions"] > 1898
    truth = condition.all()
    if truth:
        expl = f"All {len(high_basket)} high basket stores have transactions > 1898."
    else:
        viol = high_basket[~condition]
        expl = f"{len(viol)} high basket store(s) violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a store is in the west region and has a staff count greater than 14, then its customer satisfaction is greater than 4.1."""
    west_high_staff = df[(df["region"] == "west") & (df["staff_count"] > 14)]
    condition = west_high_staff["customer_satisfaction"] > 4.1
    truth = condition.all()
    if truth:
        expl = f"All {len(west_high_staff)} west high staff stores have CS > 4.1."
    else:
        viol = west_high_staff[~condition]
        expl = f"{len(viol)} west high staff store(s) violate the rule (CS: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_22.csv")

    # Convert numeric columns safely
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