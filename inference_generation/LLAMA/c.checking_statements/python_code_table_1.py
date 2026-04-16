import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with hypertension have a bmi greater than 28."""
    hypertensive = df[df["diagnosis"] == "hypertension"]
    condition = hypertensive["bmi"] > 28
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertensive)} hypertensive patients have a bmi greater than 28."
    else:
        viol = hypertensive[~condition]
        expl = f"{len(viol)} hypertensive patients violate the rule (bmi: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their cholesterol_mg_dl is greater than 200."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["cholesterol_mg_dl"] > 200
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have a cholesterol_mg_dl greater than 200."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (cholesterol_mg_dl: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every patient with diabetes has a bp_systolic greater than 130."""
    diabetic = df[df["diagnosis"] == "diabetes"]
    condition = diabetic["bp_systolic"] > 130
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetic)} diabetic patients have a bp_systolic greater than 130."
    else:
        viol = diabetic[~condition]
        expl = f"{len(viol)} diabetic patients violate the rule (bp_systolic: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Patients with asthma have a lower bmi compared to patients with arthritis."""
    asthmatic = df[df["diagnosis"] == "asthma"]
    arthritic = df[df["diagnosis"] == "arthritis"]
    condition = asthmatic["bmi"].mean() < arthritic["bmi"].mean()
    truth = condition
    if truth:
        expl = f"Asthamtic patients have a lower bmi ({asthmatic['bmi'].mean():.2f}) compared to arthritic patients ({arthritic['bmi'].mean():.2f})."
    else:
        expl = f"Asthamtic patients do not have a lower bmi ({asthmatic['bmi'].mean():.2f}) compared to arthritic patients ({arthritic['bmi'].mean():.2f})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All patients with migraine have a bp_diastolic less than 80, unless they are also smokers."""
    migrainous = df[df["diagnosis"] == "migraine"]
    non_smoker_migrainous = migrainous[migrainous["smoker"] == "no"]
    condition = non_smoker_migrainous["bp_diastolic"] < 80
    truth = condition.all()
    if truth:
        expl = f"All non-smoker migrainous patients have a bp_diastolic less than 80."
    else:
        viol = non_smoker_migrainous[~condition]
        expl = f"{len(viol)} non-smoker migrainous patients violate the rule (bp_diastolic: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a patient has a bmi greater than 30, then they are more likely to have hypertension or diabetes."""
    high_bmi = df[df["bmi"] > 30]
    condition = high_bmi["diagnosis"].isin(["hypertension", "diabetes"]).mean() > 0.5
    truth = condition
    if truth:
        expl = f"Patients with a bmi greater than 30 are more likely to have hypertension or diabetes ({condition:.2f})."
    else:
        expl = f"Patients with a bmi greater than 30 are not more likely to have hypertension or diabetes ({condition:.2f})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Patients with hypertension have a higher bp_systolic compared to patients with diabetes."""
    hypertensive = df[df["diagnosis"] == "hypertension"]
    diabetic = df[df["diagnosis"] == "diabetes"]
    condition = hypertensive["bp_systolic"].mean() > diabetic["bp_systolic"].mean()
    truth = condition
    if truth:
        expl = f"Hypertensive patients have a higher bp_systolic ({hypertensive['bp_systolic'].mean():.2f}) compared to diabetic patients ({diabetic['bp_systolic'].mean():.2f})."
    else:
        expl = f"Hypertensive patients do not have a higher bp_systolic ({hypertensive['bp_systolic'].mean():.2f}) compared to diabetic patients ({diabetic['bp_systolic'].mean():.2f})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All patients with arthritis have a cholesterol_mg_dl greater than 210."""
    arthritic = df[df["diagnosis"] == "arthritis"]
    condition = arthritic["cholesterol_mg_dl"] > 210
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritic)} arthritic patients have a cholesterol_mg_dl greater than 210."
    else:
        viol = arthritic[~condition]
        expl = f"{len(viol)} arthritic patients violate the rule (cholesterol_mg_dl: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a patient is a smoker and has hypertension, then their bp_systolic is greater than 140."""
    smoker_hypertensive = df[(df["smoker"] == "yes") & (df["diagnosis"] == "hypertension")]
    condition = smoker_hypertensive["bp_systolic"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(smoker_hypertensive)} smoker hypertensive patients have a bp_systolic greater than 140."
    else:
        viol = smoker_hypertensive[~condition]
        expl = f"{len(viol)} smoker hypertensive patients violate the rule (bp_systolic: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Patients with asthma have a lower age compared to patients with arthritis."""
    asthmatic = df[df["diagnosis"] == "asthma"]
    arthritic = df[df["diagnosis"] == "arthritis"]
    condition = asthmatic["age"].mean() < arthritic["age"].mean()
    truth = condition
    if truth:
        expl = f"Asthamtic patients have a lower age ({asthmatic['age'].mean():.2f}) compared to arthritic patients ({arthritic['age'].mean():.2f})."
    else:
        expl = f"Asthamtic patients do not have a lower age ({asthmatic['age'].mean():.2f}) compared to arthritic patients ({arthritic['age'].mean():.2f})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Every patient with a bmi greater than 32 has diabetes or hypertension."""
    high_bmi = df[df["bmi"] > 32]
    condition = high_bmi["diagnosis"].isin(["diabetes", "hypertension"]).all()
    truth = condition
    if truth:
        expl = f"All {len(high_bmi)} patients with a bmi greater than 32 have diabetes or hypertension."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with a bmi greater than 32 violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a patient has a cholesterol_mg_dl greater than 220, then they are more likely to have hypertension or diabetes."""
    high_cholesterol = df[df["cholesterol_mg_dl"] > 220]
    condition = high_cholesterol["diagnosis"].isin(["hypertension", "diabetes"]).mean() > 0.5
    truth = condition
    if truth:
        expl = f"Patients with a cholesterol_mg_dl greater than 220 are more likely to have hypertension or diabetes ({condition:.2f})."
    else:
        expl = f"Patients with a cholesterol_mg_dl greater than 220 are not more likely to have hypertension or diabetes ({condition:.2f})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Patients with migraine have a lower bp_systolic compared to patients with hypertension."""
    migrainous = df[df["diagnosis"] == "migraine"]
    hypertensive = df[df["diagnosis"] == "hypertension"]
    condition = migrainous["bp_systolic"].mean() < hypertensive["bp_systolic"].mean()
    truth = condition
    if truth:
        expl = f"Migrainous patients have a lower bp_systolic ({migrainous['bp_systolic'].mean():.2f}) compared to hypertensive patients ({hypertensive['bp_systolic'].mean():.2f})."
    else:
        expl = f"Migrainous patients do not have a lower bp_systolic ({migrainous['bp_systolic'].mean():.2f}) compared to hypertensive patients ({hypertensive['bp_systolic'].mean():.2f})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All patients with a bp_diastolic greater than 90 have hypertension."""
    high_diastolic = df[df["bp_diastolic"] > 90]
    condition = high_diastolic["diagnosis"] == "hypertension"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_diastolic)} patients with a bp_diastolic greater than 90 have hypertension."
    else:
        viol = high_diastolic[~condition]
        expl = f"{len(viol)} patients with a bp_diastolic greater than 90 violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a patient has a bmi greater than 28 and is a smoker, then they are more likely to have hypertension."""
    high_bmi_smoker = df[(df["bmi"] > 28) & (df["smoker"] == "yes")]
    condition = high_bmi_smoker["diagnosis"] == "hypertension"
    truth = condition.mean() > 0.5
    if truth:
        expl = f"Patients with a bmi greater than 28 and are smokers are more likely to have hypertension ({condition.mean():.2f})."
    else:
        expl = f"Patients with a bmi greater than 28 and are smokers are not more likely to have hypertension ({condition.mean():.2f})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_1.csv")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["bp_systolic"] = pd.to_numeric(df["bp_systolic"], errors="coerce")
    df["bp_diastolic"] = pd.to_numeric(df["bp_diastolic"], errors="coerce")
    df["cholesterol_mg_dl"] = pd.to_numeric(df["cholesterol_mg_dl"], errors="coerce")
    df["bmi"] = pd.to_numeric(df["bmi"], errors="coerce")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10), (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()