import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 9 have a test score less than 95."""
    subset = df[df["grade_level"] == 9]
    condition = subset["test_score"] < 95
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students in grade 9 have test scores < 95."
    else:
        viol = subset[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} students in grade 9 violate the rule (scores: {scores})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is less than 90% or greater than 90.5%."""
    members = df[df["club_member"] == "yes"]
    condition = (members["attendance_rate"] < 90) | (members["attendance_rate"] > 90.5)
    truth = condition.all()
    if truth:
        expl = f"All {len(members)} club members satisfy the attendance condition."
    else:
        viol = members[~condition]
        rates = viol["attendance_rate"].tolist()
        expl = f"{len(viol)} club members violate the rule (attendance rates: {rates})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in grade level 10 who has a study hours per week of less than 6."""
    exists = ((df["grade_level"] == 10) & (df["study_hours_week"] < 6)).any()
    if exists:
        expl = "At least one student in grade 10 has study hours < 6."
    else:
        expl = "No student in grade 10 has study hours < 6."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All students with a study hours per week of 10 or more have a grade level of 10 or 12."""
    subset = df[df["study_hours_week"] >= 10]
    condition = subset["grade_level"].isin([10, 12])
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with study hours ≥ 10 are in grades 10 or 12."
    else:
        viol = subset[~condition]
        grades = viol["grade_level"].tolist()
        expl = f"{len(viol)} students with study hours ≥ 10 violate the rule (grades: {grades})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student has a test score of 89 or more, then their attendance rate is greater than 86%."""
    subset = df[df["test_score"] >= 89]
    condition = subset["attendance_rate"] > 86
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test score ≥ 89 have attendance > 86%."
    else:
        viol = subset[~condition]
        rates = viol["attendance_rate"].tolist()
        expl = f"{len(viol)} students with test score ≥ 89 violate the rule (attendance rates: {rates})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students have a study hours per week of less than 8."""
    total = len(df)
    count = (df["study_hours_week"] < 8).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        expl = f"{count}/{total} students ({proportion:.2%}) have study hours < 8."
    else:
        expl = f"Only {count}/{total} students ({proportion:.2%}) have study hours < 8."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a grade level of 12 have a test score less than 90."""
    subset = df[df["grade_level"] == 12]
    condition = subset["test_score"] < 90
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students in grade 12 have test scores < 90."
    else:
        viol = subset[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} students in grade 12 violate the rule (scores: {scores})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is not a club member, then their test score is less than 96."""
    non_members = df[df["club_member"] == "no"]
    condition = non_members["test_score"] < 96
    truth = condition.all()
    if truth:
        expl = f"All {len(non_members)} non-club members have test scores < 96."
    else:
        viol = non_members[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} non-club members violate the rule (scores: {scores})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student in grade level 9 who has a study hours per week of 8 or more."""
    exists = ((df["grade_level"] == 9) & (df["study_hours_week"] >= 8)).any()
    if exists:
        expl = "At least one student in grade 9 has study hours ≥ 8."
    else:
        expl = "No student in grade 9 has study hours ≥ 8."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All students with a test score of 70 or less have a grade level of 9."""
    subset = df[df["test_score"] <= 70]
    condition = subset["grade_level"] == 9
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test score ≤ 70 are in grade 9."
    else:
        viol = subset[~condition]
        grades = viol["grade_level"].tolist()
        expl = f"{len(viol)} students with test score ≤ 70 violate the rule (grades: {grades})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study hours per week of 6 or more, then their attendance rate is greater than 84%."""
    subset = df[df["study_hours_week"] >= 6]
    condition = subset["attendance_rate"] > 84
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with study hours ≥ 6 have attendance > 84%."
    else:
        viol = subset[~condition]
        rates = viol["attendance_rate"].tolist()
        expl = f"{len(viol)} students with study hours ≥ 6 violate the rule (attendance rates: {rates})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All students with a grade level of 11 have a test score of 83 or more."""
    subset = df[df["grade_level"] == 11]
    condition = subset["test_score"] >= 83
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students in grade 11 have test scores ≥ 83."
    else:
        viol = subset[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} students in grade 11 violate the rule (scores: {scores})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. There exists at least one student who is a club member and has a test score of 72 or less."""
    exists = ((df["club_member"] == "yes") & (df["test_score"] <= 72)).any()
    if exists:
        expl = "At least one club member has a test score ≤ 72."
    else:
        expl = "No club member has a test score ≤ 72."
    return exists, expl

def stmt_14(df: pd.DataFrame):
    """14. All students with a study hours per week of 2.5 or less have a test score of 70 or less."""
    subset = df[df["study_hours_week"] <= 2.5]
    condition = subset["test_score"] <= 70
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with study hours ≤ 2.5 have test scores ≤ 70."
    else:
        viol = subset[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} students with study hours ≤ 2.5 violate the rule (scores: {scores})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a student has a test score of 94 or more, then their study hours per week is 6 or more."""
    subset = df[df["test_score"] >= 94]
    condition = subset["study_hours_week"] >= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test score ≥ 94 have study hours ≥ 6."
    else:
        viol = subset[~condition]
        hours = viol["study_hours_week"].tolist()
        expl = f"{len(viol)} students with test score ≥ 94 violate the rule (study hours: {hours})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. Most students have an attendance rate of 88% or more."""
    total = len(df)
    count = (df["attendance_rate"] >= 88).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        expl = f"{count}/{total} students ({proportion:.2%}) have attendance ≥ 88%."
    else:
        expl = f"Only {count}/{total} students ({proportion:.2%}) have attendance ≥ 88%."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All students with a grade level of 10 have a test score of 69 or more."""
    subset = df[df["grade_level"] == 10]
    condition = subset["test_score"] >= 69
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students in grade 10 have test scores ≥ 69."
    else:
        viol = subset[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} students in grade 10 violate the rule (scores: {scores})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a student is not a club member, then their study hours per week is 6.5 or less."""
    non_members = df[df["club_member"] == "no"]
    condition = non_members["study_hours_week"] <= 6.5
    truth = condition.all()
    if truth:
        expl = f"All {len(non_members)} non-club members have study hours ≤ 6.5."
    else:
        viol = non_members[~condition]
        hours = viol["study_hours_week"].tolist()
        expl = f"{len(viol)} non-club members violate the rule (study hours: {hours})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. There exists at least one student in grade level 12 who has a study hours per week of 9 or more."""
    exists = ((df["grade_level"] == 12) & (df["study_hours_week"] >= 9)).any()
    if exists:
        expl = "At least one student in grade 12 has study hours ≥ 9."
    else:
        expl = "No student in grade 12 has study hours ≥ 9."
    return exists, expl

def stmt_20(df: pd.DataFrame):
    """20. All students with a test score of 96 or more have a grade level of 10."""
    subset = df[df["test_score"] >= 96]
    condition = subset["grade_level"] == 10
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test score ≥ 96 are in grade 10."
    else:
        viol = subset[~condition]
        grades = viol["grade_level"].tolist()
        expl = f"{len(viol)} students with test score ≥ 96 violate the rule (grades: {grades})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. If a student has a study hours per week of 7 or more, then their test score is 82 or more."""
    subset = df[df["study_hours_week"] >= 7]
    condition = subset["test_score"] >= 82
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with study hours ≥ 7 have test scores ≥ 82."
    else:
        viol = subset[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} students with study hours ≥ 7 violate the rule (test scores: {scores})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_80.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col not in ["student_id", "club_member"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Normalize club_member to lowercase
    df["club_member"] = df["club_member"].str.lower()

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
        (21, stmt_21),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()