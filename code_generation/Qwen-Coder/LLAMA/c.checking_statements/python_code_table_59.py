import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the operations department have a monthly salary less than or equal to $10.3k."""
    ops = df[df["department"] == "operations"]
    if ops.empty:
        truth = True
        expl = "No employees in operations department."
    else:
        condition = ops["monthly_salary_k"] <= 10.3
        truth = condition.all()
        if truth:
            expl = f"All {len(ops)} operations employees have salary <= 10.3k."
        else:
            viol = ops[~condition]
            expl = f"{len(viol)} operations employees have salary > 10.3k."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If an employee is in the marketing department, then their years of experience are either less than 2 or greater than 10."""
    marketing = df[df["department"] == "marketing"]
    if marketing.empty:
        truth = True
        expl = "No employees in marketing department."
    else:
        condition = (marketing["years_experience"] < 2) | (marketing["years_experience"] > 10)
        truth = condition.all()
        if truth:
            expl = f"All {len(marketing)} marketing employees satisfy the experience condition."
        else:
            viol = marketing[~condition]
            expl = f"{len(viol)} marketing employees violate the experience condition."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one employee in the engineering department whose performance rating is less than 4."""
    eng = df[df["department"] == "engineering"]
    if eng.empty:
        truth = False
        expl = "No employees in engineering department."
    else:
        condition = eng["performance_rating"] < 4
        truth = condition.any()
        if truth:
            count = condition.sum()
            expl = f"{count} engineering employee(s) have performance rating < 4."
        else:
            expl = "No engineering employees have performance rating < 4."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 5 years of experience have a monthly salary greater than or equal to $7.7k."""
    exp = df[df["years_experience"] > 5]
    if exp.empty:
        truth = True
        expl = "No employees with >5 years experience."
    else:
        condition = exp["monthly_salary_k"] >= 7.7
        truth = condition.all()
        if truth:
            expl = f"All {len(exp)} employees with >5 years experience have salary >= 7.7k."
        else:
            viol = exp[~condition]
            expl = f"{len(viol)} employees with >5 years experience have salary < 7.7k."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If an employee is in the hr department, then their monthly salary is less than or equal to $7.7k."""
    hr = df[df["department"] == "hr"]
    if hr.empty:
        truth = True
        expl = "No employees in hr department."
    else:
        condition = hr["monthly_salary_k"] <= 7.7
        truth = condition.all()
        if truth:
            expl = f"All {len(hr)} hr employees have salary <= 7.7k."
        else:
            viol = hr[~condition]
            expl = f"{len(viol)} hr employees have salary > 7.7k."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most employees have a performance rating greater than 4."""
    condition = df["performance_rating"] > 4
    total = len(df)
    count = condition.sum()
    truth = count > total / 2
    expl = f"{count}/{total} employees have performance rating > 4."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees with a monthly salary greater than $10k have a performance rating greater than 3.8."""
    high_salary = df[df["monthly_salary_k"] > 10]
    if high_salary.empty:
        truth = True
        expl = "No employees with salary > 10k."
    else:
        condition = high_salary["performance_rating"] > 3.8
        truth = condition.all()
        if truth:
            expl = f"All {len(high_salary)} employees with salary > 10k have performance rating > 3.8."
        else:
            viol = high_salary[~condition]
            expl = f"{len(viol)} employees with salary > 10k have performance rating <= 3.8."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If an employee has more than 5 projects active, then their performance rating is less than 4.8."""
    many_projects = df[df["projects_active"] > 5]
    if many_projects.empty:
        truth = True
        expl = "No employees with >5 projects active."
    else:
        condition = many_projects["performance_rating"] < 4.8
        truth = condition.all()
        if truth:
            expl = f"All {len(many_projects)} employees with >5 projects have performance rating < 4.8."
        else:
            viol = many_projects[~condition]
            expl = f"{len(viol)} employees with >5 projects have performance rating >= 4.8."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one employee in the finance department whose years of experience are greater than 7."""
    fin = df[df["department"] == "finance"]
    if fin.empty:
        truth = False
        expl = "No employees in finance department."
    else:
        condition = fin["years_experience"] > 7
        truth = condition.any()
        if truth:
            count = condition.sum()
            expl = f"{count} finance employee(s) have years of experience > 7."
        else:
            expl = "No finance employees have years of experience > 7."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with a monthly salary less than or equal to $6.7k are in the hr department."""
    low_salary = df[df["monthly_salary_k"] <= 6.7]
    if low_salary.empty:
        truth = True
        expl = "No employees with salary <= 6.7k."
    else:
        condition = low_salary["department"] == "hr"
        truth = condition.all()
        if truth:
            expl = f"All {len(low_salary)} employees with salary <= 6.7k are in hr department."
        else:
            viol = low_salary[~condition]
            expl = f"{len(viol)} employees with salary <= 6.7k are not in hr department."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If an employee is in the operations department, then their remote days per month are either 5 or 14."""
    ops = df[df["department"] == "operations"]
    if ops.empty:
        truth = True
        expl = "No employees in operations department."
    else:
        condition = (ops["remote_days_month"] == 5) | (ops["remote_days_month"] == 14)
        truth = condition.all()
        if truth:
            expl = f"All {len(ops)} operations employees have remote days = 5 or 14."
        else:
            viol = ops[~condition]
            expl = f"{len(viol)} operations employees do not have remote days = 5 or 14."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All employees with a performance rating greater than 4.6 have a monthly salary greater than or equal to $6.7k."""
    high_perf = df[df["performance_rating"] > 4.6]
    if high_perf.empty:
        truth = True
        expl = "No employees with performance rating > 4.6."
    else:
        condition = high_perf["monthly_salary_k"] >= 6.7
        truth = condition.all()
        if truth:
            expl = f"All {len(high_perf)} employees with performance rating > 4.6 have salary >= 6.7k."
        else:
            viol = high_perf[~condition]
            expl = f"{len(viol)} employees with performance rating > 4.6 have salary < 6.7k."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most employees in the hr department have a performance rating greater than 4."""
    hr = df[df["department"] == "hr"]
    if hr.empty:
        truth = True
        expl = "No employees in hr department."
    else:
        condition = hr["performance_rating"] > 4
        total = len(hr)
        count = condition.sum()
        truth = count > total / 2
        expl = f"{count}/{total} hr employees have performance rating > 4."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_59.csv")

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
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()