import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of asthma have a cholesterol level less than 245 mg/dl."""
    asthma_patients = df[df["diagnosis"] == "asthma"]
    if asthma_patients.empty:
        truth = True
        expl = "No asthma patients in dataset."
    else:
        condition = asthma_patients["cholesterol_mg_dl"] < 245
        truth = condition.all()
        if truth:
            expl = f"All {len(asthma_patients)} asthma patients have cholesterol < 245 mg/dl."
        else:
            viol = asthma_patients[~condition]
            expl = f"{len(viol)} asthma patients violate the rule (cholesterol levels: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their BMI is greater than or equal to 22.6."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        truth = True
        expl = "No smokers in dataset."
    else:
        condition = smokers["bmi"] >= 22.6
        truth = condition.all()
        if truth:
            expl = f"All {len(smokers)} smokers have BMI >= 22.6."
        else:
            viol = smokers[~condition]
            expl = f"{len(viol)} smokers violate the rule (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of arthritis who is over 55 years old and has a BMI greater than 30."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    if arthritis_patients.empty:
        truth = False
        expl = "No arthritis patients in dataset."
    else:
        condition = (arthritis_patients["age"] > 55) & (arthritis_patients["bmi"] > 30)
        satisfied = arthritis_patients[condition]
        truth = not satisfied.empty
        if truth:
            expl = f"At least one arthritis patient satisfies the criteria (age: {satisfied['age'].iloc[0]}, BMI: {satisfied['bmi'].iloc[0]})."
        else:
            expl = f"No arthritis patients satisfy the criteria (age > 55 and BMI > 30)."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All patients with a systolic blood pressure greater than 145 have a diastolic blood pressure greater than or equal to 82."""
    high_bp_patients = df[df["bp_systolic"] > 145]
    if high_bp_patients.empty:
        truth = True
        expl = "No patients with systolic BP > 145."
    else:
        condition = high_bp_patients["bp_diastolic"] >= 82
        truth = condition.all()
        if truth:
            expl = f"All {len(high_bp_patients)} patients with systolic BP > 145 have diastolic BP >= 82."
        else:
            viol = high_bp_patients[~condition]
            expl = f"{len(viol)} patients with systolic BP > 145 violate the rule (diastolic BPs: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient has a BMI between 20 and 25, then their age is less than 50."""
    bmi_20_to_25 = df[(df["bmi"] >= 20) & (df["bmi"] <= 25)]
    if bmi_20_to_25.empty:
        truth = True
        expl = "No patients with BMI between 20 and 25."
    else:
        condition = bmi_20_to_25["age"] < 50
        truth = condition.all()
        if truth:
            expl = f"All {len(bmi_20_to_25)} patients with BMI 20-25 are under 50."
        else:
            viol = bmi_20_to_25[~condition]
            expl = f"{len(viol)} patients with BMI 20-25 are 50 or older (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most patients in the table have a cholesterol level greater than 200 mg/dl."""
    total = len(df)
    high_cholesterol = df[df["cholesterol_mg_dl"] > 200]
    count = len(high_cholesterol)
    truth = count > total / 2
    expl = f"{count} out of {total} patients have cholesterol > 200 mg/dl."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All patients with a diagnosis of hypertension have a systolic blood pressure greater than or equal to 115."""
    hypertensive = df[df["diagnosis"] == "hypertension"]
    if hypertensive.empty:
        truth = True
        expl = "No hypertension patients in dataset."
    else:
        condition = hypertensive["bp_systolic"] >= 115
        truth = condition.all()
        if truth:
            expl = f"All {len(hypertensive)} hypertension patients have systolic BP >= 115."
        else:
            viol = hypertensive[~condition]
            expl = f"{len(viol)} hypertension patients violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is over 60 years old, then their diastolic blood pressure is less than or equal to 94."""
    elderly = df[df["age"] > 60]
    if elderly.empty:
        truth = True
        expl = "No patients over 60."
    else:
        condition = elderly["bp_diastolic"] <= 94
        truth = condition.all()
        if truth:
            expl = f"All {len(elderly)} patients over 60 have diastolic BP <= 94."
        else:
            viol = elderly[~condition]
            expl = f"{len(viol)} patients over 60 violate the rule (diastolic BPs: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one patient with a diagnosis of migraine who is under 30 years old and has a BMI greater than 27."""
    migraine_patients = df[df["diagnosis"] == "migraine"]
    if migraine_patients.empty:
        truth = False
        expl = "No migraine patients in dataset."
    else:
        condition = (migraine_patients["age"] < 30) & (migraine_patients["bmi"] > 27)
        satisfied = migraine_patients[condition]
        truth = not satisfied.empty
        if truth:
            expl = f"At least one migraine patient satisfies the criteria (age: {satisfied['age'].iloc[0]}, BMI: {satisfied['bmi'].iloc[0]})."
        else:
            expl = f"No migraine patients satisfy the criteria (age < 30 and BMI > 27)."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All patients who are non-smokers have a BMI greater than or equal to 24.2."""
    non_smokers = df[df["smoker"] == "no"]
    if non_smokers.empty:
        truth = True
        expl = "No non-smokers in dataset."
    else:
        condition = non_smokers["bmi"] >= 24.2
        truth = condition.all()
        if truth:
            expl = f"All {len(non_smokers)} non-smokers have BMI >= 24.2."
        else:
            viol = non_smokers[~condition]
            expl = f"{len(viol)} non-smokers violate the rule (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a patient has a cholesterol level greater than 230 mg/dl, then their BMI is greater than or equal to 27.5."""
    high_cholesterol = df[df["cholesterol_mg_dl"] > 230]
    if high_cholesterol.empty:
        truth = True
        expl = "No patients with cholesterol > 230 mg/dl."
    else:
        condition = high_cholesterol["bmi"] >= 27.5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_cholesterol)} patients with cholesterol > 230 have BMI >= 27.5."
        else:
            viol = high_cholesterol[~condition]
            expl = f"{len(viol)} patients with cholesterol > 230 violate the rule (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most patients in the table are smokers."""
    total = len(df)
    smokers = df[df["smoker"] == "yes"]
    count = len(smokers)
    truth = count > total / 2
    expl = f"{count} out of {total} patients are smokers."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All patients with a diagnosis of asthma have a systolic blood pressure less than 151."""
    asthma_patients = df[df["diagnosis"] == "asthma"]
    if asthma_patients.empty:
        truth = True
        expl = "No asthma patients in dataset."
    else:
        condition = asthma_patients["bp_systolic"] < 151
        truth = condition.all()
        if truth:
            expl = f"All {len(asthma_patients)} asthma patients have systolic BP < 151."
        else:
            viol = asthma_patients[~condition]
            expl = f"{len(viol)} asthma patients violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a patient is under 40 years old, then their systolic blood pressure is less than or equal to 150."""
    young = df[df["age"] < 40]
    if young.empty:
        truth = True
        expl = "No patients under 40."
    else:
        condition = young["bp_systolic"] <= 150
        truth = condition.all()
        if truth:
            expl = f"All {len(young)} patients under 40 have systolic BP <= 150."
        else:
            viol = young[~condition]
            expl = f"{len(viol)} patients under 40 violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one patient with a diagnosis of arthritis who has a cholesterol level greater than 235 mg/dl."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    if arthritis_patients.empty:
        truth = False
        expl = "No arthritis patients in dataset."
    else:
        condition = arthritis_patients["cholesterol_mg_dl"] > 235
        satisfied = arthritis_patients[condition]
        truth = not satisfied.empty
        if truth:
            expl = f"At least one arthritis patient has cholesterol > 235 mg/dl (cholesterol: {satisfied['cholesterol_mg_dl'].iloc[0]})."
        else:
            expl = f"No arthritis patients have cholesterol > 235 mg/dl."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All patients with a BMI greater than 30 have a diastolic blood pressure greater than or equal to 91."""
    obese = df[df["bmi"] > 30]
    if obese.empty:
        truth = True
        expl = "No patients with BMI > 30."
    else:
        condition = obese["bp_diastolic"] >= 91
        truth = condition.all()
        if truth:
            expl = f"All {len(obese)} patients with BMI > 30 have diastolic BP >= 91."
        else:
            viol = obese[~condition]
            expl = f"{len(viol)} patients with BMI > 30 violate the rule (diastolic BPs: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a patient has a systolic blood pressure greater than 140, then their diastolic blood pressure is greater than or equal to 78."""
    high_systolic = df[df["bp_systolic"] > 140]
    if high_systolic.empty:
        truth = True
        expl = "No patients with systolic BP > 140."
    else:
        condition = high_systolic["bp_diastolic"] >= 78
        truth = condition.all()
        if truth:
            expl = f"All {len(high_systolic)} patients with systolic BP > 140 have diastolic BP >= 78."
        else:
            viol = high_systolic[~condition]
            expl = f"{len(viol)} patients with systolic BP > 140 violate the rule (diastolic BPs: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
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
        (8, stmt_8),
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()