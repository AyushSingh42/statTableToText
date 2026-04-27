import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the marketing department with more than 5 years of experience have a monthly salary greater than $6.1k."""
    subset = df[(df["department"] == "marketing") & (df["years_experience"] > 5)]
    if subset.empty:
        return True, "No marketing employees with >5 years of experience; statement vacuously true."
    condition = subset["monthly_salary_k"] > 6.1
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} marketing employees with >5 years of experience have salary > 6.1k."
    viol = subset[~condition]
    return False, f"{len(viol)} employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def stmt_2(df: pd.DataFrame):
    """2. If an employee is in the finance department, then their monthly salary is greater than or equal to $5.9k."""
    subset = df[df["department"] == "finance"]
    if subset.empty:
        return True, "No finance employees; statement vacuously true."
    condition = subset["monthly_salary_k"] >= 5.9
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} finance employees have salary >= 5.9k."
    viol = subset[~condition]
    return False, f"{len(viol)} finance employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one employee in the engineering department with a performance rating greater than 4.4."""
    subset = df[(df["department"] == "engineering") & (df["performance_rating"] > 4.4)]
    truth = not subset.empty
    if truth:
        return True, f"Found {len(subset)} engineering employee(s) with rating > 4.4 (ids: {', '.join(subset['employee_id'])})."
    return False, "No engineering employee has performance rating > 4.4."

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 8 years of experience have a monthly salary greater than $6.6k."""
    subset = df[df["years_experience"] > 8]
    if subset.empty:
        return True, "No employees with >8 years of experience; statement vacuously true."
    condition = subset["monthly_salary_k"] > 6.6
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees with >8 years of experience have salary > 6.6k."
    viol = subset[~condition]
    return False, f"{len(viol)} employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def stmt_5(df: pd.DataFrame):
    """5. If an employee is in the HR department, then their years of experience are less than 9 years."""
    subset = df[df["department"] == "HR"]
    if subset.empty:
        return True, "No HR employees; statement vacuously true."
    condition = subset["years_experience"] < 9
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} HR employees have <9 years of experience."
    viol = subset[~condition]
    return False, f"{len(viol)} HR employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def stmt_6(df: pd.DataFrame):
    """6. Most employees in the marketing department have a monthly salary greater than $6.0k."""
    subset = df[df["department"] == "marketing"]
    if subset.empty:
        return False, "No marketing employees to evaluate majority."
    count = len(subset)
    satisfied = subset["monthly_salary_k"] > 6.0
    num_satisfied = satisfied.sum()
    truth = num_satisfied > count / 2
    percent = num_satisfied / count * 100
    if truth:
        return True, f"{num_satisfied} out of {count} marketing employees have salary > 6.0k ({percent:.1f}%)."
    return False, f"Only {num_satisfied} out of {count} marketing employees have salary > 6.0k ({percent:.1f}%)."

def stmt_7(df: pd.DataFrame):
    """7. All employees with a performance rating greater than 4.5 have more than 3 projects active."""
    subset = df[df["performance_rating"] > 4.5]
    if subset.empty:
        return True, "No employees with rating > 4.5; statement vacuously true."
    condition = subset["projects_active"] > 3
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees with rating > 4.5 have >3 projects."
    viol = subset[~condition]
    return False, f"{len(viol)} employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def stmt_8(df: pd.DataFrame):
    """8. If an employee has more than 10 remote days per month, then their monthly salary is greater than $6.0k."""
    subset = df[df["remote_days_month"] > 10]
    if subset.empty:
        return True, "No employees with >10 remote days; statement vacuously true."
    condition = subset["monthly_salary_k"] > 6.0
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees with >10 remote days have salary > 6.0k."
    viol = subset[~condition]
    return False, f"{len(viol)} employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one employee in the finance department with a monthly salary greater than $7.8k."""
    subset = df[(df["department"] == "finance") & (df["monthly_salary_k"] > 7.8)]
    truth = not subset.empty
    if truth:
        return True, f"Found {len(subset)} finance employee(s) with salary > 7.8k (ids: {', '.join(subset['employee_id'])})."
    return False, "No finance employee has salary > 7.8k."

def stmt_10(df: pd.DataFrame):
    """10. All employees with more than 4 years of experience in the marketing department have a performance rating greater than 3.7."""
    subset = df[(df["department"] == "marketing") & (df["years_experience"] > 4)]
    if subset.empty:
        return True, "No marketing employees with >4 years; statement vacuously true."
    condition = subset["performance_rating"] > 3.7
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} marketing employees with >4 years have rating > 3.7."
    viol = subset[~condition]
    return False, f"{len(viol)} employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def stmt_11(df: pd.DataFrame):
    """11. If an employee is in the engineering department, then their monthly salary is greater than or equal to $6.0k."""
    subset = df[df["department"] == "engineering"]
    if subset.empty:
        return True, "No engineering employees; statement vacuously true."
    condition = subset["monthly_salary_k"] >= 6.0
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} engineering employees have salary >= 6.0k."
    viol = subset[~condition]
    return False, f"{len(viol)} engineering employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def stmt_12(df: pd.DataFrame):
    """12. Most employees with more than 5 years of experience have a monthly salary greater than $6.2k."""
    subset = df[df["years_experience"] > 5]
    if subset.empty:
        return False, "No employees with >5 years of experience to evaluate majority."
    count = len(subset)
    satisfied = subset["monthly_salary_k"] > 6.2
    num_satisfied = satisfied.sum()
    truth = num_satisfied > count / 2
    percent = num_satisfied / count * 100
    if truth:
        return True, f"{num_satisfied} out of {count} employees with >5 years have salary > 6.2k ({percent:.1f}%)."
    return False, f"Only {num_satisfied} out of {count} employees with >5 years have salary > 6.2k ({percent:.1f}%)."

def stmt_13(df: pd.DataFrame):
    """13. All employees with a monthly salary greater than $7.0k have more than 2 projects active."""
    subset = df[df["monthly_salary_k"] > 7.0]
    if subset.empty:
        return True, "No employees with salary > 7.0k; statement vacuously true."
    condition = subset["projects_active"] > 2
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees with salary > 7.0k have >2 projects."
    viol = subset[~condition]
    return False, f"{len(viol)} employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def stmt_14(df: pd.DataFrame):
    """14. If an employee has more than 5 years of experience in the HR department, then their monthly salary is less than $6.2k."""
    subset = df[(df["department"] == "HR") & (df["years_experience"] > 5)]
    if subset.empty:
        return True, "No HR employees with >5 years; statement vacuously true."
    condition = subset["monthly_salary_k"] < 6.2
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} HR employees with >5 years have salary < 6.2k."
    viol = subset[~condition]
    return False, f"{len(viol)} HR employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one employee in the marketing department with a monthly salary greater than $8.6k."""
    subset = df[(df["department"] == "marketing") & (df["monthly_salary_k"] > 8.6)]
    truth = not subset.empty
    if truth:
        return True, f"Found {len(subset)} marketing employee(s) with salary > 8.6k (ids: {', '.join(subset['employee_id'])})."
    return False, "No marketing employee has salary > 8.6k."

def stmt_16(df: pd.DataFrame):
    """16. All employees with a performance rating greater than 4.8 have more than 2 projects active."""
    subset = df[df["performance_rating"] > 4.8]
    if subset.empty:
        return True, "No employees with rating > 4.8; statement vacuously true."
    condition = subset["projects_active"] > 2
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees with rating > 4.8 have >2 projects."
    viol = subset[~condition]
    return False, f"{len(viol)} employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def stmt_17(df: pd.DataFrame):
    """17. If an employee is in the finance department with more than 8 years of experience, then their monthly salary is greater than $7.0k."""
    subset = df[(df["department"] == "finance") & (df["years_experience"] > 8)]
    if subset.empty:
        return True, "No finance employees with >8 years; statement vacuously true."
    condition = subset["monthly_salary_k"] > 7.0
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} finance employees with >8 years have salary > 7.0k."
    viol = subset[~condition]
    return False, f"{len(viol)} finance employees violate the rule (ids: {', '.join(viol['employee_id'])})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_89.csv")

    # Convert numeric columns
    numeric_cols = ["years_experience", "monthly_salary_k", "projects_active", "performance_rating", "remote_days_month"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

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
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()