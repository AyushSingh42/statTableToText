import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the engineering department with more than 10 years of experience have a monthly salary less than or equal to $6.9k."""
    cond = (df["department"] == "engineering") & (df["years_experience"] > 10)
    subset = df[cond]
    if subset.empty:
        return True, "No engineering employees with >10 years of experience."
    truth = (subset["monthly_salary_k"] <= 6.9).all()
    if truth:
        return True, f"All {len(subset)} qualifying employees have salary <= 6.9k."
    viol = subset[~(subset["monthly_salary_k"] <= 6.9)]
    ids = viol["employee_id"].tolist()
    return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_2(df: pd.DataFrame):
    """2. All employees in the finance department have a monthly salary greater than or equal to $7.0k."""
    subset = df[df["department"] == "finance"]
    if subset.empty:
        return True, "No finance employees."
    truth = (subset["monthly_salary_k"] >= 7.0).all()
    if truth:
        return True, f"All {len(subset)} finance employees have salary >= 7.0k."
    viol = subset[~(subset["monthly_salary_k"] >= 7.0)]
    ids = viol["employee_id"].tolist()
    return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_3(df: pd.DataFrame):
    """3. If an employee is in the operations department, then their years of experience are greater than 8."""
    subset = df[df["department"] == "operations"]
    if subset.empty:
        return True, "No operations employees."
    truth = (subset["years_experience"] > 8).all()
    if truth:
        return True, f"All {len(subset)} operations employees have >8 years experience."
    viol = subset[~(subset["years_experience"] > 8)]
    ids = viol["employee_id"].tolist()
    return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_4(df: pd.DataFrame):
    """4. All employees with a performance rating greater than 4.5 have a monthly salary less than or equal to $7.8k."""
    subset = df[df["performance_rating"] > 4.5]
    if subset.empty:
        return True, "No employees with performance rating >4.5."
    truth = (subset["monthly_salary_k"] <= 7.8).all()
    if truth:
        return True, f"All {len(subset)} employees with rating >4.5 have salary <= 7.8k."
    viol = subset[~(subset["monthly_salary_k"] <= 7.8)]
    ids = viol["employee_id"].tolist()
    return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_5(df: pd.DataFrame):
    """5. There exists at least one employee in the marketing department with a monthly salary greater than $9.0k."""
    subset = df[(df["department"] == "marketing") & (df["monthly_salary_k"] > 9.0)]
    truth = not subset.empty
    if truth:
        ids = subset["employee_id"].tolist()
        return True, f"Employees {', '.join(ids)} satisfy the condition."
    return False, "No marketing employee has salary >9.0k."

def stmt_6(df: pd.DataFrame):
    """6. All employees with more than 10 years of experience have a performance rating less than or equal to 4.8."""
    subset = df[df["years_experience"] > 10]
    if subset.empty:
        return True, "No employees with >10 years experience."
    truth = (subset["performance_rating"] <= 4.8).all()
    if truth:
        return True, f"All {len(subset)} employees with >10 years experience have rating <= 4.8."
    viol = subset[~(subset["performance_rating"] <= 4.8)]
    ids = viol["employee_id"].tolist()
    return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_7(df: pd.DataFrame):
    """7. If an employee is in the hr department, then their monthly salary is less than or equal to $5.4k."""
    subset = df[df["department"] == "hr"]
    if subset.empty:
        return True, "No hr employees."
    truth = (subset["monthly_salary_k"] <= 5.4).all()
    if truth:
        return True, f"All {len(subset)} hr employees have salary <= 5.4k."
    viol = subset[~(subset["monthly_salary_k"] <= 5.4)]
    ids = viol["employee_id"].tolist()
    return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_8(df: pd.DataFrame):
    """8. All employees with a monthly salary greater than $9.0k have less than or equal to 3 projects active."""
    subset = df[df["monthly_salary_k"] > 9.0]
    if subset.empty:
        return True, "No employees with salary >9.0k."
    truth = (subset["projects_active"] <= 3).all()
    if truth:
        return True, f"All {len(subset)} employees with salary >9.0k have <=3 projects."
    viol = subset[~(subset["projects_active"] <= 3)]
    ids = viol["employee_id"].tolist()
    return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_9(df: pd.DataFrame):
    """9. Most employees have a remote days per month greater than or equal to 5."""
    count = (df["remote_days_month"] >= 5).sum()
    truth = count > len(df) / 2
    if truth:
        return True, f"{count} out of {len(df)} employees have remote days >=5."
    return False, f"Only {count} out of {len(df)} employees have remote days >=5."

def stmt_10(df: pd.DataFrame):
    """10. All employees with a performance rating greater than 4.0 have a monthly salary greater than or equal to $5.1k."""
    subset = df[df["performance_rating"] > 4.0]
    if subset.empty:
        return True, "No employees with performance rating >4.0."
    truth = (subset["monthly_salary_k"] >= 5.1).all()
    if truth:
        return True, f"All {len(subset)} employees with rating >4.0 have salary >=5.1k."
    viol = subset[~(subset["monthly_salary_k"] >= 5.1)]
    ids = viol["employee_id"].tolist()
    return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def stmt_11(df: pd.DataFrame):
    """11. If an employee is in the engineering department, then their years of experience are greater than or equal to 2."""
    subset = df[df["department"] == "engineering"]
    if subset.empty:
        return True, "No engineering employees."
    truth = (subset["years_experience"] >= 2).all()
    if truth:
        return True, f"All {len(subset)} engineering employees have >=2 years experience."
    viol = subset[~(subset["years_experience"] >= 2)]
    ids = viol["employee_id"].tolist()
    return False, f"{len(viol)} employees violate the rule (IDs: {', '.join(ids)})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_69.csv")

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
        (10, stmt_10),
        (11, stmt_11),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()