import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the operations department have a monthly salary less than or equal to $8.7k."""
    ops = df[df["department"] == "operations"]
    if ops.empty:
        truth = True
        expl = "No employees in operations department."
    else:
        condition = ops["monthly_salary_k"] <= 8.7
        truth = condition.all()
        if truth:
            expl = f"All {len(ops)} operations employees have salary <= 8.7k."
        else:
            viol = ops[~condition]
            expl = f"{len(viol)} operations employees have salary > 8.7k."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All employees with more than 10 years of experience have a monthly salary greater than or equal to $7.2k."""
    exp = df[df["years_experience"] > 10]
    if exp.empty:
        truth = True
        expl = "No employees with >10 years experience."
    else:
        condition = exp["monthly_salary_k"] >= 7.2
        truth = condition.all()
        if truth:
            expl = f"All {len(exp)} employees with >10 years experience have salary >= 7.2k."
        else:
            viol = exp[~condition]
            expl = f"{len(viol)} employees with >10 years experience have salary < 7.2k."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If an employee is in the engineering department, then their monthly salary is greater than or equal to $5.7k."""
    eng = df[df["department"] == "engineering"]
    if eng.empty:
        truth = True
        expl = "No employees in engineering department."
    else:
        condition = eng["monthly_salary_k"] >= 5.7
        truth = condition.all()
        if truth:
            expl = f"All {len(eng)} engineering employees have salary >= 5.7k."
        else:
            viol = eng[~condition]
            expl = f"{len(viol)} engineering employees have salary < 5.7k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one employee in the marketing department whose performance rating is less than 4.0."""
    mrkt = df[df["department"] == "marketing"]
    if mrkt.empty:
        truth = False
        expl = "No employees in marketing department."
    else:
        condition = mrkt["performance_rating"] < 4.0
        truth = condition.any()
        if truth:
            expl = f"At least one marketing employee has performance rating < 4.0."
        else:
            expl = f"No marketing employees have performance rating < 4.0."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees with a performance rating greater than or equal to 4.7 have more than 3 projects active."""
    perf = df[df["performance_rating"] >= 4.7]
    if perf.empty:
        truth = True
        expl = "No employees with performance rating >= 4.7."
    else:
        condition = perf["projects_active"] > 3
        truth = condition.all()
        if truth:
            expl = f"All {len(perf)} employees with performance rating >= 4.7 have >3 projects."
        else:
            viol = perf[~condition]
            expl = f"{len(viol)} employees with performance rating >= 4.7 have <=3 projects."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If an employee has more than 5 years of experience, then their monthly salary is greater than or equal to $6.2k."""
    exp = df[df["years_experience"] > 5]
    if exp.empty:
        truth = True
        expl = "No employees with >5 years experience."
    else:
        condition = exp["monthly_salary_k"] >= 6.2
        truth = condition.all()
        if truth:
            expl = f"All {len(exp)} employees with >5 years experience have salary >= 6.2k."
        else:
            viol = exp[~condition]
            expl = f"{len(viol)} employees with >5 years experience have salary < 6.2k."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most employees in the hr department have a monthly salary greater than or equal to $8.4k."""
    hr = df[df["department"] == "hr"]
    if hr.empty:
        truth = False
        expl = "No employees in hr department."
    else:
        condition = hr["monthly_salary_k"] >= 8.4
        count_ge = condition.sum()
        total = len(hr)
        truth = count_ge > total / 2
        if truth:
            expl = f"More than half ({count_ge}/{total}) of HR employees have salary >= 8.4k."
        else:
            expl = f"Less than half ({count_ge}/{total}) of HR employees have salary >= 8.4k."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees who work remotely for more than 8 days a month have a monthly salary less than or equal to $9.5k."""
    remote = df[df["remote_days_month"] > 8]
    if remote.empty:
        truth = True
        expl = "No employees work remotely >8 days/month."
    else:
        condition = remote["monthly_salary_k"] <= 9.5
        truth = condition.all()
        if truth:
            expl = f"All {len(remote)} employees working remotely >8 days/month have salary <= 9.5k."
        else:
            viol = remote[~condition]
            expl = f"{len(viol)} employees working remotely >8 days/month have salary > 9.5k."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If an employee is in the finance department, then their years of experience are greater than or equal to 8.2."""
    fin = df[df["department"] == "finance"]
    if fin.empty:
        truth = True
        expl = "No employees in finance department."
    else:
        condition = fin["years_experience"] >= 8.2
        truth = condition.all()
        if truth:
            expl = f"All {len(fin)} finance employees have experience >= 8.2 years."
        else:
            viol = fin[~condition]
            expl = f"{len(viol)} finance employees have experience < 8.2 years."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one employee in the operations department whose monthly salary is greater than $8k."""
    ops = df[df["department"] == "operations"]
    if ops.empty:
        truth = False
        expl = "No employees in operations department."
    else:
        condition = ops["monthly_salary_k"] > 8.0
        truth = condition.any()
        if truth:
            expl = f"At least one operations employee has salary > 8k."
        else:
            expl = f"No operations employees have salary > 8k."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All employees with a performance rating less than 4.2 have more than 4 projects active."""
    perf = df[df["performance_rating"] < 4.2]
    if perf.empty:
        truth = True
        expl = "No employees with performance rating < 4.2."
    else:
        condition = perf["projects_active"] > 4
        truth = condition.all()
        if truth:
            expl = f"All {len(perf)} employees with performance rating < 4.2 have >4 projects."
        else:
            viol = perf[~condition]
            expl = f"{len(viol)} employees with performance rating < 4.2 have <=4 projects."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If an employee has a monthly salary greater than or equal to $9k, then their years of experience are greater than or equal to 4.9."""
    sal = df[df["monthly_salary_k"] >= 9.0]
    if sal.empty:
        truth = True
        expl = "No employees with salary >= 9k."
    else:
        condition = sal["years_experience"] >= 4.9
        truth = condition.all()
        if truth:
            expl = f"All {len(sal)} employees with salary >= 9k have experience >= 4.9 years."
        else:
            viol = sal[~condition]
            expl = f"{len(viol)} employees with salary >= 9k have experience < 4.9 years."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most employees have a monthly salary less than or equal to $8.7k."""
    condition = df["monthly_salary_k"] <= 8.7
    count_le = condition.sum()
    total = len(df)
    truth = count_le > total / 2
    if truth:
        expl = f"More than half ({count_le}/{total}) of employees have salary <= 8.7k."
    else:
        expl = f"Less than half ({count_le}/{total}) of employees have salary <= 8.7k."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All employees with more than 6 projects active have a monthly salary less than or equal to $7.6k."""
    proj = df[df["projects_active"] > 6]
    if proj.empty:
        truth = True
        expl = "No employees with >6 projects."
    else:
        condition = proj["monthly_salary_k"] <= 7.6
        truth = condition.all()
        if truth:
            expl = f"All {len(proj)} employees with >6 projects have salary <= 7.6k."
        else:
            viol = proj[~condition]
            expl = f"{len(viol)} employees with >6 projects have salary > 7.6k."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If an employee is in the marketing department, then their monthly salary is less than or equal to $8.7k."""
    mrkt = df[df["department"] == "marketing"]
    if mrkt.empty:
        truth = True
        expl = "No employees in marketing department."
    else:
        condition = mrkt["monthly_salary_k"] <= 8.7
        truth = condition.all()
        if truth:
            expl = f"All {len(mrkt)} marketing employees have salary <= 8.7k."
        else:
            viol = mrkt[~condition]
            expl = f"{len(viol)} marketing employees have salary > 8.7k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one employee in the engineering department whose years of experience are greater than 10."""
    eng = df[df["department"] == "engineering"]
    if eng.empty:
        truth = False
        expl = "No employees in engineering department."
    else:
        condition = eng["years_experience"] > 10
        truth = condition.any()
        if truth:
            expl = f"At least one engineering employee has experience > 10 years."
        else:
            expl = f"No engineering employees have experience > 10 years."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All employees who work remotely for less than or equal to 8 days a month have a monthly salary greater than or equal to $7.4k."""
    remote = df[df["remote_days_month"] <= 8]
    if remote.empty:
        truth = True
        expl = "No employees work remotely <=8 days/month."
    else:
        condition = remote["monthly_salary_k"] >= 7.4
        truth = condition.all()
        if truth:
            expl = f"All {len(remote)} employees working remotely <=8 days/month have salary >= 7.4k."
        else:
            viol = remote[~condition]
            expl = f"{len(viol)} employees working remotely <=8 days/month have salary < 7.4k."
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
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()