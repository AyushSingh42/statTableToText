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
        return True, "No employees in the operations department."
    condition = ops["monthly_salary_k"] <= 8.7
    truth = condition.all()
    if truth:
        return True, f"All {len(ops)} operations employees have salary <= 8.7k."
    viol = ops[~condition]
    return False, f"{len(viol)} operations employee(s) violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. All employees with more than 10 years of experience have a monthly salary greater than or equal to $7.2k."""
    exp = df[df["years_experience"] > 10]
    if exp.empty:
        return True, "No employees with more than 10 years of experience."
    condition = exp["monthly_salary_k"] >= 7.2
    truth = condition.all()
    if truth:
        return True, f"All {len(exp)} employees with >10 years experience have salary >= 7.2k."
    viol = exp[~condition]
    return False, f"{len(viol)} employee(s) violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. If an employee is in the engineering department, then their monthly salary is greater than or equal to $5.7k."""
    eng = df[df["department"] == "engineering"]
    if eng.empty:
        return True, "No employees in the engineering department."
    condition = eng["monthly_salary_k"] >= 5.7
    truth = condition.all()
    if truth:
        return True, f"All {len(eng)} engineering employees have salary >= 5.7k."
    viol = eng[~condition]
    return False, f"{len(viol)} engineering employee(s) violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one employee in the marketing department whose performance rating is less than 4.0."""
    marketing = df[(df["department"] == "marketing") & (df["performance_rating"] < 4.0)]
    truth = not marketing.empty
    if truth:
        return True, f"Found {len(marketing)} marketing employee(s) with performance rating < 4.0."
    return False, "No marketing employee has performance rating < 4.0."

def stmt_5(df: pd.DataFrame):
    """5. All employees with a performance rating greater than or equal to 4.7 have more than 3 projects active."""
    perf = df[df["performance_rating"] >= 4.7]
    if perf.empty:
        return True, "No employees with performance rating >= 4.7."
    condition = perf["projects_active"] > 3
    truth = condition.all()
    if truth:
        return True, f"All {len(perf)} employees with rating >= 4.7 have >3 projects."
    viol = perf[~condition]
    return False, f"{len(viol)} employee(s) violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."

def stmt_6(df: pd.DataFrame):
    """6. If an employee has more than 5 years of experience, then their monthly salary is greater than or equal to $6.2k."""
    exp = df[df["years_experience"] > 5]
    if exp.empty:
        return True, "No employees with >5 years experience."
    condition = exp["monthly_salary_k"] >= 6.2
    truth = condition.all()
    if truth:
        return True, f"All {len(exp)} employees with >5 years experience have salary >= 6.2k."
    viol = exp[~condition]
    return False, f"{len(viol)} employee(s) violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."

def stmt_7(df: pd.DataFrame):
    """7. Most employees in the hr department have a monthly salary greater than or equal to $8.4k."""
    hr = df[df["department"] == "hr"]
    if hr.empty:
        return False, "No employees in the hr department."
    count = len(hr)
    satisfied = hr[hr["monthly_salary_k"] >= 8.4]
    proportion = len(satisfied) / count
    truth = proportion > 0.5
    if truth:
        return True, f"{len(satisfied)}/{count} ({proportion:.2%}) hr employees have salary >= 8.4k."
    return False, f"{len(satisfied)}/{count} ({proportion:.2%}) hr employees have salary >= 8.4k."

def stmt_8(df: pd.DataFrame):
    """8. All employees who work remotely for more than 8 days a month have a monthly salary less than or equal to $9.5k."""
    remote = df[df["remote_days_month"] > 8]
    if remote.empty:
        return True, "No employees work remotely >8 days/month."
    condition = remote["monthly_salary_k"] <= 9.5
    truth = condition.all()
    if truth:
        return True, f"All {len(remote)} remote employees (>8 days) have salary <= 9.5k."
    viol = remote[~condition]
    return False, f"{len(viol)} employee(s) violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."

def stmt_9(df: pd.DataFrame):
    """9. If an employee is in the finance department, then their years of experience are greater than or equal to 8.2."""
    fin = df[df["department"] == "finance"]
    if fin.empty:
        return True, "No employees in the finance department."
    condition = fin["years_experience"] >= 8.2
    truth = condition.all()
    if truth:
        return True, f"All {len(fin)} finance employees have years_experience >= 8.2."
    viol = fin[~condition]
    return False, f"{len(viol)} finance employee(s) violate the rule (years: {', '.join(map(str, viol['years_experience'].tolist()))})."

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one employee in the operations department whose monthly salary is greater than $8k."""
    ops = df[(df["department"] == "operations") & (df["monthly_salary_k"] > 8)]
    truth = not ops.empty
    if truth:
        return True, f"Found {len(ops)} operations employee(s) with salary > 8k."
    return False, "No operations employee has salary > 8k."

def stmt_11(df: pd.DataFrame):
    """11. All employees with a performance rating less than 4.2 have more than 4 projects active."""
    perf = df[df["performance_rating"] < 4.2]
    if perf.empty:
        return True, "No employees with performance rating < 4.2."
    condition = perf["projects_active"] > 4
    truth = condition.all()
    if truth:
        return True, f"All {len(perf)} employees with rating < 4.2 have >4 projects."
    viol = perf[~condition]
    return False, f"{len(viol)} employee(s) violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."

def stmt_12(df: pd.DataFrame):
    """12. If an employee has a monthly salary greater than or equal to $9k, then their years of experience are greater than or equal to 4.9."""
    high_salary = df[df["monthly_salary_k"] >= 9]
    if high_salary.empty:
        return True, "No employees with salary >= 9k."
    condition = high_salary["years_experience"] >= 4.9
    truth = condition.all()
    if truth:
        return True, f"All {len(high_salary)} employees with salary >= 9k have years_experience >= 4.9."
    viol = high_salary[~condition]
    return False, f"{len(viol)} employee(s) violate the rule (years: {', '.join(map(str, viol['years_experience'].tolist()))})."

def stmt_13(df: pd.DataFrame):
    """13. Most employees have a monthly salary less than or equal to $8.7k."""
    total = len(df)
    satisfied = df[df["monthly_salary_k"] <= 8.7]
    proportion = len(satisfied) / total
    truth = proportion > 0.5
    if truth:
        return True, f"{len(satisfied)}/{total} ({proportion:.2%}) employees have salary <= 8.7k."
    return False, f"{len(satisfied)}/{total} ({proportion:.2%}) employees have salary <= 8.7k."

def stmt_14(df: pd.DataFrame):
    """14. All employees with more than 6 projects active have a monthly salary less than or equal to $7.6k."""
    proj = df[df["projects_active"] > 6]
    if proj.empty:
        return True, "No employees with >6 projects active."
    condition = proj["monthly_salary_k"] <= 7.6
    truth = condition.all()
    if truth:
        return True, f"All {len(proj)} employees with >6 projects have salary <= 7.6k."
    viol = proj[~condition]
    return False, f"{len(viol)} employee(s) violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."

def stmt_15(df: pd.DataFrame):
    """15. If an employee is in the marketing department, then their monthly salary is less than or equal to $8.7k."""
    marketing = df[df["department"] == "marketing"]
    if marketing.empty:
        return True, "No employees in the marketing department."
    condition = marketing["monthly_salary_k"] <= 8.7
    truth = condition.all()
    if truth:
        return True, f"All {len(marketing)} marketing employees have salary <= 8.7k."
    viol = marketing[~condition]
    return False, f"{len(viol)} marketing employee(s) violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one employee in the engineering department whose years of experience are greater than 10."""
    eng = df[(df["department"] == "engineering") & (df["years_experience"] > 10)]
    truth = not eng.empty
    if truth:
        return True, f"Found {len(eng)} engineering employee(s) with years_experience > 10."
    return False, "No engineering employee has years_experience > 10."

def stmt_17(df: pd.DataFrame):
    """17. All employees who work remotely for less than or equal to 8 days a month have a monthly salary greater than or equal to $7.4k."""
    remote = df[df["remote_days_month"] <= 8]
    if remote.empty:
        return True, "No employees work remotely <=8 days/month."
    condition = remote["monthly_salary_k"] >= 7.4
    truth = condition.all()
    if truth:
        return True, f"All {len(remote)} remote employees (<=8 days) have salary >= 7.4k."
    viol = remote[~condition]
    return False, f"{len(viol)} employee(s) violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_9.csv")

    # Convert numeric columns safely
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
        (17, stmt_17),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()