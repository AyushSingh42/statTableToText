import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 9 have a test score less than 90."""
    condition = (df['grade_level'] == 9) & (df['test_score'] >= 90)
    truth = not condition.any()
    if truth:
        expl = "All students with grade level 9 have test scores less than 90."
    else:
        viol = df[condition]
        expl = f"{len(viol)} students with grade level 9 have test score >= 90."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their study hours per week are greater than or equal to 3.3."""
    condition = (df['club_member'] == 'yes') & (df['study_hours_week'] < 3.3)
    truth = not condition.any()
    if truth:
        expl = "All club members have study hours >= 3.3."
    else:
        viol = df[condition]
        expl = f"{len(viol)} club members have study hours < 3.3."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student with a grade level of 12 who has a test score of 91."""
    condition = (df['grade_level'] == 12) & (df['test_score'] == 91)
    truth = condition.any()
    if truth:
        expl = "At least one student with grade level 12 has test score 91."
    else:
        expl = "No student with grade level 12 has test score 91."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All students with a study hours per week of 11.1 or more have a grade level of 9 or 12."""
    condition = (df['study_hours_week'] >= 11.1) & (~df['grade_level'].isin([9, 12]))
    truth = not condition.any()
    if truth:
        expl = "All students with study hours >= 11.1 have grade level 9 or 12."
    else:
        viol = df[condition]
        expl = f"{len(viol)} students with study hours >= 11.1 do not have grade level 9 or 12."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student has an attendance rate greater than 96, then their test score is less than 90."""
    condition = (df['attendance_rate'] > 96) & (df['test_score'] >= 90)
    truth = not condition.any()
    if truth:
        expl = "All students with attendance > 96 have test score < 90."
    else:
        viol = df[condition]
        expl = f"{len(viol)} students with attendance > 96 have test score >= 90."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students have an attendance rate greater than 90."""
    condition = df['attendance_rate'] > 90
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of students have attendance > 90."
    else:
        expl = f"Less than or equal to half ({count}/{total}) of students have attendance > 90."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a grade level of 11 have a test score less than 90."""
    condition = (df['grade_level'] == 11) & (df['test_score'] >= 90)
    truth = not condition.any()
    if truth:
        expl = "All students with grade level 11 have test scores < 90."
    else:
        viol = df[condition]
        expl = f"{len(viol)} students with grade level 11 have test score >= 90."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is a club member, then their grade level is not 12."""
    condition = (df['club_member'] == 'yes') & (df['grade_level'] == 12)
    truth = not condition.any()
    if truth:
        expl = "No club members have grade level 12."
    else:
        viol = df[condition]
        expl = f"{len(viol)} club members have grade level 12."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student with a grade level of 9 who has a study hours per week of 7.7 or more."""
    condition = (df['grade_level'] == 9) & (df['study_hours_week'] >= 7.7)
    truth = condition.any()
    if truth:
        expl = "At least one student with grade level 9 has study hours >= 7.7."
    else:
        expl = "No student with grade level 9 has study hours >= 7.7."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All students with a test score of 91 or more have a grade level of 12."""
    condition = (df['test_score'] >= 91) & (df['grade_level']!= 12)
    truth = not condition.any()
    if truth:
        expl = "All students with test score >= 91 have grade level 12."
    else:
        viol = df[condition]
        expl = f"{len(viol)} students with test score >= 91 do not have grade level 12."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study hours per week of 2.5 or less, then their test score is less than 90."""
    condition = (df['study_hours_week'] <= 2.5) & (df['test_score'] >= 90)
    truth = not condition.any()
    if truth:
        expl = "All students with study hours <= 2.5 have test score < 90."
    else:
        viol = df[condition]
        expl = f"{len(viol)} students with study hours <= 2.5 have test score >= 90."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All students with a grade level of 10 have a test score less than 91."""
    condition = (df['grade_level'] == 10) & (df['test_score'] >= 91)
    truth = not condition.any()
    if truth:
        expl = "All students with grade level 10 have test scores < 91."
    else:
        viol = df[condition]
        expl = f"{len(viol)} students with grade level 10 have test score >= 91."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most students are not club members."""
    condition = df['club_member'] == 'no'
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of students are not club members."
    else:
        expl = f"Less than or equal to half ({count}/{total}) of students are not club members."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a student has an attendance rate greater than 94, then their test score is less than 91."""
    condition = (df['attendance_rate'] > 94) & (df['test_score'] >= 91)
    truth = not condition.any()
    if truth:
        expl = "All students with attendance > 94 have test score < 91."
    else:
        viol = df[condition]
        expl = f"{len(viol)} students with attendance > 94 have test score >= 91."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one student with a grade level of 11 who has a study hours per week of 9.8 or more."""
    condition = (df['grade_level'] == 11) & (df['study_hours_week'] >= 9.8)
    truth = condition.any()
    if truth:
        expl = "At least one student with grade level 11 has study hours >= 9.8."
    else:
        expl = "No student with grade level 11 has study hours >= 9.8."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All students with a study hours per week of 8.2 or more have a grade level of 10 or 11."""
    condition = (df['study_hours_week'] >= 8.2) & (~df['grade_level'].isin([10, 11]))
    truth = not condition.any()
    if truth:
        expl = "All students with study hours >= 8.2 have grade level 10 or 11."
    else:
        viol = df[condition]
        expl = f"{len(viol)} students with study hours >= 8.2 do not have grade level 10 or 11."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_10.csv")

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