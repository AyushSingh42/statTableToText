import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All patients with hypertension have a systolic blood pressure above 140."""
    hypertension = df[df["diagnosis"] == "hypertension"]
    condition = hypertension["bp_systolic"] > 140
    truth = condition.all()
    if truth:
        expl = f"All {len(hypertension)} patients with hypertension have a systolic blood pressure above 140."
    else:
        viol = hypertension[~condition]
        expl = f"{len(viol)} patients with hypertension violate the rule (systolic blood pressures: {', '.join(map(str, viol['bp_systolic'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. There exists at least one patient with diabetes who is a smoker."""
    diabetes = df[df["diagnosis"] == "diabetes"]
    smokers = diabetes[diabetes["smoker"] == "yes"]
    truth = len(smokers) > 0
    if truth:
        expl = f"There are {len(smokers)} patients with diabetes who are smokers."
    else:
        expl = "No patients with diabetes are smokers."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Most patients with asthma are under the age of 40."""
    asthma = df[df["diagnosis"] == "asthma"]
    condition = asthma["age"] < 40
    truth = condition.mean() > 0.5
    if truth:
        expl = f"{len(asthma[condition])} out of {len(asthma)} patients with asthma are under the age of 40."
    else:
        expl = f"{len(asthma[~condition])} out of {len(asthma)} patients with asthma are 40 or older."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a patient has arthritis, then they are likely to have a higher diastolic blood pressure, with all recorded values above 80."""
    arthritis = df[df["diagnosis"] == "arthritis"]
    condition = arthritis["bp_diastolic"] > 80
    truth = condition.all()
    if truth:
        expl = f"All {len(arthritis)} patients with arthritis have a diastolic blood pressure above 80."
    else:
        viol = arthritis[~condition]
        expl = f"{len(viol)} patients with arthritis violate the rule (diastolic blood pressures: {', '.join(map(str, viol['bp_diastolic'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All patients with migraine have a BMI below 30."""
    migraine = df[df["diagnosis"] == "migraine"]
    condition = migraine["bmi"] < 30
    truth = condition.all()
    if truth:
        expl = f"All {len(migraine)} patients with migraine have a BMI below 30."
    else:
        viol = migraine[~condition]
        expl = f"{len(viol)} patients with migraine violate the rule (BMIs: {', '.join(map(str, viol['bmi'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. There exists at least one patient with hypertension who is over the age of 60."""
    hypertension = df[df["diagnosis"] == "hypertension"]
    seniors = hypertension[hypertension["age"] > 60]
    truth = len(seniors) > 0
    if truth:
        expl = f"There are {len(seniors)} patients with hypertension who are over the age of 60."
    else:
        expl = "No patients with hypertension are over the age of 60."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most patients who are smokers have a diagnosis of hypertension."""
    smokers = df[df["smoker"] == "yes"]
    condition = smokers["diagnosis"] == "hypertension"
    truth = condition.mean() > 0.5
    if truth:
        expl = f"{len(smokers[condition])} out of {len(smokers)} smokers have a diagnosis of hypertension."
    else:
        expl = f"{len(smokers[~condition])} out of {len(smokers)} smokers do not have a diagnosis of hypertension."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a patient has a cholesterol level above 220, then they are likely to have a diagnosis of hypertension or diabetes."""
    high_cholesterol = df[df["cholesterol_mg_dl"] > 220]
    condition = high_cholesterol["diagnosis"].isin(["hypertension", "diabetes"])
    truth = condition.mean() > 0.5
    if truth:
        expl = f"{len(high_cholesterol[condition])} out of {len(high_cholesterol)} patients with high cholesterol have a diagnosis of hypertension or diabetes."
    else:
        expl = f"{len(high_cholesterol[~condition])} out of {len(high_cholesterol)} patients with high cholesterol do not have a diagnosis of hypertension or diabetes."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All patients with a BMI above 30 have a diagnosis of either diabetes or hypertension."""
    obese = df[df["bmi"] > 30]
    condition = obese["diagnosis"].isin(["diabetes", "hypertension"])
    truth = condition.all()
    if truth:
        expl = f"All {len(obese)} patients with a BMI above 30 have a diagnosis of either diabetes or hypertension."
    else:
        viol = obese[~condition]
        expl = f"{len(viol)} patients with a BMI above 30 violate the rule (diagnoses: {', '.join(map(str, viol['diagnosis'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one patient with asthma who is under the age of 30 and has a normal BMI."""
    asthma = df[df["diagnosis"] == "asthma"]
    young = asthma[asthma["age"] < 30]
    normal_bmi = young[(young["bmi"] >= 18.5) & (young["bmi"] <= 24.9)]
    truth = len(normal_bmi) > 0
    if truth:
        expl = f"There are {len(normal_bmi)} patients with asthma who are under the age of 30 and have a normal BMI."
    else:
        expl = "No patients with asthma are under the age of 30 and have a normal BMI."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_1.csv")
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["bp_systolic"] = pd.to_numeric(df["bp_systolic"], errors="coerce")
    df["bp_diastolic"] = pd.to_numeric(df["bp_diastolic"], errors="coerce")
    df["cholesterol_mg_dl"] = pd.to_numeric(df["cholesterol_mg_dl"], errors="coerce")
    df["bmi"] = pd.to_numeric(df["bmi"], errors="coerce")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()