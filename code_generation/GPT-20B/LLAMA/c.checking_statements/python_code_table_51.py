import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with asthma have a BMI greater than or equal to 20.6."""
    asthma = df[df["diagnosis"] == "asthma"]
    condition = asthma["bmi"] >= 20.6
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients have BMI >= 20.6."
    else:
        viol = asthma[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} asthma patients violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All patients with diabetes have a cholesterol level greater than or equal to 191 mg/dl."""
    diabetes = df[df["diagnosis"] == "diabetes"]
    condition = diabetes["cholesterol_mg_dl"] >= 191
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetes)} diabetes patients have cholesterol >= 191 mg/dl."
    else:
        viol = diabetes[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} diabetes patients violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a patient is a smoker, then their BMI is greater than or equal to 22.7."""
    smokers = df[df["smoker"].str.lower() == "yes"]
    condition = smokers["bmi"] >= 22.7
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have BMI >= 22.7."
    else:
        viol = smokers[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} smokers violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one patient with arthritis whose systolic blood pressure is greater than 150 mmHg."""
    arthritis = df[df["diagnosis"] == "arthritis"]
    exists = (arthritis["bp_systolic"] > 150).any()
    if exists:
        ids = arthritis[arthritis["bp_systolic"] > 150]["patient_id"].tolist()
        expl = f"Found {len(ids)} arthritis patient(s) with systolic BP > 150 mmHg (IDs: {', '.join(ids)})."
    else:
        expl = "No arthritis patient has systolic BP > 150 mmHg."
    return exists, expl

def stmt_5(df: pd.DataFrame):
    """5. All patients with hypertension have a diastolic blood pressure greater than or equal to 74 mmHg."""
    hypertension = df[df["diagnosis"] == "hypertension"]
    condition = hypertension["bp_diastolic"] >= 74
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension)} hypertension patients have diastolic BP >= 74 mmHg."
    else:
        viol = hypertension[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} hypertension patients violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a patient's age is greater than 50, then their systolic blood pressure is less than or equal to 156 mmHg."""
    older = df[df["age"] > 50]
    condition = older["bp_systolic"] <= 156
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} patients older than 50 have systolic BP <= 156 mmHg."
    else:
        viol = older[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} patients older than 50 violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients have a cholesterol level greater than 200 mg/dl."""
    total = len(df)
    count = (df["cholesterol_mg_dl"] > 200).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        expl = f"{count}/{total} patients ({proportion:.2%}) have cholesterol > 200 mg/dl."
    else:
        expl = f"Only {count}/{total} patients ({proportion:.2%}) have cholesterol > 200 mg/dl."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All patients with migraine have a BMI greater than or equal to 26.9."""
    migraine = df[df["diagnosis"] == "migraine"]
    condition = migraine["bmi"] >= 26.9
    truth = condition.all()
    if truth:
        expl = f"All {len(migraine)} migraine patients have BMI >= 26.9."
    else:
        viol = migraine[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} migraine patients violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a patient's BMI is greater than 30, then they are a smoker."""
    high_bmi = df[df["bmi"] > 30]
    if high_bmi.empty:
        return True, "No patients with BMI > 30, rule vacuously true."
    condition = high_bmi["smoker"].str.lower() == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 are smokers."
    else:
        viol = high_bmi[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} patients with BMI > 30 are not smokers (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one patient with diabetes whose age is less than 30."""
    diabetes = df[df["diagnosis"] == "diabetes"]
    exists = (diabetes["age"] < 30).any()
    if exists:
        ids = diabetes[diabetes["age"] < 30]["patient_id"].tolist()
        expl = f"Found {len(ids)} diabetes patient(s) younger than 30 (IDs: {', '.join(ids)})."
    else:
        expl = "No diabetes patient is younger than 30."
    return exists, expl

def stmt_11(df: pd.DataFrame):
    """11. All patients with asthma have a systolic blood pressure greater than or equal to 119 mmHg."""
    asthma = df[df["diagnosis"] == "asthma"]
    condition = asthma["bp_systolic"] >= 119
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients have systolic BP >= 119 mmHg."
    else:
        viol = asthma[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} asthma patients violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a patient is a non-smoker, then their BMI is less than or equal to 31.8."""
    nonsmokers = df[df["smoker"].str.lower() == "no"]
    if nonsmokers.empty:
        return True, "No non-smokers, rule vacuously true."
    condition = nonsmokers["bmi"] <= 31.8
    truth = condition.all()
    if truth:
        expl = f"All {len(nonsmokers)} non-smokers have BMI <= 31.8."
    else:
        viol = nonsmokers[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} non-smokers violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All patients with hypertension have an age greater than or equal to 43."""
    hypertension = df[df["diagnosis"] == "hypertension"]
    condition = hypertension["age"] >= 43
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension)} hypertension patients have age >= 43."
    else:
        viol = hypertension[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} hypertension patients violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Most patients are smokers."""
    total = len(df)
    smokers = (df["smoker"].str.lower() == "yes").sum()
    proportion = smokers / total
    truth = proportion > 0.5
    if truth:
        expl = f"{smokers}/{total} patients ({proportion:.2%}) are smokers."
    else:
        expl = f"Only {smokers}/{total} patients ({proportion:.2%}) are smokers."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a patient's cholesterol level is greater than 230 mg/dl, then they are a smoker."""
    high_chol = df[df["cholesterol_mg_dl"] > 230]
    if high_chol.empty:
        return True, "No patients with cholesterol > 230 mg/dl, rule vacuously true."
    condition = high_chol["smoker"].str.lower() == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_chol)} patients with cholesterol > 230 mg/dl are smokers."
    else:
        viol = high_chol[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} patients with cholesterol > 230 mg/dl are not smokers (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All patients with arthritis have a systolic blood pressure greater than or equal to 156 mmHg."""
    arthritis = df[df["diagnosis"] == "arthritis"]
    condition = arthritis["bp_systolic"] >= 156
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritis)} arthritis patients have systolic BP >= 156 mmHg."
    else:
        viol = arthritis[~condition]
        ids = viol["patient_id"].tolist()
        expl = f"{len(viol)} arthritis patients violate the rule (IDs: {', '.join(ids)})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. There exists at least one patient with migraine whose diastolic blood pressure is less than 90 mmHg."""
    migraine = df[df["diagnosis"] == "migraine"]
    exists = (migraine["bp_diastolic"] < 90).any()
    if exists:
        ids = migraine[migraine["bp_diastolic"] < 90]["patient_id"].tolist()
        expl = f"Found {len(ids)} migraine patient(s) with diastolic BP < 90 mmHg (IDs: {', '.join(ids)})."
    else:
        expl = "No migraine patient has diastolic BP < 90 mmHg."
    return exists, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_51.csv")

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