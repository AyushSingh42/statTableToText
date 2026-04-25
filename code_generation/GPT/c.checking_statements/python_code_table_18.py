import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all organic farms, soil quality index is at least 69.6."""
    organic_farms = df[df["organic"] == "yes"]
    condition = organic_farms["soil_quality_index"] >= 69.6
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms meet the soil quality index requirement."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all non-organic farms, soil quality index does not exceed 81.0."""
    non_organic_farms = df[df["organic"] == "no"]
    condition = non_organic_farms["soil_quality_index"] <= 81.0
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic_farms)} non-organic farms meet the soil quality index limit."
    else:
        viol = non_organic_farms[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All corn farms use between 626 and 817 kg of fertilizer."""
    corn_farms = df[df["crop_type"] == "corn"]
    condition = df["fertilizer_kg"].between(626, 817, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms use between 626 and 817 kg of fertilizer."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (fertilizer amounts: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All wheat farms have soil quality index of at least 71.5."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = wheat_farms["soil_quality_index"] >= 71.5
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms meet the soil quality index requirement."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All wheat farms yield at most 458.9 tons."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = wheat_farms["yield_tons"] <= 458.9
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms meet the yield limit."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All rice farms have acreage of at least 101 acres."""
    rice_farms = df[df["crop_type"] == "rice"]
    condition = rice_farms["acreage"] >= 101
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms meet the acreage requirement."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All farms irrigating more than 18 hours per week yield at least 382.4 tons."""
    high_irrigation_farms = df[df["irrigation_hours_week"] > 18]
    condition = high_irrigation_farms["yield_tons"] >= 382.4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation_farms)} high irrigation farms meet the yield requirement."
    else:
        viol = high_irrigation_farms[~condition]
        expl = f"{len(viol)} high irrigation farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most soybean farms irrigate less than 16 hours per week."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    condition = soybean_farms["irrigation_hours_week"] < 16
    truth = condition.sum() / len(soybean_farms) > 0.5
    if truth:
        expl = f"More than half ({condition.sum()}/{len(soybean_farms)}) of soybean farms irrigate less than 16 hours per week."
    else:
        expl = f"Less than or equal to half ({condition.sum()}/{len(soybean_farms)}) of soybean farms irrigate less than 16 hours per week."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most farms have soil quality index greater than 70."""
    condition = df["soil_quality_index"] > 70
    truth = condition.sum() / len(df) > 0.5
    if truth:
        expl = f"More than half ({condition.sum()}/{len(df)}) of farms have soil quality index greater than 70."
    else:
        expl = f"Less than or equal to half ({condition.sum()}/{len(df)}) of farms have soil quality index greater than 70."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_18.csv")

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
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()