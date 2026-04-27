import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All club members have attendance rates of at least 90%."""
    club = df[df["club_member"].str.lower() == "yes"]
    condition = club["attendance_rate"] >= 90
    truth = condition.all()
    if truth:
        expl = f"All {len(club)} club members have attendance >= 90%."
    else:
        viol = club[~condition]
        expl = f"{len(viol)} club members violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. No club member has a test score of 90 or above."""
    club = df[df["club_member"].str.lower() == "yes"]
    condition = club["test_score"] < 90
    truth = condition.all()
    if truth:
        expl = f"All {len(club)} club members have test scores below 90."
    else:
        viol = club[~condition]
        expl = f"{len(viol)} club members violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All 9th-grade students study at least 4.3 hours per week."""
    ninth = df[df["grade_level"] == 9]
    condition = ninth["study_hours_week"] >= 4.3
    truth = condition.all()
    if truth:
        expl = f"All {len(ninth)} 9th graders study >= 4.3 hours."
    else:
        viol = ninth[~condition]
        expl = f"{len(viol)} 9th graders violate the rule (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All 10th graders have attendance rates of at least 97%."""
    tenth = df[df["grade_level"] == 10]
    condition = tenth["attendance_rate"] >= 97
    truth = condition.all()
    if truth:
        expl = f"All {len(tenth)} 10th graders have attendance >= 97%."
    else:
        viol = tenth[~condition]
        expl = f"{len(viol)} 10th graders violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All 11th graders study at least 3.2 hours per week."""
    eleventh = df[df["grade_level"] == 11]
    condition = eleventh["study_hours_week"] >= 3.2
    truth = condition.all()
    if truth:
        expl = f"All {len(eleventh)} 11th graders study >= 3.2 hours."
    else:
        viol = eleventh[~condition]
        expl = f"{len(viol)} 11th graders violate the rule (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All 12th graders study at least 4.3 hours per week."""
    twelfth = df[df["grade_level"] == 12]
    condition = twelfth["study_hours_week"] >= 4.3
    truth = condition.all()
    if truth:
        expl = f"All {len(twelfth)} 12th graders study >= 4.3 hours."
    else:
        viol = twelfth[~condition]
        expl = f"{len(viol)} 12th graders violate the rule (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most students have attendance rates of at least 90%."""
    condition = df["attendance_rate"] >= 90
    proportion = condition.mean()
    truth = proportion > 0.5
    percent = round(proportion * 100, 1)
    if truth:
        expl = f"{percent}% of students have attendance >= 90%."
    else:
        expl = f"Only {percent}% of students have attendance >= 90%."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All students who study at least 9 hours per week achieve test scores of at least 64."""
    heavy = df[df["study_hours_week"] >= 9]
    condition = heavy["test_score"] >= 64
    truth = condition.all()
    if truth:
        expl = f"All {len(heavy)} students studying >= 9 hours have test scores >= 64."
    else:
        viol = heavy[~condition]
        expl = f"{len(viol)} students studying >= 9 hours violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All students with test scores of 68 or lower have attendance rates of at least 91.6%."""
    low_test = df[df["test_score"] <= 68]
    condition = low_test["attendance_rate"] >= 91.6
    truth = condition.all()
    if truth:
        expl = f"All {len(low_test)} students with test <= 68 have attendance >= 91.6%."
    else:
        viol = low_test[~condition]
        expl = f"{len(viol)} students with test <= 68 violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_70.csv")

    # Convert numeric columns safely, keep club_member as string
    for col in df.columns:
        if col!= "club_member":
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