import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients older than 70 have a diagnosis of diabetes."""
    older_than_70 = df[df["age"] > 70]
    if older_than_70.empty:
        truth = True
        expl = "No patients older than 70 in dataset."
    else:
        has_diabetes = older_than_70["diagnosis"] == "diabetes"
        truth = has_diabetes.all()
        if truth:
            expl = f"All {len(older_than_70)} patients older than 70 have diabetes."
        else:
            violators = older_than_70[~has_diabetes]
            expl = f"{len(violators)} patients older than 70 do not have diabetes."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All smokers have cholesterol of at least 167 mg/dL."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        truth = True
        expl = "No smokers in dataset."
    else:
        high_cholesterol = smokers["cholesterol_mg_dl"] >= 167
        truth = high_cholesterol.all()
        if truth:
            expl = f"All {len(smokers)} smokers have cholesterol >= 167 mg/dL."
        else:
            violators = smokers[~high_cholesterol]
            expl = f"{len(violators)} smokers have cholesterol < 167 mg/dL."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All patients with BMI greater than 30 have a diagnosis of asthma, arthritis, or diabetes."""
    high_bmi = df[df["bmi"] > 30]
    if high_bmi.empty:
        truth = True
        expl = "No patients with BMI > 30 in dataset."
    else:
        valid_diagnoses = ["asthma", "arthritis", "diabetes"]
        has_valid_diag = high_bmi["diagnosis"].isin(valid_diagnoses)
        truth = has_valid_diag.all()
        if truth:
            expl = f"All {len(high_bmi)} patients with BMI > 30 have asthma, arthritis, or diabetes."
        else:
            violators = high_bmi[~has_valid_diag]
            expl = f"{len(violators)} patients with BMI > 30 do not have asthma, arthritis, or diabetes."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All patients with cholesterol of at least 230 mg/dL have either migraine or arthritis."""
    high_cholesterol = df[df["cholesterol_mg_dl"] >= 230]
    if high_cholesterol.empty:
        truth = True
        expl = "No patients with cholesterol >= 230 mg/dL in dataset."
    else:
        valid_diagnoses = ["migraine", "arthritis"]
        has_valid_diag = high_cholesterol["diagnosis"].isin(valid_diagnoses)
        truth = has_valid_diag.all()
        if truth:
            expl = f"All {len(high_cholesterol)} patients with cholesterol >= 230 mg/dL have migraine or arthritis."
        else:
            violators = high_cholesterol[~has_valid_diag]
            expl = f"{len(violators)} patients with cholesterol >= 230 mg/dL do not have migraine or arthritis."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All patients with BMI below 22 have either migraine or arthritis."""
    low_bmi = df[df["bmi"] < 22]
    if low_bmi.empty:
        truth = True
        expl = "No patients with BMI < 22 in dataset."
    else:
        valid_diagnoses = ["migraine", "arthritis"]
        has_valid_diag = low_bmi["diagnosis"].isin(valid_diagnoses)
        truth = has_valid_diag.all()
        if truth:
            expl = f"All {len(low_bmi)} patients with BMI < 22 have migraine or arthritis."
        else:
            violators = low_bmi[~has_valid_diag]
            expl = f"{len(violators)} patients with BMI < 22 do not have migraine or arthritis."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most patients have cholesterol greater than 180 mg/dL."""
    total_patients = len(df)
    high_cholesterol = df[df["cholesterol_mg_dl"] > 180]
    proportion = len(high_cholesterol) / total_patients
    truth = proportion > 0.5
    expl = f"{len(high_cholesterol)} out of {total_patients} patients have cholesterol > 180 mg/dL ({proportion:.2%} of total)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients are smokers."""
    total_patients = len(df)
    smokers = df[df["smoker"] == "yes"]
    proportion = len(smokers) / total_patients
    truth = proportion > 0.5
    expl = f"{len(smokers)} out of {total_patients} patients are smokers ({proportion:.2%} of total)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_81.csv")

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
        (7, stmt_7)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()