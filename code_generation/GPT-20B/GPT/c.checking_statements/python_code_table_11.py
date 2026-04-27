import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all individuals diagnosed with hypertension, systolic blood pressure does not exceed 135 mmHg."""
    hypos = df[df["diagnosis"] == "hypertension"]
    condition = hypos["bp_systolic"] <= 135
    truth = condition.all()
    if truth:
        expl = f"All {len(hypos)} hypertension patients have systolic ≤ 135."
    else:
        viol = hypos[~condition]
        expl = f"{len(viol)} hypertension patients violate the rule (IDs: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Every patient who is a smoker has a cholesterol level of at least 215 mg/dL."""
    smokers = df[df["smoker"].str.lower() == "yes"]
    condition = smokers["cholesterol_mg_dl"] >= 215
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have cholesterol ≥ 215."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (IDs: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a patient’s cholesterol is 240 mg/dL or higher, the diagnosis is hypertension."""
    high_chol = df["cholesterol_mg_dl"] >= 240
    condition = df.loc[high_chol, "diagnosis"] == "hypertension"
    truth = condition.all()
    if truth:
        expl = f"All patients with cholesterol ≥ 240 are diagnosed with hypertension."
    else:
        viol = df.loc[high_chol & (df["diagnosis"]!= "hypertension")]
        expl = f"{len(viol)} patients with cholesterol ≥ 240 are not diagnosed with hypertension (IDs: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All migraine patients have a diastolic blood pressure of at least 71 mmHg."""
    migraines = df[df["diagnosis"] == "migraine"]
    condition = migraines["bp_diastolic"] >= 71
    truth = condition.all()
    if truth:
        expl = f"All {len(migraines)} migraine patients have diastolic ≥ 71."
    else:
        viol = migraines[~condition]
        expl = f"{len(viol)} migraine patients violate the rule (IDs: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Every asthma patient has a systolic blood pressure of at least 120 mmHg."""
    asthma = df[df["diagnosis"] == "asthma"]
    condition = asthma["bp_systolic"] >= 120
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients have systolic ≥ 120."
    else:
        viol = asthma[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (IDs: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a patient’s systolic blood pressure is 150 mmHg or higher, the diagnosis is not hypertension."""
    high_bp = df["bp_systolic"] >= 150
    condition = df.loc[high_bp, "diagnosis"]!= "hypertension"
    truth = condition.all()
    if truth:
        expl = f"All patients with systolic ≥ 150 are not diagnosed with hypertension."
    else:
        viol = df.loc[high_bp & (df["diagnosis"] == "hypertension")]
        expl = f"{len(viol)} patients with systolic ≥ 150 are diagnosed with hypertension (IDs: {', '.join(viol['patient_id'])})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Patients with a BMI greater than 33 kg/m² are never diagnosed with migraine or diabetes."""
    high_bmi = df["bmi"] > 33
    condition = ~df.loc[high_bmi, "diagnosis"].isin(["migraine", "diabetes"])
    truth = condition.all()
    if truth:
        expl = f"All patients with BMI > 33 are not diagnosed with migraine or diabetes."
    else:
        viol = df.loc[high_bmi & df["diagnosis"].isin(["migraine", "diabetes"])]
        expl = f"{len(viol)} patients with BMI > 33 have diagnosis migraine or diabetes (IDs: {', '.join(viol['patient_id'])})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_11.csv")

    # Convert numeric columns
    numeric_cols = ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Ensure smoker column is lowercase for comparison
    df["smoker"] = df["smoker"].str.lower()

    checks = [
        (1, stmt_1),
        (2, stmt_2),
        (3, stmt_3),
        (4, stmt_4),
        (5, stmt_5),
        (6, stmt_6),
        (7, stmt_7),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()