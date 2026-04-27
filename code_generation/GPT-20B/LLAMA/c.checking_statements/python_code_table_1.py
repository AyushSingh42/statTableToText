import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of diabetes have a cholesterol level greater than 190 mg/dl."""
    diag = df[df["diagnosis"] == "diabetes"]
    if diag.empty:
        return True, "No diabetes patients to evaluate."
    condition = diag["cholesterol_mg_dl"] > 190
    truth = condition.all()
    if truth:
        return True, f"All {len(diag)} diabetes patients have cholesterol >190."
    else:
        viol = diag[~condition]
        return False, f"{len(viol)} diabetes patients violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is less than 70 years."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        return True, "No smokers to evaluate."
    condition = smokers["age"] < 70
    truth = condition.all()
    if truth:
        return True, f"All {len(smokers)} smokers are younger than 70."
    else:
        viol = smokers[~condition]
        return False, f"{len(viol)} smokers are 70 or older (ages: {', '.join(map(str, viol['age'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of arthritis whose BMI is less than 28."""
    exists = df[(df["diagnosis"] == "arthritis") & (df["bmi"] < 28)].any(axis=1).any()
    if exists:
        return True, "At least one arthritis patient with BMI <28 exists."
    else:
        return False, "No arthritis patient with BMI <28 found."

def stmt_4(df: pd.DataFrame):
    """4. All patients with a BMI greater than 33 have a diagnosis of either asthma or arthritis."""
    high_bmi = df[df["bmi"] > 33]
    if high_bmi.empty:
        return True, "No patients with BMI >33 to evaluate."
    condition = high_bmi["diagnosis"].isin(["asthma", "arthritis"])
    truth = condition.all()
    if truth:
        return True, f"All {len(high_bmi)} patients with BMI >33 have diagnosis asthma or arthritis."
    else:
        viol = high_bmi[~condition]
        return False, f"{len(viol)} patients with BMI >33 have diagnosis {', '.join(viol['diagnosis'].unique())}."

def stmt_5(df: pd.DataFrame):
    """5. If a patient has a systolic blood pressure greater than 140, then their diagnosis is either diabetes or hypertension."""
    high_sys = df[df["bp_systolic"] > 140]
    if high_sys.empty:
        return True, "No patients with systolic BP >140 to evaluate."
    condition = high_sys["diagnosis"].isin(["diabetes", "hypertension"])
    truth = condition.all()
    if truth:
        return True, f"All {len(high_sys)} patients with systolic BP >140 have diagnosis diabetes or hypertension."
    else:
        viol = high_sys[~condition]
        return False, f"{len(viol)} patients with systolic BP >140 have diagnosis {', '.join(viol['diagnosis'].unique())}."

def stmt_6(df: pd.DataFrame):
    """6. Most patients with a diagnosis of arthritis have a diastolic blood pressure less than 85."""
    arthritis = df[df["diagnosis"] == "arthritis"]
    if arthritis.empty:
        return True, "No arthritis patients to evaluate."
    proportion = (arthritis["bp_diastolic"] < 85).mean()
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% of arthritis patients have diastolic BP <85."
    else:
        return False, f"Only {proportion*100:.1f}% of arthritis patients have diastolic BP <85."

def stmt_7(df: pd.DataFrame):
    """7. All patients with a cholesterol level greater than 230 mg/dl have a diagnosis of either diabetes or migraine."""
    high_chol = df[df["cholesterol_mg_dl"] > 230]
    if high_chol.empty:
        return True, "No patients with cholesterol >230 to evaluate."
    condition = high_chol["diagnosis"].isin(["diabetes", "migraine"])
    truth = condition.all()
    if truth:
        return True, f"All {len(high_chol)} patients with cholesterol >230 have diagnosis diabetes or migraine."
    else:
        viol = high_chol[~condition]
        return False, f"{len(viol)} patients with cholesterol >230 have diagnosis {', '.join(viol['diagnosis'].unique())}."

def stmt_8(df: pd.DataFrame):
    """8. If a patient is a non-smoker, then their BMI is less than 34."""
    non_smokers = df[df["smoker"] == "no"]
    if non_smokers.empty:
        return True, "No non-smokers to evaluate."
    condition = non_smokers["bmi"] < 34
    truth = condition.all()
    if truth:
        return True, f"All {len(non_smokers)} non-smokers have BMI <34."
    else:
        viol = non_smokers[~condition]
        return False, f"{len(viol)} non-smokers have BMI >=34 (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one patient with a diagnosis of migraine whose systolic blood pressure is less than 125."""
    exists = df[(df["diagnosis"] == "migraine") & (df["bp_systolic"] < 125)].any(axis=1).any()
    if exists:
        return True, "At least one migraine patient with systolic BP <125 exists."
    else:
        return False, "No migraine patient with systolic BP <125 found."

def stmt_10(df: pd.DataFrame):
    """10. All patients with a BMI less than 27 have a diagnosis of either arthritis or diabetes."""
    low_bmi = df[df["bmi"] < 27]
    if low_bmi.empty:
        return True, "No patients with BMI <27 to evaluate."
    condition = low_bmi["diagnosis"].isin(["arthritis", "diabetes"])
    truth = condition.all()
    if truth:
        return True, f"All {len(low_bmi)} patients with BMI <27 have diagnosis arthritis or diabetes."
    else:
        viol = low_bmi[~condition]
        return False, f"{len(viol)} patients with BMI <27 have diagnosis {', '.join(viol['diagnosis'].unique())}."

def stmt_11(df: pd.DataFrame):
    """11. If a patient has a diastolic blood pressure greater than 90, then their age is less than 75 years."""
    high_diast = df[df["bp_diastolic"] > 90]
    if high_diast.empty:
        return True, "No patients with diastolic BP >90 to evaluate."
    condition = high_diast["age"] < 75
    truth = condition.all()
    if truth:
        return True, f"All {len(high_diast)} patients with diastolic BP >90 are younger than 75."
    else:
        viol = high_diast[~condition]
        return False, f"{len(viol)} patients with diastolic BP >90 are 75 or older (ages: {', '.join(map(str, viol['age'].tolist()))})."

def stmt_12(df: pd.DataFrame):
    """12. Most patients with a diagnosis of diabetes have a BMI greater than 25."""
    diabetes = df[df["diagnosis"] == "diabetes"]
    if diabetes.empty:
        return True, "No diabetes patients to evaluate."
    proportion = (diabetes["bmi"] > 25).mean()
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% of diabetes patients have BMI >25."
    else:
        return False, f"Only {proportion*100:.1f}% of diabetes patients have BMI >25."

def stmt_13(df: pd.DataFrame):
    """13. All patients with a systolic blood pressure less than 130 have a diagnosis of either arthritis or migraine."""
    low_sys = df[df["bp_systolic"] < 130]
    if low_sys.empty:
        return True, "No patients with systolic BP <130 to evaluate."
    condition = low_sys["diagnosis"].isin(["arthritis", "migraine"])
    truth = condition.all()
    if truth:
        return True, f"All {len(low_sys)} patients with systolic BP <130 have diagnosis arthritis or migraine."
    else:
        viol = low_sys[~condition]
        return False, f"{len(viol)} patients with systolic BP <130 have diagnosis {', '.join(viol['diagnosis'].unique())}."

def stmt_14(df: pd.DataFrame):
    """14. If a patient has a cholesterol level less than 200 mg/dl, then their BMI is less than 32."""
    low_chol = df[df["cholesterol_mg_dl"] < 200]
    if low_chol.empty:
        return True, "No patients with cholesterol <200 to evaluate."
    condition = low_chol["bmi"] < 32
    truth = condition.all()
    if truth:
        return True, f"All {len(low_chol)} patients with cholesterol <200 have BMI <32."
    else:
        viol = low_chol[~condition]
        return False, f"{len(viol)} patients with cholesterol <200 have BMI >=32 (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one patient with a diagnosis of asthma whose BMI is greater than 33."""
    exists = df[(df["diagnosis"] == "asthma") & (df["bmi"] > 33)].any(axis=1).any()
    if exists:
        return True, "At least one asthma patient with BMI >33 exists."
    else:
        return False, "No asthma patient with BMI >33 found."

def stmt_16(df: pd.DataFrame):
    """16. All patients with a BMI greater than 32 have a diagnosis of either arthritis or diabetes."""
    high_bmi = df[df["bmi"] > 32]
    if high_bmi.empty:
        return True, "No patients with BMI >32 to evaluate."
    condition = high_bmi["diagnosis"].isin(["arthritis", "diabetes"])
    truth = condition.all()
    if truth:
        return True, f"All {len(high_bmi)} patients with BMI >32 have diagnosis arthritis or diabetes."
    else:
        viol = high_bmi[~condition]
        return False, f"{len(viol)} patients with BMI >32 have diagnosis {', '.join(viol['diagnosis'].unique())}."

def stmt_17(df: pd.DataFrame):
    """17. If a patient is a smoker, then their cholesterol level is greater than 220 mg/dl."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        return True, "No smokers to evaluate."
    condition = smokers["cholesterol_mg_dl"] > 220
    truth = condition.all()
    if truth:
        return True, f"All {len(smokers)} smokers have cholesterol >220."
    else:
        viol = smokers[~condition]
        return False, f"{len(viol)} smokers have cholesterol <=220 (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."

def stmt_18(df: pd.DataFrame):
    """18. Most patients with a diagnosis of arthritis have a systolic blood pressure less than 140."""
    arthritis = df[df["diagnosis"] == "arthritis"]
    if arthritis.empty:
        return True, "No arthritis patients to evaluate."
    proportion = (arthritis["bp_systolic"] < 140).mean()
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% of arthritis patients have systolic BP <140."
    else:
        return False, f"Only {proportion*100:.1f}% of arthritis patients have systolic BP <140."

def stmt_19(df: pd.DataFrame):
    """19. All patients with a diastolic blood pressure less than 80 have a diagnosis of either hypertension or migraine."""
    low_diast = df[df["bp_diastolic"] < 80]
    if low_diast.empty:
        return True, "No patients with diastolic BP <80 to evaluate."
    condition = low_diast["diagnosis"].isin(["hypertension", "migraine"])
    truth = condition.all()
    if truth:
        return True, f"All {len(low_diast)} patients with diastolic BP <80 have diagnosis hypertension or migraine."
    else:
        viol = low_diast[~condition]
        return False, f"{len(viol)} patients with diastolic BP <80 have diagnosis {', '.join(viol['diagnosis'].unique())}."

def main():
    df = pd.read_csv("../inference_generation/tables/table_1.csv")

    # Standardize text columns
    df["smoker"] = df["smoker"].str.lower()
    df["diagnosis"] = df["diagnosis"].str.lower()

    # Convert numeric columns
    numeric_cols = ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()