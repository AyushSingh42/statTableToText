

import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All club members with attendance rates above 95% have test scores of at least 90."""
    club_high_att = df[(df['club_member']) & (df['attendance_rate'] > 95)]
    condition = club_high_att['test_score'] >= 90
    truth = condition.all() if not club_high_att.empty else True
    if truth:
        expl = f"All {len(club_high_att)} club members with attendance >95% have test scores >=90."
    else:
        viol = club_high_att[~condition]
        expl = f"{len(viol)} violations found. Example scores: {', '.join(map(str, viol['test_score'].tolist()))}"
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Students who are not club members and study fewer than 5 hours per week have test scores below 75."""
    non_club_low_study = df[(~df['club_member']) & (df['study_hours_week'] < 5)]
    condition = non_club_low_study['test_score'] < 75
    truth = condition.all() if not non_club_low_study.empty else True
    if truth:
        expl = f"All {len(non_club_low_study)} non-club students with <5 study hours have scores <75."
    else:
        viol = non_club_low_study[~condition]
        expl = f"{len(viol)} violations found. Example scores: {', '.join(map(str, viol['test_score'].tolist()))}"
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every club member in grade 10 has a test score higher than any non-club member in the same grade."""
    grade_10 = df[df['grade_level'] == 10]
    club_10 = grade_10[grade_10['club_member']]['test_score']
    non_club_10 = grade_10[~grade_10['club_member']]['test_score']
    if club_10.empty or non_club_10.empty:
        truth = True
        expl = "No club or non-club members in grade 10 to compare."
    else:
        min_club = club_10.min()
        max_non_club = non_club_10.max()
        truth = min_club > max_non_club
        if truth:
            expl = f"Minimum club score ({min_club}) exceeds maximum non-club score ({max_non_club})."
        else:
            expl = f"Club member has score {min_club} which is not higher than non-club's max {max_non_club}."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a student is in grade 11 and studies more than 7 hours per week, their test score is at least 82."""
    grade_11_high_study = df[(df['grade_level'] == 11) & (df['study_hours_week'] > 7)]
    condition = grade_11_high_study['test_score'] >= 82
    truth = condition.all() if not grade_11_high_study.empty else True
    if truth:
        expl = f"All {len(grade_11_high_study)} grade 11 students with >7 study hours have scores >=82."
    else:
        viol = grade_11_high_study[~condition]
        expl = f"{len(viol)} violations found. Example scores: {', '.join(map(str, viol['test_score'].tolist()))}"
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All club members have attendance rates above 89%."""
    club_members = df[df['club_member']]
    condition = club_members['attendance_rate'] > 89
    truth = condition.all() if not club_members.empty else True
    if truth:
        expl = f"All {len(club_members)} club members have attendance rates above 89%."
    else:
        viol = club_members[~condition]
        expl = f"{len(viol)} violations found. Example attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))}"
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Students who are club members and study more than 9 hours per week have test scores exceeding 90."""
    club_high_study = df[(df['club_member']) & (df['study_hours_week'] > 9)]
    condition = club_high_study['test_score'] > 90
    truth = condition.all() if not club_high_study.empty else True
    if truth:
        expl = f"All {len(club_high_study)} club members with >9 study hours have scores >90."
    else:
        viol = club_high_study[~condition]
        expl = f"{len(viol)} violations found. Example scores: {', '.join(map(str, viol['test_score'].tolist()))}"
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. In grade 12, students who study more than 8 hours per week have test scores of at least 87."""
    grade_12_high_study = df[(df['grade_level'] == 12) & (df['study_hours_week'] > 8)]
    condition = grade_12_high_study['test_score'] >= 87
    truth = condition.all() if not grade_12_high_study.empty else True
    if truth:
        expl = f"All {len(grade_12_high_study)} grade 12 students with >8 study hours have scores >=87."
    else:
        viol = grade_12_high_study[~condition]
        expl = f"{len(viol)} violations found. Example scores: {', '.join(map(str, viol['test_score'].tolist()))}"
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Students in grade 9 who are club members have higher test scores than non-club members in the same grade."""
    grade_9 = df[df['grade_level'] == 9]
    club_9 = grade_9[grade_9['club_member']]['test_score']
    non_club_9 = grade_9[~grade_9['club_member']]['test_score']
    if club_9.empty or non_club_9.empty:
        truth = True
        expl = "No club or non-club members in grade 9 to compare."
    else:
        min_club = club_9.min()
        max_non_club = non_club_9.max()
        truth = min_club > max_non_club
        if truth:
            expl = f"Minimum club score ({min_club}) exceeds maximum non-club score ({max_non_club})."
        else:
            expl = f"Club member has score {min_club} which is not higher than non-club's max {max_non_club}."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a student is in grade 10 and studies more than 8 hours per week, their test score is above 85."""
    grade_10_high_study = df[(df['grade_level'] == 10) & (df['study_hours_week'] > 8)]
    condition = grade_10_high_study['test_score'] > 85
    truth = condition.all() if not grade_10_high_study.empty else True
    if truth:
        expl = f"All {len(grade_10_high_study)} grade 10 students with >8 study hours have scores >85."
    else:
        viol = grade_10_high_study[~condition]
        expl = f"{len(viol)} violations found. Example scores: {', '.join(map(str, viol['test_score'].tolist()))}"
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All students who study more than 10 hours per week are club members."""
    long_study = df[df['study_hours_week'] > 10]
    condition = long_study['club_member']
    truth = condition.all() if not long_study.empty else True
    if truth:
        expl = f"All {len(long_study)} students studying >10 hours are club members."
    else:
        viol = long_study[~condition]
        expl = f"{len(viol)} violations found. Example student IDs: {', '.join(map(str, viol['student_id'].tolist()))}"
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Students who are club members and have study hours between 4–6 hours have test scores below 80."""
    club_mid_study = df[(df['club_member']) & (df['study_hours_week'].between(4, 6, inclusive=True))]
    condition = club_mid_study['test_score'] < 80
    truth = condition.all() if not club_mid_study.empty else True
    if truth:
        expl = f"All {len(club_mid_study)} club members with 4–6 study hours have scores <80."
    else:
        viol = club_mid_study[~condition]
        expl = f"{len(viol)} violations found. Example scores: {', '.join(map(str, viol['test_score'].tolist()))}"
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Students in grade 12 with attendance rates above 95% are non-club members."""
    grade_12_high_att = df[(df['grade_level'] == 12) & (df['attendance_rate'] > 95)]
    condition = ~grade_12_high_att['club_member']
    truth = condition.all() if not grade_12_high_att.empty else True
    if truth:
        expl = f"All {len(grade_12_high_att)} grade 12 students with attendance >95% are non-club members."
    else:
        viol = grade_12_high_att[~condition]
        expl = f"{len(viol)} violations found. Example student IDs: {', '.join(map(str, viol['student_id'].tolist()))}"
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a student is a club member and has an attendance rate above 95%, they must be in grade 9, 11, or 12."""
    high_att_club = df[(df['club_member']) & (df['attendance_rate'] > 95)]
    valid_grades = high_att_club['grade_level'].isin([9, 11, 12])
    truth = valid_grades.all() if not high_att_club.empty else True
    if truth:
        expl = f"All {len(high_att_club)} club members with attendance >95% are in grades 9, 11, or 12."
    else:
        viol = high_att_club[~valid_grades]
        expl = f"{len(viol)} violations found. Invalid grades: {', '.join(map(str, viol['grade_level'].tolist()))}"
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All grade 10 students who study more than 8 hours per week are club members."""
    grade_10_high_study = df[(df['grade_level'] == 10) & (df['study_hours_week'] > 8)]
    condition = grade_10_high_study['club_member']
    truth = condition.all() if not grade_10_high_study.empty else True
    if truth:
        expl = f"All {len(grade_10_high_study)} grade 10 students with >8 study hours are club members."
    else:
        viol = grade_10_high_study[~condition]
        expl = f"{len(viol)} violations found. Example student IDs: {', '.join(map(str, viol['student_id'].tolist()))}"
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Students who are club members and have attendance rates between 90–95% have test scores above 80."""
    club_mid_att = df[(df['club_member']) & (df['attendance_rate'].between(90, 95, inclusive=True))]
    condition = club_mid_att['test_score'] > 80
    truth = condition.all() if not club_mid_att.empty else True
    if truth:
        expl = f"All {len(club_mid_att)} club members with attendance 90–95% have scores >80."
    else:
        viol = club_mid_att[~condition]
        expl = f"{len(viol)} violations found. Example scores: {', '.join(map(str, viol['test_score'].tolist()))}"
    return truth, expl

def main():
    df = pd.read_csv("tables/table_0.csv")
    for col in ['grade_level','study_hours_week', 'attendance_rate', 'test_score']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df['club_member'] = df['club_member'].astype(bool)
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
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()