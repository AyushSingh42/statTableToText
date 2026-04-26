import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the north region have a customer satisfaction rating of 4.2 or higher."""
    north_stores = df[df["region"] == "north"]
    if north_stores.empty:
        truth = True
        expl = "No stores in the north region."
    else:
        condition = north_stores["customer_satisfaction"] >= 4.2
        truth = condition.all()
        if truth:
            expl = f"All {len(north_stores)} stores in the north region have a customer satisfaction rating of 4.2 or higher."
        else:
            viol = north_stores[~condition]
            expl = f"{len(viol)} stores in the north region violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the west region, then its average basket size is less than 60."""
    west_stores = df[df["region"] == "west"]
    if west_stores.empty:
        truth = True
        expl = "No stores in the west region."
    else:
        condition = west_stores["avg_basket_size"] < 60
        truth = condition.all()
        if truth:
            expl = f"All {len(west_stores)} stores in the west region have an average basket size less than 60."
        else:
            viol = west_stores[~condition]
            expl = f"{len(viol)} stores in the west region violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the south region with a staff count greater than 20."""
    south_stores = df[df["region"] == "south"]
    if south_stores.empty:
        truth = False
        expl = "No stores in the south region."
    else:
        condition = south_stores["staff_count"] > 20
        truth = condition.any()
        if truth:
            expl = f"At least one store in the south region has a staff count greater than 20."
        else:
            expl = f"No stores in the south region have a staff count greater than 20."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all stores with monthly sales greater than 150k, their transactions are greater than 1800."""
    high_sales = df[df["monthly_sales_k"] > 150]
    if high_sales.empty:
        truth = True
        expl = "No stores with monthly sales greater than 150k."
    else:
        condition = high_sales["transactions"] > 1800
        truth = condition.all()
        if truth:
            expl = f"All {len(high_sales)} stores with monthly sales greater than 150k have transactions greater than 1800."
        else:
            viol = high_sales[~condition]
            expl = f"{len(viol)} stores with monthly sales greater than 150k violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with a staff count greater than 20 have a customer satisfaction rating of 4.0 or higher."""
    high_staff = df[df["staff_count"] > 20]
    if high_staff.empty:
        truth = True
        expl = "No stores with staff count greater than 20."
    else:
        condition = high_staff["customer_satisfaction"] >= 4.0
        truth = condition.all()
        if truth:
            expl = f"All {len(high_staff)} stores with staff count greater than 20 have a customer satisfaction rating of 4.0 or higher."
        else:
            viol = high_staff[~condition]
            expl = f"{len(viol)} stores with staff count greater than 20 violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a store is in the east region, then its average basket size is greater than 55."""
    east_stores = df[df["region"] == "east"]
    if east_stores.empty:
        truth = True
        expl = "No stores in the east region."
    else:
        condition = east_stores["avg_basket_size"] > 55
        truth = condition.all()
        if truth:
            expl = f"All {len(east_stores)} stores in the east region have an average basket size greater than 55."
        else:
            viol = east_stores[~condition]
            expl = f"{len(viol)} stores in the east region violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most stores in the data have a monthly sales figure less than 170k."""
    total_stores = len(df)
    low_sales = df[df["monthly_sales_k"] < 170]
    count_low = len(low_sales)
    truth = count_low > total_stores / 2
    if truth:
        expl = f"Most stores ({count_low}/{total_stores}) have a monthly sales figure less than 170k."
    else:
        expl = f"Only {count_low}/{total_stores} stores have a monthly sales figure less than 170k."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all stores with transactions greater than 2200, their average basket size is less than 60."""
    high_transactions = df[df["transactions"] > 2200]
    if high_transactions.empty:
        truth = True
        expl = "No stores with transactions greater than 2200."
    else:
        condition = high_transactions["avg_basket_size"] < 60
        truth = condition.all()
        if truth:
            expl = f"All {len(high_transactions)} stores with transactions greater than 2200 have an average basket size less than 60."
        else:
            viol = high_transactions[~condition]
            expl = f"{len(viol)} stores with transactions greater than 2200 violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the north region with a monthly sales figure less than 100k."""
    north_stores = df[df["region"] == "north"]
    if north_stores.empty:
        truth = False
        expl = "No stores in the north region."
    else:
        condition = north_stores["monthly_sales_k"] < 100
        truth = condition.any()
        if truth:
            expl = f"At least one store in the north region has a monthly sales figure less than 100k."
        else:
            expl = f"No stores in the north region have a monthly sales figure less than 100k."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a store is in the south region, then its customer satisfaction rating is 4.1 or higher."""
    south_stores = df[df["region"] == "south"]
    if south_stores.empty:
        truth = True
        expl = "No stores in the south region."
    else:
        condition = south_stores["customer_satisfaction"] >= 4.1
        truth = condition.all()
        if truth:
            expl = f"All {len(south_stores)} stores in the south region have a customer satisfaction rating of 4.1 or higher."
        else:
            viol = south_stores[~condition]
            expl = f"{len(viol)} stores in the south region violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All stores with a customer satisfaction rating of 4.7 have a staff count of 12 or greater."""
    high_satisfaction = df[df["customer_satisfaction"] == 4.7]
    if high_satisfaction.empty:
        truth = True
        expl = "No stores with customer satisfaction rating of 4.7."
    else:
        condition = high_satisfaction["staff_count"] >= 12
        truth = condition.all()
        if truth:
            expl = f"All {len(high_satisfaction)} stores with customer satisfaction rating of 4.7 have a staff count of 12 or greater."
        else:
            viol = high_satisfaction[~condition]
            expl = f"{len(viol)} stores with customer satisfaction rating of 4.7 violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all stores with an average basket size greater than 65, their monthly sales are less than 140k."""
    high_basket = df[df["avg_basket_size"] > 65]
    if high_basket.empty:
        truth = True
        expl = "No stores with average basket size greater than 65."
    else:
        condition = high_basket["monthly_sales_k"] < 140
        truth = condition.all()
        if truth:
            expl = f"All {len(high_basket)} stores with average basket size greater than 65 have monthly sales less than 140k."
        else:
            viol = high_basket[~condition]
            expl = f"{len(viol)} stores with average basket size greater than 65 violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a store has a staff count of 25 or greater, then its customer satisfaction rating is 4.2 or higher."""
    high_staff = df[df["staff_count"] >= 25]
    if high_staff.empty:
        truth = True
        expl = "No stores with staff count of 25 or greater."
    else:
        condition = high_staff["customer_satisfaction"] >= 4.2
        truth = condition.all()
        if truth:
            expl = f"All {len(high_staff)} stores with staff count of 25 or greater have a customer satisfaction rating of 4.2 or higher."
        else:
            viol = high_staff[~condition]
            expl = f"{len(viol)} stores with staff count of 25 or greater violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Most stores in the data have a staff count less than 20."""
    total_stores = len(df)
    low_staff = df[df["staff_count"] < 20]
    count_low = len(low_staff)
    truth = count_low > total_stores / 2
    if truth:
        expl = f"Most stores ({count_low}/{total_stores}) have a staff count less than 20."
    else:
        expl = f"Only {count_low}/{total_stores} stores have a staff count less than 20."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the west region with a monthly sales figure greater than 160k."""
    west_stores = df[df["region"] == "west"]
    if west_stores.empty:
        truth = False
        expl = "No stores in the west region."
    else:
        condition = west_stores["monthly_sales_k"] > 160
        truth = condition.any()
        if truth:
            expl = f"At least one store in the west region has a monthly sales figure greater than 160k."
        else:
            expl = f"No stores in the west region have a monthly sales figure greater than 160k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. For all stores with transactions less than 2000, their average basket size is greater than 55."""
    low_transactions = df[df["transactions"] < 2000]
    if low_transactions.empty:
        truth = True
        expl = "No stores with transactions less than 2000."
    else:
        condition = low_transactions["avg_basket_size"] > 55
        truth = condition.all()
        if truth:
            expl = f"All {len(low_transactions)} stores with transactions less than 2000 have an average basket size greater than 55."
        else:
            viol = low_transactions[~condition]
            expl = f"{len(viol)} stores with transactions less than 2000 violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All stores with a customer satisfaction rating of 3.7 have a staff count of 17 or less."""
    low_satisfaction = df[df["customer_satisfaction"] == 3.7]
    if low_satisfaction.empty:
        truth = True
        expl = "No stores with customer satisfaction rating of 3.7."
    else:
        condition = low_satisfaction["staff_count"] <= 17
        truth = condition.all()
        if truth:
            expl = f"All {len(low_satisfaction)} stores with customer satisfaction rating of 3.7 have a staff count of 17 or less."
        else:
            viol = low_satisfaction[~condition]
            expl = f"{len(viol)} stores with customer satisfaction rating of 3.7 violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a store is in the east region, then its transactions are greater than 1600."""
    east_stores = df[df["region"] == "east"]
    if east_stores.empty:
        truth = True
        expl = "No stores in the east region."
    else:
        condition = east_stores["transactions"] > 1600
        truth = condition.all()
        if truth:
            expl = f"All {len(east_stores)} stores in the east region have transactions greater than 1600."
        else:
            viol = east_stores[~condition]
            expl = f"{len(viol)} stores in the east region violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. For all stores with a monthly sales figure greater than 120k, their staff count is greater than 10."""
    high_sales = df[df["monthly_sales_k"] > 120]
    if high_sales.empty:
        truth = True
        expl = "No stores with monthly sales greater than 120k."
    else:
        condition = high_sales["staff_count"] > 10
        truth = condition.all()
        if truth:
            expl = f"All {len(high_sales)} stores with monthly sales greater than 120k have a staff count greater than 10."
        else:
            viol = high_sales[~condition]
            expl = f"{len(viol)} stores with monthly sales greater than 120k violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_2.csv")

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
        (18, stmt_18),
        (19, stmt_19)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()