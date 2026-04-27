import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the finance department have a monthly salary less than or equal to $10.2k."""
    finance = df[df["department"] == "finance"]
    if finance.empty:
        truth = True
        expl = "No employees in finance department."
    else:
        condition = finance["monthly_salary_k"] <= 10.2
        truth = condition.all()
        if truth:
            expl = f"All {len(finance)} finance employees have salary <= $10.2k."
        else:
            viol = finance[~condition]
            expl = f"{len(viol)} finance employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All employees with more than 10 years of experience have a performance rating greater than or equal to 4.0."""
    exp = df[df["years_experience"] > 10]
    if exp.empty:
        truth = True
        expl = "No employees with >10 years experience."
    else:
        condition = exp["performance_rating"] >= 4.0
        truth = condition.all()
        if truth:
            expl = f"All {len(exp)} employees with >10 years experience have rating >= 4.0."
        else:
            viol = exp[~condition]
            expl = f"{len(viol)} employees with >10 years experience violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If an employee is in the marketing department, then their monthly salary is greater than or equal to $9.0k."""
    marketing = df[df["department"] == "marketing"]
    if marketing.empty:
        truth = True
        expl = "No employees in marketing department."
    else:
        condition = marketing["monthly_salary_k"] >= 9.0
        truth = condition.all()
        if truth:
            expl = f"All {len(marketing)} marketing employees have salary >= $9.0k."
        else:
            viol = marketing[~condition]
            expl = f"{len(viol)} marketing employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one employee in the engineering department whose monthly salary is greater than $9.0k."""
    eng = df[df["department"] == "engineering"]
    if eng.empty:
        truth = False
        expl = "No employees in engineering department."
    else:
        condition = eng["monthly_salary_k"] > 9.0
        truth = condition.any()
        if truth:
            expl = f"At least one engineering employee has salary > $9.0k."
        else:
            expl = f"No engineering employees have salary > $9.0k."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees with a performance rating greater than 4.5 have more than 5 years of experience."""
    high_perf = df[df["performance_rating"] > 4.5]
    if high_perf.empty:
        truth = True
        expl = "No employees with performance rating > 4.5."
    else:
        condition = high_perf["years_experience"] > 5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_perf)} employees with rating > 4.5 have >5 years experience."
        else:
            viol = high_perf[~condition]
            expl = f"{len(viol)} employees with rating > 4.5 violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If an employee has more than 5 projects active, then their performance rating is less than or equal to 4.7."""
    many_proj = df[df["projects_active"] > 5]
    if many_proj.empty:
        truth = True
        expl = "No employees with >5 projects active."
    else:
        condition = many_proj["performance_rating"] <= 4.7
        truth = condition.all()
        if truth:
            expl = f"All {len(many_proj)} employees with >5 projects have rating <= 4.7."
        else:
            viol = many_proj[~condition]
            expl = f"{len(viol)} employees with >5 projects violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most employees in the finance department have a monthly salary less than $8.0k."""
    finance = df[df["department"] == "finance"]
    if finance.empty:
        truth = True
        expl = "No employees in finance department."
    else:
        condition = finance["monthly_salary_k"] < 8.0
        count = condition.sum()
        total = len(finance)
        truth = count > total / 2
        if truth:
            expl = f"More than half ({count}/{total}) of finance employees have salary < $8.0k."
        else:
            expl = f"Less than half ({count}/{total}) of finance employees have salary < $8.0k."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees with a monthly salary greater than $9.5k have more than 4 years of experience."""
    high_sal = df[df["monthly_salary_k"] > 9.5]
    if high_sal.empty:
        truth = True
        expl = "No employees with salary > $9.5k."
    else:
        condition = high_sal["years_experience"] > 4
        truth = condition.all()
        if truth:
            expl = f"All {len(high_sal)} employees with salary > $9.5k have >4 years experience."
        else:
            viol = high_sal[~condition]
            expl = f"{len(viol)} employees with salary > $9.5k violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If an employee is in the operations department, then their monthly salary is less than or equal to $10.5k."""
    ops = df[df["department"] == "operations"]
    if ops.empty:
        truth = True
        expl = "No employees in operations department."
    else:
        condition = ops["monthly_salary_k"] <= 10.5
        truth = condition.all()
        if truth:
            expl = f"All {len(ops)} operations employees have salary <= $10.5k."
        else:
            viol = ops[~condition]
            expl = f"{len(viol)} operations employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one employee in the hr department whose monthly salary is greater than $9.0k."""
    hr = df[df["department"] == "hr"]
    if hr.empty:
        truth = False
        expl = "No employees in HR department."
    else:
        condition = hr["monthly_salary_k"] > 9.0
        truth = condition.any()
        if truth:
            expl = f"At least one HR employee has salary > $9.0k."
        else:
            expl = f"No HR employees have salary > $9.0k."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All employees with more than 10 years of experience have a monthly salary greater than or equal to $5.5k."""
    exp = df[df["years_experience"] > 10]
    if exp.empty:
        truth = True
        expl = "No employees with >10 years experience."
    else:
        condition = exp["monthly_salary_k"] >= 5.5
        truth = condition.all()
        if truth:
            expl = f"All {len(exp)} employees with >10 years experience have salary >= $5.5k."
        else:
            viol = exp[~condition]
            expl = f"{len(viol)} employees with >10 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If an employee has a performance rating greater than 4.0, then their monthly salary is greater than or equal to $5.5k."""
    high_perf = df[df["performance_rating"] > 4.0]
    if high_perf.empty:
        truth = True
        expl = "No employees with performance rating > 4.0."
    else:
        condition = high_perf["monthly_salary_k"] >= 5.5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_perf)} employees with rating > 4.0 have salary >= $5.5k."
        else:
            viol = high_perf[~condition]
            expl = f"{len(viol)} employees with rating > 4.0 violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most employees have a monthly salary greater than $5.0k."""
    condition = df["monthly_salary_k"] > 5.0
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of employees have salary > $5.0k."
    else:
        expl = f"Less than half ({count}/{total}) of employees have salary > $5.0k."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All employees with a monthly salary less than $6.0k have a performance rating less than or equal to 4.7."""
    low_sal = df[df["monthly_salary_k"] < 6.0]
    if low_sal.empty:
        truth = True
        expl = "No employees with salary < $6.0k."
    else:
        condition = low_sal["performance_rating"] <= 4.7
        truth = condition.all()
        if truth:
            expl = f"All {len(low_sal)} employees with salary < $6.0k have rating <= 4.7."
        else:
            viol = low_sal[~condition]
            expl = f"{len(viol)} employees with salary < $6.0k violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If an employee is in the engineering department, then their monthly salary is greater than or equal to $8.0k."""
    eng = df[df["department"] == "engineering"]
    if eng.empty:
        truth = True
        expl = "No employees in engineering department."
    else:
        condition = eng["monthly_salary_k"] >= 8.0
        truth = condition.all()
        if truth:
            expl = f"All {len(eng)} engineering employees have salary >= $8.0k."
        else:
            viol = eng[~condition]
            expl = f"{len(viol)} engineering employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one employee in the marketing department whose monthly salary is greater than $10.0k."""
    marketing = df[df["department"] == "marketing"]
    if marketing.empty:
        truth = False
        expl = "No employees in marketing department."
    else:
        condition = marketing["monthly_salary_k"] > 10.0
        truth = condition.any()
        if truth:
            expl = f"At least one marketing employee has salary > $10.0k."
        else:
            expl = f"No marketing employees have salary > $10.0k."
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
        (8, stmt_8),
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()