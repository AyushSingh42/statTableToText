import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All HR employees work remotely at least 4 days per month."""
    hr_employees = df[df["department"] == "hr"]
    condition = hr_employees["remote_days_month"] >= 4
    truth = condition.all()
    if truth:
        expl = f"All {len(hr_employees)} HR employees work remotely at least 4 days/month."
    else:
        viol = hr_employees[~condition]
        expl = f"{len(viol)} HR employees work remotely less than 4 days/month (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All employees with a performance rating of 4.5 or higher earn a monthly salary of at least $6.2k."""
    high_performers = df[df["performance_rating"] >= 4.5]
    condition = high_performers["monthly_salary_k"] >= 6.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_performers)} high-performing employees earn at least $6.2k/month."
    else:
        viol = high_performers[~condition]
        expl = f"{len(viol)} high-performing employees earn less than $6.2k/month (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every employee with more than 9 years of experience has a performance rating of at least 4.0."""
    experienced = df[df["years_experience"] > 9]
    condition = experienced["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(experienced)} employees with >9 years experience have performance rating ≥ 4.0."
    else:
        viol = experienced[~condition]
        expl = f"{len(viol)} employees with >9 years experience have performance rating < 4.0 (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees handling six active projects have a performance rating of at least 3.9."""
    many_projects = df[df["projects_active"] == 6]
    condition = many_projects["performance_rating"] >= 3.9
    truth = condition.all()
    if truth:
        expl = f"All {len(many_projects)} employees with 6 active projects have performance rating ≥ 3.9."
    else:
        viol = many_projects[~condition]
        expl = f"{len(viol)} employees with 6 active projects have performance rating < 3.9 (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All finance department employees earn no more than $8.5k per month."""
    finance_employees = df[df["department"] == "finance"]
    condition = finance_employees["monthly_salary_k"] <= 8.5
    truth = condition.all()
    if truth:
        expl = f"All {len(finance_employees)} finance employees earn ≤ $8.5k/month."
    else:
        viol = finance_employees[~condition]
        expl = f"{len(viol)} finance employees earn more than $8.5k/month (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All employees earning more than $10k per month have 8.5 years of experience or less."""
    high_earners = df[df["monthly_salary_k"] > 10]
    condition = high_earners["years_experience"] <= 8.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_earners)} employees earning >$10k/month have ≤8.5 years experience."
    else:
        viol = high_earners[~condition]
        expl = f"{len(viol)} employees earning >$10k/month have >8.5 years experience (years: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every employee with a performance rating of 4.6 or higher receives a monthly salary of at least $6.4k."""
    top_performers = df[df["performance_rating"] >= 4.6]
    condition = top_performers["monthly_salary_k"] >= 6.4
    truth = condition.all()
    if truth:
        expl = f"All {len(top_performers)} top-performing employees receive ≥$6.4k/month."
    else:
        viol = top_performers[~condition]
        expl = f"{len(viol)} top-performing employees receive < $6.4k/month (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If an operations employee has at least 8 years of experience, their performance rating is at least 4.6."""
    ops_employees = df[df["department"] == "operations"]
    qualified = ops_employees[ops_employees["years_experience"] >= 8]
    condition = qualified["performance_rating"] >= 4.6
    truth = condition.all()
    if truth:
        expl = f"All {len(qualified)} operations employees with ≥8 years experience have performance rating ≥ 4.6."
    else:
        viol = qualified[~condition]
        expl = f"{len(viol)} operations employees with ≥8 years experience have performance rating < 4.6 (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most employees have a performance rating of at least 4.0."""
    total = len(df)
    high_rated = df[df["performance_rating"] >= 4.0]
    truth = len(high_rated) > total / 2
    if truth:
        expl = f"{len(high_rated)} out of {total} employees have performance rating ≥ 4.0 (more than half)."
    else:
        expl = f"{len(high_rated)} out of {total} employees have performance rating ≥ 4.0 (not more than half)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_49.csv")

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