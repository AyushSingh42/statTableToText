import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of arthritis have a BMI less than or equal to 34."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    if arthritis_patients.empty:
        truth = True
        expl = "No patients with arthritis in dataset."
    else:
        condition = arthritis_patients["bmi"] <= 34
        truth = condition.all()
        if truth:
            expl = f"All {len(arthritis_patients)} arthritis patients have BMI <= 34."
        else:
            viol = arthritis_patients[~condition]
            expl = f"{len(viol)} arthritis patients have BMI > 34 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is greater than or equal to 49 or less than or equal to 63."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        truth = True
        expl = "No smokers in dataset."
    else:
        condition = (smokers["age"] >= 49) | (smokers["age"] <= 63)
        truth = condition.all()
        if truth:
            expl = f"All {len(smokers)} smokers are aged >=49 or <=63."
        else:
            viol = smokers[~condition]
            expl = f"{len(viol)} smokers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of asthma whose cholesterol level is less than 180 mg/dl."""
    asthmatics = df[df["diagnosis"] == "asthma"]
    if asthmatics.empty:
        truth = False
        expl = "No patients with asthma in dataset."
    else:
        condition = asthmatics["cholesterol_mg_dl"] < 180
        truth = condition.any()
        if truth:
            satisfied = asthmatics[condition]
            expl = f"At least one asthma patient (n={len(satisfied)}) has cholesterol < 180 mg/dl."
        else:
            expl = f"No asthma patients have cholesterol < 180 mg/dl."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all patients with a BMI greater than 30, their systolic blood pressure is greater than or equal to 120."""
    high_bmi = df[df["bmi"] > 30]
    if high_bmi.empty:
        truth = True
        expl = "No patients with BMI > 30 in dataset."
    else:
        condition = high_bmi["bp_systolic"] >= 120
        truth = condition.all()
        if truth:
            expl = f"All {len(high_bmi)} patients with BMI > 30 have BP systolic >= 120."
        else:
            viol = high_bmi[~condition]
            expl = f"{len(viol)} patients with BMI > 30 have BP systolic < 120 (BP values: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient has a diagnosis of diabetes, then their diastolic blood pressure is greater than or equal to 71."""
    diabetics = df[df["diagnosis"] == "diabetes"]
    if diabetics.empty:
        truth = True
        expl = "No patients with diabetes in dataset."
    else:
        condition = diabetics["bp_diastolic"] >= 71
        truth = condition.all()
        if truth:
            expl = f"All {len(diabetics)} diabetic patients have diastolic BP >= 71."
        else:
            viol = diabetics[~condition]
            expl = f"{len(viol)} diabetic patients have diastolic BP < 71 (BP values: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All patients with a systolic blood pressure greater than 150 have a diagnosis of either migraine or hypertension."""
    high_bp = df[df["bp_systolic"] > 150]
    if high_bp.empty:
        truth = True
        expl = "No patients with systolic BP > 150 in dataset."
    else:
        valid_diag = (high_bp["diagnosis"] == "migraine") | (high_bp["diagnosis"] == "hypertension")
        truth = valid_diag.all()
        if truth:
            expl = f"All {len(high_bp)} patients with BP systolic > 150 have diagnosis of migraine or hypertension."
        else:
            viol = high_bp[~valid_diag]
            expl = f"{len(viol)} patients with BP systolic > 150 do not have diagnosis of migraine or hypertension (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients in the table have a cholesterol level greater than 200 mg/dl."""
    total = len(df)
    high_chol = df[df["cholesterol_mg_dl"] > 200]
    count_high = len(high_chol)
    truth = count_high > total / 2
    if truth:
        expl = f"More than half ({count_high}/{total}) of patients have cholesterol > 200 mg/dl."
    else:
        expl = f"Less than half ({count_high}/{total}) of patients have cholesterol > 200 mg/dl."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is a non-smoker, then their BMI is greater than or equal to 28.9."""
    non_smokers = df[df["smoker"] == "no"]
    if non_smokers.empty:
        truth = True
        expl = "No non-smokers in dataset."
    else:
        condition = non_smokers["bmi"] >= 28.9
        truth = condition.all()
        if truth:
            expl = f"All {len(non_smokers)} non-smokers have BMI >= 28.9."
        else:
            viol = non_smokers[~condition]
            expl = f"{len(viol)} non-smokers have BMI < 28.9 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one patient with a diagnosis of migraine whose BMI is less than 25."""
    migraines = df[df["diagnosis"] == "migraine"]
    if migraines.empty:
        truth = False
        expl = "No patients with migraine in dataset."
    else:
        condition = migraines["bmi"] < 25
        truth = condition.any()
        if truth:
            satisfied = migraines[condition]
            expl = f"At least one migraine patient (n={len(satisfied)}) has BMI < 25."
        else:
            expl = f"No migraine patients have BMI < 25."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. For all patients with a diastolic blood pressure less than 90, their age is greater than or equal to 49."""
    low_dbp = df[df["bp_diastolic"] < 90]
    if low_dbp.empty:
        truth = True
        expl = "No patients with diastolic BP < 90 in dataset."
    else:
        condition = low_dbp["age"] >= 49
        truth = condition.all()
        if truth:
            expl = f"All {len(low_dbp)} patients with diastolic BP < 90 are aged >= 49."
        else:
            viol = low_dbp[~condition]
            expl = f"{len(viol)} patients with diastolic BP < 90 are aged < 49 (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_41.csv")

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
        (10, stmt_10)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()