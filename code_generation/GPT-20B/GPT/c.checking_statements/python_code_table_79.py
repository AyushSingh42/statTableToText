import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all engineering employees with more than 8 years of experience, performance rating is at most 3.8."""
    subset = df[(df["department"] == "engineering") & (df["years_experience"] > 8)]
    if subset.empty:
        return True, "No engineering employees with >8 years of experience to evaluate."
    condition = subset["performance_rating"] <= 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} qualifying employees have performance rating <= 3.8."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all HR employees, monthly salary is between $6.0k and $10.1k."""
    subset = df[df["department"] == "hr"]
    if subset.empty:
        return True, "No HR employees to evaluate."
    condition = subset["monthly_salary_k"].between(6.0, 10.1, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} HR employees have monthly salary between 6.0k and 10.1k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} HR employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all finance employees, performance rating is at least 4.2."""
    subset = df[df["department"] == "finance"]
    if subset.empty:
        return True, "No finance employees to evaluate."
    condition = subset["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} finance employees have performance rating >= 4.2."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} finance employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all employees who work remotely 12 or more days per month, the number of active projects does not exceed 6."""
    subset = df[df["remote_days_month"] >= 12]
    if subset.empty:
        return True, "No employees work remotely 12+ days per month."
    condition = subset["projects_active"] <= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} remote employees have <= 6 active projects."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all employees with monthly salary greater than $9k, performance rating is at least 4.0."""
    subset = df[df["monthly_salary_k"] > 9.0]
    if subset.empty:
        return True, "No employees with salary > 9k to evaluate."
    condition = subset["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} employees with salary > 9k have performance rating >= 4.0."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most employees have at least four active projects."""
    total = len(df)
    count_at_least_4 = df[df["projects_active"] >= 4].shape[0]
    truth = count_at_least_4 > total / 2
    if truth:
        expl = f"{count_at_least_4} out of {total} employees (>{total/2}) have >= 4 active projects."
    else:
        expl = f"Only {count_at_least_4} out of {total} employees have >= 4 active projects."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. There exists at least one marketing employee with a performance rating above 4.5."""
    subset = df[(df["department"] == "marketing") & (df["performance_rating"] > 4.5)]
    truth = not subset.empty
    if truth:
        expl = f"Found {len(subset)} marketing employee(s) with rating > 4.5."
    else:
        expl = "No marketing employee with rating > 4.5 found."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all employees with less than 2 years of experience, performance rating is at least 4.3."""
    subset = df[df["years_experience"] < 2]
    if subset.empty:
        return True, "No employees with < 2 years of experience."
    condition = subset["performance_rating"] >= 4.3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} employees with < 2 years have rating >= 4.3."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. For all employees with six active projects, monthly salary does not exceed $8.6k."""
    subset = df[df["projects_active"] == 6]
    if subset.empty:
        return True, "No employees with exactly 6 active projects."
    condition = subset["monthly_salary_k"] <= 8.6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} employees with 6 projects have salary <= 8.6k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. For all employees with a performance rating of at least 4.6, monthly salary is at least $7.3k."""
    subset = df[df["performance_rating"] >= 4.6]
    if subset.empty:
        return True, "No employees with rating >= 4.6."
    condition = subset["monthly_salary_k"] >= 7.3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} employees with rating >= 4.6 have salary >= 7.3k."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_79.csv")

    # Convert numeric columns safely
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()