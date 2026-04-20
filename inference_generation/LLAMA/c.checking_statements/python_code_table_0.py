import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students who are club members have a test score above 70."""
    club_members = df[df["club_member"] == True]
    condition = club_members["test_score"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(club_members)} club members have a test score above 70."
    else:
        viol = club_members[~condition]
        expl = f"{len(viol)} club members violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. There exists at least one student in each grade level who is not a club member."""
    non_club_members = df[df["club_member"] == False]
    truth = non_club_members["grade_level"].nunique() == df["grade_level"].nunique()
    if truth:
        expl = f"There is at least one non-club member in each of the {df['grade_level'].nunique()} grade levels."
    else:
        viol = df["grade_level"].unique()[~non_club_members["grade_level"].isin(df["grade_level"].unique())]
        expl = f"No non-club members found in grade levels {', '.join(map(str, viol))}."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Most students in grade 12 have an attendance rate above 90."""
    grade_12 = df[df["grade_level"] == 12]
    condition = grade_12["attendance_rate"] > 90
    truth = condition.mean() > 0.5
    if truth:
        expl = f"{condition.sum()} out of {len(grade_12)} students in grade 12 have an attendance rate above 90."
    else:
        viol = grade_12[~condition]
        expl = f"{len(viol)} out of {len(grade_12)} students in grade 12 have an attendance rate of 90 or below."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a student studies more than 8 hours a week, then they have a test score above 80."""
    study_more_than_8 = df[df["study_hours_week"] > 8]
    condition = study_more_than_8["test_score"] > 80
    truth = condition.all()
    if truth:
        expl = f"All {len(study_more_than_8)} students who study more than 8 hours have a test score above 80."
    else:
        viol = study_more_than_8[~condition]
        expl = f"{len(viol)} students who study more than 8 hours violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All students with an attendance rate above 95 are club members."""
    attendance_above_95 = df[df["attendance_rate"] > 95]
    condition = attendance_above_95["club_member"] == True
    truth = condition.all()
    if truth:
        expl = f"All {len(attendance_above_95)} students with an attendance rate above 95 are club members."
    else:
        viol = attendance_above_95[~condition]
        expl = f"{len(viol)} students with an attendance rate above 95 are not club members."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. There exists at least one student in grade 9 who studies more than 10 hours a week."""
    grade_9 = df[df["grade_level"] == 9]
    condition = grade_9["study_hours_week"] > 10
    truth = condition.any()
    if truth:
        expl = f"There is at least one student in grade 9 who studies more than 10 hours a week."
    else:
        expl = f"No students in grade 9 study more than 10 hours a week."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most students who study more than 7 hours a week have a test score above 80."""
    study_more_than_7 = df[df["study_hours_week"] > 7]
    condition = study_more_than_7["test_score"] > 80
    truth = condition.mean() > 0.5
    if truth:
        expl = f"{condition.sum()} out of {len(study_more_than_7)} students who study more than 7 hours have a test score above 80."
    else:
        viol = study_more_than_7[~condition]
        expl = f"{len(viol)} out of {len(study_more_than_7)} students who study more than 7 hours have a test score of 80 or below."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All students with a test score above 90 are club members."""
    test_score_above_90 = df[df["test_score"] > 90]
    condition = test_score_above_90["club_member"] == True
    truth = condition.all()
    if truth:
        expl = f"All {len(test_score_above_90)} students with a test score above 90 are club members."
    else:
        viol = test_score_above_90[~condition]
        expl = f"{len(viol)} students with a test score above 90 are not club members."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_0.csv")
    df["study_hours_week"] = pd.to_numeric(df["study_hours_week"], errors="coerce")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()