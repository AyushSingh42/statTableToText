import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hypertension patients have diastolic blood pressure of at least 85 mmHg."""
    hypertensives = df[df["diagnosis"] == "hypertension"]
    condition = hypertensives["bp_diastolic"] >= 85
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertensives)} hypertension patients have diastolic BP >= 85."
    else:
        viol = hypertensives[~condition]
        expl = f"{len(viol)} hypertension patients have diastolic BP < 85 (values: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hypertension patients have systolic blood pressure between 119 and 148 mmHg."""
    hypertensives = df[df["diagnosis"] == "hypertension"]
    condition = hypertensives["bp_systolic"].between(119, 148, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertensives)} hypertension patients have systolic BP between 119-148."
    else:
        viol = hypertensives[~condition]
        expl = f"{len(viol)} hypertension patients have systolic BP outside 119-148 range (values: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All patients aged 20 to 30 have cholesterol at most 212 mg/dL."""
    age_group = df[(df["age"] >= 20) & (df["age"] <= 30)]
    condition = age_group["cholesterol_mg_dl"] <= 212
    truth = condition.all()
    if truth:
        expl = f"All {len(age_group)} patients aged 20-30 have cholesterol <= 212."
    else:
        viol = age_group[~condition]
        expl = f"{len(viol)} patients aged 20-30 have cholesterol > 212 (values: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All asthma patients have cholesterol levels between 184 and 241 mg/dL."""
    asthmatics = df[df["diagnosis"] == "asthma"]
    condition = asthmatics["cholesterol_mg_dl"].between(184, 241, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(asthmatics)} asthma patients have cholesterol between 184-241."
    else:
        viol = asthmatics[~condition]
        expl = f"{len(viol)} asthma patients have cholesterol outside 184-241 range (values: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most patients have diastolic blood pressure of at least 85 mmHg."""
    condition = df["bp_diastolic"] >= 85
    count_true = condition.sum()
    total = len(df)
    truth = count_true > total / 2
    expl = f"{count_true} out of {total} patients have diastolic BP >= 85 ({count_true/total*100:.1f}% > 50%)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most patients are non-smokers."""
    non_smokers = df[df["smoker"] == "no"]
    count_non_smokers = len(non_smokers)
    total = len(df)
    truth = count_non_smokers > total / 2
    expl = f"{count_non_smokers} out of {total} patients are non-smokers ({count_non_smokers/total*100:.1f}% > 50%)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All patients with cholesterol at most 200 mg/dL have a BMI of at most 27.3."""
    low_cholesterol = df[df["cholesterol_mg_dl"] <= 200]
    condition = low_cholesterol["bmi"] <= 27.3
    truth = condition.all()
    if truth:
        expl = f"All {len(low_cholesterol)} patients with cholesterol <= 200 have BMI <= 27.3."
    else:
        viol = low_cholesterol[~condition]
        expl = f"{len(viol)} patients with cholesterol <= 200 have BMI > 27.3 (values: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is 30 years old or younger, then their systolic blood pressure does not exceed 148 mmHg."""
    young_patients = df[df["age"] <= 30]
    condition = young_patients["bp_systolic"] <= 148
    truth = condition.all()
    if truth:
        expl = f"All {len(young_patients)} patients aged 30 or younger have systolic BP <= 148."
    else:
        viol = young_patients[~condition]
        expl = f"{len(viol)} patients aged 30 or younger have systolic BP > 148 (values: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All patients with a BMI of 33 or higher have a diagnosis of diabetes, arthritis, or hypertension."""
    high_bmi = df[df["bmi"] >= 33]
    valid_diagnoses = ["diabetes", "arthritis", "hypertension"]
    condition = df.loc[high_bmi.index, "diagnosis"].isin(valid_diagnoses)
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI >= 33 have diagnosis of diabetes, arthritis, or hypertension."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI >= 33 do not have diagnosis of diabetes, arthritis, or hypertension (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
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
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()