import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all engineering employees, monthly salary is at most $7.6k."""
    subset = df[df["department"] == "engineering"]
    if subset.empty:
        return True, "No engineering employees; statement holds vacuously."
    condition = subset["monthly_salary_k"] <= 7.6
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} engineering employees have salary <= 7.6k."
    violators = subset[~condition]
    ids = violators["employee_id"].tolist()
    salaries = violators["monthly_salary_k"].tolist()
    details = ", ".join(f"{eid} (${sal}k)" for eid, sal in zip(ids, salaries))
    return False, f"{len(violators)} engineering employees violate the rule: {details}."

def stmt_2(df: pd.DataFrame):
    """2. All HR employees have a performance rating of at least 4.2."""
    subset = df[df["department"] == "hr"]
    if subset.empty:
        return True, "No HR employees; statement holds vacuously."
    condition = subset["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} HR employees have rating >= 4.2."
    violators = subset[~condition]
    ids = violators["employee_id"].tolist()
    ratings = violators["performance_rating"].tolist()
    details = ", ".join(f"{eid} ({rat})" for eid, rat in zip(ids, ratings))
    return False, f"{len(violators)} HR employees violate the rule: {details}."

def stmt_3(df: pd.DataFrame):
    """3. All finance employees are involved in at least two active projects."""
    subset = df[df["department"] == "finance"]
    if subset.empty:
        return True, "No finance employees; statement holds vacuously."
    condition = subset["projects_active"] >= 2
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} finance employees have >= 2 active projects."
    violators = subset[~condition]
    ids = violators["employee_id"].tolist()
    projects = violators["projects_active"].tolist()
    details = ", ".join(f"{eid} ({proj})" for eid, proj in zip(ids, projects))
    return False, f"{len(violators)} finance employees violate the rule: {details}."

def stmt_4(df: pd.DataFrame):
    """4. All employees with six active projects have monthly salary at most $7.4k."""
    subset = df[df["projects_active"] == 6]
    if subset.empty:
        return True, "No employees with six active projects; statement holds vacuously."
    condition = subset["monthly_salary_k"] <= 7.4
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees with 6 projects have salary <= 7.4k."
    violators = subset[~condition]
    ids = violators["employee_id"].tolist()
    salaries = violators["monthly_salary_k"].tolist()
    details = ", ".join(f"{eid} (${sal}k)" for eid, sal in zip(ids, salaries))
    return False, f"{len(violators)} employees violate the rule: {details}."

def stmt_5(df: pd.DataFrame):
    """5. All employees who work remotely fourteen or more days per month have a performance rating of at least 4.2."""
    subset = df[df["remote_days_month"] >= 14]
    if subset.empty:
        return True, "No employees remote >= 14 days; statement holds vacuously."
    condition = subset["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees remote >= 14 days have rating >= 4.2."
    violators = subset[~condition]
    ids = violators["employee_id"].tolist()
    ratings = violators["performance_rating"].tolist()
    details = ", ".join(f"{eid} ({rat})" for eid, rat in zip(ids, ratings))
    return False, f"{len(violators)} employees violate the rule: {details}."

def stmt_6(df: pd.DataFrame):
    """6. All operations employees work remotely no more than nine days per month."""
    subset = df[df["department"] == "operations"]
    if subset.empty:
        return True, "No operations employees; statement holds vacuously."
    condition = subset["remote_days_month"] <= 9
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} operations employees remote <= 9 days."
    violators = subset[~condition]
    ids = violators["employee_id"].tolist()
    days = violators["remote_days_month"].tolist()
    details = ", ".join(f"{eid} ({day})" for eid, day in zip(ids, days))
    return False, f"{len(violators)} operations employees violate the rule: {details}."

def stmt_7(df: pd.DataFrame):
    """7. Most employees have a performance rating of at least 4.0."""
    total = len(df)
    count = (df["performance_rating"] >= 4.0).sum()
    truth = count > total / 2
    if truth:
        return True, f"{count} out of {total} employees have rating >= 4.0 ({count/total:.2%})."
    else:
        return False, f"Only {count} out of {total} employees have rating >= 4.0 ({count/total:.2%})."

def stmt_8(df: pd.DataFrame):
    """8. All employees earning more than $9k per month work remotely no more than eight days per month."""
    subset = df[df["monthly_salary_k"] > 9]
    if subset.empty:
        return True, "No employees earning > 9k; statement holds vacuously."
    condition = subset["remote_days_month"] <= 8
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees earning > 9k remote <= 8 days."
    violators = subset[~condition]
    ids = violators["employee_id"].tolist()
    days = violators["remote_days_month"].tolist()
    details = ", ".join(f"{eid} ({day})" for eid, day in zip(ids, days))
    return False, f"{len(violators)} employees violate the rule: {details}."

def stmt_9(df: pd.DataFrame):
    """9. All marketing employees are involved in at least three active projects."""
    subset = df[df["department"] == "marketing"]
    if subset.empty:
        return True, "No marketing employees; statement holds vacuously."
    condition = subset["projects_active"] >= 3
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} marketing employees have >= 3 active projects."
    violators = subset[~condition]
    ids = violators["employee_id"].tolist()
    projects = violators["projects_active"].tolist()
    details = ", ".join(f"{eid} ({proj})" for eid, proj in zip(ids, projects))
    return False, f"{len(violators)} marketing employees violate the rule: {details}."

def stmt_10(df: pd.DataFrame):
    """10. All employees with at least twelve years of experience have a performance rating of at least 4.0."""
    subset = df[df["years_experience"] >= 12]
    if subset.empty:
        return True, "No employees with >= 12 years experience; statement holds vacuously."
    condition = subset["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees with >= 12 years have rating >= 4.0."
    violators = subset[~condition]
    ids = violators["employee_id"].tolist()
    ratings = violators["performance_rating"].tolist()
    details = ", ".join(f"{eid} ({rat})" for eid, rat in zip(ids, ratings))
    return False, f"{len(violators)} employees violate the rule: {details}."

def main():
    df = pd.read_csv("../inference_generation/tables/table_9.csv")
    # Convert numeric columns safely
    for col in df.columns:
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
        (10, stmt_10),
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()