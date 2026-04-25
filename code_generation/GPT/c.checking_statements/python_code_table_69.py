import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all engineering employees with more than 11 years of experience, monthly salary is at most $6.0k."""
    eng_expert = df[(df["department"] == "engineering") & (df["years_experience"] > 11)]
    if len(eng_expert) == 0:
        truth = True
        expl = "No engineering employees with more than 11 years of experience."
    else:
        condition = eng_expert["monthly_salary_k"] <= 6.0
        truth = condition.all()
        if truth:
            expl = f"All {len(eng_expert)} engineering employees with >11 years experience have salary <= $6.0k."
        else:
            viol = eng_expert[~condition]
            expl = f"{len(viol)} engineering employees with >11 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All finance employees have a performance rating of at least 4.0."""
    finance = df[df["department"] == "finance"]
    if len(finance) == 0:
        truth = True
        expl = "No finance employees."
    else:
        condition = finance["performance_rating"] >= 4.0
        truth = condition.all()
        if truth:
            expl = f"All {len(finance)} finance employees have performance rating >= 4.0."
        else:
            viol = finance[~condition]
            expl = f"{len(viol)} finance employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All operations employees work remotely exactly 5 days per month."""
    ops = df[df["department"] == "operations"]
    if len(ops) == 0:
        truth = True
        expl = "No operations employees."
    else:
        condition = ops["remote_days_month"] == 5
        truth = condition.all()
        if truth:
            expl = f"All {len(ops)} operations employees work remotely exactly 5 days/month."
        else:
            viol = ops[~condition]
            expl = f"{len(viol)} operations employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Every employee with a performance rating of 4.8 or higher earns a monthly salary of at least $5.3k."""
    high_perf = df[df["performance_rating"] >= 4.8]
    if len(high_perf) == 0:
        truth = True
        expl = "No employees with performance rating >= 4.8."
    else:
        condition = high_perf["monthly_salary_k"] >= 5.3
        truth = condition.all()
        if truth:
            expl = f"All {len(high_perf)} employees with performance rating >= 4.8 earn >= $5.3k/month."
        else:
            viol = high_perf[~condition]
            expl = f"{len(viol)} employees with performance rating >= 4.8 violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All marketing employees have a performance rating of no more than 4.1."""
    marketing = df[df["department"] == "marketing"]
    if len(marketing) == 0:
        truth = True
        expl = "No marketing employees."
    else:
        condition = marketing["performance_rating"] <= 4.1
        truth = condition.all()
        if truth:
            expl = f"All {len(marketing)} marketing employees have performance rating <= 4.1."
        else:
            viol = marketing[~condition]
            expl = f"{len(viol)} marketing employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All HR employees receive a monthly salary of no more than $5.4k."""
    hr = df[df["department"] == "hr"]
    if len(hr) == 0:
        truth = True
        expl = "No HR employees."
    else:
        condition = hr["monthly_salary_k"] <= 5.4
        truth = condition.all()
        if truth:
            expl = f"All {len(hr)} HR employees receive <= $5.4k/month."
        else:
            viol = hr[~condition]
            expl = f"{len(viol)} HR employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees with less than 3 years of experience earn a monthly salary of at least $8.3k."""
    low_exp = df[df["years_experience"] < 3]
    if len(low_exp) == 0:
        truth = True
        expl = "No employees with less than 3 years of experience."
    else:
        condition = low_exp["monthly_salary_k"] >= 8.3
        truth = condition.all()
        if truth:
            expl = f"All {len(low_exp)} employees with <3 years experience earn >= $8.3k/month."
        else:
            viol = low_exp[~condition]
            expl = f"{len(viol)} employees with <3 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees with more than 10 years of experience have a performance rating of at most 4.5."""
    high_exp = df[df["years_experience"] > 10]
    if len(high_exp) == 0:
        truth = True
        expl = "No employees with more than 10 years of experience."
    else:
        condition = high_exp["performance_rating"] <= 4.5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_exp)} employees with >10 years experience have performance rating <= 4.5."
        else:
            viol = high_exp[~condition]
            expl = f"{len(viol)} employees with >10 years experience violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All engineering employees are assigned to no more than 4 active projects."""
    eng = df[df["department"] == "engineering"]
    if len(eng) == 0:
        truth = True
        expl = "No engineering employees."
    else:
        condition = eng["projects_active"] <= 4
        truth = condition.all()
        if truth:
            expl = f"All {len(eng)} engineering employees are assigned to <= 4 active projects."
        else:
            viol = eng[~condition]
            expl = f"{len(viol)} engineering employees violate the rule (active projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with exactly 2 active projects earn a monthly salary of at least $7.3k."""
    two_proj = df[df["projects_active"] == 2]
    if len(two_proj) == 0:
        truth = True
        expl = "No employees with exactly 2 active projects."
    else:
        condition = two_proj["monthly_salary_k"] >= 7.3
        truth = condition.all()
        if truth:
            expl = f"All {len(two_proj)} employees with exactly 2 active projects earn >= $7.3k/month."
        else:
            viol = two_proj[~condition]
            expl = f"{len(viol)} employees with exactly 2 active projects violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
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
        (10, stmt_10)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()