import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all individuals diagnosed with hypertension, systolic blood pressure does not exceed 135 mmHg."""
    hypertensives = df[df["diagnosis"] == "hypertension"]
    condition = hypertensives["bp_systolic"] <= 135
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertensives)} hypertensive patients have systolic BP <= 135."
    else:
        viol = hypertensives[~condition]
        expl = f"{len(viol)} hypertensive patients violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Every patient who is a smoker has a cholesterol level of at least 215 mg/dL."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["cholesterol_mg_dl"] >= 215
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have cholesterol >= 215."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (cholesterols: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a patient’s cholesterol is 240 mg/dL or higher, the diagnosis is hypertension."""
    high_cholesterol = df[df["cholesterol_mg_dl"] >= 240]
    condition = high_cholesterol["diagnosis"] == "hypertension"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_cholesterol)} patients with cholesterol >= 240 are diagnosed as hypertensive."
    else:
        viol = high_cholesterol[~condition]
        expl = f"{len(viol)} patients with cholesterol >= 240 are not diagnosed as hypertensive (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All migraine patients have a diastolic blood pressure of at least 71 mmHg."""
    migraine_patients = df[df["diagnosis"] == "migraine"]
    condition = migraine_patients["bp_diastolic"] >= 71
    truth = condition.all()
    if truth:
        expl = f"All {len(migraine_patients)} migraine patients have diastolic BP >= 71."
    else:
        viol = migraine_patients[~condition]
        expl = f"{len(viol)} migraine patients violate the rule (diastolic BPs: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Every asthma patient has a systolic blood pressure of at least 120 mmHg."""
    asthma_patients = df[df["diagnosis"] == "asthma"]
    condition = asthma_patients["bp_systolic"] >= 120
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma_patients)} asthma patients have systolic BP >= 120."
    else:
        viol = asthma_patients[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a patient’s systolic blood pressure is 150 mmHg or higher, the diagnosis is not hypertension."""
    high_systolic = df[df["bp_systolic"] >= 150]
    condition = high_systolic["diagnosis"]!= "hypertension"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_systolic)} patients with systolic BP >= 150 are not diagnosed as hypertensive."
    else:
        viol = high_systolic[high_systolic["diagnosis"] == "hypertension"]
        expl = f"{len(viol)} patients with systolic BP >= 150 are incorrectly diagnosed as hypertensive (IDs: {', '.join(viol['patient_id'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Patients with a BMI greater than 33 kg/m² are never diagnosed with migraine or diabetes."""
    obese = df[df["bmi"] > 33]
    condition = ~obese["diagnosis"].isin(["migraine", "diabetes"])
    truth = condition.all()
    if truth:
        expl = f"All {len(obese)} obese patients are not diagnosed with migraine or diabetes."
    else:
        viol = obese[obese["diagnosis"].isin(["migraine", "diabetes"])]
        expl = f"{len(viol)} obese patients are diagnosed with migraine or diabetes (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_11.csv")

    # Convert likely numeric columns safely.
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            pass

    checks = [
        (1, stmt_1),
        (2, stmt_2),
        (3, stmt_3),
        (4, stmt_4),
        (5, stmt_5),
        (6, stmt_6),
        (7, stmt_7)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()