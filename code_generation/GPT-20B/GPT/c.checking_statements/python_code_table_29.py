import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All finance employees have a monthly salary between $8.6k and $9.4k."""
    finance = df[df["department"].str.lower() == "finance"]
    condition = finance["monthly_salary_k"].between(8.6, 9.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have salaries between 8.6k and 9.4k."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All engineering employees have a performance rating of at least 4.2."""
    eng = df[df["department"].str.lower() == "engineering"]
    condition = eng["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have performance rating >= 4.2."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All marketing employees are involved in at least 2 active projects."""
    marketing = df[df["department"].str.lower() == "marketing"]
    condition = marketing["projects_active"] >= 2
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees have at least 2 active projects."
    else:
        viol = marketing[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All HR employees work remotely between 5 and 10 days per month."""
    hr = df[df["department"].str.lower() == "hr"]
    condition = hr["remote_days_month"].between(5, 10, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees work remotely between 5 and 10 days per month."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees with five or more active projects have a performance rating of at least 4.1."""
    many_proj = df[df["projects_active"] >= 5]
    condition = many_proj["performance_rating"] >= 4.1
    truth = condition.all()
    if truth:
        expl = f"All {len(many_proj)} employees with >=5 projects have performance rating >= 4.1."
    else:
        viol = many_proj[~condition]
        expl = f"{len(viol)} employees with >=5 projects violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All employees with two or fewer years of experience have a performance rating of at least 4.2."""
    low_exp = df[df["years_experience"] <= 2]
    condition = low_exp["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(low_exp)} employees with <=2 years experience have performance rating >= 4.2."
    else:
        viol = low_exp[~condition]
        expl = f"{len(viol)} employees with <=2 years experience violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All finance employees have a performance rating of at least 3.8."""
    finance = df[df["department"].str.lower() == "finance"]
    condition = finance["performance_rating"] >= 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have performance rating >= 3.8."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees who work remotely 13 or more days per month have a monthly salary of at most $8.9k."""
    remote_many = df[df["remote_days_month"] >= 13]
    condition = remote_many["monthly_salary_k"] <= 8.9
    truth = condition.all()
    if truth:
        expl = f"All {len(remote_many)} employees working remotely >=13 days have salary <= 8.9k."
    else:
        viol = remote_many[~condition]
        expl = f"{len(viol)} employees working remotely >=13 days violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most employees have a performance rating of at least 4.0."""
    total = len(df)
    count = (df["performance_rating"] >= 4.0).sum()
    proportion = count / total if total > 0 else 0
    truth = proportion > 0.5
    if truth:
        expl = f"{count}/{total} employees ({proportion:.2%}) have performance rating >= 4.0."
    else:
        expl = f"Only {count}/{total} employees ({proportion:.2%}) have performance rating >= 4.0."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_29.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()