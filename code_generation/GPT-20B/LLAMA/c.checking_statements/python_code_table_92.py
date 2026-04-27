import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the north region have a customer satisfaction rating greater than or equal to 3.6."""
    north = df[df["region"] == "north"]
    if north.empty:
        return True, "No north region stores to evaluate."
    condition = north["customer_satisfaction"] >= 3.6
    truth = condition.all()
    if truth:
        return True, f"All {len(north)} north region stores satisfy the rating requirement."
    else:
        viol = north[~condition]
        ids = viol["store_id"].tolist()
        return False, f"{len(viol)} north region stores violate the rating requirement (IDs: {', '.join(ids)})."

def stmt_2(df: pd.DataFrame):
    """2. If a store is in the west region, then its average basket size is less than or equal to 68."""
    west = df[df["region"] == "west"]
    if west.empty:
        return True, "No west region stores to evaluate."
    condition = west["avg_basket_size"] <= 68
    truth = condition.all()
    if truth:
        return True, f"All {len(west)} west region stores have avg basket size <= 68."
    else:
        viol = west[~condition]
        ids = viol["store_id"].tolist()
        return False, f"{len(viol)} west region stores violate the basket size requirement (IDs: {', '.join(ids)})."

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one store in the north region with a monthly sales value greater than $150k."""
    north = df[(df["region"] == "north") & (df["monthly_sales_k"] > 150)]
    truth = not north.empty
    if truth:
        ids = north["store_id"].tolist()
        return True, f"Found {len(north)} north region store(s) with sales > 150k (IDs: {', '.join(ids)})."
    else:
        return False, "No north region store has monthly sales > 150k."

def stmt_4(df: pd.DataFrame):
    """4. All stores with a staff count greater than 20 have a customer satisfaction rating greater than or equal to 4.5."""
    staff_gt20 = df[df["staff_count"] > 20]
    if staff_gt20.empty:
        return True, "No stores with staff count > 20 to evaluate."
    condition = staff_gt20["customer_satisfaction"] >= 4.5
    truth = condition.all()
    if truth:
        return True, f"All {len(staff_gt20)} stores with staff > 20 satisfy the rating requirement."
    else:
        viol = staff_gt20[~condition]
        ids = viol["store_id"].tolist()
        return False, f"{len(viol)} stores with staff > 20 violate the rating requirement (IDs: {', '.join(ids)})."

def stmt_5(df: pd.DataFrame):
    """5. If a store is in the west region and has a staff count greater than 15, then its average basket size is greater than 48."""
    subset = df[(df["region"] == "west") & (df["staff_count"] > 15)]
    if subset.empty:
        return True, "No west region stores with staff > 15 to evaluate."
    condition = subset["avg_basket_size"] > 48
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} west region stores with staff > 15 have avg basket size > 48."
    else:
        viol = subset[~condition]
        ids = viol["store_id"].tolist()
        return False, f"{len(viol)} west region stores with staff > 15 violate the basket size requirement (IDs: {', '.join(ids)})."

def stmt_6(df: pd.DataFrame):
    """6. Most stores in the dataset have a monthly sales value less than $150k."""
    count_lt150 = (df["monthly_sales_k"] < 150).sum()
    total = len(df)
    truth = count_lt150 > total / 2
    if truth:
        return True, f"{count_lt150} out of {total} stores have sales < 150k, which is >50%."
    else:
        return False, f"Only {count_lt150} out of {total} stores have sales < 150k, which is not >50%."

def stmt_7(df: pd.DataFrame):
    """7. All stores with a customer satisfaction rating greater than 4.5 have a staff count greater than 20."""
    cs_gt45 = df[df["customer_satisfaction"] > 4.5]
    if cs_gt45.empty:
        return True, "No stores with customer satisfaction > 4.5 to evaluate."
    condition = cs_gt45["staff_count"] > 20
    truth = condition.all()
    if truth:
        return True, f"All {len(cs_gt45)} stores with CS > 4.5 have staff > 20."
    else:
        viol = cs_gt45[~condition]
        ids = viol["store_id"].tolist()
        return False, f"{len(viol)} stores with CS > 4.5 violate the staff count requirement (IDs: {', '.join(ids)})."

def stmt_8(df: pd.DataFrame):
    """8. If a store is in the north region, then its transactions are greater than 1500."""
    north = df[df["region"] == "north"]
    if north.empty:
        return True, "No north region stores to evaluate."
    condition = north["transactions"] > 1500
    truth = condition.all()
    if truth:
        return True, f"All {len(north)} north region stores have transactions > 1500."
    else:
        viol = north[~condition]
        ids = viol["store_id"].tolist()
        return False, f"{len(viol)} north region stores violate the transaction requirement (IDs: {', '.join(ids)})."

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one store in the west region with a monthly sales value greater than $120k and an average basket size greater than 50."""
    subset = df[(df["region"] == "west") & (df["monthly_sales_k"] > 120) & (df["avg_basket_size"] > 50)]
    truth = not subset.empty
    if truth:
        ids = subset["store_id"].tolist()
        return True, f"Found {len(subset)} west region store(s) with sales > 120k and basket size > 50 (IDs: {', '.join(ids)})."
    else:
        return False, "No west region store satisfies both sales > 120k and basket size > 50."

def stmt_10(df: pd.DataFrame):
    """10. All stores with a staff count less than 15 have a customer satisfaction rating less than 4.0."""
    staff_lt15 = df[df["staff_count"] < 15]
    if staff_lt15.empty:
        return True, "No stores with staff count < 15 to evaluate."
    condition = staff_lt15["customer_satisfaction"] < 4.0
    truth = condition.all()
    if truth:
        return True, f"All {len(staff_lt15)} stores with staff < 15 have CS < 4.0."
    else:
        viol = staff_lt15[~condition]
        ids = viol["store_id"].tolist()
        return False, f"{len(viol)} stores with staff < 15 violate the CS requirement (IDs: {', '.join(ids)})."

def stmt_11(df: pd.DataFrame):
    """11. If a store is in the east region, then its monthly sales value is greater than $150k."""
    east = df[df["region"] == "east"]
    if east.empty:
        return True, "No east region stores to evaluate."
    condition = east["monthly_sales_k"] > 150
    truth = condition.all()
    if truth:
        return True, f"All {len(east)} east region stores have sales > 150k."
    else:
        viol = east[~condition]
        ids = viol["store_id"].tolist()
        return False, f"{len(viol)} east region stores violate the sales requirement (IDs: {', '.join(ids)})."

def stmt_12(df: pd.DataFrame):
    """12. Most stores in the west region have a staff count greater than 15."""
    west = df[df["region"] == "west"]
    if west.empty:
        return True, "No west region stores to evaluate."
    count_gt15 = (west["staff_count"] > 15).sum()
    total = len(west)
    truth = count_gt15 > total / 2
    if truth:
        return True, f"{count_gt15} out of {total} west region stores have staff > 15, which is >50%."
    else:
        return False, f"Only {count_gt15} out of {total} west region stores have staff > 15, which is not >50%."

def stmt_13(df: pd.DataFrame):
    """13. All stores with a customer satisfaction rating less than 4.0 have a staff count less than 18."""
    cs_lt4 = df[df["customer_satisfaction"] < 4.0]
    if cs_lt4.empty:
        return True, "No stores with customer satisfaction < 4.0 to evaluate."
    condition = cs_lt4["staff_count"] < 18
    truth = condition.all()
    if truth:
        return True, f"All {len(cs_lt4)} stores with CS < 4.0 have staff < 18."
    else:
        viol = cs_lt4[~condition]
        ids = viol["store_id"].tolist()
        return False, f"{len(viol)} stores with CS < 4.0 violate the staff count requirement (IDs: {', '.join(ids)})."

def stmt_14(df: pd.DataFrame):
    """14. If a store has a monthly sales value greater than $120k, then its transactions are greater than 1500."""
    subset = df[df["monthly_sales_k"] > 120]
    if subset.empty:
        return True, "No stores with sales > 120k to evaluate."
    condition = subset["transactions"] > 1500
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} stores with sales > 120k have transactions > 1500."
    else:
        viol = subset[~condition]
        ids = viol["store_id"].tolist()
        return False, f"{len(viol)} stores with sales > 120k violate the transaction requirement (IDs: {', '.join(ids)})."

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one store in the north region with a customer satisfaction rating greater than 4.5 and a staff count greater than 20."""
    subset = df[(df["region"] == "north") & (df["customer_satisfaction"] > 4.5) & (df["staff_count"] > 20)]
    truth = not subset.empty
    if truth:
        ids = subset["store_id"].tolist()
        return True, f"Found {len(subset)} north region store(s) with CS > 4.5 and staff > 20 (IDs: {', '.join(ids)})."
    else:
        return False, "No north region store satisfies CS > 4.5 and staff > 20."

def main():
    df = pd.read_csv("../inference_generation/tables/table_92.csv")

    # Convert numeric columns safely.
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()