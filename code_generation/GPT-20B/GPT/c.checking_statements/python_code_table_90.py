import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all students who study at least 9 hours per week, the test score is at least 83."""
    subset = df[df["study_hours_week"] >= 9]
    condition = subset["test_score"] >= 83
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students studying >=9 hours have test scores >=83."
    else:
        viol = subset[~condition]
        expl = (
            f"{len(viol)} students violate the rule "
            f"(study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))}, "
            f"test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
        )
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all students with a test score of 90 or higher, the attendance rate is at least 86.6%."""
    subset = df[df["test_score"] >= 90]
    condition = subset["attendance_rate"] >= 86.6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test score >=90 have attendance >=86.6%."
    else:
        viol = subset[~condition]
        expl = (
            f"{len(viol)} students violate the rule "
            f"(test scores: {', '.join(map(str, viol['test_score'].tolist()))}, "
            f"attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
        )
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All students with an attendance rate of 95% or higher are members of a club."""
    subset = df[df["attendance_rate"] >= 95]
    condition = subset["club_member"].str.lower() == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with attendance >=95% are club members."
    else:
        viol = subset[~condition]
        expl = (
            f"{len(viol)} students violate the rule "
            f"(attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))}, "
            f"club membership: {', '.join(viol['club_member'].tolist()))})."
        )
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All grade 12 students who are club members have test scores of at most 92."""
    subset = df[(df["grade_level"] == 12) & (df["club_member"].str.lower() == "yes")]
    condition = subset["test_score"] <= 92
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} grade 12 club members have test scores <=92."
    else:
        viol = subset[~condition]
        expl = (
            f"{len(viol)} students violate the rule "
            f"(test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
        )
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. There exists at least one student who studies less than 3 hours per week and has a test score of at least 71."""
    subset = df[(df["study_hours_week"] < 3) & (df["test_score"] >= 71)]
    truth = not subset.empty
    if truth:
        expl = f"Found {len(subset)} student(s) meeting the criteria."
    else:
        expl = "No student meets the criteria."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most students have a test score of at least 75."""
    total = len(df)
    count = df[df["test_score"] >= 75].shape[0]
    proportion = count / total if total > 0 else 0
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of students have test scores >=75."
    else:
        expl = f"Only {proportion*100:.1f}% of students have test scores >=75."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_90.csv")

    # Convert numeric columns (except student_id and club_member)
    for col in df.columns:
        if col not in ["student_id", "club_member"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Normalize club_member to lowercase for consistency
    df["club_member"] = df["club_member"].str.lower()

    checks = [
        (1, stmt_1),
        (2, stmt_2),
        (3, stmt_3),
        (4, stmt_4),
        (5, stmt_5),
        (6, stmt_6),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()