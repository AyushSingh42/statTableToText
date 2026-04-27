import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 9 have a test score less than 95."""
    g9 = df[df["grade_level"] == 9]
    condition = g9["test_score"] < 95
    truth = condition.all()
    if truth:
        expl = f"All {len(g9)} students in grade 9 have test scores < 95."
    else:
        viol = g9[~condition]
        ids = viol["student_id"].tolist()
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)}; scores: {', '.join(map(str, scores))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is greater than 85."""
    club = df[df["club_member"]]
    condition = club["attendance_rate"] > 85
    truth = condition.all()
    if truth:
        expl = f"All {len(club)} club members have attendance > 85."
    else:
        viol = club[~condition]
        ids = viol["student_id"].tolist()
        rates = viol["attendance_rate"].tolist()
        expl = f"{len(viol)} club members violate the rule (IDs: {', '.join(ids)}; rates: {', '.join(map(str, rates))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in grade level 11 who has a test score greater than 95."""
    g11 = df[df["grade_level"] == 11]
    condition = g11["test_score"] > 95
    truth = condition.any()
    if truth:
        viol = g11[condition]
        ids = viol["student_id"].tolist()
        scores = viol["test_score"].tolist()
        expl = f"Found {len(viol)} student(s) in grade 11 with test score > 95 (IDs: {', '.join(ids)}; scores: {', '.join(map(str, scores))})."
    else:
        expl = "No students in grade 11 have test score > 95."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All students with study hours per week greater than 9 have a test score greater than 85."""
    high_hours = df[df["study_hours_week"] > 9]
    condition = high_hours["test_score"] > 85
    truth = condition.all()
    if truth:
        expl = f"All {len(high_hours)} students with >9 study hours have test score > 85."
    else:
        viol = high_hours[~condition]
        ids = viol["student_id"].tolist()
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)}; scores: {', '.join(map(str, scores))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student is in grade level 10, then their study hours per week are greater than 5."""
    g10 = df[df["grade_level"] == 10]
    condition = g10["study_hours_week"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(g10)} students in grade 10 have study hours > 5."
    else:
        viol = g10[~condition]
        ids = viol["student_id"].tolist()
        hours = viol["study_hours_week"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)}; hours: {', '.join(map(str, hours))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students in the table have an attendance rate greater than 90."""
    condition = df["attendance_rate"] > 90
    proportion = condition.mean()
    truth = proportion > 0.5
    percent = round(proportion * 100, 2)
    if truth:
        expl = f"{percent}% of students have attendance > 90."
    else:
        expl = f"{percent}% of students have attendance > 90, which is not a majority."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a test score less than 80 have a grade level greater than 9."""
    low_score = df[df["test_score"] < 80]
    condition = low_score["grade_level"] > 9
    truth = condition.all()
    if truth:
        expl = f"All {len(low_score)} students with test score < 80 have grade level > 9."
    else:
        viol = low_score[~condition]
        ids = viol["student_id"].tolist()
        grades = viol["grade_level"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)}; grades: {', '.join(map(str, grades))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is not a club member, then their test score is less than 90."""
    non_club = df[~df["club_member"]]
    condition = non_club["test_score"] < 90
    truth = condition.all()
    if truth:
        expl = f"All {len(non_club)} non-club members have test score < 90."
    else:
        viol = non_club[~condition]
        ids = viol["student_id"].tolist()
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} non-club members violate the rule (IDs: {', '.join(ids)}; scores: {', '.join(map(str, scores))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student in grade level 9 who has a study hours per week less than 3."""
    g9 = df[df["grade_level"] == 9]
    condition = g9["study_hours_week"] < 3
    truth = condition.any()
    if truth:
        viol = g9[condition]
        ids = viol["student_id"].tolist()
        hours = viol["study_hours_week"].tolist()
        expl = f"Found {len(viol)} student(s) in grade 9 with study hours < 3 (IDs: {', '.join(ids)}; hours: {', '.join(map(str, hours))})."
    else:
        expl = "No students in grade 9 have study hours < 3."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All students with a grade level of 12 have a test score less than 85."""
    g12 = df[df["grade_level"] == 12]
    condition = g12["test_score"] < 85
    truth = condition.all()
    if truth:
        expl = f"All {len(g12)} students in grade 12 have test score < 85."
    else:
        viol = g12[~condition]
        ids = viol["student_id"].tolist()
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)}; scores: {', '.join(map(str, scores))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study hours per week greater than 10, then they are a club member."""
    high_hours = df[df["study_hours_week"] > 10]
    condition = high_hours["club_member"]
    truth = condition.all()
    if truth:
        expl = f"All {len(high_hours)} students with >10 study hours are club members."
    else:
        viol = high_hours[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most students in the table have a study hours per week less than 10."""
    condition = df["study_hours_week"] < 10
    proportion = condition.mean()
    truth = proportion > 0.5
    percent = round(proportion * 100, 2)
    if truth:
        expl = f"{percent}% of students have study hours < 10."
    else:
        expl = f"{percent}% of students have study hours < 10, which is not a majority."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All students with an attendance rate greater than 95 have a grade level greater than 9."""
    high_att = df[df["attendance_rate"] > 95]
    condition = high_att["grade_level"] > 9
    truth = condition.all()
    if truth:
        expl = f"All {len(high_att)} students with attendance > 95 have grade level > 9."
    else:
        viol = high_att[~condition]
        ids = viol["student_id"].tolist()
        grades = viol["grade_level"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)}; grades: {', '.join(map(str, grades))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a student is in grade level 11, then their attendance rate is greater than 92."""
    g11 = df[df["grade_level"] == 11]
    condition = g11["attendance_rate"] > 92
    truth = condition.all()
    if truth:
        expl = f"All {len(g11)} students in grade 11 have attendance > 92."
    else:
        viol = g11[~condition]
        ids = viol["student_id"].tolist()
        rates = viol["attendance_rate"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)}; rates: {', '.join(map(str, rates))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one student in grade level 10 who has a test score greater than 90."""
    g10 = df[df["grade_level"] == 10]
    condition = g10["test_score"] > 90
    truth = condition.any()
    if truth:
        viol = g10[condition]
        ids = viol["student_id"].tolist()
        scores = viol["test_score"].tolist()
        expl = f"Found {len(viol)} student(s) in grade 10 with test score > 90 (IDs: {', '.join(ids)}; scores: {', '.join(map(str, scores))})."
    else:
        expl = "No students in grade 10 have test score > 90."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All students with a test score greater than 95 have a grade level greater than 10."""
    high_score = df[df["test_score"] > 95]
    condition = high_score["grade_level"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(high_score)} students with test score > 95 have grade level > 10."
    else:
        viol = high_score[~condition]
        ids = viol["student_id"].tolist()
        grades = viol["grade_level"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)}; grades: {', '.join(map(str, grades))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_0.csv")

    # Convert numeric columns safely
    numeric_cols = ["grade_level", "study_hours_week", "attendance_rate", "test_score"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert club_member to boolean
    df["club_member"] = df["club_member"].astype(str).str.lower() == "yes"

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()