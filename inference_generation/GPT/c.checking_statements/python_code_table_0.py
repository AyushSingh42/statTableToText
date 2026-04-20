import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # Convert possible numeric columns stored as strings to proper dtypes
    numeric_cols = ["grade_level", "study_hours_week", "attendance_rate", "test_score"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    # Convert club_member to boolean (accept 0/1, True/False, yes/no)
    if "club_member" in df.columns:
        df["club_member"] = df["club_member"].map(
            {"True": True, "true": True, "1": True, "yes": True, "Yes": True,
             "False": False, "false": False, "0": False, "no": False, "No": False}
        ).fillna(df["club_member"]).astype(bool)
    return df

def stmt_1(df: pd.DataFrame):
    """All students who are club members have attendance rates above 89%."""
    members = df[df["club_member"]]
    condition = members["attendance_rate"] > 89
    truth = condition.all()
    if truth:
        expl = f"All {len(members)} club members have attendance > 89%."
    else:
        viol = members[~condition]
        expl = f"{len(viol)} club members violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """All 12th‑grade students scored at least 78 on the test."""
    twelfth = df[df["grade_level"] == 12]
    condition = twelfth["test_score"] >= 78
    truth = condition.all()
    if truth:
        expl = f"All {len(twelfth)} 12th‑grade students scored ≥ 78."
    else:
        viol = twelfth[~condition]
        expl = f"{len(viol)} 12th‑graders scored below 78 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """All students who study more than 9 hours per week scored 90 or higher on the test."""
    heavy = df[df["study_hours_week"] > 9]
    condition = heavy["test_score"] >= 90
    truth = condition.all()
    if truth:
        expl = f"All {len(heavy)} students studying >9 hrs/week scored ≥ 90."
    else:
        viol = heavy[~condition]
        expl = f"{len(viol)} students studying >9 hrs/week scored below 90 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """Most 10th‑grade students are not members of a club."""
    tenth = df[df["grade_level"] == 10]
    total = len(tenth)
    not_members = tenth[~tenth["club_member"]]
    count_not = len(not_members)
    truth = count_not > total / 2
    if total == 0:
        expl = "No 10th‑grade students in data; cannot evaluate."
        truth = False
    else:
        expl = f"{count_not} out of {total} (≈{count_not/total:.1%}) 10th‑graders are not club members."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """The student with the highest attendance rate (99.1%) also achieved the highest test score (95)."""
    max_att = df["attendance_rate"].max()
    max_score = df["test_score"].max()
    top_att_rows = df[df["attendance_rate"] == max_att]
    same_student = top_att_rows["test_score"].eq(max_score).all()
    truth = (abs(max_att - 99.1) < 1e-6) and (abs(max_score - 95) < 1e-6) and same_student
    if truth:
        expl = f"Highest attendance is 99.1% and highest test score is 95, both belonging to the same student."
    else:
        expl = (f"Highest attendance = {max_att} (expected 99.1). "
                f"Highest test score = {max_score} (expected 95). "
                f"Student(s) with max attendance have scores: {', '.join(map(str, top_att_rows['test_score'].tolist()))}.")
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """All students with attendance rates of 95% or higher scored at least 88 on the test."""
    high_att = df[df["attendance_rate"] >= 95]
    condition = high_att["test_score"] >= 88
    truth = condition.all()
    if truth:
        expl = f"All {len(high_att)} students with attendance ≥95% scored ≥88."
    else:
        viol = high_att[~condition]
        expl = f"{len(viol)} students with attendance ≥95% scored below 88 (scores: {', '.join(map(str, viol['test_score'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """There is at least one 9th‑grader who studied fewer than 5 hours per week and scored below 70 on the test."""
    subset = df[
        (df["grade_level"] == 9) &
        (df["study_hours_week"] < 5) &
        (df["test_score"] < 70)
    ]
    truth = not subset.empty
    if truth:
        expl = f"Found {len(subset)} matching 9th‑grader(s) (student_id(s): {', '.join(map(str, subset['student_id'].tolist()))})."
    else:
        expl = "No 9th‑grader meets all three conditions."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """The majority of club members (7 out of 8) earned test scores above 80."""
    members = df[df["club_member"]]
    total = len(members)
    above80 = members[members["test_score"] > 80]
    count_above = len(above80)
    truth = (total == 8) and (count_above >= 7)
    if total == 0:
        expl = "No club members in data; cannot evaluate."
        truth = False
    else:
        expl = f"{count_above} out of {total} club members scored >80."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_0.csv")
    df = clean_dataframe(df)

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