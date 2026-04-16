

import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All hypertension patients are smokers."""
    hyp = df[df['diagnosis'] == 'hypertension']
    if hyp.empty:
        truth = True
        expl = "No hypertension patients."
    else:
        smokers = hyp['smoker'].astype(bool)
        truth = smokers.all()
        if truth:
            expl = f"All {len(hyp)} hypertension patients are smokers."
        else:
            viol = hyp[~smokers]
            expl = f"{len(viol)} hypertension patients are non-smokers."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Asthma patients have systolic blood pressure below 120 mmHg."""
    asthma = df[df['diagnosis'] == 'asthma']
    if asthma.empty:
        truth = True
        expl = "No asthma patients."
    else:
        systolic = asthma['bp_systolic']
        truth = (systolic < 120).all()
        if truth:
            expl = f"All {len(asthma)} asthma patients have systolic BP <120."
        else:
            viol = asthma[~(systolic < 120)]
            expl = f"{len(viol)} asthma patients have systolic BP ≥120."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Patients with BMI ≥ 30 have higher systolic blood pressure than those with BMI < 30."""
    group1 = df[df['bmi'] >= 30]
    group2 = df[df['bmi'] < 30]
    if group1.empty or group2.empty:
        truth = False
        expl = "One or both BMI groups are empty."
    else:
        mean1 = group1['bp_systolic'].mean()
        mean2 = group2['bp_systolic'].mean()
        truth = mean1 > mean2
        expl = f"Mean systolic BP for BMI≥30: {mean1:.2f}, BMI<30: {mean2:.2f}."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Among smokers, those with hypertension have higher systolic blood pressure than non-hypertensive smokers."""
    smokers = df[df['smoker'].astype(bool)]
    hyp_smokers = smokers[smokers['diagnosis'] == 'hypertension']
    non_hyp_smokers = smokers[smokers['diagnosis']!= 'hypertension']
    if hyp_smokers.empty or non_hyp_smokers.empty:
        truth = False
        expl = "One or both smoker groups are empty."
    else:
        mean_hyp = hyp_smokers['bp_systolic'].mean()
        mean_non_hyp = non_hyp_smokers['bp_systolic'].mean()
        truth = mean_hyp > mean_non_hyp
        expl = f"Mean systolic BP for hypertensive smokers: {mean_hyp:.2f}, non-hypertensive smokers: {mean_non_hyp:.2f}."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All patients with systolic blood pressure ≥ 140 mmHg have hypertension."""
    systolic_high = df[df['bp_systolic'] >= 140]
    if systolic_high.empty:
        truth = True
        expl = "No patients with systolic BP ≥140."
    else:
        truth = (systolic_high['diagnosis'] == 'hypertension').all()
        if truth:
            expl = f"All {len(systolic_high)} patients with systolic BP ≥140 have hypertension."
        else:
            viol = systolic_high[systolic_high['diagnosis']!= 'hypertension']
            expl = f"{len(viol)} patients with systolic BP ≥140 do not have hypertension."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Migraine patients have diastolic blood pressure below 80 mmHg."""
    migraine = df[df['diagnosis'] =='migraine']
    if migraine.empty:
        truth = True
        expl = "No migraine patients."
    else:
        truth = (migraine['bp_diastolic'] < 80).all()
        if truth:
            expl = f"All {len(migraine)} migraine patients have diastolic BP <80."
        else:
            viol = migraine[~(migraine['bp_diastolic'] < 80)]
            expl = f"{len(viol)} migraine patients have diastolic BP ≥80."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Hypertension patients with BMI ≥ 30 have higher cholesterol levels than non-hypertensive patients with BMI ≥ 30."""
    group1 = df[(df['diagnosis'] == 'hypertension') & (df['bmi'] >= 30)]
    group2 = df[(df['diagnosis']!= 'hypertension') & (df['bmi'] >= 30)]
    if group1.empty or group2.empty:
        truth = False
        expl = "One or both BMI≥30 groups are empty."
    else:
        mean1 = group1['cholesterol_mg_dl'].mean()
        mean2 = group2['cholesterol_mg_dl'].mean()
        truth = mean1 > mean2
        expl = f"Mean cholesterol for hypertensive BMI≥30: {mean1:.2f}, non-hypertensive BMI≥30: {mean2:.2f}."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Patients with diabetes are older than those with asthma."""
    diabetes = df[df['diagnosis'] == 'diabetes']
    asthma = df[df['diagnosis'] == 'asthma']
    if diabetes.empty or asthma.empty:
        truth = False
        expl = "One or both diagnosis groups are empty."
    else:
        mean_diag = diabetes['age'].mean()
        mean_asth = asthma['age'].mean()
        truth = mean_diag > mean_asth
        expl = f"Mean age for diabetes: {mean_diag:.2f}, asthma: {mean_asth:.2f}."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All asthma patients are non-smokers."""
    asthma = df[df['diagnosis'] == 'asthma']
    if asthma.empty:
        truth = True
        expl = "No asthma patients."
    else:
        truth = (asthma['smoker'].astype(bool) == False).all()
        if truth:
            expl = f"All {len(asthma)} asthma patients are non-smokers."
        else:
            viol = asthma[asthma['smoker'].astype(bool)]
            expl = f"{len(viol)} asthma patients are smokers."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Hypertension patients have higher cholesterol levels than diabetes patients."""
    hyp = df[df['diagnosis'] == 'hypertension']
    diabetes = df[df['diagnosis'] == 'diabetes']
    if hyp.empty or diabetes.empty:
        truth = False
        expl = "One or both diagnosis groups are empty."
    else:
        mean_hyp = hyp['cholesterol_mg_dl'].mean()
        mean_diag = diabetes['cholesterol_mg_dl'].mean()
        truth = mean_hyp > mean_diag
        expl = f"Mean cholesterol for hypertension: {mean_hyp:.2f}, diabetes: {mean_diag:.2f}."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Patients with systolic blood pressure ≥ 140 mmHg and BMI ≥ 30 are all smokers."""
    group = df[(df['bp_systolic'] >= 140) & (df['bmi'] >= 30)]
    if group.empty:
        truth = True
        expl = "No patients meet systolic ≥140 and BMI ≥30."
    else:
        truth = group['smoker'].astype(bool).all()
        if truth:
            expl = f"All {len(group)} patients with systolic ≥140 and BMI ≥30 are smokers."
        else:
            viol = group[~group['smoker'].astype(bool)]
            expl = f"{len(viol)} patients meet systolic ≥140 and BMI ≥30 but are non-smokers."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Among patients aged ≥ 60, all have BMI ≥ 30."""
    old = df[df['age'] >= 60]
    if old.empty:
        truth = True
        expl = "No patients aged ≥60."
    else:
        truth = (old['bmi'] >= 30).all()
        if truth:
            expl = f"All {len(old)} patients aged ≥60 have BMI ≥30."
        else:
            viol = old[old['bmi'] < 30]
            expl = f"{len(viol)} patients aged ≥60 have BMI <30."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a patient has hypertension and BMI ≥ 30, their systolic blood pressure exceeds 140 mmHg."""
    group = df[(df['diagnosis'] == 'hypertension') & (df['bmi'] >= 30)]
    if group.empty:
        truth = True
        expl = "No hypertension patients with BMI ≥30."
    else:
        truth = (group['bp_systolic'] > 140).all()
        if truth:
            expl = f"All {len(group)} hypertension patients with BMI ≥30 have systolic BP >140."
        else:
            viol = group[group['bp_systolic'] <= 140]
            expl = f"{len(viol)} hypertension patients with BMI ≥30 have systolic BP ≤140."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Patients with diabetes who are smokers have higher BMI than non-smoking diabetes patients."""
    diabetic_smokers = df[(df['diagnosis'] == 'diabetes') & (df['smoker'].astype(bool))]
    diabetic_non_smokers = df[(df['diagnosis'] == 'diabetes') & (~df['smoker'].astype(bool))]
    if diabetic_smokers.empty or diabetic_non_smokers.empty:
        truth = False
        expl = "One or both diabetes groups are empty."
    else:
        mean_smokers = diabetic_smokers['bmi'].mean()
        mean_non_smokers = diabetic_non_smokers['bmi'].mean()
        truth = mean_smokers > mean_non_smokers
        expl = f"Mean BMI for diabetic smokers: {mean_smokers:.2f}, non-smokers: {mean_non_smokers:.2f}."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Hypertension patients have higher systolic blood pressure than diabetes patients."""
    hyp = df[df['diagnosis'] == 'hypertension']
    diabetes = df[df['diagnosis'] == 'diabetes']
    if hyp.empty or diabetes.empty:
        truth = False
        expl = "One or both diagnosis groups are empty."
    else:
        mean_hyp = hyp['bp_systolic'].mean()
        mean_diag = diabetes['bp_systolic'].mean()
        truth = mean_hyp > mean_diag
        expl = f"Mean systolic BP for hypertension: {mean_hyp:.2f}, diabetes: {mean_diag:.2f}."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_1.csv")
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['bp_systolic'] = pd.to_numeric(df['bp_systolic'], errors='coerce')
    df['bp_diastolic'] = pd.to_numeric(df['bp_diastolic'], errors='coerce')
    df['cholesterol_mg_dl'] = pd.to_numeric(df['cholesterol_mg_dl'], errors='coerce')
    df['bmi'] = pd.to_numeric(df['bmi'], errors='coerce')
    df['smoker'] = df['smoker'].astype(bool)
    
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
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()