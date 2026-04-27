import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All grade 9 students have attendance rates above 90%."""
    grade_9 = df[df["grade_level"] == 9]
    condition = grade_9["attendance_rate"] > 90
    truth = condition.all()
    if truth:
        expl = f"All {len(grade_9)} grade 9 students have attendance rates above 90%."
    else:
        viol = grade_9[~condition]
        expl = f"{len(viol)} grade 9 students have attendance rates <= 90%."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All grade 9 students have test scores of at least 87."""
    grade_9 = df[df["grade_level"] == 9]
    condition = grade_9["test_score"] >= 87
    truth = condition.all()
    if truth:
        expl = f"All {len(grade_9)} grade 9 students have test scores of at least 87."
    else:
        viol = grade_9[~condition]
        expl = f"{len(viol)} grade 9 students have test scores < 87."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All grade 12 students have attendance rates greater than 93%."""
    grade_12 = df[df["grade_level"] == 12]
    condition = grade_12["attendance_rate"] > 93
    truth = condition.all()
    if truth:
        expl = f"All {len(grade_12)} grade 12 students have attendance rates > 93%."
    else:
        viol = grade_12[~condition]
        expl = f"{len(viol)} grade 12 students have attendance rates <= 93%."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a student studies at least 11 hours per week, their test score is at least 70."""
    studied_enough = df[df["study_hours_week"] >= 11]
    condition = studied_enough["test_score"] >= 70
    truth = condition.all()
    if truth:
        expl = f"All {len(studied_enough)} students studying >=11 hours/week have test scores >= 70."
    else:
        viol = studied_enough[~condition]
        expl = f"{len(viol)} students studying >=11 hours/week have test scores < 70."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All grade 11 students who are not club members have attendance rates above 91%."""
    grade_11_non_club = df[(df["grade_level"] == 11) & (df["club_member"] == "no")]
    condition = grade_11_non_club["attendance_rate"] > 91
    truth = condition.all()
    if truth:
        expl = f"All {len(grade_11_non_club)} grade 11 non-club members have attendance rates > 91%."
    else:
        viol = grade_11_non_club[~condition]
        expl = f"{len(viol)} grade 11 non-club members have attendance rates <= 91%."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students have attendance rates above 90%."""
    condition = df["attendance_rate"] > 90
    count_above = condition.sum()
    total = len(df)
    truth = count_above > total / 2
    expl = f"{count_above} out of {total} students have attendance rates > 90%, which is {'more' if truth else 'less'} than half."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most students study at least 5 hours per week."""
    condition = df["study_hours_week"] >= 5
    count_above = condition.sum()
    total = len(df)
    truth = count_above > total / 2
    expl = f"{count_above} out of {total} students study >= 5 hours/week, which is {'more' if truth else 'less'} than half."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Non-club members have a higher average test score (≈84.6) than club members (≈82.0)."""
    non_club_avg = df[df["club_member"] == "no"]["test_score"].mean()
    club_avg = df[df["club_member"] == "yes"]["test_score"].mean()
    truth = non_club_avg > club_avg
    expl = f"Non-club members average {non_club_avg:.1f}, club members average {club_avg:.1f}. {'Higher' if truth else 'Lower'} for non-club members."
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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()