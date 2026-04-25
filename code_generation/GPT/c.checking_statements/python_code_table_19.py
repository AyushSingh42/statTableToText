import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All finance employees have a monthly salary of at least $5.5k."""
    finance = df[df["department"] == "finance"]
    condition = finance["monthly_salary_k"] >= 5.5
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have a salary >= $5.5k."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All operations employees have a performance rating of at least 4.1."""
    operations = df[df["department"] == "operations"]
    condition = operations["performance_rating"] >= 4.1
    truth = condition.all()
    if truth:
        expl = f"All {len(operations)} operations employees have a rating >= 4.1."
    else:
        viol = operations[~condition]
        expl = f"{len(viol)} operations employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All engineering employees have at least 3 active projects."""
    engineering = df[df["department"] == "engineering"]
    condition = engineering["projects_active"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(engineering)} engineering employees have >= 3 projects."
    else:
        viol = engineering[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (project counts: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 10 years of experience have a monthly salary of at most $9.3k."""
    experienced = df[df["years_experience"] > 10]
    condition = experienced["monthly_salary_k"] <= 9.3
    truth = condition.all()
    if truth:
        expl = f"All {len(experienced)} employees with >10 years have a salary <= $9.3k."
    else:
        viol = experienced[~condition]
        expl = f"{len(viol)} employees with >10 years violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees who work remotely 13 or more days per month have a performance rating of at least 4.0."""
    remote = df[df["remote_days_month"] >= 13]
    condition = remote["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(remote)} remote workers (>=13 days) have a rating >= 4.0."
    else:
        viol = remote[~condition]
        expl = f"{len(viol)} remote workers violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All HR employees have a performance rating of at most 4.1."""
    hr = df[df["department"] == "hr"]
    condition = hr["performance_rating"] <= 4.1
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have a rating <= 4.1."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees with a monthly salary greater than $10k have at most 6.7 years of experience."""
    high_salary = df[df["monthly_salary_k"] > 10]
    condition = high_salary["years_experience"] <= 6.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_salary)} high-salary employees have <= 6.7 years experience."
    else:
        viol = high_salary[~condition]
        expl = f"{len(viol)} high-salary employees violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most employees have a performance rating of at least 4.0."""
    total = len(df)
    qualified = len(df[df["performance_rating"] >= 4.0])
    truth = qualified > total / 2
    expl = f"{qualified} out of {total} employees have a rating >= 4.0. {'Most' if truth else 'Not most'} employees qualify."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_19.csv")

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