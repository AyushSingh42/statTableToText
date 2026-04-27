import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with attendance rate above 95% study at least 7.9 hours per week."""
    subset = df[df["attendance_rate"] > 95]
    condition = subset["study_hours_week"] >= 7.9
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with attendance >95% study at least 7.9 hours."
    else:
        viol = subset[~condition]
        viol_ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All 11th graders have test scores of at least 76."""
    subset = df[df["grade_level"] == 11]
    condition = subset["test_score"] >= 76
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} 11th graders have test scores ≥ 76."
    else:
        viol = subset[~condition]
        viol_ids = viol["student_id"].tolist()
        expl = f"{len(viol)} 11th graders violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All 10th graders have attendance rates of at least 87.2%."""
    subset = df[df["grade_level"] == 10]
    condition = subset["attendance_rate"] >= 87.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} 10th graders have attendance ≥ 87.2%."
    else:
        viol = subset[~condition]
        viol_ids = viol["student_id"].tolist()
        expl = f"{len(viol)} 10th graders violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All students who study 2.5 hours or less per week have test scores of at least 76."""
    subset = df[df["study_hours_week"] <= 2.5]
    condition = subset["test_score"] >= 76
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students studying ≤ 2.5 hours have test scores ≥ 76."
    else:
        viol = subset[~condition]
        viol_ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All students with test scores of 90 or higher have attendance rates of at least 87.4%."""
    subset = df[df["test_score"] >= 90]
    condition = subset["attendance_rate"] >= 87.4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test scores ≥ 90 have attendance ≥ 87.4%."
    else:
        viol = subset[~condition]
        viol_ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students study more than 5 hours per week."""
    total = len(df)
    count = (df["study_hours_week"] > 5).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of students study >5 hours, which is more than 50%."
    else:
        expl = f"{proportion*100:.1f}% of students study >5 hours, which is not more than 50%."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All 9th‑grade students who are club members have test scores of at least 76."""
    subset = df[(df["grade_level"] == 9) & (df["club_member"].str.lower() == "yes")]
    condition = subset["test_score"] >= 76
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} 9th‑grade club members have test scores ≥ 76."
    else:
        viol = subset[~condition]
        viol_ids = viol["student_id"].tolist()
        expl = f"{len(viol)} 9th‑grade club members violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All 9th‑grade students who study 2.5 hours or less per week have attendance rates of at least 87.4%."""
    subset = df[(df["grade_level"] == 9) & (df["study_hours_week"] <= 2.5)]
    condition = subset["attendance_rate"] >= 87.4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} 9th‑grade students studying ≤ 2.5 hours have attendance ≥ 87.4%."
    else:
        viol = subset[~condition]
        viol_ids = viol["student_id"].tolist()
        expl = f"{len(viol)} students violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_0.csv")

    # Convert numeric columns where possible
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')

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