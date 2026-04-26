import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the operations department with more than 5 years of experience have a monthly salary greater than $6.2k."""
    ops_df = df[(df['department'] == 'operations') & (df['years_experience'] > 5)]
    condition = ops_df['monthly_salary_k'] > 6.2
    truth = condition.all()
    if truth:
        expl = f"All {len(ops_df)} operations employees with >5 years experience have salary >$6.2k."
    else:
        viol = ops_df[~condition]
        expl = f"{len(viol)} operations employees with >5 years experience have salary <=$6.2k."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If an employee is in the engineering department, then their monthly salary is greater than $6.4k."""
    eng_df = df[df['department'] == 'engineering']
    condition = eng_df['monthly_salary_k'] > 6.4
    truth = condition.all()
    if truth:
        expl = f"All {len(eng_df)} engineering employees have salary >$6.4k."
    else:
        viol = eng_df[~condition]
        expl = f"{len(viol)} engineering employees have salary <=$6.4k."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one employee in the operations department with a performance rating greater than 4.7."""
    ops_df = df[(df['department'] == 'operations') & (df['performance_rating'] > 4.7)]
    truth = len(ops_df) > 0
    if truth:
        expl = f"There are {len(ops_df)} operations employees with performance rating >4.7."
    else:
        expl = "No operations employees have performance rating >4.7."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 10 years of experience have a monthly salary less than or equal to $10.7k."""
    exp_df = df[df['years_experience'] > 10]
    condition = exp_df['monthly_salary_k'] <= 10.7
    truth = condition.all()
    if truth:
        expl = f"All {len(exp_df)} employees with >10 years experience have salary <=$10.7k."
    else:
        viol = exp_df[~condition]
        expl = f"{len(viol)} employees with >10 years experience have salary >$10.7k."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If an employee is in the finance department, then their years of experience are less than 8 years."""
    fin_df = df[df['department'] == 'finance']
    condition = fin_df['years_experience'] < 8
    truth = condition.all()
    if truth:
        expl = f"All {len(fin_df)} finance employees have <8 years experience."
    else:
        viol = fin_df[~condition]
        expl = f"{len(viol)} finance employees have >=8 years experience."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All employees with a monthly salary greater than $10k have a performance rating greater than 4.0."""
    sal_df = df[df['monthly_salary_k'] > 10.0]
    condition = sal_df['performance_rating'] > 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(sal_df)} employees with salary >$10k have performance rating >4.0."
    else:
        viol = sal_df[~condition]
        expl = f"{len(viol)} employees with salary >$10k have performance rating <=4.0."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most employees in the operations department have a monthly salary less than $10k."""
    ops_df = df[df['department'] == 'operations']
    low_sal = ops_df[ops_df['monthly_salary_k'] < 10.0]
    truth = len(low_sal) > len(ops_df) / 2
    if truth:
        expl = f"More than half ({len(low_sal)}/{len(ops_df)}) of operations employees have salary <$10k."
    else:
        expl = f"Less than half ({len(low_sal)}/{len(ops_df)}) of operations employees have salary <$10k."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If an employee has more than 5 projects active, then their monthly salary is less than $10.2k."""
    proj_df = df[df['projects_active'] > 5]
    condition = proj_df['monthly_salary_k'] < 10.2
    truth = condition.all()
    if truth:
        expl = f"All {len(proj_df)} employees with >5 projects have salary <$10.2k."
    else:
        viol = proj_df[~condition]
        expl = f"{len(viol)} employees with >5 projects have salary >=$10.2k."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one employee in the engineering department with a monthly salary less than $8.2k."""
    eng_df = df[(df['department'] == 'engineering') & (df['monthly_salary_k'] < 8.2)]
    truth = len(eng_df) > 0
    if truth:
        expl = f"There are {len(eng_df)} engineering employees with salary <$8.2k."
    else:
        expl = "No engineering employees have salary <$8.2k."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with a performance rating greater than 4.6 have a monthly salary greater than $6.7k."""
    perf_df = df[df['performance_rating'] > 4.6]
    condition = perf_df['monthly_salary_k'] > 6.7
    truth = condition.all()
    if truth:
        expl = f"All {len(perf_df)} employees with performance rating >4.6 have salary >$6.7k."
    else:
        viol = perf_df[~condition]
        expl = f"{len(viol)} employees with performance rating >4.6 have salary <=$6.7k."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If an employee is in the hr department, then their monthly salary is greater than $6.7k."""
    hr_df = df[df['department'] == 'hr']
    condition = hr_df['monthly_salary_k'] > 6.7
    truth = condition.all()
    if truth:
        expl = f"All {len(hr_df)} hr employees have salary >$6.7k."
    else:
        viol = hr_df[~condition]
        expl = f"{len(viol)} hr employees have salary <=$6.7k."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All employees with more than 4 remote days per month have a monthly salary less than $10.7k."""
    rem_df = df[df['remote_days_month'] > 4]
    condition = rem_df['monthly_salary_k'] < 10.7
    truth = condition.all()
    if truth:
        expl = f"All {len(rem_df)} employees with >4 remote days have salary <$10.7k."
    else:
        viol = rem_df[~condition]
        expl = f"{len(viol)} employees with >4 remote days have salary >=$10.7k."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most employees in the engineering department have a monthly salary greater than $7.5k."""
    eng_df = df[df['department'] == 'engineering']
    high_sal = eng_df[eng_df['monthly_salary_k'] > 7.5]
    truth = len(high_sal) > len(eng_df) / 2
    if truth:
        expl = f"More than half ({len(high_sal)}/{len(eng_df)}) of engineering employees have salary >$7.5k."
    else:
        expl = f"Less than half ({len(high_sal)}/{len(eng_df)}) of engineering employees have salary >$7.5k."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If an employee has more than 3 years of experience, then their monthly salary is greater than $5.9k."""
    exp_df = df[df['years_experience'] > 3]
    condition = exp_df['monthly_salary_k'] > 5.9
    truth = condition.all()
    if truth:
        expl = f"All {len(exp_df)} employees with >3 years experience have salary >$5.9k."
    else:
        viol = exp_df[~condition]
        expl = f"{len(viol)} employees with >3 years experience have salary <=$5.9k."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one employee in the finance department with a monthly salary greater than $10.1k."""
    fin_df = df[(df['department'] == 'finance') & (df['monthly_salary_k'] > 10.1)]
    truth = len(fin_df) > 0
    if truth:
        expl = f"There are {len(fin_df)} finance employees with salary >$10.1k."
    else:
        expl = "No finance employees have salary >$10.1k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All employees with a monthly salary less than $6k have a performance rating less than 4.7."""
    sal_df = df[df['monthly_salary_k'] < 6.0]
    condition = sal_df['performance_rating'] < 4.7
    truth = condition.all()
    if truth:
        expl = f"All {len(sal_df)} employees with salary <$6k have performance rating <4.7."
    else:
        viol = sal_df[~condition]
        expl = f"{len(viol)} employees with salary <$6k have performance rating >=4.7."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If an employee is in the operations department, then their years of experience are less than 12 years."""
    ops_df = df[df['department'] == 'operations']
    condition = ops_df['years_experience'] < 12
    truth = condition.all()
    if truth:
        expl = f"All {len(ops_df)} operations employees have <12 years experience."
    else:
        viol = ops_df[~condition]
        expl = f"{len(viol)} operations employees have >=12 years experience."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All employees with a performance rating greater than 4.4 have a monthly salary greater than $5.5k."""
    perf_df = df[df['performance_rating'] > 4.4]
    condition = perf_df['monthly_salary_k'] > 5.5
    truth = condition.all()
    if truth:
        expl = f"All {len(perf_df)} employees with performance rating >4.4 have salary >$5.5k."
    else:
        viol = perf_df[~condition]
        expl = f"{len(viol)} employees with performance rating >4.4 have salary <=$5.5k."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_19.csv")

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
        (17, stmt_17),
        (18, stmt_18)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()