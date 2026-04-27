import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the finance department have a monthly salary less than or equal to $10.2k."""
    finance = df[df["department"] == "finance"]
    condition = finance["monthly_salary_k"] <= 10.2
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have salary <= 10.2k."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All employees with more than 10 years of experience have a performance rating greater than or equal to 4.0."""
    exp10 = df[df["years_experience"] > 10]
    condition = exp10["performance_rating"] >= 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(exp10)} employees with >10 years experience have rating >= 4.0."
    else:
        viol = exp10[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If an employee is in the marketing department, then their monthly salary is greater than or equal to $9.0k."""
    marketing = df[df["department"] == "marketing"]
    condition = marketing["monthly_salary_k"] >= 9.0
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees have salary >= 9.0k."
    else:
        viol = marketing[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one employee in the engineering department whose monthly salary is greater than $9.0k."""
    engineering = df[df["department"] == "engineering"]
    condition = engineering["monthly_salary_k"] > 9.0
    truth = condition.any()
    if truth:
        viol = engineering[condition]
        expl = f"Found {len(viol)} engineering employee(s) with salary > 9.0k (IDs: {', '.join(viol['employee_id'].tolist())})."
    else:
        expl = "No engineering employee has salary > 9.0k."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All employees with a performance rating greater than 4.5 have more than 5 years of experience."""
    high_rating = df[df["performance_rating"] > 4.5]
    condition = high_rating["years_experience"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rating)} employees with rating > 4.5 have >5 years experience."
    else:
        viol = high_rating[~condition]
        expl = f"{len(viol)} employees violate the rule (years: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If an employee has more than 5 projects active, then their performance rating is less than or equal to 4.7."""
    many_projects = df[df["projects_active"] > 5]
    condition = many_projects["performance_rating"] <= 4.7
    truth = condition.all()
    if truth:
        expl = f"All {len(many_projects)} employees with >5 projects have rating <= 4.7."
    else:
        viol = many_projects[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most employees in the finance department have a monthly salary less than $8.0k."""
    finance = df[df["department"] == "finance"]
    if len(finance) == 0:
        truth = True
        expl = "No finance employees to evaluate; vacuously true."
    else:
        lt8 = finance["monthly_salary_k"] < 8.0
        truth = lt8.sum() > (len(finance) - lt8.sum())
        if truth:
            expl = f"{lt8.sum()} out of {len(finance)} finance employees have salary < 8.0k."
        else:
            expl = f"Only {lt8.sum()} out of {len(finance)} finance employees have salary < 8.0k."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All employees with a monthly salary greater than $9.5k have more than 4 years of experience."""
    high_salary = df[df["monthly_salary_k"] > 9.5]
    condition = high_salary["years_experience"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_salary)} employees with salary > 9.5k have >4 years experience."
    else:
        viol = high_salary[~condition]
        expl = f"{len(viol)} employees violate the rule (years: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If an employee is in the operations department, then their monthly salary is less than or equal to $10.5k."""
    ops = df[df["department"] == "operations"]
    condition = ops["monthly_salary_k"] <= 10.5
    truth = condition.all()
    if truth:
        expl = f"All {len(ops)} operations employees have salary <= 10.5k."
    else:
        viol = ops[~condition]
        expl = f"{len(viol)} operations employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one employee in the hr department whose monthly salary is greater than $9.0k."""
    hr = df[df["department"] == "hr"]
    condition = hr["monthly_salary_k"] > 9.0
    truth = condition.any()
    if truth:
        viol = hr[condition]
        expl = f"Found {len(viol)} HR employee(s) with salary > 9.0k (IDs: {', '.join(viol['employee_id'].tolist())})."
    else:
        expl = "No HR employee has salary > 9.0k."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All employees with more than 10 years of experience have a monthly salary greater than or equal to $5.5k."""
    exp10 = df[df["years_experience"] > 10]
    condition = exp10["monthly_salary_k"] >= 5.5
    truth = condition.all()
    if truth:
        expl = f"All {len(exp10)} employees with >10 years experience have salary >= 5.5k."
    else:
        viol = exp10[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If an employee has a performance rating greater than 4.0, then their monthly salary is greater than or equal to $5.5k."""
    high_rating = df[df["performance_rating"] > 4.0]
    condition = high_rating["monthly_salary_k"] >= 5.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rating)} employees with rating > 4.0 have salary >= 5.5k."
    else:
        viol = high_rating[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most employees have a monthly salary greater than $5.0k."""
    if len(df) == 0:
        truth = True
        expl = "No employees to evaluate; vacuously true."
    else:
        gt5 = df["monthly_salary_k"] > 5.0
        truth = gt5.sum() > (len(df) - gt5.sum())
        if truth:
            expl = f"{gt5.sum()} out of {len(df)} employees have salary > 5.0k."
        else:
            expl = f"Only {gt5.sum()} out of {len(df)} employees have salary > 5.0k."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All employees with a monthly salary less than $6.0k have a performance rating less than or equal to 4.7."""
    low_salary = df[df["monthly_salary_k"] < 6.0]
    condition = low_salary["performance_rating"] <= 4.7
    truth = condition.all()
    if truth:
        expl = f"All {len(low_salary)} employees with salary < 6.0k have rating <= 4.7."
    else:
        viol = low_salary[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If an employee is in the engineering department, then their monthly salary is greater than or equal to $8.0k."""
    engineering = df[df["department"] == "engineering"]
    condition = engineering["monthly_salary_k"] >= 8.0
    truth = condition.all()
    if truth:
        expl = f"All {len(engineering)} engineering employees have salary >= 8.0k."
    else:
        viol = engineering[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one employee in the marketing department whose monthly salary is greater than $10.0k."""
    marketing = df[df["department"] == "marketing"]
    condition = marketing["monthly_salary_k"] > 10.0
    truth = condition.any()
    if truth:
        viol = marketing[condition]
        expl = f"Found {len(viol)} marketing employee(s) with salary > 10.0k (IDs: {', '.join(viol['employee_id'].tolist())})."
    else:
        expl = "No marketing employee has salary > 10.0k."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_39.csv")

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
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()