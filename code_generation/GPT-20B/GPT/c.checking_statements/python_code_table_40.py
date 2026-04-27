import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. If a student's attendance rate is at least 96.1%, their test score is at least 81."""
    subset = df[df["attendance_rate"] >= 96.1]
    if subset.empty:
        return True, "No students have attendance rate >= 96.1%, so the rule holds vacuously."
    truth = (subset["test_score"] >= 81).all()
    if truth:
        return True, f"All {len(subset)} students with attendance >= 96.1% have test score >= 81."
    viol = subset[subset["test_score"] < 81]
    return False, f"{len(viol)} students violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))}, test_score: {', '.join(map(str, viol['test_score'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. All club members have an attendance rate of at least 89.6%."""
    members = df[df["club_member"].str.lower() == "yes"]
    if members.empty:
        return True, "No club members, so the rule holds vacuously."
    truth = (members["attendance_rate"] >= 89.6).all()
    if truth:
        return True, f"All {len(members)} club members have attendance rate >= 89.6%."
    viol = members[members["attendance_rate"] < 89.6]
    return False, f"{len(viol)} club members violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. All 10th‑grade students have an attendance rate of at least 90.9%."""
    tenth = df[df["grade_level"] == 10]
    if tenth.empty:
        return True, "No 10th‑grade students, so the rule holds vacuously."
    truth = (tenth["attendance_rate"] >= 90.9).all()
    if truth:
        return True, f"All {len(tenth)} 10th‑grade students have attendance rate >= 90.9%."
    viol = tenth[tenth["attendance_rate"] < 90.9]
    return False, f"{len(viol)} 10th‑grade students violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."

def stmt_4(df: pd.DataFrame):
    """4. All 12th‑grade students have test scores no higher than 92."""
    twelfth = df[df["grade_level"] == 12]
    if twelfth.empty:
        return True, "No 12th‑grade students, so the rule holds vacuously."
    truth = (twelfth["test_score"] <= 92).all()
    if truth:
        return True, f"All {len(twelfth)} 12th‑grade students have test scores <= 92."
    viol = twelfth[twelfth["test_score"] > 92]
    return False, f"{len(viol)} 12th‑grade students violate the rule (test_score: {', '.join(map(str, viol['test_score'].tolist()))})."

def stmt_5(df: pd.DataFrame):
    """5. All students who study more than 9 hours per week have an attendance rate of at least 89%."""
    subset = df[df["study_hours_week"] > 9]
    if subset.empty:
        return True, "No students study more than 9 hours per week, so the rule holds vacuously."
    truth = (subset["attendance_rate"] >= 89).all()
    if truth:
        return True, f"All {len(subset)} students studying >9h/week have attendance rate >= 89%."
    viol = subset[subset["attendance_rate"] < 89]
    return False, f"{len(viol)} students violate the rule (attendance: {', '.join(map(str, viol['attendance_rate'].tolist()))})."

def stmt_6(df: pd.DataFrame):
    """6. All students who study at least 10 hours per week have test scores of at most 69."""
    subset = df[df["study_hours_week"] >= 10]
    if subset.empty:
        return True, "No students study at least 10 hours per week, so the rule holds vacuously."
    truth = (subset["test_score"] <= 69).all()
    if truth:
        return True, f"All {len(subset)} students studying >=10h/week have test scores <= 69."
    viol = subset[subset["test_score"] > 69]
    return False, f"{len(viol)} students violate the rule (test_score: {', '.join(map(str, viol['test_score'].tolist()))})."

def stmt_7(df: pd.DataFrame):
    """7. All students scoring below 70 are in grade 9 or grade 12."""
    subset = df[df["test_score"] < 70]
    if subset.empty:
        return True, "No students score below 70, so the rule holds vacuously."
    truth = subset["grade_level"].isin([9, 12]).all()
    if truth:
        return True, f"All {len(subset)} students with test score < 70 are in grade 9 or 12."
    viol = subset[~subset["grade_level"].isin([9, 12])]
    return False, f"{len(viol)} students violate the rule (grade_level: {', '.join(map(str, viol['grade_level'].tolist()))})."

def stmt_8(df: pd.DataFrame):
    """8. Most club members have test scores above 80."""
    members = df[df["club_member"].str.lower() == "yes"]
    if members.empty:
        return False, "No club members to evaluate majority."
    proportion = (members["test_score"] > 80).mean()
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% of club members have test scores > 80, which is a majority."
    else:
        return False, f"Only {proportion*100:.1f}% of club members have test scores > 80, which is not a majority."

def main():
    df = pd.read_csv("../inference_generation/tables/table_40.csv")

    # Convert numeric columns safely
    numeric_cols = ["grade_level", "study_hours_week", "attendance_rate", "test_score"]
    for col in numeric_cols:
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()