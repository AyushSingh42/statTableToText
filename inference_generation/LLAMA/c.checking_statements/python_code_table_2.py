import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All stores in the north region have higher average customer satisfaction ratings than those in the west region."""
    north = df[df["region"] == "north"]
    west = df[df["region"] == "west"]
    avg_north = north["customer_satisfaction"].mean()
    avg_west = west["customer_satisfaction"].mean()
    truth = avg_north > avg_west
    if truth:
        expl = f"The average customer satisfaction rating in the north region ({avg_north:.2f}) is higher than in the west region ({avg_west:.2f})."
    else:
        expl = f"The average customer satisfaction rating in the north region ({avg_north:.2f}) is not higher than in the west region ({avg_west:.2f})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. There exists at least one store in each region with a monthly sales figure exceeding 100,000."""
    regions = df["region"].unique()
    truth = all(df[df["region"] == region]["monthly_sales_k"].gt(100).any() for region in regions)
    if truth:
        expl = "At least one store in each region has a monthly sales figure exceeding 100,000."
    else:
        viol = [region for region in regions if not df[df["region"] == region]["monthly_sales_k"].gt(100).any()]
        expl = f"No stores in the following regions have a monthly sales figure exceeding 100,000: {', '.join(viol)}."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Most stores with staff counts above 18 have average customer satisfaction ratings above 4.3."""
    above_18 = df[df["staff_count"].gt(18)]
    truth = above_18["customer_satisfaction"].gt(4.3).mean() > 0.5
    if truth:
        expl = f"{(above_18['customer_satisfaction'].gt(4.3).mean()*100):.2f}% of stores with staff counts above 18 have average customer satisfaction ratings above 4.3."
    else:
        expl = f"{(above_18['customer_satisfaction'].gt(4.3).mean()*100):.2f}% of stores with staff counts above 18 do not have average customer satisfaction ratings above 4.3."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a store is located in the east region, then it is likely to have a higher monthly sales figure than those in the south region."""
    east = df[df["region"] == "east"]
    south = df[df["region"] == "south"]
    avg_east = east["monthly_sales_k"].mean()
    avg_south = south["monthly_sales_k"].mean()
    truth = avg_east > avg_south
    if truth:
        expl = f"The average monthly sales figure in the east region ({avg_east:.2f}) is higher than in the south region ({avg_south:.2f})."
    else:
        expl = f"The average monthly sales figure in the east region ({avg_east:.2f}) is not higher than in the south region ({avg_south:.2f})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All stores with average basket sizes above 60 have customer satisfaction ratings above 4.2."""
    above_60 = df[df["avg_basket_size"].gt(60)]
    truth = above_60["customer_satisfaction"].gt(4.2).all()
    if truth:
        expl = "All stores with average basket sizes above 60 have customer satisfaction ratings above 4.2."
    else:
        viol = above_60[~above_60["customer_satisfaction"].gt(4.2)]
        expl = f"{len(viol)} stores with average basket sizes above 60 do not have customer satisfaction ratings above 4.2 (ratings: {', '.join(map(str, viol['customer_satisfaction'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. There exists at least one store in the west region with a lower staff count than the average staff count of stores in the south region."""
    south_avg = df[df["region"] == "south"]["staff_count"].mean()
    west = df[df["region"] == "west"]
    truth = west["staff_count"].lt(south_avg).any()
    if truth:
        expl = f"At least one store in the west region has a lower staff count than the average staff count of stores in the south region ({south_avg:.2f})."
    else:
        expl = f"No stores in the west region have a lower staff count than the average staff count of stores in the south region ({south_avg:.2f})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Stores in the north region tend to have higher average basket sizes than those in the south region."""
    north = df[df["region"] == "north"]
    south = df[df["region"] == "south"]
    avg_north = north["avg_basket_size"].mean()
    avg_south = south["avg_basket_size"].mean()
    truth = avg_north > avg_south
    if truth:
        expl = f"The average basket size in the north region ({avg_north:.2f}) is higher than in the south region ({avg_south:.2f})."
    else:
        expl = f"The average basket size in the north region ({avg_north:.2f}) is not higher than in the south region ({avg_south:.2f})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All stores with monthly sales figures above 150,000 have staff counts above 20."""
    above_150k = df[df["monthly_sales_k"].gt(150)]
    truth = above_150k["staff_count"].gt(20).all()
    if truth:
        expl = "All stores with monthly sales figures above 150,000 have staff counts above 20."
    else:
        viol = above_150k[~above_150k["staff_count"].gt(20)]
        expl = f"{len(viol)} stores with monthly sales figures above 150,000 do not have staff counts above 20 (staff counts: {', '.join(map(str, viol['staff_count'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most stores with customer satisfaction ratings above 4.5 are located in the north region."""
    above_45 = df[df["customer_satisfaction"].gt(4.5)]
    truth = above_45["region"].eq("north").mean() > 0.5
    if truth:
        expl = f"{(above_45['region'].eq('north').mean()*100):.2f}% of stores with customer satisfaction ratings above 4.5 are located in the north region."
    else:
        expl = f"{(above_45['region'].eq('north').mean()*100):.2f}% of stores with customer satisfaction ratings above 4.5 are not located in the north region."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a store has a staff count above 19, then it is likely to have a higher average customer satisfaction rating than those with lower staff counts."""
    above_19 = df[df["staff_count"].gt(19)]
    below_19 = df[df["staff_count"].le(19)]
    avg_above = above_19["customer_satisfaction"].mean()
    avg_below = below_19["customer_satisfaction"].mean()
    truth = avg_above > avg_below
    if truth:
        expl = f"The average customer satisfaction rating for stores with staff counts above 19 ({avg_above:.2f}) is higher than for those with lower staff counts ({avg_below:.2f})."
    else:
        expl = f"The average customer satisfaction rating for stores with staff counts above 19 ({avg_above:.2f}) is not higher than for those with lower staff counts ({avg_below:.2f})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_2.csv")
    df["monthly_sales_k"] = pd.to_numeric(df["monthly_sales_k"], errors="coerce")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()