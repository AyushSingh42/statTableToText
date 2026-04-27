import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all organic farms, soil_quality_index is at least 68.5."""
    organic = df[df["organic"].str.lower() == "yes"]
    condition = organic["soil_quality_index"] >= 68.5
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms satisfy the condition."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil_quality_index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all non‑organic farms, soil_quality_index is at least 69.2."""
    non_organic = df[df["organic"].str.lower() == "no"]
    condition = non_organic["soil_quality_index"] >= 69.2
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic)} non‑organic farms satisfy the condition."
    else:
        viol = non_organic[~condition]
        expl = f"{len(viol)} non‑organic farms violate the rule (soil_quality_index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If soil_quality_index is at least 81.2, then the crop type is soybean."""
    high_soil = df[df["soil_quality_index"] >= 81.2]
    condition = high_soil["crop_type"].str.lower() == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil_quality_index ≥ 81.2 are soybean."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms with soil_quality_index ≥ 81.2 are not soybean (crop_type: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all corn farms, fertilizer_kg is at least 611."""
    corn = df[df["crop_type"].str.lower() == "corn"]
    condition = corn["fertilizer_kg"] >= 611
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms satisfy the condition."
    else:
        viol = corn[~condition]
        expl = f"{len(viol)} corn farms violate the rule (fertilizer_kg: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all wheat farms, yield_tons is at least 294.4."""
    wheat = df[df["crop_type"].str.lower() == "wheat"]
    condition = wheat["yield_tons"] >= 294.4
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms satisfy the condition."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yield_tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most farms have soil_quality_index greater than 70."""
    count_gt70 = (df["soil_quality_index"] > 70).sum()
    truth = count_gt70 > len(df) / 2
    if truth:
        expl = f"{count_gt70} out of {len(df)} farms have soil_quality_index > 70."
    else:
        expl = f"Only {count_gt70} out of {len(df)} farms have soil_quality_index > 70."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all organic farms, irrigation_hours_week is at least 10.9."""
    organic = df[df["organic"].str.lower() == "yes"]
    condition = organic["irrigation_hours_week"] >= 10.9
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms satisfy the condition."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (irrigation_hours_week: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all non‑organic farms, irrigation_hours_week is at most 18.6."""
    non_organic = df[df["organic"].str.lower() == "no"]
    condition = non_organic["irrigation_hours_week"] <= 18.6
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic)} non‑organic farms satisfy the condition."
    else:
        viol = non_organic[~condition]
        expl = f"{len(viol)} non‑organic farms violate the rule (irrigation_hours_week: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If fertilizer_kg exceeds 1000 kg, the crop type is soybean."""
    high_fert = df[df["fertilizer_kg"] > 1000]
    condition = high_fert["crop_type"].str.lower() == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} farms with fertilizer_kg > 1000 are soybean."
    else:
        viol = high_fert[~condition]
        expl = f"{len(viol)} farms with fertilizer_kg > 1000 are not soybean (crop_type: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_38.csv")

    # Convert numeric columns
    numeric_cols = ["acreage", "yield_tons", "irrigation_hours_week", "fertilizer_kg", "soil_quality_index"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Ensure organic column is lower case for consistency
    df["organic"] = df["organic"].str.lower()

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