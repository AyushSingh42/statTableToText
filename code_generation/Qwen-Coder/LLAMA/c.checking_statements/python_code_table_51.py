import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with asthma have a BMI greater than or equal to 20.6."""
    asthmatics = df[df["diagnosis"] == "asthma"]
    if asthmatics.empty:
        truth = True
        expl = "No patients with asthma in dataset."
    else:
        condition = asthmatics["bmi"] >= 20.6
        truth = condition.all()
        if truth:
            expl = f"All {len(asthmatics)} asthma patients have BMI >= 20.6."
        else:
            viol = asthmatics[~condition]
            expl = f"{len(viol)} asthma patients have BMI < 20.6 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All patients with diabetes have a cholesterol level greater than or equal to 191 mg/dl."""
    diabetics = df[df["diagnosis"] == "diabetes"]
    if diabetics.empty:
        truth = True
        expl = "No patients with diabetes in dataset."
    else:
        condition = diabetics["cholesterol_mg_dl"] >= 191
        truth = condition.all()
        if truth:
            expl = f"All {len(diabetics)} diabetic patients have cholesterol >= 191 mg/dl."
        else:
            viol = diabetics[~condition]
            expl = f"{len(viol)} diabetic patients have cholesterol < 191 mg/dl (cholesterols: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a patient is a smoker, then their BMI is greater than or equal to 22.7."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        truth = True
        expl = "No smokers in dataset."
    else:
        condition = smokers["bmi"] >= 22.7
        truth = condition.all()
        if truth:
            expl = f"All {len(smokers)} smokers have BMI >= 22.7."
        else:
            viol = smokers[~condition]
            expl = f"{len(viol)} smokers have BMI < 22.7 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one patient with arthritis whose systolic blood pressure is greater than 150 mmHg."""
    arthritics = df[df["diagnosis"] == "arthritis"]
    if arthritics.empty:
        truth = False
        expl = "No patients with arthritis in dataset."
    else:
        condition = arthritics["bp_systolic"] > 150
        truth = condition.any()
        if truth:
            found = arthritics[condition]
            expl = f"At least one arthritis patient (ID: {found.iloc[0]['patient_id']}) has systolic BP > 150 mmHg."
        else:
            expl = f"No arthritis patients have systolic BP > 150 mmHg."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All patients with hypertension have a diastolic blood pressure greater than or equal to 74 mmHg."""
    hypertensives = df[df["diagnosis"] == "hypertension"]
    if hypertensives.empty:
        truth = True
        expl = "No patients with hypertension in dataset."
    else:
        condition = hypertensives["bp_diastolic"] >= 74
        truth = condition.all()
        if truth:
            expl = f"All {len(hypertensives)} hypertensive patients have diastolic BP >= 74 mmHg."
        else:
            viol = hypertensives[~condition]
            expl = f"{len(viol)} hypertensive patients have diastolic BP < 74 mmHg (diastolic BPs: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a patient's age is greater than 50, then their systolic blood pressure is less than or equal to 156 mmHg."""
    older = df[df["age"] > 50]
    if older.empty:
        truth = True
        expl = "No patients over age 50 in dataset."
    else:
        condition = older["bp_systolic"] <= 156
        truth = condition.all()
        if truth:
            expl = f"All {len(older)} patients over age 50 have systolic BP <= 156 mmHg."
        else:
            viol = older[~condition]
            expl = f"{len(viol)} patients over age 50 have systolic BP > 156 mmHg (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients have a cholesterol level greater than 200 mg/dl."""
    total = len(df)
    high_cholesterol = df[df["cholesterol_mg_dl"] > 200]
    proportion = len(high_cholesterol) / total
    truth = proportion > 0.5
    expl = f"{len(high_cholesterol)} out of {total} patients have cholesterol > 200 mg/dl ({proportion:.2%} of total)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All patients with migraine have a BMI greater than or equal to 26.9."""
    migrainics = df[df["diagnosis"] == "migraine"]
    if migrainics.empty:
        truth = True
        expl = "No patients with migraine in dataset."
    else:
        condition = migrainics["bmi"] >= 26.9
        truth = condition.all()
        if truth:
            expl = f"All {len(migrainics)} migraine patients have BMI >= 26.9."
        else:
            viol = migrainics[~condition]
            expl = f"{len(viol)} migraine patients have BMI < 26.9 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a patient's BMI is greater than 30, then they are a smoker."""
    obese = df[df["bmi"] > 30]
    if obese.empty:
        truth = True
        expl = "No patients with BMI > 30 in dataset."
    else:
        condition = obese["smoker"] == "yes"
        truth = condition.all()
        if truth:
            expl = f"All {len(obese)} patients with BMI > 30 are smokers."
        else:
            viol = obese[~condition]
            expl = f"{len(viol)} patients with BMI > 30 are not smokers (IDs: {', '.join(viol['patient_id'].tolist())})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one patient with diabetes whose age is less than 30."""
    diabetics = df[df["diagnosis"] == "diabetes"]
    if diabetics.empty:
        truth = False
        expl = "No patients with diabetes in dataset."
    else:
        young_diabetics = diabetics[diabetics["age"] < 30]
        truth = not young_diabetics.empty
        if truth:
            expl = f"At least one diabetic patient (ID: {young_diabetics.iloc[0]['patient_id']}) is under 30 years old."
        else:
            expl = "No diabetic patients are under 30 years old."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All patients with asthma have a systolic blood pressure greater than or equal to 119 mmHg."""
    asthmatics = df[df["diagnosis"] == "asthma"]
    if asthmatics.empty:
        truth = True
        expl = "No patients with asthma in dataset."
    else:
        condition = asthmatics["bp_systolic"] >= 119
        truth = condition.all()
        if truth:
            expl = f"All {len(asthmatics)} asthma patients have systolic BP >= 119 mmHg."
        else:
            viol = asthmatics[~condition]
            expl = f"{len(viol)} asthma patients have systolic BP < 119 mmHg (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a patient is a non-smoker, then their BMI is less than or equal to 31.8."""
    non_smokers = df[df["smoker"] == "no"]
    if non_smokers.empty:
        truth = True
        expl = "No non-smokers in dataset."
    else:
        condition = non_smokers["bmi"] <= 31.8
        truth = condition.all()
        if truth:
            expl = f"All {len(non_smokers)} non-smokers have BMI <= 31.8."
        else:
            viol = non_smokers[~condition]
            expl = f"{len(viol)} non-smokers have BMI > 31.8 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All patients with hypertension have an age greater than or equal to 43."""
    hypertensives = df[df["diagnosis"] == "hypertension"]
    if hypertensives.empty:
        truth = True
        expl = "No patients with hypertension in dataset."
    else:
        condition = hypertensives["age"] >= 43
        truth = condition.all()
        if truth:
            expl = f"All {len(hypertensives)} hypertensive patients are aged >= 43."
        else:
            viol = hypertensives[~condition]
            expl = f"{len(viol)} hypertensive patients are under 43 years old (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Most patients are smokers."""
    total = len(df)
    smokers = df[df["smoker"] == "yes"]
    proportion = len(smokers) / total
    truth = proportion > 0.5
    expl = f"{len(smokers)} out of {total} patients are smokers ({proportion:.2%} of total)."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a patient's cholesterol level is greater than 230 mg/dl, then they are a smoker."""
    high_cholesterol = df[df["cholesterol_mg_dl"] > 230]
    if high_cholesterol.empty:
        truth = True
        expl = "No patients with cholesterol > 230 mg/dl in dataset."
    else:
        condition = high_cholesterol["smoker"] == "yes"
        truth = condition.all()
        if truth:
            expl = f"All {len(high_cholesterol)} patients with cholesterol > 230 mg/dl are smokers."
        else:
            viol = high_cholesterol[~condition]
            expl = f"{len(viol)} patients with cholesterol > 230 mg/dl are not smokers (IDs: {', '.join(viol['patient_id'].tolist())})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All patients with arthritis have a systolic blood pressure greater than or equal to 156 mmHg."""
    arthritics = df[df["diagnosis"] == "arthritis"]
    if arthritics.empty:
        truth = True
        expl = "No patients with arthritis in dataset."
    else:
        condition = arthritics["bp_systolic"] >= 156
        truth = condition.all()
        if truth:
            expl = f"All {len(arthritics)} arthritis patients have systolic BP >= 156 mmHg."
        else:
            viol = arthritics[~condition]
            expl = f"{len(viol)} arthritis patients have systolic BP < 156 mmHg (systolic BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. There exists at least one patient with migraine whose diastolic blood pressure is less than 90 mmHg."""
    migrainics = df[df["diagnosis"] == "migraine"]
    if migrainics.empty:
        truth = False
        expl = "No patients with migraine in dataset."
    else:
        low_diastolic = migrainics[migrainics["bp_diastolic"] < 90]
        truth = not low_diastolic.empty
        if truth:
            expl = f"At least one migraine patient (ID: {low_diastolic.iloc[0]['patient_id']}) has diastolic BP < 90 mmHg."
        else:
            expl = "No migraine patients have diastolic BP < 90 mmHg."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_51.csv")

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