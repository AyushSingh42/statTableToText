import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All HR employees have a monthly salary of at most $7.7k."""
    hr = df[df["department"] == "hr"]
    condition = hr["monthly_salary_k"] <= 7.7
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have salary <= 7.7k."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All HR employees have a performance rating of at least 3.9."""
    hr = df[df["department"] == "hr"]
    condition = hr["performance_rating"] >= 3.9
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have rating >= 3.9."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All finance employees have a performance rating of exactly 4.3."""
    fin = df[df["department"] == "finance"]
    condition = fin["performance_rating"] == 4.3
    truth = condition.all()
    if truth:
        expl = f"All {len(fin)} finance employees have rating exactly 4.3."
    else:
        viol = fin[~condition]
        expl = f"{len(viol)} finance employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All engineering employees work remotely at least 13 days per month."""
    eng = df[df["department"] == "engineering"]
    condition = eng["remote_days_month"] >= 13
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have remote_days_month >= 13."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All operations employees with more than 7 years of experience have a monthly salary of at most $8.5k."""
    ops = df[(df["department"] == "operations") & (df["years_experience"] > 7)]
    condition = ops["monthly_salary_k"] <= 8.5
    truth = condition.all()
    if truth:
        expl = f"All {len(ops)} operations employees with >7 years have salary <= 8.5k."
    else:
        viol = ops[~condition]
        expl = f"{len(viol)} operations employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All employees with a performance rating of at least 4.5 have more than 5 years of experience."""
    high_perf = df[df["performance_rating"] >= 4.5]
    condition = high_perf["years_experience"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf)} employees with rating >= 4.5 have >5 years experience."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees violate the rule (years: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees earning more than $9k per month have a performance rating of no higher than 4.4."""
    high_salary = df[df["monthly_salary_k"] > 9]
    condition = high_salary["performance_rating"] <= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_salary)} employees with salary >9k have rating <= 4.4."
    else:
        viol = high_salary[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees with at least 10 years of experience are active on at most five projects."""
    exp10 = df[df["years_experience"] >= 10]
    condition = exp10["projects_active"] <= 5
    truth = condition.all()
    if truth:
        expl = f"All {len(exp10)} employees with >=10 years have <=5 projects."
    else:
        viol = exp10[~condition]
        expl = f"{len(viol)} employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All employees with a performance rating of at least 4.5 have more than 5 years of experience."""
    # Same as statement 6
    high_perf = df[df["performance_rating"] >= 4.5]
    condition = high_perf["years_experience"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf)} employees with rating >= 4.5 have >5 years experience."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees violate the rule (years: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_59.csv")

    # Convert numeric columns explicitly
    numeric_cols = ["years_experience", "monthly_salary_k", "projects_active", "performance_rating", "remote_days_month"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()