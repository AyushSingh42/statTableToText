import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all individuals with asthma, systolic blood pressure is between 129 and 130 mmHg."""
    asthma = df[df["diagnosis"] == "asthma"]
    if asthma.empty:
        return True, "No asthma patients to evaluate."
    condition = asthma["bp_systolic"].between(129, 130, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients have systolic BP between 129 and 130 mmHg."
    else:
        viol = asthma[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all individuals with diabetes, diastolic blood pressure is at least 76 mmHg."""
    diabetes = df[df["diagnosis"] == "diabetes"]
    if diabetes.empty:
        return True, "No diabetes patients to evaluate."
    condition = diabetes["bp_diastolic"] >= 76
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetes)} diabetes patients have diastolic BP >= 76 mmHg."
    else:
        viol = diabetes[~condition]
        expl = f"{len(viol)} diabetes patients violate the rule (diastolic BP: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All smokers have cholesterol at least 182 mg/dL."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        return True, "No smokers to evaluate."
    condition = smokers["cholesterol_mg_dl"] >= 182
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have cholesterol >= 182 mg/dL."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all individuals with BMI greater than 33, systolic blood pressure does not exceed 143 mmHg."""
    high_bmi = df[df["bmi"] > 33]
    if high_bmi.empty:
        return True, "No individuals with BMI > 33 to evaluate."
    condition = high_bmi["bp_systolic"] <= 143
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} individuals with BMI > 33 have systolic BP <= 143 mmHg."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} individuals with BMI > 33 violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All individuals older than 70 have cholesterol at least 179 mg/dL."""
    older = df[df["age"] > 70]
    if older.empty:
        return True, "No individuals older than 70 to evaluate."
    condition = older["cholesterol_mg_dl"] >= 179
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} individuals older than 70 have cholesterol >= 179 mg/dL."
    else:
        viol = older[~condition]
        expl = f"{len(viol)} individuals older than 70 violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a person's systolic blood pressure is greater than 150 mmHg, then their diagnosis is diabetes."""
    high_systolic = df[df["bp_systolic"] > 150]
    if high_systolic.empty:
        return True, "No systolic BP > 150 mmHg to evaluate."
    condition = high_systolic["diagnosis"] == "diabetes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_systolic)} patients with systolic BP > 150 mmHg are diagnosed with diabetes."
    else:
        viol = high_systolic[~condition]
        expl = f"{len(viol)} patients with systolic BP > 150 mmHg are not diagnosed with diabetes (diagnoses: {', '.join(map(str, viol['diagnosis'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All migraine patients are older than 55 years."""
    migraine = df[df["diagnosis"] == "migraine"]
    if migraine.empty:
        return True, "No migraine patients to evaluate."
    condition = migraine["age"] > 55
    truth = condition.all()
    if truth:
        expl = f"All {len(migraine)} migraine patients are older than 55 years."
    else:
        viol = migraine[~condition]
        expl = f"{len(viol)} migraine patients violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All individuals with asthma are non-smokers."""
    asthma = df[df["diagnosis"] == "asthma"]
    if asthma.empty:
        return True, "No asthma patients to evaluate."
    condition = asthma["smoker"] == "no"
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients are non-smokers."
    else:
        viol = asthma[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (smoker status: {', '.join(map(str, viol['smoker'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_1.csv")

    # Convert numeric columns
    numeric_cols = ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Normalize smoker column to lowercase
    if "smoker" in df.columns:
        df["smoker"] = df["smoker"].str.lower()

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