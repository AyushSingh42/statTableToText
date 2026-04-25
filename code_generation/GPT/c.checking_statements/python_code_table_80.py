import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students who study at least 10 hours per week have test scores of at least 89."""
    condition = df["study_hours_week"] >= 10
    subset = df[condition]
    if subset.empty:
        expl = "No students study at least 10 hours per week."
        return True, expl
    valid = subset["test_score"] >= 89
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} students studying >=10 hours/week have test scores >=89."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} students studying >=10 hours/week have test scores <89."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All club members study at least 5.5 hours per week."""
    condition = df["club_member"] == "yes"
    subset = df[condition]
    if subset.empty:
        expl = "No club members found."
        return True, expl
    valid = subset["study_hours_week"] >= 5.5
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} club members study >=5.5 hours/week."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} club members study <5.5 hours/week."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All grade 12 students study at least 7.2 hours per week."""
    condition = df["grade_level"] == 12
    subset = df[condition]
    if subset.empty:
        expl = "No grade 12 students found."
        return True, expl
    valid = subset["study_hours_week"] >= 7.2
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} grade 12 students study >=7.2 hours/week."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} grade 12 students study <7.2 hours/week."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All grade 9 students have test scores no higher than 94."""
    condition = df["grade_level"] == 9
    subset = df[condition]
    if subset.empty:
        expl = "No grade 9 students found."
        return True, expl
    valid = subset["test_score"] <= 94
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} grade 9 students have test scores <=94."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} grade 9 students have test scores >94."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All grade 9 students have attendance rates of at least 88.0%."""
    condition = df["grade_level"] == 9
    subset = df[condition]
    if subset.empty:
        expl = "No grade 9 students found."
        return True, expl
    valid = subset["attendance_rate"] >= 88.0
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} grade 9 students have attendance >=88.0%."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} grade 9 students have attendance <88.0%."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All students with test scores of at least 95 have attendance rates of at least 88.4%."""
    condition = df["test_score"] >= 95
    subset = df[condition]
    if subset.empty:
        expl = "No students with test scores >=95 found."
        return True, expl
    valid = subset["attendance_rate"] >= 88.4
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} students with test scores >=95 have attendance >=88.4%."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} students with test scores >=95 have attendance <88.4%."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most students have attendance rates above 85%."""
    valid = df["attendance_rate"] > 85
    count_valid = valid.sum()
    total = len(df)
    truth = count_valid > total / 2
    expl = f"{count_valid} out of {total} students have attendance >85%, which is {'more' if truth else 'not more'} than half."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_80.csv")

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
        (7, stmt_7)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()