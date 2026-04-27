import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All finance employees have monthly salary ≤ $8.9k."""
    finance = df[df["department"] == "finance"]
    condition = finance["monthly_salary_k"] <= 8.9
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have salary ≤ 8.9k."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employee(s) violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All employees with performance rating at least 4.7 work remotely at least 6 days per month."""
    high_perf = df[df["performance_rating"] >= 4.7]
    condition = high_perf["remote_days_month"] >= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf)} high‑rating employees work remotely ≥ 6 days."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employee(s) with rating ≥ 4.7 work remotely < 6 days (days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All employees with more than 10 years of experience have monthly salary at least $5.5k."""
    experienced = df[df["years_experience"] > 10]
    condition = experienced["monthly_salary_k"] >= 5.5
    truth = condition.all()
    if truth:
        expl = f"All {len(experienced)} employees with >10 years experience have salary ≥ 5.5k."
    else:
        viol = experienced[~condition]
        expl = f"{len(viol)} employee(s) with >10 years experience have salary < 5.5k (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All engineering employees are assigned to at least 4 active projects."""
    eng = df[df["department"] == "engineering"]
    condition = eng["projects_active"] >= 4
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have ≥ 4 active projects."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} engineering employee(s) have < 4 active projects (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees earning more than $10k per month have performance rating of at least 4.0."""
    high_salary = df[df["monthly_salary_k"] > 10]
    condition = high_salary["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(high_salary)} employees earning >10k have rating ≥ 4.0."
    else:
        viol = high_salary[~condition]
        expl = f"{len(viol)} employee(s) earning >10k have rating < 4.0 (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most employees work remotely at least 5 days per month."""
    total = len(df)
    at_least_5 = df[df["remote_days_month"] >= 5]
    proportion = len(at_least_5) / total if total > 0 else 0
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of employees work remotely ≥ 5 days."
    else:
        expl = f"Only {proportion*100:.1f}% of employees work remotely ≥ 5 days."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All HR employees have performance rating of at least 3.8."""
    hr = df[df["department"] == "HR"]
    if len(hr) == 0:
        return True, "No HR employees present; statement vacuously true."
    condition = hr["performance_rating"] >= 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have rating ≥ 3.8."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employee(s) have rating < 3.8 (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All marketing employees work remotely no more than 6 days per month."""
    marketing = df[df["department"] == "marketing"]
    if len(marketing) == 0:
        return True, "No marketing employees present; statement vacuously true."
    condition = marketing["remote_days_month"] <= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees work remotely ≤ 6 days."
    else:
        viol = marketing[~condition]
        expl = f"{len(viol)} marketing employee(s) work remotely > 6 days (days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_39.csv")
    df = df.apply(pd.to_numeric, errors='ignore')
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