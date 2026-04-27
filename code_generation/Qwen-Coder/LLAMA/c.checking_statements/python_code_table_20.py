import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 12 have a test score greater than or equal to 75."""
    condition = (df['grade_level'] == 12) & (df['test_score'] >= 75)
    truth = df[condition].shape[0] == df[df['grade_level'] == 12].shape[0]
    if truth:
        expl = f"All students with grade level 12 have test scores >= 75 ({df[df['grade_level'] == 12].shape[0]} total)."
    else:
        viol = df[(df['grade_level'] == 12) & (df['test_score'] < 75)]
        expl = f"{len(viol)} students with grade level 12 have test scores < 75."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is greater than or equal to 90."""
    condition = (df['club_member'] == 'yes') & (df['attendance_rate'] >= 90)
    truth = df[condition].shape[0] == df[df['club_member'] == 'yes'].shape[0]
    if truth:
        expl = f"All club members have attendance rate >= 90 ({df[df['club_member'] == 'yes'].shape[0]} total)."
    else:
        viol = df[(df['club_member'] == 'yes') & (df['attendance_rate'] < 90)]
        expl = f"{len(viol)} club members have attendance rate < 90."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student with a study hours per week greater than 11 who is not a club member."""
    condition = (df['study_hours_week'] > 11) & (df['club_member']!= 'yes')
    truth = df[condition].shape[0] > 0
    if truth:
        expl = f"There is at least one student with study hours > 11 and not a club member."
    else:
        expl = f"No student has study hours > 11 and is not a club member."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All students with a study hours per week less than 4 have a test score less than 90."""
    condition = (df['study_hours_week'] < 4) & (df['test_score'] < 90)
    truth = df[condition].shape[0] == df[df['study_hours_week'] < 4].shape[0]
    if truth:
        expl = f"All students with study hours < 4 have test scores < 90 ({df[df['study_hours_week'] < 4].shape[0]} total)."
    else:
        viol = df[(df['study_hours_week'] < 4) & (df['test_score'] >= 90)]
        expl = f"{len(viol)} students with study hours < 4 have test scores >= 90."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student has a grade level of 10, then their test score is less than 95."""
    condition = (df['grade_level'] == 10) & (df['test_score'] < 95)
    truth = df[condition].shape[0] == df[df['grade_level'] == 10].shape[0]
    if truth:
        expl = f"All students with grade level 10 have test scores < 95 ({df[df['grade_level'] == 10].shape[0]} total)."
    else:
        viol = df[(df['grade_level'] == 10) & (df['test_score'] >= 95)]
        expl = f"{len(viol)} students with grade level 10 have test scores >= 95."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students have an attendance rate greater than 90."""
    condition = df['attendance_rate'] > 90
    truth = df[condition].shape[0] > df.shape[0] / 2
    if truth:
        expl = f"More than half of students ({df[condition].shape[0]}/{df.shape[0]}) have attendance rate > 90."
    else:
        expl = f"Less than or equal to half of students ({df[condition].shape[0]}/{df.shape[0]}) have attendance rate > 90."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a test score greater than 90 have a grade level greater than or equal to 11."""
    condition = (df['test_score'] > 90) & (df['grade_level'] >= 11)
    truth = df[condition].shape[0] == df[df['test_score'] > 90].shape[0]
    if truth:
        expl = f"All students with test score > 90 have grade level >= 11 ({df[df['test_score'] > 90].shape[0]} total)."
    else:
        viol = df[(df['test_score'] > 90) & (df['grade_level'] < 11)]
        expl = f"{len(viol)} students with test score > 90 have grade level < 11."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is not a club member, then their test score is less than 96."""
    condition = (df['club_member']!= 'yes') & (df['test_score'] < 96)
    truth = df[condition].shape[0] == df[df['club_member']!= 'yes'].shape[0]
    if truth:
        expl = f"All non-club members have test scores < 96 ({df[df['club_member']!= 'yes'].shape[0]} total)."
    else:
        viol = df[(df['club_member']!= 'yes') & (df['test_score'] >= 96)]
        expl = f"{len(viol)} non-club members have test scores >= 96."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student with a study hours per week greater than 7 who has a test score less than 80."""
    condition = (df['study_hours_week'] > 7) & (df['test_score'] < 80)
    truth = df[condition].shape[0] > 0
    if truth:
        expl = f"There is at least one student with study hours > 7 and test score < 80."
    else:
        expl = f"No student has study hours > 7 and test score < 80."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All students with a grade level of 9 have a test score less than 90."""
    condition = (df['grade_level'] == 9) & (df['test_score'] < 90)
    truth = df[condition].shape[0] == df[df['grade_level'] == 9].shape[0]
    if truth:
        expl = f"All students with grade level 9 have test scores < 90 ({df[df['grade_level'] == 9].shape[0]} total)."
    else:
        viol = df[(df['grade_level'] == 9) & (df['test_score'] >= 90)]
        expl = f"{len(viol)} students with grade level 9 have test scores >= 90."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study hours per week greater than 8, then they are not a club member."""
    condition = (df['study_hours_week'] > 8) & (df['club_member']!= 'yes')
    truth = df[condition].shape[0] == df[df['study_hours_week'] > 8].shape[0]
    if truth:
        expl = f"All students with study hours > 8 are not club members ({df[df['study_hours_week'] > 8].shape[0]} total)."
    else:
        viol = df[(df['study_hours_week'] > 8) & (df['club_member'] == 'yes')]
        expl = f"{len(viol)} students with study hours > 8 are club members."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most students who are club members have a test score less than 90."""
    condition = (df['club_member'] == 'yes') & (df['test_score'] < 90)
    club_members = df[df['club_member'] == 'yes']
    truth = df[condition].shape[0] > club_members.shape[0] / 2
    if truth:
        expl = f"More than half of club members ({df[condition].shape[0]}/{club_members.shape[0]}) have test scores < 90."
    else:
        expl = f"Less than or equal to half of club members ({df[condition].shape[0]}/{club_members.shape[0]}) have test scores < 90."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All students with a test score greater than 95 have a study hours per week less than 8."""
    condition = (df['test_score'] > 95) & (df['study_hours_week'] < 8)
    truth = df[condition].shape[0] == df[df['test_score'] > 95].shape[0]
    if truth:
        expl = f"All students with test score > 95 have study hours < 8 ({df[df['test_score'] > 95].shape[0]} total)."
    else:
        viol = df[(df['test_score'] > 95) & (df['study_hours_week'] >= 8)]
        expl = f"{len(viol)} students with test score > 95 have study hours >= 8."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a student has a grade level of 11, then their study hours per week is greater than 8."""
    condition = (df['grade_level'] == 11) & (df['study_hours_week'] > 8)
    truth = df[condition].shape[0] == df[df['grade_level'] == 11].shape[0]
    if truth:
        expl = f"All students with grade level 11 have study hours > 8 ({df[df['grade_level'] == 11].shape[0]} total)."
    else:
        viol = df[(df['grade_level'] == 11) & (df['study_hours_week'] <= 8)]
        expl = f"{len(viol)} students with grade level 11 have study hours <= 8."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one student with a study hours per week less than 4 who is a club member."""
    condition = (df['study_hours_week'] < 4) & (df['club_member'] == 'yes')
    truth = df[condition].shape[0] > 0
    if truth:
        expl = f"There is at least one student with study hours < 4 and is a club member."
    else:
        expl = f"No student has study hours < 4 and is a club member."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All students with a test score less than 80 have a grade level less than or equal to 10."""
    condition = (df['test_score'] < 80) & (df['grade_level'] <= 10)
    truth = df[condition].shape[0] == df[df['test_score'] < 80].shape[0]
    if truth:
        expl = f"All students with test score < 80 have grade level <= 10 ({df[df['test_score'] < 80].shape[0]} total)."
    else:
        viol = df[(df['test_score'] < 80) & (df['grade_level'] > 10)]
        expl = f"{len(viol)} students with test score < 80 have grade level > 10."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a student is a club member, then their grade level is less than or equal to 12."""
    condition = (df['club_member'] == 'yes') & (df['grade_level'] <= 12)
    truth = df[condition].shape[0] == df[df['club_member'] == 'yes'].shape[0]
    if truth:
        expl = f"All club members have grade level <= 12 ({df[df['club_member'] == 'yes'].shape[0]} total)."
    else:
        viol = df[(df['club_member'] == 'yes') & (df['grade_level'] > 12)]
        expl = f"{len(viol)} club members have grade level > 12."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most students who have a study hours per week greater than 7 do not have a test score greater than 90."""
    condition = (df['study_hours_week'] > 7) & (df['test_score'] <= 90)
    high_study = df[df['study_hours_week'] > 7]
    truth = df[condition].shape[0] > high_study.shape[0] / 2
    if truth:
        expl = f"More than half of students with study hours > 7 ({df[condition].shape[0]}/{high_study.shape[0]}) do not have test score > 90."
    else:
        expl = f"Less than or equal to half of students with study hours > 7 ({df[condition].shape[0]}/{high_study.shape[0]}) do not have test score > 90."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_20.csv")

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