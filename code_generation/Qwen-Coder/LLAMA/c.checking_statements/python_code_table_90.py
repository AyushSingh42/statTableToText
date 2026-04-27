import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 10 have a test score less than 80, except for one student with a test score of 91."""
    grade_10 = df[df["grade_level"] == 10]
    if len(grade_10) == 0:
        return True, "No students in grade 10."
    scores = grade_10["test_score"]
    # Count how many are >= 80
    count_ge_80 = (scores >= 80).sum()
    # Only one exception allowed (score 91)
    if count_ge_80 == 1 and (scores == 91).any():
        return True, "One student with grade 10 has score 91, others < 80."
    elif count_ge_80 == 0:
        return True, "All students with grade 10 have scores < 80."
    else:
        return False, f"{count_ge_80} students with grade 10 have score >= 80."

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is greater than or equal to 84.8."""
    club_members = df[df["club_member"] == "yes"]
    if len(club_members) == 0:
        return True, "No club members."
    condition = club_members["attendance_rate"] >= 84.8
    truth = condition.all()
    if truth:
        expl = f"All {len(club_members)} club members have attendance >= 84.8."
    else:
        viol = club_members[~condition]
        expl = f"{len(viol)} club members violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in grade level 12 who has a study hours per week greater than 9."""
    grade_12 = df[df["grade_level"] == 12]
    if len(grade_12) == 0:
        return False, "No students in grade 12."
    high_study = grade_12[grade_12["study_hours_week"] > 9]
    truth = len(high_study) > 0
    if truth:
        expl = f"{len(high_study)} student(s) in grade 12 have study hours > 9."
    else:
        expl = "No students in grade 12 have study hours > 9."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All students with a study hours per week less than 5 have a test score less than 80."""
    low_study = df[df["study_hours_week"] < 5]
    if len(low_study) == 0:
        return True, "No students with study hours < 5."
    condition = low_study["test_score"] < 80
    truth = condition.all()
    if truth:
        expl = f"All {len(low_study)} students with study hours < 5 have test scores < 80."
    else:
        viol = low_study[~condition]
        expl = f"{len(viol)} students with study hours < 5 have test score >= 80 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student is in grade level 10, then their attendance rate is greater than or equal to 84.8."""
    grade_10 = df[df["grade_level"] == 10]
    if len(grade_10) == 0:
        return True, "No students in grade 10."
    condition = grade_10["attendance_rate"] >= 84.8
    truth = condition.all()
    if truth:
        expl = f"All {len(grade_10)} students in grade 10 have attendance >= 84.8."
    else:
        viol = grade_10[~condition]
        expl = f"{len(viol)} students in grade 10 have attendance < 84.8 (rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students in the table have an attendance rate greater than 86."""
    total = len(df)
    if total == 0:
        return False, "No students in dataset."
    above_86 = (df["attendance_rate"] > 86).sum()
    truth = above_86 > total / 2
    if truth:
        expl = f"{above_86} out of {total} students have attendance > 86."
    else:
        expl = f"{above_86} out of {total} students have attendance > 86 (less than half)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. There exists at least one student in grade level 12 who has a test score greater than 90."""
    grade_12 = df[df["grade_level"] == 12]
    if len(grade_12) == 0:
        return False, "No students in grade 12."
    high_score = grade_12[grade_12["test_score"] > 90]
    truth = len(high_score) > 0
    if truth:
        expl = f"{len(high_score)} student(s) in grade 12 have test score > 90."
    else:
        expl = "No students in grade 12 have test score > 90."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All students with a test score greater than 90 have a grade level of 11 or 12."""
    high_score = df[df["test_score"] > 90]
    if len(high_score) == 0:
        return True, "No students with test score > 90."
    valid_grade = high_score["grade_level"].isin([11, 12])
    truth = valid_grade.all()
    if truth:
        expl = f"All {len(high_score)} students with test score > 90 have grade level 11 or 12."
    else:
        viol = high_score[~valid_grade]
        expl = f"{len(viol)} students with test score > 90 have invalid grade levels ({', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a student is a club member, then their test score is less than or equal to 92."""
    club_members = df[df["club_member"] == "yes"]
    if len(club_members) == 0:
        return True, "No club members."
    condition = club_members["test_score"] <= 92
    truth = condition.all()
    if truth:
        expl = f"All {len(club_members)} club members have test score <= 92."
    else:
        viol = club_members[~condition]
        expl = f"{len(viol)} club members violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All students with a study hours per week greater than 9 have a grade level of 12."""
    high_study = df[df["study_hours_week"] > 9]
    if len(high_study) == 0:
        return True, "No students with study hours > 9."
    valid_grade = high_study["grade_level"] == 12
    truth = valid_grade.all()
    if truth:
        expl = f"All {len(high_study)} students with study hours > 9 have grade level 12."
    else:
        viol = high_study[~valid_grade]
        expl = f"{len(viol)} students with study hours > 9 have invalid grade levels ({', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Most students in the table have a study hours per week less than 7."""
    total = len(df)
    if total == 0:
        return False, "No students in dataset."
    below_7 = (df["study_hours_week"] < 7).sum()
    truth = below_7 > total / 2
    if truth:
        expl = f"{below_7} out of {total} students have study hours < 7."
    else:
        expl = f"{below_7} out of {total} students have study hours < 7 (less than half)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. There exists at least one student in grade level 10 who has a test score greater than 75 and is a club member."""
    grade_10 = df[(df["grade_level"] == 10) & (df["club_member"] == "yes")]
    if len(grade_10) == 0:
        return False, "No students in grade 10 who are club members."
    high_score = grade_10[grade_10["test_score"] > 75]
    truth = len(high_score) > 0
    if truth:
        expl = f"{len(high_score)} student(s) in grade 10 are club members with test score > 75."
    else:
        expl = "No students in grade 10 who are club members have test score > 75."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All students with an attendance rate greater than 96 have a grade level of 12."""
    high_attendance = df[df["attendance_rate"] > 96]
    if len(high_attendance) == 0:
        return True, "No students with attendance > 96."
    valid_grade = high_attendance["grade_level"] == 12
    truth = valid_grade.all()
    if truth:
        expl = f"All {len(high_attendance)} students with attendance > 96 have grade level 12."
    else:
        viol = high_attendance[~valid_grade]
        expl = f"{len(viol)} students with attendance > 96 have invalid grade levels ({', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a student is in grade level 9, then their test score is less than 80."""
    grade_9 = df[df["grade_level"] == 9]
    if len(grade_9) == 0:
        return True, "No students in grade 9."
    condition = grade_9["test_score"] < 80
    truth = condition.all()
    if truth:
        expl = f"All {len(grade_9)} students in grade 9 have test score < 80."
    else:
        viol = grade_9[~condition]
        expl = f"{len(viol)} students in grade 9 have test score >= 80 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All students with a test score less than 70 have a grade level of 12."""
    low_score = df[df["test_score"] < 70]
    if len(low_score) == 0:
        return True, "No students with test score < 70."
    valid_grade = low_score["grade_level"] == 12
    truth = valid_grade.all()
    if truth:
        expl = f"All {len(low_score)} students with test score < 70 have grade level 12."
    else:
        viol = low_score[~valid_grade]
        expl = f"{len(viol)} students with test score < 70 have invalid grade levels ({', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one student in grade level 11 who has a test score greater than 80 and is not a club member."""
    grade_11 = df[(df["grade_level"] == 11) & (df["club_member"] == "no")]
    if len(grade_11) == 0:
        return False, "No students in grade 11 who are not club members."
    high_score = grade_11[grade_11["test_score"] > 80]
    truth = len(high_score) > 0
    if truth:
        expl = f"{len(high_score)} student(s) in grade 11 are not club members with test score > 80."
    else:
        expl = "No students in grade 11 who are not club members have test score > 80."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_90.csv")

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