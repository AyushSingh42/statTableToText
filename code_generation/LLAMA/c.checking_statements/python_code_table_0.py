import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 9 have a test score less than 95."""
    condition = (df["grade_level"] == 9) & (df["test_score"] >= 95)
    truth = not condition.any()
    if truth:
        expl = "No grade 9 student has a test score >= 95."
    else:
        viol = df[condition]
        expl = f"{len(viol)} grade 9 student(s) have test score >= 95."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is greater than 85."""
    condition = (df["club_member"] == "yes") & (df["attendance_rate"] <= 85)
    truth = not condition.any()
    if truth:
        expl = "All club members have attendance > 85."
    else:
        viol = df[condition]
        expl = f"{len(viol)} club member(s) have attendance <= 85."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in grade level 11 who has a test score greater than 95."""
    condition = (df["grade_level"] == 11) & (df["test_score"] > 95)
    truth = condition.any()
    if truth:
        expl = "At least one grade 11 student has test score > 95."
    else:
        expl = "No grade 11 student has test score > 95."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All students with study hours per week greater than 9 have a test score greater than 85."""
    condition = (df["study_hours_week"] > 9) & (df["test_score"] <= 85)
    truth = not condition.any()
    if truth:
        expl = "All students with study hours > 9 have test score > 85."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) with study hours > 9 have test score <= 85."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student is in grade level 10, then their study hours per week are greater than 5."""
    condition = (df["grade_level"] == 10) & (df["study_hours_week"] <= 5)
    truth = not condition.any()
    if truth:
        expl = "All grade 10 students have study hours > 5."
    else:
        viol = df[condition]
        expl = f"{len(viol)} grade 10 student(s) have study hours <= 5."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students in the table have an attendance rate greater than 90."""
    condition = df["attendance_rate"] > 90
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} students have attendance > 90."
    else:
        expl = f"{count} out of {total} students have attendance > 90 (not majority)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a test score less than 80 have a grade level greater than 9."""
    condition = (df["test_score"] < 80) & (df["grade_level"] <= 9)
    truth = not condition.any()
    if truth:
        expl = "All students with test score < 80 have grade level > 9."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) with test score < 80 have grade level <= 9."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is not a club member, then their test score is less than 90."""
    condition = (df["club_member"] == "no") & (df["test_score"] >= 90)
    truth = not condition.any()
    if truth:
        expl = "All non-club members have test score < 90."
    else:
        viol = df[condition]
        expl = f"{len(viol)} non-club member(s) have test score >= 90."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student in grade level 9 who has a study hours per week less than 3."""
    condition = (df["grade_level"] == 9) & (df["study_hours_week"] < 3)
    truth = condition.any()
    if truth:
        expl = "At least one grade 9 student has study hours < 3."
    else:
        expl = "No grade 9 student has study hours < 3."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All students with a grade level of 12 have a test score less than 85."""
    condition = (df["grade_level"] == 12) & (df["test_score"] >= 85)
    truth = not condition.any()
    if truth:
        expl = "No grade 12 student has test score >= 85."
    else:
        viol = df[condition]
        expl = f"{len(viol)} grade 12 student(s) have test score >= 85."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study hours per week greater than 10, then they are a club member."""
    condition = (df["study_hours_week"] > 10) & (df["club_member"]!= "yes")
    truth = not condition.any()
    if truth:
        expl = "All students with study hours > 10 are club members."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) with study hours > 10 are not club members."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most students in the table have a study hours per week less than 10."""
    condition = df["study_hours_week"] < 10
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} students have study hours < 10."
    else:
        expl = f"{count} out of {total} students have study hours < 10 (not majority)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All students with an attendance rate greater than 95 have a grade level greater than 9."""
    condition = (df["attendance_rate"] > 95) & (df["grade_level"] <= 9)
    truth = not condition.any()
    if truth:
        expl = "All students with attendance > 95 have grade level > 9."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) with attendance > 95 have grade level <= 9."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a student is in grade level 11, then their attendance rate is greater than 92."""
    condition = (df["grade_level"] == 11) & (df["attendance_rate"] <= 92)
    truth = not condition.any()
    if truth:
        expl = "All grade 11 students have attendance > 92."
    else:
        viol = df[condition]
        expl = f"{len(viol)} grade 11 student(s) have attendance <= 92."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one student in grade level 10 who has a test score greater than 90."""
    condition = (df["grade_level"] == 10) & (df["test_score"] > 90)
    truth = condition.any()
    if truth:
        expl = "At least one grade 10 student has test score > 90."
    else:
        expl = "No grade 10 student has test score > 90."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All students with a test score greater than 95 have a grade level greater than 10."""
    condition = (df["test_score"] > 95) & (df["grade_level"] <= 10)
    truth = not condition.any()
    if truth:
        expl = "All students with test score > 95 have grade level > 10."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) with test score > 95 have grade level <= 10."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_0.csv")

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
        (16, stmt_16)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()