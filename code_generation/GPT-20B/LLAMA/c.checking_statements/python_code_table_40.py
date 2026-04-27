import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a test score greater than or equal to 93 have an attendance rate greater than or equal to 90."""
    subset = df[df["test_score"] >= 93]
    condition = subset["attendance_rate"] >= 90
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test_score >= 93 have attendance_rate >= 90."
    else:
        viol = subset[~condition]
        ids = ", ".join(viol["student_id"].tolist())
        expl = f"{len(viol)} students violate the rule (IDs: {ids})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their test score is greater than or equal to 69."""
    subset = df[df["club_member"].str.lower() == "yes"]
    condition = subset["test_score"] >= 69
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} club members have test_score >= 69."
    else:
        viol = subset[~condition]
        ids = ", ".join(viol["student_id"].tolist())
        expl = f"{len(viol)} club members violate the rule (IDs: {ids})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in grade level 9 who has a study hours per week greater than or equal to 9.5."""
    exists = ((df["grade_level"] == 9) & (df["study_hours_week"] >= 9.5)).any()
    if exists:
        ids = df[(df["grade_level"] == 9) & (df["study_hours_week"] >= 9.5)]["student_id"].tolist()
        expl = f"Students {', '.join(ids)} satisfy the condition."
    else:
        expl = "No student satisfies the condition."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All students in grade level 12 have a study hours per week less than or equal to 11.5."""
    subset = df[df["grade_level"] == 12]
    condition = subset["study_hours_week"] <= 11.5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} grade 12 students have study_hours_week <= 11.5."
    else:
        viol = subset[~condition]
        ids = ", ".join(viol["student_id"].tolist())
        expl = f"{len(viol)} grade 12 students violate the rule (IDs: {ids})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student has a study hours per week less than 3, then their test score is greater than or equal to 97."""
    subset = df[df["study_hours_week"] < 3]
    condition = subset["test_score"] >= 97
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with study_hours_week < 3 have test_score >= 97."
    else:
        viol = subset[~condition]
        ids = ", ".join(viol["student_id"].tolist())
        expl = f"{len(viol)} students violate the rule (IDs: {ids})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students in the table have an attendance rate greater than 90."""
    count = (df["attendance_rate"] > 90).sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} students have attendance_rate > 90."
    else:
        expl = f"Only {count} out of {total} students have attendance_rate > 90."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a test score less than 70 have a grade level of 9."""
    subset = df[df["test_score"] < 70]
    condition = subset["grade_level"] == 9
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test_score < 70 are grade 9."
    else:
        viol = subset[~condition]
        ids = ", ".join(viol["student_id"].tolist())
        expl = f"{len(viol)} students violate the rule (IDs: {ids})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is in grade level 10, then their test score is greater than or equal to 83."""
    subset = df[df["grade_level"] == 10]
    condition = subset["test_score"] >= 83
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} grade 10 students have test_score >= 83."
    else:
        viol = subset[~condition]
        ids = ", ".join(viol["student_id"].tolist())
        expl = f"{len(viol)} grade 10 students violate the rule (IDs: {ids})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student in grade level 9 who has a test score greater than or equal to 97."""
    exists = ((df["grade_level"] == 9) & (df["test_score"] >= 97)).any()
    if exists:
        ids = df[(df["grade_level"] == 9) & (df["test_score"] >= 97)]["student_id"].tolist()
        expl = f"Students {', '.join(ids)} satisfy the condition."
    else:
        expl = "No student satisfies the condition."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All students who are club members have a test score greater than or equal to 69."""
    # Same as stmt_2
    return stmt_2(df)

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study hours per week greater than or equal to 9, then their attendance rate is greater than or equal to 89."""
    subset = df[df["study_hours_week"] >= 9]
    condition = subset["attendance_rate"] >= 89
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with study_hours_week >= 9 have attendance_rate >= 89."
    else:
        viol = subset[~condition]
        ids = ", ".join(viol["student_id"].tolist())
        expl = f"{len(viol)} students violate the rule (IDs: {ids})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All students in grade level 12 have a test score less than or equal to 92."""
    subset = df[df["grade_level"] == 12]
    condition = subset["test_score"] <= 92
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} grade 12 students have test_score <= 92."
    else:
        viol = subset[~condition]
        ids = ", ".join(viol["student_id"].tolist())
        expl = f"{len(viol)} grade 12 students violate the rule (IDs: {ids})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most students in the table have a study hours per week less than or equal to 7."""
    count = (df["study_hours_week"] <= 7).sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} students have study_hours_week <= 7."
    else:
        expl = f"Only {count} out of {total} students have study_hours_week <= 7."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_40.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col not in ["student_id", "club_member"]:
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()