import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the north region have a customer satisfaction rating greater than or equal to 3.6."""
    north_stores = df[df["region"] == "north"]
    if north_stores.empty:
        truth = True
        expl = "No stores in the north region."
    else:
        condition = north_stores["customer_satisfaction"] >= 3.6
        truth = condition.all()
        if truth:
            expl = f"All {len(north_stores)} stores in the north region satisfy the condition."
        else:
            viol = north_stores[~condition]
            expl = f"{len(viol)} stores in the north region violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the west region, then its average basket size is less than or equal to 68."""
    west_stores = df[df["region"] == "west"]
    if west_stores.empty:
        truth = True
        expl = "No stores in the west region."
    else:
        condition = west_stores["avg_basket_size"] <= 68
        truth = condition.all()
        if truth:
            expl = f"All {len(west_stores)} stores in the west region satisfy the condition."
        else:
            viol = west_stores[~condition]
            expl = f"{len(viol)} stores in the west region violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the north region with a monthly sales value greater than $150k."""
    north_stores = df[df["region"] == "north"]
    if north_stores.empty:
        truth = False
        expl = "No stores in the north region."
    else:
        condition = north_stores["monthly_sales_k"] > 150
        truth = condition.any()
        if truth:
            expl = f"At least one store in the north region exceeds $150k in monthly sales."
        else:
            expl = f"No stores in the north region exceed $150k in monthly sales."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with a staff count greater than 20 have a customer satisfaction rating greater than or equal to 4.5."""
    high_staff = df[df["staff_count"] > 20]
    if high_staff.empty:
        truth = True
        expl = "No stores with staff count > 20."
    else:
        condition = high_staff["customer_satisfaction"] >= 4.5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_staff)} stores with staff count > 20 satisfy the condition."
        else:
            viol = high_staff[~condition]
            expl = f"{len(viol)} stores with staff count > 20 violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store is in the west region and has a staff count greater than 15, then its average basket size is greater than 48."""
    west_high_staff = df[(df["region"] == "west") & (df["staff_count"] > 15)]
    if west_high_staff.empty:
        truth = True
        expl = "No stores in the west region with staff count > 15."
    else:
        condition = west_high_staff["avg_basket_size"] > 48
        truth = condition.all()
        if truth:
            expl = f"All {len(west_high_staff)} stores in the west region with staff count > 15 satisfy the condition."
        else:
            viol = west_high_staff[~condition]
            expl = f"{len(viol)} stores in the west region with staff count > 15 violate the rule (basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most stores in the dataset have a monthly sales value less than $150k."""
    total_stores = len(df)
    low_sales = df[df["monthly_sales_k"] < 150]
    count_low = len(low_sales)
    truth = count_low > total_stores / 2
    if truth:
        expl = f"More than half ({count_low}/{total_stores}) of stores have monthly sales < $150k."
    else:
        expl = f"Less than half ({count_low}/{total_stores}) of stores have monthly sales < $150k."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with a customer satisfaction rating greater than 4.5 have a staff count greater than 20."""
    high_satisfaction = df[df["customer_satisfaction"] > 4.5]
    if high_satisfaction.empty:
        truth = True
        expl = "No stores with satisfaction > 4.5."
    else:
        condition = high_satisfaction["staff_count"] > 20
        truth = condition.all()
        if truth:
            expl = f"All {len(high_satisfaction)} stores with satisfaction > 4.5 satisfy the condition."
        else:
            viol = high_satisfaction[~condition]
            expl = f"{len(viol)} stores with satisfaction > 4.5 violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store is in the north region, then its transactions are greater than 1500."""
    north_stores = df[df["region"] == "north"]
    if north_stores.empty:
        truth = True
        expl = "No stores in the north region."
    else:
        condition = north_stores["transactions"] > 1500
        truth = condition.all()
        if truth:
            expl = f"All {len(north_stores)} stores in the north region satisfy the condition."
        else:
            viol = north_stores[~condition]
            expl = f"{len(viol)} stores in the north region violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the west region with a monthly sales value greater than $120k and an average basket size greater than 50."""
    west_stores = df[df["region"] == "west"]
    if west_stores.empty:
        truth = False
        expl = "No stores in the west region."
    else:
        condition = (west_stores["monthly_sales_k"] > 120) & (west_stores["avg_basket_size"] > 50)
        truth = condition.any()
        if truth:
            expl = f"At least one store in the west region satisfies both conditions."
        else:
            expl = f"No stores in the west region satisfy both conditions."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All stores with a staff count less than 15 have a customer satisfaction rating less than 4.0."""
    low_staff = df[df["staff_count"] < 15]
    if low_staff.empty:
        truth = True
        expl = "No stores with staff count < 15."
    else:
        condition = low_staff["customer_satisfaction"] < 4.0
        truth = condition.all()
        if truth:
            expl = f"All {len(low_staff)} stores with staff count < 15 satisfy the condition."
        else:
            viol = low_staff[~condition]
            expl = f"{len(viol)} stores with staff count < 15 violate the rule (satisfactions: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a store is in the east region, then its monthly sales value is greater than $150k."""
    east_stores = df[df["region"] == "east"]
    if east_stores.empty:
        truth = True
        expl = "No stores in the east region."
    else:
        condition = east_stores["monthly_sales_k"] > 150
        truth = condition.all()
        if truth:
            expl = f"All {len(east_stores)} stores in the east region satisfy the condition."
        else:
            viol = east_stores[~condition]
            expl = f"{len(viol)} stores in the east region violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most stores in the west region have a staff count greater than 15."""
    west_stores = df[df["region"] == "west"]
    if west_stores.empty:
        truth = False
        expl = "No stores in the west region."
    else:
        high_staff = west_stores[west_stores["staff_count"] > 15]
        count_high = len(high_staff)
        total_west = len(west_stores)
        truth = count_high > total_west / 2
        if truth:
            expl = f"More than half ({count_high}/{total_west}) of stores in the west region have staff count > 15."
        else:
            expl = f"Less than half ({count_high}/{total_west}) of stores in the west region have staff count > 15."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All stores with a customer satisfaction rating less than 4.0 have a staff count less than 18."""
    low_satisfaction = df[df["customer_satisfaction"] < 4.0]
    if low_satisfaction.empty:
        truth = True
        expl = "No stores with satisfaction < 4.0."
    else:
        condition = low_satisfaction["staff_count"] < 18
        truth = condition.all()
        if truth:
            expl = f"All {len(low_satisfaction)} stores with satisfaction < 4.0 satisfy the condition."
        else:
            viol = low_satisfaction[~condition]
            expl = f"{len(viol)} stores with satisfaction < 4.0 violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a store has a monthly sales value greater than $120k, then its transactions are greater than 1500."""
    high_sales = df[df["monthly_sales_k"] > 120]
    if high_sales.empty:
        truth = True
        expl = "No stores with monthly sales > $120k."
    else:
        condition = high_sales["transactions"] > 1500
        truth = condition.all()
        if truth:
            expl = f"All {len(high_sales)} stores with monthly sales > $120k satisfy the condition."
        else:
            viol = high_sales[~condition]
            expl = f"{len(viol)} stores with monthly sales > $120k violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the north region with a customer satisfaction rating greater than 4.5 and a staff count greater than 20."""
    north_stores = df[df["region"] == "north"]
    if north_stores.empty:
        truth = False
        expl = "No stores in the north region."
    else:
        condition = (north_stores["customer_satisfaction"] > 4.5) & (north_stores["staff_count"] > 20)
        truth = condition.any()
        if truth:
            expl = f"At least one store in the north region satisfies both conditions."
        else:
            expl = f"No stores in the north region satisfy both conditions."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_92.csv")

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
        (15, stmt_15)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()