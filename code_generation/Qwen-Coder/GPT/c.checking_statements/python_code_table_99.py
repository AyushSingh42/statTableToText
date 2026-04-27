import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All HR employees have a performance rating of at least 3.8."""
    hr_employees = df[df["department"] == "hr"]
    condition = hr_employees["performance_rating"] >= 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(hr_employees)} HR employees have performance rating >= 3.8."
    else:
        viol = hr_employees[~condition]
        expl = f"{len(viol)} HR employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All employees earning at least $10 k per month have less than 9 years of experience."""
    high_earners = df[df["monthly_salary_k"] >= 10.0]
    condition = high_earners["years_experience"] < 9.0
    truth = condition.all()
    if truth:
        expl = f"All {len(high_earners)} high earners have < 9 years experience."
    else:
        viol = high_earners[~condition]
        expl = f"{len(viol)} high earners violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All employees with a performance rating of 4.8 or higher work remotely at least 6 days per month."""
    high_performers = df[df["performance_rating"] >= 4.8]
    condition = high_performers["remote_days_month"] >= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(high_performers)} high performers work remote >= 6 days/month."
    else:
        viol = high_performers[~condition]
        expl = f"{len(viol)} high performers violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Every finance employee works remotely either 4 or 12 days per month."""
    finance_employees = df[df["department"] == "finance"]
    condition = finance_employees["remote_days_month"].isin([4, 12])
    truth = condition.all()
    if truth:
        expl = f"All {len(finance_employees)} finance employees work 4 or 12 days/month."
    else:
        viol = finance_employees[~condition]
        expl = f"{len(viol)} finance employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees handling six active projects have a performance rating of at least 4.0."""
    six_projects = df[df["projects_active"] == 6]
    condition = six_projects["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(six_projects)} employees with 6 projects have performance rating >= 4.0."
    else:
        viol = six_projects[~condition]
        expl = f"{len(viol)} employees with 6 projects violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All employees with more than 10 years of experience earn no more than $7.8 k per month."""
    experienced = df[df["years_experience"] > 10.0]
    condition = experienced["monthly_salary_k"] <= 7.8
    truth = condition.all()
    if truth:
        expl = f"All {len(experienced)} experienced employees earn <= $7.8k/month."
    else:
        viol = experienced[~condition]
        expl = f"{len(viol)} experienced employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All marketing staff have a performance rating of at least 4.4."""
    marketing_staff = df[df["department"] == "marketing"]
    condition = marketing_staff["performance_rating"] >= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing_staff)} marketing staff have performance rating >= 4.4."
    else:
        viol = marketing_staff[~condition]
        expl = f"{len(viol)} marketing staff violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees who work remotely ten or more days per month have a performance rating no higher than 4.0."""
    remote_employees = df[df["remote_days_month"] >= 10.0]
    condition = remote_employees["performance_rating"] <= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(remote_employees)} remote-heavy employees have performance rating <= 4.0."
    else:
        viol = remote_employees[~condition]
        expl = f"{len(viol)} remote-heavy employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most employees have a performance rating of at least 4.0."""
    total_count = len(df)
    qualified = df[df["performance_rating"] >= 4.0]
    proportion = len(qualified) / total_count
    truth = proportion > 0.5
    if truth:
        expl = f"{len(qualified)}/{total_count} employees (proportion: {proportion:.2%}) have performance rating >= 4.0."
    else:
        expl = f"{len(qualified)}/{total_count} employees (proportion: {proportion:.2%}) have performance rating >= 4.0."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_99.csv")

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
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()