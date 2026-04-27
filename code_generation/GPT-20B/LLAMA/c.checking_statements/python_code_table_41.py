import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of arthritis have a BMI less than or equal to 34."""
    arthritis = df[df["diagnosis"] == "arthritis"]
    condition = arthritis["bmi"] <= 34
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritis)} arthritis patients have BMI <= 34."
    else:
        viol = arthritis[~condition]
        expl = f"{len(viol)} arthritis patients violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a patient is a smoker, then their age is greater than or equal to 49 or less than or equal to 63."""
    smokers = df[df["smoker"] == "yes"]
    condition = (smokers["age"] >= 49) | (smokers["age"] <= 63)
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers satisfy age >=49 or age <=63."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one patient with a diagnosis of asthma whose cholesterol level is less than 180 mg/dl."""
    asthma = df[df["diagnosis"] == "asthma"]
    condition = asthma["cholesterol_mg_dl"] < 180
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"{count} asthma patient(s) have cholesterol < 180 mg/dl."
    else:
        expl = "No asthma patient has cholesterol < 180 mg/dl."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all patients with a BMI greater than 30, their systolic blood pressure is greater than or equal to 120."""
    high_bmi = df[df["bmi"] > 30]
    condition = high_bmi["bp_systolic"] >= 120
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 have systolic BP >= 120."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 30 violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a patient has a diagnosis of diabetes, then their diastolic blood pressure is greater than or equal to 71."""
    diabetes = df[df["diagnosis"] == "diabetes"]
    condition = diabetes["bp_diastolic"] >= 71
    truth = condition.all()
    if truth:
        expl = f"All {len(diabetes)} diabetes patients have diastolic BP >= 71."
    else:
        viol = diabetes[~condition]
        expl = f"{len(viol)} diabetes patients violate the rule (diastolic BP: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All patients with a systolic blood pressure greater than 150 have a diagnosis of either migraine or hypertension."""
    high_sys = df[df["bp_systolic"] > 150]
    condition = high_sys["diagnosis"].isin(["migraine", "hypertension"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sys)} patients with systolic BP > 150 have diagnosis migraine or hypertension."
    else:
        viol = high_sys[~condition]
        expl = f"{len(viol)} patients with systolic BP > 150 violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients in the table have a cholesterol level greater than 200 mg/dl."""
    proportion = (df["cholesterol_mg_dl"] > 200).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of patients have cholesterol > 200 mg/dl."
    else:
        expl = f"Only {proportion*100:.1f}% of patients have cholesterol > 200 mg/dl."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient is a non-smoker, then their BMI is greater than or equal to 28.9."""
    non_smokers = df[df["smoker"]!= "yes"]
    condition = non_smokers["bmi"] >= 28.9
    truth = condition.all()
    if truth:
        expl = f"All {len(non_smokers)} non-smokers have BMI >= 28.9."
    else:
        viol = non_smokers[~condition]
        expl = f"{len(viol)} non-smokers violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one patient with a diagnosis of migraine whose BMI is less than 25."""
    migraine = df[df["diagnosis"] == "migraine"]
    condition = migraine["bmi"] < 25
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"{count} migraine patient(s) have BMI < 25."
    else:
        expl = "No migraine patient has BMI < 25."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. For all patients with a diastolic blood pressure less than 90, their age is greater than or equal to 49."""
    low_diast = df[df["bp_diastolic"] < 90]
    condition = low_diast["age"] >= 49
    truth = condition.all()
    if truth:
        expl = f"All {len(low_diast)} patients with diastolic BP < 90 have age >= 49."
    else:
        viol = low_diast[~condition]
        expl = f"{len(viol)} patients with diastolic BP < 90 violate the rule (age: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

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