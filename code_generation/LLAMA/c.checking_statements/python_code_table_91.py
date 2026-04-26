import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of diabetes have a cholesterol level greater than 200 mg/dl."""
    diabetes_patients = df[df["diagnosis"] == "diabetes"]
    if diabetes_patients.empty:
        truth = True
        expl = "No patients with diabetes in dataset."
    else:
        condition = diabetes_patients["cholesterol_mg_dl"] > 200
        truth = condition.all()
        if truth:
            expl = f"All {len(diabetes_patients)} diabetes patients have cholesterol > 200 mg/dl."
        else:
            viol = diabetes_patients[~condition]
            expl = f"{len(viol)} diabetes patients have cholesterol <= 200 mg/dl."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is less than 40 years."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        truth = True
        expl = "No smokers in dataset."
    else:
        condition = smokers["age"] < 40
        truth = condition.all()
        if truth:
            expl = f"All {len(smokers)} smokers are under 40 years old."
        else:
            viol = smokers[~condition]
            expl = f"{len(viol)} smokers are 40 or older."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All patients with a BMI greater than 30 have a systolic blood pressure greater than 140 mmHg."""
    obese_patients = df[df["bmi"] > 30]
    if obese_patients.empty:
        truth = True
        expl = "No patients with BMI > 30 in dataset."
    else:
        condition = obese_patients["bp_systolic"] > 140
        truth = condition.all()
        if truth:
            expl = f"All {len(obese_patients)} obese patients have systolic BP > 140 mmHg."
        else:
            viol = obese_patients[~condition]
            expl = f"{len(viol)} obese patients have systolic BP <= 140 mmHg."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one patient with a diagnosis of arthritis whose BMI is less than 25."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    if arthritis_patients.empty:
        truth = False
        expl = "No patients with arthritis in dataset."
    else:
        condition = arthritis_patients["bmi"] < 25
        truth = condition.any()
        if truth:
            found = arthritis_patients[condition]
            expl = f"At least one arthritis patient (ID: {found.iloc[0]['patient_id']}) has BMI < 25."
        else:
            expl = f"No arthritis patients have BMI < 25."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient has a diagnosis of hypertension, then their diastolic blood pressure is greater than 80 mmHg."""
    hypertensive_patients = df[df["diagnosis"] == "hypertension"]
    if hypertensive_patients.empty:
        truth = True
        expl = "No patients with hypertension in dataset."
    else:
        condition = hypertensive_patients["bp_diastolic"] > 80
        truth = condition.all()
        if truth:
            expl = f"All {len(hypertensive_patients)} hypertensive patients have diastolic BP > 80 mmHg."
        else:
            viol = hypertensive_patients[~condition]
            expl = f"{len(viol)} hypertensive patients have diastolic BP <= 80 mmHg."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All patients with a cholesterol level greater than 220 mg/dl have a BMI greater than 25."""
    high_cholesterol_patients = df[df["cholesterol_mg_dl"] > 220]
    if high_cholesterol_patients.empty:
        truth = True
        expl = "No patients with cholesterol > 220 mg/dl in dataset."
    else:
        condition = high_cholesterol_patients["bmi"] > 25
        truth = condition.all()
        if truth:
            expl = f"All {len(high_cholesterol_patients)} high cholesterol patients have BMI > 25."
        else:
            viol = high_cholesterol_patients[~condition]
            expl = f"{len(viol)} high cholesterol patients have BMI <= 25."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients in the table have a systolic blood pressure greater than 130 mmHg."""
    total = len(df)
    high_bp = df[df["bp_systolic"] > 130]
    count = len(high_bp)
    truth = count > total / 2
    expl = f"{count} out of {total} patients have systolic BP > 130 mmHg."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is a non-smoker, then their BMI is less than 30."""
    non_smokers = df[df["smoker"] == "no"]
    if non_smokers.empty:
        truth = True
        expl = "No non-smokers in dataset."
    else:
        condition = non_smokers["bmi"] < 30
        truth = condition.all()
        if truth:
            expl = f"All {len(non_smokers)} non-smokers have BMI < 30."
        else:
            viol = non_smokers[~condition]
            expl = f"{len(viol)} non-smokers have BMI >= 30."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All patients with a diagnosis of migraine have a systolic blood pressure less than 150 mmHg."""
    migraine_patients = df[df["diagnosis"] == "migraine"]
    if migraine_patients.empty:
        truth = True
        expl = "No patients with migraine in dataset."
    else:
        condition = migraine_patients["bp_systolic"] < 150
        truth = condition.all()
        if truth:
            expl = f"All {len(migraine_patients)} migraine patients have systolic BP < 150 mmHg."
        else:
            viol = migraine_patients[~condition]
            expl = f"{len(viol)} migraine patients have systolic BP >= 150 mmHg."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one patient with a diagnosis of asthma whose BMI is less than 22."""
    asthma_patients = df[df["diagnosis"] == "asthma"]
    if asthma_patients.empty:
        truth = False
        expl = "No patients with asthma in dataset."
    else:
        condition = asthma_patients["bmi"] < 22
        truth = condition.any()
        if truth:
            found = asthma_patients[condition]
            expl = f"At least one asthma patient (ID: {found.iloc[0]['patient_id']}) has BMI < 22."
        else:
            expl = f"No asthma patients have BMI < 22."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a patient has a BMI between 25 and 30, then their age is greater than 30 years."""
    bmi_25_to_30 = df[(df["bmi"] >= 25) & (df["bmi"] <= 30)]
    if bmi_25_to_30.empty:
        truth = True
        expl = "No patients with BMI between 25 and 30."
    else:
        condition = bmi_25_to_30["age"] > 30
        truth = condition.all()
        if truth:
            expl = f"All {len(bmi_25_to_30)} patients with BMI 25-30 are over 30 years old."
        else:
            viol = bmi_25_to_30[~condition]
            expl = f"{len(viol)} patients with BMI 25-30 are 30 or younger."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All patients with a diastolic blood pressure greater than 90 mmHg have a cholesterol level greater than 200 mg/dl."""
    high_dbp_patients = df[df["bp_diastolic"] > 90]
    if high_dbp_patients.empty:
        truth = True
        expl = "No patients with diastolic BP > 90 mmHg."
    else:
        condition = high_dbp_patients["cholesterol_mg_dl"] > 200
        truth = condition.all()
        if truth:
            expl = f"All {len(high_dbp_patients)} high diastolic BP patients have cholesterol > 200 mg/dl."
        else:
            viol = high_dbp_patients[~condition]
            expl = f"{len(viol)} high diastolic BP patients have cholesterol <= 200 mg/dl."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most patients in the table have a BMI greater than 25."""
    total = len(df)
    high_bmi = df[df["bmi"] > 25]
    count = len(high_bmi)
    truth = count > total / 2
    expl = f"{count} out of {total} patients have BMI > 25."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a patient is a smoker, then their cholesterol level is greater than 200 mg/dl."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        truth = True
        expl = "No smokers in dataset."
    else:
        condition = smokers["cholesterol_mg_dl"] > 200
        truth = condition.all()
        if truth:
            expl = f"All {len(smokers)} smokers have cholesterol > 200 mg/dl."
        else:
            viol = smokers[~condition]
            expl = f"{len(viol)} smokers have cholesterol <= 200 mg/dl."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All patients with a diagnosis of diabetes have a BMI greater than 20."""
    diabetes_patients = df[df["diagnosis"] == "diabetes"]
    if diabetes_patients.empty:
        truth = True
        expl = "No patients with diabetes in dataset."
    else:
        condition = diabetes_patients["bmi"] > 20
        truth = condition.all()
        if truth:
            expl = f"All {len(diabetes_patients)} diabetes patients have BMI > 20."
        else:
            viol = diabetes_patients[~condition]
            expl = f"{len(viol)} diabetes patients have BMI <= 20."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one patient with a diagnosis of arthritis whose age is greater than 60 years."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    if arthritis_patients.empty:
        truth = False
        expl = "No patients with arthritis in dataset."
    else:
        condition = arthritis_patients["age"] > 60
        truth = condition.any()
        if truth:
            found = arthritis_patients[condition]
            expl = f"At least one arthritis patient (ID: {found.iloc[0]['patient_id']}) is over 60 years old."
        else:
            expl = f"No arthritis patients are over 60 years old."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a patient has a systolic blood pressure greater than 150 mmHg, then their age is greater than 50 years."""
    high_sbp_patients = df[df["bp_systolic"] > 150]
    if high_sbp_patients.empty:
        truth = True
        expl = "No patients with systolic BP > 150 mmHg."
    else:
        condition = high_sbp_patients["age"] > 50
        truth = condition.all()
        if truth:
            expl = f"All {len(high_sbp_patients)} high systolic BP patients are over 50 years old."
        else:
            viol = high_sbp_patients[~condition]
            expl = f"{len(viol)} high systolic BP patients are 50 or younger."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All patients with a cholesterol level greater than 240 mg/dl have a BMI greater than 30."""
    high_cholesterol_patients = df[df["cholesterol_mg_dl"] > 240]
    if high_cholesterol_patients.empty:
        truth = True
        expl = "No patients with cholesterol > 240 mg/dl."
    else:
        condition = high_cholesterol_patients["bmi"] > 30
        truth = condition.all()
        if truth:
            expl = f"All {len(high_cholesterol_patients)} high cholesterol patients have BMI > 30."
        else:
            viol = high_cholesterol_patients[~condition]
            expl = f"{len(viol)} high cholesterol patients have BMI <= 30."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_91.csv")

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
        (8, stmt_8),
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
        (18, stmt_18)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()