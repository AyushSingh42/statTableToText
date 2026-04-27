import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the marketing department with more than 5 years of experience have a monthly salary greater than $6.1k."""
    condition = (df['department'] =='marketing') & (df['years_experience'] > 5)
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No marketing employees with >5 years experience to check."
    else:
        truth = (subset['monthly_salary_k'] > 6.1).all()
        if truth:
            expl = f"All {len(subset)} marketing employees with >5 years experience have salary >$6.1k."
        else:
            viol = subset[~(subset['monthly_salary_k'] > 6.1)]
            expl = f"{len(viol)} marketing employees with >5 years experience have salary <=$6.1k."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If an employee is in the finance department, then their monthly salary is greater than or equal to $5.9k."""
    condition = df['department'] == 'finance'
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No finance employees to check."
    else:
        truth = (subset['monthly_salary_k'] >= 5.9).all()
        if truth:
            expl = f"All {len(subset)} finance employees have salary >=$5.9k."
        else:
            viol = subset[~(subset['monthly_salary_k'] >= 5.9)]
            expl = f"{len(viol)} finance employees have salary <$5.9k."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one employee in the engineering department with a performance rating greater than 4.4."""
    condition = (df['department'] == 'engineering') & (df['performance_rating'] > 4.4)
    subset = df[condition]
    truth = not subset.empty
    if truth:
        expl = f"There is at least one engineering employee with performance rating >4.4 ({len(subset)} such employees)."
    else:
        expl = "No engineering employees with performance rating >4.4."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 8 years of experience have a monthly salary greater than $6.6k."""
    condition = df['years_experience'] > 8
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No employees with >8 years experience to check."
    else:
        truth = (subset['monthly_salary_k'] > 6.6).all()
        if truth:
            expl = f"All {len(subset)} employees with >8 years experience have salary >$6.6k."
        else:
            viol = subset[~(subset['monthly_salary_k'] > 6.6)]
            expl = f"{len(viol)} employees with >8 years experience have salary <=$6.6k."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If an employee is in the HR department, then their years of experience are less than 9 years."""
    condition = df['department'] == 'HR'
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No HR employees to check."
    else:
        truth = (subset['years_experience'] < 9).all()
        if truth:
            expl = f"All {len(subset)} HR employees have <9 years experience."
        else:
            viol = subset[~(subset['years_experience'] < 9)]
            expl = f"{len(viol)} HR employees have >=9 years experience."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most employees in the marketing department have a monthly salary greater than $6.0k."""
    condition = df['department'] =='marketing'
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No marketing employees to check."
    else:
        count_above = (subset['monthly_salary_k'] > 6.0).sum()
        total = len(subset)
        truth = count_above > total / 2
        if truth:
            expl = f"Most ({count_above}/{total}) marketing employees have salary >$6.0k."
        else:
            expl = f"Only {count_above}/{total} marketing employees have salary >$6.0k."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees with a performance rating greater than 4.5 have more than 3 projects active."""
    condition = df['performance_rating'] > 4.5
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No employees with performance rating >4.5 to check."
    else:
        truth = (subset['projects_active'] > 3).all()
        if truth:
            expl = f"All {len(subset)} employees with performance rating >4.5 have >3 projects."
        else:
            viol = subset[~(subset['projects_active'] > 3)]
            expl = f"{len(viol)} employees with performance rating >4.5 have <=3 projects."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If an employee has more than 10 remote days per month, then their monthly salary is greater than $6.0k."""
    condition = df['remote_days_month'] > 10
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No employees with >10 remote days/month to check."
    else:
        truth = (subset['monthly_salary_k'] > 6.0).all()
        if truth:
            expl = f"All {len(subset)} employees with >10 remote days/month have salary >$6.0k."
        else:
            viol = subset[~(subset['monthly_salary_k'] > 6.0)]
            expl = f"{len(viol)} employees with >10 remote days/month have salary <=$6.0k."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one employee in the finance department with a monthly salary greater than $7.8k."""
    condition = (df['department'] == 'finance') & (df['monthly_salary_k'] > 7.8)
    subset = df[condition]
    truth = not subset.empty
    if truth:
        expl = f"There is at least one finance employee with salary >$7.8k ({len(subset)} such employees)."
    else:
        expl = "No finance employees with salary >$7.8k."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with more than 4 years of experience in the marketing department have a performance rating greater than 3.7."""
    condition = (df['department'] =='marketing') & (df['years_experience'] > 4)
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No marketing employees with >4 years experience to check."
    else:
        truth = (subset['performance_rating'] > 3.7).all()
        if truth:
            expl = f"All {len(subset)} marketing employees with >4 years experience have performance rating >3.7."
        else:
            viol = subset[~(subset['performance_rating'] > 3.7)]
            expl = f"{len(viol)} marketing employees with >4 years experience have performance rating <=3.7."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If an employee is in the engineering department, then their monthly salary is greater than or equal to $6.0k."""
    condition = df['department'] == 'engineering'
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No engineering employees to check."
    else:
        truth = (subset['monthly_salary_k'] >= 6.0).all()
        if truth:
            expl = f"All {len(subset)} engineering employees have salary >=$6.0k."
        else:
            viol = subset[~(subset['monthly_salary_k'] >= 6.0)]
            expl = f"{len(viol)} engineering employees have salary <$6.0k."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most employees with more than 5 years of experience have a monthly salary greater than $6.2k."""
    condition = df['years_experience'] > 5
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No employees with >5 years experience to check."
    else:
        count_above = (subset['monthly_salary_k'] > 6.2).sum()
        total = len(subset)
        truth = count_above > total / 2
        if truth:
            expl = f"Most ({count_above}/{total}) employees with >5 years experience have salary >$6.2k."
        else:
            expl = f"Only {count_above}/{total} employees with >5 years experience have salary >$6.2k."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All employees with a monthly salary greater than $7.0k have more than 2 projects active."""
    condition = df['monthly_salary_k'] > 7.0
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No employees with salary >$7.0k to check."
    else:
        truth = (subset['projects_active'] > 2).all()
        if truth:
            expl = f"All {len(subset)} employees with salary >$7.0k have >2 projects."
        else:
            viol = subset[~(subset['projects_active'] > 2)]
            expl = f"{len(viol)} employees with salary >$7.0k have <=2 projects."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If an employee has more than 5 years of experience in the HR department, then their monthly salary is less than $6.2k."""
    condition = (df['department'] == 'HR') & (df['years_experience'] > 5)
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No HR employees with >5 years experience to check."
    else:
        truth = (subset['monthly_salary_k'] < 6.2).all()
        if truth:
            expl = f"All {len(subset)} HR employees with >5 years experience have salary <$6.2k."
        else:
            viol = subset[~(subset['monthly_salary_k'] < 6.2)]
            expl = f"{len(viol)} HR employees with >5 years experience have salary >=$6.2k."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one employee in the marketing department with a monthly salary greater than $8.6k."""
    condition = (df['department'] =='marketing') & (df['monthly_salary_k'] > 8.6)
    subset = df[condition]
    truth = not subset.empty
    if truth:
        expl = f"There is at least one marketing employee with salary >$8.6k ({len(subset)} such employees)."
    else:
        expl = "No marketing employees with salary >$8.6k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All employees with a performance rating greater than 4.8 have more than 2 projects active."""
    condition = df['performance_rating'] > 4.8
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No employees with performance rating >4.8 to check."
    else:
        truth = (subset['projects_active'] > 2).all()
        if truth:
            expl = f"All {len(subset)} employees with performance rating >4.8 have >2 projects."
        else:
            viol = subset[~(subset['projects_active'] > 2)]
            expl = f"{len(viol)} employees with performance rating >4.8 have <=2 projects."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If an employee is in the finance department with more than 8 years of experience, then their monthly salary is greater than $7.0k."""
    condition = (df['department'] == 'finance') & (df['years_experience'] > 8)
    subset = df[condition]
    if subset.empty:
        truth = True
        expl = "No finance employees with >8 years experience to check."
    else:
        truth = (subset['monthly_salary_k'] > 7.0).all()
        if truth:
            expl = f"All {len(subset)} finance employees with >8 years experience have salary >$7.0k."
        else:
            viol = subset[~(subset['monthly_salary_k'] > 7.0)]
            expl = f"{len(viol)} finance employees with >8 years experience have salary <=$7.0k."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_89.csv")

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
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()