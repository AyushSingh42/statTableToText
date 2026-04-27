import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the north region have a customer satisfaction rating of 4.3 or higher."""
    north = df[df["region"] == "north"]
    condition = north["customer_satisfaction"] >= 4.3
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores have satisfaction >= 4.3."
    else:
        viol = north[~condition]
        expl = f"{len(viol)} north stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the south region, then its average basket size is between 50 and 57."""
    south = df[df["region"] == "south"]
    condition = south["avg_basket_size"].between(50, 57, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores have avg basket size between 50 and 57."
    else:
        viol = south[~condition]
        expl = f"{len(viol)} south stores violate the rule (sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the west region with a staff count of 24 and a customer satisfaction rating of 3.7."""
    exists = df[(df["region"] == "west") & (df["staff_count"] == 24) & (df["customer_satisfaction"] == 3.7)]
    truth = not exists.empty
    if truth:
        expl = f"Found {len(exists)} matching west store(s)."
    else:
        expl = "No matching west store found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all stores with monthly sales greater than 140k, their transactions are greater than 1900."""
    high_sales = df[df["monthly_sales_k"] > 140]
    condition = high_sales["transactions"] > 1900
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high-sales stores have transactions > 1900."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} high-sales stores violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with a staff count of 21 or more have a customer satisfaction rating of 4.2 or higher."""
    staff_21 = df[df["staff_count"] >= 21]
    condition = staff_21["customer_satisfaction"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(staff_21)} stores with staff >= 21 have satisfaction >= 4.2."
    else:
        viol = staff_21[~condition]
        expl = f"{len(viol)} stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a store is in the east region, then its average basket size is between 49 and 67."""
    east = df[df["region"] == "east"]
    condition = east["avg_basket_size"].between(49, 67, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have avg basket size between 49 and 67."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east stores violate the rule (sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most stores in the table have a monthly sales figure between 100k and 160k."""
    between = df["monthly_sales_k"].between(100, 160, inclusive="both")
    truth = between.sum() > len(df) / 2
    if truth:
        expl = f"{between.sum()} out of {len(df)} stores have sales between 100k and 160k."
    else:
        expl = f"Only {between.sum()} out of {len(df)} stores have sales between 100k and 160k."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one store in the north region with a staff count of 18 and a customer satisfaction rating of 4.6."""
    exists = df[(df["region"] == "north") & (df["staff_count"] == 18) & (df["customer_satisfaction"] == 4.6)]
    truth = not exists.empty
    if truth:
        expl = f"Found {len(exists)} matching north store(s)."
    else:
        expl = "No matching north store found."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. For all stores with transactions greater than 2200, their average basket size is between 56 and 67."""
    high_trans = df[df["transactions"] > 2200]
    condition = high_trans["avg_basket_size"].between(56, 67, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_trans)} high-transaction stores have avg basket size between 56 and 67."
    else:
        viol = high_trans[~condition]
        expl = f"{len(viol)} high-transaction stores violate the rule (sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All stores with a customer satisfaction rating of 4.5 or higher have a staff count of 11 or more."""
    high_sat = df[df["customer_satisfaction"] >= 4.5]
    condition = high_sat["staff_count"] >= 11
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sat)} high-satisfaction stores have staff >= 11."
    else:
        viol = high_sat[~condition]
        expl = f"{len(viol)} stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a store is in the west region, then its monthly sales are between 80k and 150k."""
    west = df[df["region"] == "west"]
    condition = west["monthly_sales_k"].between(80, 150, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores have sales between 80k and 150k."
    else:
        viol = west[~condition]
        expl = f"{len(viol)} west stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. There exists at least one store in the south region with a staff count of 13 and a customer satisfaction rating of 4.0."""
    exists = df[(df["region"] == "south") & (df["staff_count"] == 13) & (df["customer_satisfaction"] == 4.0)]
    truth = not exists.empty
    if truth:
        expl = f"Found {len(exists)} matching south store(s)."
    else:
        expl = "No matching south store found."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. For all stores with an average basket size greater than 60, their transactions are greater than 1500."""
    high_basket = df[df["avg_basket_size"] > 60]
    condition = high_basket["transactions"] > 1500
    truth = condition.all()
    if truth:
        expl = f"All {len(high_basket)} high-basket stores have transactions > 1500."
    else:
        viol = high_basket[~condition]
        expl = f"{len(viol)} high-basket stores violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Most stores in the table have a staff count of 18 or less."""
    condition = df["staff_count"] <= 18
    truth = condition.sum() > len(df) / 2
    if truth:
        expl = f"{condition.sum()} out of {len(df)} stores have staff <= 18."
    else:
        expl = f"Only {condition.sum()} out of {len(df)} stores have staff <= 18."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All stores with a customer satisfaction rating of 3.7 or lower have a staff count of 24 or more."""
    low_sat = df[df["customer_satisfaction"] <= 3.7]
    condition = low_sat["staff_count"] >= 24
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sat)} low-satisfaction stores have staff >= 24."
    else:
        viol = low_sat[~condition]
        expl = f"{len(viol)} stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a store is in the east region, then its transactions are greater than 1500."""
    east = df[df["region"] == "east"]
    condition = east["transactions"] > 1500
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have transactions > 1500."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east stores violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. There exists at least one store in the north region with a monthly sales figure of 82.5k and a customer satisfaction rating of 4.6."""
    exists = df[(df["region"] == "north") & (df["monthly_sales_k"] == 82.5) & (df["customer_satisfaction"] == 4.6)]
    truth = not exists.empty
    if truth:
        expl = f"Found {len(exists)} matching north store(s)."
    else:
        expl = "No matching north store found."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_12.csv")

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