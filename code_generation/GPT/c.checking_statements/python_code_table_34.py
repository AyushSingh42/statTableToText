import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all households with utility cost greater than 200, vehicle count is at least 1."""
    condition = (df['utility_cost'] > 200)
    subset = df[condition]
    if subset.empty:
        expl = "No households with utility cost > 200."
        return True, expl
    valid = (subset['vehicle_count'] >= 1)
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} households with utility cost > 200 have at least 1 vehicle."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} households violate the rule (utility_cost: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Every rural household uses either cable or satellite internet."""
    rural = df[df['region'] == 'rural']
    if rural.empty:
        expl = "No rural households."
        return True, expl
    valid_types = ['cable','satellite']
    valid = rural['internet_type'].isin(valid_types)
    truth = valid.all()
    if truth:
        expl = f"All {len(rural)} rural households use cable or satellite."
    else:
        viol = rural[~valid]
        expl = f"{len(viol)} rural households use other internet type ({', '.join(viol['internet_type'].tolist())})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. No urban household uses satellite internet."""
    urban = df[df['region'] == 'urban']
    if urban.empty:
        expl = "No urban households."
        return True, expl
    has_satellite = (urban['internet_type'] =='satellite')
    truth = not has_satellite.any()
    if truth:
        expl = f"No urban households use satellite internet."
    else:
        viol = urban[has_satellite]
        expl = f"{len(viol)} urban households use satellite internet."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all households with monthly income of at least $10k, rent is at least $2.2k."""
    condition = (df['monthly_income_k'] >= 10.0)
    subset = df[condition]
    if subset.empty:
        expl = "No households with income >= $10k."
        return True, expl
    valid = (subset['rent_k'] >= 2.2)
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} households with income >= $10k have rent >= $2.2k."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} households violate the rule (income: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Every satellite-internet household pays rent of at least $2.2k."""
    sat_households = df[df['internet_type'] =='satellite']
    if sat_households.empty:
        expl = "No satellite-internet households."
        return True, expl
    valid = (sat_households['rent_k'] >= 2.2)
    truth = valid.all()
    if truth:
        expl = f"All {len(sat_households)} satellite-internet households pay rent >= $2.2k."
    else:
        viol = sat_households[~valid]
        expl = f"{len(viol)} satellite-internet households pay less than $2.2k rent."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all households with six members, rent does not exceed $2.7k."""
    condition = (df['household_size'] == 6)
    subset = df[condition]
    if subset.empty:
        expl = "No households with 6 members."
        return True, expl
    valid = (subset['rent_k'] <= 2.7)
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} households with 6 members have rent <= $2.7k."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} households with 6 members have rent > $2.7k."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All cable-internet households have utility cost no greater than $217.6."""
    cable_households = df[df['internet_type'] == 'cable']
    if cable_households.empty:
        expl = "No cable-internet households."
        return True, expl
    valid = (cable_households['utility_cost'] <= 217.6)
    truth = valid.all()
    if truth:
        expl = f"All {len(cable_households)} cable-internet households have utility cost <= $217.6."
    else:
        viol = cable_households[~valid]
        expl = f"{len(viol)} cable-internet households have utility cost > $217.6."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_34.csv")

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
        (7, stmt_7)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()