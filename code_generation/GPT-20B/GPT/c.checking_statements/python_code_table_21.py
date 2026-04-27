import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients younger than 30 years have a diagnosis of diabetes."""
    young = df[df["age"] < 30]
    if young.empty:
        return True, "No patients younger than 30, statement vacuously true."
    condition = young["diagnosis"] == "diabetes"
    truth = condition.all()
    if truth:
        return True, f"All {len(young)} patients younger than 30 have diabetes."
    viol = young[~condition]
    ids = viol["patient_id"].tolist()
    return False, f"{len(viol)} patients violate the rule (patient_ids: {', '.join(ids)})."

def stmt_2(df: pd.DataFrame):
    """2. All patients diagnosed with diabetes have cholesterol levels of at least 207 mg/dL."""
    diag = df[df["diagnosis"] == "diabetes"]
    if diag.empty:
        return True, "No patients diagnosed with diabetes, statement vacuously true."
    condition = diag["cholesterol_mg_dl"] >= 207
    truth = condition.all()
    if truth:
        return True, f"All {len(diag)} diabetic patients have cholesterol ≥ 207 mg/dL."
    viol = diag[~condition]
    ids = viol["patient_id"].tolist()
    return False, f"{len(viol)} diabetic patients violate the rule (patient_ids: {', '.join(ids)})."

def stmt_3(df: pd.DataFrame):
    """3. All smokers have a body‑mass index of at least 25."""
    smokers = df[df["smoker"].str.lower() == "yes"]
    if smokers.empty:
        return True, "No smokers, statement vacuously true."
    condition = smokers["bmi"] >= 25
    truth = condition.all()
    if truth:
        return True, f"All {len(smokers)} smokers have BMI ≥ 25."
    viol = smokers[~condition]
    ids = viol["patient_id"].tolist()
    return False, f"{len(viol)} smokers violate the rule (patient_ids: {', '.join(ids)})."

def stmt_4(df: pd.DataFrame):
    """4. All patients with hypertension have a systolic blood pressure of at least 148 mmHg."""
    hypos = df[df["diagnosis"] == "hypertension"]
    if hypos.empty:
        return True, "No patients with hypertension, statement vacuously true."
    condition = hypos["bp_systolic"] >= 148
    truth = condition.all()
    if truth:
        return True, f"All {len(hypos)} hypertensive patients have systolic BP ≥ 148 mmHg."
    viol = hypos[~condition]
    ids = viol["patient_id"].tolist()
    return False, f"{len(viol)} hypertensive patients violate the rule (patient_ids: {', '.join(ids)})."

def stmt_5(df: pd.DataFrame):
    """5. All asthma patients have a diastolic blood pressure no greater than 93 mmHg."""
    asth = df[df["diagnosis"] == "asthma"]
    if asth.empty:
        return True, "No asthma patients, statement vacuously true."
    condition = asth["bp_diastolic"] <= 93
    truth = condition.all()
    if truth:
        return True, f"All {len(asth)} asthma patients have diastolic BP ≤ 93 mmHg."
    viol = asth[~condition]
    ids = viol["patient_id"].tolist()
    return False, f"{len(viol)} asthma patients violate the rule (patient_ids: {', '.join(ids)})."

def stmt_6(df: pd.DataFrame):
    """6. All arthritis patients have cholesterol of at most 180 mg/dL."""
    arth = df[df["diagnosis"] == "arthritis"]
    if arth.empty:
        return True, "No arthritis patients, statement vacuously true."
    condition = arth["cholesterol_mg_dl"] <= 180
    truth = condition.all()
    if truth:
        return True, f"All {len(arth)} arthritis patients have cholesterol ≤ 180 mg/dL."
    viol = arth[~condition]
    ids = viol["patient_id"].tolist()
    return False, f"{len(viol)} arthritis patients violate the rule (patient_ids: {', '.join(ids)})."

def stmt_7(df: pd.DataFrame):
    """7. If a patient’s systolic blood pressure is at least 150 mmHg, then their diastolic pressure is at least 73 mmHg."""
    high_sys = df[df["bp_systolic"] >= 150]
    if high_sys.empty:
        return True, "No patients with systolic BP ≥ 150 mmHg, statement vacuously true."
    condition = high_sys["bp_diastolic"] >= 73
    truth = condition.all()
    if truth:
        return True, f"All {len(high_sys)} patients with systolic BP ≥ 150 mmHg have diastolic BP ≥ 73 mmHg."
    viol = high_sys[~condition]
    ids = viol["patient_id"].tolist()
    return False, f"{len(viol)} patients violate the rule (patient_ids: {', '.join(ids)})."

def stmt_8(df: pd.DataFrame):
    """8. Most patients have cholesterol levels above 200 mg/dL."""
    total = len(df)
    if total == 0:
        return True, "No patients in dataset, statement vacuously true."
    above_200 = df[df["cholesterol_mg_dl"] > 200]
    proportion = len(above_200) / total
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% of patients have cholesterol > 200 mg/dL."
    else:
        return False, f"Only {proportion*100:.1f}% of patients have cholesterol > 200 mg/dL."

def main():
    df = pd.read_csv("../inference_generation/tables/table_21.csv")

    # Convert numeric columns safely
    numeric_cols = ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Ensure smoker column is lower case
    if "smoker" in df.columns:
        df["smoker"] = df["smoker"].astype(str).str.lower()

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