import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of asthma have a cholesterol level less than 245 mg/dl."""
    asthma = df[df["diagnosis"] == "asthma"]
    if asthma.empty:
        return True, "No asthma patients in the data."
    condition = asthma["cholesterol_mg_dl"] < 245
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients have cholesterol < 245."
    else:
        viol = asthma[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl']))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their BMI is greater than or equal to 22.6."""
    smokers = df[df["smoker"] == True]
    if smokers.empty:
        return True, "No smokers in the data."
    condition = smokers["bmi"] >= 22.6
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have BMI >= 22.6."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (BMI: {', '.join(map(str, viol['bmi']))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of arthritis who is over 55 years old and has a BMI greater than 30."""
    arthritis = df[(df["diagnosis"] == "arthritis") & (df["age"] > 55) & (df["bmi"] > 30)]
    truth = not arthritis.empty
    if truth:
        expl = f"Found {len(arthritis)} arthritis patient(s) over 55 with BMI > 30."
    else:
        expl = "No arthritis patient over 55 with BMI > 30 found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All patients with a systolic blood pressure greater than 145 have a diastolic blood pressure greater than or equal to 82."""
    high_systolic = df[df["bp_systolic"] > 145]
    if high_systolic.empty:
        return True, "No patients with systolic > 145."
    condition = high_systolic["bp_diastolic"] >= 82
    truth = condition.all()
    if truth:
        expl = f"All {len(high_systolic)} patients with systolic > 145 have diastolic >= 82."
    else:
        viol = high_systolic[~condition]
        expl = f"{len(viol)} patients with systolic > 145 violate the rule (diastolic: {', '.join(map(str, viol['bp_diastolic']))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient has a BMI between 20 and 25, then their age is less than 50."""
    bmi_range = df[(df["bmi"] >= 20) & (df["bmi"] <= 25)]
    if bmi_range.empty:
        return True, "No patients with BMI between 20 and 25."
    condition = bmi_range["age"] < 50
    truth = condition.all()
    if truth:
        expl = f"All {len(bmi_range)} patients with BMI 20-25 are under 50."
    else:
        viol = bmi_range[~condition]
        expl = f"{len(viol)} patients with BMI 20-25 are 50 or older (ages: {', '.join(map(str, viol['age']))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most patients in the table have a cholesterol level greater than 200 mg/dl."""
    majority = df["cholesterol_mg_dl"] > 200
    truth = majority.mean() > 0.5
    count = majority.sum()
    expl = f"{count} out of {len(df)} patients have cholesterol > 200 ({majority.mean()*100:.1f}%)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All patients with a diagnosis of hypertension have a systolic blood pressure greater than or equal to 115."""
    hypertension = df[df["diagnosis"] == "hypertension"]
    if hypertension.empty:
        return True, "No hypertension patients in the data."
    condition = hypertension["bp_systolic"] >= 115
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension)} hypertension patients have systolic >= 115."
    else:
        viol = hypertension[~condition]
        expl = f"{len(viol)} hypertension patients violate the rule (systolic: {', '.join(map(str, viol['bp_systolic']))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is over 60 years old, then their diastolic blood pressure is less than or equal to 94."""
    older = df[df["age"] > 60]
    if older.empty:
        return True, "No patients over 60."
    condition = older["bp_diastolic"] <= 94
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} patients over 60 have diastolic <= 94."
    else:
        viol = older[~condition]
        expl = f"{len(viol)} patients over 60 violate the rule (diastolic: {', '.join(map(str, viol['bp_diastolic']))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one patient with a diagnosis of migraine who is under 30 years old and has a BMI greater than 27."""
    migraine = df[(df["diagnosis"] == "migraine") & (df["age"] < 30) & (df["bmi"] > 27)]
    truth = not migraine.empty
    if truth:
        expl = f"Found {len(migraine)} migraine patient(s) under 30 with BMI > 27."
    else:
        expl = "No migraine patient under 30 with BMI > 27 found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All patients who are non-smokers have a BMI greater than or equal to 24.2."""
    non_smokers = df[df["smoker"] == False]
    if non_smokers.empty:
        return True, "No non-smokers in the data."
    condition = non_smokers["bmi"] >= 24.2
    truth = condition.all()
    if truth:
        expl = f"All {len(non_smokers)} non-smokers have BMI >= 24.2."
    else:
        viol = non_smokers[~condition]
        expl = f"{len(viol)} non-smokers violate the rule (BMI: {', '.join(map(str, viol['bmi']))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a patient has a cholesterol level greater than 230 mg/dl, then their BMI is greater than or equal to 27.5."""
    high_chol = df[df["cholesterol_mg_dl"] > 230]
    if high_chol.empty:
        return True, "No patients with cholesterol > 230."
    condition = high_chol["bmi"] >= 27.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_chol)} patients with cholesterol > 230 have BMI >= 27.5."
    else:
        viol = high_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol > 230 violate the rule (BMI: {', '.join(map(str, viol['bmi']))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most patients in the table are smokers."""
    smokers = df["smoker"] == True
    truth = smokers.mean() > 0.5
    count = smokers.sum()
    expl = f"{count} out of {len(df)} patients are smokers ({smokers.mean()*100:.1f}%)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All patients with a diagnosis of asthma have a systolic blood pressure less than 151."""
    asthma = df[df["diagnosis"] == "asthma"]
    if asthma.empty:
        return True, "No asthma patients in the data."
    condition = asthma["bp_systolic"] < 151
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients have systolic < 151."
    else:
        viol = asthma[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (systolic: {', '.join(map(str, viol['bp_systolic']))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a patient is under 40 years old, then their systolic blood pressure is less than or equal to 150."""
    young = df[df["age"] < 40]
    if young.empty:
        return True, "No patients under 40."
    condition = young["bp_systolic"] <= 150
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} patients under 40 have systolic <= 150."
    else:
        viol = young[~condition]
        expl = f"{len(viol)} patients under 40 violate the rule (systolic: {', '.join(map(str, viol['bp_systolic']))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one patient with a diagnosis of arthritis who has a cholesterol level greater than 235 mg/dl."""
    arthritis = df[(df["diagnosis"] == "arthritis") & (df["cholesterol_mg_dl"] > 235)]
    truth = not arthritis.empty
    if truth:
        expl = f"Found {len(arthritis)} arthritis patient(s) with cholesterol > 235."
    else:
        expl = "No arthritis patient with cholesterol > 235 found."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All patients with a BMI greater than 30 have a diastolic blood pressure greater than or equal to 91."""
    high_bmi = df[df["bmi"] > 30]
    if high_bmi.empty:
        return True, "No patients with BMI > 30."
    condition = high_bmi["bp_diastolic"] >= 91
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 have diastolic >= 91."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 30 violate the rule (diastolic: {', '.join(map(str, viol['bp_diastolic']))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a patient has a systolic blood pressure greater than 140, then their diastolic blood pressure is greater than or equal to 78."""
    high_systolic = df[df["bp_systolic"] > 140]
    if high_systolic.empty:
        return True, "No patients with systolic > 140."
    condition = high_systolic["bp_diastolic"] >= 78
    truth = condition.all()
    if truth:
        expl = f"All {len(high_systolic)} patients with systolic > 140 have diastolic >= 78."
    else:
        viol = high_systolic[~condition]
        expl = f"{len(viol)} patients with systolic > 140 violate the rule (diastolic: {', '.join(map(str, viol['bp_diastolic']))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_71.csv")

    # Convert numeric columns
    numeric_cols = ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert smoker to boolean
    df["smoker"] = df["smoker"].map({"yes": True, "no": False})

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