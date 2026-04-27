import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of diabetes have a BMI greater than or equal to 24.8."""
    diabetes_patients = df[df["diagnosis"] == "diabetes"]
    condition = diabetes_patients["bmi"] >= 24.8
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetes_patients)} diabetes patients have BMI >= 24.8."
    else:
        viol = diabetes_patients[~condition]
        expl = f"{len(viol)} diabetes patients violate the rule (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is less than 78 years."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["age"] < 78
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers are under 78 years old."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of asthma whose cholesterol level is greater than 230 mg/dl."""
    asthmatics = df[df["diagnosis"] == "asthma"]
    condition = asthmatics["cholesterol_mg_dl"] > 230
    truth = condition.any()
    if truth:
        found = asthmatics[condition]
        expl = f"At least one asthma patient (ID: {found.iloc[0]['patient_id']}) has cholesterol > 230 mg/dl."
    else:
        expl = "No asthma patients have cholesterol > 230 mg/dl."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all patients with a BMI greater than 30, their systolic blood pressure is greater than 118 mmHg."""
    high_bmi = df[df["bmi"] > 30]
    condition = high_bmi["bp_systolic"] > 118
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} high-BMI patients have systolic BP > 118 mmHg."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} high-BMI patients violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient is a non-smoker, then their diastolic blood pressure is less than 98 mmHg."""
    non_smokers = df[df["smoker"] == "no"]
    condition = non_smokers["bp_diastolic"] < 98
    truth = condition.all()
    if truth:
        expl = f"All {len(non_smokers)} non-smokers have diastolic BP < 98 mmHg."
    else:
        viol = non_smokers[~condition]
        expl = f"{len(viol)} non-smokers violate the rule (diastolic BPs: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All patients with a diagnosis of arthritis have a BMI less than 30."""
    arthritics = df[df["diagnosis"] == "arthritis"]
    condition = arthritics["bmi"] < 30
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritics)} arthritis patients have BMI < 30."
    else:
        viol = arthritics[~condition]
        expl = f"{len(viol)} arthritis patients violate the rule (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients in the table have a systolic blood pressure greater than 120 mmHg."""
    total = len(df)
    high_bp = df[df["bp_systolic"] > 120]
    truth = len(high_bp) > total / 2
    if truth:
        expl = f"{len(high_bp)} out of {total} patients have systolic BP > 120 mmHg."
    else:
        expl = f"{len(high_bp)} out of {total} patients have systolic BP > 120 mmHg (less than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient's age is greater than 60, then their cholesterol level is less than 240 mg/dl."""
    older = df[df["age"] > 60]
    condition = older["cholesterol_mg_dl"] < 240
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} patients over 60 have cholesterol < 240 mg/dl."
    else:
        viol = older[~condition]
        expl = f"{len(viol)} patients over 60 violate the rule (cholesterols: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. For all patients with a BMI between 20 and 25, their age is less than 62 years."""
    bmi_range = df[(df["bmi"] >= 20) & (df["bmi"] <= 25)]
    condition = bmi_range["age"] < 62
    truth = condition.all()
    if truth:
        expl = f"All {len(bmi_range)} patients with BMI 20-25 are under 62 years old."
    else:
        viol = bmi_range[~condition]
        expl = f"{len(viol)} patients with BMI 20-25 violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one patient with a diagnosis of hypertension whose systolic blood pressure is greater than 150 mmHg."""
    hypertensives = df[df["diagnosis"] == "hypertension"]
    condition = hypertensives["bp_systolic"] > 150
    truth = condition.any()
    if truth:
        found = hypertensives[condition]
        expl = f"At least one hypertension patient (ID: {found.iloc[0]['patient_id']}) has systolic BP > 150 mmHg."
    else:
        expl = "No hypertension patients have systolic BP > 150 mmHg."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All patients with a cholesterol level greater than 220 mg/dl have a BMI greater than 23.8."""
    high_cholesterol = df[df["cholesterol_mg_dl"] > 220]
    condition = high_cholesterol["bmi"] > 23.8
    truth = condition.all()
    if truth:
        expl = f"All {len(high_cholesterol)} patients with cholesterol > 220 have BMI > 23.8."
    else:
        viol = high_cholesterol[~condition]
        expl = f"{len(viol)} patients with cholesterol > 220 violate the rule (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a patient is a smoker and has a diagnosis of asthma, then their age is less than 77 years."""
    smokers_asthmatics = df[(df["smoker"] == "yes") & (df["diagnosis"] == "asthma")]
    condition = smokers_asthmatics["age"] < 77
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers_asthmatics)} smoker-asthma patients are under 77 years old."
    else:
        viol = smokers_asthmatics[~condition]
        expl = f"{len(viol)} smoker-asthma patients violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. For all patients with a diastolic blood pressure greater than 80 mmHg, their systolic blood pressure is greater than 140 mmHg."""
    high_dbp = df[df["bp_diastolic"] > 80]
    condition = high_dbp["bp_systolic"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(high_dbp)} patients with DBP > 80 have systolic BP > 140 mmHg."
    else:
        viol = high_dbp[~condition]
        expl = f"{len(viol)} patients with DBP > 80 violate the rule (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Most patients in the table have a BMI greater than 25."""
    total = len(df)
    high_bmi = df[df["bmi"] > 25]
    truth = len(high_bmi) > total / 2
    if truth:
        expl = f"{len(high_bmi)} out of {total} patients have BMI > 25."
    else:
        expl = f"{len(high_bmi)} out of {total} patients have BMI > 25 (less than half)."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a patient's age is less than 40, then their cholesterol level is greater than 200 mg/dl."""
    young = df[df["age"] < 40]
    condition = young["cholesterol_mg_dl"] > 200
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} patients under 40 have cholesterol > 200 mg/dl."
    else:
        viol = young[~condition]
        expl = f"{len(viol)} patients under 40 violate the rule (cholesterols: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one patient with a diagnosis of diabetes whose BMI is greater than 32."""
    diabetic_high_bmi = df[(df["diagnosis"] == "diabetes") & (df["bmi"] > 32)]
    truth = len(diabetic_high_bmi) > 0
    if truth:
        found = diabetic_high_bmi.iloc[0]
        expl = f"At least one diabetes patient (ID: {found['patient_id']}) has BMI > 32."
    else:
        expl = "No diabetes patients have BMI > 32."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All patients with a systolic blood pressure greater than 150 mmHg have a diagnosis of either diabetes or hypertension."""
    high_sbp = df[df["bp_systolic"] > 150]
    valid_diag = (high_sbp["diagnosis"] == "diabetes") | (high_sbp["diagnosis"] == "hypertension")
    truth = valid_diag.all()
    if truth:
        expl = f"All {len(high_sbp)} patients with SBP > 150 have diagnosis of diabetes or hypertension."
    else:
        viol = high_sbp[~valid_diag]
        expl = f"{len(viol)} patients with SBP > 150 do not have diagnosis of diabetes or hypertension (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
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