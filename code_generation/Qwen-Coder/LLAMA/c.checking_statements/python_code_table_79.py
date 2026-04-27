import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the engineering department with more than 8 years of experience have a monthly salary greater than $8k."""
    eng_exp = df[(df["department"] == "engineering") & (df["years_experience"] > 8)]
    condition = eng_exp["monthly_salary_k"] > 8
    truth = condition.all()
    if truth:
        expl = f"All {len(eng_exp)} engineering employees with >8 years experience have salary >$8k."
    else:
        viol = eng_exp[~condition]
        expl = f"{len(viol)} engineering employees with >8 years experience have salary <=$8k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If an employee is in the finance department, then their performance rating is greater than 4.0."""
    fin = df[df["department"] == "finance"]
    condition = fin["performance_rating"] > 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(fin)} finance employees have performance rating >4.0."
    else:
        viol = fin[~condition]
        expl = f"{len(viol)} finance employees have performance rating <=4.0 ({', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one employee in the hr department with a monthly salary greater than $10k."""
    hr = df[df["department"] == "hr"]
    condition = hr["monthly_salary_k"] > 10
    truth = condition.any()
    if truth:
        expl = f"At least one HR employee has salary >$10k."
    else:
        expl = f"No HR employee has salary >$10k."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 10 years of experience have a performance rating greater than 4.0."""
    exp = df[df["years_experience"] > 10]
    condition = exp["performance_rating"] > 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >10 years experience have performance rating >4.0."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >10 years experience have performance rating <=4.0 ({', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If an employee has more than 5 active projects, then their monthly salary is greater than $7k."""
    proj = df[df["projects_active"] > 5]
    condition = proj["monthly_salary_k"] > 7
    truth = condition.all()
    if truth:
        expl = f"All {len(proj)} employees with >5 projects have salary >$7k."
    else:
        viol = proj[~condition]
        expl = f"{len(viol)} employees with >5 projects have salary <=$7k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most employees in the engineering department have a monthly salary greater than $6k."""
    eng = df[df["department"] == "engineering"]
    condition = eng["monthly_salary_k"] > 6
    count = len(eng)
    satisfied = condition.sum()
    truth = satisfied > count / 2
    if truth:
        expl = f"More than half ({satisfied}/{count}) of engineering employees have salary >$6k."
    else:
        expl = f"Less than half ({satisfied}/{count}) of engineering employees have salary >$6k."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees with a performance rating greater than 4.5 have more than 2 active projects."""
    perf = df[df["performance_rating"] > 4.5]
    condition = perf["projects_active"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(perf)} employees with performance rating >4.5 have >2 projects."
    else:
        viol = perf[~condition]
        expl = f"{len(viol)} employees with performance rating >4.5 have <=2 projects ({', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If an employee is in the marketing department, then their years of experience are less than 5."""
    mark = df[df["department"] == "marketing"]
    condition = mark["years_experience"] < 5
    truth = condition.all()
    if truth:
        expl = f"All {len(mark)} marketing employees have <5 years experience."
    else:
        viol = mark[~condition]
        expl = f"{len(viol)} marketing employees have >=5 years experience ({', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one employee in the operations department with more than 12 years of experience."""
    ops = df[df["department"] == "operations"]
    condition = ops["years_experience"] > 12
    truth = condition.any()
    if truth:
        expl = f"At least one operations employee has >12 years experience."
    else:
        expl = f"No operations employee has >12 years experience."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with a monthly salary greater than $9k have more than 3 active projects."""
    sal = df[df["monthly_salary_k"] > 9]
    condition = sal["projects_active"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(sal)} employees with salary >$9k have >3 projects."
    else:
        viol = sal[~condition]
        expl = f"{len(viol)} employees with salary >$9k have <=3 projects ({', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If an employee has more than 4 active projects, then their performance rating is greater than 4.0."""
    proj = df[df["projects_active"] > 4]
    condition = proj["performance_rating"] > 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(proj)} employees with >4 projects have performance rating >4.0."
    else:
        viol = proj[~condition]
        expl = f"{len(viol)} employees with >4 projects have performance rating <=4.0 ({', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most employees in the finance department have a monthly salary less than $8k."""
    fin = df[df["department"] == "finance"]
    condition = fin["monthly_salary_k"] < 8
    count = len(fin)
    satisfied = condition.sum()
    truth = satisfied > count / 2
    if truth:
        expl = f"More than half ({satisfied}/{count}) of finance employees have salary <$8k."
    else:
        expl = f"Less than half ({satisfied}/{count}) of finance employees have salary <$8k."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All employees with more than 6 years of experience have a performance rating greater than 4.0."""
    exp = df[df["years_experience"] > 6]
    condition = exp["performance_rating"] > 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >6 years experience have performance rating >4.0."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >6 years experience have performance rating <=4.0 ({', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If an employee is in the hr department, then their monthly salary is less than $8k."""
    hr = df[df["department"] == "hr"]
    condition = hr["monthly_salary_k"] < 8
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have salary <$8k."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees have salary >=$8k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one employee in the engineering department with a monthly salary less than $7k."""
    eng = df[df["department"] == "engineering"]
    condition = eng["monthly_salary_k"] < 7
    truth = condition.any()
    if truth:
        expl = f"At least one engineering employee has salary <$7k."
    else:
        expl = f"No engineering employee has salary <$7k."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All employees with a performance rating greater than 4.2 have more than 3 active projects."""
    perf = df[df["performance_rating"] > 4.2]
    condition = perf["projects_active"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(perf)} employees with performance rating >4.2 have >3 projects."
    else:
        viol = perf[~condition]
        expl = f"{len(viol)} employees with performance rating >4.2 have <=3 projects ({', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If an employee has more than 10 years of experience, then their monthly salary is greater than $7k."""
    exp = df[df["years_experience"] > 10]
    condition = exp["monthly_salary_k"] > 7
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >10 years experience have salary >$7k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >10 years experience have salary <=$7k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most employees in the engineering department have more than 3 active projects."""
    eng = df[df["department"] == "engineering"]
    condition = eng["projects_active"] > 3
    count = len(eng)
    satisfied = condition.sum()
    truth = satisfied > count / 2
    if truth:
        expl = f"More than half ({satisfied}/{count}) of engineering employees have >3 projects."
    else:
        expl = f"Less than half ({satisfied}/{count}) of engineering employees have >3 projects."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All employees with a monthly salary greater than $8k have more than 4 active projects."""
    sal = df[df["monthly_salary_k"] > 8]
    condition = sal["projects_active"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(sal)} employees with salary >$8k have >4 projects."
    else:
        viol = sal[~condition]
        expl = f"{len(viol)} employees with salary >$8k have <=4 projects ({', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If an employee is in the finance department, then their years of experience are greater than 5."""
    fin = df[df["department"] == "finance"]
    condition = fin["years_experience"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(fin)} finance employees have >5 years experience."
    else:
        viol = fin[~condition]
        expl = f"{len(viol)} finance employees have <=5 years experience ({', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one employee in the hr department with more than 5 active projects."""
    hr = df[df["department"] == "hr"]
    condition = hr["projects_active"] > 5
    truth = condition.any()
    if truth:
        expl = f"At least one HR employee has >5 projects."
    else:
        expl = f"No HR employee has >5 projects."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. All employees with more than 5 years of experience have a performance rating greater than 4.0."""
    exp = df[df["years_experience"] > 5]
    condition = exp["performance_rating"] > 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >5 years experience have performance rating >4.0."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >5 years experience have performance rating <=4.0 ({', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_23(df: pd.DataFrame):
    """23. If an employee has more than 3 active projects, then their monthly salary is greater than $6k."""
    proj = df[df["projects_active"] > 3]
    condition = proj["monthly_salary_k"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(proj)} employees with >3 projects have salary >$6k."
    else:
        viol = proj[~condition]
        expl = f"{len(viol)} employees with >3 projects have salary <=$6k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_24(df: pd.DataFrame):
    """24. Most employees in the finance department have more than 2 active projects."""
    fin = df[df["department"] == "finance"]
    condition = fin["projects_active"] > 2
    count = len(fin)
    satisfied = condition.sum()
    truth = satisfied > count / 2
    if truth:
        expl = f"More than half ({satisfied}/{count}) of finance employees have >2 projects."
    else:
        expl = f"Less than half ({satisfied}/{count}) of finance employees have >2 projects."
    return truth, expl

def stmt_25(df: pd.DataFrame):
    """25. All employees with a performance rating greater than 4.5 have more than 4 active projects."""
    perf = df[df["performance_rating"] > 4.5]
    condition = perf["projects_active"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(perf)} employees with performance rating >4.5 have >4 projects."
    else:
        viol = perf[~condition]
        expl = f"{len(viol)} employees with performance rating >4.5 have <=4 projects ({', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_26(df: pd.DataFrame):
    """26. If an employee is in the engineering department, then their monthly salary is greater than $6k."""
    eng = df[df["department"] == "engineering"]
    condition = eng["monthly_salary_k"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have salary >$6k."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} engineering employees have salary <=$6k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_27(df: pd.DataFrame):
    """27. There exists at least one employee in the operations department with a monthly salary greater than $7k."""
    ops = df[df["department"] == "operations"]
    condition = ops["monthly_salary_k"] > 7
    truth = condition.any()
    if truth:
        expl = f"At least one operations employee has salary >$7k."
    else:
        expl = f"No operations employee has salary >$7k."
    return truth, expl

def stmt_28(df: pd.DataFrame):
    """28. All employees with more than 8 years of experience have a performance rating greater than 4.2."""
    exp = df[df["years_experience"] > 8]
    condition = exp["performance_rating"] > 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >8 years experience have performance rating >4.2."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >8 years experience have performance rating <=4.2 ({', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_29(df: pd.DataFrame):
    """29. If an employee has more than 4 active projects, then their monthly salary is greater than $7k."""
    proj = df[df["projects_active"] > 4]
    condition = proj["monthly_salary_k"] > 7
    truth = condition.all()
    if truth:
        expl = f"All {len(proj)} employees with >4 projects have salary >$7k."
    else:
        viol = proj[~condition]
        expl = f"{len(viol)} employees with >4 projects have salary <=$7k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_30(df: pd.DataFrame):
    """30. Most employees in the hr department have a monthly salary less than $8k."""
    hr = df[df["department"] == "hr"]
    condition = hr["monthly_salary_k"] < 8
    count = len(hr)
    satisfied = condition.sum()
    truth = satisfied > count / 2
    if truth:
        expl = f"More than half ({satisfied}/{count}) of HR employees have salary <$8k."
    else:
        expl = f"Less than half ({satisfied}/{count}) of HR employees have salary <$8k."
    return truth, expl

def stmt_31(df: pd.DataFrame):
    """31. All employees with a monthly salary greater than $9k have more than 5 active projects."""
    sal = df[df["monthly_salary_k"] > 9]
    condition = sal["projects_active"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(sal)} employees with salary >$9k have >5 projects."
    else:
        viol = sal[~condition]
        expl = f"{len(viol)} employees with salary >$9k have <=5 projects ({', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_32(df: pd.DataFrame):
    """32. If an employee is in the marketing department, then their monthly salary is greater than $9k."""
    mark = df[df["department"] == "marketing"]
    condition = mark["monthly_salary_k"] > 9
    truth = condition.all()
    if truth:
        expl = f"All {len(mark)} marketing employees have salary >$9k."
    else:
        viol = mark[~condition]
        expl = f"{len(viol)} marketing employees have salary <=$9k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_33(df: pd.DataFrame):
    """33. There exists at least one employee in the engineering department with more than 10 years of experience."""
    eng = df[df["department"] == "engineering"]
    condition = eng["years_experience"] > 10
    truth = condition.any()
    if truth:
        expl = f"At least one engineering employee has >10 years experience."
    else:
        expl = f"No engineering employee has >10 years experience."
    return truth, expl

def stmt_34(df: pd.DataFrame):
    """34. All employees with more than 6 years of experience have a monthly salary greater than $6k."""
    exp = df[df["years_experience"] > 6]
    condition = exp["monthly_salary_k"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >6 years experience have salary >$6k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >6 years experience have salary <=$6k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_35(df: pd.DataFrame):
    """35. If an employee has more than 5 active projects, then their performance rating is greater than 4.2."""
    proj = df[df["projects_active"] > 5]
    condition = proj["performance_rating"] > 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(proj)} employees with >5 projects have performance rating >4.2."
    else:
        viol = proj[~condition]
        expl = f"{len(viol)} employees with >5 projects have performance rating <=4.2 ({', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_36(df: pd.DataFrame):
    """36. Most employees in the finance department have a performance rating greater than 4.0."""
    fin = df[df["department"] == "finance"]
    condition = fin["performance_rating"] > 4.0
    count = len(fin)
    satisfied = condition.sum()
    truth = satisfied > count / 2
    if truth:
        expl = f"More than half ({satisfied}/{count}) of finance employees have performance rating >4.0."
    else:
        expl = f"Less than half ({satisfied}/{count}) of finance employees have performance rating >4.0."
    return truth, expl

def stmt_37(df: pd.DataFrame):
    """37. All employees with a performance rating greater than 4.5 have more than 5 active projects."""
    perf = df[df["performance_rating"] > 4.5]
    condition = perf["projects_active"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(perf)} employees with performance rating >4.5 have >5 projects."
    else:
        viol = perf[~condition]
        expl = f"{len(viol)} employees with performance rating >4.5 have <=5 projects ({', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_38(df: pd.DataFrame):
    """38. If an employee is in the hr department, then their years of experience are greater than 5."""
    hr = df[df["department"] == "hr"]
    condition = hr["years_experience"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have >5 years experience."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees have <=5 years experience ({', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_39(df: pd.DataFrame):
    """39. There exists at least one employee in the operations department with a performance rating greater than 4.5."""
    ops = df[df["department"] == "operations"]
    condition = ops["performance_rating"] > 4.5
    truth = condition.any()
    if truth:
        expl = f"At least one operations employee has performance rating >4.5."
    else:
        expl = f"No operations employee has performance rating >4.5."
    return truth, expl

def stmt_40(df: pd.DataFrame):
    """40. All employees with more than 10 years of experience have a monthly salary greater than $8k."""
    exp = df[df["years_experience"] > 10]
    condition = exp["monthly_salary_k"] > 8
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >10 years experience have salary >$8k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >10 years experience have salary <=$8k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_41(df: pd.DataFrame):
    """41. If an employee has more than 3 active projects, then their performance rating is greater than 4.0."""
    proj = df[df["projects_active"] > 3]
    condition = proj["performance_rating"] > 4.0
    truth = condition.all()
    if truth:
        expl = f"All {len(proj)} employees with >3 projects have performance rating >4.0."
    else:
        viol = proj[~condition]
        expl = f"{len(viol)} employees with >3 projects have performance rating <=4.0 ({', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_42(df: pd.DataFrame):
    """42. Most employees in the engineering department have a performance rating greater than 4.0."""
    eng = df[df["department"] == "engineering"]
    condition = eng["performance_rating"] > 4.0
    count = len(eng)
    satisfied = condition.sum()
    truth = satisfied > count / 2
    if truth:
        expl = f"More than half ({satisfied}/{count}) of engineering employees have performance rating >4.0."
    else:
        expl = f"Less than half ({satisfied}/{count}) of engineering employees have performance rating >4.0."
    return truth, expl

def stmt_43(df: pd.DataFrame):
    """43. All employees with a monthly salary greater than $8k have more than 6 active projects."""
    sal = df[df["monthly_salary_k"] > 8]
    condition = sal["projects_active"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(sal)} employees with salary >$8k have >6 projects."
    else:
        viol = sal[~condition]
        expl = f"{len(viol)} employees with salary >$8k have <=6 projects ({', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_44(df: pd.DataFrame):
    """44. If an employee is in the finance department, then their monthly salary is less than $9k."""
    fin = df[df["department"] == "finance"]
    condition = fin["monthly_salary_k"] < 9
    truth = condition.all()
    if truth:
        expl = f"All {len(fin)} finance employees have salary <$9k."
    else:
        viol = fin[~condition]
        expl = f"{len(viol)} finance employees have salary >=$9k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_45(df: pd.DataFrame):
    """45. There exists at least one employee in the hr department with a performance rating greater than 4.5."""
    hr = df[df["department"] == "hr"]
    condition = hr["performance_rating"] > 4.5
    truth = condition.any()
    if truth:
        expl = f"At least one HR employee has performance rating >4.5."
    else:
        expl = f"No HR employee has performance rating >4.5."
    return truth, expl

def stmt_46(df: pd.DataFrame):
    """46. All employees with more than 5 years of experience have a monthly salary greater than $6k."""
    exp = df[df["years_experience"] > 5]
    condition = exp["monthly_salary_k"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >5 years experience have salary >$6k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >5 years experience have salary <=$6k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_47(df: pd.DataFrame):
    """47. If an employee has more than 4 active projects, then their monthly salary is greater than $8k."""
    proj = df[df["projects_active"] > 4]
    condition = proj["monthly_salary_k"] > 8
    truth = condition.all()
    if truth:
        expl = f"All {len(proj)} employees with >4 projects have salary >$8k."
    else:
        viol = proj[~condition]
        expl = f"{len(viol)} employees with >4 projects have salary <=$8k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_48(df: pd.DataFrame):
    """48. Most employees in the finance department have a monthly salary less than $9k."""
    fin = df[df["department"] == "finance"]
    condition = fin["monthly_salary_k"] < 9
    count = len(fin)
    satisfied = condition.sum()
    truth = satisfied > count / 2
    if truth:
        expl = f"More than half ({satisfied}/{count}) of finance employees have salary <$9k."
    else:
        expl = f"Less than half ({satisfied}/{count}) of finance employees have salary <$9k."
    return truth, expl

def stmt_49(df: pd.DataFrame):
    """49. All employees with a performance rating greater than 4.2 have more than 6 active projects."""
    perf = df[df["performance_rating"] > 4.2]
    condition = perf["projects_active"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(perf)} employees with performance rating >4.2 have >6 projects."
    else:
        viol = perf[~condition]
        expl = f"{len(viol)} employees with performance rating >4.2 have <=6 projects ({', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_50(df: pd.DataFrame):
    """50. If an employee is in the engineering department, then their years of experience are greater than 3."""
    eng = df[df["department"] == "engineering"]
    condition = eng["years_experience"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have >3 years experience."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} engineering employees have <=3 years experience ({', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_51(df: pd.DataFrame):
    """51. There exists at least one employee in the operations department with more than 5 active projects."""
    ops = df[df["department"] == "operations"]
    condition = ops["projects_active"] > 5
    truth = condition.any()
    if truth:
        expl = f"At least one operations employee has >5 projects."
    else:
        expl = f"No operations employee has >5 projects."
    return truth, expl

def stmt_52(df: pd.DataFrame):
    """52. All employees with more than 8 years of experience have a monthly salary greater than $9k."""
    exp = df[df["years_experience"] > 8]
    condition = exp["monthly_salary_k"] > 9
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >8 years experience have salary >$9k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >8 years experience have salary <=$9k ({', '.join(map(str, viol['monthly_salary_k'].tolist()))}k)."
    return truth, expl

def stmt_53(df: pd.DataFrame):
    """53. If an employee has more than 5 active projects, then their performance rating is greater than 4.5."""
    proj = df[df["projects_active"] > 5]
    condition = proj["performance_rating"] > 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(proj)} employees with >5 projects have performance rating >4.5."
    else:
        viol = proj[~condition]
        expl = f"{len(viol)} employees with >5 projects have performance rating <=4.5 ({', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_54(df: pd.DataFrame):
    """54. Most employees in the hr department have a performance rating greater than 4.0."""
    hr = df[df["department"] == "hr"]
    condition = hr["performance_rating"] > 4.0
    count = len(hr)
    satisfied = condition.sum()
    truth = satisfied > count / 2
    if truth:
        expl = f"More than half ({satisfied}/{count}) of HR employees have performance rating >4.0."
    else:
        expl = f"Less than half ({satisfied}/{count}) of HR employees have performance rating >4.0."
    return truth, expl

def stmt_55(df: pd.DataFrame):
    """55. All employees with a monthly salary greater than $9k have more than 7 active projects."""
    sal = df[df["monthly_salary_k"] > 9]
    condition = sal["projects_active"] > 7
    truth = condition.all()
    if truth:
        expl = f"All {len(sal)} employees with salary >$9k have >7 projects."
    else:
        viol = sal[~condition]
        expl = f"{len(viol)} employees with salary >$9k have <=7 projects ({', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_56(df: pd.DataFrame):
    """56. If an employee is in the marketing department, then their years of experience are less than 4."""
    mark = df[df["department"] == "marketing"]
    condition = mark["years_experience"] < 4
    truth = condition.all()
    if truth:
        expl = f"All {len(mark)} marketing employees have <4 years experience."
    else:
        viol = mark[~condition]
        expl = f"{len(viol)} marketing employees have >=4 years experience ({', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_57(df: pd.DataFrame):
    """57. There exists at least one employee in the engineering department with a performance rating greater than 4.5."""
    eng = df[df["department"] == "engineering"]
    condition = eng["performance_rating"] > 4.5
    truth = condition.any()
    if truth:
        expl = f"At least one engineering employee has performance rating >4.5."
    else:
        expl = f"No engineering employee has performance rating >4.5."
    return truth, expl

def stmt_58(df: pd.DataFrame):
    """58.