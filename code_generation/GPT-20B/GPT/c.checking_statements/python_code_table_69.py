import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all engineering employees with more than 11 years of experience, monthly salary is at most $6.0k."""
    subset = df[(df["department"] == "engineering") & (df["years_experience"] > 11)]
    if subset.empty:
        return True, "No engineering employees with >11 years of experience to check."
    condition = subset["monthly_salary_k"] <= 6.0
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} engineering employees with >11 years of experience have monthly salary <= 6.0k."
    else:
        viol = subset[~condition]
        ids = viol["employee_id"].tolist()
        return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_2(df: pd.DataFrame):
    """2. All finance employees have a performance rating of at least 4.0."""
    subset = df[df["department"] == "finance"]
    if subset.empty:
        return True, "No finance employees to check."
    condition = subset["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} finance employees have performance rating >= 4.0."
    else:
        viol = subset[~condition]
        ids = viol["employee_id"].tolist()
        return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_3(df: pd.DataFrame):
    """3. All operations employees work remotely exactly 5 days per month."""
    subset = df[df["department"] == "operations"]
    if subset.empty:
        return True, "No operations employees to check."
    condition = subset["remote_days_month"] == 5
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} operations employees work remotely exactly 5 days per month."
    else:
        viol = subset[~condition]
        ids = viol["employee_id"].tolist()
        return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_4(df: pd.DataFrame):
    """4. Every employee with a performance rating of 4.8 or higher earns a monthly salary of at least $5.3k."""
    subset = df[df["performance_rating"] >= 4.8]
    if subset.empty:
        return True, "No employees with performance rating >= 4.8 to check."
    condition = subset["monthly_salary_k"] >= 5.3
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees with performance rating >= 4.8 have monthly salary >= 5.3k."
    else:
        viol = subset[~condition]
        ids = viol["employee_id"].tolist()
        return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_5(df: pd.DataFrame):
    """5. All marketing employees have a performance rating of no more than 4.1."""
    subset = df[df["department"] == "marketing"]
    if subset.empty:
        return True, "No marketing employees to check."
    condition = subset["performance_rating"] <= 4.1
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} marketing employees have performance rating <= 4.1."
    else:
        viol = subset[~condition]
        ids = viol["employee_id"].tolist()
        return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_6(df: pd.DataFrame):
    """6. All HR employees receive a monthly salary of no more than $5.4k."""
    subset = df[df["department"] == "hr"]
    if subset.empty:
        return True, "No HR employees to check."
    condition = subset["monthly_salary_k"] <= 5.4
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} HR employees have monthly salary <= 5.4k."
    else:
        viol = subset[~condition]
        ids = viol["employee_id"].tolist()
        return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_7(df: pd.DataFrame):
    """7. All employees with less than 3 years of experience earn a monthly salary of at least $8.3k."""
    subset = df[df["years_experience"] < 3]
    if subset.empty:
        return True, "No employees with <3 years of experience to check."
    condition = subset["monthly_salary_k"] >= 8.3
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees with <3 years of experience have monthly salary >= 8.3k."
    else:
        viol = subset[~condition]
        ids = viol["employee_id"].tolist()
        return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_8(df: pd.DataFrame):
    """8. All employees with more than 10 years of experience have a performance rating of at most 4.5."""
    subset = df[df["years_experience"] > 10]
    if subset.empty:
        return True, "No employees with >10 years of experience to check."
    condition = subset["performance_rating"] <= 4.5
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees with >10 years of experience have performance rating <= 4.5."
    else:
        viol = subset[~condition]
        ids = viol["employee_id"].tolist()
        return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_9(df: pd.DataFrame):
    """9. All engineering employees are assigned to no more than 4 active projects."""
    subset = df[df["department"] == "engineering"]
    if subset.empty:
        return True, "No engineering employees to check."
    condition = subset["projects_active"] <= 4
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} engineering employees have <= 4 active projects."
    else:
        viol = subset[~condition]
        ids = viol["employee_id"].tolist()
        return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_10(df: pd.DataFrame):
    """10. All employees with exactly 2 active projects earn a monthly salary of at least $7.3k."""
    subset = df[df["projects_active"] == 2]
    if subset.empty:
        return True, "No employees with exactly 2 active projects to check."
    condition = subset["monthly_salary_k"] >= 7.3
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} employees with 2 active projects have monthly salary >= 7.3k."
    else:
        viol = subset[~condition]
        ids = viol["employee_id"].tolist()
        return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_69.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col not in ["employee_id", "department"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Normalize department names to lowercase for consistency
    df["department"] = df["department"].str.lower()

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