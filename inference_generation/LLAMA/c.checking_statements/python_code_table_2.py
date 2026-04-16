import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the north region have higher average basket sizes than those in the west region."""
    north = df[df["region"] == "north"]
    west = df[df["region"] == "west"]
    avg_north = north["avg_basket_size"].mean()
    avg_west = west["avg_basket_size"].mean()
    truth = avg_north > avg_west
    if truth:
        expl = f"The average basket size in the north region ({avg_north:.2f}) is higher than in the west region ({avg_west:.2f})."
    else:
        expl = f"The average basket size in the north region ({avg_north:.2f}) is not higher than in the west region ({avg_west:.2f})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a store has a high customer satisfaction rating (above 4.4), then it also has a high staff count (above 18)."""
    high_satisfaction = df[df["customer_satisfaction"] > 4.4]
    high_staff = high_satisfaction[high_satisfaction["staff_count"] > 18]
    truth = len(high_staff) == len(high_satisfaction)
    if truth:
        expl = f"All {len(high_satisfaction)} stores with high customer satisfaction also have high staff counts."
    else:
        viol = high_satisfaction[~(high_satisfaction["staff_count"] > 18)]
        expl = f"{len(viol)} stores with high customer satisfaction violate the rule (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every store with monthly sales above 150k is located in either the north or east region."""
    high_sales = df[df["monthly_sales_k"] > 150]
    north_or_east = high_sales[high_sales["region"].isin(["north", "east"])]
    truth = len(north_or_east) == len(high_sales)
    if truth:
        expl = f"All {len(high_sales)} stores with high monthly sales are located in the north or east region."
    else:
        viol = high_sales[~(high_sales["region"].isin(["north", "east"]))]
        expl = f"{len(viol)} stores with high monthly sales violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Stores in the south region have a lower average basket size than those in the east region, but a higher staff count."""
    south = df[df["region"] == "south"]
    east = df[df["region"] == "east"]
    avg_south = south["avg_basket_size"].mean()
    avg_east = east["avg_basket_size"].mean()
    avg_staff_south = south["staff_count"].mean()
    avg_staff_east = east["staff_count"].mean()
    truth = avg_south < avg_east and avg_staff_south > avg_staff_east
    if truth:
        expl = f"The average basket size in the south region ({avg_south:.2f}) is lower than in the east region ({avg_east:.2f}), and the average staff count in the south region ({avg_staff_south:.2f}) is higher than in the east region ({avg_staff_east:.2f})."
    else:
        expl = f"The average basket size in the south region ({avg_south:.2f}) is not lower than in the east region ({avg_east:.2f}), or the average staff count in the south region ({avg_staff_south:.2f}) is not higher than in the east region ({avg_staff_east:.2f})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a store has a high transaction count (above 2200), then it also has a high monthly sales figure (above 120k)."""
    high_transactions = df[df["transactions"] > 2200]
    high_sales = high_transactions[high_transactions["monthly_sales_k"] > 120]
    truth = len(high_sales) == len(high_transactions)
    if truth:
        expl = f"All {len(high_transactions)} stores with high transaction counts also have high monthly sales."
    else:
        viol = high_transactions[~(high_transactions["monthly_sales_k"] > 120)]
        expl = f"{len(viol)} stores with high transaction counts violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All stores with a low customer satisfaction rating (below 4.0) are located in the west or south region."""
    low_satisfaction = df[df["customer_satisfaction"] < 4.0]
    west_or_south = low_satisfaction[low_satisfaction["region"].isin(["west", "south"])]
    truth = len(west_or_south) == len(low_satisfaction)
    if truth:
        expl = f"All {len(low_satisfaction)} stores with low customer satisfaction are located in the west or south region."
    else:
        viol = low_satisfaction[~(low_satisfaction["region"].isin(["west", "south"]))]
        expl = f"{len(viol)} stores with low customer satisfaction violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Stores in the east region have a higher average basket size than those in the south region, but a lower staff count."""
    east = df[df["region"] == "east"]
    south = df[df["region"] == "south"]
    avg_east = east["avg_basket_size"].mean()
    avg_south = south["avg_basket_size"].mean()
    avg_staff_east = east["staff_count"].mean()
    avg_staff_south = south["staff_count"].mean()
    truth = avg_east > avg_south and avg_staff_east < avg_staff_south
    if truth:
        expl = f"The average basket size in the east region ({avg_east:.2f}) is higher than in the south region ({avg_south:.2f}), and the average staff count in the east region ({avg_staff_east:.2f}) is lower than in the south region ({avg_staff_south:.2f})."
    else:
        expl = f"The average basket size in the east region ({avg_east:.2f}) is not higher than in the south region ({avg_south:.2f}), or the average staff count in the east region ({avg_staff_east:.2f}) is not lower than in the south region ({avg_staff_south:.2f})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Every store with a high staff count (above 20) is located in either the north or east region."""
    high_staff = df[df["staff_count"] > 20]
    north_or_east = high_staff[high_staff["region"].isin(["north", "east"])]
    truth = len(north_or_east) == len(high_staff)
    if truth:
        expl = f"All {len(high_staff)} stores with high staff counts are located in the north or east region."
    else:
        viol = high_staff[~(high_staff["region"].isin(["north", "east"]))]
        expl = f"{len(viol)} stores with high staff counts violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a store has a low monthly sales figure (below 100k), then it also has a low transaction count (below 1800)."""
    low_sales = df[df["monthly_sales_k"] < 100]
    low_transactions = low_sales[low_sales["transactions"] < 1800]
    truth = len(low_transactions) == len(low_sales)
    if truth:
        expl = f"All {len(low_sales)} stores with low monthly sales also have low transaction counts."
    else:
        viol = low_sales[~(low_sales["transactions"] < 1800)]
        expl = f"{len(viol)} stores with low monthly sales violate the rule (transaction counts: {', '.join(map(str, viol['transactions'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Stores in the north region have a higher customer satisfaction rating than those in the west region, but a lower staff count."""
    north = df[df["region"] == "north"]
    west = df[df["region"] == "west"]
    avg_satisfaction_north = north["customer_satisfaction"].mean()
    avg_satisfaction_west = west["customer_satisfaction"].mean()
    avg_staff_north = north["staff_count"].mean()
    avg_staff_west = west["staff_count"].mean()
    truth = avg_satisfaction_north > avg_satisfaction_west and avg_staff_north < avg_staff_west
    if truth:
        expl = f"The average customer satisfaction rating in the north region ({avg_satisfaction_north:.2f}) is higher than in the west region ({avg_satisfaction_west:.2f}), and the average staff count in the north region ({avg_staff_north:.2f}) is lower than in the west region ({avg_staff_west:.2f})."
    else:
        expl = f"The average customer satisfaction rating in the north region ({avg_satisfaction_north:.2f}) is not higher than in the west region ({avg_satisfaction_west:.2f}), or the average staff count in the north region ({avg_staff_north:.2f}) is not lower than in the west region ({avg_staff_west:.2f})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All stores with a high average basket size (above 60) are located in either the north or east region."""
    high_basket = df[df["avg_basket_size"] > 60]
    north_or_east = high_basket[high_basket["region"].isin(["north", "east"])]
    truth = len(north_or_east) == len(high_basket)
    if truth:
        expl = f"All {len(high_basket)} stores with high average basket sizes are located in the north or east region."
    else:
        viol = high_basket[~(high_basket["region"].isin(["north", "east"]))]
        expl = f"{len(viol)} stores with high average basket sizes violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a store has a high customer satisfaction rating (above 4.5), then it also has a high monthly sales figure (above 140k)."""
    high_satisfaction = df[df["customer_satisfaction"] > 4.5]
    high_sales = high_satisfaction[high_satisfaction["monthly_sales_k"] > 140]
    truth = len(high_sales) == len(high_satisfaction)
    if truth:
        expl = f"All {len(high_satisfaction)} stores with high customer satisfaction also have high monthly sales."
    else:
        viol = high_satisfaction[~(high_satisfaction["monthly_sales_k"] > 140)]
        expl = f"{len(viol)} stores with high customer satisfaction violate the rule (monthly sales: {', '.join(map(str, viol['monthly_sales_k'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Stores in the south region have a lower monthly sales figure than those in the east region, but a higher transaction count."""
    south = df[df["region"] == "south"]
    east = df[df["region"] == "east"]
    avg_sales_south = south["monthly_sales_k"].mean()
    avg_sales_east = east["monthly_sales_k"].mean()
    avg_transactions_south = south["transactions"].mean()
    avg_transactions_east = east["transactions"].mean()
    truth = avg_sales_south < avg_sales_east and avg_transactions_south > avg_transactions_east
    if truth:
        expl = f"The average monthly sales figure in the south region ({avg_sales_south:.2f}) is lower than in the east region ({avg_sales_east:.2f}), and the average transaction count in the south region ({avg_transactions_south:.2f}) is higher than in the east region ({avg_transactions_east:.2f})."
    else:
        expl = f"The average monthly sales figure in the south region ({avg_sales_south:.2f}) is not lower than in the east region ({avg_sales_east:.2f}), or the average transaction count in the south region ({avg_transactions_south:.2f}) is not higher than in the east region ({avg_transactions_east:.2f})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Every store with a low staff count (below 15) is located in either the west or south region."""
    low_staff = df[df["staff_count"] < 15]
    west_or_south = low_staff[low_staff["region"].isin(["west", "south"])]
    truth = len(west_or_south) == len(low_staff)
    if truth:
        expl = f"All {len(low_staff)} stores with low staff counts are located in the west or south region."
    else:
        viol = low_staff[~(low_staff["region"].isin(["west", "south"]))]
        expl = f"{len(viol)} stores with low staff counts violate the rule (regions: {', '.join(map(str, viol['region'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a store has a high transaction count (above 2400), then it also has a high average basket size (above 62)."""
    high_transactions = df[df["transactions"] > 2400]
    high_basket = high_transactions[high_transactions["avg_basket_size"] > 62]
    truth = len(high_basket) == len(high_transactions)
    if truth:
        expl = f"All {len(high_transactions)} stores with high transaction counts also have high average basket sizes."
    else:
        viol = high_transactions[~(high_transactions["avg_basket_size"] > 62)]
        expl = f"{len(viol)} stores with high transaction counts violate the rule (average basket sizes: {', '.join(map(str, viol['avg_basket_size'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_2.csv")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10), (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()