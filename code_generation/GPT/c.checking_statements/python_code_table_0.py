import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with attendance rate above 95% study at least 7.9 hours per week."""
    condition = df[df["attendance_rate"] > 95]["study_hours_week"] >= 7.9
    truth = condition.all()
    if truth:
        expl = f"All students with attendance >95% study >=7.9 hours/week ({len(condition[condition])} out of {len(df[df['attendance_rate'] > 95])})"
    else:
        viol = df[(df["attendance_rate"] > 95) & (df["study_hours_week"] < 7.9)]
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(viol['student_id'].tolist())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All 11th graders have test scores of at least 76."""
    condition = df[df["grade_level"] == 11]["test_score"] >= 76
    truth = condition.all()
    if truth:
        expl = f"All 11th graders have test score >=76 ({len(condition[condition])} out of {len(df[df['grade_level'] == 11])})"
    else:
        viol = df[(df["grade_level"] == 11) & (df["test_score"] < 76)]
        expl = f"{len(viol)} 11th graders violate the rule (IDs: {', '.join(viol['student_id'].tolist())})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All 10th graders have attendance rates of at least 87.2%."""
    condition = df[df["grade_level"] == 10]["attendance_rate"] >= 87.2
    truth = condition.all()
    if truth:
        expl = f"All 10th graders have attendance >=87.2% ({len(condition[condition])} out of {len(df[df['grade_level'] == 10])})"
    else:
        viol = df[(df["grade_level"] == 10) & (df["attendance_rate"] < 87.2)]
        expl = f"{len(viol)} 10th graders violate the rule (IDs: {', '.join(viol['student_id'].tolist())})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All students who study 2.5 hours or less per week have test scores of at least 76."""
    condition = df[df["study_hours_week"] <= 2.5]["test_score"] >= 76
    truth = condition.all()
    if truth:
        expl = f"All students studying <=2.5 hours/week have test score >=76 ({len(condition[condition])} out of {len(df[df['study_hours_week'] <= 2.5])})"
    else:
        viol = df[(df["study_hours_week"] <= 2.5) & (df["test_score"] < 76)]
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(viol['student_id'].tolist())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All students with test scores of 90 or higher have attendance rates of at least 87.4%."""
    condition = df[df["test_score"] >= 90]["attendance_rate"] >= 87.4
    truth = condition.all()
    if truth:
        expl = f"All students with test score >=90 have attendance >=87.4% ({len(condition[condition])} out of {len(df[df['test_score'] >= 90])})"
    else:
        viol = df[(df["test_score"] >= 90) & (df["attendance_rate"] < 87.4)]
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(viol['student_id'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students study more than 5 hours per week."""
    condition = df["study_hours_week"] > 5
    count = len(condition[condition])
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} students study >5 hours/week. {'Yes' if truth else 'No'}."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All 9th-grade students who are club members have test scores of at least 76."""
    condition = (df["grade_level"] == 9) & (df["club_member"] == "yes")
    subset = df[condition]
    if len(subset) == 0:
        expl = "No 9th-grade club members found."
        truth = True
    else:
        valid = subset["test_score"] >= 76
        truth = valid.all()
        if truth:
            expl = f"All {len(subset)} 9th-grade club members have test score >=76."
        else:
            viol = subset[~valid]
            expl = f"{len(viol)} 9th-grade club members violate the rule (IDs: {', '.join(viol['student_id'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All 9th-grade students who study 2.5 hours or less per week have attendance rates of at least 87.4%."""
    condition = (df["grade_level"] == 9) & (df["study_hours_week"] <= 2.5)
    subset = df[condition]
    if len(subset) == 0:
        expl = "No 9th-grade students studying <=2.5 hours/week found."
        truth = True
    else:
        valid = subset["attendance_rate"] >= 87.4
        truth = valid.all()
        if truth:
            expl = f"All {len(subset)} 9th-grade students studying <=2.5 hours/week have attendance >=87.4%."
        else:
            viol = subset[~valid]
            expl = f"{len(viol)} 9th-grade students violate the rule (IDs: {', '.join(viol['student_id'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_0.csv")

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