import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all individuals with asthma, systolic blood pressure is between 129 and 130 mmHg."""
    asthmatics = df[df["diagnosis"] == "asthma"]
    condition = asthmatics["bp_systolic"].between(129, 130, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(asthmatics)} asthma patients have systolic BP between 129 and 130."
    else:
        viol = asthmatics[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all individuals with diabetes, diastolic blood pressure is at least 76 mmHg."""
    diabetics = df[df["diagnosis"] == "diabetes"]
    condition = diabetics["bp_diastolic"] >= 76
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetics)} diabetic patients have diastolic BP >= 76."
    else:
        viol = diabetics[~condition]
        expl = f"{len(viol)} diabetic patients violate the rule (BP: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All smokers have cholesterol at least 182 mg/dL."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["cholesterol_mg_dl"] >= 182
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have cholesterol >= 182."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all individuals with BMI greater than 33, systolic blood pressure does not exceed 143 mmHg."""
    high_bmi = df[df["bmi"] > 33]
    condition = high_bmi["bp_systolic"] <= 143
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 33 have systolic BP <= 143."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 33 violate the rule (BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All individuals older than 70 have cholesterol at least 179 mg/dL."""
    seniors = df[df["age"] > 70]
    condition = seniors["cholesterol_mg_dl"] >= 179
    truth = condition.all()
    if truth:
        expl = f"All {len(seniors)} individuals over 70 have cholesterol >= 179."
    else:
        viol = seniors[~condition]
        expl = f"{len(viol)} individuals over 70 violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a person's systolic blood pressure is greater than 150 mmHg, then their diagnosis is diabetes."""
    high_bp = df[df["bp_systolic"] > 150]
    condition = high_bp["diagnosis"] == "diabetes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bp)} patients with systolic BP > 150 are diagnosed with diabetes."
    else:
        viol = high_bp[~condition]
        expl = f"{len(viol)} patients with systolic BP > 150 are not diagnosed with diabetes (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All migraine patients are older than 55 years."""
    migraine_patients = df[df["diagnosis"] == "migraine"]
    condition = migraine_patients["age"] > 55
    truth = condition.all()
    if truth:
        expl = f"All {len(migraine_patients)} migraine patients are older than 55."
    else:
        viol = migraine_patients[~condition]
        expl = f"{len(viol)} migraine patients are 55 or younger (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All individuals with asthma are non-smokers."""
    asthmatics = df[df["diagnosis"] == "asthma"]
    condition = asthmatics["smoker"] == "no"
    truth = condition.all()
    if truth:
        expl = f"All {len(asthmatics)} asthma patients are non-smokers."
    else:
        viol = asthmatics[~condition]
        expl = f"{len(viol)} asthma patients are smokers (IDs: {', '.join(viol['patient_id'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_1.csv")

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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()