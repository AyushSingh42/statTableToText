import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the east region have a customer satisfaction rating of 4.0 or higher."""
    east_stores = df[df["region"] == "east"]
    if east_stores.empty:
        truth = True
        expl = "No stores in the east region."
    else:
        condition = east_stores["customer_satisfaction"] >= 4.0
        truth = condition.all()
        if truth:
            expl = f"All {len(east_stores)} east region stores have satisfaction >= 4.0."
        else:
            viol = east_stores[~condition]
            expl = f"{len(viol)} east region stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the south region, then its average basket size is greater than 60."""
    south_stores = df[df["region"] == "south"]
    if south_stores.empty:
        truth = True
        expl = "No stores in the south region."
    else:
        condition = south_stores["avg_basket_size"] > 60
        truth = condition.all()
        if truth:
            expl = f"All {len(south_stores)} south region stores have avg basket size > 60."
        else:
            viol = south_stores[~condition]
            expl = f"{len(viol)} south region stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the west region with a staff count of 20 or more."""
    west_stores = df[df["region"] == "west"]
    if west_stores.empty:
        truth = False
        expl = "No stores in the west region."
    else:
        condition = west_stores["staff_count"] >= 20
        truth = condition.any()
        if truth:
            found = west_stores[condition]
            expl = f"At least one west region store ({found.iloc[0]['store_id']}) has staff count >= 20."
        else:
            expl = f"No west region stores have staff count >= 20."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with a monthly sales value of $150k or more have a transaction count of 1800 or less."""
    high_sales = df[df["monthly_sales_k"] >= 150]
    if high_sales.empty:
        truth = True
        expl = "No stores with monthly sales >= 150k."
    else:
        condition = high_sales["transactions"] <= 1800
        truth = condition.all()
        if truth:
            expl = f"All {len(high_sales)} high sales stores have transactions <= 1800."
        else:
            viol = high_sales[~condition]
            expl = f"{len(viol)} high sales stores violate the rule (transaction counts: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store has a staff count of 15 or less, then its customer satisfaction rating is 4.5 or higher."""
    low_staff = df[df["staff_count"] <= 15]
    if low_staff.empty:
        truth = True
        expl = "No stores with staff count <= 15."
    else:
        condition = low_staff["customer_satisfaction"] >= 4.5
        truth = condition.all()
        if truth:
            expl = f"All {len(low_staff)} low staff stores have satisfaction >= 4.5."
        else:
            viol = low_staff[~condition]
            expl = f"{len(viol)} low staff stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most stores in the east region have a monthly sales value of $120k or less."""
    east_stores = df[df["region"] == "east"]
    if east_stores.empty:
        truth = True
        expl = "No stores in the east region."
    else:
        condition = east_stores["monthly_sales_k"] <= 120
        satisfied = condition.sum()
        total = len(east_stores)
        truth = satisfied > total / 2
        if truth:
            expl = f"Most east region stores ({satisfied}/{total}) have sales <= 120k."
        else:
            expl = f"Only {satisfied}/{total} east region stores have sales <= 120k, which is not'most'."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with an average basket size of 65 or more have a customer satisfaction rating of 4.0 or higher."""
    high_basket = df[df["avg_basket_size"] >= 65]
    if high_basket.empty:
        truth = True
        expl = "No stores with avg basket size >= 65."
    else:
        condition = high_basket["customer_satisfaction"] >= 4.0
        truth = condition.all()
        if truth:
            expl = f"All {len(high_basket)} high basket stores have satisfaction >= 4.0."
        else:
            viol = high_basket[~condition]
            expl = f"{len(viol)} high basket stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store is in the west region, then its staff count is 18 or more."""
    west_stores = df[df["region"] == "west"]
    if west_stores.empty:
        truth = True
        expl = "No stores in the west region."
    else:
        condition = west_stores["staff_count"] >= 18
        truth = condition.all()
        if truth:
            expl = f"All {len(west_stores)} west region stores have staff count >= 18."
        else:
            viol = west_stores[~condition]
            expl = f"{len(viol)} west region stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the east region with a transaction count of 2700 or more."""
    east_stores = df[df["region"] == "east"]
    if east_stores.empty:
        truth = False
        expl = "No stores in the east region."
    else:
        condition = east_stores["transactions"] >= 2700
        truth = condition.any()
        if truth:
            found = east_stores[condition]
            expl = f"At least one east region store ({found.iloc[0]['store_id']}) has transactions >= 2700."
        else:
            expl = f"No east region stores have transactions >= 2700."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All stores with a customer satisfaction rating of 4.8 or higher have an average basket size of 60 or more."""
    high_satisfaction = df[df["customer_satisfaction"] >= 4.8]
    if high_satisfaction.empty:
        truth = True
        expl = "No stores with satisfaction >= 4.8."
    else:
        condition = high_satisfaction["avg_basket_size"] >= 60
        truth = condition.all()
        if truth:
            expl = f"All {len(high_satisfaction)} high satisfaction stores have avg basket size >= 60."
        else:
            viol = high_satisfaction[~condition]
            expl = f"{len(viol)} high satisfaction stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a store has a monthly sales value of $100k or less, then its staff count is 15 or more."""
    low_sales = df[df["monthly_sales_k"] <= 100]
    if low_sales.empty:
        truth = True
        expl = "No stores with monthly sales <= 100k."
    else:
        condition = low_sales["staff_count"] >= 15
        truth = condition.all()
        if truth:
            expl = f"All {len(low_sales)} low sales stores have staff count >= 15."
        else:
            viol = low_sales[~condition]
            expl = f"{len(viol)} low sales stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most stores in the south region have a customer satisfaction rating of 4.7 or higher."""
    south_stores = df[df["region"] == "south"]
    if south_stores.empty:
        truth = True
        expl = "No stores in the south region."
    else:
        condition = south_stores["customer_satisfaction"] >= 4.7
        satisfied = condition.sum()
        total = len(south_stores)
        truth = satisfied > total / 2
        if truth:
            expl = f"Most south region stores ({satisfied}/{total}) have satisfaction >= 4.7."
        else:
            expl = f"Only {satisfied}/{total} south region stores have satisfaction >= 4.7, which is not'most'."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All stores with a staff count of 20 or more have a monthly sales value of $150k or less."""
    high_staff = df[df["staff_count"] >= 20]
    if high_staff.empty:
        truth = True
        expl = "No stores with staff count >= 20."
    else:
        condition = high_staff["monthly_sales_k"] <= 150
        truth = condition.all()
        if truth:
            expl = f"All {len(high_staff)} high staff stores have sales <= 150k."
        else:
            viol = high_staff[~condition]
            expl = f"{len(viol)} high staff stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a store is in the east region, then its average basket size is 55 or more."""
    east_stores = df[df["region"] == "east"]
    if east_stores.empty:
        truth = True
        expl = "No stores in the east region."
    else:
        condition = east_stores["avg_basket_size"] >= 55
        truth = condition.all()
        if truth:
            expl = f"All {len(east_stores)} east region stores have avg basket size >= 55."
        else:
            viol = east_stores[~condition]
            expl = f"{len(viol)} east region stores violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the west region with a customer satisfaction rating of 3.6 or less."""
    west_stores = df[df["region"] == "west"]
    if west_stores.empty:
        truth = False
        expl = "No stores in the west region."
    else:
        condition = west_stores["customer_satisfaction"] <= 3.6
        truth = condition.any()
        if truth:
            found = west_stores[condition]
            expl = f"At least one west region store ({found.iloc[0]['store_id']}) has satisfaction <= 3.6."
        else:
            expl = f"No west region stores have satisfaction <= 3.6."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All stores with a transaction count of 2000 or more have a staff count of 11 or more."""
    high_transactions = df[df["transactions"] >= 2000]
    if high_transactions.empty:
        truth = True
        expl = "No stores with transactions >= 2000."
    else:
        condition = high_transactions["staff_count"] >= 11
        truth = condition.all()
        if truth:
            expl = f"All {len(high_transactions)} high transaction stores have staff count >= 11."
        else:
            viol = high_transactions[~condition]
            expl = f"{len(viol)} high transaction stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a store has an average basket size of 50 or less, then its staff count is 20 or more."""
    low_basket = df[df["avg_basket_size"] <= 50]
    if low_basket.empty:
        truth = True
        expl = "No stores with avg basket size <= 50."
    else:
        condition = low_basket["staff_count"] >= 20
        truth = condition.all()
        if truth:
            expl = f"All {len(low_basket)} low basket stores have staff count >= 20."
        else:
            viol = low_basket[~condition]
            expl = f"{len(viol)} low basket stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_42.csv")

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
        (17, stmt_17)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()