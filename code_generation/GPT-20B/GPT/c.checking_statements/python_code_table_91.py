import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All arthritis patients have systolic blood pressure no greater than 154 mmHg."""
    arthritis = df[df["diagnosis"] == "arthritis"]
    condition = arthritis["bp_systolic"] <= 154
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritis)} arthritis patients have systolic BP ≤ 154."
    else:
        viol = arthritis[~condition]
        expl = f"{len(viol)} arthritis patients violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All hypertension patients have diastolic blood pressure at least 75 mmHg."""
    hypertension = df[df["diagnosis"] == "hypertension"]
    condition = hypertension["bp_diastolic"] >= 75
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension)} hypertension patients have diastolic BP ≥ 75."
    else:
        viol = hypertension[~condition]
        expl = f"{len(viol)} hypertension patients violate the rule (diastolic BP: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All patients with BMI greater than 30 have cholesterol at least 189 mg/dL."""
    high_bmi = df[df["bmi"] > 30]
    condition = high_bmi["cholesterol_mg_dl"] >= 189
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 have cholesterol ≥ 189."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 30 violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All smokers have systolic blood pressure no greater than 144 mmHg."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["bp_systolic"] <= 144
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers have systolic BP ≤ 144."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers violate the rule (systolic BP: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All asthma patients have cholesterol at least 212 mg/dL."""
    asthma = df[df["diagnosis"] == "asthma"]
    condition = asthma["cholesterol_mg_dl"] >= 212
    truth = condition.all()
    if truth:
        expl = f"All {len(asthma)} asthma patients have cholesterol ≥ 212."
    else:
        viol = asthma[~condition]
        expl = f"{len(viol)} asthma patients violate the rule (cholesterol: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All migraine patients have BMI between 21.0 and 30.4."""
    migraine = df[df["diagnosis"] == "migraine"]
    condition = migraine["bmi"].between(21.0, 30.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(migraine)} migraine patients have BMI between 21.0 and 30.4."
    else:
        viol = migraine[~condition]
        expl = f"{len(viol)} migraine patients violate the rule (BMI: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients have cholesterol greater than 188 mg/dL."""
    total = len(df)
    count = (df["cholesterol_mg_dl"] > 188).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} patients (>{total/2}) have cholesterol > 188."
    else:
        expl = f"Only {count} out of {total} patients have cholesterol > 188."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All patients with cholesterol above 230 mg/dL have either asthma or diabetes."""
    high_chol = df[df["cholesterol_mg_dl"] > 230]
    condition = high_chol["diagnosis"].isin(["asthma", "diabetes"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_chol)} patients with cholesterol > 230 have asthma or diabetes."
    else:
        viol = high_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol > 230 violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All patients with BMI at least 33 have either arthritis or diabetes."""
    high_bmi = df[df["bmi"] >= 33]
    condition = high_bmi["diagnosis"].isin(["arthritis", "diabetes"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI ≥ 33 have arthritis or diabetes."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI ≥ 33 violate the rule (diagnosis: {', '.join(map(str, viol['diagnosis'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_91.csv")

    # Convert numeric columns safely
    for col in ["age", "bp_systolic", "bp_diastolic", "cholesterol_mg_dl", "bmi"]:
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()