import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a grade level of 9 have a test score less than 90."""
    g9 = df[df["grade_level"] == 9]
    condition = g9["test_score"] < 90
    truth = condition.all()
    if truth:
        expl = f"All {len(g9)} students with grade 9 have test scores < 90."
    else:
        viol = g9[~condition]
        expl = f"{len(viol)} students with grade 9 violate the rule (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their study hours per week are greater than or equal to 3.3."""
    club = df[df["club_member"]]
    condition = club["study_hours_week"] >= 3.3
    truth = condition.all()
    if truth:
        expl = f"All {len(club)} club members have study hours >= 3.3."
    else:
        viol = club[~condition]
        expl = f"{len(viol)} club members violate the rule (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student with a grade level of 12 who has a test score of 91."""
    exists = ((df["grade_level"] == 12) & (df["test_score"] == 91)).any()
    if exists:
        count = df[(df["grade_level"] == 12) & (df["test_score"] == 91)].shape[0]
        expl = f"Found {count} student(s) with grade 12 and test score 91."
    else:
        expl = "No student with grade 12 and test score 91 found."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All students with a study hours per week of 11.1 or more have a grade level of 9 or 12."""
    high_hours = df[df["study_hours_week"] >= 11.1]
    condition = high_hours["grade_level"].isin([9, 12])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_hours)} students with study hours >= 11.1 have grade 9 or 12."
    else:
        viol = high_hours[~condition]
        expl = f"{len(viol)} students with study hours >= 11.1 violate the rule (grades: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a student has an attendance rate greater than 96, then their test score is less than 90."""
    high_att = df[df["attendance_rate"] > 96]
    condition = high_att["test_score"] < 90
    truth = condition.all()
    if truth:
        expl = f"All {len(high_att)} students with attendance > 96 have test scores < 90."
    else:
        viol = high_att[~condition]
        expl = f"{len(viol)} students with attendance > 96 violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students have an attendance rate greater than 90."""
    proportion = (df["attendance_rate"] > 90).mean()
    truth = proportion > 0.5
    expl = f"{proportion*100:.1f}% of students have attendance > 90."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a grade level of 11 have a test score less than 90."""
    g11 = df[df["grade_level"] == 11]
    condition = g11["test_score"] < 90
    truth = condition.all()
    if truth:
        expl = f"All {len(g11)} students with grade 11 have test scores < 90."
    else:
        viol = g11[~condition]
        expl = f"{len(viol)} students with grade 11 violate the rule (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a student is a club member, then their grade level is not 12."""
    club = df[df["club_member"]]
    condition = club["grade_level"]!= 12
    truth = condition.all()
    if truth:
        expl = f"All {len(club)} club members do not have grade 12."
    else:
        viol = club[~condition]
        expl = f"{len(viol)} club members violate the rule (grades: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one student with a grade level of 9 who has a study hours per week of 7.7 or more."""
    exists = ((df["grade_level"] == 9) & (df["study_hours_week"] >= 7.7)).any()
    if exists:
        count = df[(df["grade_level"] == 9) & (df["study_hours_week"] >= 7.7)].shape[0]
        expl = f"Found {count} student(s) with grade 9 and study hours >= 7.7."
    else:
        expl = "No student with grade 9 and study hours >= 7.7 found."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All students with a test score of 91 or more have a grade level of 12."""
    high_score = df[df["test_score"] >= 91]
    condition = high_score["grade_level"] == 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_score)} students with test score >= 91 have grade 12."
    else:
        viol = high_score[~condition]
        expl = f"{len(viol)} students with test score >= 91 violate the rule (grades: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a student has a study hours per week of 2.5 or less, then their test score is less than 90."""
    low_hours = df[df["study_hours_week"] <= 2.5]
    condition = low_hours["test_score"] < 90
    truth = condition.all()
    if truth:
        expl = f"All {len(low_hours)} students with study hours <= 2.5 have test scores < 90."
    else:
        viol = low_hours[~condition]
        expl = f"{len(viol)} students with study hours <= 2.5 violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All students with a grade level of 10 have a test score less than 91."""
    g10 = df[df["grade_level"] == 10]
    condition = g10["test_score"] < 91
    truth = condition.all()
    if truth:
        expl = f"All {len(g10)} students with grade 10 have test scores < 91."
    else:
        viol = g10[~condition]
        expl = f"{len(viol)} students with grade 10 violate the rule (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most students are not club members."""
    proportion = (~df["club_member"]).mean()
    truth = proportion > 0.5
    expl = f"{proportion*100:.1f}% of students are not club members."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a student has an attendance rate greater than 94, then their test score is less than 91."""
    high_att = df[df["attendance_rate"] > 94]
    condition = high_att["test_score"] < 91
    truth = condition.all()
    if truth:
        expl = f"All {len(high_att)} students with attendance > 94 have test scores < 91."
    else:
        viol = high_att[~condition]
        expl = f"{len(viol)} students with attendance > 94 violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one student with a grade level of 11 who has a study hours per week of 9.8 or more."""
    exists = ((df["grade_level"] == 11) & (df["study_hours_week"] >= 9.8)).any()
    if exists:
        count = df[(df["grade_level"] == 11) & (df["study_hours_week"] >= 9.8)].shape[0]
        expl = f"Found {count} student(s) with grade 11 and study hours >= 9.8."
    else:
        expl = "No student with grade 11 and study hours >= 9.8 found."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. All students with a study hours per week of 8.2 or more have a grade level of 10 or 11."""
    high_hours = df[df["study_hours_week"] >= 8.2]
    condition = high_hours["grade_level"].isin([10, 11])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_hours)} students with study hours >= 8.2 have grade 10 or 11."
    else:
        viol = high_hours[~condition]
        expl = f"{len(viol)} students with study hours >= 8.2 violate the rule (grades: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_10.csv")

    # Convert numeric columns
    numeric_cols = ["grade_level", "study_hours_week", "attendance_rate", "test_score"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert club_member to boolean
    df["club_member"] = df["club_member"].str.lower() == "yes"

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