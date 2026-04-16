import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with study hours greater than 8 have a test score above 80."""
    students = df[df["study_hours_week"] > 8]
    condition = students["test_score"] > 80
    truth = condition.all()
    if truth:
        expl = f"All {len(students)} students with study hours > 8 have a test score > 80."
    else:
        viol = students[~condition]
        expl = f"{len(viol)} students violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is in grade 9, then their attendance rate is always above 87."""
    students = df[df["grade_level"] == 9]
    condition = students["attendance_rate"] > 87
    truth = condition.all()
    if truth:
        expl = f"All {len(students)} students in grade 9 have an attendance rate > 87."
    else:
        viol = students[~condition]
        expl = f"{len(viol)} students in grade 9 violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every student with a test score above 90 is a club member."""
    students = df[df["test_score"] > 90]
    condition = students["club_member"]
    truth = condition.all()
    if truth:
        expl = f"All {len(students)} students with a test score > 90 are club members."
    else:
        viol = students[~condition]
        expl = f"{len(viol)} students with a test score > 90 violate the rule."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Students in grade 12 with study hours less than 7 have a lower test score than those with more study hours."""
    students = df[df["grade_level"] == 12]
    less_than_7 = students[students["study_hours_week"] < 7]
    more_than_7 = students[students["study_hours_week"] >= 7]
    truth = (less_than_7["test_score"].max() < more_than_7["test_score"].min())
    if truth:
        expl = f"Students in grade 12 with study hours < 7 have a lower test score than those with more study hours."
    else:
        expl = f"Students in grade 12 with study hours < 7 do not have a lower test score than those with more study hours."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All students with an attendance rate above 96 are in either grade 10 or 12."""
    students = df[df["attendance_rate"] > 96]
    condition = students["grade_level"].isin([10, 12])
    truth = condition.all()
    if truth:
        expl = f"All {len(students)} students with an attendance rate > 96 are in grade 10 or 12."
    else:
        viol = students[~condition]
        expl = f"{len(viol)} students with an attendance rate > 96 violate the rule (grades: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a student is a club member, then their study hours are always above 4."""
    students = df[df["club_member"]]
    condition = students["study_hours_week"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(students)} club members have study hours > 4."
    else:
        viol = students[~condition]
        expl = f"{len(viol)} club members violate the rule (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Students in grade 11 with study hours above 6 have a higher test score than those with fewer study hours."""
    students = df[df["grade_level"] == 11]
    more_than_6 = students[students["study_hours_week"] > 6]
    less_than_6 = students[students["study_hours_week"] <= 6]
    truth = (more_than_6["test_score"].min() > less_than_6["test_score"].max())
    if truth:
        expl = f"Students in grade 11 with study hours > 6 have a higher test score than those with fewer study hours."
    else:
        expl = f"Students in grade 11 with study hours > 6 do not have a higher test score than those with fewer study hours."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All students with a test score below 75 have an attendance rate below 90."""
    students = df[df["test_score"] < 75]
    condition = students["attendance_rate"] < 90
    truth = condition.all()
    if truth:
        expl = f"All {len(students)} students with a test score < 75 have an attendance rate < 90."
    else:
        viol = students[~condition]
        expl = f"{len(viol)} students with a test score < 75 violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a student has a study hours to test score ratio above 0.1, then they are a club member."""
    students = df[df["study_hours_week"] / df["test_score"] > 0.1]
    condition = students["club_member"]
    truth = condition.all()
    if truth:
        expl = f"All {len(students)} students with a study hours to test score ratio > 0.1 are club members."
    else:
        viol = students[~condition]
        expl = f"{len(viol)} students with a study hours to test score ratio > 0.1 violate the rule."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Every student in grade 10 with an attendance rate above 95 is a club member."""
    students = df[(df["grade_level"] == 10) & (df["attendance_rate"] > 95)]
    condition = students["club_member"]
    truth = condition.all()
    if truth:
        expl = f"All {len(students)} students in grade 10 with an attendance rate > 95 are club members."
    else:
        viol = students[~condition]
        expl = f"{len(viol)} students in grade 10 with an attendance rate > 95 violate the rule."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Students with study hours between 4 and 7 have a lower test score than those with more or fewer study hours."""
    students = df[(df["study_hours_week"] >= 4) & (df["study_hours_week"] <= 7)]
    less_than_4 = df[df["study_hours_week"] < 4]
    more_than_7 = df[df["study_hours_week"] > 7]
    truth = (students["test_score"].max() < less_than_4["test_score"].min()) and (students["test_score"].max() < more_than_7["test_score"].min())
    if truth:
        expl = f"Students with study hours between 4 and 7 have a lower test score than those with more or fewer study hours."
    else:
        expl = f"Students with study hours between 4 and 7 do not have a lower test score than those with more or fewer study hours."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All students with an attendance rate above 98 are in grade 9 or 12."""
    students = df[df["attendance_rate"] > 98]
    condition = students["grade_level"].isin([9, 12])
    truth = condition.all()
    if truth:
        expl = f"All {len(students)} students with an attendance rate > 98 are in grade 9 or 12."
    else:
        viol = students[~condition]
        expl = f"{len(viol)} students with an attendance rate > 98 violate the rule (grades: {', '.join(map(str, viol['grade_level'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a student is not a club member, then their test score is always below 90."""
    students = df[~df["club_member"]]
    condition = students["test_score"] < 90
    truth = condition.all()
    if truth:
        expl = f"All {len(students)} non-club members have a test score < 90."
    else:
        viol = students[~condition]
        expl = f"{len(viol)} non-club members violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Students in grade 11 with an attendance rate above 92 have a higher test score than those with a lower attendance rate."""
    students = df[df["grade_level"] == 11]
    more_than_92 = students[students["attendance_rate"] > 92]
    less_than_92 = students[students["attendance_rate"] <= 92]
    truth = (more_than_92["test_score"].min() > less_than_92["test_score"].max())
    if truth:
        expl = f"Students in grade 11 with an attendance rate > 92 have a higher test score than those with a lower attendance rate."
    else:
        expl = f"Students in grade 11 with an attendance rate > 92 do not have a higher test score than those with a lower attendance rate."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All students with a test score above 85 have study hours above 5, except for those in grade 10."""
    students = df[(df["test_score"] > 85) & (df["grade_level"]!= 10)]
    condition = students["study_hours_week"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(students)} students with a test score > 85 have study hours > 5, except for those in grade 10."
    else:
        viol = students[~condition]
        expl = f"{len(viol)} students with a test score > 85 violate the rule (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_0.csv")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10), (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()