import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All south region stores have customer satisfaction of at least 4.7."""
    south = df[df["region"] == "south"]
    condition = south["customer_satisfaction"] >= 4.7
    truth = condition.all()
    if truth:
        expl = f"All {len(south)} south stores satisfy the rule."
    else:
        viol = south[~condition]
        expl = f"{len(viol)} south store(s) violate the rule (customer satisfaction: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All west region stores have a staff count of at least 11."""
    west = df[df["region"] == "west"]
    condition = west["staff_count"] >= 11
    truth = condition.all()
    if truth:
        expl = f"All {len(west)} west stores satisfy the rule."
    else:
        viol = west[~condition]
        expl = f"{len(viol)} west store(s) violate the rule (staff count: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All east region stores have monthly sales between $94.9k and $131.4k."""
    east = df[df["region"] == "east"]
    condition = east["monthly_sales_k"].between(94.9, 131.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(east)} east stores satisfy the rule."
    else:
        viol = east[~condition]
        expl = f"{len(viol)} east store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All stores with a staff count of 20 or more have an average basket size of at most 65.7."""
    large_staff = df[df["staff_count"] >= 20]
    condition = large_staff["avg_basket_size"] <= 65.7
    truth = condition.all()
    if truth:
        expl = f"All {len(large_staff)} stores with staff >=20 satisfy the rule."
    else:
        viol = large_staff[~condition]
        expl = f"{len(viol)} store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with a customer satisfaction rating of 4.8 have monthly sales of at least $108.2k."""
    cs_48 = df[df["customer_satisfaction"] == 4.8]
    condition = cs_48["monthly_sales_k"] >= 108.2
    truth = condition.all()
    if truth:
        expl = f"All {len(cs_48)} stores with CS 4.8 satisfy the rule."
    else:
        viol = cs_48[~condition]
        expl = f"{len(viol)} store(s) violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with more than 2500 transactions have an average basket size of at most 66.4."""
    high_tx = df[df["transactions"] > 2500]
    condition = high_tx["avg_basket_size"] <= 66.4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_tx)} stores with >2500 transactions satisfy the rule."
    else:
        viol = high_tx[~condition]
        expl = f"{len(viol)} store(s) violate the rule (avg basket size: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most stores have a customer satisfaction rating of at least 4.0."""
    total = len(df)
    good_cs = df[df["customer_satisfaction"] >= 4.0]
    proportion = len(good_cs) / total
    truth = proportion > 0.5
    if truth:
        expl = f"{len(good_cs)} out of {total} stores ({proportion:.2%}) have CS >=4.0."
    else:
        expl = f"Only {len(good_cs)} out of {total} stores ({proportion:.2%}) have CS >=4.0."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. West region stores' average basket size ranges from 48.8 to 67.3."""
    west = df[df["region"] == "west"]
    min_val = west["avg_basket_size"].min()
    max_val = west["avg_basket_size"].max()
    condition = (min_val >= 48.8) and (max_val <= 67.3)
    truth = condition
    if truth:
        expl = f"West stores' avg basket size ranges from {min_val} to {max_val}."
    else:
        expl = f"West stores' avg basket size range is {min_val} to {max_val}, which violates the rule."
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()