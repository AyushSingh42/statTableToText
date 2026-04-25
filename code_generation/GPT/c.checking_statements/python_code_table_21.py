import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients younger than 30 years have a diagnosis of diabetes."""
    young_patients = df[df["age"] < 30]
    condition = young_patients["diagnosis"] == "diabetes"
    truth = condition.all()
    if truth:
        expl = f"All {len(young_patients)} patients under 30 have diabetes."
    else:
        viol = young_patients[~condition]
        expl = f"{len(viol)} patients under 30 do not have diabetes (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All patients diagnosed with diabetes have cholesterol levels of at least 207 mg/dL."""
    diabetic_patients = df[df["diagnosis"] == "diabetes"]
    condition = diabetic_patients["cholesterol_mg_dl"] >= 207
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetic_patients)} diabetic patients have cholesterol >= 207 mg/dL."
    else:
        viol = diabetic_patients[~condition]
        expl = f"{len(viol)} diabetic patients have cholesterol < 207 mg/dL (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All smokers have a body-mass index of at least 25."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["bmi"] >= 25
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have BMI >= 25."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers have BMI < 25 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All patients with hypertension have a systolic blood pressure of at least 148 mmHg."""
    hypertensive_patients = df[df["diagnosis"] == "hypertension"]
    condition = hypertensive_patients["bp_systolic"] >= 148
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertensive_patients)} hypertensive patients have systolic BP >= 148 mmHg."
    else:
        viol = hypertensive_patients[~condition]
        expl = f"{len(viol)} hypertensive patients have systolic BP < 148 mmHg (BP readings: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All asthma patients have a diastolic blood pressure no greater than 93 mmHg."""
    asthmatic_patients = df[df["diagnosis"] == "asthma"]
    condition = asthmatic_patients["bp_diastolic"] <= 93
    truth = condition.all()
    if truth:
        expl = f"All {len(asthmatic_patients)} asthmatic patients have diastolic BP <= 93 mmHg."
    else:
        viol = asthmatic_patients[~condition]
        expl = f"{len(viol)} asthmatic patients have diastolic BP > 93 mmHg (BP readings: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All arthritis patients have cholesterol of at most 180 mg/dL."""
    arthritic_patients = df[df["diagnosis"] == "arthritis"]
    condition = arthritic_patients["cholesterol_mg_dl"] <= 180
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritic_patients)} arthritic patients have cholesterol <= 180 mg/dL."
    else:
        viol = arthritic_patients[~condition]
        expl = f"{len(viol)} arthritic patients have cholesterol > 180 mg/dL (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a patient’s systolic blood pressure is at least 150 mmHg, then their diastolic pressure is at least 73 mmHg."""
    high_systolic = df[df["bp_systolic"] >= 150]
    condition = high_systolic["bp_diastolic"] >= 73
    truth = condition.all()
    if truth:
        expl = f"All {len(high_systolic)} patients with systolic BP >= 150 have diastolic BP >= 73 mmHg."
    else:
        viol = high_systolic[~condition]
        expl = f"{len(viol)} patients with systolic BP >= 150 have diastolic BP < 73 mmHg (diastolic readings: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most patients have cholesterol levels above 200 mg/dL."""
    total_count = len(df)
    above_200 = df[df["cholesterol_mg_dl"] > 200]
    proportion = len(above_200) / total_count
    truth = proportion > 0.5
    if truth:
        expl = f"{len(above_200)} out of {total_count} patients have cholesterol > 200 mg/dL ({proportion:.2%} of patients)."
    else:
        expl = f"{len(above_200)} out of {total_count} patients have cholesterol > 200 mg/dL ({proportion:.2%} of patients)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_21.csv")

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
        (7, stmt_7),
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()