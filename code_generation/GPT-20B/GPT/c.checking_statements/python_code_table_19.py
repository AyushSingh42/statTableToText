import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All finance employees have a monthly salary of at least $5.5k."""
    finance = df[df["department"] == "finance"]
    condition = finance["monthly_salary_k"] >= 5.5
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have salary >= 5.5k."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employee(s) violate the rule (salary: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All operations employees have a performance rating of at least 4.1."""
    ops = df[df["department"] == "operations"]
    condition = ops["performance_rating"] >= 4.1
    truth = condition.all()
    if truth:
        expl = f"All {len(ops)} operations employees have rating >= 4.1."
    else:
        viol = ops[~condition]
        expl = f"{len(viol)} operations employee(s) violate the rule (rating: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All engineering employees have at least 3 active projects."""
    eng = df[df["department"] == "engineering"]
    condition = eng["projects_active"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have >= 3 active projects."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} engineering employee(s) violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 10 years of experience have a monthly salary of at most $9.3k."""
    exp = df[df["years_experience"] > 10]
    condition = exp["monthly_salary_k"] <= 9.3
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >10 years experience have salary <= 9.3k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employee(s) violate the rule (salary: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees who work remotely 13 or more days per month have a performance rating of at least 4.0."""
    remote = df[df["remote_days_month"] >= 13]
    condition = remote["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(remote)} remote employees (>=13 days) have rating >= 4.0."
    else:
        viol = remote[~condition]
        expl = f"{len(viol)} remote employee(s) violate the rule (rating: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All HR employees have a performance rating of at most 4.1."""
    hr = df[df["department"] == "hr"]
    condition = hr["performance_rating"] <= 4.1
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have rating <= 4.1."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employee(s) violate the rule (rating: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees with a monthly salary greater than $10k have at most 6.7 years of experience."""
    high_salary = df[df["monthly_salary_k"] > 10]
    condition = high_salary["years_experience"] <= 6.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_salary)} employees with salary >10k have <= 6.7 years experience."
    else:
        viol = high_salary[~condition]
        expl = f"{len(viol)} employee(s) violate the rule (years experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most employees have a performance rating of at least 4.0."""
    total = len(df)
    count_ge_4 = (df["performance_rating"] >= 4.0).sum()
    truth = count_ge_4 > total / 2
    if truth:
        expl = f"{count_ge_4} out of {total} employees (>{total/2}) have rating >= 4.0."
    else:
        expl = f"Only {count_ge_4} out of {total} employees have rating >= 4.0, which is not a majority."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_19.csv")

    # Convert numeric columns
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()