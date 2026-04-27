import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients aged 65 or older have asthma."""
    aged_65_plus = df[df["age"] >= 65]
    if aged_65_plus.empty:
        return True, "No patients aged 65 or older, so the statement holds vacuously."
    condition = aged_65_plus["diagnosis"].str.lower() == "asthma"
    truth = condition.all()
    if truth:
        expl = f"All {len(aged_65_plus)} patients aged 65+ have asthma."
    else:
        viol = aged_65_plus[~condition]
        expl = f"{len(viol)} patients aged 65+ do not have asthma (ids: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hypertension patients have systolic blood pressure at least 148 mmHg."""
    hypertension = df[df["diagnosis"].str.lower() == "hypertension"]
    if hypertension.empty:
        return True, "No hypertension patients, so the statement holds vacuously."
    condition = hypertension["bp_systolic"] >= 148
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension)} hypertension patients have systolic BP >= 148."
    else:
        viol = hypertension[~condition]
        expl = f"{len(viol)} hypertension patients have systolic BP < 148 (ids: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hypertension patients have diastolic blood pressure at most 83 mmHg."""
    hypertension = df[df["diagnosis"].str.lower() == "hypertension"]
    if hypertension.empty:
        return True, "No hypertension patients, so the statement holds vacuously."
    condition = hypertension["bp_diastolic"] <= 83
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension)} hypertension patients have diastolic BP <= 83."
    else:
        viol = hypertension[~condition]
        expl = f"{len(viol)} hypertension patients have diastolic BP > 83 (ids: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All diabetes patients are 35 years old or younger."""
    diabetes = df[df["diagnosis"].str.lower() == "diabetes"]
    if diabetes.empty:
        return True, "No diabetes patients, so the statement holds vacuously."
    condition = diabetes["age"] <= 35
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetes)} diabetes patients are 35 or younger."
    else:
        viol = diabetes[~condition]
        expl = f"{len(viol)} diabetes patients are older than 35 (ids: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All arthritis patients have diastolic blood pressure at least 74 mmHg."""
    arthritis = df[df["diagnosis"].str.lower() == "arthritis"]
    if arthritis.empty:
        return True, "No arthritis patients, so the statement holds vacuously."
    condition = arthritis["bp_diastolic"] >= 74
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritis)} arthritis patients have diastolic BP >= 74."
    else:
        viol = arthritis[~condition]
        expl = f"{len(viol)} arthritis patients have diastolic BP < 74 (ids: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All asthma patients have systolic blood pressure between 116 and 154 mmHg inclusive."""
    asthma = df[df["diagnosis"].str.lower() == "asthma"]
    if asthma.empty:
        return True, "No asthma patients, so the statement holds vacuously."
    condition = asthma["bp_systolic"].between(116, 154, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients have systolic BP between 116 and 154."
    else:
        viol = asthma[~condition]
        expl = f"{len(viol)} asthma patients have systolic BP outside 116-154 (ids: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All smokers have cholesterol level at least 176 mg/dL."""
    smokers = df[df["smoker"].str.lower() == "yes"]
    if smokers.empty:
        return True, "No smokers, so the statement holds vacuously."
    condition = smokers["cholesterol_mg_dl"] >= 176
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have cholesterol >= 176."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers have cholesterol < 176 (ids: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All non-smokers have cholesterol level at most 193 mg/dL."""
    nonsmokers = df[df["smoker"].str.lower() == "no"]
    if nonsmokers.empty:
        return True, "No non-smokers, so the statement holds vacuously."
    condition = nonsmokers["cholesterol_mg_dl"] <= 193
    truth = condition.all()
    if truth:
        expl = f"All {len(nonsmokers)} non-smokers have cholesterol <= 193."
    else:
        viol = nonsmokers[~condition]
        expl = f"{len(viol)} non-smokers have cholesterol > 193 (ids: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most patients in the table are smokers."""
    total = len(df)
    smokers = df[df["smoker"].str.lower() == "yes"]
    count_smokers = len(smokers)
    truth = count_smokers > total / 2
    if truth:
        expl = f"{count_smokers}/{total} patients are smokers ({count_smokers/total:.1%})."
    else:
        expl = f"{count_smokers}/{total} patients are smokers ({count_smokers/total:.1%}), which is not a majority."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All patients with BMI of 30 or higher have cholesterol of at least 190 mg/dL."""
    high_bmi = df[df["bmi"] >= 30]
    if high_bmi.empty:
        return True, "No patients with BMI >= 30, so the statement holds vacuously."
    condition = high_bmi["cholesterol_mg_dl"] >= 190
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI >= 30 have cholesterol >= 190."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI >= 30 have cholesterol < 190 (ids: {', '.join(viol['patient_id'])})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_31.csv")

    # Convert numeric columns
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
        (10, stmt_10),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()