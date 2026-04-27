import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all organic farms, soil_quality_index is at least 68.0."""
    organic = df[df["organic"].str.lower() == "yes"]
    if organic.empty:
        return True, "No organic farms present; statement vacuously true."
    condition = organic["soil_quality_index"] >= 68.0
    truth = condition.all()
    if truth:
        return True, f"All {len(organic)} organic farms satisfy the condition."
    viol = organic[~condition]
    return False, f"{len(viol)} organic farms violate the rule (soil_quality_index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."

def stmt_2(df: pd.DataFrame):
    """2. For all wheat farms, yield_tons is at least 308.4."""
    wheat = df[df["crop_type"].str.lower() == "wheat"]
    if wheat.empty:
        return True, "No wheat farms present; statement vacuously true."
    condition = wheat["yield_tons"] >= 308.4
    truth = condition.all()
    if truth:
        return True, f"All {len(wheat)} wheat farms satisfy the condition."
    viol = wheat[~condition]
    return False, f"{len(viol)} wheat farms violate the rule (yield_tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."

def stmt_3(df: pd.DataFrame):
    """3. For all corn farms, irrigation_hours_week is at least 14.4."""
    corn = df[df["crop_type"].str.lower() == "corn"]
    if corn.empty:
        return True, "No corn farms present; statement vacuously true."
    condition = corn["irrigation_hours_week"] >= 14.4
    truth = condition.all()
    if truth:
        return True, f"All {len(corn)} corn farms satisfy the condition."
    viol = corn[~condition]
    return False, f"{len(viol)} corn farms violate the rule (irrigation_hours_week: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."

def stmt_4(df: pd.DataFrame):
    """4. For all soybean farms, fertilizer_kg is at least 569."""
    soybean = df[df["crop_type"].str.lower() == "soybean"]
    if soybean.empty:
        return True, "No soybean farms present; statement vacuously true."
    condition = soybean["fertilizer_kg"] >= 569
    truth = condition.all()
    if truth:
        return True, f"All {len(soybean)} soybean farms satisfy the condition."
    viol = soybean[~condition]
    return False, f"{len(viol)} soybean farms violate the rule (fertilizer_kg: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."

def stmt_5(df: pd.DataFrame):
    """5. If soil_quality_index is at least 80, then the crop is wheat."""
    high_soil = df[df["soil_quality_index"] >= 80]
    if high_soil.empty:
        return True, "No farms with soil_quality_index >= 80; statement vacuously true."
    condition = high_soil["crop_type"].str.lower() == "wheat"
    truth = condition.all()
    if truth:
        return True, f"All {len(high_soil)} farms with soil_quality_index >= 80 are wheat."
    viol = high_soil[~condition]
    return False, f"{len(viol)} farms with soil_quality_index >= 80 are not wheat (crop_type: {', '.join(map(str, viol['crop_type'].tolist()))})."

def stmt_6(df: pd.DataFrame):
    """6. For farms with acreage greater than 140 acres, yield_tons is at least 290.6."""
    large = df[df["acreage"] > 140]
    if large.empty:
        return True, "No farms with acreage > 140; statement vacuously true."
    condition = large["yield_tons"] >= 290.6
    truth = condition.all()
    if truth:
        return True, f"All {len(large)} farms with acreage > 140 satisfy the condition."
    viol = large[~condition]
    return False, f"{len(viol)} farms with acreage > 140 violate the rule (yield_tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."

def stmt_7(df: pd.DataFrame):
    """7. Most farms have irrigation_hours_week of at least 14 hours per week."""
    total = len(df)
    if total == 0:
        return True, "No farms present; statement vacuously true."
    count = (df["irrigation_hours_week"] >= 14.0).sum()
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        return True, f"{count}/{total} farms ({proportion:.2%}) have irrigation_hours_week >= 14."
    else:
        return False, f"{count}/{total} farms ({proportion:.2%}) have irrigation_hours_week >= 14; not a majority."

def stmt_8(df: pd.DataFrame):
    """8. If fertilizer_kg exceeds 900 kg, then soil_quality_index is at most 73.7."""
    high_fert = df[df["fertilizer_kg"] > 900]
    if high_fert.empty:
        return True, "No farms with fertilizer_kg > 900; statement vacuously true."
    condition = high_fert["soil_quality_index"] <= 73.7
    truth = condition.all()
    if truth:
        return True, f"All {len(high_fert)} farms with fertilizer_kg > 900 satisfy the condition."
    viol = high_fert[~condition]
    return False, f"{len(viol)} farms with fertilizer_kg > 900 violate the rule (soil_quality_index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."

def main():
    df = pd.read_csv("../inference_generation/tables/table_78.csv")

    # Convert numeric columns safely
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors='coerce')
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()