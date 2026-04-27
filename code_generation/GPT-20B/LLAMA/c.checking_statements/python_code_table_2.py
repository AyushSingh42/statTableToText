import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the north region have a customer satisfaction rating of 4.2 or higher."""
    north = df[df["region"] == "north"]
    if north.empty:
        return True, "No north region stores to evaluate."
    condition = north["customer_satisfaction"] >= 4.2
    truth = condition.all()
    if truth:
        return True, f"All {len(north)} north region stores satisfy the rating requirement."
    else:
        viol = north[~condition]
        return False, f"{len(viol)} north region stores violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the west region, then its average basket size is less than 60."""
    west = df[df["region"] == "west"]
    if west.empty:
        return True, "No west region stores to evaluate."
    condition = west["avg_basket_size"] < 60
    truth = condition.all()
    if truth:
        return True, f"All {len(west)} west region stores have avg basket size < 60."
    else:
        viol = west[~condition]
        return False, f"{len(viol)} west region stores violate the rule (sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the south region with a staff count greater than 20."""
    condition = (df["region"] == "south") & (df["staff_count"] > 20)
    truth = not df[condition].empty
    if truth:
        return True, f"Found {len(df[condition])} south region store(s) with staff count > 20."
    else:
        return False, "No south region store has staff count > 20."

def stmt_4(df: pd.DataFrame):
    """4. For all stores with monthly sales greater than 150k, their transactions are greater than 1800."""
    high_sales = df[df["monthly_sales_k"] > 150]
    if high_sales.empty:
        return True, "No stores with monthly sales > 150k to evaluate."
    condition = high_sales["transactions"] > 1800
    truth = condition.all()
    if truth:
        return True, f"All {len(high_sales)} high‑sales stores have transactions > 1800."
    else:
        viol = high_sales[~condition]
        return False, f"{len(viol)} high‑sales store(s) violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."

def stmt_5(df: pd.DataFrame):
    """5. All stores with a staff count greater than 20 have a customer satisfaction rating of 4.0 or higher."""
    staff_gt20 = df[df["staff_count"] > 20]
    if staff_gt20.empty:
        return True, "No stores with staff count > 20 to evaluate."
    condition = staff_gt20["customer_satisfaction"] >= 4.0
    truth = condition.all()
    if truth:
        return True, f"All {len(staff_gt20)} stores with staff > 20 have rating >= 4.0."
    else:
        viol = staff_gt20[~condition]
        return False, f"{len(viol)} store(s) violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."

def stmt_6(df: pd.DataFrame):
    """6. If a store is in the east region, then its average basket size is greater than 55."""
    east = df[df["region"] == "east"]
    if east.empty:
        return True, "No east region stores to evaluate."
    condition = east["avg_basket_size"] > 55
    truth = condition.all()
    if truth:
        return True, f"All {len(east)} east region stores have avg basket size > 55."
    else:
        viol = east[~condition]
        return False, f"{len(viol)} east region store(s) violate the rule (sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."

def stmt_7(df: pd.DataFrame):
    """7. Most stores in the data have a monthly sales figure less than 170k."""
    count_lt170 = df[df["monthly_sales_k"] < 170].shape[0]
    total = df.shape[0]
    truth = count_lt170 > total / 2
    if truth:
        return True, f"{count_lt170} out of {total} stores have monthly sales < 170k."
    else:
        return False, f"Only {count_lt170} out of {total} stores have monthly sales < 170k."

def stmt_8(df: pd.DataFrame):
    """8. For all stores with transactions greater than 2200, their average basket size is less than 60."""
    high_trans = df[df["transactions"] > 2200]
    if high_trans.empty:
        return True, "No stores with transactions > 2200 to evaluate."
    condition = high_trans["avg_basket_size"] < 60
    truth = condition.all()
    if truth:
        return True, f"All {len(high_trans)} high‑transaction stores have avg basket size < 60."
    else:
        viol = high_trans[~condition]
        return False, f"{len(viol)} high‑transaction store(s) violate the rule (sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the north region with a monthly sales figure less than 100k."""
    condition = (df["region"] == "north") & (df["monthly_sales_k"] < 100)
    truth = not df[condition].empty
    if truth:
        return True, f"Found {len(df[condition])} north region store(s) with monthly sales < 100k."
    else:
        return False, "No north region store has monthly sales < 100k."

def stmt_10(df: pd.DataFrame):
    """10. If a store is in the south region, then its customer satisfaction rating is 4.1 or higher."""
    south = df[df["region"] == "south"]
    if south.empty:
        return True, "No south region stores to evaluate."
    condition = south["customer_satisfaction"] >= 4.1
    truth = condition.all()
    if truth:
        return True, f"All {len(south)} south region stores have rating >= 4.1."
    else:
        viol = south[~condition]
        return False, f"{len(viol)} south region store(s) violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."

def stmt_11(df: pd.DataFrame):
    """11. All stores with a customer satisfaction rating of 4.7 have a staff count of 12 or greater."""
    rating_47 = df[df["customer_satisfaction"] == 4.7]
    if rating_47.empty:
        return True, "No stores with rating 4.7 to evaluate."
    condition = rating_47["staff_count"] >= 12
    truth = condition.all()
    if truth:
        return True, f"All {len(rating_47)} rating‑4.7 stores have staff count >= 12."
    else:
        viol = rating_47[~condition]
        return False, f"{len(viol)} rating‑4.7 store(s) violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."

def stmt_12(df: pd.DataFrame):
    """12. For all stores with an average basket size greater than 65, their monthly sales are less than 140k."""
    high_basket = df[df["avg_basket_size"] > 65]
    if high_basket.empty:
        return True, "No stores with avg basket size > 65 to evaluate."
    condition = high_basket["monthly_sales_k"] < 140
    truth = condition.all()
    if truth:
        return True, f"All {len(high_basket)} high‑basket stores have monthly sales < 140k."
    else:
        viol = high_basket[~condition]
        return False, f"{len(viol)} high‑basket store(s) violate the rule (sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."

def stmt_13(df: pd.DataFrame):
    """13. If a store has a staff count of 25 or greater, then its customer satisfaction rating is 4.2 or higher."""
    staff_ge25 = df[df["staff_count"] >= 25]
    if staff_ge25.empty:
        return True, "No stores with staff count >= 25 to evaluate."
    condition = staff_ge25["customer_satisfaction"] >= 4.2
    truth = condition.all()
    if truth:
        return True, f"All {len(staff_ge25)} staff>=25 stores have rating >= 4.2."
    else:
        viol = staff_ge25[~condition]
        return False, f"{len(viol)} staff>=25 store(s) violate the rule (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."

def stmt_14(df: pd.DataFrame):
    """14. Most stores in the data have a staff count less than 20."""
    count_lt20 = df[df["staff_count"] < 20].shape[0]
    total = df.shape[0]
    truth = count_lt20 > total / 2
    if truth:
        return True, f"{count_lt20} out of {total} stores have staff count < 20."
    else:
        return False, f"Only {count_lt20} out of {total} stores have staff count < 20."

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the west region with a monthly sales figure greater than 160k."""
    condition = (df["region"] == "west") & (df["monthly_sales_k"] > 160)
    truth = not df[condition].empty
    if truth:
        return True, f"Found {len(df[condition])} west region store(s) with monthly sales > 160k."
    else:
        return False, "No west region store has monthly sales > 160k."

def stmt_16(df: pd.DataFrame):
    """16. For all stores with transactions less than 2000, their average basket size is greater than 55."""
    low_trans = df[df["transactions"] < 2000]
    if low_trans.empty:
        return True, "No stores with transactions < 2000 to evaluate."
    condition = low_trans["avg_basket_size"] > 55
    truth = condition.all()
    if truth:
        return True, f"All {len(low_trans)} low‑transaction stores have avg basket size > 55."
    else:
        viol = low_trans[~condition]
        return False, f"{len(viol)} low‑transaction store(s) violate the rule (sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."

def stmt_17(df: pd.DataFrame):
    """17. All stores with a customer satisfaction rating of 3.7 have a staff count of 17 or less."""
    rating_37 = df[df["customer_satisfaction"] == 3.7]
    if rating_37.empty:
        return True, "No stores with rating 3.7 to evaluate."
    condition = rating_37["staff_count"] <= 17
    truth = condition.all()
    if truth:
        return True, f"All {len(rating_37)} rating‑3.7 stores have staff count <= 17."
    else:
        viol = rating_37[~condition]
        return False, f"{len(viol)} rating‑3.7 store(s) violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."

def stmt_18(df: pd.DataFrame):
    """18. If a store is in the east region, then its transactions are greater than 1600."""
    east = df[df["region"] == "east"]
    if east.empty:
        return True, "No east region stores to evaluate."
    condition = east["transactions"] > 1600
    truth = condition.all()
    if truth:
        return True, f"All {len(east)} east region stores have transactions > 1600."
    else:
        viol = east[~condition]
        return False, f"{len(viol)} east region store(s) violate the rule (transactions: {', '.join(map(str, viol['transactions'].tolist()))})."

def stmt_19(df: pd.DataFrame):
    """19. For all stores with a monthly sales figure greater than 120k, their staff count is greater than 10."""
    high_sales = df[df["monthly_sales_k"] > 120]
    if high_sales.empty:
        return True, "No stores with monthly sales > 120k to evaluate."
    condition = high_sales["staff_count"] > 10
    truth = condition.all()
    if truth:
        return True, f"All {len(high_sales)} high‑sales stores have staff count > 10."
    else:
        viol = high_sales[~condition]
        return False, f"{len(viol)} high‑sales store(s) violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_2.csv")

    # Convert numeric columns
    numeric_cols = ["monthly_sales_k", "transactions", "avg_basket_size", "staff_count", "customer_satisfaction"]
    for col in numeric_cols:
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
        (19, stmt_19),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()