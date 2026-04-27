import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 12 have a test score greater than or equal to 65."""
    condition = (df['grade_level'] == 12) & (df['test_score'] >= 65)
    truth = condition.all() or df[df['grade_level'] == 12].empty
    if truth:
        expl = "All students in grade 12 have test scores >= 65."
    else:
        viol = df[(df['grade_level'] == 12) & (df['test_score'] < 65)]
        expl = f"{len(viol)} students in grade 12 have test scores < 65."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is greater than or equal to 84.2."""
    condition = (df['club_member'] == 'yes') & (df['attendance_rate'] >= 84.2)
    truth = condition.all() or df[df['club_member'] == 'yes'].empty
    if truth:
        expl = "All club members have attendance rates >= 84.2."
    else:
        viol = df[(df['club_member'] == 'yes') & (df['attendance_rate'] < 84.2)]
        expl = f"{len(viol)} club members have attendance rates < 84.2."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in grade level 11 who has a test score greater than 90."""
    condition = (df['grade_level'] == 11) & (df['test_score'] > 90)
    truth = condition.any()
    if truth:
        expl = "At least one student in grade 11 has test score > 90."
    else:
        expl = "No student in grade 11 has test score > 90."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all students with study hours per week greater than 9, their test score is greater than or equal to 65."""
    condition = (df['study_hours_week'] > 9) & (df['test_score'] >= 65)
    truth = condition.all() or df[df['study_hours_week'] > 9].empty
    if truth:
        expl = "All students with study hours > 9 have test scores >= 65."
    else:
        viol = df[(df['study_hours_week'] > 9) & (df['test_score'] < 65)]
        expl = f"{len(viol)} students with study hours > 9 have test scores < 65."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most students in the table have an attendance rate greater than 85."""
    condition = df['attendance_rate'] > 85
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of students have attendance rate > 85."
    else:
        expl = f"Less than half ({count}/{total}) of students have attendance rate > 85."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a student is in grade level 9, then their study hours per week are greater than or equal to 5.4."""
    condition = (df['grade_level'] == 9) & (df['study_hours_week'] >= 5.4)
    truth = condition.all() or df[df['grade_level'] == 9].empty
    if truth:
        expl = "All students in grade 9 have study hours >= 5.4."
    else:
        viol = df[(df['grade_level'] == 9) & (df['study_hours_week'] < 5.4)]
        expl = f"{len(viol)} students in grade 9 have study hours < 5.4."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a test score greater than 90 have a grade level of 11 or 12."""
    condition = (df['test_score'] > 90) & (df['grade_level'].isin([11, 12]))
    truth = condition.all() or df[df['test_score'] > 90].empty
    if truth:
        expl = "All students with test score > 90 have grade level 11 or 12."
    else:
        viol = df[(df['test_score'] > 90) & (~df['grade_level'].isin([11, 12]))]
        expl = f"{len(viol)} students with test score > 90 do not have grade level 11 or 12."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one student who is not a club member and has a test score greater than 80."""
    condition = (df['club_member'] == 'no') & (df['test_score'] > 80)
    truth = condition.any()
    if truth:
        expl = "At least one non-club member has test score > 80."
    else:
        expl = "No non-club member has test score > 80."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. For all students with attendance rate greater than 90, their study hours per week are greater than or equal to 5.9."""
    condition = (df['attendance_rate'] > 90) & (df['study_hours_week'] >= 5.9)
    truth = condition.all() or df[df['attendance_rate'] > 90].empty
    if truth:
        expl = "All students with attendance rate > 90 have study hours >= 5.9."
    else:
        viol = df[(df['attendance_rate'] > 90) & (df['study_hours_week'] < 5.9)]
        expl = f"{len(viol)} students with attendance rate > 90 have study hours < 5.9."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a student has a test score less than 70, then they are in grade level 10 or 12."""
    condition = (df['test_score'] < 70) & (df['grade_level'].isin([10, 12]))
    truth = condition.all() or df[df['test_score'] < 70].empty
    if truth:
        expl = "All students with test score < 70 are in grade 10 or 12."
    else:
        viol = df[(df['test_score'] < 70) & (~df['grade_level'].isin([10, 12]))]
        expl = f"{len(viol)} students with test score < 70 are not in grade 10 or 12."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Most students in the table are club members."""
    condition = df['club_member'] == 'yes'
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of students are club members."
    else:
        expl = f"Less than half ({count}/{total}) of students are club members."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All students with study hours per week less than 4 have a test score less than 80."""
    condition = (df['study_hours_week'] < 4) & (df['test_score'] < 80)
    truth = condition.all() or df[df['study_hours_week'] < 4].empty
    if truth:
        expl = "All students with study hours < 4 have test scores < 80."
    else:
        viol = df[(df['study_hours_week'] < 4) & (df['test_score'] >= 80)]
        expl = f"{len(viol)} students with study hours < 4 have test scores >= 80."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a student is in grade level 11, then their attendance rate is greater than or equal to 85.2."""
    condition = (df['grade_level'] == 11) & (df['attendance_rate'] >= 85.2)
    truth = condition.all() or df[df['grade_level'] == 11].empty
    if truth:
        expl = "All students in grade 11 have attendance rate >= 85.2."
    else:
        viol = df[(df['grade_level'] == 11) & (df['attendance_rate'] < 85.2)]
        expl = f"{len(viol)} students in grade 11 have attendance rate < 85.2."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one student in grade level 9 who has a test score greater than 90."""
    condition = (df['grade_level'] == 9) & (df['test_score'] > 90)
    truth = condition.any()
    if truth:
        expl = "At least one student in grade 9 has test score > 90."
    else:
        expl = "No student in grade 9 has test score > 90."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. For all students with a test score greater than 95, their grade level is 9 or 11."""
    condition = (df['test_score'] > 95) & (df['grade_level'].isin([9, 11]))
    truth = condition.all() or df[df['test_score'] > 95].empty
    if truth:
        expl = "All students with test score > 95 have grade level 9 or 11."
    else:
        viol = df[(df['test_score'] > 95) & (~df['grade_level'].isin([9, 11]))]
        expl = f"{len(viol)} students with test score > 95 do not have grade level 9 or 11."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All students with attendance rate greater than 95 have a grade level of 12."""
    condition = (df['attendance_rate'] > 95) & (df['grade_level'] == 12)
    truth = condition.all() or df[df['attendance_rate'] > 95].empty
    if truth:
        expl = "All students with attendance rate > 95 have grade level 12."
    else:
        viol = df[(df['attendance_rate'] > 95) & (df['grade_level']!= 12)]
        expl = f"{len(viol)} students with attendance rate > 95 do not have grade level 12."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a student has a test score greater than 80, then their study hours per week are greater than or equal to 5.4."""
    condition = (df['test_score'] > 80) & (df['study_hours_week'] >= 5.4)
    truth = condition.all() or df[df['test_score'] > 80].empty
    if truth:
        expl = "All students with test score > 80 have study hours >= 5.4."
    else:
        viol = df[(df['test_score'] > 80) & (df['study_hours_week'] < 5.4)]
        expl = f"{len(viol)} students with test score > 80 have study hours < 5.4."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_30.csv")

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
        (17, stmt_17)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()