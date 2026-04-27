import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of diabetes have a cholesterol level greater than 200 mg/dl."""
    diag = df[df["diagnosis"] == "diabetes"]
    if diag.empty:
        return True, "No patients with diabetes, so statement vacuously true."
    condition = diag["cholesterol_mg_dl"] > 200
    truth = condition.all()
    if truth:
        return True, f"All {len(diag)} patients with diabetes have cholesterol > 200 mg/dl."
    viol = diag[~condition]
    return False, f"{len(viol)} patient(s) with diabetes violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl']))})."

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is less than 40 years."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        return True, "No smokers, so statement vacuously true."
    condition = smokers["age"] < 40
    truth = condition.all()
    if truth:
        return True, f"All {len(smokers)} smokers are younger than 40."
    viol = smokers[~condition]
    return False, f"{len(viol)} smoker(s) are 40 or older (ages: {', '.join(map(str, viol['age']))})."

def stmt_3(df: pd.DataFrame):
    """3. All patients with a BMI greater than 30 have a systolic blood pressure greater than 140 mmHg."""
    high_bmi = df[df["bmi"] > 30]
    if high_bmi.empty:
        return True, "No patients with BMI > 30, so statement vacuously true."
    condition = high_bmi["bp_systolic"] > 140
    truth = condition.all()
    if truth:
        return True, f"All {len(high_bmi)} patients with BMI > 30 have systolic BP > 140 mmHg."
    viol = high_bmi[~condition]
    return False, f"{len(viol)} patient(s) with BMI > 30 have systolic BP ≤ 140 mmHg (values: {', '.join(map(str, viol['bp_systolic']))})."

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one patient with a diagnosis of arthritis whose BMI is less than 25."""
    arthritis = df[(df["diagnosis"] == "arthritis") & (df["bmi"] < 25)]
    truth = not arthritis.empty
    if truth:
        return True, f"Found {len(arthritis)} arthritis patient(s) with BMI < 25."
    return False, "No arthritis patient with BMI < 25."

def stmt_5(df: pd.DataFrame):
    """5. If a patient has a diagnosis of hypertension, then their diastolic blood pressure is greater than 80 mmHg."""
    hypert = df[df["diagnosis"] == "hypertension"]
    if hypert.empty:
        return True, "No hypertension patients, so statement vacuously true."
    condition = hypert["bp_diastolic"] > 80
    truth = condition.all()
    if truth:
        return True, f"All {len(hypert)} hypertension patients have diastolic BP > 80 mmHg."
    viol = hypert[~condition]
    return False, f"{len(viol)} hypertension patient(s) have diastolic BP ≤ 80 mmHg (values: {', '.join(map(str, viol['bp_diastolic']))})."

def stmt_6(df: pd.DataFrame):
    """6. All patients with a cholesterol level greater than 220 mg/dl have a BMI greater than 25."""
    high_chol = df[df["cholesterol_mg_dl"] > 220]
    if high_chol.empty:
        return True, "No patients with cholesterol > 220 mg/dl, so statement vacuously true."
    condition = high_chol["bmi"] > 25
    truth = condition.all()
    if truth:
        return True, f"All {len(high_chol)} patients with cholesterol > 220 mg/dl have BMI > 25."
    viol = high_chol[~condition]
    return False, f"{len(viol)} patient(s) with cholesterol > 220 mg/dl have BMI ≤ 25 (values: {', '.join(map(str, viol['bmi']))})."

def stmt_7(df: pd.DataFrame):
    """7. Most patients in the table have a systolic blood pressure greater than 130 mmHg."""
    total = len(df)
    count = (df["bp_systolic"] > 130).sum()
    truth = count > total / 2
    percent = count / total * 100
    if truth:
        return True, f"{count} out of {total} patients have systolic BP > 130 mmHg ({percent:.1f}%)."
    return False, f"Only {count} out of {total} patients have systolic BP > 130 mmHg ({percent:.1f}%)."

def stmt_8(df: pd.DataFrame):
    """8. If a patient is a non-smoker, then their BMI is less than 30."""
    nonsmokers = df[df["smoker"] == "no"]
    if nonsmokers.empty:
        return True, "No non-smokers, so statement vacuously true."
    condition = nonsmokers["bmi"] < 30
    truth = condition.all()
    if truth:
        return True, f"All {len(nonsmokers)} non-smokers have BMI < 30."
    viol = nonsmokers[~condition]
    return False, f"{len(viol)} non-smoker(s) have BMI ≥ 30 (values: {', '.join(map(str, viol['bmi']))})."

def stmt_9(df: pd.DataFrame):
    """9. All patients with a diagnosis of migraine have a systolic blood pressure less than 150 mmHg."""
    migraine = df[df["diagnosis"] == "migraine"]
    if migraine.empty:
        return True, "No migraine patients, so statement vacuously true."
    condition = migraine["bp_systolic"] < 150
    truth = condition.all()
    if truth:
        return True, f"All {len(migraine)} migraine patients have systolic BP < 150 mmHg."
    viol = migraine[~condition]
    return False, f"{len(viol)} migraine patient(s) have systolic BP ≥ 150 mmHg (values: {', '.join(map(str, viol['bp_systolic']))})."

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one patient with a diagnosis of asthma whose BMI is less than 22."""
    asthma = df[(df["diagnosis"] == "asthma") & (df["bmi"] < 22)]
    truth = not asthma.empty
    if truth:
        return True, f"Found {len(asthma)} asthma patient(s) with BMI < 22."
    return False, "No asthma patient with BMI < 22."

def stmt_11(df: pd.DataFrame):
    """11. If a patient has a BMI between 25 and 30, then their age is greater than 30 years."""
    bmi_range = df[(df["bmi"] >= 25) & (df["bmi"] <= 30)]
    if bmi_range.empty:
        return True, "No patients with BMI between 25 and 30, so statement vacuously true."
    condition = bmi_range["age"] > 30
    truth = condition.all()
    if truth:
        return True, f"All {len(bmi_range)} patients with BMI 25-30 have age > 30."
    viol = bmi_range[~condition]
    return False, f"{len(viol)} patient(s) with BMI 25-30 have age ≤ 30 (ages: {', '.join(map(str, viol['age']))})."

def stmt_12(df: pd.DataFrame):
    """12. All patients with a diastolic blood pressure greater than 90 mmHg have a cholesterol level greater than 200 mg/dl."""
    high_diast = df[df["bp_diastolic"] > 90]
    if high_diast.empty:
        return True, "No patients with diastolic BP > 90 mmHg, so statement vacuously true."
    condition = high_diast["cholesterol_mg_dl"] > 200
    truth = condition.all()
    if truth:
        return True, f"All {len(high_diast)} patients with diastolic BP > 90 mmHg have cholesterol > 200 mg/dl."
    viol = high_diast[~condition]
    return False, f"{len(viol)} patient(s) with diastolic BP > 90 mmHg have cholesterol ≤ 200 mg/dl (values: {', '.join(map(str, viol['cholesterol_mg_dl']))})."

def stmt_13(df: pd.DataFrame):
    """13. Most patients in the table have a BMI greater than 25."""
    total = len(df)
    count = (df["bmi"] > 25).sum()
    truth = count > total / 2
    percent = count / total * 100
    if truth:
        return True, f"{count} out of {total} patients have BMI > 25 ({percent:.1f}%)."
    return False, f"Only {count} out of {total} patients have BMI > 25 ({percent:.1f}%)."

def stmt_14(df: pd.DataFrame):
    """14. If a patient is a smoker, then their cholesterol level is greater than 200 mg/dl."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        return True, "No smokers, so statement vacuously true."
    condition = smokers["cholesterol_mg_dl"] > 200
    truth = condition.all()
    if truth:
        return True, f"All {len(smokers)} smokers have cholesterol > 200 mg/dl."
    viol = smokers[~condition]
    return False, f"{len(viol)} smoker(s) have cholesterol ≤ 200 mg/dl (values: {', '.join(map(str, viol['cholesterol_mg_dl']))})."

def stmt_15(df: pd.DataFrame):
    """15. All patients with a diagnosis of diabetes have a BMI greater than 20."""
    diag = df[df["diagnosis"] == "diabetes"]
    if diag.empty:
        return True, "No patients with diabetes, so statement vacuously true."
    condition = diag["bmi"] > 20
    truth = condition.all()
    if truth:
        return True, f"All {len(diag)} patients with diabetes have BMI > 20."
    viol = diag[~condition]
    return False, f"{len(viol)} patient(s) with diabetes have BMI ≤ 20 (values: {', '.join(map(str, viol['bmi']))})."

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one patient with a diagnosis of arthritis whose age is greater than 60 years."""
    arthritis = df[(df["diagnosis"] == "arthritis") & (df["age"] > 60)]
    truth = not arthritis.empty
    if truth:
        return True, f"Found {len(arthritis)} arthritis patient(s) older than 60."
    return False, "No arthritis patient older than 60."

def stmt_17(df: pd.DataFrame):
    """17. If a patient has a systolic blood pressure greater than 150 mmHg, then their age is greater than 50 years."""
    high_sys = df[df["bp_systolic"] > 150]
    if high_sys.empty:
        return True, "No patients with systolic BP > 150 mmHg, so statement vacuously true."
    condition = high_sys["age"] > 50
    truth = condition.all()
    if truth:
        return True, f"All {len(high_sys)} patients with systolic BP > 150 mmHg are older than 50."
    viol = high_sys[~condition]
    return False, f"{len(viol)} patient(s) with systolic BP > 150 mmHg are 50 or younger (ages: {', '.join(map(str, viol['age']))})."

def stmt_18(df: pd.DataFrame):
    """18. All patients with a cholesterol level greater than 240 mg/dl have a BMI greater than 30."""
    high_chol = df[df["cholesterol_mg_dl"] > 240]
    if high_chol.empty:
        return True, "No patients with cholesterol > 240 mg/dl, so statement vacuously true."
    condition = high_chol["bmi"] > 30
    truth = condition.all()
    if truth:
        return True, f"All {len(high_chol)} patients with cholesterol > 240 mg/dl have BMI > 30."
    viol = high_chol[~condition]
    return False, f"{len(viol)} patient(s) with cholesterol > 240 mg/dl have BMI ≤ 30 (values: {', '.join(map(str, viol['bmi']))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_91.csv")
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
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()