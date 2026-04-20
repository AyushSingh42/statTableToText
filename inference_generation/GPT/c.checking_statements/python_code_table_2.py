import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def convert_numeric(df: pd.DataFrame) -> pd.DataFrame:
    # Convert possible numeric columns stored as strings to proper numeric types
    for col in ["monthly_sales_k", "transactions", "avg_basket_size", "staff_count", "customer_satisfaction"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

def stmt_1(df: pd.DataFrame):
    """All north region stores have customer satisfaction scores of at least 4.3."""
    north = df[df["region"].str.lower() == "north"]
    condition = north["customer_satisfaction"] >= 4.3
    truth = condition.all()
    if truth:
        expl = f"All {len(north)} north stores meet the threshold."
    else:
        viol = north[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} north stores violate (store_id: {', '.join(map(str, ids))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """All south region stores have customer satisfaction of 4.0 or higher."""
    south = df[df["region"].str.lower() == "south"]
    condition = south["customer_satisfaction"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores meet the threshold."
    else:
        viol = south[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} south stores violate (store_id: {', '.join(map(str, ids))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """The store with the highest staff count (B009) also records the highest monthly sales."""
    max_staff = df["staff_count"].max()
    top_staff = df[df["staff_count"] == max_staff]
    # Expect exactly one store and its id should be B009
    correct_id = (top_staff["store_id"] == "B009").all()
    max_sales = df["monthly_sales_k"].max()
    top_sales = df[df["monthly_sales_k"] == max_sales]
    same_store = (top_staff["store_id"].values[0] == top_sales["store_id"].values[0]) if not top_staff.empty and not top_sales.empty else False
    truth = correct_id and same_store
    if truth:
        expl = f"Store B009 has the highest staff count ({max_staff}) and also the highest sales ({max_sales}k)."
    else:
        expl = f"Highest staff count store(s): {', '.join(top_staff['store_id'].tolist())} (staff {max_staff}). Highest sales store(s): {', '.join(top_sales['store_id'].tolist())} (sales {max_sales}k)."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """Stores with an average basket size above 62 have customer satisfaction of at least 4.5."""
    subset = df[df["avg_basket_size"] > 62]
    condition = subset["customer_satisfaction"] >= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} stores with basket >62 meet the satisfaction threshold."
    else:
        viol = subset[~condition]
        ids = viol["store_id"].tolist()
        expl = f"{len(viol)} stores violate (store_id: {', '.join(map(str, ids))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """There exists a west region store with customer satisfaction below 4.0."""
    west = df[df["region"].str.lower() == "west"]
    condition = west["customer_satisfaction"] < 4.0
    truth = condition.any()
    if truth:
        viol = west[condition]
        ids = viol["store_id"].tolist()
        expl = f"Found {len(viol)} west store(s) below 4.0 (store_id: {', '.join(map(str, ids))})."
    else:
        expl = "No west store has satisfaction below 4.0."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """Most stores with staff counts of 20 or more have monthly sales exceeding 130,000."""
    subset = df[df["staff_count"] >= 20]
    if subset.empty:
        truth = False
        expl = "No stores have staff count >=20."
    else:
        condition = subset["monthly_sales_k"] > 130  # sales are in thousands
        proportion = condition.mean()
        truth = proportion > 0.5
        expl = f"{condition.sum()} out of {len(subset)} stores ({proportion:.0%}) exceed 130k."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """East region stores have average basket sizes ranging from 58.3 to 62.0."""
    east = df[df["region"].str.lower() == "east"]
    if east.empty:
        truth = False
        expl = "No east region stores found."
    else:
        min_val = east["avg_basket_size"].min()
        max_val = east["avg_basket_size"].max()
        truth = (min_val >= 58.3) and (max_val <= 62.0)
        expl = f"East basket sizes range from {min_val:.2f} to {max_val:.2f}."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """The average basket size of west region stores is below 54."""
    west = df[df["region"].str.lower() == "west"]
    if west.empty:
        truth = False
        expl = "No west region stores found."
    else:
        mean_val = west["avg_basket_size"].mean()
        truth = mean_val < 54
        expl = f"Mean basket size for west is {mean_val:.2f}."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_2.csv")
    df = convert_numeric(df)

    checks = [
        (1, stmt_1),
        (2, stmt_2),
        (3, stmt_3),
        (4, stmt_4),
        (5, stmt_5),
        (6, stmt_6),
        (7, stmt_7),
        (8, stmt_8),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()