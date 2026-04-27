import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All HR employees work remotely at least 4 days per month."""
    hr = df[df["department"] == "hr"]
    condition = hr["remote_days_month"] >= 4
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have remote days >= 4."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All employees with a performance rating of 4.5 or higher earn a monthly salary of at least $6.2k."""
    high_perf = df[df["performance_rating"] >= 4.5]
    condition = high_perf["monthly_salary_k"] >= 6.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf)} employees with rating >= 4.5 have salary >= 6.2k."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every employee with more than 9 years of experience has a performance rating of at least 4.0."""
    exp_gt9 = df[df["years_experience"] > 9]
    condition = exp_gt9["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(exp_gt9)} employees with >9 years experience have rating >= 4.0."
    else:
        viol = exp_gt9[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees handling six active projects have a performance rating of at least 3.9."""
    six_proj = df[df["projects_active"] == 6]
    condition = six_proj["performance_rating"] >= 3.9
    truth = condition.all()
    if truth:
        expl = f"All {len(six_proj)} employees with 6 projects have rating >= 3.9."
    else:
        viol = six_proj[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All finance department employees earn no more than $8.5k per month."""
    finance = df[df["department"] == "finance"]
    condition = finance["monthly_salary_k"] <= 8.5
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have salary <= 8.5k."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All employees earning more than $10k per month have 8.5 years of experience or less."""
    high_salary = df[df["monthly_salary_k"] > 10]
    condition = high_salary["years_experience"] <= 8.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_salary)} employees with salary > 10k have experience <= 8.5 years."
    else:
        viol = high_salary[~condition]
        expl = f"{len(viol)} employees violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every employee with a performance rating of 4.6 or higher receives a monthly salary of at least $6.4k."""
    high_perf = df[df["performance_rating"] >= 4.6]
    condition = high_perf["monthly_salary_k"] >= 6.4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf)} employees with rating >= 4.6 have salary >= 6.4k."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If an operations employee has at least 8 years of experience, their performance rating is at least 4.6."""
    ops_exp = df[(df["department"] == "operations") & (df["years_experience"] >= 8)]
    condition = ops_exp["performance_rating"] >= 4.6
    truth = condition.all()
    if truth:
        expl = f"All {len(ops_exp)} operations employees with >=8 years experience have rating >= 4.6."
    else:
        viol = ops_exp[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most employees have a performance rating of at least 4.0."""
    total = len(df)
    count = (df["performance_rating"] >= 4.0).sum()
    truth = count > total / 2
    percent = count / total * 100
    if truth:
        expl = f"{count} out of {total} employees ({percent:.1f}%) have rating >= 4.0, which is > 50%."
    else:
        expl = f"{count} out of {total} employees ({percent:.1f}%) have rating >= 4.0, which is not > 50%."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_49.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()