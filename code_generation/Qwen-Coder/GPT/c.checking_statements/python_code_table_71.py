import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all individuals with migraine, cholesterol is at least 172 mg/dL."""
    migraine = df[df["diagnosis"] == "migraine"]
    condition = migraine["cholesterol_mg_dl"] >= 172
    truth = condition.all()
    if truth:
        expl = f"All {len(migraine)} migraine patients have cholesterol >= 172 mg/dL."
    else:
        viol = migraine[~condition]
        expl = f"{len(viol)} migraine patients violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all individuals with BMI greater than 30, the diagnosis is either hypertension or arthritis."""
    high_bmi = df[df["bmi"] > 30]
    valid_diag = df["diagnosis"].isin(["hypertension", "arthritis"])
    condition = df.loc[high_bmi.index, "diagnosis"].isin(["hypertension", "arthritis"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 have diagnosis of hypertension or arthritis."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 30 do not have diagnosis of hypertension or arthritis (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all smokers, systolic blood pressure is at least 113 mmHg."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["bp_systolic"] >= 113
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have systolic BP >= 113 mmHg."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all non-smokers, diastolic blood pressure is at most 91 mmHg."""
    non_smokers = df[df["smoker"] == "no"]
    condition = non_smokers["bp_diastolic"] <= 91
    truth = condition.all()
    if truth:
        expl = f"All {len(non_smokers)} non-smokers have diastolic BP <= 91 mmHg."
    else:
        viol = non_smokers[~condition]
        expl = f"{len(viol)} non-smokers violate the rule (diastolic BPs: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all patients older than 60 years, systolic blood pressure is at least 143 mmHg."""
    old_patients = df[df["age"] > 60]
    condition = old_patients["bp_systolic"] >= 143
    truth = condition.all()
    if truth:
        expl = f"All {len(old_patients)} patients over 60 have systolic BP >= 143 mmHg."
    else:
        viol = old_patients[~condition]
        expl = f"{len(viol)} patients over 60 violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all patients with hypertension, diastolic blood pressure is at least 91 mmHg."""
    hypertensive = df[df["diagnosis"] == "hypertension"]
    condition = hypertensive["bp_diastolic"] >= 91
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertensive)} hypertensive patients have diastolic BP >= 91 mmHg."
    else:
        viol = hypertensive[~condition]
        expl = f"{len(viol)} hypertensive patients violate the rule (diastolic BPs: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All patients have a body-mass index between 22 and 35."""
    condition = df["bmi"].between(22, 35, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(df)} patients have BMI between 22 and 35."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} patients have BMI outside range [22, 35] (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For the sole patient with diabetes, the BMI is less than 23."""
    diabetic = df[df["diagnosis"] == "diabetes"]
    if len(diabetic) == 0:
        truth = True
        expl = "No patient diagnosed with diabetes found."
    elif len(diabetic) == 1:
        bmi = diabetic.iloc[0]["bmi"]
        truth = bmi < 23
        if truth:
            expl = f"Patient with diabetes has BMI {bmi} which is less than 23."
        else:
            expl = f"Patient with diabetes has BMI {bmi} which is not less than 23."
    else:
        truth = False
        expl = f"Multiple patients diagnosed with diabetes found ({len(diabetic)})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_71.csv")

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