import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all engineering employees, monthly salary is at most $7.6k."""
    eng_employees = df[df["department"] == "engineering"]
    condition = eng_employees["monthly_salary_k"] <= 7.6
    truth = condition.all()
    if truth:
        expl = f"All {len(eng_employees)} engineering employees earn at most $7.6k."
    else:
        viol = eng_employees[~condition]
        expl = f"{len(viol)} engineering employees exceed $7.6k (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All HR employees have a performance rating of at least 4.2."""
    hr_employees = df[df["department"] == "hr"]
    condition = hr_employees["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(hr_employees)} HR employees have performance rating >= 4.2."
    else:
        viol = hr_employees[~condition]
        expl = f"{len(viol)} HR employees have rating < 4.2 (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All finance employees are involved in at least two active projects."""
    fin_employees = df[df["department"] == "finance"]
    condition = fin_employees["projects_active"] >= 2
    truth = condition.all()
    if truth:
        expl = f"All {len(fin_employees)} finance employees are in at least 2 projects."
    else:
        viol = fin_employees[~condition]
        expl = f"{len(viol)} finance employees are in fewer than 2 projects (project counts: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with six active projects have monthly salary at most $7.4k."""
    emp_with_six_proj = df[df["projects_active"] == 6]
    condition = emp_with_six_proj["monthly_salary_k"] <= 7.4
    truth = condition.all()
    if truth:
        expl = f"All {len(emp_with_six_proj)} employees with 6 projects earn at most $7.4k."
    else:
        viol = emp_with_six_proj[~condition]
        expl = f"{len(viol)} employees with 6 projects exceed $7.4k (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees who work remotely fourteen or more days per month have a performance rating of at least 4.2."""
    remote_14_plus = df[df["remote_days_month"] >= 14]
    condition = remote_14_plus["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(remote_14_plus)} employees working remotely ≥14 days have performance rating ≥4.2."
    else:
        viol = remote_14_plus[~condition]
        expl = f"{len(viol)} employees working remotely ≥14 days have rating < 4.2 (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All operations employees work remotely no more than nine days per month."""
    ops_employees = df[df["department"] == "operations"]
    condition = ops_employees["remote_days_month"] <= 9
    truth = condition.all()
    if truth:
        expl = f"All {len(ops_employees)} operations employees work ≤9 days remotely."
    else:
        viol = ops_employees[~condition]
        expl = f"{len(viol)} operations employees work >9 days remotely (days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most employees have a performance rating of at least 4.0."""
    condition = df["performance_rating"] >= 4.0
    count_ge_4 = condition.sum()
    total_count = len(df)
    truth = count_ge_4 > total_count / 2
    if truth:
        expl = f"{count_ge_4} out of {total_count} employees have performance rating ≥4.0 (more than half)."
    else:
        expl = f"{count_ge_4} out of {total_count} employees have performance rating ≥4.0 (not more than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees earning more than $9k per month work remotely no more than eight days per month."""
    high_earners = df[df["monthly_salary_k"] > 9.0]
    condition = high_earners["remote_days_month"] <= 8
    truth = condition.all()
    if truth:
        expl = f"All {len(high_earners)} employees earning >$9k work ≤8 days remotely."
    else:
        viol = high_earners[~condition]
        expl = f"{len(viol)} employees earning >$9k work >8 days remotely (days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All marketing employees are involved in at least three active projects."""
    mrkt_employees = df[df["department"] == "marketing"]
    condition = mrkt_employees["projects_active"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(mrkt_employees)} marketing employees are in at least 3 projects."
    else:
        viol = mrkt_employees[~condition]
        expl = f"{len(viol)} marketing employees are in fewer than 3 projects (project counts: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with at least twelve years of experience have a performance rating of at least 4.0."""
    exp_12_plus = df[df["years_experience"] >= 12]
    condition = exp_12_plus["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(exp_12_plus)} employees with ≥12 years experience have performance rating ≥4.0."
    else:
        viol = exp_12_plus[~condition]
        expl = f"{len(viol)} employees with ≥12 years experience have rating < 4.0 (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_9.csv")

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