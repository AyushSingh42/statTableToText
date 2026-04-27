import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the north region have monthly sales greater than or equal to $110k."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["monthly_sales_k"] >= 110
    truth = condition.all()
    if truth:
        expl = f"All {len(north_stores)} north region stores meet the monthly sales requirement."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north region stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))}k)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the west region, then its staff count is less than or equal to 25."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["staff_count"] <= 25
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west region stores meet the staff count requirement."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west region stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the east region with customer satisfaction less than 4.0."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["customer_satisfaction"] < 4.0
    truth = condition.any()
    if truth:
        found = east_stores[condition]
        expl = f"At least one east region store ({found.iloc[0]['store_id']}) has customer satisfaction below 4.0."
    else:
        expl = "No east region store has customer satisfaction below 4.0."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all stores with transactions greater than 2500, their average basket size is less than or equal to 55."""
    high_transaction_stores = df[df["transactions"] > 2500]
    condition = high_transaction_stores["avg_basket_size"] <= 55
    truth = condition.all()
    if truth:
        expl = f"All {len(high_transaction_stores)} high transaction stores meet the average basket size requirement."
    else:
        viol = high_transaction_stores[~condition]
        expl = f"{len(viol)} high transaction stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with staff count greater than 20 have monthly sales greater than or equal to $120k."""
    high_staff_stores = df[df["staff_count"] > 20]
    condition = high_staff_stores["monthly_sales_k"] >= 120
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff_stores)} high staff count stores meet the monthly sales requirement."
    else:
        viol = high_staff_stores[~condition]
        expl = f"{len(viol)} high staff count stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))}k)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a store is in the south region, then its average basket size is greater than 59."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["avg_basket_size"] > 59
    truth = condition.all()
    if truth:
        expl = f"All {len(south_stores)} south region stores meet the average basket size requirement."
    else:
        viol = south_stores[~condition]
        expl = f"{len(viol)} south region stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most stores in the data have customer satisfaction greater than 4.0."""
    total_stores = len(df)
    satisfied_stores = df[df["customer_satisfaction"] > 4.0]
    truth = len(satisfied_stores) > total_stores / 2
    if truth:
        expl = f"{len(satisfied_stores)} out of {total_stores} stores have customer satisfaction > 4.0."
    else:
        expl = f"{len(satisfied_stores)} out of {total_stores} stores have customer satisfaction > 4.0 (less than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all stores with monthly sales less than $100k, their transactions are less than 2200."""
    low_sales_stores = df[df["monthly_sales_k"] < 100]
    condition = low_sales_stores["transactions"] < 2200
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sales_stores)} low sales stores meet the transaction limit."
    else:
        viol = low_sales_stores[~condition]
        expl = f"{len(viol)} low sales stores violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the west region with staff count less than 12."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["staff_count"] < 12
    truth = condition.any()
    if truth:
        found = west_stores[condition]
        expl = f"At least one west region store ({found.iloc[0]['store_id']}) has staff count below 12."
    else:
        expl = "No west region store has staff count below 12."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a store is in the north region, then its monthly sales are greater than or equal to $110k or its transactions are greater than 2000."""
    north_stores = df[df["region"] == "north"]
    condition = (north_stores["monthly_sales_k"] >= 110) | (north_stores["transactions"] > 2000)
    truth = condition.all()
    if truth:
        expl = f"All {len(north_stores)} north region stores satisfy the condition."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north region stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All stores with average basket size greater than 60 have staff count less than or equal to 12."""
    high_basket_stores = df[df["avg_basket_size"] > 60]
    condition = high_basket_stores["staff_count"] <= 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_basket_stores)} high basket size stores meet the staff count requirement."
    else:
        viol = high_basket_stores[~condition]
        expl = f"{len(viol)} high basket size stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all stores with customer satisfaction greater than 4.4, their monthly sales are greater than or equal to $140k."""
    high_satisfaction_stores = df[df["customer_satisfaction"] > 4.4]
    condition = high_satisfaction_stores["monthly_sales_k"] >= 140
    truth = condition.all()
    if truth:
        expl = f"All {len(high_satisfaction_stores)} high satisfaction stores meet the monthly sales requirement."
    else:
        viol = high_satisfaction_stores[~condition]
        expl = f"{len(viol)} high satisfaction stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))}k)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a store is in the east region, then its transactions are greater than 2000 or its average basket size is greater than 54."""
    east_stores = df[df["region"] == "east"]
    condition = (east_stores["transactions"] > 2000) | (east_stores["avg_basket_size"] > 54)
    truth = condition.all()
    if truth:
        expl = f"All {len(east_stores)} east region stores satisfy the condition."
    else:
        viol = east_stores[~condition]
        expl = f"{len(viol)} east region stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one store in the south region with customer satisfaction less than 4.0."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["customer_satisfaction"] < 4.0
    truth = condition.any()
    if truth:
        found = south_stores[condition]
        expl = f"At least one south region store ({found.iloc[0]['store_id']}) has customer satisfaction below 4.0."
    else:
        expl = "No south region store has customer satisfaction below 4.0."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most stores in the data have staff count greater than 10."""
    total_stores = len(df)
    high_staff_stores = df[df["staff_count"] > 10]
    truth = len(high_staff_stores) > total_stores / 2
    if truth:
        expl = f"{len(high_staff_stores)} out of {total_stores} stores have staff count > 10."
    else:
        expl = f"{len(high_staff_stores)} out of {total_stores} stores have staff count > 10 (less than half)."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. For all stores with monthly sales greater than $160k, their transactions are greater than 2500."""
    high_sales_stores = df[df["monthly_sales_k"] > 160]
    condition = high_sales_stores["transactions"] > 2500
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales_stores)} high sales stores meet the transaction requirement."
    else:
        viol = high_sales_stores[~condition]
        expl = f"{len(viol)} high sales stores violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a store is in the west region, then its monthly sales are greater than or equal to $110k or its average basket size is greater than 51."""
    west_stores = df[df["region"] == "west"]
    condition = (west_stores["monthly_sales_k"] >= 110) | (west_stores["avg_basket_size"] > 51)
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west region stores satisfy the condition."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west region stores violate the rule (IDs: {', '.join(viol['store_id'].tolist())})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All stores with transactions less than 2000 have monthly sales less than $120k."""
    low_transaction_stores = df[df["transactions"] < 2000]
    condition = low_transaction_stores["monthly_sales_k"] < 120
    truth = condition.all()
    if truth:
        expl = f"All {len(low_transaction_stores)} low transaction stores meet the monthly sales limit."
    else:
        viol = low_transaction_stores[~condition]
        expl = f"{len(viol)} low transaction stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))}k)."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. There exists at least one store in the north region with customer satisfaction less than 4.0."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["customer_satisfaction"] < 4.0
    truth = condition.any()
    if truth:
        found = north_stores[condition]
        expl = f"At least one north region store ({found.iloc[0]['store_id']}) has customer satisfaction below 4.0."
    else:
        expl = "No north region store has customer satisfaction below 4.0."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_72.csv")

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