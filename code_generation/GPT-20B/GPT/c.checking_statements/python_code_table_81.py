import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients older than 70 have a diagnosis of diabetes."""
    older = df[df["age"] > 70]
    if older.empty:
        return True, "No patients older than 70, rule vacuously satisfied."
    condition = older["diagnosis"] == "diabetes"
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} patients older than 70 have diagnosis diabetes."
    else:
        viol = older[~condition]
        expl = f"{len(viol)} patients older than 70 violate the rule (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All smokers have cholesterol of at least 167 mg/dL."""
    smokers = df[df["smoker"] == "yes"]
    if smokers.empty:
        return True, "No smokers, rule vacuously satisfied."
    condition = smokers["cholesterol_mg_dl"] >= 167
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have cholesterol >= 167 mg/dL."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All patients with BMI greater than 30 have a diagnosis of asthma, arthritis, or diabetes."""
    high_bmi = df[df["bmi"] > 30]
    if high_bmi.empty:
        return True, "No patients with BMI > 30, rule vacuously satisfied."
    allowed = {"asthma", "arthritis", "diabetes"}
    condition = high_bmi["diagnosis"].isin(allowed)
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 have diagnosis in {allowed}."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 30 violate the rule (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All patients with cholesterol of at least 230 mg/dL have either migraine or arthritis."""
    high_chol = df[df["cholesterol_mg_dl"] >= 230]
    if high_chol.empty:
        return True, "No patients with cholesterol >= 230 mg/dL, rule vacuously satisfied."
    allowed = {"migraine", "arthritis"}
    condition = high_chol["diagnosis"].isin(allowed)
    truth = condition.all()
    if truth:
        expl = f"All {len(high_chol)} patients with cholesterol >= 230 mg/dL have diagnosis in {allowed}."
    else:
        viol = high_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol >= 230 mg/dL violate the rule (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All patients with BMI below 22 have either migraine or arthritis."""
    low_bmi = df[df["bmi"] < 22]
    if low_bmi.empty:
        return True, "No patients with BMI < 22, rule vacuously satisfied."
    allowed = {"migraine", "arthritis"}
    condition = low_bmi["diagnosis"].isin(allowed)
    truth = condition.all()
    if truth:
        expl = f"All {len(low_bmi)} patients with BMI < 22 have diagnosis in {allowed}."
    else:
        viol = low_bmi[~condition]
        expl = f"{len(viol)} patients with BMI < 22 violate the rule (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most patients have cholesterol greater than 180 mg/dL."""
    total = len(df)
    if total == 0:
        return True, "No patients, rule vacuously satisfied."
    count = (df["cholesterol_mg_dl"] > 180).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% ({count} of {total}) of patients have cholesterol > 180 mg/dL."
    else:
        expl = f"{proportion*100:.1f}% ({count} of {total}) of patients have cholesterol > 180 mg/dL, which is not a majority."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients are smokers."""
    total = len(df)
    if total == 0:
        return True, "No patients, rule vacuously satisfied."
    count = (df["smoker"] == "yes").sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% ({count} of {total}) of patients are smokers."
    else:
        expl = f"{proportion*100:.1f}% ({count} of {total}) of patients are smokers, which is not a majority."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_81.csv")

    # Convert numeric columns safely
    numeric_cols = ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Standardize string columns
    if "diagnosis" in df.columns:
        df["diagnosis"] = df["diagnosis"].str.lower()
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()