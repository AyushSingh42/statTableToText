

import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All North region stores have higher monthly sales than any South or West region stores."""
    north_sales = df[df['region'] == 'North']['monthly_sales_k']
    south_west_sales = df[df['region'].isin(['South', 'West'])]['monthly_sales_k']
    max_south_west = south_west_sales.max()
    truth = north_sales.min() > max_south_west
    if truth:
        expl = f"All North stores have sales higher than max South/West sales ({max_south_west:.2f})."
    else:
        viol = df[(df['region'] == 'North') & (df['monthly_sales_k'] <= max_south_west)]
        expl = f"{len(viol)} North stores have sales <= max South/West sales ({max_south_west:.2f})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Stores with more than 20 staff members have higher average basket sizes than those with fewer staff."""
    more_20 = df[df['staff_count'] > 20]['avg_basket_size'].mean()
    less_20 = df[df['staff_count'] <= 20]['avg_basket_size'].mean()
    truth = more_20 > less_20
    expl = f"Avg basket size for >20 staff: {more_20:.2f}, <=20 staff: {less_20:.2f}."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a store's average basket size exceeds 60, its customer satisfaction score is at least 4.4."""
    viol = df[(df['avg_basket_size'] > 60) & (df['customer_satisfaction'] < 4.4)]
    truth = len(viol) == 0
    expl = f"{len(viol)} stores violate the condition (avg basket >60 but satisfaction <4.4)."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. In the East region, stores with over 2000 transactions have higher customer satisfaction than those with fewer transactions."""
    east = df[df['region'] == 'East']
    over_2000 = east[east['transactions'] > 2000]['customer_satisfaction'].mean()
    under_2000 = east[east['transactions'] <= 2000]['customer_satisfaction'].mean()
    truth = over_2000 > under_2000
    expl = f"Avg satisfaction for >2000 transactions: {over_2000:.2f}, <=2000: {under_2000:.2f}."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Every store with a customer satisfaction score above 4.5 has more than 21 transactions per staff member."""
    viol = df[(df['customer_satisfaction'] > 4.5) & (df['transactions'] / df['staff_count'] <= 21)]
    truth = len(viol) == 0
    expl = f"{len(viol)} stores violate (satisfaction >4.5 but transactions/staff <=21)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Stores in the West region have the lowest monthly sales among all regions."""
    west_sales = df[df['region'] == 'West']['monthly_sales_k']
    other_sales = df[df['region']!= 'West']['monthly_sales_k']
    min_other = other_sales.min()
    max_west = west_sales.max()
    truth = max_west < min_other
    expl = f"West max sales: {max_west:.2f}, other min sales: {min_other:.2f}."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All stores with staff counts between 14-16 have customer satisfaction scores below 4.3."""
    viol = df[(df['staff_count'].between(14, 16, inclusive=True)) & (df['customer_satisfaction'] >= 4.3)]
    truth = len(viol) == 0
    expl = f"{len(viol)} stores violate (staff 14-16 with satisfaction >=4.3)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a store's monthly sales exceed 150k, it must be located in the North region."""
    viol = df[(df['monthly_sales_k'] > 150) & (df['region']!= 'North')]
    truth = len(viol) == 0
    expl = f"{len(viol)} stores violate (sales >150k not in North)."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All stores with customer satisfaction above 4.4 have an average basket size above 59."""
    viol = df[(df['customer_satisfaction'] > 4.4) & (df['avg_basket_size'] <= 59)]
    truth = len(viol) == 0
    expl = f"{len(viol)} stores violate (satisfaction >4.4 but basket <=59)."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. In the South region, stores with higher staff counts have higher customer satisfaction scores."""
    south = df[df['region'] == 'South']
    corr = south['staff_count'].corr(south['customer_satisfaction'])
    truth = corr > 0
    expl = f"Correlation between staff and satisfaction in South: {corr:.2f}."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Stores with more than 2300 transactions have monthly sales exceeding 140k."""
    viol = df[(df['transactions'] > 2300) & (df['monthly_sales_k'] <= 140)]
    truth = len(viol) == 0
    expl = f"{len(viol)} stores violate (transactions >2300 but sales <=140k)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. The East region stores have higher average basket sizes than West region stores with similar staff counts."""
    east = df[df['region'] == 'East']
    west = df[df['region'] == 'West']
    common_staff = set(east['staff_count']).intersection(set(west['staff_count']))
    viol = []
    for sc in common_staff:
        east_sc = east[east['staff_count'] == sc]['avg_basket_size'].mean()
        west_sc = west[west['staff_count'] == sc]['avg_basket_size'].mean()
        if east_sc <= west_sc:
            viol.append(sc)
    truth = len(viol) == 0
    expl = f"{len(viol)} staff counts where East's avg basket <= West's."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. No store with fewer than 12 staff members has a customer satisfaction score above 4.0."""
    viol = df[(df['staff_count'] < 12) & (df['customer_satisfaction'] > 4.0)]
    truth = len(viol) == 0
    expl = f"{len(viol)} stores violate (staff <12 but satisfaction >4.0)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Stores where transactions exceed 2400 are exclusively in the North region."""
    viol = df[(df['transactions'] > 2400) & (df['region']!= 'North')]
    truth = len(viol) == 0
    expl = f"{len(viol)} stores violate (transactions >2400 not in North)."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. For stores with staff count between 17-20, customer satisfaction is always above 4.2."""
    viol = df[(df['staff_count'].between(17, 20, inclusive=True)) & (df['customer_satisfaction'] <= 4.2)]
    truth = len(viol) == 0
    expl = f"{len(viol)} stores violate (staff 17-20 with satisfaction <=4.2)."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_2.csv")
    df['monthly_sales_k'] = pd.to_numeric(df['monthly_sales_k'], errors='coerce')
    df['transactions'] = pd.to_numeric(df['transactions'], errors='coerce')
    df['avg_basket_size'] = pd.to_numeric(df['avg_basket_size'], errors='coerce')
    df['staff_count'] = pd.to_numeric(df['staff_count'], errors='coerce')
    df['customer_satisfaction'] = pd.to_numeric(df['customer_satisfaction'], errors='coerce')
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