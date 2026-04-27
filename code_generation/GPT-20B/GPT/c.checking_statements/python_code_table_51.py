import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All individuals diagnosed with asthma are smokers."""
    asthma = df[df["diagnosis"] == "asthma"]
    condition = asthma["smoker"] == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients are smokers."
    else:
        viol = asthma[~condition]
        ids = ", ".join(viol["patient_id"].astype(str).tolist())
        expl = f"{len(viol)} asthma patients are not smokers (ids: {ids})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All diabetes patients have cholesterol between 191 and 244 mg/dL."""
    diabetes = df[df["diagnosis"] == "diabetes"]
    condition = diabetes["cholesterol_mg_dl"].between(191, 244, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetes)} diabetes patients have cholesterol between 191 and 244 mg/dL."
    else:
        viol = diabetes[~condition]
        ids = ", ".join(viol["patient_id"].astype(str).tolist())
        expl = f"{len(viol)} diabetes patients violate the cholesterol range (ids: {ids})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All migraine patients have BMI ≥ 26.9."""
    migraine = df[df["diagnosis"] == "migraine"]
    condition = migraine["bmi"] >= 26.9
    truth = condition.all()
    if truth:
        expl = f"All {len(migraine)} migraine patients have BMI ≥ 26.9."
    else:
        viol = migraine[~condition]
        ids = ", ".join(viol["patient_id"].astype(str).tolist())
        expl = f"{len(viol)} migraine patients have BMI < 26.9 (ids: {ids})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hypertension patients have systolic ≥ 127 mmHg."""
    hypertension = df[df["diagnosis"] == "hypertension"]
    condition = hypertension["bp_systolic"] >= 127
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension)} hypertension patients have systolic ≥ 127 mmHg."
    else:
        viol = hypertension[~condition]
        ids = ", ".join(viol["patient_id"].astype(str).tolist())
        expl = f"{len(viol)} hypertension patients have systolic < 127 mmHg (ids: {ids})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient is younger than 30, then they have diabetes."""
    young = df[df["age"] < 30]
    condition = young["diagnosis"] == "diabetes"
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} patients younger than 30 have diabetes."
    else:
        viol = young[~condition]
        ids = ", ".join(viol["patient_id"].astype(str).tolist())
        expl = f"{len(viol)} patients younger than 30 do not have diabetes (ids: {ids})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All smokers have systolic blood pressure ≤ 156 mmHg."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["bp_systolic"] <= 156
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have systolic BP ≤ 156 mmHg."
    else:
        viol = smokers[~condition]
        ids = ", ".join(viol["patient_id"].astype(str).tolist())
        expl = f"{len(viol)} smokers have systolic BP > 156 mmHg (ids: {ids})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hypertension patients have diastolic ≤ 87 mmHg."""
    hypertension = df[df["diagnosis"] == "hypertension"]
    condition = hypertension["bp_diastolic"] <= 87
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension)} hypertension patients have diastolic ≤ 87 mmHg."
    else:
        viol = hypertension[~condition]
        ids = ", ".join(viol["patient_id"].astype(str).tolist())
        expl = f"{len(viol)} hypertension patients have diastolic > 87 mmHg (ids: {ids})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most patients have cholesterol above 200 mg/dL."""
    proportion = (df["cholesterol_mg_dl"] > 200).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of patients have cholesterol > 200 mg/dL, which is >50%."
    else:
        expl = f"{proportion*100:.1f}% of patients have cholesterol > 200 mg/dL, which is ≤50%."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_51.csv")

    # Convert numeric columns where possible
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

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