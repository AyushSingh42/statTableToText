import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all engineering employees with more than 8 years of experience, performance rating is at most 3.8."""
    eng_expert = df[(df["department"] == "engineering") & (df["years_experience"] > 8)]
    if eng_expert.empty:
        truth = True
        expl = "No engineering employees with more than 8 years of experience."
    else:
        condition = eng_expert["performance_rating"] <= 3.8
        truth = condition.all()
        if truth:
            expl = f"All {len(eng_expert)} engineering employees with >8 years experience have performance rating <= 3.8."
        else:
            viol = eng_expert[~condition]
            expl = f"{len(viol)} engineering employees with >8 years experience violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all HR employees, monthly salary is between $6.0k and $10.1k."""
    hr_employees = df[df["department"] == "hr"]
    if hr_employees.empty:
        truth = True
        expl = "No HR employees."
    else:
        condition = hr_employees["monthly_salary_k"].between(6.0, 10.1, inclusive="both")
        truth = condition.all()
        if truth:
            expl = f"All {len(hr_employees)} HR employees have monthly salary between $6.0k and $10.1k."
        else:
            viol = hr_employees[~condition]
            expl = f"{len(viol)} HR employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all finance employees, performance rating is at least 4.2."""
    fin_employees = df[df["department"] == "finance"]
    if fin_employees.empty:
        truth = True
        expl = "No finance employees."
    else:
        condition = fin_employees["performance_rating"] >= 4.2
        truth = condition.all()
        if truth:
            expl = f"All {len(fin_employees)} finance employees have performance rating >= 4.2."
        else:
            viol = fin_employees[~condition]
            expl = f"{len(viol)} finance employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all employees who work remotely 12 or more days per month, the number of active projects does not exceed 6."""
    remote_employees = df[df["remote_days_month"] >= 12]
    if remote_employees.empty:
        truth = True
        expl = "No employees work remotely 12+ days/month."
    else:
        condition = remote_employees["projects_active"] <= 6
        truth = condition.all()
        if truth:
            expl = f"All {len(remote_employees)} employees working remotely 12+ days/month have <=6 active projects."
        else:
            viol = remote_employees[~condition]
            expl = f"{len(viol)} employees working remotely 12+ days/month violate the rule (active projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all employees with monthly salary greater than $9k, performance rating is at least 4.0."""
    high_salary = df[df["monthly_salary_k"] > 9.0]
    if high_salary.empty:
        truth = True
        expl = "No employees with monthly salary >$9k."
    else:
        condition = high_salary["performance_rating"] >= 4.0
        truth = condition.all()
        if truth:
            expl = f"All {len(high_salary)} employees with monthly salary >$9k have performance rating >= 4.0."
        else:
            viol = high_salary[~condition]
            expl = f"{len(viol)} employees with monthly salary >$9k violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most employees have at least four active projects."""
    condition = df["projects_active"] >= 4
    count_ge_four = condition.sum()
    total = len(df)
    truth = count_ge_four > total / 2
    if truth:
        expl = f"{count_ge_four} out of {total} employees have at least 4 active projects (more than half)."
    else:
        expl = f"{count_ge_four} out of {total} employees have at least 4 active projects (not more than half)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. There exists at least one marketing employee with a performance rating above 4.5."""
    marketing = df[df["department"] == "marketing"]
    if marketing.empty:
        truth = False
        expl = "No marketing employees."
    else:
        condition = marketing["performance_rating"] > 4.5
        truth = condition.any()
        if truth:
            expl = f"At least one marketing employee has performance rating > 4.5."
        else:
            expl = f"No marketing employees have performance rating > 4.5."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all employees with less than 2 years of experience, performance rating is at least 4.3."""
    low_exp = df[df["years_experience"] < 2]
    if low_exp.empty:
        truth = True
        expl = "No employees with less than 2 years of experience."
    else:
        condition = low_exp["performance_rating"] >= 4.3
        truth = condition.all()
        if truth:
            expl = f"All {len(low_exp)} employees with <2 years experience have performance rating >= 4.3."
        else:
            viol = low_exp[~condition]
            expl = f"{len(viol)} employees with <2 years experience violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. For all employees with six active projects, monthly salary does not exceed $8.6k."""
    six_projects = df[df["projects_active"] == 6]
    if six_projects.empty:
        truth = True
        expl = "No employees with exactly 6 active projects."
    else:
        condition = six_projects["monthly_salary_k"] <= 8.6
        truth = condition.all()
        if truth:
            expl = f"All {len(six_projects)} employees with 6 active projects have monthly salary <= $8.6k."
        else:
            viol = six_projects[~condition]
            expl = f"{len(viol)} employees with 6 active projects violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. For all employees with a performance rating of at least 4.6, monthly salary is at least $7.3k."""
    high_rating = df[df["performance_rating"] >= 4.6]
    if high_rating.empty:
        truth = True
        expl = "No employees with performance rating >= 4.6."
    else:
        condition = high_rating["monthly_salary_k"] >= 7.3
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rating)} employees with performance rating >= 4.6 have monthly salary >= $7.3k."
        else:
            viol = high_rating[~condition]
            expl = f"{len(viol)} employees with performance rating >= 4.6 violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_79.csv")

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
        (9, stmt_9),
        (10, stmt_10)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()