import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the south region have monthly sales greater than $130k or less than $92k."""
    south_stores = df[df["region"] == "south"]
    condition = (south_stores["monthly_sales_k"] > 130) | (south_stores["monthly_sales_k"] < 92)
    truth = condition.all()
    if truth:
        expl = f"All {len(south_stores)} south region stores satisfy the condition."
    else:
        viol = south_stores[~condition]
        expl = f"{len(viol)} south region stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the north region, then its customer satisfaction is greater than or equal to 4.2."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["customer_satisfaction"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(north_stores)} north region stores satisfy the condition."
    else:
        viol = north_stores[~condition]
        expl = f"{len(viol)} north region stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the east region with customer satisfaction less than 4.0."""
    east_stores = df[df["region"] == "east"]
    condition = east_stores["customer_satisfaction"] < 4.0
    truth = condition.any()
    if truth:
        expl = f"At least one east region store ({east_stores[condition]['store_id'].iloc[0]}) satisfies the condition."
    else:
        expl = f"No east region store satisfies the condition."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with staff count greater than 20 have monthly sales greater than $158k."""
    high_staff = df[df["staff_count"] > 20]
    condition = high_staff["monthly_sales_k"] > 158
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} high-staff stores satisfy the condition."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} high-staff stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store is in the west region, then its average basket size is greater than 58k."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["avg_basket_size"] > 58
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west region stores satisfy the condition."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west region stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most stores have transactions greater than 2000."""
    total_stores = len(df)
    condition = df["transactions"] > 2000
    satisfied = condition.sum()
    truth = satisfied > total_stores / 2
    if truth:
        expl = f"{satisfied} out of {total_stores} stores satisfy the condition (>2000 transactions)."
    else:
        expl = f"{satisfied} out of {total_stores} stores satisfy the condition (>2000 transactions), which is not more than half."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with customer satisfaction greater than 4.5 have staff count less than 18."""
    high_satisfaction = df[df["customer_satisfaction"] > 4.5]
    condition = high_satisfaction["staff_count"] < 18
    truth = condition.all()
    if truth:
        expl = f"All {len(high_satisfaction)} high-satisfaction stores satisfy the condition."
    else:
        viol = high_satisfaction[~condition]
        expl = f"{len(viol)} high-satisfaction stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store is in the south region, then its average basket size is less than 65k."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["avg_basket_size"] < 65
    truth = condition.all()
    if truth:
        expl = f"All {len(south_stores)} south region stores satisfy the condition."
    else:
        viol = south_stores[~condition]
        expl = f"{len(viol)} south region stores violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the north region with monthly sales greater than $166k."""
    north_stores = df[df["region"] == "north"]
    condition = north_stores["monthly_sales_k"] > 166
    truth = condition.any()
    if truth:
        expl = f"At least one north region store ({north_stores[condition]['store_id'].iloc[0]}) satisfies the condition."
    else:
        expl = f"No north region store satisfies the condition."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All stores with average basket size greater than 64k have customer satisfaction greater than or equal to 4.2."""
    large_basket = df[df["avg_basket_size"] > 64]
    condition = large_basket["customer_satisfaction"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(large_basket)} large-basket stores satisfy the condition."
    else:
        viol = large_basket[~condition]
        expl = f"{len(viol)} large-basket stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a store has transactions less than 1800, then its staff count is less than 18."""
    low_transactions = df[df["transactions"] < 1800]
    condition = low_transactions["staff_count"] < 18
    truth = condition.all()
    if truth:
        expl = f"All {len(low_transactions)} low-transaction stores satisfy the condition."
    else:
        viol = low_transactions[~condition]
        expl = f"{len(viol)} low-transaction stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most stores in the east region have customer satisfaction greater than 4.4."""
    east_stores = df[df["region"] == "east"]
    total_east = len(east_stores)
    condition = east_stores["customer_satisfaction"] > 4.4
    satisfied = condition.sum()
    truth = satisfied > total_east / 2
    if truth:
        expl = f"{satisfied} out of {total_east} east region stores satisfy the condition (>4.4 satisfaction)."
    else:
        expl = f"{satisfied} out of {total_east} east region stores satisfy the condition (>4.4 satisfaction), which is not more than half."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All stores with staff count less than 15 have monthly sales less than $150k."""
    low_staff = df[df["staff_count"] < 15]
    condition = low_staff["monthly_sales_k"] < 150
    truth = condition.all()
    if truth:
        expl = f"All {len(low_staff)} low-staff stores satisfy the condition."
    else:
        viol = low_staff[~condition]
        expl = f"{len(viol)} low-staff stores violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a store is in the west region, then its customer satisfaction is greater than or equal to 4.1."""
    west_stores = df[df["region"] == "west"]
    condition = west_stores["customer_satisfaction"] >= 4.1
    truth = condition.all()
    if truth:
        expl = f"All {len(west_stores)} west region stores satisfy the condition."
    else:
        viol = west_stores[~condition]
        expl = f"{len(viol)} west region stores violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the south region with staff count greater than 25."""
    south_stores = df[df["region"] == "south"]
    condition = south_stores["staff_count"] > 25
    truth = condition.any()
    if truth:
        expl = f"At least one south region store ({south_stores[condition]['store_id'].iloc[0]}) satisfies the condition."
    else:
        expl = f"No south region store satisfies the condition."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All stores with monthly sales greater than $160k have transactions greater than 1500."""
    high_sales = df[df["monthly_sales_k"] > 160]
    condition = high_sales["transactions"] > 1500
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} high-sales stores satisfy the condition."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} high-sales stores violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a store has average basket size less than 60k, then its staff count is less than 20."""
    small_basket = df[df["avg_basket_size"] < 60]
    condition = small_basket["staff_count"] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(small_basket)} small-basket stores satisfy the condition."
    else:
        viol = small_basket[~condition]
        expl = f"{len(viol)} small-basket stores violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most stores have monthly sales less than $170k."""
    total_stores = len(df)
    condition = df["monthly_sales_k"] < 170
    satisfied = condition.sum()
    truth = satisfied > total_stores / 2
    if truth:
        expl = f"{satisfied} out of {total_stores} stores satisfy the condition (<$170k sales)."
    else:
        expl = f"{satisfied} out of {total_stores} stores satisfy the condition (<$170k sales), which is not more than half."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_52.csv")

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