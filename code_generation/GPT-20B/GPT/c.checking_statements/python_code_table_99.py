import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All HR employees have a performance rating of at least 3.8."""
    hr = df[df["department"] == "hr"]
    condition = hr["performance_rating"] >= 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have rating >= 3.8."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All employees earning at least $10 k per month have less than 9 years of experience."""
    high_salary = df[df["monthly_salary_k"] >= 10]
    condition = high_salary["years_experience"] < 9
    truth = condition.all()
    if truth:
        expl = f"All {len(high_salary)} employees earning >= $10k/month have < 9 years experience."
    else:
        viol = high_salary[~condition]
        expl = f"{len(viol)} employees violate the rule (years: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All employees with a performance rating of 4.8 or higher work remotely at least 6 days per month."""
    high_perf = df[df["performance_rating"] >= 4.8]
    condition = high_perf["remote_days_month"] >= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf)} employees with rating >= 4.8 work remotely >= 6 days/month."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Every finance employee works remotely either 4 or 12 days per month."""
    finance = df[df["department"] == "finance"]
    condition = finance["remote_days_month"].isin([4, 12])
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees work remotely 4 or 12 days/month."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees handling six active projects have a performance rating of at least 4.0."""
    six_proj = df[df["projects_active"] == 6]
    condition = six_proj["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(six_proj)} employees with 6 active projects have rating >= 4.0."
    else:
        viol = six_proj[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All employees with more than 10 years of experience earn no more than $7.8 k per month."""
    exp_gt10 = df[df["years_experience"] > 10]
    condition = exp_gt10["monthly_salary_k"] <= 7.8
    truth = condition.all()
    if truth:
        expl = f"All {len(exp_gt10)} employees with >10 years experience earn <= $7.8k/month."
    else:
        viol = exp_gt10[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All marketing staff have a performance rating of at least 4.4."""
    marketing = df[df["department"] == "marketing"]
    condition = marketing["performance_rating"] >= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees have rating >= 4.4."
    else:
        viol = marketing[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees who work remotely ten or more days per month have a performance rating no higher than 4.0."""
    remote_10plus = df[df["remote_days_month"] >= 10]
    condition = remote_10plus["performance_rating"] <= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(remote_10plus)} employees working >=10 remote days/month have rating <= 4.0."
    else:
        viol = remote_10plus[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most employees have a performance rating of at least 4.0."""
    total = len(df)
    count_ge4 = (df["performance_rating"] >= 4.0).sum()
    proportion = count_ge4 / total
    truth = proportion > 0.5
    if truth:
        expl = f"{count_ge4}/{total} employees (proportion {proportion:.2f}) have rating >= 4.0."
    else:
        expl = f"Only {count_ge4}/{total} employees (proportion {proportion:.2f}) have rating >= 4.0."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_99.csv")

    # Convert numeric columns safely
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