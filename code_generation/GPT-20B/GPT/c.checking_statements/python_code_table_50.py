import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 9th‑grade students scored at least 93 on the test."""
    ninth = df[df["grade_level"] == 9]
    condition = ninth["test_score"] >= 93
    truth = condition.all()
    if truth:
        expl = f"All {len(ninth)} 9th‑grade students scored at least 93."
    else:
        viol = ninth[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} 9th‑grade student(s) scored below 93 (scores: {', '.join(map(str, scores))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All 11th‑grade students scored at least 79 on the test."""
    eleventh = df[df["grade_level"] == 11]
    condition = eleventh["test_score"] >= 79
    truth = condition.all()
    if truth:
        expl = f"All {len(eleventh)} 11th‑grade students scored at least 79."
    else:
        viol = eleventh[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} 11th‑grade student(s) scored below 79 (scores: {', '.join(map(str, scores))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All 10th‑grade students have an attendance rate of at least 86.8 %."""
    tenth = df[df["grade_level"] == 10]
    condition = tenth["attendance_rate"] >= 86.8
    truth = condition.all()
    if truth:
        expl = f"All {len(tenth)} 10th‑grade students have attendance ≥ 86.8%."
    else:
        viol = tenth[~condition]
        rates = viol["attendance_rate"].tolist()
        expl = f"{len(viol)} 10th‑grade student(s) have attendance below 86.8% (rates: {', '.join(map(str, rates))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For every student whose attendance rate is at least 96 %, the test score is at least 86."""
    high_att = df[df["attendance_rate"] >= 96]
    condition = high_att["test_score"] >= 86
    truth = condition.all()
    if truth:
        expl = f"All {len(high_att)} students with attendance ≥ 96% scored at least 86."
    else:
        viol = high_att[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} student(s) with attendance ≥ 96% scored below 86 (scores: {', '.join(map(str, scores))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All students who studied at least 10 hours per week scored at least 70 on the test."""
    study_10 = df[df["study_hours_week"] >= 10]
    condition = study_10["test_score"] >= 70
    truth = condition.all()
    if truth:
        expl = f"All {len(study_10)} students who studied ≥ 10 hours/week scored at least 70."
    else:
        viol = study_10[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} student(s) who studied ≥ 10 hours/week scored below 70 (scores: {', '.join(map(str, scores))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All students who studied less than 4 hours per week scored at least 86 on the test."""
    study_lt4 = df[df["study_hours_week"] < 4]
    condition = study_lt4["test_score"] >= 86
    truth = condition.all()
    if truth:
        expl = f"All {len(study_lt4)} students who studied < 4 hours/week scored at least 86."
    else:
        viol = study_lt4[~condition]
        scores = viol["test_score"].tolist()
        expl = f"{len(viol)} student(s) who studied < 4 hours/week scored below 86 (scores: {', '.join(map(str, scores))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All club members have an attendance rate of at least 84.5 %."""
    club = df[df["club_member"].str.lower() == "yes"]
    condition = club["attendance_rate"] >= 84.5
    truth = condition.all()
    if truth:
        expl = f"All {len(club)} club members have attendance ≥ 84.5%."
    else:
        viol = club[~condition]
        rates = viol["attendance_rate"].tolist()
        expl = f"{len(viol)} club member(s) have attendance below 84.5% (rates: {', '.join(map(str, rates))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_50.csv")

    # Convert numeric columns safely
    for col in ["grade_level", "study_hours_week", "attendance_rate", "test_score"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Ensure club_member is lowercase for comparison
    df["club_member"] = df["club_member"].str.lower()

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