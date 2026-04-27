import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of asthma have a BMI less than 33."""
    asthma = df[df["diagnosis"] == "asthma"]
    if asthma.empty:
        return True, "No asthma patients to evaluate."
    condition = asthma["bmi"] < 33
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients have BMI < 33."
    else:
        viol = asthma[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their cholesterol level is greater than 200 mg/dl."""
    smokers = df[df["smoker"] == True]
    if smokers.empty:
        return True, "No smokers to evaluate."
    condition = smokers["cholesterol_mg_dl"] > 200
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have cholesterol > 200 mg/dl."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of diabetes who is less than 25 years old."""
    exists = ((df["diagnosis"] == "diabetes") & (df["age"] < 25)).any()
    if exists:
        expl = "At least one diabetes patient is under 25 years old."
    else:
        expl = "No diabetes patient under 25 years old found."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All patients with a diagnosis of arthritis have a systolic blood pressure less than 160."""
    arth = df[df["diagnosis"] == "arthritis"]
    if arth.empty:
        return True, "No arthritis patients to evaluate."
    condition = arth["bp_systolic"] < 160
    truth = condition.all()
    if truth:
        expl = f"All {len(arth)} arthritis patients have systolic BP < 160."
    else:
        viol = arth[~condition]
        expl = f"{len(viol)} arthritis patients violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient's BMI is greater than 30, then they are a smoker."""
    high_bmi = df[df["bmi"] > 30]
    if high_bmi.empty:
        return True, "No patients with BMI > 30 to evaluate."
    condition = high_bmi["smoker"] == True
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 are smokers."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 30 are not smokers."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most patients with a diagnosis of asthma have a diastolic blood pressure less than 90."""
    asthma = df[df["diagnosis"] == "asthma"]
    if asthma.empty:
        return True, "No asthma patients to evaluate."
    count = len(asthma)
    good = (asthma["bp_diastolic"] < 90).sum()
    proportion = good / count
    truth = proportion > 0.5
    if truth:
        expl = f"{good}/{count} asthma patients have diastolic BP < 90 ({proportion:.2f} > 0.5)."
    else:
        expl = f"{good}/{count} asthma patients have diastolic BP < 90 ({proportion:.2f} <= 0.5)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All patients with a systolic blood pressure greater than 150 have a diagnosis of either hypertension or asthma."""
    high_syst = df[df["bp_systolic"] > 150]
    if high_syst.empty:
        return True, "No patients with systolic BP > 150 to evaluate."
    condition = high_syst["diagnosis"].isin(["hypertension", "asthma"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_syst)} patients with systolic BP > 150 have diagnosis hypertension or asthma."
    else:
        viol = high_syst[~condition]
        expl = f"{len(viol)} patients with systolic BP > 150 have diagnosis {', '.join(viol['diagnosis'].unique())}."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is less than 40 years old, then their BMI is less than 28."""
    young = df[df["age"] < 40]
    if young.empty:
        return True, "No patients under 40 to evaluate."
    condition = young["bmi"] < 28
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} patients under 40 have BMI < 28."
    else:
        viol = young[~condition]
        expl = f"{len(viol)} patients under 40 have BMI >= 28."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one patient with a diagnosis of migraine who is less than 45 years old and has a BMI greater than 30."""
    exists = ((df["diagnosis"] == "migraine") & (df["age"] < 45) & (df["bmi"] > 30)).any()
    if exists:
        expl = "At least one migraine patient is under 45 and has BMI > 30."
    else:
        expl = "No migraine patient under 45 with BMI > 30 found."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All patients with a cholesterol level greater than 220 mg/dl have a diagnosis of either diabetes or arthritis."""
    high_chol = df[df["cholesterol_mg_dl"] > 220]
    if high_chol.empty:
        return True, "No patients with cholesterol > 220 to evaluate."
    condition = high_chol["diagnosis"].isin(["diabetes", "arthritis"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_chol)} patients with cholesterol > 220 have diagnosis diabetes or arthritis."
    else:
        viol = high_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol > 220 have diagnosis {', '.join(viol['diagnosis'].unique())}."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a patient's diastolic blood pressure is less than 80, then their age is less than 60."""
    low_diast = df[df["bp_diastolic"] < 80]
    if low_diast.empty:
        return True, "No patients with diastolic BP < 80 to evaluate."
    condition = low_diast["age"] < 60
    truth = condition.all()
    if truth:
        expl = f"All {len(low_diast)} patients with diastolic BP < 80 are under 60."
    else:
        viol = low_diast[~condition]
        expl = f"{len(viol)} patients with diastolic BP < 80 are 60 or older."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most patients with a diagnosis of diabetes have a BMI greater than 25."""
    diab = df[df["diagnosis"] == "diabetes"]
    if diab.empty:
        return True, "No diabetes patients to evaluate."
    count = len(diab)
    good = (diab["bmi"] > 25).sum()
    proportion = good / count
    truth = proportion > 0.5
    if truth:
        expl = f"{good}/{count} diabetes patients have BMI > 25 ({proportion:.2f} > 0.5)."
    else:
        expl = f"{good}/{count} diabetes patients have BMI > 25 ({proportion:.2f} <= 0.5)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All patients with a BMI less than 22 have a diagnosis of either asthma or arthritis."""
    low_bmi = df[df["bmi"] < 22]
    if low_bmi.empty:
        return True, "No patients with BMI < 22 to evaluate."
    condition = low_bmi["diagnosis"].isin(["asthma", "arthritis"])
    truth = condition.all()
    if truth:
        expl = f"All {len(low_bmi)} patients with BMI < 22 have diagnosis asthma or arthritis."
    else:
        viol = low_bmi[~condition]
        expl = f"{len(viol)} patients with BMI < 22 have diagnosis {', '.join(viol['diagnosis'].unique())}."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a patient is a smoker and has a BMI greater than 25, then their systolic blood pressure is greater than 140."""
    cond = (df["smoker"] == True) & (df["bmi"] > 25)
    subset = df[cond]
    if subset.empty:
        return True, "No patients who are smokers with BMI > 25 to evaluate."
    condition = subset["bp_systolic"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} smokers with BMI > 25 have systolic BP > 140."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} smokers with BMI > 25 have systolic BP <= 140."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one patient with a diagnosis of asthma who is less than 25 years old and has a BMI greater than 22."""
    exists = ((df["diagnosis"] == "asthma") & (df["age"] < 25) & (df["bmi"] > 22)).any()
    if exists:
        expl = "At least one asthma patient is under 25 and has BMI > 22."
    else:
        expl = "No asthma patient under 25 with BMI > 22 found."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. All patients with a systolic blood pressure less than 120 have a diagnosis of either arthritis or migraine."""
    low_syst = df[df["bp_systolic"] < 120]
    if low_syst.empty:
        return True, "No patients with systolic BP < 120 to evaluate."
    condition = low_syst["diagnosis"].isin(["arthritis", "migraine"])
    truth = condition.all()
    if truth:
        expl = f"All {len(low_syst)} patients with systolic BP < 120 have diagnosis arthritis or migraine."
    else:
        viol = low_syst[~condition]
        expl = f"{len(viol)} patients with systolic BP < 120 have diagnosis {', '.join(viol['diagnosis'].unique())}."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a patient's cholesterol level is less than 200 mg/dl, then their age is less than 50."""
    low_chol = df[df["cholesterol_mg_dl"] < 200]
    if low_chol.empty:
        return True, "No patients with cholesterol < 200 to evaluate."
    condition = low_chol["age"] < 50
    truth = condition.all()
    if truth:
        expl = f"All {len(low_chol)} patients with cholesterol < 200 are under 50."
    else:
        viol = low_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol < 200 are 50 or older."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most patients with a diagnosis of arthritis have a BMI less than 27."""
    arth = df[df["diagnosis"] == "arthritis"]
    if arth.empty:
        return True, "No arthritis patients to evaluate."
    count = len(arth)
    good = (arth["bmi"] < 27).sum()
    proportion = good / count
    truth = proportion > 0.5
    if truth:
        expl = f"{good}/{count} arthritis patients have BMI < 27 ({proportion:.2f} > 0.5)."
    else:
        expl = f"{good}/{count} arthritis patients have BMI < 27 ({proportion:.2f} <= 0.5)."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All patients with a BMI greater than 28 have a diagnosis of either diabetes or hypertension."""
    high_bmi = df[df["bmi"] > 28]
    if high_bmi.empty:
        return True, "No patients with BMI > 28 to evaluate."
    condition = high_bmi["diagnosis"].isin(["diabetes", "hypertension"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 28 have diagnosis diabetes or hypertension."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 28 have diagnosis {', '.join(viol['diagnosis'].unique())}."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a patient is less than 30 years old, then their diastolic blood pressure is less than 85."""
    young = df[df["age"] < 30]
    if young.empty:
        return True, "No patients under 30 to evaluate."
    condition = young["bp_diastolic"] < 85
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} patients under 30 have diastolic BP < 85."
    else:
        viol = young[~condition]
        expl = f"{len(viol)} patients under 30 have diastolic BP >= 85."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one patient with a diagnosis of migraine who is less than 50 years old and has a BMI less than 25."""
    exists = ((df["diagnosis"] == "migraine") & (df["age"] < 50) & (df["bmi"] < 25)).any()
    if exists:
        expl = "At least one migraine patient is under 50 and has BMI < 25."
    else:
        expl = "No migraine patient under 50 with BMI < 25 found."
    return exists, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_31.csv")

    # Convert numeric columns
    numeric_cols = ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert smoker to boolean
    df["smoker"] = df["smoker"].map({"yes": True, "no": False})

    checks = [
        (1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5),
        (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10),
        (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15),
        (16, stmt_16), (17, stmt_17), (18, stmt_18), (19, stmt_19), (20, stmt_20), (21, stmt_21)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()