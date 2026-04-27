import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All HR employees have a monthly salary of at most $7.7k."""
    hr_df = df[df["department"] == "hr"]
    if hr_df.empty:
        return True, "No HR employees in dataset."
    condition = hr_df["monthly_salary_k"] <= 7.7
    truth = condition.all()
    if truth:
        expl = f"All {len(hr_df)} HR employees have salary <= $7.7k."
    else:
        viol = hr_df[~condition]
        expl = f"{len(viol)} HR employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All HR employees have a performance rating of at least 3.9."""
    hr_df = df[df["department"] == "hr"]
    if hr_df.empty:
        return True, "No HR employees in dataset."
    condition = hr_df["performance_rating"] >= 3.9
    truth = condition.all()
    if truth:
        expl = f"All {len(hr_df)} HR employees have performance rating >= 3.9."
    else:
        viol = hr_df[~condition]
        expl = f"{len(viol)} HR employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All finance employees have a performance rating of exactly 4.3."""
    fin_df = df[df["department"] == "finance"]
    if fin_df.empty:
        return True, "No finance employees in dataset."
    condition = fin_df["performance_rating"] == 4.3
    truth = condition.all()
    if truth:
        expl = f"All {len(fin_df)} finance employees have performance rating = 4.3."
    else:
        viol = fin_df[~condition]
        expl = f"{len(viol)} finance employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All engineering employees work remotely at least 13 days per month."""
    eng_df = df[df["department"] == "engineering"]
    if eng_df.empty:
        return True, "No engineering employees in dataset."
    condition = eng_df["remote_days_month"] >= 13
    truth = condition.all()
    if truth:
        expl = f"All {len(eng_df)} engineering employees work remotely >= 13 days/month."
    else:
        viol = eng_df[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All operations employees with more than 7 years of experience have a monthly salary of at most $8.5k."""
    ops_df = df[(df["department"] == "operations") & (df["years_experience"] > 7)]
    if ops_df.empty:
        return True, "No qualifying operations employees in dataset."
    condition = ops_df["monthly_salary_k"] <= 8.5
    truth = condition.all()
    if truth:
        expl = f"All {len(ops_df)} operations employees with >7 years experience have salary <= $8.5k."
    else:
        viol = ops_df[~condition]
        expl = f"{len(viol)} operations employees with >7 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All employees with a performance rating of at least 4.5 have more than 5 years of experience."""
    emp_df = df[df["performance_rating"] >= 4.5]
    if emp_df.empty:
        return True, "No employees with performance rating >= 4.5 in dataset."
    condition = emp_df["years_experience"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(emp_df)} employees with performance rating >= 4.5 have >5 years experience."
    else:
        viol = emp_df[~condition]
        expl = f"{len(viol)} employees with performance rating >= 4.5 violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees earning more than $9k per month have a performance rating of no higher than 4.4."""
    emp_df = df[df["monthly_salary_k"] > 9]
    if emp_df.empty:
        return True, "No employees earning >$9k in dataset."
    condition = emp_df["performance_rating"] <= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(emp_df)} employees earning >$9k have performance rating <= 4.4."
    else:
        viol = emp_df[~condition]
        expl = f"{len(viol)} employees earning >$9k violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees with at least 10 years of experience are active on at most five projects."""
    emp_df = df[df["years_experience"] >= 10]
    if emp_df.empty:
        return True, "No employees with >=10 years experience in dataset."
    condition = emp_df["projects_active"] <= 5
    truth = condition.all()
    if truth:
        expl = f"All {len(emp_df)} employees with >=10 years experience are active on <=5 projects."
    else:
        viol = emp_df[~condition]
        expl = f"{len(viol)} employees with >=10 years experience violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All employees with a performance rating of at least 4.5 have more than 5 years of experience."""
    emp_df = df[df["performance_rating"] >= 4.5]
    if emp_df.empty:
        return True, "No employees with performance rating >= 4.5 in dataset."
    condition = emp_df["years_experience"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(emp_df)} employees with performance rating >= 4.5 have >5 years experience."
    else:
        viol = emp_df[~condition]
        expl = f"{len(viol)} employees with performance rating >= 4.5 violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_59.csv")

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