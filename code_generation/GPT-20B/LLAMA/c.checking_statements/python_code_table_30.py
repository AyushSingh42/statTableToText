import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 12 have a test score greater than or equal to 65."""
    subset = df[df["grade_level"] == 12]
    condition = subset["test_score"] >= 65
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students in grade 12 have test scores >= 65."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students in grade 12 violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is greater than or equal to 84.2."""
    subset = df[df["club_member"]]
    condition = subset["attendance_rate"] >= 84.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} club members have attendance rate >= 84.2."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} club members violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in grade level 11 who has a test score greater than 90."""
    exists = ((df["grade_level"] == 11) & (df["test_score"] > 90)).any()
    if exists:
        ids = df[(df["grade_level"] == 11) & (df["test_score"] > 90)]["student_id"].tolist()
        expl = f"Students {', '.join(ids)} satisfy the condition."
    else:
        expl = "No student in grade 11 has a test score > 90."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. For all students with study hours per week greater than 9, their test score is greater than or equal to 65."""
    subset = df[df["study_hours_week"] > 9]
    condition = subset["test_score"] >= 65
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with >9 study hours have test score >= 65."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most students in the table have an attendance rate greater than 85."""
    total = len(df)
    count = (df["attendance_rate"] > 85).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        expl = f"{count}/{total} ({proportion:.1%}) students have attendance rate > 85."
    else:
        expl = f"{count}/{total} ({proportion:.1%}) students have attendance rate > 85."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a student is in grade level 9, then their study hours per week are greater than or equal to 5.4."""
    subset = df[df["grade_level"] == 9]
    condition = subset["study_hours_week"] >= 5.4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students in grade 9 have study hours >= 5.4."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students in grade 9 violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a test score greater than 90 have a grade level of 11 or 12."""
    subset = df[df["test_score"] > 90]
    condition = subset["grade_level"].isin([11, 12])
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test score > 90 are in grades 11 or 12."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one student who is not a club member and has a test score greater than 80."""
    exists = ((df["club_member"] == False) & (df["test_score"] > 80)).any()
    if exists:
        ids = df[(df["club_member"] == False) & (df["test_score"] > 80)]["student_id"].tolist()
        expl = f"Students {', '.join(ids)} satisfy the condition."
    else:
        expl = "No non-club member has a test score > 80."
    return exists, expl

def stmt_9(df: pd.DataFrame):
    """9. For all students with attendance rate greater than 90, their study hours per week are greater than or equal to 5.9."""
    subset = df[df["attendance_rate"] > 90]
    condition = subset["study_hours_week"] >= 5.9
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with attendance > 90 have study hours >= 5.9."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a student has a test score less than 70, then they are in grade level 10 or 12."""
    subset = df[df["test_score"] < 70]
    condition = subset["grade_level"].isin([10, 12])
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test score < 70 are in grades 10 or 12."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Most students in the table are club members."""
    total = len(df)
    count = df["club_member"].sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        expl = f"{count}/{total} ({proportion:.1%}) students are club members."
    else:
        expl = f"{count}/{total} ({proportion:.1%}) students are club members."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All students with study hours per week less than 4 have a test score less than 80."""
    subset = df[df["study_hours_week"] < 4]
    condition = subset["test_score"] < 80
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with study hours < 4 have test score < 80."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a student is in grade level 11, then their attendance rate is greater than or equal to 85.2."""
    subset = df[df["grade_level"] == 11]
    condition = subset["attendance_rate"] >= 85.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students in grade 11 have attendance rate >= 85.2."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students in grade 11 violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one student in grade level 9 who has a test score greater than 90."""
    exists = ((df["grade_level"] == 9) & (df["test_score"] > 90)).any()
    if exists:
        ids = df[(df["grade_level"] == 9) & (df["test_score"] > 90)]["student_id"].tolist()
        expl = f"Students {', '.join(ids)} satisfy the condition."
    else:
        expl = "No student in grade 9 has a test score > 90."
    return exists, expl

def stmt_15(df: pd.DataFrame):
    """15. For all students with a test score greater than 95, their grade level is 9 or 11."""
    subset = df[df["test_score"] > 95]
    condition = subset["grade_level"].isin([9, 11])
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test score > 95 are in grades 9 or 11."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All students with attendance rate greater than 95 have a grade level of 12."""
    subset = df[df["attendance_rate"] > 95]
    condition = subset["grade_level"] == 12
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with attendance > 95 are in grade 12."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a student has a test score greater than 80, then their study hours per week are greater than or equal to 5.4."""
    subset = df[df["test_score"] > 80]
    condition = subset["study_hours_week"] >= 5.4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test score > 80 have study hours >= 5.4."
    else:
        viol = subset[~condition]
        ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_30.csv")

    # Convert numeric columns
    for col in ["grade_level", "study_hours_week", "attendance_rate", "test_score"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert club_member to boolean
    df["club_member"] = df["club_member"].str.lower().map({"yes": True, "no": False})

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()