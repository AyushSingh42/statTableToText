import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All employees in the marketing department have a monthly salary less than or equal to $10.3k."""
    marketing = df[df["department"] == "marketing"]
    condition = marketing["monthly_salary_k"] <= 10.3
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees have salary <= 10.3k."
    else:
        viol = marketing[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If an employee is in the engineering department, then their years of experience are less than or equal to 11.3 years."""
    eng = df[df["department"] == "engineering"]
    condition = eng["years_experience"] <= 11.3
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have experience <= 11.3 years."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one employee in the finance department whose performance rating is less than 4.0."""
    finance = df[df["department"] == "finance"]
    condition = finance["performance_rating"] < 4.0
    truth = condition.any()
    if truth:
        expl = f"At least one finance employee has performance rating < 4.0."
    else:
        expl = f"No finance employee has performance rating < 4.0."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All employees with more than 10 years of experience have a monthly salary greater than or equal to $8.6k."""
    exp = df[df["years_experience"] > 10]
    condition = exp["monthly_salary_k"] >= 8.6
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >10 years experience have salary >= 8.6k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >10 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If an employee is in the hr department, then their monthly salary is less than or equal to $9.0k."""
    hr = df[df["department"] == "hr"]
    condition = hr["monthly_salary_k"] <= 9.0
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have salary <= 9.0k."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most employees in the table have a performance rating greater than 4.0."""
    condition = df["performance_rating"] > 4.0
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} employees have performance rating > 4.0."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All employees with a monthly salary greater than $9.4k have a performance rating greater than 3.8."""
    high_sal = df[df["monthly_salary_k"] > 9.4]
    condition = high_sal["performance_rating"] > 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sal)} employees with salary > 9.4k have performance rating > 3.8."
    else:
        viol = high_sal[~condition]
        expl = f"{len(viol)} employees with salary > 9.4k violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If an employee is in the operations department, then their years of experience are greater than or equal to 9.4 years."""
    ops = df[df["department"] == "operations"]
    condition = ops["years_experience"] >= 9.4
    truth = condition.all()
    if truth:
        expl = f"All {len(ops)} operations employees have experience >= 9.4 years."
    else:
        viol = ops[~condition]
        expl = f"{len(viol)} operations employees violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one employee in the engineering department whose remote days per month are greater than or equal to 12 days."""
    eng = df[df["department"] == "engineering"]
    condition = eng["remote_days_month"] >= 12
    truth = condition.any()
    if truth:
        expl = f"At least one engineering employee has remote days >= 12."
    else:
        expl = f"No engineering employee has remote days >= 12."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All employees with a monthly salary less than or equal to $6.3k have a performance rating greater than or equal to 4.5."""
    low_sal = df[df["monthly_salary_k"] <= 6.3]
    condition = low_sal["performance_rating"] >= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sal)} employees with salary <= 6.3k have performance rating >= 4.5."
    else:
        viol = low_sal[~condition]
        expl = f"{len(viol)} employees with salary <= 6.3k violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If an employee is in the marketing department, then their projects active are less than or equal to 6 projects."""
    marketing = df[df["department"] == "marketing"]
    condition = marketing["projects_active"] <= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees have projects active <= 6."
    else:
        viol = marketing[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most employees in the table have a monthly salary less than or equal to $9.9k."""
    condition = df["monthly_salary_k"] <= 9.9
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} employees have salary <= 9.9k."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All employees with more than 5 years of experience have a monthly salary greater than or equal to $6.2k."""
    exp = df[df["years_experience"] > 5]
    condition = exp["monthly_salary_k"] >= 6.2
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >5 years experience have salary >= 6.2k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >5 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If an employee is in the finance department, then their years of experience are greater than or equal to 9.3 years."""
    finance = df[df["department"] == "finance"]
    condition = finance["years_experience"] >= 9.3
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have experience >= 9.3 years."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one employee in the hr department whose years of experience are greater than or equal to 10.9 years."""
    hr = df[df["department"] == "hr"]
    condition = hr["years_experience"] >= 10.9
    truth = condition.any()
    if truth:
        expl = f"At least one HR employee has experience >= 10.9 years."
    else:
        expl = f"No HR employee has experience >= 10.9 years."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All employees with a performance rating greater than 4.2 have a monthly salary greater than or equal to $7.7k."""
    high_perf = df[df["performance_rating"] > 4.2]
    condition = high_perf["monthly_salary_k"] >= 7.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf)} employees with performance rating > 4.2 have salary >= 7.7k."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees with performance rating > 4.2 violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If an employee is in the engineering department, then their monthly salary is greater than or equal to $6.3k."""
    eng = df[df["department"] == "engineering"]
    condition = eng["monthly_salary_k"] >= 6.3
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have salary >= 6.3k."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most employees in the table have a monthly salary greater than or equal to $6.2k."""
    condition = df["monthly_salary_k"] >= 6.2
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} employees have salary >= 6.2k."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All employees with a monthly salary less than or equal to $8.2k have a performance rating greater than or equal to 4.4."""
    low_sal = df[df["monthly_salary_k"] <= 8.2]
    condition = low_sal["performance_rating"] >= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sal)} employees with salary <= 8.2k have performance rating >= 4.4."
    else:
        viol = low_sal[~condition]
        expl = f"{len(viol)} employees with salary <= 8.2k violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If an employee is in the marketing department, then their years of experience are less than or equal to 12.5 years."""
    marketing = df[df["department"] == "marketing"]
    condition = marketing["years_experience"] <= 12.5
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees have experience <= 12.5 years."
    else:
        viol = marketing[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one employee in the finance department whose remote days per month are greater than or equal to 11 days."""
    finance = df[df["department"] == "finance"]
    condition = finance["remote_days_month"] >= 11
    truth = condition.any()
    if truth:
        expl = f"At least one finance employee has remote days >= 11."
    else:
        expl = f"No finance employee has remote days >= 11."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. All employees with more than 4 years of experience have a monthly salary greater than or equal to $5.3k."""
    exp = df[df["years_experience"] > 4]
    condition = exp["monthly_salary_k"] >= 5.3
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >4 years experience have salary >= 5.3k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >4 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_23(df: pd.DataFrame):
    """23. If an employee is in the operations department, then their monthly salary is greater than or equal to $5.3k."""
    ops = df[df["department"] == "operations"]
    condition = ops["monthly_salary_k"] >= 5.3
    truth = condition.all()
    if truth:
        expl = f"All {len(ops)} operations employees have salary >= 5.3k."
    else:
        viol = ops[~condition]
        expl = f"{len(viol)} operations employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_24(df: pd.DataFrame):
    """24. Most employees in the table have a monthly salary less than or equal to $8.9k."""
    condition = df["monthly_salary_k"] <= 8.9
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} employees have salary <= 8.9k."
    return truth, expl

def stmt_25(df: pd.DataFrame):
    """25. All employees with a performance rating greater than 3.9 have a monthly salary greater than or equal to $6.9k."""
    high_perf = df[df["performance_rating"] > 3.9]
    condition = high_perf["monthly_salary_k"] >= 6.9
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf)} employees with performance rating > 3.9 have salary >= 6.9k."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees with performance rating > 3.9 violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_26(df: pd.DataFrame):
    """26. If an employee is in the hr department, then their projects active are less than or equal to 2 projects."""
    hr = df[df["department"] == "hr"]
    condition = hr["projects_active"] <= 2
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have projects active <= 2."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_27(df: pd.DataFrame):
    """27. There exists at least one employee in the engineering department whose years of experience are less than or equal to 1.0 year."""
    eng = df[df["department"] == "engineering"]
    condition = eng["years_experience"] <= 1.0
    truth = condition.any()
    if truth:
        expl = f"At least one engineering employee has experience <= 1.0 year."
    else:
        expl = f"No engineering employee has experience <= 1.0 year."
    return truth, expl

def stmt_28(df: pd.DataFrame):
    """28. All employees with a monthly salary less than or equal to $7.7k have a performance rating greater than or equal to 4.4."""
    low_sal = df[df["monthly_salary_k"] <= 7.7]
    condition = low_sal["performance_rating"] >= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sal)} employees with salary <= 7.7k have performance rating >= 4.4."
    else:
        viol = low_sal[~condition]
        expl = f"{len(viol)} employees with salary <= 7.7k violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_29(df: pd.DataFrame):
    """29. If an employee is in the marketing department, then their monthly salary is greater than or equal to $5.3k."""
    marketing = df[df["department"] == "marketing"]
    condition = marketing["monthly_salary_k"] >= 5.3
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees have salary >= 5.3k."
    else:
        viol = marketing[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_30(df: pd.DataFrame):
    """30. Most employees in the table have a monthly salary greater than or equal to $5.3k."""
    condition = df["monthly_salary_k"] >= 5.3
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} employees have salary >= 5.3k."
    return truth, expl

def stmt_31(df: pd.DataFrame):
    """31. All employees with more than 1 year of experience have a monthly salary greater than or equal to $5.3k."""
    exp = df[df["years_experience"] > 1]
    condition = exp["monthly_salary_k"] >= 5.3
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >1 year experience have salary >= 5.3k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >1 year experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_32(df: pd.DataFrame):
    """32. If an employee is in the finance department, then their projects active are less than or equal to 4 projects."""
    finance = df[df["department"] == "finance"]
    condition = finance["projects_active"] <= 4
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have projects active <= 4."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_33(df: pd.DataFrame):
    """33. There exists at least one employee in the hr department whose monthly salary is less than or equal to $5.3k."""
    hr = df[df["department"] == "hr"]
    condition = hr["monthly_salary_k"] <= 5.3
    truth = condition.any()
    if truth:
        expl = f"At least one HR employee has salary <= 5.3k."
    else:
        expl = f"No HR employee has salary <= 5.3k."
    return truth, expl

def stmt_34(df: pd.DataFrame):
    """34. All employees with a performance rating greater than 4.1 have a monthly salary greater than or equal to $6.2k."""
    high_perf = df[df["performance_rating"] > 4.1]
    condition = high_perf["monthly_salary_k"] >= 6.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf)} employees with performance rating > 4.1 have salary >= 6.2k."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees with performance rating > 4.1 violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_35(df: pd.DataFrame):
    """35. If an employee is in the operations department, then their performance rating is greater than or equal to 4.1."""
    ops = df[df["department"] == "operations"]
    condition = ops["performance_rating"] >= 4.1
    truth = condition.all()
    if truth:
        expl = f"All {len(ops)} operations employees have performance rating >= 4.1."
    else:
        viol = ops[~condition]
        expl = f"{len(viol)} operations employees violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_36(df: pd.DataFrame):
    """36. Most employees in the table have a monthly salary less than or equal to $6.9k."""
    condition = df["monthly_salary_k"] <= 6.9
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} employees have salary <= 6.9k."
    return truth, expl

def stmt_37(df: pd.DataFrame):
    """37. All employees with a monthly salary less than or equal to $6.2k have a performance rating greater than or equal to 4.5."""
    low_sal = df[df["monthly_salary_k"] <= 6.2]
    condition = low_sal["performance_rating"] >= 4.5
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sal)} employees with salary <= 6.2k have performance rating >= 4.5."
    else:
        viol = low_sal[~condition]
        expl = f"{len(viol)} employees with salary <= 6.2k violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_38(df: pd.DataFrame):
    """38. If an employee is in the marketing department, then their remote days per month are less than or equal to 13 days."""
    marketing = df[df["department"] == "marketing"]
    condition = marketing["remote_days_month"] <= 13
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees have remote days <= 13."
    else:
        viol = marketing[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_39(df: pd.DataFrame):
    """39. There exists at least one employee in the finance department whose years of experience are less than or equal to 10.0 years."""
    finance = df[df["department"] == "finance"]
    condition = finance["years_experience"] <= 10.0
    truth = condition.any()
    if truth:
        expl = f"At least one finance employee has experience <= 10.0 years."
    else:
        expl = f"No finance employee has experience <= 10.0 years."
    return truth, expl

def stmt_40(df: pd.DataFrame):
    """40. All employees with more than 5 years of experience have a monthly salary greater than or equal to $6.3k."""
    exp = df[df["years_experience"] > 5]
    condition = exp["monthly_salary_k"] >= 6.3
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >5 years experience have salary >= 6.3k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >5 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_41(df: pd.DataFrame):
    """41. If an employee is in the engineering department, then their monthly salary is less than or equal to $10.1k."""
    eng = df[df["department"] == "engineering"]
    condition = eng["monthly_salary_k"] <= 10.1
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have salary <= 10.1k."
    else:
        viol = eng[~condition]
        expl = f"{len(viol)} engineering employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_42(df: pd.DataFrame):
    """42. Most employees in the table have a monthly salary greater than or equal to $6.3k."""
    condition = df["monthly_salary_k"] >= 6.3
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} employees have salary >= 6.3k."
    return truth, expl

def stmt_43(df: pd.DataFrame):
    """43. All employees with a performance rating greater than 4.2 have a monthly salary greater than or equal to $7.7k."""
    high_perf = df[df["performance_rating"] > 4.2]
    condition = high_perf["monthly_salary_k"] >= 7.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf)} employees with performance rating > 4.2 have salary >= 7.7k."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees with performance rating > 4.2 violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_44(df: pd.DataFrame):
    """44. If an employee is in the hr department, then their years of experience are less than or equal to 1.1 years."""
    hr = df[df["department"] == "hr"]
    condition = hr["years_experience"] <= 1.1
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have experience <= 1.1 years."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (experience: {', '.join(map(str, viol['years_experience'].tolist()))})."
    return truth, expl

def stmt_45(df: pd.DataFrame):
    """45. There exists at least one employee in the operations department whose remote days per month are less than or equal to 6 days."""
    ops = df[df["department"] == "operations"]
    condition = ops["remote_days_month"] <= 6
    truth = condition.any()
    if truth:
        expl = f"At least one operations employee has remote days <= 6."
    else:
        expl = f"No operations employee has remote days <= 6."
    return truth, expl

def stmt_46(df: pd.DataFrame):
    """46. All employees with a monthly salary less than or equal to $8.6k have a performance rating greater than or equal to 4.2."""
    low_sal = df[df["monthly_salary_k"] <= 8.6]
    condition = low_sal["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sal)} employees with salary <= 8.6k have performance rating >= 4.2."
    else:
        viol = low_sal[~condition]
        expl = f"{len(viol)} employees with salary <= 8.6k violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_47(df: pd.DataFrame):
    """47. If an employee is in the marketing department, then their monthly salary is less than or equal to $10.3k."""
    marketing = df[df["department"] == "marketing"]
    condition = marketing["monthly_salary_k"] <= 10.3
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees have salary <= 10.3k."
    else:
        viol = marketing[~condition]
        expl = f"{len(viol)} marketing employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_48(df: pd.DataFrame):
    """48. Most employees in the table have a monthly salary less than or equal to $8.6k."""
    condition = df["monthly_salary_k"] <= 8.6
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} employees have salary <= 8.6k."
    return truth, expl

def stmt_49(df: pd.DataFrame):
    """49. All employees with more than 8 years of experience have a monthly salary greater than or equal to $6.9k."""
    exp = df[df["years_experience"] > 8]
    condition = exp["monthly_salary_k"] >= 6.9
    truth = condition.all()
    if truth:
        expl = f"All {len(exp)} employees with >8 years experience have salary >= 6.9k."
    else:
        viol = exp[~condition]
        expl = f"{len(viol)} employees with >8 years experience violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_50(df: pd.DataFrame):
    """50. If an employee is in the finance department, then their projects active are less than or equal to 3 projects."""
    finance = df[df["department"] == "finance"]
    condition = finance["projects_active"] <= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have projects active <= 3."
    else:
        viol = finance[~condition]
        expl = f"{len(viol)} finance employees violate the rule (projects: {', '.join(map(str, viol['projects_active'].tolist()))})."
    return truth, expl

def stmt_51(df: pd.DataFrame):
    """51. There exists at least one employee in the engineering department whose performance rating is greater than or equal to 4.5."""
    eng = df[df["department"] == "engineering"]
    condition = eng["performance_rating"] >= 4.5
    truth = condition.any()
    if truth:
        expl = f"At least one engineering employee has performance rating >= 4.5."
    else:
        expl = f"No engineering employee has performance rating >= 4.5."
    return truth, expl

def stmt_52(df: pd.DataFrame):
    """52. All employees with a performance rating greater than 3.8 have a monthly salary greater than or equal to $7.7k."""
    high_perf = df[df["performance_rating"] > 3.8]
    condition = high_perf["monthly_salary_k"] >= 7.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_perf)} employees with performance rating > 3.8 have salary >= 7.7k."
    else:
        viol = high_perf[~condition]
        expl = f"{len(viol)} employees with performance rating > 3.8 violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_53(df: pd.DataFrame):
    """53. If an employee is in the operations department, then their monthly salary is less than or equal to $6.9k."""
    ops = df[df["department"] == "operations"]
    condition = ops["monthly_salary_k"] <= 6.9
    truth = condition.all()
    if truth:
        expl = f"All {len(ops)} operations employees have salary <= 6.9k."
    else:
        viol = ops[~condition]
        expl = f"{len(viol)} operations employees violate the rule (salaries: {', '.join(map(str, viol['monthly_salary_k'].tolist()))})."
    return truth, expl

def stmt_54(df: pd.DataFrame):
    """54. Most employees in the table have a monthly salary greater than or equal to $6.9k."""
    condition = df["monthly_salary_k"] >= 6.9
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} employees have salary >= 6.9k."
    return truth, expl

def stmt_55(df: pd.DataFrame):
    """55. All employees with a monthly salary less than or equal to $7.7k have a performance rating greater than or equal to 4.4."""
    low_sal = df[df["monthly_salary_k"] <= 7.7]
    condition = low_sal["performance_rating"] >= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sal)} employees with salary <= 7.7k have performance rating >= 4.4."
    else:
        viol = low_sal[~condition]
        expl = f"{len(viol)} employees with salary <= 7.7k violate the rule (ratings: {', '.join(map(str, viol['performance_rating'].tolist()))})."
    return truth, expl

def stmt_56(df: pd.DataFrame):
    """56. If an employee is in the hr department, then their remote days per month are less than or equal to 10 days."""
    hr = df[df["department"] == "hr"]
    condition = hr["remote_days_month"] <= 10
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have remote days <= 10."
    else:
        viol = hr[~condition]
        expl = f"{len(viol)} HR employees violate the rule (remote days: {', '.join(map(str, viol['remote_days_month'].tolist()))})."
    return truth, expl

def stmt_57(df: pd.DataFrame