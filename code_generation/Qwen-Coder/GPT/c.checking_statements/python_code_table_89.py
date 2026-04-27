import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All finance employees have a performance rating of at least 4.6."""
    finance = df[df["department"] == "finance"]
    condition = finance["performance_rating"] >= 4.6
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have performance rating >= 4.6."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All finance employees work remotely at least 10 days per month."""
    finance = df[df["department"] == "finance"]
    condition = finance["remote_days_month"] >= 10
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees work remotely at least 10 days/month."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All engineering employees receive a monthly salary of at least $6.0k."""
    eng = df[df["department"] == "engineering"]
    condition = eng["monthly_salary_k"] >= 6.0
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees receive at least $6.0k/month."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All HR employees work remotely no more than 12 days per month."""
    hr = df[df["department"] == "hr"]
    condition = hr["remote_days_month"] <= 12
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees work remotely no more than 12 days/month."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Every employee with a performance rating of 4.9 has exactly 4 active projects."""
    perf_49 = df[df["performance_rating"] == 4.9]
    condition = perf_49["projects_active"] == 4
    truth = condition.all()
    if truth:
        expl = f"All {len(perf_49)} employees with performance rating 4.9 have exactly 4 active projects."
    else:
        viol = perf_49[~condition]
        expl = f"{len(viol)} employees with performance rating 4.9 violate the rule (active projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All marketing employees with 13 or more remote work days have a monthly salary of at least $6.6k."""
    marketing = df[df["department"] == "marketing"]
    eligible = marketing[marketing["remote_days_month"] >= 13]
    condition = eligible["monthly_salary_k"] >= 6.6
    truth = condition.all()
    if truth:
        expl = f"All {len(eligible)} marketing employees with 13+ remote days have at least $6.6k/month."
    else:
        viol = eligible[~condition]
        expl = f"{len(viol)} marketing employees with 13+ remote days violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All marketing employees with more than 5 years of experience earn at least $5.1k per month."""
    marketing = df[df["department"] == "marketing"]
    eligible = marketing[marketing["years_experience"] > 5]
    condition = eligible["monthly_salary_k"] >= 5.1
    truth = condition.all()
    if truth:
        expl = f"All {len(eligible)} marketing employees with >5 years experience earn at least $5.1k/month."
    else:
        viol = eligible[~condition]
        expl = f"{len(viol)} marketing employees with >5 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees with more than 8 years of experience earn at least $5.1k per month."""
    eligible = df[df["years_experience"] > 8]
    condition = eligible["monthly_salary_k"] >= 5.1
    truth = condition.all()
    if truth:
        expl = f"All {len(eligible)} employees with >8 years experience earn at least $5.1k/month."
    else:
        viol = eligible[~condition]
        expl = f"{len(viol)} employees with >8 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All employees who work remotely 14 or more days per month have a performance rating of at least 4.2."""
    eligible = df[df["remote_days_month"] >= 14]
    condition = eligible["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(eligible)} employees working remotely 14+ days/month have performance rating >= 4.2."
    else:
        viol = eligible[~condition]
        expl = f"{len(viol)} employees working remotely 14+ days/month violate the rule (performance ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_89.csv")

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
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()