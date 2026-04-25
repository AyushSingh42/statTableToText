import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All finance employees have a monthly salary between $8.6k and $9.4k."""
    finance = df[df["department"] == "finance"]
    condition = finance["monthly_salary_k"].between(8.6, 9.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have salaries between $8.6k and $9.4k."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All engineering employees have a performance rating of at least 4.2."""
    engineering = df[df["department"] == "engineering"]
    condition = engineering["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(engineering)} engineering employees have performance ratings of at least 4.2."
    else:
        viol = engineering[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All marketing employees are involved in at least 2 active projects."""
    marketing = df[df["department"] == "marketing"]
    condition = marketing["projects_active"] >= 2
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees are involved in at least 2 active projects."
    else:
        viol = marketing[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (project counts: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All HR employees work remotely between 5 and 10 days per month."""
    hr = df[df["department"] == "hr"]
    condition = hr["remote_days_month"].between(5, 10, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees work remotely between 5 and 10 days per month."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees with five or more active projects have a performance rating of at least 4.1."""
    high_projects = df[df["projects_active"] >= 5]
    condition = high_projects["performance_rating"] >= 4.1
    truth = condition.all()
    if truth:
        expl = f"All {len(high_projects)} employees with 5+ projects have performance ratings of at least 4.1."
    else:
        viol = high_projects[~condition]
        expl = f"{len(viol)} employees with 5+ projects violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All employees with two or fewer years of experience have a performance rating of at least 4.2."""
    low_experience = df[df["years_experience"] <= 2]
    condition = low_experience["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(low_experience)} employees with 2 or fewer years of experience have performance ratings of at least 4.2."
    else:
        viol = low_experience[~condition]
        expl = f"{len(viol)} employees with 2 or fewer years of experience violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All finance employees have a performance rating of at least 3.8."""
    finance = df[df["department"] == "finance"]
    condition = finance["performance_rating"] >= 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have performance ratings of at least 3.8."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees who work remotely 13 or more days per month have a monthly salary of at most $8.9k."""
    remote_high = df[df["remote_days_month"] >= 13]
    condition = remote_high["monthly_salary_k"] <= 8.9
    truth = condition.all()
    if truth:
        expl = f"All {len(remote_high)} employees working remotely 13+ days have salaries of at most $8.9k."
    else:
        viol = remote_high[~condition]
        expl = f"{len(viol)} employees working remotely 13+ days violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most employees have a performance rating of at least 4.0."""
    condition = df["performance_rating"] >= 4.0
    count_ge_4 = condition.sum()
    total = len(df)
    truth = count_ge_4 > total / 2
    if truth:
        expl = f"{count_ge_4} out of {total} employees have performance ratings of at least 4.0 (more than half)."
    else:
        expl = f"{count_ge_4} out of {total} employees have performance ratings of at least 4.0 (not more than half)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_29.csv")

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