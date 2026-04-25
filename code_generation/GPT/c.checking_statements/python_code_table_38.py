import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all organic farms, soil_quality_index is at least 68.5."""
    organic_farms = df[df["organic"] == "yes"]
    condition = organic_farms["soil_quality_index"] >= 68.5
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms meet the soil quality index requirement."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all non-organic farms, soil_quality_index is at least 69.2."""
    non_organic_farms = df[df["organic"] == "no"]
    condition = non_organic_farms["soil_quality_index"] >= 69.2
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic_farms)} non-organic farms meet the soil quality index requirement."
    else:
        viol = non_organic_farms[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If soil_quality_index is at least 81.2, then the crop type is soybean."""
    filtered_df = df[df["soil_quality_index"] >= 81.2]
    condition = filtered_df["crop_type"] == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered_df)} farms with soil quality index >= 81.2 have crop type soybean."
    else:
        viol = filtered_df[~condition]
        expl = f"{len(viol)} farms with soil quality index >= 81.2 do not have crop type soybean (crop types: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all corn farms, fertilizer_kg is at least 611."""
    corn_farms = df[df["crop_type"] == "corn"]
    condition = corn_farms["fertilizer_kg"] >= 611
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms meet the fertilizer requirement."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (fertilizer kg: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all wheat farms, yield_tons is at least 294.4."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = wheat_farms["yield_tons"] >= 294.4
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms meet the yield requirement."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yield tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most farms have soil_quality_index greater than 70."""
    total_farms = len(df)
    condition = df["soil_quality_index"] > 70
    count_greater_than_70 = condition.sum()
    truth = count_greater_than_70 > total_farms / 2
    if truth:
        expl = f"{count_greater_than_70} out of {total_farms} farms have soil quality index > 70, which is more than half."
    else:
        expl = f"{count_greater_than_70} out of {total_farms} farms have soil quality index > 70, which is not more than half."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all organic farms, irrigation_hours_week is at least 10.9."""
    organic_farms = df[df["organic"] == "yes"]
    condition = organic_farms["irrigation_hours_week"] >= 10.9
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms meet the irrigation hours requirement."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all non-organic farms, irrigation_hours_week is at most 18.6."""
    non_organic_farms = df[df["organic"] == "no"]
    condition = non_organic_farms["irrigation_hours_week"] <= 18.6
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic_farms)} non-organic farms meet the irrigation hours requirement."
    else:
        viol = non_organic_farms[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If fertilizer_kg exceeds 1000 kg, the crop type is soybean."""
    filtered_df = df[df["fertilizer_kg"] > 1000]
    condition = filtered_df["crop_type"] == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered_df)} farms with fertilizer_kg > 1000 have crop type soybean."
    else:
        viol = filtered_df[~condition]
        expl = f"{len(viol)} farms with fertilizer_kg > 1000 do not have crop type soybean (crop types: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_38.csv")

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