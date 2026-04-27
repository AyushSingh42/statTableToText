import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of diabetes have a cholesterol level greater than 190 mg/dl."""
    diabetes_patients = df[df["diagnosis"] == "diabetes"]
    condition = diabetes_patients["cholesterol_mg_dl"] > 190
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetes_patients)} diabetes patients have cholesterol > 190."
    else:
        viol = diabetes_patients[~condition]
        expl = f"{len(viol)} diabetes patients have cholesterol <= 190 (cholesterol levels: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is less than 70 years."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["age"] < 70
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers are under 70 years old."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers are 70 or older (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of arthritis whose BMI is less than 28."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    condition = arthritis_patients["bmi"] < 28
    truth = condition.any()
    if truth:
        expl = f"At least one arthritis patient has BMI < 28."
    else:
        expl = f"No arthritis patients have BMI < 28."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All patients with a BMI greater than 33 have a diagnosis of either asthma or arthritis."""
    high_bmi_patients = df[df["bmi"] > 33]
    condition = (high_bmi_patients["diagnosis"] == "asthma") | (high_bmi_patients["diagnosis"] == "arthritis")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi_patients)} patients with BMI > 33 have diagnosis of asthma or arthritis."
    else:
        viol = high_bmi_patients[~condition]
        expl = f"{len(viol)} patients with BMI > 33 do not have diagnosis of asthma or arthritis (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient has a systolic blood pressure greater than 140, then their diagnosis is either diabetes or hypertension."""
    high_bp_patients = df[df["bp_systolic"] > 140]
    condition = (high_bp_patients["diagnosis"] == "diabetes") | (high_bp_patients["diagnosis"] == "hypertension")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bp_patients)} patients with BP > 140 have diagnosis of diabetes or hypertension."
    else:
        viol = high_bp_patients[~condition]
        expl = f"{len(viol)} patients with BP > 140 do not have diagnosis of diabetes or hypertension (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most patients with a diagnosis of arthritis have a diastolic blood pressure less than 85."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    condition = arthritis_patients["bp_diastolic"] < 85
    truth = condition.sum() > len(arthritis_patients) / 2
    if truth:
        expl = f"More than half ({condition.sum()}/{len(arthritis_patients)}) arthritis patients have diastolic BP < 85."
    else:
        expl = f"Less than half ({condition.sum()}/{len(arthritis_patients)}) arthritis patients have diastolic BP < 85."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All patients with a cholesterol level greater than 230 mg/dl have a diagnosis of either diabetes or migraine."""
    high_chol_patients = df[df["cholesterol_mg_dl"] > 230]
    condition = (high_chol_patients["diagnosis"] == "diabetes") | (high_chol_patients["diagnosis"] == "migraine")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_chol_patients)} patients with cholesterol > 230 have diagnosis of diabetes or migraine."
    else:
        viol = high_chol_patients[~condition]
        expl = f"{len(viol)} patients with cholesterol > 230 do not have diagnosis of diabetes or migraine (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is a non-smoker, then their BMI is less than 34."""
    non_smokers = df[df["smoker"] == "no"]
    condition = non_smokers["bmi"] < 34
    truth = condition.all()
    if truth:
        expl = f"All {len(non_smokers)} non-smokers have BMI < 34."
    else:
        viol = non_smokers[~condition]
        expl = f"{len(viol)} non-smokers have BMI >= 34 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one patient with a diagnosis of migraine whose systolic blood pressure is less than 125."""
    migraine_patients = df[df["diagnosis"] == "migraine"]
    condition = migraine_patients["bp_systolic"] < 125
    truth = condition.any()
    if truth:
        expl = f"At least one migraine patient has systolic BP < 125."
    else:
        expl = f"No migraine patients have systolic BP < 125."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All patients with a BMI less than 27 have a diagnosis of either arthritis or diabetes."""
    low_bmi_patients = df[df["bmi"] < 27]
    condition = (low_bmi_patients["diagnosis"] == "arthritis") | (low_bmi_patients["diagnosis"] == "diabetes")
    truth = condition.all()
    if truth:
        expl = f"All {len(low_bmi_patients)} patients with BMI < 27 have diagnosis of arthritis or diabetes."
    else:
        viol = low_bmi_patients[~condition]
        expl = f"{len(viol)} patients with BMI < 27 do not have diagnosis of arthritis or diabetes (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a patient has a diastolic blood pressure greater than 90, then their age is less than 75 years."""
    high_dbp_patients = df[df["bp_diastolic"] > 90]
    condition = high_dbp_patients["age"] < 75
    truth = condition.all()
    if truth:
        expl = f"All {len(high_dbp_patients)} patients with diastolic BP > 90 are under 75 years old."
    else:
        viol = high_dbp_patients[~condition]
        expl = f"{len(viol)} patients with diastolic BP > 90 are 75 or older (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most patients with a diagnosis of diabetes have a BMI greater than 25."""
    diabetes_patients = df[df["diagnosis"] == "diabetes"]
    condition = diabetes_patients["bmi"] > 25
    truth = condition.sum() > len(diabetes_patients) / 2
    if truth:
        expl = f"More than half ({condition.sum()}/{len(diabetes_patients)}) diabetes patients have BMI > 25."
    else:
        expl = f"Less than half ({condition.sum()}/{len(diabetes_patients)}) diabetes patients have BMI > 25."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All patients with a systolic blood pressure less than 130 have a diagnosis of either arthritis or migraine."""
    low_bp_patients = df[df["bp_systolic"] < 130]
    condition = (low_bp_patients["diagnosis"] == "arthritis") | (low_bp_patients["diagnosis"] == "migraine")
    truth = condition.all()
    if truth:
        expl = f"All {len(low_bp_patients)} patients with systolic BP < 130 have diagnosis of arthritis or migraine."
    else:
        viol = low_bp_patients[~condition]
        expl = f"{len(viol)} patients with systolic BP < 130 do not have diagnosis of arthritis or migraine (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a patient has a cholesterol level less than 200 mg/dl, then their BMI is less than 32."""
    low_chol_patients = df[df["cholesterol_mg_dl"] < 200]
    condition = low_chol_patients["bmi"] < 32
    truth = condition.all()
    if truth:
        expl = f"All {len(low_chol_patients)} patients with cholesterol < 200 have BMI < 32."
    else:
        viol = low_chol_patients[~condition]
        expl = f"{len(viol)} patients with cholesterol < 200 have BMI >= 32 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one patient with a diagnosis of asthma whose BMI is greater than 33."""
    asthma_patients = df[df["diagnosis"] == "asthma"]
    condition = asthma_patients["bmi"] > 33
    truth = condition.any()
    if truth:
        expl = f"At least one asthma patient has BMI > 33."
    else:
        expl = f"No asthma patients have BMI > 33."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All patients with a BMI greater than 32 have a diagnosis of either arthritis or diabetes."""
    high_bmi_patients = df[df["bmi"] > 32]
    condition = (high_bmi_patients["diagnosis"] == "arthritis") | (high_bmi_patients["diagnosis"] == "diabetes")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi_patients)} patients with BMI > 32 have diagnosis of arthritis or diabetes."
    else:
        viol = high_bmi_patients[~condition]
        expl = f"{len(viol)} patients with BMI > 32 do not have diagnosis of arthritis or diabetes (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a patient is a smoker, then their cholesterol level is greater than 220 mg/dl."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["cholesterol_mg_dl"] > 220
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have cholesterol > 220."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers have cholesterol <= 220 (cholesterol levels: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most patients with a diagnosis of arthritis have a systolic blood pressure less than 140."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    condition = arthritis_patients["bp_systolic"] < 140
    truth = condition.sum() > len(arthritis_patients) / 2
    if truth:
        expl = f"More than half ({condition.sum()}/{len(arthritis_patients)}) arthritis patients have systolic BP < 140."
    else:
        expl = f"Less than half ({condition.sum()}/{len(arthritis_patients)}) arthritis patients have systolic BP < 140."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All patients with a diastolic blood pressure less than 80 have a diagnosis of either hypertension or migraine."""
    low_dbp_patients = df[df["bp_diastolic"] < 80]
    condition = (low_dbp_patients["diagnosis"] == "hypertension") | (low_dbp_patients["diagnosis"] == "migraine")
    truth = condition.all()
    if truth:
        expl = f"All {len(low_dbp_patients)} patients with diastolic BP < 80 have diagnosis of hypertension or migraine."
    else:
        viol = low_dbp_patients[~condition]
        expl = f"{len(viol)} patients with diastolic BP < 80 do not have diagnosis of hypertension or migraine (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_1.csv")

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
        (19, stmt_19)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()