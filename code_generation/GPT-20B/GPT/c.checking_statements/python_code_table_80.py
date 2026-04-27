import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students who study at least 10 hours per week have test scores of at least 89."""
    subset = df[df["study_hours_week"] >= 10]
    condition = subset["test_score"] >= 89
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students studying ≥10h have test scores ≥89."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} students violate the rule (study_hours: {', '.join(map(str, viol['study_hours_week'].tolist()))}, test_scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All club members study at least 5.5 hours per week."""
    members = df[df["club_member"] == True]
    condition = members["study_hours_week"] >= 5.5
    truth = condition.all()
    if truth:
        expl = f"All {len(members)} club members study ≥5.5h."
    else:
        viol = members[~condition]
        expl = f"{len(viol)} club members violate the rule (study_hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All grade 12 students study at least 7.2 hours per week."""
    grade12 = df[df["grade_level"] == 12]
    condition = grade12["study_hours_week"] >= 7.2
    truth = condition.all()
    if truth:
        expl = f"All {len(grade12)} grade 12 students study ≥7.2h."
    else:
        viol = grade12[~condition]
        expl = f"{len(viol)} grade 12 students violate the rule (study_hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All grade 9 students have test scores no higher than 94."""
    grade9 = df[df["grade_level"] == 9]
    condition = grade9["test_score"] <= 94
    truth = condition.all()
    if truth:
        expl = f"All {len(grade9)} grade 9 students have test scores ≤94."
    else:
        viol = grade9[~condition]
        expl = f"{len(viol)} grade 9 students violate the rule (test_scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All grade 9 students have attendance rates of at least 88.0%."""
    grade9 = df[df["grade_level"] == 9]
    condition = grade9["attendance_rate"] >= 88.0
    truth = condition.all()
    if truth:
        expl = f"All {len(grade9)} grade 9 students have attendance ≥88.0%."
    else:
        viol = grade9[~condition]
        expl = f"{len(viol)} grade 9 students violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All students with test scores of at least 95 have attendance rates of at least 88.4%."""
    high_score = df[df["test_score"] >= 95]
    condition = high_score["attendance_rate"] >= 88.4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_score)} students with test scores ≥95 have attendance ≥88.4%."
    else:
        viol = high_score[~condition]
        expl = f"{len(viol)} students violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most students have attendance rates above 85%."""
    total = len(df)
    above_85 = df[df["attendance_rate"] > 85]
    proportion = len(above_85) / total
    truth = proportion > 0.5
    if truth:
        expl = f"{len(above_85)} out of {total} students ({proportion*100:.1f}%) have attendance >85%."
    else:
        expl = f"Only {len(above_85)} out of {total} students ({proportion*100:.1f}%) have attendance >85%."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_80.csv")

    # Convert numeric columns safely
    for col in ["grade_level", "study_hours_week", "attendance_rate", "test_score"]:
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()