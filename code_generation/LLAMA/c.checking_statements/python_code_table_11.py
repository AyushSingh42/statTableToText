import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with a diagnosis of arthritis have a cholesterol level greater than 215 mg/dl."""
    arthritics = df[df["diagnosis"] == "arthritis"]
    condition = arthritics["cholesterol_mg_dl"] > 215
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritics)} arthritis patients have cholesterol > 215."
    else:
        viol = arthritics[~condition]
        expl = f"{len(viol)} arthritis patients have cholesterol <= 215 (cholesterol levels: {', '.join(map(str, viol['cholesterol_mg_dl'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All patients with a diagnosis of asthma have a BMI less than 34."""
    asthmatics = df[df["diagnosis"] == "asthma"]
    condition = asthmatics["bmi"] < 34
    truth = condition.all()
    if truth:
        expl = f"All {len(asthmatics)} asthma patients have BMI < 34."
    else:
        viol = asthmatics[~condition]
        expl = f"{len(viol)} asthma patients have BMI >= 34 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a patient is a smoker, then their age is greater than 35."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["age"] > 35
    truth = condition.all()
    if truth:
        expl = f"All {len(smokers)} smokers are older than 35."
    else:
        viol = smokers[~condition]
        expl = f"{len(viol)} smokers are 35 or younger (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All patients with a systolic blood pressure greater than 150 have a diagnosis of migraine."""
    high_bp = df[df["bp_systolic"] > 150]
    condition = high_bp["diagnosis"] == "migraine"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bp)} patients with BP > 150 have diagnosis migraine."
    else:
        viol = high_bp[~condition]
        expl = f"{len(viol)} patients with BP > 150 do not have diagnosis migraine (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. There exists at least one patient with a diagnosis of hypertension who is a smoker."""
    hyperten_smokers = df[(df["diagnosis"] == "hypertension") & (df["smoker"] == "yes")]
    truth = len(hyperten_smokers) > 0
    if truth:
        expl = f"There are {len(hyperten_smokers)} hypertensive smokers."
    else:
        expl = "No hypertensive smokers found."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All patients with a BMI greater than 30 have a diagnosis of either arthritis or hypertension."""
    high_bmi = df[df["bmi"] > 30]
    condition = (high_bmi["diagnosis"] == "arthritis") | (high_bmi["diagnosis"] == "hypertension")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 30 have diagnosis arthritis or hypertension."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 30 do not have diagnosis arthritis or hypertension (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a patient has a diastolic blood pressure less than 80, then their age is less than 40."""
    low_dbp = df[df["bp_diastolic"] < 80]
    condition = low_dbp["age"] < 40
    truth = condition.all()
    if truth:
        expl = f"All {len(low_dbp)} patients with DBP < 80 are under 40."
    else:
        viol = low_dbp[~condition]
        expl = f"{len(viol)} patients with DBP < 80 are 40 or older (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All patients with a cholesterol level greater than 230 mg/dl have a BMI greater than 25."""
    high_chol = df[df["cholesterol_mg_dl"] > 230]
    condition = high_chol["bmi"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(high_chol)} patients with cholesterol > 230 have BMI > 25."
    else:
        viol = high_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol > 230 have BMI <= 25 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most patients with a diagnosis of hypertension have a systolic blood pressure greater than 125."""
    hypertensives = df[df["diagnosis"] == "hypertension"]
    high_sbp = hypertensives[hypertensives["bp_systolic"] > 125]
    truth = len(high_sbp) > len(hypertensives) / 2
    if truth:
        expl = f"More than half ({len(high_sbp)}/{len(hypertensives)}) of hypertensive patients have SBP > 125."
    else:
        expl = f"Less than half ({len(high_sbp)}/{len(hypertensives)}) of hypertensive patients have SBP > 125."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All patients with a BMI less than 25 have a diagnosis of either asthma or migraine."""
    low_bmi = df[df["bmi"] < 25]
    condition = (low_bmi["diagnosis"] == "asthma") | (low_bmi["diagnosis"] == "migraine")
    truth = condition.all()
    if truth:
        expl = f"All {len(low_bmi)} patients with BMI < 25 have diagnosis asthma or migraine."
    else:
        viol = low_bmi[~condition]
        expl = f"{len(viol)} patients with BMI < 25 do not have diagnosis asthma or migraine (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a patient is older than 60, then their diagnosis is either hypertension or asthma."""
    old = df[df["age"] > 60]
    condition = (old["diagnosis"] == "hypertension") | (old["diagnosis"] == "asthma")
    truth = condition.all()
    if truth:
        expl = f"All {len(old)} patients over 60 have diagnosis hypertension or asthma."
    else:
        viol = old[~condition]
        expl = f"{len(viol)} patients over 60 do not have diagnosis hypertension or asthma (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All patients with a systolic blood pressure less than 130 have a diagnosis of either hypertension or migraine."""
    low_sbp = df[df["bp_systolic"] < 130]
    condition = (low_sbp["diagnosis"] == "hypertension") | (low_sbp["diagnosis"] == "migraine")
    truth = condition.all()
    if truth:
        expl = f"All {len(low_sbp)} patients with SBP < 130 have diagnosis hypertension or migraine."
    else:
        viol = low_sbp[~condition]
        expl = f"{len(viol)} patients with SBP < 130 do not have diagnosis hypertension or migraine (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. There exists at least one patient with a diagnosis of arthritis who is a smoker."""
    arthritics_smokers = df[(df["diagnosis"] == "arthritis") & (df["smoker"] == "yes")]
    truth = len(arthritics_smokers) > 0
    if truth:
        expl = f"There are {len(arthritics_smokers)} arthritis smokers."
    else:
        expl = "No arthritis smokers found."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All patients with a cholesterol level less than 200 mg/dl have a BMI less than 30."""
    low_chol = df[df["cholesterol_mg_dl"] < 200]
    condition = low_chol["bmi"] < 30
    truth = condition.all()
    if truth:
        expl = f"All {len(low_chol)} patients with cholesterol < 200 have BMI < 30."
    else:
        viol = low_chol[~condition]
        expl = f"{len(viol)} patients with cholesterol < 200 have BMI >= 30 (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a patient has a BMI greater than 32, then their diagnosis is either arthritis or hypertension."""
    high_bmi = df[df["bmi"] > 32]
    condition = (high_bmi["diagnosis"] == "arthritis") | (high_bmi["diagnosis"] == "hypertension")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_bmi)} patients with BMI > 32 have diagnosis arthritis or hypertension."
    else:
        viol = high_bmi[~condition]
        expl = f"{len(viol)} patients with BMI > 32 do not have diagnosis arthritis or hypertension (diagnoses: {', '.join(viol['diagnosis'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_11.csv")

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
        (8, stmt_8),
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()