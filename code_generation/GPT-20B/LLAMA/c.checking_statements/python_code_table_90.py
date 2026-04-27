import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 10 have a test score less than 80, except for one student with a test score of 91."""
    grade10 = df[df["grade_level"] == 10]
    if grade10.empty:
        return False, "No students in grade 10."
    count_91 = grade10[grade10["test_score"] == 91].shape[0]
    others = grade10[(grade10["test_score"] >= 80) & (grade10["test_score"]!= 91)]
    truth = (count_91 == 1) and others.empty
    if truth:
        expl = f"Grade 10 has {grade10.shape[0]} students: 1 with test score 91, all others <80."
    else:
        if count_91!= 1:
            expl = f"Expected exactly one student with test score 91 in grade 10, found {count_91}."
        else:
            viol = others
            expl = f"{viol.shape[0]} grade 10 students violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is greater than or equal to 84.8."""
    club = df[df["club_member"] == "yes"]
    if club.empty:
        return True, "No club members in the data."
    condition = club["attendance_rate"] >= 84.8
    truth = condition.all()
    if truth:
        expl = f"All {club.shape[0]} club members have attendance rate >= 84.8."
    else:
        viol = club[~condition]
        expl = f"{viol.shape[0]} club members violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in grade level 12 who has a study hours per week greater than 9."""
    exists = df[(df["grade_level"] == 12) & (df["study_hours_week"] > 9)].shape[0] > 0
    if exists:
        expl = "At least one grade 12 student has study hours > 9."
    else:
        expl = "No grade 12 student has study hours > 9."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All students with a study hours per week less than 5 have a test score less than 80."""
    low_hours = df[df["study_hours_week"] < 5]
    if low_hours.empty:
        return True, "No students with study hours < 5."
    condition = low_hours["test_score"] < 80
    truth = condition.all()
    if truth:
        expl = f"All {low_hours.shape[0]} students with study hours < 5 have test score < 80."
    else:
        viol = low_hours[~condition]
        expl = f"{viol.shape[0]} students with study hours < 5 violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student is in grade level 10, then their attendance rate is greater than or equal to 84.8."""
    grade10 = df[df["grade_level"] == 10]
    if grade10.empty:
        return True, "No students in grade 10."
    condition = grade10["attendance_rate"] >= 84.8
    truth = condition.all()
    if truth:
        expl = f"All {grade10.shape[0]} grade 10 students have attendance rate >= 84.8."
    else:
        viol = grade10[~condition]
        expl = f"{viol.shape[0]} grade 10 students violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students in the table have an attendance rate greater than 86."""
    total = df.shape[0]
    count = df[df["attendance_rate"] > 86].shape[0]
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} students have attendance rate > 86."
    else:
        expl = f"Only {count} out of {total} students have attendance rate > 86."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. There exists at least one student in grade level 12 who has a test score greater than 90."""
    exists = df[(df["grade_level"] == 12) & (df["test_score"] > 90)].shape[0] > 0
    if exists:
        expl = "At least one grade 12 student has test score > 90."
    else:
        expl = "No grade 12 student has test score > 90."
    return exists, expl

def stmt_8(df: pd.DataFrame):
    """8. All students with a test score greater than 90 have a grade level of 11 or 12."""
    high_score = df[df["test_score"] > 90]
    if high_score.empty:
        return True, "No students with test score > 90."
    condition = high_score["grade_level"].isin([11, 12])
    truth = condition.all()
    if truth:
        expl = f"All {high_score.shape[0]} students with test score > 90 have grade level 11 or 12."
    else:
        viol = high_score[~condition]
        expl = f"{viol.shape[0]} students with test score > 90 violate the rule (grade levels: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a student is a club member, then their test score is less than or equal to 92."""
    club = df[df["club_member"] == "yes"]
    if club.empty:
        return True, "No club members in the data."
    condition = club["test_score"] <= 92
    truth = condition.all()
    if truth:
        expl = f"All {club.shape[0]} club members have test score <= 92."
    else:
        viol = club[~condition]
        expl = f"{viol.shape[0]} club members violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All students with a study hours per week greater than 9 have a grade level of 12."""
    high_hours = df[df["study_hours_week"] > 9]
    if high_hours.empty:
        return True, "No students with study hours > 9."
    condition = high_hours["grade_level"] == 12
    truth = condition.all()
    if truth:
        expl = f"All {high_hours.shape[0]} students with study hours > 9 have grade level 12."
    else:
        viol = high_hours[~condition]
        expl = f"{viol.shape[0]} students with study hours > 9 violate the rule (grade levels: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Most students in the table have a study hours per week less than 7."""
    total = df.shape[0]
    count = df[df["study_hours_week"] < 7].shape[0]
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} students have study hours < 7."
    else:
        expl = f"Only {count} out of {total} students have study hours < 7."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. There exists at least one student in grade level 10 who has a test score greater than 75 and is a club member."""
    exists = df[(df["grade_level"] == 10) & (df["test_score"] > 75) & (df["club_member"] == "yes")].shape[0] > 0
    if exists:
        expl = "At least one grade 10 student has test score > 75 and is a club member."
    else:
        expl = "No grade 10 student has test score > 75 and is a club member."
    return exists, expl

def stmt_13(df: pd.DataFrame):
    """13. All students with an attendance rate greater than 96 have a grade level of 12."""
    high_att = df[df["attendance_rate"] > 96]
    if high_att.empty:
        return True, "No students with attendance rate > 96."
    condition = high_att["grade_level"] == 12
    truth = condition.all()
    if truth:
        expl = f"All {high_att.shape[0]} students with attendance rate > 96 have grade level 12."
    else:
        viol = high_att[~condition]
        expl = f"{viol.shape[0]} students with attendance rate > 96 violate the rule (grade levels: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a student is in grade level 9, then their test score is less than 80."""
    grade9 = df[df["grade_level"] == 9]
    if grade9.empty:
        return True, "No students in grade 9."
    condition = grade9["test_score"] < 80
    truth = condition.all()
    if truth:
        expl = f"All {grade9.shape[0]} grade 9 students have test score < 80."
    else:
        viol = grade9[~condition]
        expl = f"{viol.shape[0]} grade 9 students violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All students with a test score less than 70 have a grade level of 12."""
    low_score = df[df["test_score"] < 70]
    if low_score.empty:
        return True, "No students with test score < 70."
    condition = low_score["grade_level"] == 12
    truth = condition.all()
    if truth:
        expl = f"All {low_score.shape[0]} students with test score < 70 have grade level 12."
    else:
        viol = low_score[~condition]
        expl = f"{viol.shape[0]} students with test score < 70 violate the rule (grade levels: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one student in grade level 11 who has a test score greater than 80 and is not a club member."""
    exists = df[(df["grade_level"] == 11) & (df["test_score"] > 80) & (df["club_member"] == "no")].shape[0] > 0
    if exists:
        expl = "At least one