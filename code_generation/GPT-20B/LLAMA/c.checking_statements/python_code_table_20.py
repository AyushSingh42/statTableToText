import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 12 have a test score greater than or equal to 75."""
    subset = df[df["grade_level"] == 12]
    condition = subset["test_score"] >= 75
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with grade 12 have test scores >= 75."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students with grade 12 violate the rule (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is greater than or equal to 90."""
    subset = df[df["club_member"] == "yes"]
    condition = subset["attendance_rate"] >= 90
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} club members have attendance >= 90."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} club members violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student with a study hours per week greater than 11 who is not a club member."""
    exists = ((df["study_hours_week"] > 11) & (df["club_member"]!= "yes")).any()
    if exists:
        count = df[(df["study_hours_week"] > 11) & (df["club_member"]!= "yes")].shape[0]
        expl = f"{count} student(s) satisfy the condition."
    else:
        expl = "No student satisfies the condition."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All students with a study hours per week less than 4 have a test score less than 90."""
    subset = df[df["study_hours_week"] < 4]
    condition = subset["test_score"] < 90
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with <4 study hours have test scores < 90."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student has a grade level of 10, then their test score is less than 95."""
    subset = df[df["grade_level"] == 10]
    condition = subset["test_score"] < 95
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with grade 10 have test scores < 95."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students have an attendance rate greater than 90."""
    count = (df["attendance_rate"] > 90).sum()
    truth = count > 0.5 * len(df)
    percent = count / len(df) * 100
    if truth:
        expl = f"{percent:.1f}% of students have attendance > 90."
    else:
        expl = f"Only {percent:.1f}% of students have attendance > 90."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a test score greater than 90 have a grade level greater than or equal to 11."""
    subset = df[df["test_score"] > 90]
    condition = subset["grade_level"] >= 11
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test > 90 have grade >= 11."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (grades: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is not a club member, then their test score is less than 96."""
    subset = df[df["club_member"]!= "yes"]
    condition = subset["test_score"] < 96
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} non‑club members have test scores < 96."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} non‑club members violate the rule (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student with a study hours per week greater than 7 who has a test score less than 80."""
    exists = ((df["study_hours_week"] > 7) & (df["test_score"] < 80)).any()
    if exists:
        count = df[(df["study_hours_week"] > 7) & (df["test_score"] < 80)].shape[0]
        expl = f"{count} student(s) satisfy the condition."
    else:
        expl = "No student satisfies the condition."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All students with a grade level of 9 have a test score less than 90."""
    subset = df[df["grade_level"] == 9]
    condition = subset["test_score"] < 90
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with grade 9 have test scores < 90."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study hours per week greater than 8, then they are not a club member."""
    subset = df[df["study_hours_week"] > 8]
    condition = subset["club_member"]!= "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with >8 study hours are not club members."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (club members: {', '.join(map(str, viol['student_id'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most students who are club members have a test score less than 90."""
    subset = df[df["club_member"] == "yes"]
    if subset.empty:
        truth = True
        expl = "No club members to evaluate."
    else:
        count = (subset["test_score"] < 90).sum()
        truth = count > 0.5 * len(subset)
        percent = count / len(subset) * 100
        if truth:
            expl = f"{percent:.1f}% of club members have test < 90."
        else:
            expl = f"Only {percent:.1f}% of club members have test < 90."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All students with a test score greater than 95 have a study hours per week less than 8."""
    subset = df[df["test_score"] > 95]
    condition = subset["study_hours_week"] < 8
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test > 95 have study hours < 8."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a student has a grade level of 11, then their study hours per week is greater than 8."""
    subset = df[df["grade_level"] == 11]
    condition = subset["study_hours_week"] > 8
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with grade 11 have study hours > 8."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one student with a study hours per week less than 4 who is a club member."""
    exists = ((df["study_hours_week"] < 4) & (df["club_member"] == "yes")).any()
    if exists:
        count = df[(df["study_hours_week"] < 4) & (df["club_member"] == "yes")].shape[0]
        expl = f"{count} student(s) satisfy the condition."
    else:
        expl = "No student satisfies the condition."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. All students with a test score less than 80 have a grade level less than or equal to 10."""
    subset = df[df["test_score"] < 80]
    condition = subset["grade_level"] <= 10
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test < 80 have grade <= 10."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (grades: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a student is a club member, then their grade level is less than or equal to 12."""
    subset = df[df["club_member"] == "yes"]
    condition = subset["grade_level"] <= 12
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} club members have grade <= 12."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} club members violate the rule (grades: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most students who have a study hours per week greater than 7 do not have a test score greater than 90."""
    subset = df[df["study_hours_week"] > 7]
    if subset.empty:
        truth = True
        expl = "No students with >7 study hours to evaluate."
    else:
        count = (subset["test_score"] <= 90).sum()
        truth = count > 0.5 * len(subset)
        percent = count / len(subset) * 100
        if truth:
            expl = f"{percent:.1f}% of students with >7 study hours have test <= 90."
        else:
            expl = f"Only {percent:.1f}% of students with >7 study hours have test <= 90."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_20.csv")

    # Convert numeric columns
    numeric_cols = ["grade_level", "study_hours_week", "attendance_rate", "test_score"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

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