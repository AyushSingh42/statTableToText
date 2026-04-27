import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All club members have attendance rates of at least 90%."""
    club_members = df[df["club_member"] == "yes"]
    condition = club_members["attendance_rate"] >= 90
    truth = condition.all()
    if truth:
        expl = f"All {len(club_members)} club members have attendance >= 90%."
    else:
        viol = club_members[~condition]
        expl = f"{len(viol)} club members violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. No club member has a test score of 90 or above."""
    club_members = df[df["club_member"] == "yes"]
    condition = club_members["test_score"] < 90
    truth = condition.all()
    if truth:
        expl = f"No club member has test score >= 90."
    else:
        viol = club_members[~condition]
        expl = f"{len(viol)} club members have test score >= 90 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All 9th-grade students study at least 4.3 hours per week."""
    ninth_graders = df[df["grade_level"] == 9]
    condition = ninth_graders["study_hours_week"] >= 4.3
    truth = condition.all()
    if truth:
        expl = f"All {len(ninth_graders)} 9th graders study >= 4.3 hours/week."
    else:
        viol = ninth_graders[~condition]
        expl = f"{len(viol)} 9th graders study < 4.3 hours/week (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All 10th graders have attendance rates of at least 97%."""
    tenth_graders = df[df["grade_level"] == 10]
    condition = tenth_graders["attendance_rate"] >= 97
    truth = condition.all()
    if truth:
        expl = f"All {len(tenth_graders)} 10th graders have attendance >= 97%."
    else:
        viol = tenth_graders[~condition]
        expl = f"{len(viol)} 10th graders have attendance < 97% (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All 11th graders study at least 3.2 hours per week."""
    eleventh_graders = df[df["grade_level"] == 11]
    condition = eleventh_graders["study_hours_week"] >= 3.2
    truth = condition.all()
    if truth:
        expl = f"All {len(eleventh_graders)} 11th graders study >= 3.2 hours/week."
    else:
        viol = eleventh_graders[~condition]
        expl = f"{len(viol)} 11th graders study < 3.2 hours/week (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All 12th graders study at least 4.3 hours per week."""
    twelfth_graders = df[df["grade_level"] == 12]
    condition = twelfth_graders["study_hours_week"] >= 4.3
    truth = condition.all()
    if truth:
        expl = f"All {len(twelfth_graders)} 12th graders study >= 4.3 hours/week."
    else:
        viol = twelfth_graders[~condition]
        expl = f"{len(viol)} 12th graders study < 4.3 hours/week (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most students have attendance rates of at least 90%."""
    total_students = len(df)
    qualified = df[df["attendance_rate"] >= 90]
    proportion = len(qualified) / total_students
    truth = proportion > 0.5
    if truth:
        expl = f"{len(qualified)} out of {total_students} students have attendance >= 90% ({proportion:.1%} of total)."
    else:
        expl = f"{len(qualified)} out of {total_students} students have attendance >= 90% ({proportion:.1%} of total), which is not more than half."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All students who study at least 9 hours per week achieve test scores of at least 64."""
    high_studiers = df[df["study_hours_week"] >= 9]
    condition = high_studiers["test_score"] >= 64
    truth = condition.all()
    if truth:
        expl = f"All {len(high_studiers)} students studying >= 9 hours/week have test score >= 64."
    else:
        viol = high_studiers[~condition]
        expl = f"{len(viol)} students studying >= 9 hours/week have test score < 64 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All students with test scores of 68 or lower have attendance rates of at least 91.6%."""
    low_scorers = df[df["test_score"] <= 68]
    condition = low_scorers["attendance_rate"] >= 91.6
    truth = condition.all()
    if truth:
        expl = f"All {len(low_scorers)} students with test score <= 68 have attendance >= 91.6%."
    else:
        viol = low_scorers[~condition]
        expl = f"{len(viol)} students with test score <= 68 have attendance < 91.6% (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_70.csv")

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
        (8, stmt_8),
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()