import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 9 have a test score less than 95."""
    condition = (df['grade_level'] == 9) & (df['test_score'] >= 95)
    truth = not condition.any()
    if truth:
        expl = "No grade 9 student has a test score of 95 or higher."
    else:
        viol = df[condition]
        expl = f"{len(viol)} grade 9 student(s) have a test score of 95 or higher."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is less than 90% or greater than 90.5%."""
    condition = (df['club_member'] == 'yes') & (df['attendance_rate'].between(90, 90.5, inclusive='both'))
    truth = not condition.any()
    if truth:
        expl = "All club members have attendance rates outside the range [90, 90.5]."
    else:
        viol = df[condition]
        expl = f"{len(viol)} club member(s) have attendance rates between 90 and 90.5."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in grade level 10 who has a study hours per week of less than 6."""
    condition = (df['grade_level'] == 10) & (df['study_hours_week'] < 6)
    truth = condition.any()
    if truth:
        expl = "At least one grade 10 student studies less than 6 hours per week."
    else:
        expl = "No grade 10 student studies less than 6 hours per week."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All students with a study hours per week of 10 or more have a grade level of 10 or 12."""
    condition = (df['study_hours_week'] >= 10) & (~df['grade_level'].isin([10, 12]))
    truth = not condition.any()
    if truth:
        expl = "All students studying 10+ hours per week have grade levels 10 or 12."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) study 10+ hours but do not have grade levels 10 or 12."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student has a test score of 89 or more, then their attendance rate is greater than 86%."""
    condition = (df['test_score'] >= 89) & (df['attendance_rate'] <= 86)
    truth = not condition.any()
    if truth:
        expl = "All students with test scores of 89+ have attendance rates > 86%."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) with test scores of 89+ have attendance rates <= 86%."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students have a study hours per week of less than 8."""
    total_students = len(df)
    condition = df['study_hours_week'] >= 8
    count_ge_8 = len(df[condition])
    truth = count_ge_8 < total_students / 2
    if truth:
        expl = f"Less than half ({count_ge_8}/{total_students}) of students study 8 or more hours per week."
    else:
        expl = f"At least half ({count_ge_8}/{total_students}) of students study 8 or more hours per week."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a grade level of 12 have a test score less than 90."""
    condition = (df['grade_level'] == 12) & (df['test_score'] >= 90)
    truth = not condition.any()
    if truth:
        expl = "No grade 12 student has a test score of 90 or higher."
    else:
        viol = df[condition]
        expl = f"{len(viol)} grade 12 student(s) have a test score of 90 or higher."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is not a club member, then their test score is less than 96."""
    condition = (df['club_member'] == 'no') & (df['test_score'] >= 96)
    truth = not condition.any()
    if truth:
        expl = "All non-club members have test scores less than 96."
    else:
        viol = df[condition]
        expl = f"{len(viol)} non-club member(s) have test scores of 96 or higher."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student in grade level 9 who has a study hours per week of 8 or more."""
    condition = (df['grade_level'] == 9) & (df['study_hours_week'] >= 8)
    truth = condition.any()
    if truth:
        expl = "At least one grade 9 student studies 8 or more hours per week."
    else:
        expl = "No grade 9 student studies 8 or more hours per week."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All students with a test score of 70 or less have a grade level of 9."""
    condition = (df['test_score'] <= 70) & (df['grade_level']!= 9)
    truth = not condition.any()
    if truth:
        expl = "All students with test scores of 70 or less have grade level 9."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) with test scores of 70 or less do not have grade level 9."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study hours per week of 6 or more, then their attendance rate is greater than 84%."""
    condition = (df['study_hours_week'] >= 6) & (df['attendance_rate'] <= 84)
    truth = not condition.any()
    if truth:
        expl = "All students studying 6+ hours per week have attendance rates > 84%."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) studying 6+ hours per week have attendance rates <= 84%."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All students with a grade level of 11 have a test score of 83 or more."""
    condition = (df['grade_level'] == 11) & (df['test_score'] < 83)
    truth = not condition.any()
    if truth:
        expl = "All grade 11 students have test scores of 83 or higher."
    else:
        viol = df[condition]
        expl = f"{len(viol)} grade 11 student(s) have test scores below 83."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. There exists at least one student who is a club member and has a test score of 72 or less."""
    condition = (df['club_member'] == 'yes') & (df['test_score'] <= 72)
    truth = condition.any()
    if truth:
        expl = "At least one club member has a test score of 72 or less."
    else:
        expl = "No club member has a test score of 72 or less."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All students with a study hours per week of 2.5 or less have a test score of 70 or less."""
    condition = (df['study_hours_week'] <= 2.5) & (df['test_score'] > 70)
    truth = not condition.any()
    if truth:
        expl = "All students studying 2.5 or fewer hours per week have test scores of 70 or less."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) studying 2.5 or fewer hours per week have test scores > 70."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a student has a test score of 94 or more, then their study hours per week is 6 or more."""
    condition = (df['test_score'] >= 94) & (df['study_hours_week'] < 6)
    truth = not condition.any()
    if truth:
        expl = "All students with test scores of 94+ study 6 or more hours per week."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) with test scores of 94+ study less than 6 hours per week."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. Most students have an attendance rate of 88% or more."""
    total_students = len(df)
    condition = df['attendance_rate'] < 88
    count_lt_88 = len(df[condition])
    truth = count_lt_88 < total_students / 2
    if truth:
        expl = f"Less than half ({count_lt_88}/{total_students}) of students have attendance rates < 88%."
    else:
        expl = f"At least half ({count_lt_88}/{total_students}) of students have attendance rates < 88%."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All students with a grade level of 10 have a test score of 69 or more."""
    condition = (df['grade_level'] == 10) & (df['test_score'] < 69)
    truth = not condition.any()
    if truth:
        expl = "All grade 10 students have test scores of 69 or higher."
    else:
        viol = df[condition]
        expl = f"{len(viol)} grade 10 student(s) have test scores below 69."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a student is not a club member, then their study hours per week is 6.5 or less."""
    condition = (df['club_member'] == 'no') & (df['study_hours_week'] > 6.5)
    truth = not condition.any()
    if truth:
        expl = "All non-club members study 6.5 or fewer hours per week."
    else:
        viol = df[condition]
        expl = f"{len(viol)} non-club member(s) study more than 6.5 hours per week."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. There exists at least one student in grade level 12 who has a study hours per week of 9 or more."""
    condition = (df['grade_level'] == 12) & (df['study_hours_week'] >= 9)
    truth = condition.any()
    if truth:
        expl = "At least one grade 12 student studies 9 or more hours per week."
    else:
        expl = "No grade 12 student studies 9 or more hours per week."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. All students with a test score of 96 or more have a grade level of 10."""
    condition = (df['test_score'] >= 96) & (df['grade_level']!= 10)
    truth = not condition.any()
    if truth:
        expl = "All students with test scores of 96 or higher have grade level 10."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) with test scores of 96+ do not have grade level 10."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. If a student has a study hours per week of 7 or more, then their test score is 82 or more."""
    condition = (df['study_hours_week'] >= 7) & (df['test_score'] < 82)
    truth = not condition.any()
    if truth:
        expl = "All students studying 7+ hours per week have test scores of 82 or higher."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) studying 7+ hours per week have test scores below 82."
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
        (18, stmt_18),
        (19, stmt_19),
        (20, stmt_20),
        (21, stmt_21)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()