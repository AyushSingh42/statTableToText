import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a test score greater than or equal to 93 have an attendance rate greater than or equal to 90."""
    condition = (df['test_score'] >= 93)
    filtered = df[condition]
    if filtered.empty:
        truth = True
        expl = "No students with test score >= 93 to check."
    else:
        valid = filtered['attendance_rate'] >= 90
        truth = valid.all()
        if truth:
            expl = f"All {len(filtered)} students with test score >= 93 have attendance rate >= 90."
        else:
            viol = filtered[~valid]
            expl = f"{len(viol)} students violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their test score is greater than or equal to 69."""
    condition = (df['club_member'] == 'yes')
    filtered = df[condition]
    if filtered.empty:
        truth = True
        expl = "No club members to check."
    else:
        valid = filtered['test_score'] >= 69
        truth = valid.all()
        if truth:
            expl = f"All {len(filtered)} club members have test score >= 69."
        else:
            viol = filtered[~valid]
            expl = f"{len(viol)} club members violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in grade level 9 who has a study hours per week greater than or equal to 9.5."""
    condition = (df['grade_level'] == 9) & (df['study_hours_week'] >= 9.5)
    filtered = df[condition]
    truth = not filtered.empty
    if truth:
        expl = f"There is at least one student in grade 9 with study hours >= 9.5 ({filtered.iloc[0]['student_id']})."
    else:
        expl = "No student in grade 9 has study hours >= 9.5."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All students in grade level 12 have a study hours per week less than or equal to 11.5."""
    condition = (df['grade_level'] == 12)
    filtered = df[condition]
    if filtered.empty:
        truth = True
        expl = "No students in grade 12 to check."
    else:
        valid = filtered['study_hours_week'] <= 11.5
        truth = valid.all()
        if truth:
            expl = f"All {len(filtered)} students in grade 12 have study hours <= 11.5."
        else:
            viol = filtered[~valid]
            expl = f"{len(viol)} students in grade 12 violate the rule (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student has a study hours per week less than 3, then their test score is greater than or equal to 97."""
    condition = (df['study_hours_week'] < 3)
    filtered = df[condition]
    if filtered.empty:
        truth = True
        expl = "No students with study hours < 3 to check."
    else:
        valid = filtered['test_score'] >= 97
        truth = valid.all()
        if truth:
            expl = f"All {len(filtered)} students with study hours < 3 have test score >= 97."
        else:
            viol = filtered[~valid]
            expl = f"{len(viol)} students with study hours < 3 violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students in the table have an attendance rate greater than 90."""
    total = len(df)
    condition = df['attendance_rate'] > 90
    count = condition.sum()
    truth = count > total / 2
    expl = f"{count} out of {total} students have attendance rate > 90. {'Most' if truth else 'Not most'} students meet this criteria."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a test score less than 70 have a grade level of 9."""
    condition = (df['test_score'] < 70)
    filtered = df[condition]
    if filtered.empty:
        truth = True
        expl = "No students with test score < 70 to check."
    else:
        valid = filtered['grade_level'] == 9
        truth = valid.all()
        if truth:
            expl = f"All {len(filtered)} students with test score < 70 are in grade 9."
        else:
            viol = filtered[~valid]
            expl = f"{len(viol)} students with test score < 70 are not in grade 9 (grade levels: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is in grade level 10, then their test score is greater than or equal to 83."""
    condition = (df['grade_level'] == 10)
    filtered = df[condition]
    if filtered.empty:
        truth = True
        expl = "No students in grade 10 to check."
    else:
        valid = filtered['test_score'] >= 83
        truth = valid.all()
        if truth:
            expl = f"All {len(filtered)} students in grade 10 have test score >= 83."
        else:
            viol = filtered[~valid]
            expl = f"{len(viol)} students in grade 10 violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student in grade level 9 who has a test score greater than or equal to 97."""
    condition = (df['grade_level'] == 9) & (df['test_score'] >= 97)
    filtered = df[condition]
    truth = not filtered.empty
    if truth:
        expl = f"There is at least one student in grade 9 with test score >= 97 ({filtered.iloc[0]['student_id']})."
    else:
        expl = "No student in grade 9 has test score >= 97."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All students who are club members have a test score greater than or equal to 69."""
    condition = (df['club_member'] == 'yes')
    filtered = df[condition]
    if filtered.empty:
        truth = True
        expl = "No club members to check."
    else:
        valid = filtered['test_score'] >= 69
        truth = valid.all()
        if truth:
            expl = f"All {len(filtered)} club members have test score >= 69."
        else:
            viol = filtered[~valid]
            expl = f"{len(viol)} club members violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study hours per week greater than or equal to 9, then their attendance rate is greater than or equal to 89."""
    condition = (df['study_hours_week'] >= 9)
    filtered = df[condition]
    if filtered.empty:
        truth = True
        expl = "No students with study hours >= 9 to check."
    else:
        valid = filtered['attendance_rate'] >= 89
        truth = valid.all()
        if truth:
            expl = f"All {len(filtered)} students with study hours >= 9 have attendance rate >= 89."
        else:
            viol = filtered[~valid]
            expl = f"{len(viol)} students with study hours >= 9 violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All students in grade level 12 have a test score less than or equal to 92."""
    condition = (df['grade_level'] == 12)
    filtered = df[condition]
    if filtered.empty:
        truth = True
        expl = "No students in grade 12 to check."
    else:
        valid = filtered['test_score'] <= 92
        truth = valid.all()
        if truth:
            expl = f"All {len(filtered)} students in grade 12 have test score <= 92."
        else:
            viol = filtered[~valid]
            expl = f"{len(viol)} students in grade 12 violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most students in the table have a study hours per week less than or equal to 7."""
    total = len(df)
    condition = df['study_hours_week'] <= 7
    count = condition.sum()
    truth = count > total / 2
    expl = f"{count} out of {total} students have study hours <= 7. {'Most' if truth else 'Not most'} students meet this criteria."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_40.csv")

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