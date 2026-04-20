import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def _to_bool(series: pd.Series) -> pd.Series:
    """Convert various string representations of truth to boolean."""
    return series.astype(str).str.lower().isin(["yes", "y", "true", "1", "smoker"])

def stmt_1(df: pd.DataFrame):
    """1. All hypertension patients (PT001, PT005, PT010, PT015) are smokers."""
    hypertension_ids = ["PT001", "PT005", "PT010", "PT015"]
    subset = df[df["patient_id"].isin(hypertension_ids)]
    condition = subset["smoker_bool"]
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} hypertension patients are smokers."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} hypertension patient(s) are non‑smokers (IDs: {', '.join(viol['patient_id']))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All asthma patients (PT003, PT008, PT013) are non-smokers."""
    asthma_ids = ["PT003", "PT008", "PT013"]
    subset = df[df["patient_id"].isin(asthma_ids)]
    condition = ~subset["smoker_bool"]
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} asthma patients are non‑smokers."
    else:
        viol = subset[subset["smoker_bool"]]
        expl = f"{len(viol)} asthma patient(s) are smokers (IDs: {', '.join(viol['patient_id']))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. The majority of diabetes patients (2 out of 3) are smokers."""
    diabetes = df[df["diagnosis"].str.lower() == "diabetes"]
    total = len(diabetes)
    smokers = diabetes["smoker_bool"].sum()
    truth = total == 3 and smokers >= 2
    if truth:
        expl = f"Diabetes patients count = 3, smokers = {smokers} (≥2)."
    else:
        expl = f"Diabetes patients count = {total}, smokers = {smokers}. Requirement not met."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All arthritis patients (PT006, PT011) are non-smokers."""
    arthritis_ids = ["PT006", "PT011"]
    subset = df[df["patient_id"].isin(arthritis_ids)]
    condition = ~subset["smoker_bool"]
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} arthritis patients are non‑smokers."
    else:
        viol = subset[subset["smoker_bool"]]
        expl = f"{len(viol)} arthritis patient(s) are smokers (IDs: {', '.join(viol['patient_id']))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. The patient with the lowest systolic blood pressure is an asthma patient aged 23 (PT008 with 115 mmHg)."""
    min_bp = df["bp_systolic"].min()
    patient = df[df["bp_systolic"] == min_bp].iloc[0]
    condition = (
        patient["patient_id"] == "PT008"
        and patient["diagnosis"].strip().lower() == "asthma"
        and patient["age"] == 23
        and patient["bp_systolic"] == 115
    )
    truth = condition
    if truth:
        expl = f"Lowest systolic BP = {min_bp} mmHg belongs to PT008, an asthma patient aged 23."
    else:
        expl = (
            f"Lowest systolic BP = {min_bp} mmHg belongs to patient {patient['patient_id']} "
            f"(diagnosis: {patient['diagnosis']}, age: {patient['age']})."
        )
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All migraine patients have systolic blood pressure between 121 mmHg and 124 mmHg."""
    migraine = df[df["diagnosis"].str.lower() == "migraine"]
    condition = migraine["bp_systolic"].between(121, 124, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(migraine)} migraine patients have systolic BP in [121,124]."
    else:
        viol = migraine[~condition]
        expl = (
            f"{len(viol)} migraine patient(s) violate the range: "
            f"IDs {', '.join(viol['patient_id'])} with BP values {', '.join(map(str, viol['bp_systolic']))}."
        )
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Every hypertension patient has a body-mass index greater than 29."""
    hypertension = df[df["diagnosis"].str.lower() == "hypertension"]
    condition = hypertension["bmi"] > 29
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension)} hypertension patients have BMI > 29."
    else:
        viol = hypertension[~condition]
        expl = (
            f"{len(viol)} hypertension patient(s) have BMI ≤ 29: "
            f"IDs {', '.join(viol['patient_id'])} with BMIs {', '.join(map(str, viol['bmi']))}."
        )
    return truth, expl

def main():
    df = pd.read_csv("tables/table_1.csv")
    # Convert numeric columns stored as strings to proper numeric types
    for col in ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    # Standardize smoker column to boolean
    df["smoker_bool"] = _to_bool(df["smoker"])
    checks = [
        (1, stmt_1),
        (2, stmt_2),
        (3, stmt_3),
        (4, stmt_4),
        (5, stmt_5),
        (6, stmt_6),
        (7, stmt_7),
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()