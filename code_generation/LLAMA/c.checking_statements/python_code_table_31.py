import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of asthma have a BMI less than 33."""
    asthma_patients = df[df["diagnosis"] == "asthma"]
    condition = asthma_patients["bmi"] < 33
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma_patients)} asthma patients have BMI < 33."
    else:
        viol = asthma_patients[~condition]
        expl = f"{len(viol)} asthma patients have BMI >= 33 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their cholesterol level is greater than 200 mg/dl."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["cholesterol_mg_dl"] > 200
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have cholesterol > 200 mg/dl."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers have cholesterol <= 200 mg/dl (cholesterols: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of diabetes who is less than 25 years old."""
    diabetic_young = df[(df["diagnosis"] == "diabetes") & (df["age"] < 25)]
    truth = len(diabetic_young) > 0
    if truth:
        expl = f"There is at least one diabetic under 25 (age: {diabetic_young.iloc[0]['age']})."
    else:
        expl = "No diabetic patients under 25 found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All patients with a diagnosis of arthritis have a systolic blood pressure less than 160."""
    arthritis_patients = df[df["diagnosis"] == "arthritis"]
    condition = arthritis_patients["bp_systolic"] < 160
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritis_patients)} arthritis patients have systolic BP < 160."
    else:
        viol = arthritis_patients[~condition]
        expl = f"{len(viol)} arthritis patients have systolic BP >= 160 (BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient's BMI is greater than 30, then they are a smoker."""
    high_bmi = df[df["bmi"] > 30]
    condition = high_bmi["smoker"] == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 are smokers."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 30 are not smokers (IDs: {', '.join(viol['patient_id'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most patients with a diagnosis of asthma have a diastolic blood pressure less than 90."""
    asthma_patients = df[df["diagnosis"] == "asthma"]
    condition = asthma_patients["bp_diastolic"] < 90
    satisfied = condition.sum()
    total = len(asthma_patients)
    truth = satisfied > total / 2
    if truth:
        expl = f"More than half ({satisfied}/{total}) of asthma patients have diastolic BP < 90."
    else:
        expl = f"Less than half ({satisfied}/{total}) of asthma patients have diastolic BP < 90."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All patients with a systolic blood pressure greater than 150 have a diagnosis of either hypertension or asthma."""
    high_bp = df[df["bp_systolic"] > 150]
    condition = (high_bp["diagnosis"] == "hypertension") | (high_bp["diagnosis"] == "asthma")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bp)} patients with systolic BP > 150 have diagnosis of hypertension or asthma."
    else:
        viol = high_bp[~condition]
        expl = f"{len(viol)} patients with systolic BP > 150 do not have diagnosis of hypertension or asthma (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is less than 40 years old, then their BMI is less than 28."""
    young = df[df["age"] < 40]
    condition = young["bmi"] < 28
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} patients under 40 have BMI < 28."
    else:
        viol = young[~condition]
        expl = f"{len(viol)} patients under 40 have BMI >= 28 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one patient with a diagnosis of migraine who is less than 45 years old and has a BMI greater than 30."""
    migraine_young_high_bmi = df[(df["diagnosis"] == "migraine") & (df["age"] < 45) & (df["bmi"] > 30)]
    truth = len(migraine_young_high_bmi) > 0
    if truth:
        expl = f"There is at least one migraine patient under 45 with BMI > 30 (age: {migraine_young_high_bmi.iloc[0]['age']}, BMI: {migraine_young_high_bmi.iloc[0]['bmi']})."
    else:
        expl = "No migraine patients under 45 with BMI > 30 found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All patients with a cholesterol level greater than 220 mg/dl have a diagnosis of either diabetes or arthritis."""
    high_chol = df[df["cholesterol_mg_dl"] > 220]
    condition = (high_chol["diagnosis"] == "diabetes") | (high_chol["diagnosis"] == "arthritis")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_chol)} patients with cholesterol > 220 have diagnosis of diabetes or arthritis."
    else:
        viol = high_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol > 220 do not have diagnosis of diabetes or arthritis (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a patient's diastolic blood pressure is less than 80, then their age is less than 60."""
    low_diastolic = df[df["bp_diastolic"] < 80]
    condition = low_diastolic["age"] < 60
    truth = condition.all()
    if truth:
        expl = f"All {len(low_diastolic)} patients with diastolic BP < 80 are under 60."
    else:
        viol = low_diastolic[~condition]
        expl = f"{len(viol)} patients with diastolic BP < 80 are 60 or older (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most patients with a diagnosis of diabetes have a BMI greater than 25."""
    diabetic = df[df["diagnosis"] == "diabetes"]
    condition = diabetic["bmi"] > 25
    satisfied = condition.sum()
    total = len(diabetic)
    truth = satisfied > total / 2
    if truth:
        expl = f"More than half ({satisfied}/{total}) of diabetic patients have BMI > 25."
    else:
        expl = f"Less than half ({satisfied}/{total}) of diabetic patients have BMI > 25."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All patients with a BMI less than 22 have a diagnosis of either asthma or arthritis."""
    low_bmi = df[df["bmi"] < 22]
    condition = (low_bmi["diagnosis"] == "asthma") | (low_bmi["diagnosis"] == "arthritis")
    truth = condition.all()
    if truth:
        expl = f"All {len(low_bmi)} patients with BMI < 22 have diagnosis of asthma or arthritis."
    else:
        viol = low_bmi[~condition]
        expl = f"{len(viol)} patients with BMI < 22 do not have diagnosis of asthma or arthritis (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a patient is a smoker and has a BMI greater than 25, then their systolic blood pressure is greater than 140."""
    smokers_high_bmi = df[(df["smoker"] == "yes") & (df["bmi"] > 25)]
    condition = smokers_high_bmi["bp_systolic"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers_high_bmi)} smokers with BMI > 25 have systolic BP > 140."
    else:
        viol = smokers_high_bmi[~condition]
        expl = f"{len(viol)} smokers with BMI > 25 have systolic BP <= 140 (BPs: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one patient with a diagnosis of asthma who is less than 25 years old and has a BMI greater than 22."""
    asthma_young_high_bmi = df[(df["diagnosis"] == "asthma") & (df["age"] < 25) & (df["bmi"] > 22)]
    truth = len(asthma_young_high_bmi) > 0
    if truth:
        expl = f"There is at least one asthma patient under 25 with BMI > 22 (age: {asthma_young_high_bmi.iloc[0]['age']}, BMI: {asthma_young_high_bmi.iloc[0]['bmi']})."
    else:
        expl = "No asthma patients under 25 with BMI > 22 found."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All patients with a systolic blood pressure less than 120 have a diagnosis of either arthritis or migraine."""
    low_bp = df[df["bp_systolic"] < 120]
    condition = (low_bp["diagnosis"] == "arthritis") | (low_bp["diagnosis"] == "migraine")
    truth = condition.all()
    if truth:
        expl = f"All {len(low_bp)} patients with systolic BP < 120 have diagnosis of arthritis or migraine."
    else:
        viol = low_bp[~condition]
        expl = f"{len(viol)} patients with systolic BP < 120 do not have diagnosis of arthritis or migraine (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a patient's cholesterol level is less than 200 mg/dl, then their age is less than 50."""
    low_chol = df[df["cholesterol_mg_dl"] < 200]
    condition = low_chol["age"] < 50
    truth = condition.all()
    if truth:
        expl = f"All {len(low_chol)} patients with cholesterol < 200 have age < 50."
    else:
        viol = low_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol < 200 have age >= 50 (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most patients with a diagnosis of arthritis have a BMI less than 27."""
    arthritis = df[df["diagnosis"] == "arthritis"]
    condition = arthritis["bmi"] < 27
    satisfied = condition.sum()
    total = len(arthritis)
    truth = satisfied > total / 2
    if truth:
        expl = f"More than half ({satisfied}/{total}) of arthritis patients have BMI < 27."
    else:
        expl = f"Less than half ({satisfied}/{total}) of arthritis patients have BMI < 27."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All patients with a BMI greater than 28 have a diagnosis of either diabetes or hypertension."""
    high_bmi = df[df["bmi"] > 28]
    condition = (high_bmi["diagnosis"] == "diabetes") | (high_bmi["diagnosis"] == "hypertension")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 28 have diagnosis of diabetes or hypertension."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 28 do not have diagnosis of diabetes or hypertension (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a patient is less than 30 years old, then their diastolic blood pressure is less than 85."""
    young = df[df["age"] < 30]
    condition = young["bp_diastolic"] < 85
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} patients under 30 have diastolic BP < 85."
    else:
        viol = young[~condition]
        expl = f"{len(viol)} patients under 30 have diastolic BP >= 85 (BPs: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one patient with a diagnosis of migraine who is less than 50 years old and has a BMI less than 25."""
    migraine_young_low_bmi = df[(df["diagnosis"] == "migraine") & (df["age"] < 50) & (df["bmi"] < 25)]
    truth = len(migraine_young_low_bmi) > 0
    if truth:
        expl = f"There is at least one migraine patient under 50 with BMI < 25 (age: {migraine_young_low_bmi.iloc[0]['age']}, BMI: {migraine_young_low_bmi.iloc[0]['bmi']})."
    else:
        expl = "No migraine patients under 50 with BMI < 25 found."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_31.csv")

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
        (21, stmt_21)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()