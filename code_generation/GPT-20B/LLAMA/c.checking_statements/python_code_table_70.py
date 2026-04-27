import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 12 have a test score greater than or equal to 68."""
    grade12 = df[df["grade_level"] == 12]
    if grade12.empty:
        return True, "No 12th grade students to evaluate."
    truth = (grade12["test_score"] >= 68).all()
    if truth:
        return True, f"All {len(grade12)} 12th grade students have test scores >= 68."
    viol = grade12[grade12["test_score"] < 68]
    return False, f"{len(viol)} 12th grade students violate the rule (scores: {', '.join(map(str, viol['test_score']))})."

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is greater than or equal to 90."""
    club = df[df["club_member"]]
    if club.empty:
        return True, "No club members to evaluate."
    truth = (club["attendance_rate"] >= 90).all()
    if truth:
        return True, f"All {len(club)} club members have attendance rate >= 90."
    viol = club[club["attendance_rate"] < 90]
    return False, f"{len(viol)} club members violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate']))})."

def stmt_3(df: pd.DataFrame):
    """3. All students with a study time of less than 6 hours per week have a test score less than 70."""
    low_study = df[df["study_hours_week"] < 6]
    if low_study.empty:
        return True, "No students with study time < 6 hours to evaluate."
    truth = (low_study["test_score"] < 70).all()
    if truth:
        return True, f"All {len(low_study)} students with study time < 6 hours have test scores < 70."
    viol = low_study[low_study["test_score"] >= 70]
    return False, f"{len(viol)} students violate the rule (test scores: {', '.join(map(str, viol['test_score']))})."

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one student in the 9th grade with a test score greater than 85."""
    exists = ((df["grade_level"] == 9) & (df["test_score"] > 85)).any()
    if exists:
        return True, "At least one 9th grade student has a test score > 85."
    return False, "No 9th grade student has a test score > 85."

def stmt_5(df: pd.DataFrame):
    """5. If a student is in the 11th grade, then their study time is less than 10 hours per week."""
    grade11 = df[df["grade_level"] == 11]
    if grade11.empty:
        return True, "No 11th grade students to evaluate."
    truth = (grade11["study_hours_week"] < 10).all()
    if truth:
        return True, f"All {len(grade11)} 11th grade students have study time < 10 hours."
    viol = grade11[grade11["study_hours_week"] >= 10]
    return False, f"{len(viol)} 11th grade students violate the rule (study times: {', '.join(map(str, viol['study_hours_week']))})."

def stmt_6(df: pd.DataFrame):
    """6. All students with an attendance rate greater than 95 have a test score greater than 60."""
    high_att = df[df["attendance_rate"] > 95]
    if high_att.empty:
        return True, "No students with attendance rate > 95 to evaluate."
    truth = (high_att["test_score"] > 60).all()
    if truth:
        return True, f"All {len(high_att)} students with attendance rate > 95 have test scores > 60."
    viol = high_att[high_att["test_score"] <= 60]
    return False, f"{len(viol)} students violate the rule (test scores: {', '.join(map(str, viol['test_score']))})."

def stmt_7(df: pd.DataFrame):
    """7. Most students have an attendance rate greater than 90."""
    total = len(df)
    if total == 0:
        return True, "No students to evaluate."
    count = (df["attendance_rate"] > 90).sum()
    truth = count > total / 2
    if truth:
        return True, f"{count} out of {total} students have attendance rate > 90."
    return False, f"Only {count} out of {total} students have attendance rate > 90."

def stmt_8(df: pd.DataFrame):
    """8. If a student is not a club member, then their test score is greater than 70."""
    non_club = df[~df["club_member"]]
    if non_club.empty:
        return True, "No non-club members to evaluate."
    truth = (non_club["test_score"] > 70).all()
    if truth:
        return True, f"All {len(non_club)} non-club members have test scores > 70."
    viol = non_club[non_club["test_score"] <= 70]
    return False, f"{len(viol)} non-club members violate the rule (test scores: {', '.join(map(str, viol['test_score']))})."

def stmt_9(df: pd.DataFrame):
    """9. All students with a study time of greater than 9 hours per week have a grade level of 9 or 11."""
    high_study = df[df["study_hours_week"] > 9]
    if high_study.empty:
        return True, "No students with study time > 9 hours to evaluate."
    truth = high_study["grade_level"].isin([9, 11]).all()
    if truth:
        return True, f"All {len(high_study)} students with study time > 9 hours have grade level 9 or 11."
    viol = high_study[~high_study["grade_level"].isin([9, 11])]
    return False, f"{len(viol)} students violate the rule (grade levels: {', '.join(map(str, viol['grade_level']))})."

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one student in the 12th grade with a study time of less than 7 hours per week."""
    exists = ((df["grade_level"] == 12) & (df["study_hours_week"] < 7)).any()
    if exists:
        return True, "At least one 12th grade student has study time < 7 hours."
    return False, "No 12th grade student has study time < 7 hours."

def stmt_11(df: pd.DataFrame):
    """11. All students with a test score greater than 85 have a grade level of 9 or 12."""
    high_score = df[df["test_score"] > 85]
    if high_score.empty:
        return True, "No students with test score > 85 to evaluate."
    truth = high_score["grade_level"].isin([9, 12]).all()
    if truth:
        return True, f"All {len(high_score)} students with test score > 85 have grade level 9 or 12."
    viol = high_score[~high_score["grade_level"].isin([9, 12])]
    return False, f"{len(viol)} students violate the rule (grade levels: {', '.join(map(str, viol['grade_level']))})."

def stmt_12(df: pd.DataFrame):
    """12. If a student has a study time of less than 5 hours per week, then they are not a club member."""
    low_study = df[df["study_hours_week"] < 5]
    if low_study.empty:
        return True, "No students with study time < 5 hours to evaluate."
    truth = (~low_study["club_member"]).all()
    if truth:
        return True, f"All {len(low_study)} students with study time < 5 hours are not club members."
    viol = low_study[low_study["club_member"]]
    return False, f"{len(viol)} students violate the rule (club members: {', '.join(map(str, viol['student_id']))})."

def stmt_13(df: pd.DataFrame):
    """13. Most students who are club members have a test score greater than 65."""
    club = df[df["club_member"]]
    total = len(club)
    if total == 0:
        return True, "No club members to evaluate."
    count = (club["test_score"] > 65).sum()
    truth = count > total / 2
    if truth:
        return True, f"{count} out of {total} club members have test scores > 65."
    return False, f"Only {count} out of {total} club members have test scores > 65."

def stmt_14(df: pd.DataFrame):
    """14. All students with an attendance rate greater than 96 have a study time of greater than 3 hours per week."""
    high_att = df[df["attendance_rate"] > 96]
    if high_att.empty:
        return True, "No students with attendance rate > 96 to evaluate."
    truth = (high_att["study_hours_week"] > 3).all()
    if truth:
        return True, f"All {len(high_att)} students with attendance rate > 96 have study time > 3 hours."
    viol = high_att[high_att["study_hours_week"] <= 3]
    return False, f"{len(viol)} students violate the rule (study times: {', '.join(map(str, viol['study_hours_week']))})."

def stmt_15(df: pd.DataFrame):
    """15. If a student is in the 10th grade, then their test score is greater than 70."""
    grade10 = df[df["grade_level"] == 10]
    if grade10.empty:
        return True, "No 10th grade students to evaluate."
    truth = (grade10["test_score"] > 70).all()
    if truth:
        return True, f"All {len(grade10)} 10th grade students have test scores > 70."
    viol = grade10[grade10["test_score"] <= 70]
    return False, f"{len(viol)} 10th grade students violate the rule (test scores: {', '.join(map(str, viol['test_score']))})."

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one student in the 11th grade with a test score greater than 90."""
    exists = ((df["grade_level"] == 11) & (df["test_score"] > 90)).any()
    if exists:
        return True, "At least one 11th grade student has a test score > 90."
    return False, "No 11th grade student has a test score > 90."

def stmt_17(df: pd.DataFrame):
    """17. All students with a study time of greater than 10 hours per week have a grade level of 9."""
    high_study = df[df["study_hours_week"] > 10]
    if high_study.empty:
        return True, "No students with study time > 10 hours to evaluate."
    truth = (high_study["grade_level"] == 9).all()
    if truth:
        return True, f"All {len(high_study)} students with study time > 10 hours have grade level 9."
    viol = high_study[high_study["grade_level"]!= 9]
    return False, f"{len(viol)} students violate the rule (grade levels: {', '.join(map(str, viol['grade_level']))})."

def stmt_18(df: pd.DataFrame):
    """18. If a student has a test score of less than 70, then they are not in the 12th grade."""
    low_score = df[df["test_score"] < 70]
    if low_score.empty:
        return True, "No students with test score < 70 to evaluate."
    truth = (low_score["grade_level"]!= 12).all()
    if truth:
        return True, f"All {len(low_score)} students with test score < 70 are not in 12th grade."
    viol = low_score[low_score["grade_level"] == 12]
    return False, f"{len(viol)} students violate the rule (student IDs: {', '.join(map(str, viol['student_id']))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_70.csv")

    # Convert numeric columns
    numeric_cols = ["grade_level", "study_hours_week", "attendance_rate", "test_score"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert club_member to boolean
    df["club_member"] = df["club_member"].map({"yes": True, "no": False})

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()