import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the west region have monthly sales greater than $100k."""
    west = df[df["region"] == "west"]
    condition = west["monthly_sales_k"] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores have monthly sales > 100k."
    else:
        viol = west[~condition]
        expl = f"{len(viol)} west store(s) violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the south region, then its staff count is less than 15."""
    south = df[df["region"] == "south"]
    condition = south["staff_count"] < 15
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores have staff count < 15."
    else:
        viol = south[~condition]
        expl = f"{len(viol)} south store(s) violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the west region with a customer satisfaction rating greater than 4.5."""
    west = df[df["region"] == "west"]
    condition = west["customer_satisfaction"] > 4.5
    truth = condition.any()
    if truth:
        expl = f"At least one west store has customer satisfaction > 4.5."
    else:
        expl = "No west store has customer satisfaction > 4.5."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with transactions greater than 2500 have an average basket size greater than 55."""
    high_tx = df[df["transactions"] > 2500]
    condition = high_tx["avg_basket_size"] > 55
    truth = condition.all()
    if truth:
        expl = f"All {len(high_tx)} stores with transactions > 2500 have avg basket size > 55."
    else:
        viol = high_tx[~condition]
        expl = f"{len(viol)} store(s) violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store is in the north region, then its monthly sales are greater than $90k."""
    north = df[df["region"] == "north"]
    condition = north["monthly_sales_k"] > 90
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores have monthly sales > 90k."
    else:
        viol = north[~condition]
        expl = f"{len(viol)} north store(s) violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most stores in the west region have a staff count greater than 15."""
    west = df[df["region"] == "west"]
    if len(west) == 0:
        truth = False
        expl = "No west stores to evaluate."
    else:
        condition = west["staff_count"] > 15
        proportion = condition.sum() / len(west)
        truth = proportion > 0.5
        if truth:
            expl = f"{proportion*100:.1f}% of west stores have staff count > 15."
        else:
            expl = f"Only {proportion*100:.1f}% of west stores have staff count > 15."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with a staff count greater than 18 have monthly sales greater than $140k."""
    high_staff = df[df["staff_count"] > 18]
    condition = high_staff["monthly_sales_k"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(high_staff)} stores with staff count > 18 have monthly sales > 140k."
    else:
        viol = high_staff[~condition]
        expl = f"{len(viol)} store(s) violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store is in the east region, then its transactions are less than 1700."""
    east = df[df["region"] == "east"]
    condition = east["transactions"] < 1700
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have transactions < 1700."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east store(s) violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the west region with a customer satisfaction rating less than 4.0."""
    west = df[df["region"] == "west"]
    condition = west["customer_satisfaction"] < 4.0
    truth = condition.any()
    if truth:
        expl = f"At least one west store has customer satisfaction < 4.0."
    else:
        expl = "No west store has customer satisfaction < 4.0."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All stores with an average basket size greater than 60 have monthly sales greater than $150k."""
    high_basket = df[df["avg_basket_size"] > 60]
    condition = high_basket["monthly_sales_k"] > 150
    truth = condition.all()
    if truth:
        expl = f"All {len(high_basket)} stores with avg basket size > 60 have monthly sales > 150k."
    else:
        viol = high_basket[~condition]
        expl = f"{len(viol)} store(s) violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a store is in the south region, then its monthly sales are less than $120k."""
    south = df[df["region"] == "south"]
    condition = south["monthly_sales_k"] < 120
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores have monthly sales < 120k."
    else:
        viol = south[~condition]
        expl = f"{len(viol)} south store(s) violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most stores in the west region have an average basket size greater than 50."""
    west = df[df["region"] == "west"]
    if len(west) == 0:
        truth = False
        expl = "No west stores to evaluate."
    else:
        condition = west["avg_basket_size"] > 50
        proportion = condition.sum() / len(west)
        truth = proportion > 0.5
        if truth:
            expl = f"{proportion*100:.1f}% of west stores have avg basket size > 50."
        else:
            expl = f"Only {proportion*100:.1f}% of west stores have avg basket size > 50."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All stores with monthly sales greater than $160k have a staff count greater than 15."""
    high_sales = df[df["monthly_sales_k"] > 160]
    condition = high_sales["staff_count"] > 15
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sales)} stores with monthly sales > 160k have staff count > 15."
    else:
        viol = high_sales[~condition]
        expl = f"{len(viol)} store(s) violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a store is in the north region, then its staff count is less than 18."""
    north = df[df["region"] == "north"]
    condition = north["staff_count"] < 18
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores have staff count < 18."
    else:
        viol = north[~condition]
        expl = f"{len(viol)} north store(s) violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the west region with a staff count greater than 20."""
    west = df[df["region"] == "west"]
    condition = west["staff_count"] > 20
    truth = condition.any()
    if truth:
        expl = f"At least one west store has staff count > 20."
    else:
        expl = "No west store has staff count > 20."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All stores with transactions less than 1800 have a customer satisfaction rating greater than 4.2."""
    low_tx = df[df["transactions"] < 1800]
    condition = low_tx["customer_satisfaction"] > 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(low_tx)} stores with transactions < 1800 have customer satisfaction > 4.2."
    else:
        viol = low_tx[~condition]
        expl = f"{len(viol)} store(s) violate the rule (customer satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a store is in the east region, then its average basket size is less than 50."""
    east = df[df["region"] == "east"]
    condition = east["avg_basket_size"] < 50
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores have avg basket size < 50."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east store(s) violate the rule (avg basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most stores in the west region have monthly sales greater than $120k."""
    west = df[df["region"] == "west"]
    if len(west) == 0:
        truth = False
        expl = "No west stores to evaluate."
    else:
        condition = west["monthly_sales_k"] > 120
        proportion = condition.sum() / len(west)
        truth = proportion > 0.5
        if truth:
            expl = f"{proportion*100:.1f}% of west stores have monthly sales > 120k."
        else:
            expl = f"Only {proportion*100:.1f}% of west stores have monthly sales > 120k."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_32.csv")

    # Convert numeric columns safely.
    for col in df.columns:
        if col!= "store_id":
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