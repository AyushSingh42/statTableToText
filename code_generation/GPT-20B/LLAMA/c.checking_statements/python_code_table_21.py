import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of diabetes have a BMI greater than or equal to 24.8."""
    subset = df[df["diagnosis"] == "diabetes"]
    if subset.empty:
        return True, "No diabetes patients to evaluate."
    condition = subset["bmi"] >= 24.8
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} diabetes patients have BMI >= 24.8."
    else:
        viol = subset[~condition]
        vals = viol["bmi"].tolist()
        return False, f"{len(viol)} diabetes patients violate the rule (BMI: {', '.join(map(str, vals))})."

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is less than 78 years."""
    subset = df[df["smoker"] == "yes"]
    if subset.empty:
        return True, "No smokers to evaluate."
    condition = subset["age"] < 78
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} smokers are younger than 78."
    else:
        viol = subset[~condition]
        ages = viol["age"].tolist()
        return False, f"{len(viol)} smokers violate the rule (ages: {', '.join(map(str, ages))})."

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of asthma whose cholesterol level is greater than 230 mg/dl."""
    subset = df[(df["diagnosis"] == "asthma") & (df["cholesterol_mg_dl"] > 230)]
    truth = not subset.empty
    if truth:
        return True, f"Found {len(subset)} asthma patient(s) with cholesterol > 230 mg/dl."
    else:
        return False, "No asthma patient with cholesterol > 230 mg/dl found."

def stmt_4(df: pd.DataFrame):
    """4. For all patients with a BMI greater than 30, their systolic blood pressure is greater than 118 mmHg."""
    subset = df[df["bmi"] > 30]
    if subset.empty:
        return True, "No patients with BMI > 30 to evaluate."
    condition = subset["bp_systolic"] > 118
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients with BMI > 30 have systolic BP > 118."
    else:
        viol = subset[~condition]
        vals = viol["bp_systolic"].tolist()
        return False, f"{len(viol)} patients with BMI > 30 violate the rule (systolic BP: {', '.join(map(str, vals))})."

def stmt_5(df: pd.DataFrame):
    """5. If a patient is a non-smoker, then their diastolic blood pressure is less than 98 mmHg."""
    subset = df[df["smoker"] == "no"]
    if subset.empty:
        return True, "No non-smokers to evaluate."
    condition = subset["bp_diastolic"] < 98
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} non-smokers have diastolic BP < 98."
    else:
        viol = subset[~condition]
        vals = viol["bp_diastolic"].tolist()
        return False, f"{len(viol)} non-smokers violate the rule (diastolic BP: {', '.join(map(str, vals))})."

def stmt_6(df: pd.DataFrame):
    """6. All patients with a diagnosis of arthritis have a BMI less than 30."""
    subset = df[df["diagnosis"] == "arthritis"]
    if subset.empty:
        return True, "No arthritis patients to evaluate."
    condition = subset["bmi"] < 30
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} arthritis patients have BMI < 30."
    else:
        viol = subset[~condition]
        vals = viol["bmi"].tolist()
        return False, f"{len(viol)} arthritis patients violate the rule (BMI: {', '.join(map(str, vals))})."

def stmt_7(df: pd.DataFrame):
    """7. Most patients in the table have a systolic blood pressure greater than 120 mmHg."""
    total = len(df)
    if total == 0:
        return True, "No patients in the table."
    count = (df["bp_systolic"] > 120).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% of patients have systolic BP > 120."
    else:
        return False, f"Only {proportion*100:.1f}% of patients have systolic BP > 120."

def stmt_8(df: pd.DataFrame):
    """8. If a patient's age is greater than 60, then their cholesterol level is less than 240 mg/dl."""
    subset = df[df["age"] > 60]
    if subset.empty:
        return True, "No patients older than 60 to evaluate."
    condition = subset["cholesterol_mg_dl"] < 240
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients older than 60 have cholesterol < 240."
    else:
        viol = subset[~condition]
        vals = viol["cholesterol_mg_dl"].tolist()
        return False, f"{len(viol)} patients older than 60 violate the rule (cholesterol: {', '.join(map(str, vals))})."

def stmt_9(df: pd.DataFrame):
    """9. For all patients with a BMI between 20 and 25, their age is less than 62 years."""
    subset = df[df["bmi"].between(20, 25, inclusive="both")]
    if subset.empty:
        return True, "No patients with BMI between 20 and 25 to evaluate."
    condition = subset["age"] < 62
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients with BMI 20-25 have age < 62."
    else:
        viol = subset[~condition]
        ages = viol["age"].tolist()
        return False, f"{len(viol)} patients with BMI 20-25 violate the rule (ages: {', '.join(map(str, ages))})."

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one patient with a diagnosis of hypertension whose systolic blood pressure is greater than 150 mmHg."""
    subset = df[(df["diagnosis"] == "hypertension") & (df["bp_systolic"] > 150)]
    truth = not subset.empty
    if truth:
        return True, f"Found {len(subset)} hypertension patient(s) with systolic BP > 150."
    else:
        return False, "No hypertension patient with systolic BP > 150 found."

def stmt_11(df: pd.DataFrame):
    """11. All patients with a cholesterol level greater than 220 mg/dl have a BMI greater than 23.8."""
    subset = df[df["cholesterol_mg_dl"] > 220]
    if subset.empty:
        return True, "No patients with cholesterol > 220 to evaluate."
    condition = subset["bmi"] > 23.8
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients with cholesterol > 220 have BMI > 23.8."
    else:
        viol = subset[~condition]
        vals = viol["bmi"].tolist()
        return False, f"{len(viol)} patients with cholesterol > 220 violate the rule (BMI: {', '.join(map(str, vals))})."

def stmt_12(df: pd.DataFrame):
    """12. If a patient is a smoker and has a diagnosis of asthma, then their age is less than 77 years."""
    subset = df[(df["smoker"] == "yes") & (df["diagnosis"] == "asthma")]
    if subset.empty:
        return True, "No smoker-asthma patients to evaluate."
    condition = subset["age"] < 77
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} smoker-asthma patients are younger than 77."
    else:
        viol = subset[~condition]
        ages = viol["age"].tolist()
        return False, f"{len(viol)} smoker-asthma patients violate the rule (ages: {', '.join(map(str, ages))})."

def stmt_13(df: pd.DataFrame):
    """13. For all patients with a diastolic blood pressure greater than 80 mmHg, their systolic blood pressure is greater than 140 mmHg."""
    subset = df[df["bp_diastolic"] > 80]
    if subset.empty:
        return True, "No patients with diastolic BP > 80 to evaluate."
    condition = subset["bp_systolic"] > 140
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients with diastolic BP > 80 have systolic BP > 140."
    else:
        viol = subset[~condition]
        vals = viol["bp_systolic"].tolist()
        return False, f"{len(viol)} patients with diastolic BP > 80 violate the rule (systolic BP: {', '.join(map(str, vals))})."

def stmt_14(df: pd.DataFrame):
    """14. Most patients in the table have a BMI greater than 25."""
    total = len(df)
    if total == 0:
        return True, "No patients in the table."
    count = (df["bmi"] > 25).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        return True, f"{proportion*100:.1f}% of patients have BMI > 25."
    else:
        return False, f"Only {proportion*100:.1f}% of patients have BMI > 25."

def stmt_15(df: pd.DataFrame):
    """15. If a patient's age is less than 40, then their cholesterol level is greater than 200 mg/dl."""
    subset = df[df["age"] < 40]
    if subset.empty:
        return True, "No patients younger than 40 to evaluate."
    condition = subset["cholesterol_mg_dl"] > 200
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients younger than 40 have cholesterol > 200."
    else:
        viol = subset[~condition]
        vals = viol["cholesterol_mg_dl"].tolist()
        return False, f"{len(viol)} patients younger than 40 violate the rule (cholesterol: {', '.join(map(str, vals))})."

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one patient with a diagnosis of diabetes whose BMI is greater than 32."""
    subset = df[(df["diagnosis"] == "diabetes") & (df["bmi"] > 32)]
    truth = not subset.empty
    if truth:
        return True, f"Found {len(subset)} diabetes patient(s) with BMI > 32."
    else:
        return False, "No diabetes patient with BMI > 32 found."

def stmt_17(df: pd.DataFrame):
    """17. All patients with a systolic blood pressure greater than 150 mmHg have a diagnosis of either diabetes or hypertension."""
    subset = df[df["bp_systolic"] > 150]
    if subset.empty:
        return True, "No patients with systolic BP > 150 to evaluate."
    condition = subset["diagnosis"].isin(["diabetes", "hypertension"])
    truth = condition.all()
    if truth:
        return True, f"All {len(subset)} patients with systolic BP > 150 have diagnosis diabetes or hypertension."
    else:
        viol = subset[~condition]
        diag = viol["diagnosis"].tolist()
        return False, f"{len(viol)} patients with systolic BP > 150 violate the rule (diagnoses: {', '.join(map(str, diag))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_21.csv")

    # Convert numeric columns safely
    numeric_cols = ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Standardize string columns
    df["smoker"] = df["smoker"].str.lower()
    df["diagnosis"] = df["diagnosis"].str.lower()

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