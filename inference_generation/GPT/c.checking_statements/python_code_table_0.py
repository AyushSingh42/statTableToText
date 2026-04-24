import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def _prepare_df(df: pd.DataFrame) -> pd.DataFrame:
    # Convert numeric columns that may be stored as strings
    for col in ["grade_level", "study_hours_week", "attendance_rate", "test_score"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    # Normalise club_member to boolean
    if "club_member" in df.columns:
        df["club_member_bool"] = df["club_member"].astype(str).str.lower().isin(
            {"true", "1", "yes", "y", "t"}
        )
    else:
        df["club_member_bool"] = False
    return df

def stmt_1(df: pd.DataFrame):
    """All students with test scores of 90 or higher are club members."""
    subset = df[df["test_score"] >= 90]
    condition = subset["club_member_bool"]
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} students with test_score ≥ 90 are club members."
    else:
        viol = subset[~condition]
        ids = ", ".join(map(str, viol["student_id"].tolist()))
        expl = f"{len(viol)} students violate the rule (student_id(s): {ids})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """All students who study less than 5 hours per week have test scores of at most 74."""
    subset = df[df["study_hours_week"] < 5]
    condition = subset["test_score"] <= 74
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} low‑study students have test_score ≤ 74."
    else:
        viol = subset[~condition]
        ids = ", ".join(map(str, viol["student_id"].tolist()))
        expl = f"{len(viol)} students violate the rule (student_id(s): {ids})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """All students who study at least 9 hours per week have attendance rates of at least 97%."""
    subset = df[df["study_hours_week"] >= 9]
    condition = subset["attendance_rate"] >= 97
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} high‑study students have attendance_rate ≥ 97%."
    else:
        viol = subset[~condition]
        ids = ", ".join(map(str, viol["student_id"].tolist()))
        expl = f"{len(viol)} students violate the rule (student_id(s): {ids})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """All students with attendance rates of at least 95% study at least 8 hours per week."""
    subset = df[df["attendance_rate"] >= 95]
    condition = subset["study_hours_week"] >= 8
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} well‑attending students study ≥ 8 hrs/week."
    else:
        viol = subset[~condition]
        ids = ", ".join(map(str, viol["student_id"].tolist()))
        expl = f"{len(viol)} students violate the rule (student_id(s): {ids})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """All students with test scores of at least 85 have attendance rates of at least 94.8%."""
    subset = df[df["test_score"] >= 85]
    condition = subset["attendance_rate"] >= 94.8
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} high‑scoring students have attendance_rate ≥ 94.8%."
    else:
        viol = subset[~condition]
        ids = ", ".join(map(str, viol["student_id"].tolist()))
        expl = f"{len(viol)} students violate the rule (student_id(s): {ids})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """All 12th‑grade students have attendance rates of at least 91.2%."""
    subset = df[df["grade_level"] == 12]
    condition = subset["attendance_rate"] >= 91.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} 12th‑grade students have attendance_rate ≥ 91.2%."
    else:
        viol = subset[~condition]
        ids = ", ".join(map(str, viol["student_id"].tolist()))
        expl = f"{len(viol)} 12th‑grade students violate the rule (student_id(s): {ids})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """Most students have attendance rates above 90%."""
    total = len(df)
    count = (df["attendance_rate"] > 90).sum()
    proportion = count / total if total > 0 else 0
    truth = proportion > 0.5
    expl = f"{count}/{total} students ({proportion:.1%}) have attendance_rate > 90%."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """All non‑club members have attendance rates of at most 96.5%."""
    subset = df[~df["club_member_bool"]]
    condition = subset["attendance_rate"] <= 96.5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} non‑club members have attendance_rate ≤ 96.5%."
    else:
        viol = subset[~condition]
        ids = ", ".join(map(str, viol["student_id"].tolist()))
        expl = f"{len(viol)} non‑club members violate the rule (student_id(s): {ids})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_0.csv")
    df = _prepare_df(df)

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