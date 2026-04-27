import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hypertension patients have diastolic blood pressure of at least 85 mmHg."""
    hypos = df[df["diagnosis"].str.lower() == "hypertension"]
    condition = hypos["bp_diastolic"] >= 85
    truth = condition.all()
    if truth:
        expl = f"All {len(hypos)} hypertension patients have diastolic BP ≥ 85."
    else:
        viol = hypos[~condition]
        expl = f"{len(viol)} hypertension patients violate the rule (diastolic BP: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hypertension patients have systolic blood pressure between 119 and 148 mmHg."""
    hypos = df[df["diagnosis"].str.lower() == "hypertension"]
    condition = hypos["bp_systolic"].between(119, 148, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(hypos)} hypertension patients have systolic BP between 119 and 148."
    else:
        viol = hypos[~condition]
        expl = f"{len(viol)} hypertension patients violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All patients aged 20 to 30 have cholesterol at most 212 mg/dL."""
    age_group = df[df["age"].between(20, 30, inclusive="both")]
    condition = age_group["cholesterol_mg_dl"] <= 212
    truth = condition.all()
    if truth:
        expl = f"All {len(age_group)} patients aged 20-30 have cholesterol ≤ 212."
    else:
        viol = age_group[~condition]
        expl = f"{len(viol)} patients aged 20-30 violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All asthma patients have cholesterol levels between 184 and 241 mg/dL."""
    asthmatics = df[df["diagnosis"].str.lower() == "asthma"]
    condition = asthmatics["cholesterol_mg_dl"].between(184, 241, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(asthmatics)} asthma patients have cholesterol between 184 and 241."
    else:
        viol = asthmatics[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most patients have diastolic blood pressure of at least 85 mmHg."""
    total = len(df)
    count = (df["bp_diastolic"] >= 85).sum()
    proportion = count / total
    truth = proportion > 0.5
    expl = f"{count} out of {total} patients have diastolic BP ≥ 85 ({proportion*100:.1f}%)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most patients are non-smokers."""
    total = len(df)
    non_smokers = (df["smoker"].str.lower() == "no").sum()
    proportion = non_smokers / total
    truth = proportion > 0.5
    expl = f"{non_smokers} out of {total} patients are non-smokers ({proportion*100:.1f}%)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All patients with cholesterol at most 200 mg/dL have a BMI of at most 27.3."""
    low_chol = df[df["cholesterol_mg_dl"] <= 200]
    condition = low_chol["bmi"] <= 27.3
    truth = condition.all()
    if truth:
        expl = f"All {len(low_chol)} patients with cholesterol ≤ 200 have BMI ≤ 27.3."
    else:
        viol = low_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol ≤ 200 violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is 30 years old or younger, then their systolic blood pressure does not exceed 148 mmHg."""
    young = df[df["age"] <= 30]
    condition = young["bp_systolic"] <= 148
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} patients aged ≤ 30 have systolic BP ≤ 148."
    else:
        viol = young[~condition]
        expl = f"{len(viol)} patients aged ≤ 30 violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All patients with a BMI of 33 or higher have a diagnosis of diabetes, arthritis, or hypertension."""
    high_bmi = df[df["bmi"] >= 33]
    allowed = ["diabetes", "arthritis", "hypertension"]
    condition = high_bmi["diagnosis"].str.lower().isin(allowed)
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI ≥ 33 have one of the allowed diagnoses."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI ≥ 33 violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_61.csv")

    # Convert numeric columns safely
    numeric_cols = ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Ensure smoker column is lower case
    if "smoker" in df.columns:
        df["smoker"] = df["smoker"].str.lower()

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