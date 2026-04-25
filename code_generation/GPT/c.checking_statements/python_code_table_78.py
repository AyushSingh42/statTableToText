import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all organic farms, soil_quality_index is at least 68.0."""
    organic_farms = df[df["organic"] == "yes"]
    condition = organic_farms["soil_quality_index"] >= 68.0
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality index >= 68.0."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all wheat farms, yield_tons is at least 308.4."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = wheat_farms["yield_tons"] >= 308.4
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have yield_tons >= 308.4."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yield_tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all corn farms, irrigation_hours_week is at least 14.4."""
    corn_farms = df[df["crop_type"] == "corn"]
    condition = corn_farms["irrigation_hours_week"] >= 14.4
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have irrigation_hours_week >= 14.4."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (irrigation_hours_week: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all soybean farms, fertilizer_kg is at least 569."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    condition = soybean_farms["fertilizer_kg"] >= 569
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have fertilizer_kg >= 569."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (fertilizer_kg: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If soil_quality_index is at least 80, then the crop is wheat."""
    condition = df[(df["soil_quality_index"] >= 80) & (df["crop_type"]!= "wheat")]
    truth = len(condition) == 0
    if truth:
        expl = "No farm with soil quality index >= 80 has crop type other than wheat."
    else:
        expl = f"{len(condition)} farms violate the rule (soil_quality_index >= 80 but crop is not wheat)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For farms with acreage greater than 140 acres, yield_tons is at least 290.6."""
    large_farms = df[df["acreage"] > 140]
    condition = large_farms["yield_tons"] >= 290.6
    truth = condition.all()
    if truth:
        expl = f"All {len(large_farms)} large farms have yield_tons >= 290.6."
    else:
        viol = large_farms[~condition]
        expl = f"{len(viol)} large farms violate the rule (yield_tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms have irrigation_hours_week of at least 14 hours per week."""
    condition = df["irrigation_hours_week"] >= 14
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} farms have irrigation_hours_week >= 14 (more than half)."
    else:
        expl = f"{count} out of {total} farms have irrigation_hours_week >= 14 (not more than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If fertilizer_kg exceeds 900 kg, then soil_quality_index is at most 73.7."""
    condition = df[(df["fertilizer_kg"] > 900) & (df["soil_quality_index"] > 73.7)]
    truth = len(condition) == 0
    if truth:
        expl = "No farm with fertilizer_kg > 900 has soil_quality_index > 73.7."
    else:
        expl = f"{len(condition)} farms violate the rule (fertilizer_kg > 900 but soil_quality_index > 73.7)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_78.csv")

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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()