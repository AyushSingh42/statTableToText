import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the HR department have a monthly salary between 5.5k and 8.0k."""
    hr_df = df[df["department"] == "hr"]
    condition = hr_df["monthly_salary_k"].between(5.5, 8.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(hr_df)} HR employees have salaries between 5.5k and 8.0k."
    else:
        viol = hr_df[~condition]
        expl = f"{len(viol)} HR employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If an employee is in the marketing department, then their years of experience are less than 12."""
    marketing_df = df[df["department"] == "marketing"]
    condition = marketing_df["years_experience"] < 12
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing_df)} marketing employees have less than 12 years of experience."
    else:
        viol = marketing_df[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one employee in the operations department with a performance rating greater than 4.0."""
    ops_df = df[df["department"] == "operations"]
    condition = ops_df["performance_rating"] > 4.0
    truth = condition.any()
    if truth:
        expl = f"At least one operation employee has performance rating > 4.0."
    else:
        expl = f"No operation employee has performance rating > 4.0."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 10 years of experience have a monthly salary greater than 6.0k."""
    exp_df = df[df["years_experience"] > 10]
    condition = exp_df["monthly_salary_k"] > 6.0
    truth = condition.all()
    if truth:
        expl = f"All {len(exp_df)} employees with >10 years experience have salary >6.0k."
    else:
        viol = exp_df[~condition]
        expl = f"{len(viol)} employees with >10 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If an employee has a performance rating greater than 4.5, then they have more than 5 projects active."""
    high_perf_df = df[df["performance_rating"] > 4.5]
    condition = high_perf_df["projects_active"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf_df)} employees with performance >4.5 have >5 projects."
    else:
        viol = high_perf_df[~condition]
        expl = f"{len(viol)} employees with performance >4.5 violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most employees in the HR department have a remote workday count between 6 and 10 days per month."""
    hr_df = df[df["department"] == "hr"]
    condition = hr_df["remote_days_month"].between(6, 10, inclusive="both")
    satisfied = condition.sum()
    total = len(hr_df)
    truth = satisfied > total / 2
    if truth:
        expl = f"Most ({satisfied}/{total}) HR employees have remote days between 6-10."
    else:
        expl = f"Only {satisfied}/{total} HR employees have remote days between 6-10."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees in the finance department have a monthly salary greater than 7.0k."""
    finance_df = df[df["department"] == "finance"]
    condition = finance_df["monthly_salary_k"] > 7.0
    truth = condition.all()
    if truth:
        expl = f"All {len(finance_df)} finance employees have salary >7.0k."
    else:
        viol = finance_df[~condition]
        expl = f"{len(viol)} finance employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If an employee is in the engineering department, then their monthly salary is less than 10.6k."""
    eng_df = df[df["department"] == "engineering"]
    condition = eng_df["monthly_salary_k"] < 10.6
    truth = condition.all()
    if truth:
        expl = f"All {len(eng_df)} engineering employees have salary <10.6k."
    else:
        viol = eng_df[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one employee in the marketing department with a monthly salary greater than 10.0k."""
    marketing_df = df[df["department"] == "marketing"]
    condition = marketing_df["monthly_salary_k"] > 10.0
    truth = condition.any()
    if truth:
        expl = f"At least one marketing employee has salary >10.0k."
    else:
        expl = f"No marketing employee has salary >10.0k."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with a performance rating less than 4.0 have more than 5 years of experience."""
    low_perf_df = df[df["performance_rating"] < 4.0]
    condition = low_perf_df["years_experience"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(low_perf_df)} employees with performance <4.0 have >5 years experience."
    else:
        viol = low_perf_df[~condition]
        expl = f"{len(viol)} employees with performance <4.0 violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If an employee has more than 5 projects active, then their performance rating is greater than 3.8."""
    many_proj_df = df[df["projects_active"] > 5]
    condition = many_proj_df["performance_rating"] > 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(many_proj_df)} employees with >5 projects have performance >3.8."
    else:
        viol = many_proj_df[~condition]
        expl = f"{len(viol)} employees with >5 projects violate the rule (performance: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most employees in the operations department have a monthly salary greater than 7.0k."""
    ops_df = df[df["department"] == "operations"]
    condition = ops_df["monthly_salary_k"] > 7.0
    satisfied = condition.sum()
    total = len(ops_df)
    truth = satisfied > total / 2
    if truth:
        expl = f"Most ({satisfied}/{total}) operations employees have salary >7.0k."
    else:
        expl = f"Only {satisfied}/{total} operations employees have salary >7.0k."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All employees with a monthly salary greater than 9.0k have more than 3 projects active."""
    high_sal_df = df[df["monthly_salary_k"] > 9.0]
    condition = high_sal_df["projects_active"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sal_df)} employees with salary >9.0k have >3 projects."
    else:
        viol = high_sal_df[~condition]
        expl = f"{len(viol)} employees with salary >9.0k violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If an employee is in the finance department, then their years of experience are greater than 8."""
    finance_df = df[df["department"] == "finance"]
    condition = finance_df["years_experience"] > 8
    truth = condition.all()
    if truth:
        expl = f"All {len(finance_df)} finance employees have >8 years experience."
    else:
        viol = finance_df[~condition]
        expl = f"{len(viol)} finance employees violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_99.csv")

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
        (14, stmt_14)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()