import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients aged 65 or older have asthma."""
    older_patients = df[df["age"] >= 65]
    has_asthma = df[df["diagnosis"] == "asthma"]
    older_with_asthma = older_patients[older_patients["patient_id"].isin(has_asthma["patient_id"])]
    truth = len(older_patients) == len(older_with_asthma)
    if truth:
        expl = f"All {len(older_patients)} patients aged 65 or older have asthma."
    else:
        viol = older_patients[~older_patients["patient_id"].isin(has_asthma["patient_id"])]
        expl = f"{len(viol)} patients aged 65 or older do not have asthma."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hypertension patients have systolic blood pressure at least 148 mmHg."""
    hypertensive = df[df["diagnosis"] == "hypertension"]
    condition = hypertensive["bp_systolic"] >= 148
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertensive)} hypertension patients have systolic BP >= 148."
    else:
        viol = hypertensive[~condition]
        expl = f"{len(viol)} hypertension patients have systolic BP < 148."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All hypertension patients have diastolic blood pressure at most 83 mmHg."""
    hypertensive = df[df["diagnosis"] == "hypertension"]
    condition = hypertensive["bp_diastolic"] <= 83
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertensive)} hypertension patients have diastolic BP <= 83."
    else:
        viol = hypertensive[~condition]
        expl = f"{len(viol)} hypertension patients have diastolic BP > 83."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All diabetes patients are 35 years old or younger."""
    diabetic = df[df["diagnosis"] == "diabetes"]
    condition = diabetic["age"] <= 35
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetic)} diabetes patients are 35 or younger."
    else:
        viol = diabetic[~condition]
        expl = f"{len(viol)} diabetes patients are older than 35."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All arthritis patients have diastolic blood pressure at least 74 mmHg."""
    arthritic = df[df["diagnosis"] == "arthritis"]
    condition = arthritic["bp_diastolic"] >= 74
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritic)} arthritis patients have diastolic BP >= 74."
    else:
        viol = arthritic[~condition]
        expl = f"{len(viol)} arthritis patients have diastolic BP < 74."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All asthma patients have systolic blood pressure between 116 and 154 mmHg inclusive."""
    asthmatic = df[df["diagnosis"] == "asthma"]
    condition = asthmatic["bp_systolic"].between(116, 154, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(asthmatic)} asthma patients have systolic BP between 116 and 154."
    else:
        viol = asthmatic[~condition]
        expl = f"{len(viol)} asthma patients have systolic BP outside range [116, 154]."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All smokers have cholesterol level at least 176 mg/dL."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["cholesterol_mg_dl"] >= 176
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have cholesterol >= 176."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers have cholesterol < 176."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All non-smokers have cholesterol level at most 193 mg/dL."""
    nonsmokers = df[df["smoker"] == "no"]
    condition = nonsmokers["cholesterol_mg_dl"] <= 193
    truth = condition.all()
    if truth:
        expl = f"All {len(nonsmokers)} non-smokers have cholesterol <= 193."
    else:
        viol = nonsmokers[~condition]
        expl = f"{len(viol)} non-smokers have cholesterol > 193."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most patients in the table are smokers."""
    total = len(df)
    smokers = len(df[df["smoker"] == "yes"])
    truth = smokers > total / 2
    if truth:
        expl = f"{smokers} out of {total} patients are smokers (>50%)."
    else:
        expl = f"{smokers} out of {total} patients are smokers (<=50%)."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All patients with BMI of 30 or higher have cholesterol of at least 190 mg/dL."""
    obese = df[df["bmi"] >= 30]
    condition = obese["cholesterol_mg_dl"] >= 190
    truth = condition.all()
    if truth:
        expl = f"All {len(obese)} patients with BMI >= 30 have cholesterol >= 190."
    else:
        viol = obese[~condition]
        expl = f"{len(viol)} patients with BMI >= 30 have cholesterol < 190."
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
        (10, stmt_10)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()