import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the engineering department with more than 10 years of experience have a monthly salary less than or equal to $6.9k."""
    eng_exp = df[(df["department"] == "engineering") & (df["years_experience"] > 10)]
    if eng_exp.empty:
        truth = True
        expl = "No engineering employees with over 10 years experience."
    else:
        condition = eng_exp["monthly_salary_k"] <= 6.9
        truth = condition.all()
        if truth:
            expl = f"All {len(eng_exp)} engineering employees with >10 years experience have salary <= $6.9k."
        else:
            viol = eng_exp[~condition]
            expl = f"{len(viol)} engineering employees with >10 years experience have salary > $6.9k."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All employees in the finance department have a monthly salary greater than or equal to $7.0k."""
    fin = df[df["department"] == "finance"]
    if fin.empty:
        truth = True
        expl = "No finance employees."
    else:
        condition = fin["monthly_salary_k"] >= 7.0
        truth = condition.all()
        if truth:
            expl = f"All {len(fin)} finance employees have salary >= $7.0k."
        else:
            viol = fin[~condition]
            expl = f"{len(viol)} finance employees have salary < $7.0k."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If an employee is in the operations department, then their years of experience are greater than 8."""
    ops = df[df["department"] == "operations"]
    if ops.empty:
        truth = True
        expl = "No operations employees."
    else:
        condition = ops["years_experience"] > 8
        truth = condition.all()
        if truth:
            expl = f"All {len(ops)} operations employees have >8 years experience."
        else:
            viol = ops[~condition]
            expl = f"{len(viol)} operations employees have <=8 years experience."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with a performance rating greater than 4.5 have a monthly salary less than or equal to $7.8k."""
    perf = df[df["performance_rating"] > 4.5]
    if perf.empty:
        truth = True
        expl = "No employees with performance rating > 4.5."
    else:
        condition = perf["monthly_salary_k"] <= 7.8
        truth = condition.all()
        if truth:
            expl = f"All {len(perf)} employees with performance rating > 4.5 have salary <= $7.8k."
        else:
            viol = perf[~condition]
            expl = f"{len(viol)} employees with performance rating > 4.5 have salary > $7.8k."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. There exists at least one employee in the marketing department with a monthly salary greater than $9.0k."""
    mark = df[df["department"] == "marketing"]
    if mark.empty:
        truth = False
        expl = "No marketing employees."
    else:
        condition = mark["monthly_salary_k"] > 9.0
        truth = condition.any()
        if truth:
            expl = f"At least one marketing employee has salary > $9.0k."
        else:
            expl = f"No marketing employees have salary > $9.0k."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All employees with more than 10 years of experience have a performance rating less than or equal to 4.8."""
    exp = df[df["years_experience"] > 10]
    if exp.empty:
        truth = True
        expl = "No employees with >10 years experience."
    else:
        condition = exp["performance_rating"] <= 4.8
        truth = condition.all()
        if truth:
            expl = f"All {len(exp)} employees with >10 years experience have performance rating <= 4.8."
        else:
            viol = exp[~condition]
            expl = f"{len(viol)} employees with >10 years experience have performance rating > 4.8."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If an employee is in the hr department, then their monthly salary is less than or equal to $5.4k."""
    hr = df[df["department"] == "hr"]
    if hr.empty:
        truth = True
        expl = "No HR employees."
    else:
        condition = hr["monthly_salary_k"] <= 5.4
        truth = condition.all()
        if truth:
            expl = f"All {len(hr)} HR employees have salary <= $5.4k."
        else:
            viol = hr[~condition]
            expl = f"{len(viol)} HR employees have salary > $5.4k."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees with a monthly salary greater than $9.0k have less than or equal to 3 projects active."""
    sal = df[df["monthly_salary_k"] > 9.0]
    if sal.empty:
        truth = True
        expl = "No employees with salary > $9.0k."
    else:
        condition = sal["projects_active"] <= 3
        truth = condition.all()
        if truth:
            expl = f"All {len(sal)} employees with salary > $9.0k have <= 3 projects."
        else:
            viol = sal[~condition]
            expl = f"{len(viol)} employees with salary > $9.0k have > 3 projects."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most employees have a remote days per month greater than or equal to 5."""
    condition = df["remote_days_month"] >= 5
    count_ge5 = condition.sum()
    total = len(df)
    truth = count_ge5 > total / 2
    if truth:
        expl = f"Most ({count_ge5}/{total}) employees have remote days >= 5."
    else:
        expl = f"Only {count_ge5}/{total} employees have remote days >= 5."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with a performance rating greater than 4.0 have a monthly salary greater than or equal to $5.1k."""
    perf = df[df["performance_rating"] > 4.0]
    if perf.empty:
        truth = True
        expl = "No employees with performance rating > 4.0."
    else:
        condition = perf["monthly_salary_k"] >= 5.1
        truth = condition.all()
        if truth:
            expl = f"All {len(perf)} employees with performance rating > 4.0 have salary >= $5.1k."
        else:
            viol = perf[~condition]
            expl = f"{len(viol)} employees with performance rating > 4.0 have salary < $5.1k."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If an employee is in the engineering department, then their years of experience are greater than or equal to 2."""
    eng = df[df["department"] == "engineering"]
    if eng.empty:
        truth = True
        expl = "No engineering employees."
    else:
        condition = eng["years_experience"] >= 2
        truth = condition.all()
        if truth:
            expl = f"All {len(eng)} engineering employees have >= 2 years experience."
        else:
            viol = eng[~condition]
            expl = f"{len(viol)} engineering employees have < 2 years experience."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_69.csv")

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
        (11, stmt_11)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()