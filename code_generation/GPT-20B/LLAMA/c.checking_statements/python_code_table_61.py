import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of arthritis have a BMI less than or equal to 33.9."""
    arth = df[df["diagnosis"] == "arthritis"]
    if arth.empty:
        return True, "No arthritis patients to evaluate."
    cond = arth["bmi"] <= 33.9
    truth = cond.all()
    if truth:
        expl = f"All {len(arth)} arthritis patients have BMI <= 33.9."
    else:
        viol = arth[~cond]
        expl = f"{len(viol)} arthritis patients violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is less than 70 years."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        return True, "No smokers to evaluate."
    cond = smokers["age"] < 70
    truth = cond.all()
    if truth:
        expl = f"All {len(smokers)} smokers are under 70 years old."
    else:
        viol = smokers[~cond]
        expl = f"{len(viol)} smokers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All patients with a diagnosis of hypertension have a systolic blood pressure greater than or equal to 142 mmHg."""
    hyp = df[df["diagnosis"] == "hypertension"]
    if hyp.empty:
        return True, "No hypertension patients to evaluate."
    cond = hyp["bp_systolic"] >= 142
    truth = cond.all()
    if truth:
        expl = f"All {len(hyp)} hypertension patients have systolic BP >= 142 mmHg."
    else:
        viol = hyp[~cond]
        expl = f"{len(viol)} hypertension patients violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one patient with a diagnosis of asthma whose cholesterol level is greater than 240 mg/dL."""
    exists = df[(df["diagnosis"] == "asthma") & (df["cholesterol_mg_dl"] > 240)].shape[0] > 0
    truth = exists
    if truth:
        count = df[(df["diagnosis"] == "asthma") & (df["cholesterol_mg_dl"] > 240)].shape[0]
        expl = f"Found {count} asthma patient(s) with cholesterol > 240 mg/dL."
    else:
        expl = "No asthma patient with cholesterol > 240 mg/dL."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient's BMI is greater than 30, then their age is less than 70 years."""
    high_bmi = df[df["bmi"] > 30]
    if high_bmi.empty:
        return True, "No patients with BMI > 30 to evaluate."
    cond = high_bmi["age"] < 70
    truth = cond.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 are under 70 years old."
    else:
        viol = high_bmi[~cond]
        expl = f"{len(viol)} patients with BMI > 30 violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All patients with a diagnosis of migraine have a diastolic blood pressure less than 80 mmHg."""
    mig = df[df["diagnosis"] == "migraine"]
    if mig.empty:
        return True, "No migraine patients to evaluate."
    cond = mig["bp_diastolic"] < 80
    truth = cond.all()
    if truth:
        expl = f"All {len(mig)} migraine patients have diastolic BP < 80 mmHg."
    else:
        viol = mig[~cond]
        expl = f"{len(viol)} migraine patients violate the rule (diastolic BP: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients in the table have a systolic blood pressure greater than 120 mmHg."""
    prop = (df["bp_systolic"] > 120).mean()
    truth = prop > 0.5
    expl = f"{prop*100:.1f}% of patients have systolic BP > 120 mmHg."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient's age is greater than 60 years, then their cholesterol level is less than 220 mg/dL."""
    over_60 = df[df["age"] > 60]
    if over_60.empty:
        return True, "No patients over 60 to evaluate."
    cond = over_60["cholesterol_mg_dl"] < 220
    truth = cond.all()
    if truth:
        expl = f"All {len(over_60)} patients over 60 have cholesterol < 220 mg/dL."
    else:
        viol = over_60[~cond]
        expl = f"{len(viol)} patients over 60 violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All patients with a diagnosis of arthritis have a cholesterol level greater than 190 mg/dL."""
    arth = df[df["diagnosis"] == "arthritis"]
    if arth.empty:
        return True, "No arthritis patients to evaluate."
    cond = arth["cholesterol_mg_dl"] > 190
    truth = cond.all()
    if truth:
        expl = f"All {len(arth)} arthritis patients have cholesterol > 190 mg/dL."
    else:
        viol = arth[~cond]
        expl = f"{len(viol)} arthritis patients violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one patient with a diagnosis of hypertension whose BMI is less than 28."""
    exists = df[(df["diagnosis"] == "hypertension") & (df["bmi"] < 28)].shape[0] > 0
    truth = exists
    if truth:
        count = df[(df["diagnosis"] == "hypertension") & (df["bmi"] < 28)].shape[0]
        expl = f"Found {count} hypertension patient(s) with BMI < 28."
    else:
        expl = "No hypertension patient with BMI < 28."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a patient is a non-smoker, then their BMI is less than 33."""
    non_smokers = df[df["smoker"] == "no"]
    if non_smokers.empty:
        return True, "No non-smokers to evaluate."
    cond = non_smokers["bmi"] < 33
    truth = cond.all()
    if truth:
        expl = f"All {len(non_smokers)} non-smokers have BMI < 33."
    else:
        viol = non_smokers[~cond]
        expl = f"{len(viol)} non-smokers violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All patients with a cholesterol level greater than 230 mg/dL have a systolic blood pressure greater than 120 mmHg."""
    high_chol = df[df["cholesterol_mg_dl"] > 230]
    if high_chol.empty:
        return True, "No patients with cholesterol > 230 mg/dL to evaluate."
    cond = high_chol["bp_systolic"] > 120
    truth = cond.all()
    if truth:
        expl = f"All {len(high_chol)} patients with cholesterol > 230 mg/dL have systolic BP > 120 mmHg."
    else:
        viol = high_chol[~cond]
        expl = f"{len(viol)} patients with cholesterol > 230 mg/dL violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most patients in the table have a BMI greater than 20."""
    prop = (df["bmi"] > 20).mean()
    truth = prop > 0.5
    expl = f"{prop*100:.1f}% of patients have BMI > 20."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a patient's age is less than 40 years, then their cholesterol level is less than 220 mg/dL."""
    under_40 = df[df["age"] < 40]
    if under_40.empty:
        return True, "No patients under 40 to evaluate."
    cond = under_40["cholesterol_mg_dl"] < 220
    truth = cond.all()
    if truth:
        expl = f"All {len(under_40)} patients under 40 have cholesterol < 220 mg/dL."
    else:
        viol = under_40[~cond]
        expl = f"{len(viol)} patients under 40 violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All patients with a diagnosis of asthma have a diastolic blood pressure greater than 85 mmHg."""
    asthma = df[df["diagnosis"] == "asthma"]
    if asthma.empty:
        return True, "No asthma patients to evaluate."
    cond = asthma["bp_diastolic"] > 85
    truth = cond.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients have diastolic BP > 85 mmHg."
    else:
        viol = asthma[~cond]
        expl = f"{len(viol)} asthma patients violate the rule (diastolic BP: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one patient with a diagnosis of migraine whose BMI is less than 28."""
    exists = df[(df["diagnosis"] == "migraine") & (df["bmi"] < 28)].shape[0] > 0
    truth = exists
    if truth:
        count = df[(df["diagnosis"] == "migraine") & (df["bmi"] < 28)].shape[0]
        expl = f"Found {count} migraine patient(s) with BMI < 28."
    else:
        expl = "No migraine patient with BMI < 28."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a patient's systolic blood pressure is greater than 140 mmHg, then their age is less than 80 years."""
    high_systolic = df[df["bp_systolic"] > 140]
    if high_systolic.empty:
        return True, "No patients with systolic BP > 140 to evaluate."
    cond = high_systolic["age"] < 80
    truth = cond.all()
    if truth:
        expl = f"All {len(high_systolic)} patients with systolic BP > 140 are under 80 years old."
    else:
        viol = high_systolic[~cond]
        expl = f"{len(viol)} patients with systolic BP > 140 violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_61.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()