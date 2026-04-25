import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All finance employees have monthly salary ≤ $8.9k."""
    finance_employees = df[df["department"] == "finance"]
    condition = finance_employees["monthly_salary_k"] <= 8.9
    truth = condition.all()
    if truth:
        expl = f"All {len(finance_employees)} finance employees have salary ≤ $8.9k."
    else:
        viol = finance_employees[~condition]
        expl = f"{len(viol)} finance employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All employees with performance rating at least 4.7 work remotely at least 6 days per month."""
    high_performers = df[df["performance_rating"] >= 4.7]
    condition = high_performers["remote_days_month"] >= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(high_performers)} high-performing employees work remotely ≥ 6 days/month."
    else:
        viol = high_performers[~condition]
        expl = f"{len(viol)} high-performing employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All employees with more than 10 years of experience have monthly salary at least $5.5k."""
    experienced = df[df["years_experience"] > 10]
    condition = experienced["monthly_salary_k"] >= 5.5
    truth = condition.all()
    if truth:
        expl = f"All {len(experienced)} experienced employees have salary ≥ $5.5k."
    else:
        viol = experienced[~condition]
        expl = f"{len(viol)} experienced employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All engineering employees are assigned to at least 4 active projects."""
    engineers = df[df["department"] == "engineering"]
    condition = engineers["projects_active"] >= 4
    truth = condition.all()
    if truth:
        expl = f"All {len(engineers)} engineering employees are assigned to ≥ 4 active projects."
    else:
        viol = engineers[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (active projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees earning more than $10k per month have performance rating of at least 4.0."""
    high_earners = df[df["monthly_salary_k"] > 10]
    condition = high_earners["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(high_earners)} high earners have performance rating ≥ 4.0."
    else:
        viol = high_earners[~condition]
        expl = f"{len(viol)} high earners violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most employees work remotely at least 5 days per month."""
    condition = df["remote_days_month"] >= 5
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} employees work remotely ≥ 5 days/month (majority)."
    else:
        expl = f"{count} out of {total} employees work remotely ≥ 5 days/month (not majority)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All HR employees have performance rating of at least 3.8."""
    hr_employees = df[df["department"] == "hr"]
    condition = hr_employees["performance_rating"] >= 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(hr_employees)} HR employees have performance rating ≥ 3.8."
    else:
        viol = hr_employees[~condition]
        expl = f"{len(viol)} HR employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All marketing employees work remotely no more than 6 days per month."""
    marketing_employees = df[df["department"] == "marketing"]
    condition = marketing_employees["remote_days_month"] <= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing_employees)} marketing employees work remotely ≤ 6 days/month."
    else:
        viol = marketing_employees[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_39.csv")

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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()