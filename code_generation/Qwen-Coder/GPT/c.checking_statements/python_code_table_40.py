import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. If a student's attendance rate is at least 96.1%, their test score is at least 81."""
    condition = (df['attendance_rate'] >= 96.1) & (df['test_score'] < 81)
    truth = not condition.any()
    if truth:
        expl = "No student with attendance >= 96.1% has test score < 81."
    else:
        viol = df[condition]
        expl = f"{len(viol)} student(s) violate the rule (attendance >= 96.1% but test score < 81)."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All club members have an attendance rate of at least 89.6%."""
    club_members = df[df['club_member'] == 'yes']
    condition = club_members['attendance_rate'] < 89.6
    truth = not condition.any()
    if truth:
        expl = f"All {len(club_members)} club members have attendance >= 89.6%."
    else:
        viol = club_members[condition]
        expl = f"{len(viol)} club member(s) violate the rule (attendance < 89.6%)."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All 10th-grade students have an attendance rate of at least 90.9%."""
    tenth_graders = df[df['grade_level'] == 10]
    condition = tenth_graders['attendance_rate'] < 90.9
    truth = not condition.any()
    if truth:
        expl = f"All {len(tenth_graders)} 10th-grade students have attendance >= 90.9%."
    else:
        viol = tenth_graders[condition]
        expl = f"{len(viol)} 10th-grade student(s) violate the rule (attendance < 90.9%)."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All 12th-grade students have test scores no higher than 92."""
    twelfth_graders = df[df['grade_level'] == 12]
    condition = twelfth_graders['test_score'] > 92
    truth = not condition.any()
    if truth:
        expl = f"All {len(twelfth_graders)} 12th-grade students have test score <= 92."
    else:
        viol = twelfth_graders[condition]
        expl = f"{len(viol)} 12th-grade student(s) violate the rule (test score > 92)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All students who study more than 9 hours per week have an attendance rate of at least 89%."""
    studious = df[df['study_hours_week'] > 9]
    condition = studious['attendance_rate'] < 89
    truth = not condition.any()
    if truth:
        expl = f"All {len(studious)} students studying > 9 hours/week have attendance >= 89%."
    else:
        viol = studious[condition]
        expl = f"{len(viol)} student(s) studying > 9 hours/week violate the rule (attendance < 89%)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All students who study at least 10 hours per week have test scores of at most 69."""
    very_studious = df[df['study_hours_week'] >= 10]
    condition = very_studious['test_score'] > 69
    truth = not condition.any()
    if truth:
        expl = f"All {len(very_studious)} students studying >= 10 hours/week have test score <= 69."
    else:
        viol = very_studious[condition]
        expl = f"{len(viol)} student(s) studying >= 10 hours/week violate the rule (test score > 69)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students scoring below 70 are in grade 9 or grade 12."""
    low_scorers = df[df['test_score'] < 70]
    condition = ~low_scorers['grade_level'].isin([9, 12])
    truth = not condition.any()
    if truth:
        expl = f"All {len(low_scorers)} students scoring below 70 are in grade 9 or 12."
    else:
        viol = low_scorers[condition]
        expl = f"{len(viol)} student(s) scoring below 70 are not in grade 9 or 12."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most club members have test scores above 80."""
    club_members = df[df['club_member'] == 'yes']
    above_80 = club_members[club_members['test_score'] > 80]
    truth = len(above_80) > len(club_members) / 2
    if truth:
        expl = f"{len(above_80)} out of {len(club_members)} club members have test score > 80."
    else:
        expl = f"Only {len(above_80)} out of {len(club_members)} club members have test score > 80."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_40.csv")

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