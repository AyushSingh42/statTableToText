

import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All engineering employees with over 5 years of experience have a monthly salary exceeding 8.0k."""
    eng = df[(df['department'] == 'engineering') & (df['years_experience'] > 5)]
    condition = eng['monthly_salary_k'] > 8.0
    truth = condition.all() if not eng.empty else True
    if truth:
        expl = f"All {len(eng)} engineering employees with >5 years have salary >8.0k."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Employees in finance with more than 5 years of experience have higher monthly salaries than marketing employees with similar experience."""
    finance_5 = df[(df['department'] == 'finance') & (df['years_experience'] > 5)]
    marketing_5 = df[(df['department'] =='marketing') & (df['years_experience'] > 5)]
    if finance_5.empty or marketing_5.empty:
        truth = True
        expl = "No applicable employees in one or both departments."
    else:
        min_finance = finance_5['monthly_salary_k'].min()
        max_marketing = marketing_5['monthly_salary_k'].max()
        truth = min_finance > max_marketing
        if truth:
            expl = f"Finance min salary {min_finance} > Marketing max salary {max_marketing}."
        else:
            expl = f"Finance min salary {min_finance} <= Marketing max salary {max_marketing}."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If an employee has a performance rating above 4.5, they must belong to engineering or finance departments."""
    high_perf = df[df['performance_rating'] > 4.5]
    valid = high_perf['department'].isin(['engineering', 'finance'])
    truth = valid.all() if not high_perf.empty else True
    if truth:
        expl = f"All {len(high_perf)} high-performance employees are in engineering or finance."
    else:
        viol = high_perf[~valid]
        expl = f"{len(viol)} employees violate the rule (departments: {', '.join(viol['department'].astype(str).tolist())})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Employees with 5 or more active projects have performance ratings above 4.5."""
    active_5 = df[df['projects_active'] >= 5]
    condition = active_5['performance_rating'] > 4.5
    truth = condition.all() if not active_5.empty else True
    if truth:
        expl = f"All {len(active_5)} employees with >=5 projects have performance >4.5."
    else:
        viol = active_5[~condition]
        expl = f"{len(viol)} employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All hr department employees have fewer than 10 remote days per month."""
    hr = df[df['department'] == 'hr']
    condition = hr['remote_days_month'] < 10
    truth = condition.all() if not hr.empty else True
    if truth:
        expl = f"All {len(hr)} HR employees have <10 remote days."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Marketing employees with over 3 years of experience have monthly salaries between 5.5k and 5.9k."""
    marketing_3 = df[(df['department'] =='marketing') & (df['years_experience'] > 3)]
    condition = marketing_3['monthly_salary_k'].between(5.5, 5.9, inclusive='both')
    truth = condition.all() if not marketing_3.empty else True
    if truth:
        expl = f"All {len(marketing_3)} marketing employees with >3 years have salaries between 5.5k and 5.9k."
    else:
        viol = marketing_3[~condition]
        expl = f"{len(viol)} employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Employees with performance ratings above 4.3 must have at least 4 active projects."""
    high_perf = df[df['performance_rating'] > 4.3]
    condition = high_perf['projects_active'] >= 4
    truth = condition.all() if not high_perf.empty else True
    if truth:
        expl = f"All {len(high_perf)} high-performance employees have >=4 projects."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Finance employees with over 6 years of experience have higher salaries than hr employees with similar experience."""
    finance_6 = df[(df['department'] == 'finance') & (df['years_experience'] > 6)]
    hr_6 = df[(df['department'] == 'hr') & (df['years_experience'] > 6)]
    if finance_6.empty or hr_6.empty:
        truth = True
        expl = "No applicable employees in one or both departments."
    else:
        min_finance = finance_6['monthly_salary_k'].min()
        max_hr = hr_6['monthly_salary_k'].max()
        truth = min_finance > max_hr
        if truth:
            expl = f"Finance min salary {min_finance} > HR max salary {max_hr}."
        else:
            expl = f"Finance min salary {min_finance} <= HR max salary {max_hr}."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Engineering employees with over 8 years of experience earn more than any marketing employee."""
    eng_8 = df[(df['department'] == 'engineering') & (df['years_experience'] > 8)]
    marketing_all = df[df['department'] =='marketing']
    if eng_8.empty or marketing_all.empty:
        truth = True
        expl = "No applicable employees in one or both departments."
    else:
        min_eng = eng_8['monthly_salary_k'].min()
        max_marketing = marketing_all['monthly_salary_k'].max()
        truth = min_eng > max_marketing
        if truth:
            expl = f"Engineering min salary {min_eng} > Marketing max salary {max_marketing}."
        else:
            expl = f"Engineering min salary {min_eng} <= Marketing max salary {max_marketing}."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Employees with monthly salaries above 8.0k are exclusively in engineering or finance departments."""
    high_salary = df[df['monthly_salary_k'] > 8.0]
    valid = high_salary['department'].isin(['engineering', 'finance'])
    truth = valid.all() if not high_salary.empty else True
    if truth:
        expl = f"All {len(high_salary)} high-salary employees are in engineering or finance."
    else:
        viol = high_salary[~valid]
        expl = f"{len(viol)} employees violate the rule (departments: {', '.join(viol['department'].astype(str).tolist())})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Hr employees with over 5 years of experience have higher performance ratings than those with under 3 years."""
    hr_5 = df[(df['department'] == 'hr') & (df['years_experience'] > 5)]
    hr_3 = df[(df['department'] == 'hr') & (df['years_experience'] < 3)]
    if hr_5.empty or hr_3.empty:
        truth = True
        expl = "No applicable employees in one or both groups."
    else:
        min_high = hr_5['performance_rating'].min()
        max_low = hr_3['performance_rating'].max()
        truth = min_high > max_low
        if truth:
            expl = f"HR employees with >5 years have min rating {min_high} > max rating {max_low} of those with <3 years."
        else:
            expl = f"HR employees with >5 years have min rating {min_high} <= max rating {max_low} of those with <3 years."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All employees with more than 10 remote days per month are in engineering."""
    remote_10 = df[df['remote_days_month'] > 10]
    valid = remote_10['department'] == 'engineering'
    truth = valid.all() if not remote_10.empty else True
    if truth:
        expl = f"All {len(remote_10)} employees with >10 remote days are in engineering."
    else:
        viol = remote_10[~valid]
        expl = f"{len(viol)} employees violate the rule (departments: {', '.join(viol['department'].astype(str).tolist())})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Finance employees with over 6 years of experience have higher salaries than those with under 6 years."""
    finance_high = df[(df['department'] == 'finance') & (df['years_experience'] > 6)]
    finance_low = df[(df['department'] == 'finance') & (df['years_experience'] < 6)]
    if finance_high.empty or finance_low.empty:
        truth = True
        expl = "No applicable employees in one or both groups."
    else:
        min_high = finance_high['monthly_salary_k'].min()
        max_low = finance_low['monthly_salary_k'].max()
        truth = min_high > max_low
        if truth:
            expl = f"Finance employees with >6 years have min salary {min_high} > max salary {max_low} of those with <6 years."
        else:
            expl = f"Finance employees with >6 years have min salary {min_high} <= max salary {max_low} of those with <6 years."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Employees with performance ratings above 4.4 must have at least 5 active projects."""
    high_perf = df[df['performance_rating'] > 4.4]
    condition = high_perf['projects_active'] >= 5
    truth = condition.all() if not high_perf.empty else True
    if truth:
        expl = f"All {len(high_perf)} high-performance employees have >=5 projects."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If an employee has a monthly salary above 7.0k, they must have at least 4 active projects or belong to engineering."""
    high_salary = df[df['monthly_salary_k'] > 7.0]
    condition = (high_salary['projects_active'] >= 4) | (high_salary['department'] == 'engineering')
    truth = condition.all() if not high_salary.empty else True
    if truth:
        expl = f"All {len(high_salary)} high-salary employees meet the project or department condition."
    else:
        viol = high_salary[~condition]
        expl = f"{len(viol)} employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))}, departments: {', '.join(viol['department'].astype(str).tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_4.csv")
    columns_to_convert = ['years_experience','monthly_salary_k', 'projects_active', 'performance_rating','remote_days_month']
    for col in columns_to_convert:
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
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()