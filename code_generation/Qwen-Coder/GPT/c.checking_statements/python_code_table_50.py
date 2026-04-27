import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 9th‑grade students scored at least 93 on the test."""
    ninth_graders = df[df["grade_level"] == 9]
    condition = ninth_graders["test_score"] >= 93
    truth = condition.all()
    if truth:
        expl = f"All {len(ninth_graders)} 9th-grade students scored at least 93."
    else:
        viol = ninth_graders[~condition]
        expl = f"{len(viol)} 9th-grade students scored below 93 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All 11th‑grade students scored at least 79 on the test."""
    eleventh_graders = df[df["grade_level"] == 11]
    condition = eleventh_graders["test_score"] >= 79
    truth = condition.all()
    if truth:
        expl = f"All {len(eleventh_graders)} 11th-grade students scored at least 79."
    else:
        viol = eleventh_graders[~condition]
        expl = f"{len(viol)} 11th-grade students scored below 79 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All 10th‑grade students have an attendance rate of at least 86.8 %."""
    tenth_graders = df[df["grade_level"] == 10]
    condition = tenth_graders["attendance_rate"] >= 86.8
    truth = condition.all()
    if truth:
        expl = f"All {len(tenth_graders)} 10th-grade students have attendance rate ≥ 86.8%."
    else:
        viol = tenth_graders[~condition]
        expl = f"{len(viol)} 10th-grade students have attendance rate < 86.8% (rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For every student whose attendance rate is at least 96 %, the test score is at least 86."""
    high_attendance = df[df["attendance_rate"] >= 96]
    condition = high_attendance["test_score"] >= 86
    truth = condition.all()
    if truth:
        expl = f"All {len(high_attendance)} students with attendance ≥ 96% scored at least 86."
    else:
        viol = high_attendance[~condition]
        expl = f"{len(viol)} students with attendance ≥ 96% scored below 86 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All students who studied at least 10 hours per week scored at least 70 on the test."""
    high_study = df[df["study_hours_week"] >= 10]
    condition = high_study["test_score"] >= 70
    truth = condition.all()
    if truth:
        expl = f"All {len(high_study)} students studying ≥ 10 hours/week scored at least 70."
    else:
        viol = high_study[~condition]
        expl = f"{len(viol)} students studying ≥ 10 hours/week scored below 70 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All students who studied less than 4 hours per week scored at least 86 on the test."""
    low_study = df[df["study_hours_week"] < 4]
    condition = low_study["test_score"] >= 86
    truth = condition.all()
    if truth:
        expl = f"All {len(low_study)} students studying < 4 hours/week scored at least 86."
    else:
        viol = low_study[~condition]
        expl = f"{len(viol)} students studying < 4 hours/week scored below 86 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All club members have an attendance rate of at least 84.5 %."""
    club_members = df[df["club_member"] == "yes"]
    condition = club_members["attendance_rate"] >= 84.5
    truth = condition.all()
    if truth:
        expl = f"All {len(club_members)} club members have attendance rate ≥ 84.5%."
    else:
        viol = club_members[~condition]
        expl = f"{len(viol)} club members have attendance rate < 84.5% (rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_50.csv")

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
        (7, stmt_7)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()