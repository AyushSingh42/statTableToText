import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of arthritis have a BMI less than 33."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    condition = arthritis_patients["bmi"] < 33
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritis_patients)} arthritis patients have BMI < 33."
    else:
        viol = arthritis_patients[~condition]
        expl = f"{len(viol)} arthritis patients violate the rule (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is less than 65."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["age"] < 65
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers are under 65 years old."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of diabetes whose cholesterol level is less than 200 mg/dl."""
    diabetes_patients = df[df["diagnosis"] == "diabetes"]
    condition = diabetes_patients["cholesterol_mg_dl"] < 200
    truth = condition.any()
    if truth:
        found = diabetes_patients[condition].iloc[0]
        expl = f"One diabetes patient (ID: {found['patient_id']}) has cholesterol < 200 mg/dl."
    else:
        expl = "No diabetes patients have cholesterol < 200 mg/dl."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All patients with a systolic blood pressure greater than 140 have a diastolic blood pressure greater than 70."""
    high_bp_patients = df[df["bp_systolic"] > 140]
    condition = high_bp_patients["bp_diastolic"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bp_patients)} high systolic BP patients have diastolic > 70."
    else:
        viol = high_bp_patients[~condition]
        expl = f"{len(viol)} high systolic BP patients violate the rule (diastolic: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient has a BMI greater than 30, then they are a smoker."""
    high_bmi_patients = df[df["bmi"] > 30]
    condition = high_bmi_patients["smoker"] == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi_patients)} high BMI patients are smokers."
    else:
        viol = high_bmi_patients[~condition]
        expl = f"{len(viol)} high BMI patients are not smokers (IDs: {', '.join(map(str, viol['patient_id'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most patients have a cholesterol level greater than 180 mg/dl."""
    total = len(df)
    high_chol = df[df["cholesterol_mg_dl"] > 180]
    truth = len(high_chol) > total / 2
    if truth:
        expl = f"{len(high_chol)} out of {total} patients have cholesterol > 180 mg/dl."
    else:
        expl = f"{len(high_chol)} out of {total} patients have cholesterol > 180 mg/dl (less than half)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All patients with a diagnosis of asthma have a BMI greater than 28."""
    asthma_patients = df[df["diagnosis"] == "asthma"]
    condition = asthma_patients["bmi"] > 28
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma_patients)} asthma patients have BMI > 28."
    else:
        viol = asthma_patients[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is older than 50, then their systolic blood pressure is greater than 120."""
    older_patients = df[df["age"] > 50]
    condition = older_patients["bp_systolic"] > 120
    truth = condition.all()
    if truth:
        expl = f"All {len(older_patients)} patients over 50 have systolic BP > 120."
    else:
        viol = older_patients[~condition]
        expl = f"{len(viol)} patients over 50 violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one patient with a diagnosis of migraine whose BMI is less than 22."""
    migraine_patients = df[df["diagnosis"] == "migraine"]
    condition = migraine_patients["bmi"] < 22
    truth = condition.any()
    if truth:
        found = migraine_patients[condition].iloc[0]
        expl = f"One migraine patient (ID: {found['patient_id']}) has BMI < 22."
    else:
        expl = "No migraine patients have BMI < 22."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All patients with a diastolic blood pressure less than 90 have a systolic blood pressure less than 130."""
    low_diastolic_patients = df[df["bp_diastolic"] < 90]
    condition = low_diastolic_patients["bp_systolic"] < 130
    truth = condition.all()
    if truth:
        expl = f"All {len(low_diastolic_patients)} low diastolic BP patients have systolic < 130."
    else:
        viol = low_diastolic_patients[~condition]
        expl = f"{len(viol)} low diastolic BP patients violate the rule (systolic: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a patient has a cholesterol level greater than 220 mg/dl, then they are a smoker."""
    high_chol_patients = df[df["cholesterol_mg_dl"] > 220]
    condition = high_chol_patients["smoker"] == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_chol_patients)} high cholesterol patients are smokers."
    else:
        viol = high_chol_patients[~condition]
        expl = f"{len(viol)} high cholesterol patients are not smokers (IDs: {', '.join(map(str, viol['patient_id'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most patients have a BMI less than 30."""
    total = len(df)
    low_bmi = df[df["bmi"] < 30]
    truth = len(low_bmi) > total / 2
    if truth:
        expl = f"{len(low_bmi)} out of {total} patients have BMI < 30."
    else:
        expl = f"{len(low_bmi)} out of {total} patients have BMI < 30 (less than half)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All patients with a diagnosis of hypertension have a systolic blood pressure greater than 140."""
    hypertension_patients = df[df["diagnosis"] == "hypertension"]
    condition = hypertension_patients["bp_systolic"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension_patients)} hypertension patients have systolic BP > 140."
    else:
        viol = hypertension_patients[~condition]
        expl = f"{len(viol)} hypertension patients violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a patient is younger than 40, then their diastolic blood pressure is greater than 80."""
    young_patients = df[df["age"] < 40]
    condition = young_patients["bp_diastolic"] > 80
    truth = condition.all()
    if truth:
        expl = f"All {len(young_patients)} patients under 40 have diastolic BP > 80."
    else:
        viol = young_patients[~condition]
        expl = f"{len(viol)} patients under 40 violate the rule (diastolic BPs: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one patient with a diagnosis of arthritis whose cholesterol level is greater than 230 mg/dl."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    condition = arthritis_patients["cholesterol_mg_dl"] > 230
    truth = condition.any()
    if truth:
        found = arthritis_patients[condition].iloc[0]
        expl = f"One arthritis patient (ID: {found['patient_id']}) has cholesterol > 230 mg/dl."
    else:
        expl = "No arthritis patients have cholesterol > 230 mg/dl."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All patients with a BMI greater than 25 have a systolic blood pressure greater than 110."""
    high_bmi_patients = df[df["bmi"] > 25]
    condition = high_bmi_patients["bp_systolic"] > 110
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi_patients)} high BMI patients have systolic BP > 110."
    else:
        viol = high_bmi_patients[~condition]
        expl = f"{len(viol)} high BMI patients violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a patient has a cholesterol level less than 190 mg/dl, then they are not a smoker."""
    low_chol_patients = df[df["cholesterol_mg_dl"] < 190]
    condition = low_chol_patients["smoker"]!= "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_chol_patients)} low cholesterol patients are not smokers."
    else:
        viol = low_chol_patients[~condition]
        expl = f"{len(viol)} low cholesterol patients are smokers (IDs: {', '.join(map(str, viol['patient_id'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most patients have a systolic blood pressure greater than 120."""
    total = len(df)
    high_sbp = df[df["bp_systolic"] > 120]
    truth = len(high_sbp) > total / 2
    if truth:
        expl = f"{len(high_sbp)} out of {total} patients have systolic BP > 120."
    else:
        expl = f"{len(high_sbp)} out of {total} patients have systolic BP > 120 (less than half)."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All patients with a diagnosis of diabetes have a BMI greater than 25."""
    diabetes_patients = df[df["diagnosis"] == "diabetes"]
    condition = diabetes_patients["bmi"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetes_patients)} diabetes patients have BMI > 25."
    else:
        viol = diabetes_patients[~condition]
        expl = f"{len(viol)} diabetes patients violate the rule (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a patient is older than 60, then their BMI is less than 29."""
    older_patients = df[df["age"] > 60]
    condition = older_patients["bmi"] < 29
    truth = condition.all()
    if truth:
        expl = f"All {len(older_patients)} patients over 60 have BMI < 29."
    else:
        viol = older_patients[~condition]
        expl = f"{len(viol)} patients over 60 violate the rule (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one patient with a diagnosis of migraine whose systolic blood pressure is greater than 145."""
    migraine_patients = df[df["diagnosis"] == "migraine"]
    condition = migraine_patients["bp_systolic"] > 145
    truth = condition.any()
    if truth:
        found = migraine_patients[condition].iloc[0]
        expl = f"One migraine patient (ID: {found['patient_id']}) has systolic BP > 145."
    else:
        expl = "No migraine patients have systolic BP > 145."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. All patients with a diastolic blood pressure greater than 95 have a systolic blood pressure greater than 125."""
    high_diastolic_patients = df[df["bp_diastolic"] > 95]
    condition = high_diastolic_patients["bp_systolic"] > 125
    truth = condition.all()
    if truth:
        expl = f"All {len(high_diastolic_patients)} high diastolic BP patients have systolic > 125."
    else:
        viol = high_diastolic_patients[~condition]
        expl = f"{len(viol)} high diastolic BP patients violate the rule (systolic: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_81.csv")

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
        (18, stmt_18),
        (19, stmt_19),
        (20, stmt_20),
        (21, stmt_21),
        (22, stmt_22)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()