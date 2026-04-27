import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all patients with systolic blood pressure ≥150 mmHg, cholesterol is at least 196 mg/dL."""
    subset = df[df["bp_systolic"] >= 150]
    if subset.empty:
        return True, "No patients have systolic BP ≥150, so the statement holds vacuously."
    condition = subset["cholesterol_mg_dl"] >= 196
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients with systolic BP ≥150 have cholesterol ≥196."
    viol = subset[~condition]
    return False, f"{len(viol)} patients violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl']))})."

def stmt_2(df: pd.DataFrame):
    """2. All smokers have a BMI of at least 20.9."""
    subset = df[df["smoker"] == "yes"]
    if subset.empty:
        return True, "No smokers in the dataset, so the statement holds vacuously."
    condition = subset["bmi"] >= 20.9
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} smokers have BMI ≥20.9."
    viol = subset[~condition]
    return False, f"{len(viol)} smokers violate the rule (BMI: {', '.join(map(str, viol['bmi']))})."

def stmt_3(df: pd.DataFrame):
    """3. All patients diagnosed with migraine are at least 59 years old."""
    subset = df[df["diagnosis"] == "migraine"]
    if subset.empty:
        return True, "No migraine patients, so the statement holds vacuously."
    condition = subset["age"] >= 59
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} migraine patients are ≥59 years old."
    viol = subset[~condition]
    return False, f"{len(viol)} migraine patients violate the rule (ages: {', '.join(map(str, viol['age']))})."

def stmt_4(df: pd.DataFrame):
    """4. All patients with a BMI greater than 33 have cholesterol no higher than 209 mg/dL."""
    subset = df[df["bmi"] > 33]
    if subset.empty:
        return True, "No patients with BMI >33, so the statement holds vacuously."
    condition = subset["cholesterol_mg_dl"] <= 209
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients with BMI >33 have cholesterol ≤209."
    viol = subset[~condition]
    return False, f"{len(viol)} patients violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl']))})."

def stmt_5(df: pd.DataFrame):
    """5. All patients with diastolic blood pressure ≤74 mmHg have asthma."""
    subset = df[df["bp_diastolic"] <= 74]
    if subset.empty:
        return True, "No patients with diastolic BP ≤74, so the statement holds vacuously."
    condition = subset["diagnosis"] == "asthma"
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients with diastolic BP ≤74 have asthma."
    viol = subset[~condition]
    return False, f"{len(viol)} patients violate the rule (diagnoses: {', '.join(map(str, viol['diagnosis']))})."

def stmt_6(df: pd.DataFrame):
    """6. Most patients have cholesterol above 200 mg/dL."""
    total = len(df)
    if total == 0:
        return True, "No patients in the dataset; the statement holds vacuously."
    count_above = (df["cholesterol_mg_dl"] > 200).sum()
    proportion = count_above / total
    truth = proportion > 0.5
    if truth:
        return True, f"{count_above}/{total} patients ({proportion:.2%}) have cholesterol >200."
    else:
        return False, f"Only {count_above}/{total} patients ({proportion:.2%}) have cholesterol >200."

def stmt_7(df: pd.DataFrame):
    """7. All patients aged 70 or older have either arthritis or migraine."""
    subset = df[df["age"] >= 70]
    if subset.empty:
        return True, "No patients aged 70 or older, so the statement holds vacuously."
    condition = subset["diagnosis"].isin(["arthritis", "migraine"])
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients aged ≥70 have arthritis or migraine."
    viol = subset[~condition]
    return False, f"{len(viol)} patients violate the rule (diagnoses: {', '.join(map(str, viol['diagnosis']))})."

def stmt_8(df: pd.DataFrame):
    """8. All asthma patients have a diastolic blood pressure of 74 mmHg."""
    subset = df[df["diagnosis"] == "asthma"]
    if subset.empty:
        return True, "No asthma patients, so the statement holds vacuously."
    condition = subset["bp_diastolic"] == 74
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} asthma patients have diastolic BP of 74."
    viol = subset[~condition]
    return False, f"{len(viol)} asthma patients violate the rule (diastolic BP: {', '.join(map(str, viol['bp_diastolic']))})."

def stmt_9(df: pd.DataFrame):
    """9. All diabetes patients have cholesterol between 206 and 210 mg/dL."""
    subset = df[df["diagnosis"] == "diabetes"]
    if subset.empty:
        return True, "No diabetes patients, so the statement holds vacuously."
    condition = subset["cholesterol_mg_dl"].between(206, 210, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} diabetes patients have cholesterol between 206 and 210."
    viol = subset[~condition]
    return False, f"{len(viol)} diabetes patients violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl']))})."

def stmt_10(df: pd.DataFrame):
    """10. All patients with a BMI between 20 and 25 have migraine."""
    subset = df[(df["bmi"] >= 20) & (df["bmi"] <= 25)]
    if subset.empty:
        return True, "No patients with BMI between 20 and 25, so the statement holds vacuously."
    condition = subset["diagnosis"] == "migraine"
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients with BMI 20-25 have migraine."
    viol = subset[~condition]
    return False, f"{len(viol)} patients violate the rule (diagnoses: {', '.join(map(str, viol['diagnosis']))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_41.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()