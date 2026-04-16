import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the engineering department with more than 5 years of experience have a monthly salary above 8 thousand."""
    eng_dept = df[df["department"] == "engineering"]
    condition = eng_dept["years_experience"] > 5
    condition = condition & (eng_dept["monthly_salary_k"] > 8)
    truth = condition.all()
    if truth:
        expl = f"All {len(eng_dept[condition])} employees in the engineering department with more than 5 years of experience have a monthly salary above 8 thousand."
    else:
        viol = eng_dept[~condition]
        expl = f"{len(viol)} employees in the engineering department with more than 5 years of experience have a monthly salary of 8 thousand or less (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If an employee has a performance rating above 4.2, they are more likely to work remotely for more than 8 days a month."""
    condition = df["performance_rating"] > 4.2
    condition = condition & (df["remote_days_month"] > 8)
    truth = condition.all()
    if truth:
        expl = f"All {len(df[condition])} employees with a performance rating above 4.2 work remotely for more than 8 days a month."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} employees with a performance rating above 4.2 do not work remotely for more than 8 days a month (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Employees in the finance department with less than 5 years of experience have a lower monthly salary than those in the marketing department."""
    finance_dept = df[df["department"] == "finance"]
    marketing_dept = df[df["department"] == "marketing"]
    finance_condition = finance_dept["years_experience"] < 5
    marketing_condition = marketing_dept["years_experience"] < 5
    finance_salaries = finance_dept[finance_condition]["monthly_salary_k"]
    marketing_salaries = marketing_dept[marketing_condition]["monthly_salary_k"]
    truth = (finance_salaries < marketing_salaries).all()
    if truth:
        expl = f"All {len(finance_salaries)} employees in the finance department with less than 5 years of experience have a lower monthly salary than those in the marketing department."
    else:
        viol = finance_salaries[finance_salaries >= marketing_salaries]
        expl = f"{len(viol)} employees in the finance department with less than 5 years of experience have a monthly salary of {', '.join(map(str, viol.tolist()))} which is not lower than those in the marketing department."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 10 years of experience are in either the engineering or finance departments."""
    condition = df["years_experience"] > 10
    condition = condition & ((df["department"] == "engineering") | (df["department"] == "finance"))
    truth = condition.all()
    if truth:
        expl = f"All {len(df[condition])} employees with more than 10 years of experience are in either the engineering or finance departments."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} employees with more than 10 years of experience are not in either the engineering or finance departments (departments: {', '.join(map(str, viol['department'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If an employee is in the hr department, they are more likely to have a performance rating between 3.9 and 4.1."""
    hr_dept = df[df["department"] == "hr"]
    condition = hr_dept["performance_rating"].between(3.9, 4.1, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(hr_dept[condition])} employees in the hr department have a performance rating between 3.9 and 4.1."
    else:
        viol = hr_dept[~condition]
        expl = f"{len(viol)} employees in the hr department have a performance rating of {', '.join(map(str, viol['performance_rating'].tolist()))} which is not between 3.9 and 4.1."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Employees with a monthly salary above 7 thousand are more likely to have more than 3 active projects."""
    condition = df["monthly_salary_k"] > 7
    condition = condition & (df["projects_active"] > 3)
    truth = condition.all()
    if truth:
        expl = f"All {len(df[condition])} employees with a monthly salary above 7 thousand have more than 3 active projects."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} employees with a monthly salary above 7 thousand do not have more than 3 active projects (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees in the marketing department with a performance rating above 4.0 have a monthly salary above 5.5 thousand."""
    marketing_dept = df[df["department"] == "marketing"]
    condition = marketing_dept["performance_rating"] > 4.0
    condition = condition & (marketing_dept["monthly_salary_k"] > 5.5)
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing_dept[condition])} employees in the marketing department with a performance rating above 4.0 have a monthly salary above 5.5 thousand."
    else:
        viol = marketing_dept[~condition]
        expl = f"{len(viol)} employees in the marketing department with a performance rating above 4.0 have a monthly salary of {', '.join(map(str, viol['monthly_salary_k'].tolist()))} which is not above 5.5 thousand."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If an employee has more than 5 active projects, they are more likely to be in the engineering department."""
    condition = df["projects_active"] > 5
    condition = condition & (df["department"] == "engineering")
    truth = condition.all()
    if truth:
        expl = f"All {len(df[condition])} employees with more than 5 active projects are in the engineering department."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} employees with more than 5 active projects are not in the engineering department (departments: {', '.join(map(str, viol['department'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Employees in the finance department with more than 5 years of experience have a higher monthly salary than those in the hr department."""
    finance_dept = df[df["department"] == "finance"]
    hr_dept = df[df["department"] == "hr"]
    finance_condition = finance_dept["years_experience"] > 5
    hr_condition = hr_dept["years_experience"] > 5
    finance_salaries = finance_dept[finance_condition]["monthly_salary_k"]
    hr_salaries = hr_dept[hr_condition]["monthly_salary_k"]
    truth = (finance_salaries > hr_salaries).all()
    if truth:
        expl = f"All {len(finance_salaries)} employees in the finance department with more than 5 years of experience have a higher monthly salary than those in the hr department."
    else:
        viol = finance_salaries[finance_salaries <= hr_salaries]
        expl = f"{len(viol)} employees in the finance department with more than 5 years of experience have a monthly salary of {', '.join(map(str, viol.tolist()))} which is not higher than those in the hr department."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with a performance rating above 4.5 have more than 2 active projects."""
    condition = df["performance_rating"] > 4.5
    condition = condition & (df["projects_active"] > 2)
    truth = condition.all()
    if truth:
        expl = f"All {len(df[condition])} employees with a performance rating above 4.5 have more than 2 active projects."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} employees with a performance rating above 4.5 do not have more than 2 active projects (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If an employee is in the engineering department, they are more likely to have a monthly salary above 6 thousand if they have more than 3 years of experience."""
    eng_dept = df[df["department"] == "engineering"]
    condition = eng_dept["years_experience"] > 3
    condition = condition & (eng_dept["monthly_salary_k"] > 6)
    truth = condition.all()
    if truth:
        expl = f"All {len(eng_dept[condition])} employees in the engineering department with more than 3 years of experience have a monthly salary above 6 thousand."
    else:
        viol = eng_dept[~condition]
        expl = f"{len(viol)} employees in the engineering department with more than 3 years of experience have a monthly salary of {', '.join(map(str, viol['monthly_salary_k'].tolist()))} which is not above 6 thousand."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Employees with a monthly salary above 8 thousand are more likely to work remotely for more than 10 days a month."""
    condition = df["monthly_salary_k"] > 8
    condition = condition & (df["remote_days_month"] > 10)
    truth = condition.all()
    if truth:
        expl = f"All {len(df[condition])} employees with a monthly salary above 8 thousand work remotely for more than 10 days a month."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} employees with a monthly salary above 8 thousand do not work remotely for more than 10 days a month (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All employees in the hr department with a performance rating above 4.0 have less than 5 years of experience."""
    hr_dept = df[df["department"] == "hr"]
    condition = hr_dept["performance_rating"] > 4.0
    condition = condition & (hr_dept["years_experience"] < 5)
    truth = condition.all()
    if truth:
        expl = f"All {len(hr_dept[condition])} employees in the hr department with a performance rating above 4.0 have less than 5 years of experience."
    else:
        viol = hr_dept[~condition]
        expl = f"{len(viol)} employees in the hr department with a performance rating above 4.0 have {', '.join(map(str, viol['years_experience'].tolist()))} years of experience which is not less than 5."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If an employee has more than 3 active projects, they are more likely to have a performance rating above 4.1."""
    condition = df["projects_active"] > 3
    condition = condition & (df["performance_rating"] > 4.1)
    truth = condition.all()
    if truth:
        expl = f"All {len(df[condition])} employees with more than 3 active projects have a performance rating above 4.1."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} employees with more than 3 active projects have a performance rating of {', '.join(map(str, viol['performance_rating'].tolist()))} which is not above 4.1."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Employees in the marketing department with a monthly salary above 5.5 thousand are more likely to have a performance rating above 4.0."""
    marketing_dept = df[df["department"] == "marketing"]
    condition = marketing_dept["monthly_salary_k"] > 5.5
    condition = condition & (marketing_dept["performance_rating"] > 4.0)
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing_dept[condition])} employees in the marketing department with a monthly salary above 5.5 thousand have a performance rating above 4.0."
    else:
        viol = marketing_dept[~condition]
        expl = f"{len(viol)} employees in the marketing department with a monthly salary above 5.5 thousand have a performance rating of {', '.join(map(str, viol['performance_rating'].tolist()))} which is not above 4.0."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_4.csv")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10), (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()