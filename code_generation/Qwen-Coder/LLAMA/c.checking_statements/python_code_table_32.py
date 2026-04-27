import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the west region have monthly sales greater than $100k."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["monthly_sales_k"] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west region stores have monthly sales > $100k."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west region stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the south region, then its staff count is less than 15."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["staff_count"] < 15
    truth = condition.all()
    if truth:
        expl = f"All {len(south_stores)} south region stores have staff count < 15."
    else:
        viol = south_stores[~condition]
        expl = f"{len(viol)} south region stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the west region with a customer satisfaction rating greater than 4.5."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["customer_satisfaction"] > 4.5
    truth = condition.any()
    if truth:
        expl = f"At least one west region store has customer satisfaction > 4.5."
    else:
        expl = f"No west region store has customer satisfaction > 4.5."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with transactions greater than 2500 have an average basket size greater than 55."""
    high_trans_stores = df[df["transactions"] > 2500]
    condition = high_trans_stores["avg_basket_size"] > 55
    truth = condition.all()
    if truth:
        expl = f"All {len(high_trans_stores)} stores with transactions > 2500 have avg basket size > 55."
    else:
        viol = high_trans_stores[~condition]
        expl = f"{len(viol)} stores with transactions > 2500 violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store is in the north region, then its monthly sales are greater than $90k."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["monthly_sales_k"] > 90
    truth = condition.all()
    if truth:
        expl = f"All {len(north_stores)} north region stores have monthly sales > $90k."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north region stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most stores in the west region have a staff count greater than 15."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["staff_count"] > 15
    count_true = condition.sum()
    total = len(west_stores)
    truth = count_true > total / 2
    if truth:
        expl = f"More than half ({count_true}/{total}) of west region stores have staff count > 15."
    else:
        expl = f"Less than or equal to half ({count_true}/{total}) of west region stores have staff count > 15."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with a staff count greater than 18 have monthly sales greater than $140k."""
    high_staff_stores = df[df["staff_count"] > 18]
    condition = high_staff_stores["monthly_sales_k"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff_stores)} stores with staff count > 18 have monthly sales > $140k."
    else:
        viol = high_staff_stores[~condition]
        expl = f"{len(viol)} stores with staff count > 18 violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store is in the east region, then its transactions are less than 1700."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["transactions"] < 1700
    truth = condition.all()
    if truth:
        expl = f"All {len(east_stores)} east region stores have transactions < 1700."
    else:
        viol = east_stores[~condition]
        expl = f"{len(viol)} east region stores violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the west region with a customer satisfaction rating less than 4.0."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["customer_satisfaction"] < 4.0
    truth = condition.any()
    if truth:
        expl = f"At least one west region store has customer satisfaction < 4.0."
    else:
        expl = f"No west region store has customer satisfaction < 4.0."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All stores with an average basket size greater than 60 have monthly sales greater than $150k."""
    high_basket_stores = df[df["avg_basket_size"] > 60]
    condition = high_basket_stores["monthly_sales_k"] > 150
    truth = condition.all()
    if truth:
        expl = f"All {len(high_basket_stores)} stores with avg basket size > 60 have monthly sales > $150k."
    else:
        viol = high_basket_stores[~condition]
        expl = f"{len(viol)} stores with avg basket size > 60 violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a store is in the south region, then its monthly sales are less than $120k."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["monthly_sales_k"] < 120
    truth = condition.all()
    if truth:
        expl = f"All {len(south_stores)} south region stores have monthly sales < $120k."
    else:
        viol = south_stores[~condition]
        expl = f"{len(viol)} south region stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most stores in the west region have an average basket size greater than 50."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["avg_basket_size"] > 50
    count_true = condition.sum()
    total = len(west_stores)
    truth = count_true > total / 2
    if truth:
        expl = f"More than half ({count_true}/{total}) of west region stores have avg basket size > 50."
    else:
        expl = f"Less than or equal to half ({count_true}/{total}) of west region stores have avg basket size > 50."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All stores with monthly sales greater than $160k have a staff count greater than 15."""
    high_sales_stores = df[df["monthly_sales_k"] > 160]
    condition = high_sales_stores["staff_count"] > 15
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales_stores)} stores with monthly sales > $160k have staff count > 15."
    else:
        viol = high_sales_stores[~condition]
        expl = f"{len(viol)} stores with monthly sales > $160k violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a store is in the north region, then its staff count is less than 18."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["staff_count"] < 18
    truth = condition.all()
    if truth:
        expl = f"All {len(north_stores)} north region stores have staff count < 18."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north region stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the west region with a staff count greater than 20."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["staff_count"] > 20
    truth = condition.any()
    if truth:
        expl = f"At least one west region store has staff count > 20."
    else:
        expl = f"No west region store has staff count > 20."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All stores with transactions less than 1800 have a customer satisfaction rating greater than 4.2."""
    low_trans_stores = df[df["transactions"] < 1800]
    condition = low_trans_stores["customer_satisfaction"] > 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(low_trans_stores)} stores with transactions < 1800 have customer satisfaction > 4.2."
    else:
        viol = low_trans_stores[~condition]
        expl = f"{len(viol)} stores with transactions < 1800 violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a store is in the east region, then its average basket size is less than 50."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["avg_basket_size"] < 50
    truth = condition.all()
    if truth:
        expl = f"All {len(east_stores)} east region stores have avg basket size < 50."
    else:
        viol = east_stores[~condition]
        expl = f"{len(viol)} east region stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most stores in the west region have monthly sales greater than $120k."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["monthly_sales_k"] > 120
    count_true = condition.sum()
    total = len(west_stores)
    truth = count_true > total / 2
    if truth:
        expl = f"More than half ({count_true}/{total}) of west region stores have monthly sales > $120k."
    else:
        expl = f"Less than or equal to half ({count_true}/{total}) of west region stores have monthly sales > $120k."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_32.csv")

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