import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All individuals diagnosed with asthma are smokers."""
    asthma_smokers = df[(df["diagnosis"] == "asthma") & (df["smoker"] == "yes")]
    truth = len(asthma_smokers) == len(df[df["diagnosis"] == "asthma"])
    if truth:
        expl = f"All {len(df[df['diagnosis'] == 'asthma'])} asthma patients are smokers."
    else:
        viol = df[(df["diagnosis"] == "asthma") & (df["smoker"]!= "yes")]
        expl = f"{len(viol)} asthma patients are not smokers."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All diabetes patients have cholesterol between 191 and 244 mg/dL."""
    diabetes_patients = df[df["diagnosis"] == "diabetes"]
    condition = diabetes_patients["cholesterol_mg_dl"].between(191, 244, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetes_patients)} diabetes patients have cholesterol in range."
    else:
        viol = diabetes_patients[~condition]
        expl = f"{len(viol)} diabetes patients have cholesterol outside range."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All migraine patients have BMI ≥ 26.9."""
    migraine_patients = df[df["diagnosis"] == "migraine"]
    condition = migraine_patients["bmi"] >= 26.9
    truth = condition.all()
    if truth:
        expl = f"All {len(migraine_patients)} migraine patients have BMI ≥ 26.9."
    else:
        viol = migraine_patients[~condition]
        expl = f"{len(viol)} migraine patients have BMI < 26.9."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All hypertension patients have systolic ≥ 127 mmHg."""
    hypertension_patients = df[df["diagnosis"] == "hypertension"]
    condition = hypertension_patients["bp_systolic"] >= 127
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension_patients)} hypertension patients have systolic ≥ 127."
    else:
        viol = hypertension_patients[~condition]
        expl = f"{len(viol)} hypertension patients have systolic < 127."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient is younger than 30, then they have diabetes."""
    young_patients = df[df["age"] < 30]
    condition = young_patients["diagnosis"] == "diabetes"
    truth = condition.all() if len(young_patients) > 0 else True
    if truth:
        expl = f"All {len(young_patients)} patients under 30 have diabetes."
    else:
        viol = young_patients[~condition]
        expl = f"{len(viol)} patients under 30 do not have diabetes."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All smokers have systolic blood pressure ≤ 156 mmHg."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["bp_systolic"] <= 156
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have systolic ≤ 156."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers have systolic > 156."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All hypertension patients have diastolic ≤ 87 mmHg."""
    hypertension_patients = df[df["diagnosis"] == "hypertension"]
    condition = hypertension_patients["bp_diastolic"] <= 87
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension_patients)} hypertension patients have diastolic ≤ 87."
    else:
        viol = hypertension_patients[~condition]
        expl = f"{len(viol)} hypertension patients have diastolic > 87."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most patients have cholesterol above 200 mg/dL."""
    total_patients = len(df)
    high_cholesterol = df[df["cholesterol_mg_dl"] > 200]
    truth = len(high_cholesterol) > total_patients / 2
    if truth:
        expl = f"{len(high_cholesterol)} out of {total_patients} patients have cholesterol > 200."
    else:
        expl = f"{len(high_cholesterol)} out of {total_patients} patients have cholesterol > 200."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_51.csv")

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