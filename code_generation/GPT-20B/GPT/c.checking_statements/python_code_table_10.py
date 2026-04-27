import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All 12th-grade students have a test score of 91."""
    sub = df[df["grade_level"] == 12]
    if sub.empty:
        return True, "No 12th-grade students present; statement vacuously true."
    condition = sub["test_score"] == 91
    truth = condition.all()
    if truth:
        return True, f"All {len(sub)} 12th-grade students have test score 91."
    else:
        viol = sub[~condition]
        return False, f"{len(viol)} 12th-grade students violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. All 9th-grade students have attendance rates greater than 89%."""
    sub = df[df["grade_level"] == 9]
    if sub.empty:
        return True, "No 9th-grade students present; statement vacuously true."
    condition = sub["attendance_rate"] > 89
    truth = condition.all()
    if truth:
        return True, f"All {len(sub)} 9th-grade students have attendance > 89%."
    else:
        viol = sub[~condition]
        return False, f"{len(viol)} 9th-grade students violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. All club members have attendance rates at most 94.5%."""
    sub = df[df["club_member"].str.lower() == "yes"]
    if sub.empty:
        return True, "No club members present; statement vacuously true."
    condition = sub["attendance_rate"] <= 94.5
    truth = condition.all()
    if truth:
        return True, f"All {len(sub)} club members have attendance <= 94.5%."
    else:
        viol = sub[~condition]
        return False, f"{len(viol)} club members violate the rule (attendance rates: {', '.join(map(str, viol['attendance_rate'].tolist()))})."

def stmt_4(df: pd.DataFrame):
    """4. All students who study more than 10 hours per week have test scores no higher than 91."""
    sub = df[df["study_hours_week"] > 10]
    if sub.empty:
        return True, "No students study >10 hours; statement vacuously true."
    condition = sub["test_score"] <= 91
    truth = condition.all()
    if truth:
        return True, f"All {len(sub)} students studying >10h have test score <= 91."
    else:
        viol = sub[~condition]
        return False, f"{len(viol)} students violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."

def stmt_5(df: pd.DataFrame):
    """5. All students with attendance rates below 88% have test scores of at least 86."""
    sub = df[df["attendance_rate"] < 88]
    if sub.empty:
        return True, "No students with attendance <88%; statement vacuously true."
    condition = sub["test_score"] >= 86
    truth = condition.all()
    if truth:
        return True, f"All {len(sub)} students with attendance <88% have test score >= 86."
    else:
        viol = sub[~condition]
        return False, f"{len(viol)} students violate the rule (test scores: {', '.join(map(str, viol['test_score'].tolist()))})."

def stmt_6(df: pd.DataFrame):
    """6. All club members study at least 3.8 hours per week."""
    sub = df[df["club_member"].str.lower() == "yes"]
    if sub.empty:
        return True, "No club members present; statement vacuously true."
    condition = sub["study_hours_week"] >= 3.8
    truth = condition.all()
    if truth:
        return True, f"All {len(sub)} club members study >= 3.8 hours."
    else:
        viol = sub[~condition]
        return False, f"{len(viol)} club members violate the rule (study hours: {', '.join(map(str, viol['study_hours_week'].tolist()))})."

def stmt_7(df: pd.DataFrame):
    """7. Most students have attendance rates above 90%."""
    total = len(df)
    if total == 0:
        return False, "No students in dataset."
    count_above = df[df["attendance_rate"] > 90].shape[0]
    proportion = count_above / total
    truth = proportion > 0.5
    if truth:
        return True, f"{count_above} out of {total} students ({proportion*100:.1f}%) have attendance > 90%."
    else:
        return False, f"{count_above} out of {total} students ({proportion*100:.1f}%) have attendance > 90%; not a majority."

def stmt_8(df: pd.DataFrame):
    """8. The average test score of 11th-grade students is 86.25."""
    sub = df[df["grade_level"] == 11]
    if sub.empty:
        return False, "No 11th-grade students present."
    mean_score = sub["test_score"].mean()
    truth = abs(mean_score - 86.25) < 1e-6
    if truth:
        return True, f"Average test score of 11th-grade students is {mean_score:.2f}."
    else:
        return False, f"Average test score of 11th-grade students is {mean_score:.2f} (expected 86.25)."

def main():
    df = pd.read_csv("../inference_generation/tables/table_10.csv")

    # Convert numeric columns
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