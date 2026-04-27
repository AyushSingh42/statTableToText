import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with an attendance rate of at least 95% are club members."""
    high_att = df[df["attendance_rate"] >= 95]
    if high_att.empty:
        truth = True
        expl = "No students have attendance >= 95%, so the statement holds vacuously."
    else:
        viol = high_att[high_att["club_member"]!= "yes"]
        truth = viol.empty
        if truth:
            expl = f"All {len(high_att)} students with attendance >= 95% are club members."
        else:
            ids = ", ".join(viol["student_id"].tolist())
            expl = f"{len(viol)} student(s) with attendance >= 95% are not club members (IDs: {ids})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All club members have an attendance rate of at least 84.2%."""
    club = df[df["club_member"] == "yes"]
    if club.empty:
        truth = True
        expl = "No club members present, so the statement holds vacuously."
    else:
        viol = club[club["attendance_rate"] < 84.2]
        truth = viol.empty
        if truth:
            expl = f"All {len(club)} club members have attendance >= 84.2%."
        else:
            ids = ", ".join(viol["student_id"].tolist())
            expl = f"{len(viol)} club member(s) have attendance < 84.2% (IDs: {ids})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All non‑club members study at least 5.9 hours per week."""
    non_club = df[df["club_member"]!= "yes"]
    if non_club.empty:
        truth = True
        expl = "No non‑club members present, so the statement holds vacuously."
    else:
        viol = non_club[non_club["study_hours_week"] < 5.9]
        truth = viol.empty
        if truth:
            expl = f"All {len(non_club)} non‑club members study >= 5.9 hours/week."
        else:
            ids = ", ".join(viol["student_id"].tolist())
            expl = f"{len(viol)} non‑club member(s) study < 5.9 hours/week (IDs: {ids})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All grade 12 students have an attendance rate of at least 85.3%."""
    g12 = df[df["grade_level"] == 12]
    if g12.empty:
        truth = True
        expl = "No grade 12 students present, so the statement holds vacuously."
    else:
        viol = g12[g12["attendance_rate"] < 85.3]
        truth = viol.empty
        if truth:
            expl = f"All {len(g12)} grade 12 students have attendance >= 85.3%."
        else:
            ids = ", ".join(viol["student_id"].tolist())
            expl = f"{len(viol)} grade 12 student(s) have attendance < 85.3% (IDs: {ids})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All grade 9 students study at least 5.4 hours per week."""
    g9 = df[df["grade_level"] == 9]
    if g9.empty:
        truth = True
        expl = "No grade 9 students present, so the statement holds vacuously."
    else:
        viol = g9[g9["study_hours_week"] < 5.4]
        truth = viol.empty
        if truth:
            expl = f"All {len(g9)} grade 9 students study >= 5.4 hours/week."
        else:
            ids = ", ".join(viol["student_id"].tolist())
            expl = f"{len(viol)} grade 9 student(s) study < 5.4 hours/week (IDs: {ids})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All grade 10 students have test scores no higher than 65."""
    g10 = df[df["grade_level"] == 10]
    if g10.empty:
        truth = True
        expl = "No grade 10 students present, so the statement holds vacuously."
    else:
        viol = g10[g10["test_score"] > 65]
        truth = viol.empty
        if truth:
            expl = f"All {len(g10)} grade 10 students have test scores <= 65."
        else:
            ids = ", ".join(viol["student_id"].tolist())
            expl = f"{len(viol)} grade 10 student(s) have test scores > 65 (IDs: {ids})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students who study at least 9 hours per week have an attendance rate of at least 85.3%."""
    stud_9 = df[df["study_hours_week"] >= 9]
    if stud_9.empty:
        truth = True
        expl = "No students study >= 9 hours/week, so the statement holds vacuously."
    else:
        viol = stud_9[stud_9["attendance_rate"] < 85.3]
        truth = viol.empty
        if truth:
            expl = f"All {len(stud_9)} students studying >= 9 hours/week have attendance >= 85.3%."
        else:
            ids = ", ".join(viol["student_id"].tolist())
            expl = f"{len(viol)} student(s) studying >= 9 hours/week have attendance < 85.3% (IDs: {ids})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most students have an attendance rate above 85%."""
    total = len(df)
    if total == 0:
        truth = True
        expl = "No students present, so the statement holds vacuously."
    else:
        above_85 = df[df["attendance_rate"] > 85]
        proportion = len(above_85) / total
        truth = proportion > 0.5
        if truth:
            expl = f"{proportion*100:.1f}% of students have attendance > 85%."
        else:
            expl = f"Only {proportion*100:.1f}% of students have attendance > 85%."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most students study at least 5 hours per week."""
    total = len(df)
    if total == 0:
        truth = True
        expl = "No students present, so the statement holds vacuously."
    else:
        at_least_5 = df[df["study_hours_week"] >= 5]
        proportion = len(at_least_5) / total
        truth = proportion > 0.5
        if truth:
            expl = f"{proportion*100:.1f}% of students study >= 5 hours/week."
        else:
            expl = f"Only {proportion*100:.1f}% of students study >= 5 hours/week."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_30.csv")

    # Convert numeric columns safely, except for identifiers and club_member
    for col in df.columns:
        if col not in ["student_id", "club_member"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

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