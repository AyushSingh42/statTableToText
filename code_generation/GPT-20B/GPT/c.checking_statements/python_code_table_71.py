import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all individuals with migraine, cholesterol is at least 172 mg/dL."""
    migraine = df[df["diagnosis"] == "migraine"]
    condition = migraine["cholesterol_mg_dl"] >= 172
    truth = condition.all()
    if truth:
        expl = f"All {len(migraine)} migraine patients have cholesterol >= 172 mg/dL."
    else:
        viol = migraine[~condition]
        expl = f"{len(viol)} migraine patient(s) violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all individuals with BMI greater than 30, the diagnosis is either hypertension or arthritis."""
    high_bmi = df[df["bmi"] > 30]
    condition = high_bmi["diagnosis"].isin(["hypertension", "arthritis"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 have diagnosis hypertension or arthritis."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patient(s) with BMI > 30 violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all smokers, systolic blood pressure is at least 113 mmHg."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["bp_systolic"] >= 113
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have systolic BP >= 113 mmHg."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smoker(s) violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all non-smokers, diastolic blood pressure is at most 91 mmHg."""
    nonsmokers = df[df["smoker"]!= "yes"]
    condition = nonsmokers["bp_diastolic"] <= 91
    truth = condition.all()
    if truth:
        expl = f"All {len(nonsmokers)} non-smokers have diastolic BP <= 91 mmHg."
    else:
        viol = nonsmokers[~condition]
        expl = f"{len(viol)} non-smoker(s) violate the rule (diastolic BP: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all patients older than 60 years, systolic blood pressure is at least 143 mmHg."""
    older = df[df["age"] > 60]
    condition = older["bp_systolic"] >= 143
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} patients older than 60 have systolic BP >= 143 mmHg."
    else:
        viol = older[~condition]
        expl = f"{len(viol)} patient(s) older than 60 violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all patients with hypertension, diastolic blood pressure is at least 91 mmHg."""
    hypert = df[df["diagnosis"] == "hypertension"]
    condition = hypert["bp_diastolic"] >= 91
    truth = condition.all()
    if truth:
        expl = f"All {len(hypert)} hypertension patients have diastolic BP >= 91 mmHg."
    else:
        viol = hypert[~condition]
        expl = f"{len(viol)} hypertension patient(s) violate the rule (diastolic BP: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All patients have a body-mass index between 22 and 35."""
    condition = df["bmi"].between(22, 35, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(df)} patients have BMI between 22 and 35."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} patient(s) violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For the sole patient with diabetes, the BMI is less than 23."""
    diabetes = df[df["diagnosis"] == "diabetes"]
    count = len(diabetes)
    if count == 1:
        truth = diabetes["bmi"].iloc[0] < 23
        if truth:
            expl = f"The sole diabetes patient has BMI {diabetes['bmi'].iloc[0]} < 23."
        else:
            expl = f"The sole diabetes patient has BMI {diabetes['bmi'].iloc[0]} >= 23."
    else:
        truth = False
        expl = f"Expected 1 diabetes patient, found {count}."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_71.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()