import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All grade 9 students have attendance rates above 90%."""
    grade9 = df[df["grade_level"] == 9]
    condition = grade9["attendance_rate"] > 90
    truth = condition.all()
    if truth:
        expl = f"All {len(grade9)} grade 9 students have attendance > 90%."
    else:
        viol = grade9[~condition]
        expl = f"{len(viol)} grade 9 students violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All grade 9 students have test scores of at least 87."""
    grade9 = df[df["grade_level"] == 9]
    condition = grade9["test_score"] >= 87
    truth = condition.all()
    if truth:
        expl = f"All {len(grade9)} grade 9 students have test scores ≥ 87."
    else:
        viol = grade9[~condition]
        expl = f"{len(viol)} grade 9 students violate the rule (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All grade 12 students have attendance rates greater than 93%."""
    grade12 = df[df["grade_level"] == 12]
    condition = grade12["attendance_rate"] > 93
    truth = condition.all()
    if truth:
        expl = f"All {len(grade12)} grade 12 students have attendance > 93%."
    else:
        viol = grade12[~condition]
        expl = f"{len(viol)} grade 12 students violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a student studies at least 11 hours per week, their test score is at least 70."""
    study_11 = df[df["study_hours_week"] >= 11]
    condition = study_11["test_score"] >= 70
    truth = condition.all()
    if truth:
        expl = f"All {len(study_11)} students studying ≥ 11 hrs have test scores ≥ 70."
    else:
        viol = study_11[~condition]
        expl = f"{len(viol)} students studying ≥ 11 hrs violate the rule (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All grade 11 students who are not club members have attendance rates above 91%."""
    grade11_nonclub = df[(df["grade_level"] == 11) & (df["club_member"] == "no")]
    condition = grade11_nonclub["attendance_rate"] > 91
    truth = condition.all()
    if truth:
        expl = f"All {len(grade11_nonclub)} grade 11 non‑club members have attendance > 91%."
    else:
        viol = grade11_nonclub[~condition]
        expl = f"{len(viol)} grade 11 non‑club members violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students have attendance rates above 90%."""
    condition = df["attendance_rate"] > 90
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of students have attendance > 90%."
    else:
        expl = f"Only {proportion*100:.1f}% of students have attendance > 90%."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most students study at least 5 hours per week."""
    condition = df["study_hours_week"] >= 5
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of students study ≥ 5 hrs/week."
    else:
        expl = f"Only {proportion*100:.1f}% of students study ≥ 5 hrs/week."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Non‑club members have a higher average test score (≈84.6) than club members (≈82.0)."""
    avg_nonclub = df[df["club_member"] == "no"]["test_score"].mean()
    avg_club = df[df["club_member"] == "yes"]["test_score"].mean()
    truth = avg_nonclub > avg_club
    if truth:
        expl = f"Avg non‑club: {avg_nonclub:.1f} > Avg club: {avg_club:.1f}."
    else:
        expl = f"Avg non‑club: {avg_nonclub:.1f} ≤ Avg club: {avg_club:.1f}."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_20.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()