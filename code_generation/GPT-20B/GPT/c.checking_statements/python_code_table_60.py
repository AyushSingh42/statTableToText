import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all students who study at least 10 hours per week, the test score is at least 87."""
    subset = df[df["study_hours_week"] >= 10]
    condition = subset["test_score"] >= 87
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students studying ≥10h have test scores ≥87."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(viol['student_id'])})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All club members have an attendance rate of at least 85%."""
    members = df[df["club_member"] == "yes"]
    condition = members["attendance_rate"] >= 85
    truth = condition.all()
    if truth:
        expl = f"All {len(members)} club members have attendance ≥85%."
    else:
        viol = members[~condition]
        expl = f"{len(viol)} club members violate the rule (IDs: {', '.join(viol['student_id'])})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every 12th‑grade student scored 89 or lower on the test."""
    twelfth = df[df["grade_level"] == 12]
    condition = twelfth["test_score"] <= 89
    truth = condition.all()
    if truth:
        expl = f"All {len(twelfth)} 12th‑grade students scored ≤89."
    else:
        viol = twelfth[~condition]
        expl = f"{len(viol)} 12th‑grade students violate the rule (IDs: {', '.join(viol['student_id'])})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Most students (11 out of 15) have an attendance rate of at least 90%."""
    total = len(df)
    count_90 = (df["attendance_rate"] >= 90).sum()
    truth = count_90 >= 11
    if truth:
        expl = f"{count_90} out of {total} students have attendance ≥90%."
    else:
        expl = f"Only {count_90} out of {total} students have attendance ≥90%."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Students who study three hours or less per week scored at least 88 on the test."""
    subset = df[df["study_hours_week"] <= 3]
    condition = subset["test_score"] >= 88
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students studying ≤3h have test scores ≥88."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(viol['student_id'])})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Any student with an attendance rate of 95% or higher is not a club member."""
    subset = df[df["attendance_rate"] >= 95]
    condition = subset["club_member"] == "no"
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with attendance ≥95% are not club members."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students with attendance ≥95% are club members (IDs: {', '.join(viol['student_id'])})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every 9th‑grade student scored at least 84 on the test."""
    ninth = df[df["grade_level"] == 9]
    condition = ninth["test_score"] >= 84
    truth = condition.all()
    if truth:
        expl = f"All {len(ninth)} 9th‑grade students scored ≥84."
    else:
        viol = ninth[~condition]
        expl = f"{len(viol)} 9th‑grade students violate the rule (IDs: {', '.join(viol['student_id'])})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All 10th‑grade students have an attendance rate of at least 85%."""
    tenth = df[df["grade_level"] == 10]
    condition = tenth["attendance_rate"] >= 85
    truth = condition.all()
    if truth:
        expl = f"All {len(tenth)} 10th‑grade students have attendance ≥85%."
    else:
        viol = tenth[~condition]
        expl = f"{len(viol)} 10th‑grade students violate the rule (IDs: {', '.join(viol['student_id'])})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All students who study at least 8 hours per week scored at least 75 on the test."""
    subset = df[df["study_hours_week"] >= 8]
    condition = subset["test_score"] >= 75
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students studying ≥8h have test scores ≥75."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(viol['student_id'])})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_60.csv")

    # Convert numeric columns
    numeric_cols = ["grade_level", "study_hours_week", "attendance_rate", "test_score"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Standardize club_member to lowercase
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()