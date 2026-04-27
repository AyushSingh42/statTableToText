import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all students who study at least 10 hours per week, the test score is at least 87."""
    condition = df["study_hours_week"] >= 10
    subset = df[condition]
    if subset.empty:
        expl = "No students study at least 10 hours per week."
        return True, expl
    valid = subset["test_score"] >= 87
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} students who study at least 10 hours per week scored at least 87."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} students who study at least 10 hours per week scored below 87."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All club members have an attendance rate of at least 85%."""
    condition = df["club_member"] == "yes"
    subset = df[condition]
    if subset.empty:
        expl = "No club members in dataset."
        return True, expl
    valid = subset["attendance_rate"] >= 85
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} club members have attendance rate of at least 85%."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} club members have attendance rate below 85%."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every 12th-grade student scored 89 or lower on the test."""
    condition = df["grade_level"] == 12
    subset = df[condition]
    if subset.empty:
        expl = "No 12th-grade students in dataset."
        return True, expl
    valid = subset["test_score"] <= 89
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} 12th-grade students scored 89 or lower."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} 12th-grade students scored above 89."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Most students (11 out of 15) have an attendance rate of at least 90%."""
    valid = df["attendance_rate"] >= 90
    count = valid.sum()
    total = len(df)
    truth = count >= 11
    if truth:
        expl = f"{count} out of {total} students have attendance rate of at least 90%."
    else:
        expl = f"{count} out of {total} students have attendance rate of at least 90%, which is less than 11."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Students who study three hours or less per week scored at least 88 on the test."""
    condition = df["study_hours_week"] <= 3
    subset = df[condition]
    if subset.empty:
        expl = "No students study three hours or less per week."
        return True, expl
    valid = subset["test_score"] >= 88
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} students who study three hours or less per week scored at least 88."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} students who study three hours or less per week scored below 88."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Any student with an attendance rate of 95% or higher is not a club member."""
    condition = df["attendance_rate"] >= 95
    subset = df[condition]
    if subset.empty:
        expl = "No students have attendance rate of 95% or higher."
        return True, expl
    not_club_member = subset["club_member"]!= "yes"
    truth = not_club_member.all()
    if truth:
        expl = f"All {len(subset)} students with attendance rate of 95% or higher are not club members."
    else:
        viol = subset[~not_club_member]
        expl = f"{len(viol)} students with attendance rate of 95% or higher are club members."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every 9th-grade student scored at least 84 on the test."""
    condition = df["grade_level"] == 9
    subset = df[condition]
    if subset.empty:
        expl = "No 9th-grade students in dataset."
        return True, expl
    valid = subset["test_score"] >= 84
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} 9th-grade students scored at least 84."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} 9th-grade students scored below 84."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All 10th-grade students have an attendance rate of at least 85%."""
    condition = df["grade_level"] == 10
    subset = df[condition]
    if subset.empty:
        expl = "No 10th-grade students in dataset."
        return True, expl
    valid = subset["attendance_rate"] >= 85
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} 10th-grade students have attendance rate of at least 85%."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} 10th-grade students have attendance rate below 85%."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All students who study at least 8 hours per week scored at least 75 on the test."""
    condition = df["study_hours_week"] >= 8
    subset = df[condition]
    if subset.empty:
        expl = "No students study at least 8 hours per week."
        return True, expl
    valid = subset["test_score"] >= 75
    truth = valid.all()
    if truth:
        expl = f"All {len(subset)} students who study at least 8 hours per week scored at least 75."
    else:
        viol = subset[~valid]
        expl = f"{len(viol)} students who study at least 8 hours per week scored below 75."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_60.csv")

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
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()