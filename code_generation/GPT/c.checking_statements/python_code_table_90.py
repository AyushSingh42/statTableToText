import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all students who study at least 9 hours per week, the test score is at least 83."""
    condition = df["study_hours_week"] >= 9
    subset = df[condition]
    if subset.empty:
        expl = "No students study at least 9 hours per week."
        return True, expl
    valid = subset["test_score"] >= 83
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} students studying at least 9 hours per week have test scores of at least 83."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} students studying at least 9 hours per week have test scores below 83."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all students with a test score of 90 or higher, the attendance rate is at least 86.6%."""
    condition = df["test_score"] >= 90
    subset = df[condition]
    if subset.empty:
        expl = "No students have a test score of 90 or higher."
        return True, expl
    valid = subset["attendance_rate"] >= 86.6
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} students with test scores of 90 or higher have attendance rates of at least 86.6%."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} students with test scores of 90 or higher have attendance rates below 86.6%."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All students with an attendance rate of 95% or higher are members of a club."""
    condition = df["attendance_rate"] >= 95
    subset = df[condition]
    if subset.empty:
        expl = "No students have an attendance rate of 95% or higher."
        return True, expl
    valid = subset["club_member"] == "yes"
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} students with attendance rates of 95% or higher are club members."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} students with attendance rates of 95% or higher are not club members."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All grade 12 students who are club members have test scores of at most 92."""
    condition = (df["grade_level"] == 12) & (df["club_member"] == "yes")
    subset = df[condition]
    if subset.empty:
        expl = "No grade 12 students are club members."
        return True, expl
    valid = subset["test_score"] <= 92
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} grade 12 club members have test scores of at most 92."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} grade 12 club members have test scores above 92."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. There exists at least one student who studies less than 3 hours per week and has a test score of at least 71."""
    condition = (df["study_hours_week"] < 3) & (df["test_score"] >= 71)
    subset = df[condition]
    truth = not subset.empty
    if truth:
        expl = f"There is at least one student ({len(subset)} total) who studies less than 3 hours per week and has a test score of at least 71."
    else:
        expl = "No student studies less than 3 hours per week and has a test score of at least 71."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students have a test score of at least 75."""
    total_students = len(df)
    condition = df["test_score"] >= 75
    count = df[condition].shape[0]
    truth = count > total_students / 2
    if truth:
        expl = f"{count} out of {total_students} students have test scores of at least 75 (more than half)."
    else:
        expl = f"{count} out of {total_students} students have test scores of at least 75 (not more than half)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_90.csv")

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
        (6, stmt_6)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()