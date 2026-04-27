import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all organic farms, soil_quality_index is at least 68.7."""
    organic_farms = df[df["organic"] == "yes"]
    if organic_farms.empty:
        return True, "No organic farms to check; statement holds."
    condition = organic_farms["soil_quality_index"] >= 68.7
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil_quality_index >= 68.7."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil_quality_index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all rice farms, yield_tons is at least 357.4."""
    rice_farms = df[df["crop_type"] == "rice"]
    if rice_farms.empty:
        return True, "No rice farms to check; statement holds."
    condition = rice_farms["yield_tons"] >= 357.4
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have yield_tons >= 357.4."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (yield_tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all corn farms, soil_quality_index is at least 70.0."""
    corn_farms = df[df["crop_type"] == "corn"]
    if corn_farms.empty:
        return True, "No corn farms to check; statement holds."
    condition = corn_farms["soil_quality_index"] >= 70.0
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have soil_quality_index >= 70.0."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (soil_quality_index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all soybean farms, irrigation_hours_week is between 13.2 and 14.1 hours per week."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    if soybean_farms.empty:
        return True, "No soybean farms to check; statement holds."
    condition = soybean_farms["irrigation_hours_week"].between(13.2, 14.1, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have irrigation_hours_week between 13.2 and 14.1."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (irrigation_hours_week: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a farm's fertilizer_kg exceeds 1000, the crop type is wheat."""
    high_fertilizer = df[df["fertilizer_kg"] > 1000]
    if high_fertilizer.empty:
        return True, "No farms with fertilizer_kg > 1000; statement holds."
    condition = high_fertilizer["crop_type"] == "wheat"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fertilizer)} farms with fertilizer_kg > 1000 have crop_type wheat."
    else:
        viol = high_fertilizer[~condition]
        expl = f"{len(viol)} farms with fertilizer_kg > 1000 violate the rule (crop_type: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All farms with soil_quality_index at least 80 are either corn or wheat."""
    high_soil = df[df["soil_quality_index"] >= 80]
    if high_soil.empty:
        return True, "No farms with soil_quality_index >= 80; statement holds."
    condition = high_soil["crop_type"].isin(["corn", "wheat"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil_quality_index >= 80 are either corn or wheat."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms with soil_quality_index >= 80 violate the rule (crop_type: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all farms with irrigation_hours_week at least 19, soil_quality_index equals 78.5."""
    high_irrigation = df[df["irrigation_hours_week"] >= 19]
    if high_irrigation.empty:
        return True, "No farms with irrigation_hours_week >= 19; statement holds."
    condition = high_irrigation["soil_quality_index"] == 78.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation)} farms with irrigation_hours_week >= 19 have soil_quality_index 78.5."
    else:
        viol = high_irrigation[~condition]
        expl = f"{len(viol)} farms with irrigation_hours_week >= 19 violate the rule (soil_quality_index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If acreage is between 70 and 80 acres inclusive, the crop is soybean."""
    mid_acreage = df[df["acreage"].between(70, 80, inclusive="both")]
    if mid_acreage.empty:
        return True, "No farms with acreage between 70 and 80; statement holds."
    condition = mid_acreage["crop_type"] == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(mid_acreage)} farms with acreage between 70 and 80 acres are soybean."
    else:
        viol = mid_acreage[~condition]
        expl = f"{len(viol)} farms with acreage between 70 and 80 acres violate the rule (crop_type: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_28.csv")

    # Convert numeric columns safely
    numeric_cols = ["acreage", "yield_tons", "irrigation_hours_week", "fertilizer_kg", "soil_quality_index"]
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()