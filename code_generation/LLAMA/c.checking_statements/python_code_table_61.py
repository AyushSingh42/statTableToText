import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of arthritis have a BMI less than or equal to 33.9."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    if arthritis_patients.empty:
        truth = True
        expl = "No patients with arthritis in dataset."
    else:
        condition = arthritis_patients["bmi"] <= 33.9
        truth = condition.all()
        if truth:
            expl = f"All {len(arthritis_patients)} arthritis patients have BMI <= 33.9."
        else:
            viol = arthritis_patients[~condition]
            expl = f"{len(viol)} arthritis patients have BMI > 33.9 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is less than 70 years."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        truth = True
        expl = "No smokers in dataset."
    else:
        condition = smokers["age"] < 70
        truth = condition.all()
        if truth:
            expl = f"All {len(smokers)} smokers are under 70 years old."
        else:
            viol = smokers[~condition]
            expl = f"{len(viol)} smokers are 70 or older (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All patients with a diagnosis of hypertension have a systolic blood pressure greater than or equal to 142 mmHg."""
    hypertensive_patients = df[df["diagnosis"] == "hypertension"]
    if hypertensive_patients.empty:
        truth = True
        expl = "No patients with hypertension in dataset."
    else:
        condition = hypertensive_patients["bp_systolic"] >= 142
        truth = condition.all()
        if truth:
            expl = f"All {len(hypertensive_patients)} hypertensive patients have BP systolic >= 142."
        else:
            viol = hypertensive_patients[~condition]
            expl = f"{len(viol)} hypertensive patients have BP systolic < 142 (values: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one patient with a diagnosis of asthma whose cholesterol level is greater than 240 mg/dL."""
    asthmatics = df[df["diagnosis"] == "asthma"]
    if asthmatics.empty:
        truth = False
        expl = "No patients with asthma in dataset."
    else:
        condition = asthmatics["cholesterol_mg_dl"] > 240
        truth = condition.any()
        if truth:
            found = asthmatics[condition]
            expl = f"At least one asthma patient has cholesterol > 240 mg/dL (cholesterol: {found['cholesterol_mg_dl'].iloc[0]})."
        else:
            expl = f"No asthma patients have cholesterol > 240 mg/dL."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient's BMI is greater than 30, then their age is less than 70 years."""
    high_bmi = df[df["bmi"] > 30]
    if high_bmi.empty:
        truth = True
        expl = "No patients with BMI > 30 in dataset."
    else:
        condition = high_bmi["age"] < 70
        truth = condition.all()
        if truth:
            expl = f"All {len(high_bmi)} patients with BMI > 30 are under 70 years old."
        else:
            viol = high_bmi[~condition]
            expl = f"{len(viol)} patients with BMI > 30 are 70 or older (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All patients with a diagnosis of migraine have a diastolic blood pressure less than 80 mmHg."""
    migraines = df[df["diagnosis"] == "migraine"]
    if migraines.empty:
        truth = True
        expl = "No patients with migraine in dataset."
    else:
        condition = migraines["bp_diastolic"] < 80
        truth = condition.all()
        if truth:
            expl = f"All {len(migraines)} migraine patients have diastolic BP < 80."
        else:
            viol = migraines[~condition]
            expl = f"{len(viol)} migraine patients have diastolic BP >= 80 (values: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients in the table have a systolic blood pressure greater than 120 mmHg."""
    total = len(df)
    condition = df["bp_systolic"] > 120
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} patients have BP systolic > 120 (more than half)."
    else:
        expl = f"{count} out of {total} patients have BP systolic > 120 (not more than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient's age is greater than 60 years, then their cholesterol level is less than 220 mg/dL."""
    elderly = df[df["age"] > 60]
    if elderly.empty:
        truth = True
        expl = "No patients over 60 in dataset."
    else:
        condition = elderly["cholesterol_mg_dl"] < 220
        truth = condition.all()
        if truth:
            expl = f"All {len(elderly)} patients over 60 have cholesterol < 220 mg/dL."
        else:
            viol = elderly[~condition]
            expl = f"{len(viol)} patients over 60 have cholesterol >= 220 mg/dL (cholesterols: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All patients with a diagnosis of arthritis have a cholesterol level greater than 190 mg/dL."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    if arthritis_patients.empty:
        truth = True
        expl = "No patients with arthritis in dataset."
    else:
        condition = arthritis_patients["cholesterol_mg_dl"] > 190
        truth = condition.all()
        if truth:
            expl = f"All {len(arthritis_patients)} arthritis patients have cholesterol > 190 mg/dL."
        else:
            viol = arthritis_patients[~condition]
            expl = f"{len(viol)} arthritis patients have cholesterol <= 190 mg/dL (cholesterols: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one patient with a diagnosis of hypertension whose BMI is less than 28."""
    hypertensives = df[df["diagnosis"] == "hypertension"]
    if hypertensives.empty:
        truth = False
        expl = "No patients with hypertension in dataset."
    else:
        condition = hypertensives["bmi"] < 28
        truth = condition.any()
        if truth:
            found = hypertensives[condition]
            expl = f"At least one hypertensive patient has BMI < 28 (BMI: {found['bmi'].iloc[0]})."
        else:
            expl = f"No hypertensive patients have BMI < 28."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a patient is a non-smoker, then their BMI is less than 33."""
    non_smokers = df[df["smoker"] == "no"]
    if non_smokers.empty:
        truth = True
        expl = "No non-smokers in dataset."
    else:
        condition = non_smokers["bmi"] < 33
        truth = condition.all()
        if truth:
            expl = f"All {len(non_smokers)} non-smokers have BMI < 33."
        else:
            viol = non_smokers[~condition]
            expl = f"{len(viol)} non-smokers have BMI >= 33 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All patients with a cholesterol level greater than 230 mg/dL have a systolic blood pressure greater than 120 mmHg."""
    high_cholesterol = df[df["cholesterol_mg_dl"] > 230]
    if high_cholesterol.empty:
        truth = True
        expl = "No patients with cholesterol > 230 in dataset."
    else:
        condition = high_cholesterol["bp_systolic"] > 120
        truth = condition.all()
        if truth:
            expl = f"All {len(high_cholesterol)} patients with cholesterol > 230 have BP systolic > 120."
        else:
            viol = high_cholesterol[~condition]
            expl = f"{len(viol)} patients with cholesterol > 230 have BP systolic <= 120 (BP values: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most patients in the table have a BMI greater than 20."""
    total = len(df)
    condition = df["bmi"] > 20
    count = condition.sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} patients have BMI > 20 (more than half)."
    else:
        expl = f"{count} out of {total} patients have BMI > 20 (not more than half)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a patient's age is less than 40 years, then their cholesterol level is less than 220 mg/dL."""
    young = df[df["age"] < 40]
    if young.empty:
        truth = True
        expl = "No patients under 40 in dataset."
    else:
        condition = young["cholesterol_mg_dl"] < 220
        truth = condition.all()
        if truth:
            expl = f"All {len(young)} patients under 40 have cholesterol < 220 mg/dL."
        else:
            viol = young[~condition]
            expl = f"{len(viol)} patients under 40 have cholesterol >= 220 mg/dL (cholesterols: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All patients with a diagnosis of asthma have a diastolic blood pressure greater than 85 mmHg."""
    asthmatics = df[df["diagnosis"] == "asthma"]
    if asthmatics.empty:
        truth = True
        expl = "No patients with asthma in dataset."
    else:
        condition = asthmatics["bp_diastolic"] > 85
        truth = condition.all()
        if truth:
            expl = f"All {len(asthmatics)} asthma patients have diastolic BP > 85."
        else:
            viol = asthmatics[~condition]
            expl = f"{len(viol)} asthma patients have diastolic BP <= 85 (values: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one patient with a diagnosis of migraine whose BMI is less than 28."""
    migraines = df[df["diagnosis"] == "migraine"]
    if migraines.empty:
        truth = False
        expl = "No patients with migraine in dataset."
    else:
        condition = migraines["bmi"] < 28
        truth = condition.any()
        if truth:
            found = migraines[condition]
            expl = f"At least one migraine patient has BMI < 28 (BMI: {found['bmi'].iloc[0]})."
        else:
            expl = f"No migraine patients have BMI < 28."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a patient's systolic blood pressure is greater than 140 mmHg, then their age is less than 80 years."""
    high_bp = df[df["bp_systolic"] > 140]
    if high_bp.empty:
        truth = True
        expl = "No patients with BP systolic > 140 in dataset."
    else:
        condition = high_bp["age"] < 80
        truth = condition.all()
        if truth:
            expl = f"All {len(high_bp)} patients with BP systolic > 140 are under 80 years old."
        else:
            viol = high_bp[~condition]
            expl = f"{len(viol)} patients with BP systolic > 140 are 80 or older (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_61.csv")

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