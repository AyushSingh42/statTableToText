import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all finance employees, performance rating is at least 4.2."""
    finance = df[df["department"] == "finance"]
    condition = finance["performance_rating"] >= 4.2
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have rating ≥4.2."
    else:
        viol = finance[~condition]
        ids = ", ".join(map(str, viol["employee_id"].tolist()))
        expl = f"{len(viol)} finance employees violate the rule (IDs: {ids})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All HR employees have remote work days per month of at least 8."""
    hr = df[df["department"] == "HR"]
    condition = hr["remote_days_month"] >= 8
    truth = condition.all()
    if truth:
        expl = f"All {len(hr)} HR employees have remote days ≥8."
    else:
        viol = hr[~condition]
        ids = ", ".join(map(str, viol["employee_id"].tolist()))
        expl = f"{len(viol)} HR employees violate the rule (IDs: {ids})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All engineering employees have remote work days per month of at least 10."""
    eng = df[df["department"] == "engineering"]
    condition = eng["remote_days_month"] >= 10
    truth = condition.all()
    if truth:
        expl = f"All {len(eng)} engineering employees have remote days ≥10."
    else:
        viol = eng[~condition]
        ids = ", ".join(map(str, viol["employee_id"].tolist()))
        expl = f"{len(viol)} engineering employees violate the rule (IDs: {ids})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If an employee works remotely at least 12 days per month, then they are in engineering."""
    subset = df[df["remote_days_month"] >= 12]
    condition = subset["department"] == "engineering"
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} employees with ≥12 remote days are in engineering."
    else:
        viol = subset[~condition]
        ids = ", ".join(map(str, viol["employee_id"].tolist()))
        expl = f"{len(viol)} employees with ≥12 remote days are not in engineering (IDs: {ids})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If an employee is involved in five or more active projects, they belong to the engineering department."""
    subset = df[df["projects_active"] >= 5]
    condition = subset["department"] == "engineering"
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} employees with ≥5 projects are in engineering."
    else:
        viol = subset[~condition]
        ids = ", ".join(map(str, viol["employee_id"].tolist()))
        expl = f"{len(viol)} employees with ≥5 projects are not in engineering (IDs: {ids})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All marketing employees have monthly salary of at most $5.9k."""
    marketing = df[df["department"] == "marketing"]
    condition = marketing["monthly_salary_k"] <= 5.9
    truth = condition.all()
    if truth:
        expl = f"All {len(marketing)} marketing employees earn ≤5.9k."
    else:
        viol = marketing[~condition]
        ids = ", ".join(map(str, viol["employee_id"].tolist()))
        expl = f"{len(viol)} marketing employees exceed 5.9k (IDs: {ids})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All finance employees have remote work days per month of 6 or fewer."""
    finance = df[df["department"] == "finance"]
    condition = finance["remote_days_month"] <= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(finance)} finance employees have remote days ≤6."
    else:
        viol = finance[~condition]
        ids = ", ".join(map(str, viol["employee_id"].tolist()))
        expl = f"{len(viol)} finance employees exceed 6 remote days (IDs: {ids})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most employees have a performance rating of at least 4.0."""
    total = len(df)
    count = (df["performance_rating"] >= 4.0).sum()
    truth = count > total / 2
    perc = (count / total) * 100 if total else 0
    expl = f"{count}/{total} employees ({perc:.1f}%) have rating ≥4.0."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If performance rating is at least 4.7, then the employee works in engineering."""
    subset = df[df["performance_rating"] >= 4.7]
    condition = subset["department"] == "engineering"
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} employees with rating ≥4.7 are in engineering."
    else:
        viol = subset[~condition]
        ids = ", ".join(map(str, viol["employee_id"].tolist()))
        expl = f"{len(viol)} employees with rating ≥4.7 are not in engineering (IDs: {ids})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_4.csv")
    # Convert numeric columns that may be stored as strings
    numeric_cols_int = ["years_experience", "projects_active", "remote_days_month"]
    numeric_cols_float = ["monthly_salary_k", "performance_rating"]
    for col in numeric_cols_int:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
    for col in numeric_cols_float:
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
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()