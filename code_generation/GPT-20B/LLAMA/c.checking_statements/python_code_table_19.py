import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the operations department with more than 5 years of experience have a monthly salary greater than $6.2k."""
    ops = df[(df["department"] == "operations") & (df["years_experience"] > 5)]
    condition = ops["monthly_salary_k"] > 6.2
    truth = condition.all()
    if truth:
        expl = f"All {len(ops)} operations employees with >5 years experience have salary > 6.2k."
    else:
        viol = ops[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} operations employees with >5 years experience violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If an employee is in the engineering department, then their monthly salary is greater than $6.4k."""
    eng = df[df["department"] == "engineering"]
    condition = eng["monthly_salary_k"] > 6.4
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have salary > 6.4k."
    else:
        viol = eng[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} engineering employees violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one employee in the operations department with a performance rating greater than 4.7."""
    ops = df[(df["department"] == "operations") & (df["performance_rating"] > 4.7)]
    truth = not ops.empty
    if truth:
        expl = f"Found {len(ops)} operations employee(s) with rating > 4.7 (IDs: {', '.join(map(str, ops['employee_id'].tolist()))})."
    else:
        expl = "No operations employee has a performance rating > 4.7."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 10 years of experience have a monthly salary less than or equal to $10.7k."""
    exp = df[df["years_experience"] > 10]
    condition = exp["monthly_salary_k"] <= 10.7
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >10 years experience have salary <= 10.7k."
    else:
        viol = exp[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} employees with >10 years experience violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If an employee is in the finance department, then their years of experience are less than 8 years."""
    fin = df[df["department"] == "finance"]
    condition = fin["years_experience"] < 8
    truth = condition.all()
    if truth:
        expl = f"All {len(fin)} finance employees have <8 years experience."
    else:
        viol = fin[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} finance employees violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All employees with a monthly salary greater than $10k have a performance rating greater than 4.0."""
    high_sal = df[df["monthly_salary_k"] > 10]
    condition = high_sal["performance_rating"] > 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sal)} employees with salary > 10k have rating > 4.0."
    else:
        viol = high_sal[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} high-salary employees violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most employees in the operations department have a monthly salary less than $10k."""
    ops = df[df["department"] == "operations"]
    count = len(ops)
    if count == 0:
        truth = True
        expl = "No operations employees to evaluate."
    else:
        good = ops["monthly_salary_k"] < 10
        good_count = good.sum()
        truth = good_count > count / 2
        if truth:
            expl = f"{good_count} out of {count} operations employees have salary < 10k."
        else:
            expl = f"Only {good_count} out of {count} operations employees have salary < 10k."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If an employee has more than 5 projects active, then their monthly salary is less than $10.2k."""
    proj = df[df["projects_active"] > 5]
    condition = proj["monthly_salary_k"] < 10.2
    truth = condition.all()
    if truth:
        expl = f"All {len(proj)} employees with >5 projects have salary < 10.2k."
    else:
        viol = proj[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} employees with >5 projects violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one employee in the engineering department with a monthly salary less than $8.2k."""
    eng = df[(df["department"] == "engineering") & (df["monthly_salary_k"] < 8.2)]
    truth = not eng.empty
    if truth:
        expl = f"Found {len(eng)} engineering employee(s) with salary < 8.2k (IDs: {', '.join(map(str, eng['employee_id'].tolist()))})."
    else:
        expl = "No engineering employee has a salary < 8.2k."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with a performance rating greater than 4.6 have a monthly salary greater than $6.7k."""
    high_rat = df[df["performance_rating"] > 4.6]
    condition = high_rat["monthly_salary_k"] > 6.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rat)} employees with rating > 4.6 have salary > 6.7k."
    else:
        viol = high_rat[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} high-rating employees violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If an employee is in the hr department, then their monthly salary is greater than $6.7k."""
    hr = df[df["department"] == "hr"]
    condition = hr["monthly_salary_k"] > 6.7
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have salary > 6.7k."
    else:
        viol = hr[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} HR employees violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All employees with more than 4 remote days per month have a monthly salary less than $10.7k."""
    remote = df[df["remote_days_month"] > 4]
    condition = remote["monthly_salary_k"] < 10.7
    truth = condition.all()
    if truth:
        expl = f"All {len(remote)} employees with >4 remote days have salary < 10.7k."
    else:
        viol = remote[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} remote employees violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most employees in the engineering department have a monthly salary greater than $7.5k."""
    eng = df[df["department"] == "engineering"]
    count = len(eng)
    if count == 0:
        truth = True
        expl = "No engineering employees to evaluate."
    else:
        good = eng["monthly_salary_k"] > 7.5
        good_count = good.sum()
        truth = good_count > count / 2
        if truth:
            expl = f"{good_count} out of {count} engineering employees have salary > 7.5k."
        else:
            expl = f"Only {good_count} out of {count} engineering employees have salary > 7.5k."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If an employee has more than 3 years of experience, then their monthly salary is greater than $5.9k."""
    exp = df[df["years_experience"] > 3]
    condition = exp["monthly_salary_k"] > 5.9
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >3 years experience have salary > 5.9k."
    else:
        viol = exp[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} employees with >3 years experience violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one employee in the finance department with a monthly salary greater than $10.1k."""
    fin = df[(df["department"] == "finance") & (df["monthly_salary_k"] > 10.1)]
    truth = not fin.empty
    if truth:
        expl = f"Found {len(fin)} finance employee(s) with salary > 10.1k (IDs: {', '.join(map(str, fin['employee_id'].tolist()))})."
    else:
        expl = "No finance employee has a salary > 10.1k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All employees with a monthly salary less than $6k have a performance rating less than 4.7."""
    low_sal = df[df["monthly_salary_k"] < 6]
    condition = low_sal["performance_rating"] < 4.7
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sal)} employees with salary < 6k have rating < 4.7."
    else:
        viol = low_sal[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} low-salary employees violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If an employee is in the operations department, then their years of experience are less than 12 years."""
    ops = df[df["department"] == "operations"]
    condition = ops["years_experience"] < 12
    truth = condition.all()
    if truth:
        expl = f"All {len(ops)} operations employees have <12 years experience."
    else:
        viol = ops[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} operations employees violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All employees with a performance rating greater than 4.4 have a monthly salary greater than $5.5k."""
    high_rat = df[df["performance_rating"] > 4.4]
    condition = high_rat["monthly_salary_k"] > 5.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rat)} employees with rating > 4.4 have salary > 5.5k."
    else:
        viol = high_rat[~condition]
        viol_ids = viol["employee_id"].tolist()
        expl = f"{len(viol)} high-rating employees violate the rule (IDs: {', '.join(map(str, viol_ids))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_19.csv")

    # Convert numeric columns safely.
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
        (18, stmt_18),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()