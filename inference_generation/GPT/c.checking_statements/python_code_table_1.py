import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def _prepare_df(df: pd.DataFrame) -> pd.DataFrame:
    # Convert patient_id to integer if stored as string
    if df["patient_id"].dtype == object:
        df["patient_id"] = pd.to_numeric(df["patient_id"], errors="coerce").astype("Int64")
    # Standardize smoker column to boolean
    if df["smoker"].dtype == object:
        true_vals = {"yes", "y", "true", "1", "t", "smoker"}
        false_vals = {"no", "n", "false", "0", "f", "non-smoker", "non smoker"}
        df["smoker"] = df["smoker"].str.lower().map(
            lambda x: True if x in true_vals else (False if x in false_vals else pd.NA)
        )
    return df

def stmt_1(df: pd.DataFrame):
    """1. All hypertension patients are smokers."""
    subset = df[df["diagnosis"].str.lower() == "hypertension"]
    if subset.empty:
        return True, "No hypertension patients in the data."
    condition = subset["smoker"] == True
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} hypertension patients are smokers."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} hypertension patients are non‑smokers (patient_ids: {', '.join(map(str, viol['patient_id'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All asthma patients are non-smokers."""
    subset = df[df["diagnosis"].str.lower() == "asthma"]
    if subset.empty:
        return True, "No asthma patients in the data."
    condition = subset["smoker"] == False
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} asthma patients are non‑smokers."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} asthma patients are smokers (patient_ids: {', '.join(map(str, viol['patient_id'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All migraine patients are non-smokers."""
    subset = df[df["diagnosis"].str.lower() == "migraine"]
    if subset.empty:
        return True, "No migraine patients in the data."
    condition = subset["smoker"] == False
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} migraine patients are non‑smokers."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} migraine patients are smokers (patient_ids: {', '.join(map(str, viol['patient_id'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all hypertension patients, age is between 57 and 63 years."""
    subset = df[df["diagnosis"].str.lower() == "hypertension"]
    if subset.empty:
        return True, "No hypertension patients in the data."
    condition = subset["age"].between(57, 63, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} hypertension patients have age 57–63."
    else:
        viol = subset[~condition]
        ages = viol["age"].astype(str).tolist()
        expl = f"{len(viol)} hypertension patients fall outside 57–63 (ages: {', '.join(ages)})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All diabetes patients have a BMI between 30.1 and 32.0."""
    subset = df[df["diagnosis"].str.lower() == "diabetes"]
    if subset.empty:
        return True, "No diabetes patients in the data."
    condition = subset["bmi"].between(30.1, 32.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} diabetes patients have BMI 30.1–32.0."
    else:
        viol = subset[~condition]
        bmis = viol["bmi"].astype(str).tolist()
        expl = f"{len(viol)} diabetes patients have BMI outside 30.1–32.0 (BMIs: {', '.join(bmis)})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All asthma patients have a systolic blood pressure between 115 and 118 mmHg."""
    subset = df[df["diagnosis"].str.lower() == "asthma"]
    if subset.empty:
        return True, "No asthma patients in the data."
    condition = subset["bp_systolic"].between(115, 118, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} asthma patients have systolic BP 115–118."
    else:
        viol = subset[~condition]
        bps = viol["bp_systolic"].astype(str).tolist()
        expl = f"{len(viol)} asthma patients have systolic BP outside 115–118 (values: {', '.join(bps)})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All migraine patients have a diastolic blood pressure between 77 and 79 mmHg."""
    subset = df[df["diagnosis"].str.lower() == "migraine"]
    if subset.empty:
        return True, "No migraine patients in the data."
    condition = subset["bp_diastolic"].between(77, 79, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} migraine patients have diastolic BP 77–79."
    else:
        viol = subset[~condition]
        bps = viol["bp_diastolic"].astype(str).tolist()
        expl = f"{len(viol)} migraine patients have diastolic BP outside 77–79 (values: {', '.join(bps)})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All arthritis patients have a cholesterol level between 210 and 227 mg/dL."""
    subset = df[df["diagnosis"].str.lower() == "arthritis"]
    if subset.empty:
        return True, "No arthritis patients in the data."
    condition = subset["cholesterol_mg_dl"].between(210, 227, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} arthritis patients have cholesterol 210–227 mg/dL."
    else:
        viol = subset[~condition]
        vals = viol["cholesterol_mg_dl"].astype(str).tolist()
        expl = f"{len(viol)} arthritis patients have cholesterol outside 210–227 (values: {', '.join(vals)})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a patient is a smoker, then they have either hypertension or diabetes."""
    smokers = df[df["smoker"] == True]
    if smokers.empty:
        return True, "No smokers in the data."
    condition = smokers["diagnosis"].str.lower().isin(["hypertension", "diabetes"])
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have hypertension or diabetes."
    else:
        viol = smokers[~condition]
        diag = viol["diagnosis"].tolist()
        expl = f"{len(viol)} smokers have other diagnoses (diagnoses: {', '.join(map(str, diag))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Most patients have a cholesterol level above 180 mg/dL."""
    total = len(df)
    above = df["cholesterol_mg_dl"] > 180
    count_above = above.sum()
    truth = count_above > total / 2
    expl = f"{count_above} out of {total} patients ({count_above/total:.1%}) have cholesterol > 180 mg/dL."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_1.csv")
    df = _prepare_df(df)

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()