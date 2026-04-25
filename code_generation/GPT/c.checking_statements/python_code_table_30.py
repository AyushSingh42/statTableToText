import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with an attendance rate of at least 95% are club members."""
    condition = df[df['attendance_rate'] >= 95]['club_member'] == 'yes'
    truth = condition.all()
    if truth:
        expl = f"All students with 95%+ attendance are club members."
    else:
        viol = df[(df['attendance_rate'] >= 95) & (df['club_member']!= 'yes')]
        expl = f"{len(viol)} students with 95%+ attendance are not club members."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All club members have an attendance rate of at least 84.2%."""
    condition = df[df['club_member'] == 'yes']['attendance_rate'] >= 84.2
    truth = condition.all()
    if truth:
        expl = f"All club members have 84.2%+ attendance."
    else:
        viol = df[(df['club_member'] == 'yes') & (df['attendance_rate'] < 84.2)]
        expl = f"{len(viol)} club members have < 84.2% attendance."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All non-club members study at least 5.9 hours per week."""
    condition = df[df['club_member'] == 'no']['study_hours_week'] >= 5.9
    truth = condition.all()
    if truth:
        expl = f"All non-club members study 5.9+ hours/week."
    else:
        viol = df[(df['club_member'] == 'no') & (df['study_hours_week'] < 5.9)]
        expl = f"{len(viol)} non-club members study < 5.9 hours/week."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All grade 12 students have an attendance rate of at least 85.3%."""
    condition = df[df['grade_level'] == 12]['attendance_rate'] >= 85.3
    truth = condition.all()
    if truth:
        expl = f"All grade 12 students have 85.3%+ attendance."
    else:
        viol = df[(df['grade_level'] == 12) & (df['attendance_rate'] < 85.3)]
        expl = f"{len(viol)} grade 12 students have < 85.3% attendance."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All grade 9 students study at least 5.4 hours per week."""
    condition = df[df['grade_level'] == 9]['study_hours_week'] >= 5.4
    truth = condition.all()
    if truth:
        expl = f"All grade 9 students study 5.4+ hours/week."
    else:
        viol = df[(df['grade_level'] == 9) & (df['study_hours_week'] < 5.4)]
        expl = f"{len(viol)} grade 9 students study < 5.4 hours/week."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All grade 10 students have test scores no higher than 65."""
    condition = df[df['grade_level'] == 10]['test_score'] <= 65
    truth = condition.all()
    if truth:
        expl = f"All grade 10 students have test scores ≤ 65."
    else:
        viol = df[(df['grade_level'] == 10) & (df['test_score'] > 65)]
        expl = f"{len(viol)} grade 10 students have test scores > 65."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students who study at least 9 hours per week have an attendance rate of at least 85.3%."""
    condition = df[df['study_hours_week'] >= 9]['attendance_rate'] >= 85.3
    truth = condition.all()
    if truth:
        expl = f"All students studying 9+ hours/week have 85.3%+ attendance."
    else:
        viol = df[(df['study_hours_week'] >= 9) & (df['attendance_rate'] < 85.3)]
        expl = f"{len(viol)} students studying 9+ hours/week have < 85.3% attendance."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most students have an attendance rate above 85%."""
    total = len(df)
    above_85 = len(df[df['attendance_rate'] > 85])
    truth = above_85 > total / 2
    if truth:
        expl = f"{above_85} out of {total} students (>50%) have >85% attendance."
    else:
        expl = f"{above_85} out of {total} students (≤50%) have >85% attendance."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most students study at least 5 hours per week."""
    total = len(df)
    at_least_5 = len(df[df['study_hours_week'] >= 5])
    truth = at_least_5 > total / 2
    if truth:
        expl = f"{at_least_5} out of {total} students (>50%) study ≥5 hours/week."
    else:
        expl = f"{at_least_5} out of {total} students (≤50%) study ≥5 hours/week."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_30.csv")

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