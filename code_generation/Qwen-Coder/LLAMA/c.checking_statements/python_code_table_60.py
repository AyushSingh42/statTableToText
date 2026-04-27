import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a test score greater than or equal to 90 have a study time greater than or equal to 9 hours per week."""
    condition = (df['test_score'] >= 90) & (df['study_hours_week'] < 9)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = f"All students with test score >= 90 have study time >= 9 hours/week ({len(df[df['test_score'] >= 90])} such students)."
    else:
        expl = f"{len(violations)} students violate the rule (test scores: {', '.join(map(str, violations['test_score'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their test score is less than or equal to 97."""
    condition = (df['club_member'] == 'yes') & (df['test_score'] > 97)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = f"All club members have test scores <= 97 ({len(df[df['club_member'] == 'yes'])} such students)."
    else:
        expl = f"{len(violations)} club members violate the rule (test scores: {', '.join(map(str, violations['test_score'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in the 9th grade with a test score greater than 90."""
    condition = (df['grade_level'] == 9) & (df['test_score'] > 90)
    found = df[condition]
    truth = len(found) > 0
    if truth:
        expl = f"Found {len(found)} 9th grade student(s) with test score > 90."
    else:
        expl = "No 9th grade student has test score > 90."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All students with an attendance rate greater than 94 have a test score greater than or equal to 84."""
    condition = (df['attendance_rate'] > 94) & (df['test_score'] < 84)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = f"All students with attendance rate > 94 have test score >= 84 ({len(df[df['attendance_rate'] > 94])} such students)."
    else:
        expl = f"{len(violations)} students violate the rule (attendance rates: {', '.join(map(str, violations['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student is in the 12th grade, then their study time is less than or equal to 8.4 hours per week."""
    condition = (df['grade_level'] == 12) & (df['study_hours_week'] > 8.4)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = f"All 12th graders have study time <= 8.4 hours/week ({len(df[df['grade_level'] == 12])} such students)."
    else:
        expl = f"{len(violations)} 12th graders violate the rule (study times: {', '.join(map(str, violations['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students have an attendance rate greater than 90."""
    total = len(df)
    condition = df['attendance_rate'] > 90
    count = df[condition].shape[0]
    truth = count > total / 2
    if truth:
        expl = f"More than half of students ({count}/{total}) have attendance rate > 90."
    else:
        expl = f"Less than or equal to half of students ({count}/{total}) have attendance rate > 90."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a test score less than 80 have a study time less than 8 hours per week."""
    condition = (df['test_score'] < 80) & (df['study_hours_week'] >= 8)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = f"All students with test score < 80 have study time < 8 hours/week ({len(df[df['test_score'] < 80])} such students)."
    else:
        expl = f"{len(violations)} students violate the rule (test scores: {', '.join(map(str, violations['test_score'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is in the 11th grade, then their test score is greater than or equal to 81."""
    condition = (df['grade_level'] == 11) & (df['test_score'] < 81)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = f"All 11th graders have test score >= 81 ({len(df[df['grade_level'] == 11])} such students)."
    else:
        expl = f"{len(violations)} 11th graders violate the rule (test scores: {', '.join(map(str, violations['test_score'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student with a study time less than 4 hours per week who is a club member."""
    condition = (df['study_hours_week'] < 4) & (df['club_member'] == 'yes')
    found = df[condition]
    truth = len(found) > 0
    if truth:
        expl = f"Found {len(found)} student(s) with study time < 4 hours/week who are club members."
    else:
        expl = "No student with study time < 4 hours/week is a club member."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All students with a test score greater than or equal to 97 have a grade level less than or equal to 10."""
    condition = (df['test_score'] >= 97) & (df['grade_level'] > 10)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = f"All students with test score >= 97 have grade level <= 10 ({len(df[df['test_score'] >= 97])} such students)."
    else:
        expl = f"{len(violations)} students violate the rule (grade levels: {', '.join(map(str, violations['grade_level'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study time greater than 10 hours per week, then they are not a club member."""
    condition = (df['study_hours_week'] > 10) & (df['club_member'] == 'yes')
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = f"All students with study time > 10 hours/week are not club members ({len(df[df['study_hours_week'] > 10])} such students)."
    else:
        expl = f"{len(violations)} students violate the rule (study times: {', '.join(map(str, violations['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most students have a study time less than 10 hours per week."""
    total = len(df)
    condition = df['study_hours_week'] < 10
    count = df[condition].shape[0]
    truth = count > total / 2
    if truth:
        expl = f"More than half of students ({count}/{total}) have study time < 10 hours/week."
    else:
        expl = f"Less than or equal to half of students ({count}/{total}) have study time < 10 hours/week."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All students with an attendance rate greater than 96 have a test score greater than or equal to 84."""
    condition = (df['attendance_rate'] > 96) & (df['test_score'] < 84)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = f"All students with attendance rate > 96 have test score >= 84 ({len(df[df['attendance_rate'] > 96])} such students)."
    else:
        expl = f"{len(violations)} students violate the rule (attendance rates: {', '.join(map(str, violations['attendance_rate'].tolist()))})."
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
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()