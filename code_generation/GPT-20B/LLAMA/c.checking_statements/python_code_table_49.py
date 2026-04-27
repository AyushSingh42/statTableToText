import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the operations department have a monthly salary less than or equal to $7.6k."""
    ops = df[df["department"] == "operations"]
    if ops.empty:
        return True, "No operations employees to evaluate."
    condition = ops["monthly_salary_k"] <= 7.6
    truth = condition.all()
    if truth:
        expl = f"All {len(ops)} operations employees have salary <= 7.6k."
    else:
        viol = ops[~condition]
        expl = f"{len(viol)} operations employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If an employee is in the engineering department, then their years of experience are less than or equal to 10 years."""
    eng = df[df["department"] == "engineering"]
    if eng.empty:
        return True, "No engineering employees to evaluate."
    condition = eng["years_experience"] <= 10
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have <= 10 years experience."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one employee in the hr department whose performance rating is less than 4.0."""
    hr = df[df["department"] == "hr"]
    condition = hr["performance_rating"] < 4.0
    truth = condition.any()
    if truth:
        viol = hr[condition]
        expl = f"Found {len(viol)} HR employee(s) with performance rating < 4.0 (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    else:
        expl = "No HR employee has a performance rating < 4.0."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 5 years of experience have a monthly salary greater than or equal to $6.2k."""
    exp = df[df["years_experience"] > 5]
    if exp.empty:
        return True, "No employees with >5 years experience to evaluate."
    condition = exp["monthly_salary_k"] >= 6.2
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >5 years experience have salary >= 6.2k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If an employee has more than 3 projects active, then their monthly salary is greater than or equal to $6.4k."""
    proj = df[df["projects_active"] > 3]
    if proj.empty:
        return True, "No employees with >3 projects active to evaluate."
    condition = proj["monthly_salary_k"] >= 6.4
    truth = condition.all()
    if truth:
        expl = f"All {len(proj)} employees with >3 projects active have salary >= 6.4k."
    else:
        viol = proj[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most employees in the hr department have a monthly salary less than or equal to $8.6k."""
    hr = df[df["department"] == "hr"]
    if hr.empty:
        return True, "No HR employees to evaluate."
    condition = hr["monthly_salary_k"] <= 8.6
    count = len(hr)
    satisfied = condition.sum()
    proportion = satisfied / count
    truth = proportion > 0.5
    if truth:
        expl = f"{satisfied}/{count} HR employees ({proportion*100:.1f}%) have salary <= 8.6k."
    else:
        expl = f"Only {satisfied}/{count} HR employees ({proportion*100:.1f}%) have salary <= 8.6k."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees with a performance rating greater than 4.5 have more than 2 projects active."""
    perf = df[df["performance_rating"] > 4.5]
    if perf.empty:
        return True, "No employees with performance rating > 4.5 to evaluate."
    condition = perf["projects_active"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(perf)} employees with rating > 4.5 have >2 projects active."
    else:
        viol = perf[~condition]
        expl = f"{len(viol)} employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If an employee is in the finance department, then their years of experience are greater than or equal to 5 years."""
    fin = df[df["department"] == "finance"]
    if fin.empty:
        return True, "No finance employees to evaluate."
    condition = fin["years_experience"] >= 5
    truth = condition.all()
    if truth:
        expl = f"All {len(fin)} finance employees have >= 5 years experience."
    else:
        viol = fin[~condition]
        expl = f"{len(viol)} finance employees violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one employee in the operations department whose remote days per month are less than or equal to 5."""
    ops = df[df["department"] == "operations"]
    condition = ops["remote_days_month"] <= 5
    truth = condition.any()
    if truth:
        viol = ops[condition]
        expl = f"Found {len(viol)} operations employee(s) with remote days <= 5 (days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    else:
        expl = "No operations employee has remote days <= 5."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with a monthly salary greater than $10k have more than 4 projects active."""
    high = df[df["monthly_salary_k"] > 10]
    if high.empty:
        return True, "No employees with salary > 10k to evaluate."
    condition = high["projects_active"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(high)} employees with salary > 10k have >4 projects active."
    else:
        viol = high[~condition]
        expl = f"{len(viol)} employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If an employee has more than 8 years of experience, then their monthly salary is greater than or equal to $7.5k."""
    exp = df[df["years_experience"] > 8]
    if exp.empty:
        return True, "No employees with >8 years experience to evaluate."
    condition = exp["monthly_salary_k"] >= 7.5
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >8 years experience have salary >= 7.5k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most employees in the engineering department have a monthly salary greater than or equal to $6.2k."""
    eng = df[df["department"] == "engineering"]
    if eng.empty:
        return True, "No engineering employees to evaluate."
    condition = eng["monthly_salary_k"] >= 6.2
    count = len(eng)
    satisfied = condition.sum()
    proportion = satisfied / count
    truth = proportion > 0.5
    if truth:
        expl = f"{satisfied}/{count} engineering employees ({proportion*100:.1f}%) have salary >= 6.2k."
    else:
        expl = f"Only {satisfied}/{count} engineering employees ({proportion*100:.1f}%) have salary >= 6.2k."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All employees with a performance rating less than 4.0 have less than or equal to 3 projects active."""
    perf = df[df["performance_rating"] < 4.0]
    if perf.empty:
        return True, "No employees with performance rating < 4.0 to evaluate."
    condition = perf["projects_active"] <= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(perf)} employees with rating < 4.0 have <= 3 projects active."
    else:
        viol = perf[~condition]
        expl = f"{len(viol)} employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_49.csv")

    # Convert numeric columns safely
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()