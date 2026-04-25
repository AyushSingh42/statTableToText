import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 12th-grade students have a test score of 91."""
    twelfth_graders = df[df["grade_level"] == 12]
    if twelfth_graders.empty:
        truth = True
        expl = "No 12th-grade students in dataset."
    else:
        condition = (twelfth_graders["test_score"] == 91)
        truth = condition.all()
        if truth:
            expl = f"All {len(twelfth_graders)} 12th-grade students have a test score of 91."
        else:
            viol = twelfth_graders[~condition]
            expl = f"{len(viol)} 12th-grade students do not have a test score of 91 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All 9th-grade students have attendance rates greater than 89%."""
    ninth_graders = df[df["grade_level"] == 9]
    if ninth_graders.empty:
        truth = True
        expl = "No 9th-grade students in dataset."
    else:
        condition = (ninth_graders["attendance_rate"] > 89)
        truth = condition.all()
        if truth:
            expl = f"All {len(ninth_graders)} 9th-grade students have attendance rates greater than 89%."
        else:
            viol = ninth_graders[~condition]
            expl = f"{len(viol)} 9th-grade students have attendance rates <= 89% (rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All club members have attendance rates at most 94.5%."""
    club_members = df[df["club_member"] == "yes"]
    if club_members.empty:
        truth = True
        expl = "No club members in dataset."
    else:
        condition = (club_members["attendance_rate"] <= 94.5)
        truth = condition.all()
        if truth:
            expl = f"All {len(club_members)} club members have attendance rates at most 94.5%."
        else:
            viol = club_members[~condition]
            expl = f"{len(viol)} club members have attendance rates > 94.5% (rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All students who study more than 10 hours per week have test scores no higher than 91."""
    over_ten_hours = df[df["study_hours_week"] > 10]
    if over_ten_hours.empty:
        truth = True
        expl = "No students study more than 10 hours per week."
    else:
        condition = (over_ten_hours["test_score"] <= 91)
        truth = condition.all()
        if truth:
            expl = f"All {len(over_ten_hours)} students studying more than 10 hours per week have test scores no higher than 91."
        else:
            viol = over_ten_hours[~condition]
            expl = f"{len(viol)} students studying more than 10 hours per week have test scores > 91 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All students with attendance rates below 88% have test scores of at least 86."""
    low_attendance = df[df["attendance_rate"] < 88]
    if low_attendance.empty:
        truth = True
        expl = "No students with attendance rates below 88%."
    else:
        condition = (low_attendance["test_score"] >= 86)
        truth = condition.all()
        if truth:
            expl = f"All {len(low_attendance)} students with attendance rates below 88% have test scores of at least 86."
        else:
            viol = low_attendance[~condition]
            expl = f"{len(viol)} students with attendance rates below 88% have test scores < 86 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All club members study at least 3.8 hours per week."""
    club_members = df[df["club_member"] == "yes"]
    if club_members.empty:
        truth = True
        expl = "No club members in dataset."
    else:
        condition = (club_members["study_hours_week"] >= 3.8)
        truth = condition.all()
        if truth:
            expl = f"All {len(club_members)} club members study at least 3.8 hours per week."
        else:
            viol = club_members[~condition]
            expl = f"{len(viol)} club members study less than 3.8 hours per week (hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most students have attendance rates above 90%."""
    above_ninety = df[df["attendance_rate"] > 90]
    total_students = len(df)
    if total_students == 0:
        truth = True
        expl = "No students in dataset."
    else:
        proportion = len(above_ninety) / total_students
        truth = proportion > 0.5
        expl = f"{len(above_ninety)} out of {total_students} students ({proportion:.2%}) have attendance rates above 90%."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. The average test score of 11th-grade students is 86.25."""
    eleventh_graders = df[df["grade_level"] == 11]
    if eleventh_graders.empty:
        truth = True
        expl = "No 11th-grade students in dataset."
    else:
        avg_score = eleventh_graders["test_score"].mean()
        truth = abs(avg_score - 86.25) < 0.001  # account for floating point precision
        expl = f"Average test score of {len(eleventh_graders)} 11th-grade students is {avg_score:.2f}, not 86.25."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_10.csv")

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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()