import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of arthritis have a BMI less than 33."""
    arth = df[df["diagnosis"] == "arthritis"]
    condition = arth["bmi"] < 33
    truth = condition.all()
    if truth:
        expl = f"All {len(arth)} arthritis patients have BMI < 33."
    else:
        viol = arth[~condition]
        expl = f"{len(viol)} arthritis patients violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is less than 65."""
    smokers = df[df["smoker"]]
    condition = smokers["age"] < 65
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers are younger than 65."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of diabetes whose cholesterol level is less than 200 mg/dl."""
    exists = df[(df["diagnosis"] == "diabetes") & (df["cholesterol_mg_dl"] < 200)].any(axis=1).any()
    truth = exists
    if truth:
        count = df[(df["diagnosis"] == "diabetes") & (df["cholesterol_mg_dl"] < 200)].shape[0]
        expl = f"Found {count} diabetes patient(s) with cholesterol < 200 mg/dl."
    else:
        expl = "No diabetes patient has cholesterol < 200 mg/dl."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All patients with a systolic blood pressure greater than 140 have a diastolic blood pressure greater than 70."""
    high_sys = df[df["bp_systolic"] > 140]
    condition = high_sys["bp_diastolic"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sys)} patients with systolic > 140 have diastolic > 70."
    else:
        viol = high_sys[~condition]
        expl = f"{len(viol)} patients violate the rule (diastolic: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient has a BMI greater than 30, then they are a smoker."""
    high_bmi = df[df["bmi"] > 30]
    condition = high_bmi["smoker"]
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 are smokers."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 30 are not smokers (IDs: {', '.join(viol['patient_id'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most patients have a cholesterol level greater than 180 mg/dl."""
    total = len(df)
    count = df[df["cholesterol_mg_dl"] > 180].shape[0]
    truth = count > total / 2
    percent = count / total * 100
    if truth:
        expl = f"{count} out of {total} patients ({percent:.1f}%) have cholesterol > 180 mg/dl."
    else:
        expl = f"Only {count} out of {total} patients ({percent:.1f}%) have cholesterol > 180 mg/dl."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All patients with a diagnosis of asthma have a BMI greater than 28."""
    asth = df[df["diagnosis"] == "asthma"]
    condition = asth["bmi"] > 28
    truth = condition.all()
    if truth:
        expl = f"All {len(asth)} asthma patients have BMI > 28."
    else:
        viol = asth[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is older than 50, then their systolic blood pressure is greater than 120."""
    older = df[df["age"] > 50]
    condition = older["bp_systolic"] > 120
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} patients older than 50 have systolic > 120."
    else:
        viol = older[~condition]
        expl = f"{len(viol)} patients older than 50 violate the rule (systolic: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one patient with a diagnosis of migraine whose BMI is less than 22."""
    exists = df[(df["diagnosis"] == "migraine") & (df["bmi"] < 22)].any(axis=1).any()
    truth = exists
    if truth:
        count = df[(df["diagnosis"] == "migraine") & (df["bmi"] < 22)].shape[0]
        expl = f"Found {count} migraine patient(s) with BMI < 22."
    else:
        expl = "No migraine patient has BMI < 22."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All patients with a diastolic blood pressure less than 90 have a systolic blood pressure less than 130."""
    low_diast = df[df["bp_diastolic"] < 90]
    condition = low_diast["bp_systolic"] < 130
    truth = condition.all()
    if truth:
        expl = f"All {len(low_diast)} patients with diastolic < 90 have systolic < 130."
    else:
        viol = low_diast[~condition]
        expl = f"{len(viol)} patients violate the rule (systolic: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a patient has a cholesterol level greater than 220 mg/dl, then they are a smoker."""
    high_chol = df[df["cholesterol_mg_dl"] > 220]
    condition = high_chol["smoker"]
    truth = condition.all()
    if truth:
        expl = f"All {len(high_chol)} patients with cholesterol > 220 mg/dl are smokers."
    else:
        viol = high_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol > 220 mg/dl are not smokers (IDs: {', '.join(viol['patient_id'].tolist())})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most patients have a BMI less than 30."""
    total = len(df)
    count = df[df["bmi"] < 30].shape[0]
    truth = count > total / 2
    percent = count / total * 100
    if truth:
        expl = f"{count} out of {total} patients ({percent:.1f}%) have BMI < 30."
    else:
        expl = f"Only {count} out of {total} patients ({percent:.1f}%) have BMI < 30."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All patients with a diagnosis of hypertension have a systolic blood pressure greater than 140."""
    hypo = df[df["diagnosis"] == "hypertension"]
    condition = hypo["bp_systolic"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(hypo)} hypertension patients have systolic > 140."
    else:
        viol = hypo[~condition]
        expl = f"{len(viol)} hypertension patients violate the rule (systolic: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a patient is younger than 40, then their diastolic blood pressure is greater than 80."""
    young = df[df["age"] < 40]
    condition = young["bp_diastolic"] > 80
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} patients younger than 40 have diastolic > 80."
    else:
        viol = young[~condition]
        expl = f"{len(viol)} patients younger than 40 violate the rule (diastolic: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one patient with a diagnosis of arthritis whose cholesterol level is greater than 230 mg/dl."""
    exists = df[(df["diagnosis"] == "arthritis") & (df["cholesterol_mg_dl"] > 230)].any(axis=1).any()
    truth = exists
    if truth:
        count = df[(df["diagnosis"] == "arthritis") & (df["cholesterol_mg_dl"] > 230)].shape[0]
        expl = f"Found {count} arthritis patient(s) with cholesterol > 230 mg/dl."
    else:
        expl = "No arthritis patient has cholesterol > 230 mg/dl."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All patients with a BMI greater than 25 have a systolic blood pressure greater than 110."""
    high_bmi = df[df["bmi"] > 25]
    condition = high_bmi["bp_systolic"] > 110
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 25 have systolic > 110."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 25 violate the rule (systolic: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a patient has a cholesterol level less than 190 mg/dl, then they are not a smoker."""
    low_chol = df[df["cholesterol_mg_dl"] < 190]
    condition = ~low_chol["smoker"]
    truth = condition.all()
    if truth:
        expl = f"All {len(low_chol)} patients with cholesterol < 190 mg/dl are not smokers."
    else:
        viol = low_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol < 190 mg/dl are smokers (IDs: {', '.join(viol['patient_id'].tolist())})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most patients have a systolic blood pressure greater than 120."""
    total = len(df)
    count = df[df["bp_systolic"] > 120].shape[0]
    truth = count > total / 2
    percent = count / total * 100
    if truth:
        expl = f"{count} out of {total} patients ({percent:.1f}%) have systolic > 120."
    else:
        expl = f"Only {count} out of {total} patients ({percent:.1f}%) have systolic > 120."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All patients with a diagnosis of diabetes have a BMI greater than 25."""
    diag = df[df["diagnosis"] == "diabetes"]
    condition = diag["bmi"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(diag)} diabetes patients have BMI > 25."
    else:
        viol = diag[~condition]
        expl = f"{len(viol)} diabetes patients violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a patient is older than 60, then their BMI is less than 29."""
    older = df[df["age"] > 60]
    condition = older["bmi"] < 29
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} patients older than 60 have BMI < 29."
    else:
        viol = older[~condition]
        expl = f"{len(viol)} patients older than 60 violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one patient with a diagnosis of migraine whose systolic blood pressure is greater than 145."""
    exists = df[(df["diagnosis"] == "migraine") & (df["bp_systolic"] > 145)].any(axis=1).any()
    truth = exists
    if truth:
        count = df[(df["diagnosis"] == "migraine") & (df["bp_systolic"] > 145)].shape[0]
        expl = f"Found {count} migraine patient(s) with systolic > 145."
    else:
        expl = "No migraine patient has systolic > 145."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. All patients with a diastolic blood pressure greater than 95 have a systolic blood pressure greater than 125."""
    high_diast = df[df["bp_diastolic"] > 95]
    condition = high_diast["bp_systolic"] > 125
    truth = condition.all()
    if truth:
        expl = f"All {len(high_diast)} patients with diastolic > 95 have systolic > 125."
    else:
        viol = high_diast[~condition]
        expl = f"{len(viol)} patients violate the rule (systolic: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_81.csv")

    # Convert numeric columns
    numeric_cols = ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert smoker to boolean
    df["smoker"] = df["smoker"].map({"yes": True, "no": False})

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
        (22, stmt_22),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()