import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of arthritis have a cholesterol level greater than 215 mg/dl."""
    arth = df[df["diagnosis"] == "arthritis"]
    if arth.empty:
        return True, "No arthritis patients to evaluate."
    condition = arth["cholesterol_mg_dl"] > 215
    truth = condition.all()
    if truth:
        return True, f"All {len(arth)} arthritis patients have cholesterol > 215."
    viol = arth[~condition]
    return False, f"{len(viol)} arthritis patient(s) violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl']))})."

def stmt_2(df: pd.DataFrame):
    """2. All patients with a diagnosis of asthma have a BMI less than 34."""
    ast = df[df["diagnosis"] == "asthma"]
    if ast.empty:
        return True, "No asthma patients to evaluate."
    condition = ast["bmi"] < 34
    truth = condition.all()
    if truth:
        return True, f"All {len(ast)} asthma patients have BMI < 34."
    viol = ast[~condition]
    return False, f"{len(viol)} asthma patient(s) violate the rule (BMI: {', '.join(map(str, viol['bmi']))})."

def stmt_3(df: pd.DataFrame):
    """3. If a patient is a smoker, then their age is greater than 35."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        return True, "No smokers to evaluate."
    condition = smokers["age"] > 35
    truth = condition.all()
    if truth:
        return True, f"All {len(smokers)} smokers are older than 35."
    viol = smokers[~condition]
    return False, f"{len(viol)} smoker(s) violate the rule (age: {', '.join(map(str, viol['age']))})."

def stmt_4(df: pd.DataFrame):
    """4. All patients with a systolic blood pressure greater than 150 have a diagnosis of migraine."""
    high_syst = df[df["bp_systolic"] > 150]
    if high_syst.empty:
        return True, "No patients with systolic BP > 150 to evaluate."
    condition = high_syst["diagnosis"] == "migraine"
    truth = condition.all()
    if truth:
        return True, f"All {len(high_syst)} patients with systolic BP > 150 have diagnosis migraine."
    viol = high_syst[~condition]
    return False, f"{len(viol)} patient(s) violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis']))})."

def stmt_5(df: pd.DataFrame):
    """5. There exists at least one patient with a diagnosis of hypertension who is a smoker."""
    exists = df[(df["diagnosis"] == "hypertension") & (df["smoker"] == "yes")].any(axis=1).any()
    if exists:
        return True, "At least one hypertension patient is a smoker."
    return False, "No hypertension patient is a smoker."

def stmt_6(df: pd.DataFrame):
    """6. All patients with a BMI greater than 30 have a diagnosis of either arthritis or hypertension."""
    high_bmi = df[df["bmi"] > 30]
    if high_bmi.empty:
        return True, "No patients with BMI > 30 to evaluate."
    condition = high_bmi["diagnosis"].isin(["arthritis", "hypertension"])
    truth = condition.all()
    if truth:
        return True, f"All {len(high_bmi)} patients with BMI > 30 have diagnosis arthritis or hypertension."
    viol = high_bmi[~condition]
    return False, f"{len(viol)} patient(s) violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis']))})."

def stmt_7(df: pd.DataFrame):
    """7. If a patient has a diastolic blood pressure less than 80, then their age is less than 40."""
    low_diast = df[df["bp_diastolic"] < 80]
    if low_diast.empty:
        return True, "No patients with diastolic BP < 80 to evaluate."
    condition = low_diast["age"] < 40
    truth = condition.all()
    if truth:
        return True, f"All {len(low_diast)} patients with diastolic BP < 80 are younger than 40."
    viol = low_diast[~condition]
    return False, f"{len(viol)} patient(s) violate the rule (age: {', '.join(map(str, viol['age']))})."

def stmt_8(df: pd.DataFrame):
    """8. All patients with a cholesterol level greater than 230 mg/dl have a BMI greater than 25."""
    high_chol = df[df["cholesterol_mg_dl"] > 230]
    if high_chol.empty:
        return True, "No patients with cholesterol > 230 to evaluate."
    condition = high_chol["bmi"] > 25
    truth = condition.all()
    if truth:
        return True, f"All {len(high_chol)} patients with cholesterol > 230 have BMI > 25."
    viol = high_chol[~condition]
    return False, f"{len(viol)} patient(s) violate the rule (BMI: {', '.join(map(str, viol['bmi']))})."

def stmt_9(df: pd.DataFrame):
    """9. Most patients with a diagnosis of hypertension have a systolic blood pressure greater than 125."""
    hypos = df[df["diagnosis"] == "hypertension"]
    if hypos.empty:
        return True, "No hypertension patients to evaluate."
    count_gt = (hypos["bp_systolic"] > 125).sum()
    total = len(hypos)
    proportion = count_gt / total
    truth = proportion > 0.5
    if truth:
        return True, f"{count_gt} out of {total} hypertension patients have systolic BP > 125 ({proportion*100:.1f}%)."
    return False, f"{count_gt} out of {total} hypertension patients have systolic BP > 125 ({proportion*100:.1f}%)."

def stmt_10(df: pd.DataFrame):
    """10. All patients with a BMI less than 25 have a diagnosis of either asthma or migraine."""
    low_bmi = df[df["bmi"] < 25]
    if low_bmi.empty:
        return True, "No patients with BMI < 25 to evaluate."
    condition = low_bmi["diagnosis"].isin(["asthma", "migraine"])
    truth = condition.all()
    if truth:
        return True, f"All {len(low_bmi)} patients with BMI < 25 have diagnosis asthma or migraine."
    viol = low_bmi[~condition]
    return False, f"{len(viol)} patient(s) violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis']))})."

def stmt_11(df: pd.DataFrame):
    """11. If a patient is older than 60, then their diagnosis is either hypertension or asthma."""
    old = df[df["age"] > 60]
    if old.empty:
        return True, "No patients older than 60 to evaluate."
    condition = old["diagnosis"].isin(["hypertension", "asthma"])
    truth = condition.all()
    if truth:
        return True, f"All {len(old)} patients older than 60 have diagnosis hypertension or asthma."
    viol = old[~condition]
    return False, f"{len(viol)} patient(s) violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis']))})."

def stmt_12(df: pd.DataFrame):
    """12. All patients with a systolic blood pressure less than 130 have a diagnosis of either hypertension or migraine."""
    low_syst = df[df["bp_systolic"] < 130]
    if low_syst.empty:
        return True, "No patients with systolic BP < 130 to evaluate."
    condition = low_syst["diagnosis"].isin(["hypertension", "migraine"])
    truth = condition.all()
    if truth:
        return True, f"All {len(low_syst)} patients with systolic BP < 130 have diagnosis hypertension or migraine."
    viol = low_syst[~condition]
    return False, f"{len(viol)} patient(s) violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis']))})."

def stmt_13(df: pd.DataFrame):
    """13. There exists at least one patient with a diagnosis of arthritis who is a smoker."""
    exists = df[(df["diagnosis"] == "arthritis") & (df["smoker"] == "yes")].any(axis=1).any()
    if exists:
        return True, "At least one arthritis patient is a smoker."
    return False, "No arthritis patient is a smoker."

def stmt_14(df: pd.DataFrame):
    """14. All patients with a cholesterol level less than 200 mg/dl have a BMI less than 30."""
    low_chol = df[df["cholesterol_mg_dl"] < 200]
    if low_chol.empty:
        return True, "No patients with cholesterol < 200 to evaluate."
    condition = low_chol["bmi"] < 30
    truth = condition.all()
    if truth:
        return True, f"All {len(low_chol)} patients with cholesterol < 200 have BMI < 30."
    viol = low_chol[~condition]
    return False, f"{len(viol)} patient(s) violate the rule (BMI: {', '.join(map(str, viol['bmi']))})."

def stmt_15(df: pd.DataFrame):
    """15. If a patient has a BMI greater than 32, then their diagnosis is either arthritis or hypertension."""
    high_bmi = df[df["bmi"] > 32]
    if high_bmi.empty:
        return True, "No patients with BMI > 32 to evaluate."
    condition = high_bmi["diagnosis"].isin(["arthritis", "hypertension"])
    truth = condition.all()
    if truth:
        return True, f"All {len(high_bmi)} patients with BMI > 32 have diagnosis arthritis or hypertension."
    viol = high_bmi[~condition]
    return False, f"{len(viol)} patient(s) violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis']))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_11.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()