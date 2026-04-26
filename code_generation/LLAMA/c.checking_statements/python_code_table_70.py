import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 12 have a test score greater than or equal to 68."""
    condition = (df['grade_level'] == 12) & (df['test_score'] >= 68)
    truth = df[condition].shape[0] == df[df['grade_level'] == 12].shape[0]
    if truth:
        expl = "All students in 12th grade have test scores >= 68."
    else:
        viol = df[(df['grade_level'] == 12) & (df['test_score'] < 68)]
        expl = f"{len(viol)} students in 12th grade have test scores < 68."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is greater than or equal to 90."""
    condition = (df['club_member'] == 'yes') & (df['attendance_rate'] >= 90)
    truth = df[condition].shape[0] == df[df['club_member'] == 'yes'].shape[0]
    if truth:
        expl = "All club members have attendance rate >= 90."
    else:
        viol = df[(df['club_member'] == 'yes') & (df['attendance_rate'] < 90)]
        expl = f"{len(viol)} club members have attendance rate < 90."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All students with a study time of less than 6 hours per week have a test score less than 70."""
    condition = (df['study_hours_week'] < 6) & (df['test_score'] < 70)
    truth = df[condition].shape[0] == df[df['study_hours_week'] < 6].shape[0]
    if truth:
        expl = "All students with <6 study hours have test scores < 70."
    else:
        viol = df[(df['study_hours_week'] < 6) & (df['test_score'] >= 70)]
        expl = f"{len(viol)} students with <6 study hours have test scores >= 70."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one student in the 9th grade with a test score greater than 85."""
    condition = (df['grade_level'] == 9) & (df['test_score'] > 85)
    truth = df[condition].shape[0] > 0
    if truth:
        expl = "At least one 9th grader has test score > 85."
    else:
        expl = "No 9th graders have test scores > 85."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student is in the 11th grade, then their study time is less than 10 hours per week."""
    condition = (df['grade_level'] == 11) & (df['study_hours_week'] < 10)
    truth = df[condition].shape[0] == df[df['grade_level'] == 11].shape[0]
    if truth:
        expl = "All 11th graders have study time < 10 hours/week."
    else:
        viol = df[(df['grade_level'] == 11) & (df['study_hours_week'] >= 10)]
        expl = f"{len(viol)} 11th graders have study time >= 10 hours/week."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All students with an attendance rate greater than 95 have a test score greater than 60."""
    condition = (df['attendance_rate'] > 95) & (df['test_score'] > 60)
    truth = df[condition].shape[0] == df[df['attendance_rate'] > 95].shape[0]
    if truth:
        expl = "All students with attendance > 95 have test score > 60."
    else:
        viol = df[(df['attendance_rate'] > 95) & (df['test_score'] <= 60)]
        expl = f"{len(viol)} students with attendance > 95 have test score <= 60."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most students have an attendance rate greater than 90."""
    total = len(df)
    condition = df['attendance_rate'] > 90
    count = df[condition].shape[0]
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of students have attendance > 90."
    else:
        expl = f"Less than half ({count}/{total}) of students have attendance > 90."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is not a club member, then their test score is greater than 70."""
    condition = (df['club_member'] == 'no') & (df['test_score'] > 70)
    truth = df[condition].shape[0] == df[df['club_member'] == 'no'].shape[0]
    if truth:
        expl = "All non-club members have test score > 70."
    else:
        viol = df[(df['club_member'] == 'no') & (df['test_score'] <= 70)]
        expl = f"{len(viol)} non-club members have test score <= 70."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All students with a study time of greater than 9 hours per week have a grade level of 9 or 11."""
    condition = (df['study_hours_week'] > 9) & ((df['grade_level'] == 9) | (df['grade_level'] == 11))
    truth = df[condition].shape[0] == df[df['study_hours_week'] > 9].shape[0]
    if truth:
        expl = "All students with >9 study hours have grade level 9 or 11."
    else:
        viol = df[(df['study_hours_week'] > 9) & ~((df['grade_level'] == 9) | (df['grade_level'] == 11))]
        expl = f"{len(viol)} students with >9 study hours do not have grade level 9 or 11."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one student in the 12th grade with a study time of less than 7 hours per week."""
    condition = (df['grade_level'] == 12) & (df['study_hours_week'] < 7)
    truth = df[condition].shape[0] > 0
    if truth:
        expl = "At least one 12th grader has study time < 7 hours/week."
    else:
        expl = "No 12th graders have study time < 7 hours/week."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All students with a test score greater than 85 have a grade level of 9 or 12."""
    condition = (df['test_score'] > 85) & ((df['grade_level'] == 9) | (df['grade_level'] == 12))
    truth = df[condition].shape[0] == df[df['test_score'] > 85].shape[0]
    if truth:
        expl = "All students with test score > 85 have grade level 9 or 12."
    else:
        viol = df[(df['test_score'] > 85) & ~((df['grade_level'] == 9) | (df['grade_level'] == 12))]
        expl = f"{len(viol)} students with test score > 85 do not have grade level 9 or 12."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a student has a study time of less than 5 hours per week, then they are not a club member."""
    condition = (df['study_hours_week'] < 5) & (df['club_member'] == 'no')
    truth = df[condition].shape[0] == df[df['study_hours_week'] < 5].shape[0]
    if truth:
        expl = "All students with <5 study hours are not club members."
    else:
        viol = df[(df['study_hours_week'] < 5) & (df['club_member'] == 'yes')]
        expl = f"{len(viol)} students with <5 study hours are club members."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most students who are club members have a test score greater than 65."""
    club_members = df[df['club_member'] == 'yes']
    if club_members.empty:
        truth = True
        expl = "No club members exist."
    else:
        condition = club_members['test_score'] > 65
        count = club_members[condition].shape[0]
        total = len(club_members)
        truth = count > total / 2
        if truth:
            expl = f"More than half ({count}/{total}) of club members have test score > 65."
        else:
            expl = f"Less than half ({count}/{total}) of club members have test score > 65."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All students with an attendance rate greater than 96 have a study time of greater than 3 hours per week."""
    condition = (df['attendance_rate'] > 96) & (df['study_hours_week'] > 3)
    truth = df[condition].shape[0] == df[df['attendance_rate'] > 96].shape[0]
    if truth:
        expl = "All students with attendance > 96 have study time > 3 hours/week."
    else:
        viol = df[(df['attendance_rate'] > 96) & (df['study_hours_week'] <= 3)]
        expl = f"{len(viol)} students with attendance > 96 have study time <= 3 hours/week."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a student is in the 10th grade, then their test score is greater than 70."""
    condition = (df['grade_level'] == 10) & (df['test_score'] > 70)
    truth = df[condition].shape[0] == df[df['grade_level'] == 10].shape[0]
    if truth:
        expl = "All 10th graders have test score > 70."
    else:
        viol = df[(df['grade_level'] == 10) & (df['test_score'] <= 70)]
        expl = f"{len(viol)} 10th graders have test score <= 70."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one student in the 11th grade with a test score greater than 90."""
    condition = (df['grade_level'] == 11) & (df['test_score'] > 90)
    truth = df[condition].shape[0] > 0
    if truth:
        expl = "At least one 11th grader has test score > 90."
    else:
        expl = "No 11th graders have test scores > 90."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All students with a study time of greater than 10 hours per week have a grade level of 9."""
    condition = (df['study_hours_week'] > 10) & (df['grade_level'] == 9)
    truth = df[condition].shape[0] == df[df['study_hours_week'] > 10].shape[0]
    if truth:
        expl = "All students with >10 study hours have grade level 9."
    else:
        viol = df[(df['study_hours_week'] > 10) & (df['grade_level']!= 9)]
        expl = f"{len(viol)} students with >10 study hours do not have grade level 9."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a student has a test score of less than 70, then they are not in the 12th grade."""
    condition = (df['test_score'] < 70) & (df['grade_level']!= 12)
    truth = df[condition].shape[0] == df[df['test_score'] < 70].shape[0]
    if truth:
        expl = "All students with test score < 70 are not in 12th grade."
    else:
        viol = df[(df['test_score'] < 70) & (df['grade_level'] == 12)]
        expl = f"{len(viol)} students with test score < 70 are in 12th grade."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_70.csv")

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