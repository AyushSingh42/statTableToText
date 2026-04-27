import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a test score greater than or equal to 90 have a study time greater than or equal to 9 hours per week."""
    subset = df[df["test_score"] >= 90]
    if subset.empty:
        return True, "No students with test score >= 90, so the statement holds vacuously."
    truth = (subset["study_hours_week"] >= 9).all()
    if truth:
        return True, f"All {len(subset)} students with test score >= 90 have study time >= 9 hours."
    else:
        viol = subset[subset["study_hours_week"] < 9]
        return False, f"{len(viol)} students violate the rule (study times: {', '.join(map(str, viol['study_hours_week'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their test score is less than or equal to 97."""
    subset = df[df["club_member"] == "yes"]
    if subset.empty:
        return True, "No club members, so the statement holds vacuously."
    truth = (subset["test_score"] <= 97).all()
    if truth:
        return True, f"All {len(subset)} club members have test score <= 97."
    else:
        viol = subset[subset["test_score"] > 97]
        return False, f"{len(viol)} club members violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in the 9th grade with a test score greater than 90."""
    exists = ((df["grade_level"] == 9) & (df["test_score"] > 90)).any()
    if exists:
        row = df[(df["grade_level"] == 9) & (df["test_score"] > 90)].iloc[0]
        return True, f"Student {row['student_id']} meets the condition (grade 9, test score {row['test_score']})."
    else:
        return False, "No 9th grade student has a test score > 90."

def stmt_4(df: pd.DataFrame):
    """4. All students with an attendance rate greater than 94 have a test score greater than or equal to 84."""
    subset = df[df["attendance_rate"] > 94]
    if subset.empty:
        return True, "No students with attendance > 94, so the statement holds vacuously."
    truth = (subset["test_score"] >= 84).all()
    if truth:
        return True, f"All {len(subset)} students with attendance > 94 have test score >= 84."
    else:
        viol = subset[subset["test_score"] < 84]
        return False, f"{len(viol)} students violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."

def stmt_5(df: pd.DataFrame):
    """5. If a student is in the 12th grade, then their study time is less than or equal to 8.4 hours per week."""
    subset = df[df["grade_level"] == 12]
    if subset.empty:
        return True, "No 12th grade students, so the statement holds vacuously."
    truth = (subset["study_hours_week"] <= 8.4).all()
    if truth:
        return True, f"All {len(subset)} 12th grade students have study time <= 8.4 hours."
    else:
        viol = subset[subset["study_hours_week"] > 8.4]
        return False, f"{len(viol)} 12th grade students violate the rule (study times: {', '.join(map(str, viol['study_hours_week'].tolist()))})."

def stmt_6(df: pd.DataFrame):
    """6. Most students have an attendance rate greater than 90."""
    total = len(df)
    count = (df["attendance_rate"] > 90).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        return True, f"{count} out of {total} students ({proportion:.2%}) have attendance > 90."
    else:
        return False, f"{count} out of {total} students ({proportion:.2%}) have attendance > 90, which is not a majority."

def stmt_7(df: pd.DataFrame):
    """7. All students with a test score less than 80 have a study time less than 8 hours per week."""
    subset = df[df["test_score"] < 80]
    if subset.empty:
        return True, "No students with test score < 80, so the statement holds vacuously."
    truth = (subset["study_hours_week"] < 8).all()
    if truth:
        return True, f"All {len(subset)} students with test score < 80 have study time < 8 hours."
    else:
        viol = subset[subset["study_hours_week"] >= 8]
        return False, f"{len(viol)} students violate the rule (study times: {', '.join(map(str, viol['study_hours_week'].tolist()))})."

def stmt_8(df: pd.DataFrame):
    """8. If a student is in the 11th grade, then their test score is greater than or equal to 81."""
    subset = df[df["grade_level"] == 11]
    if subset.empty:
        return True, "No 11th grade students, so the statement holds vacuously."
    truth = (subset["test_score"] >= 81).all()
    if truth:
        return True, f"All {len(subset)} 11th grade students have test score >= 81."
    else:
        viol = subset[subset["test_score"] < 81]
        return False, f"{len(viol)} 11th grade students violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student with a study time less than 4 hours per week who is a club member."""
    exists = ((df["study_hours_week"] < 4) & (df["club_member"] == "yes")).any()
    if exists:
        row = df[(df["study_hours_week"] < 4) & (df["club_member"] == "yes")].iloc[0]
        return True, f"Student {row['student_id']} meets the condition (study time {row['study_hours_week']} hrs, club member)."
    else:
        return False, "No club member has study time < 4 hours."

def stmt_10(df: pd.DataFrame):
    """10. All students with a test score greater than or equal to 97 have a grade level less than or equal to 10."""
    subset = df[df["test_score"] >= 97]
    if subset.empty:
        return True, "No students with test score >= 97, so the statement holds vacuously."
    truth = (subset["grade_level"] <= 10).all()
    if truth:
        return True, f"All {len(subset)} students with test score >= 97 have grade level <= 10."
    else:
        viol = subset[subset["grade_level"] > 10]
        return False, f"{len(viol)} students violate the rule (grade levels: {', '.join(map(str, viol['grade_level'].tolist()))})."

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study time greater than 10 hours per week, then they are not a club member."""
    subset = df[df["study_hours_week"] > 10]
    if subset.empty:
        return True, "No students with study time > 10 hours, so the statement holds vacuously."
    truth = (subset["club_member"] == "no").all()
    if truth:
        return True, f"All {len(subset)} students with study time > 10 hours are not club members."
    else:
        viol = subset[subset["club_member"] == "yes"]
        return False, f"{len(viol)} students violate the rule (club members with study time > 10 hours)."

def stmt_12(df: pd.DataFrame):
    """12. Most students have a study time less than 10 hours per week."""
    total = len(df)
    count = (df["study_hours_week"] < 10).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        return True, f"{count} out of {total} students ({proportion:.2%}) have study time < 10 hours."
    else:
        return False, f"{count} out of {total} students ({proportion:.2%}) have study time < 10 hours, which is not a majority."

def stmt_13(df: pd.DataFrame):
    """13. All students with an attendance rate greater than 96 have a test score greater than or equal to 84."""
    subset = df[df["attendance_rate"] > 96]
    if subset.empty:
        return True, "No students with attendance > 96, so the statement holds vacuously."
    truth = (subset["test_score"] >= 84).all()
    if truth:
        return True, f"All {len(subset)} students with attendance > 96 have test score >= 84."
    else:
        viol = subset[subset["test_score"] < 84]
        return False, f"{len(viol)} students violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_60.csv")

    # Convert numeric columns safely
    numeric_cols = ["grade_level", "study_hours_week", "attendance_rate", "test_score"]
    for col in numeric_cols:
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()