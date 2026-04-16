import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. If a farm grows soybean, then it is organic."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    condition = soybean_farms["organic"] == True
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms are organic."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All farms with high soil quality index (> 78) grow soybean."""
    high_soil_quality_farms = df[df["soil_quality_index"] > 78]
    condition = high_soil_quality_farms["crop_type"] == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_quality_farms)} farms with high soil quality index grow soybean."
    else:
        viol = high_soil_quality_farms[~condition]
        expl = f"{len(viol)} farms with high soil quality index violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))}, crops: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a farm has high irrigation hours per week (> 17), then it grows either corn or rice."""
    high_irrigation_farms = df[df["irrigation_hours_week"] > 17]
    condition = high_irrigation_farms["crop_type"].isin(["corn", "rice"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation_farms)} farms with high irrigation hours per week grow either corn or rice."
    else:
        viol = high_irrigation_farms[~condition]
        expl = f"{len(viol)} farms with high irrigation hours per week violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))}, crops: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Every farm that grows wheat has a fertilizer usage between 800 and 900 kg."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = wheat_farms["fertilizer_kg"].between(800, 900, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have a fertilizer usage between 800 and 900 kg."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))}, fertilizer usage: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a farm has low acreage (< 100), then it grows either rice or soybean."""
    low_acreage_farms = df[df["acreage"] < 100]
    condition = low_acreage_farms["crop_type"].isin(["rice", "soybean"])
    truth = condition.all()
    if truth:
        expl = f"All {len(low_acreage_farms)} farms with low acreage grow either rice or soybean."
    else:
        viol = low_acreage_farms[~condition]
        expl = f"{len(viol)} farms with low acreage violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))}, crops: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All farms with high yield tons (> 400) have a soil quality index above 70."""
    high_yield_farms = df[df["yield_tons"] > 400]
    condition = high_yield_farms["soil_quality_index"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield_farms)} farms with high yield tons have a soil quality index above 70."
    else:
        viol = high_yield_farms[~condition]
        expl = f"{len(viol)} farms with high yield tons violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))}, soil quality index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a farm grows corn, then it has a higher fertilizer usage than if it grows soybean."""
    corn_farms = df[df["crop_type"] == "corn"]
    soybean_farms = df[df["crop_type"] == "soybean"]
    condition = corn_farms["fertilizer_kg"].mean() > soybean_farms["fertilizer_kg"].mean()
    truth = condition
    if truth:
        expl = f"Corn farms have a higher fertilizer usage than soybean farms."
    else:
        expl = f"Corn farms do not have a higher fertilizer usage than soybean farms."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Every farm that grows rice has a high irrigation hours per week (> 19)."""
    rice_farms = df[df["crop_type"] == "rice"]
    condition = rice_farms["irrigation_hours_week"] > 19
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have a high irrigation hours per week."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))}, irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a farm has a high soil quality index (> 75) and grows wheat, then it has a high yield tons (> 400)."""
    high_soil_quality_wheat_farms = df[(df["soil_quality_index"] > 75) & (df["crop_type"] == "wheat")]
    condition = high_soil_quality_wheat_farms["yield_tons"] > 400
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_quality_wheat_farms)} farms with high soil quality index and growing wheat have a high yield tons."
    else:
        viol = high_soil_quality_wheat_farms[~condition]
        expl = f"{len(viol)} farms with high soil quality index and growing wheat violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))}, yield tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All organic farms have a lower fertilizer usage than non-organic farms."""
    organic_farms = df[df["organic"] == True]
    non_organic_farms = df[df["organic"] == False]
    condition = organic_farms["fertilizer_kg"].mean() < non_organic_farms["fertilizer_kg"].mean()
    truth = condition
    if truth:
        expl = f"Organic farms have a lower fertilizer usage than non-organic farms."
    else:
        expl = f"Organic farms do not have a lower fertilizer usage than non-organic farms."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm has a high yield tons (> 400) and grows soybean, then it has a high soil quality index (> 78)."""
    high_yield_soybean_farms = df[(df["yield_tons"] > 400) & (df["crop_type"] == "soybean")]
    condition = high_yield_soybean_farms["soil_quality_index"] > 78
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield_soybean_farms)} farms with high yield tons and growing soybean have a high soil quality index."
    else:
        viol = high_yield_soybean_farms[~condition]
        expl = f"{len(viol)} farms with high yield tons and growing soybean violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))}, soil quality index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Every farm that grows wheat has a lower irrigation hours per week than farms that grow corn or rice."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    corn_rice_farms = df[df["crop_type"].isin(["corn", "rice"])]
    condition = wheat_farms["irrigation_hours_week"].mean() < corn_rice_farms["irrigation_hours_week"].mean()
    truth = condition
    if truth:
        expl = f"Wheat farms have a lower irrigation hours per week than corn or rice farms."
    else:
        expl = f"Wheat farms do not have a lower irrigation hours per week than corn or rice farms."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a farm has a low soil quality index (< 72), then it grows either rice or wheat."""
    low_soil_quality_farms = df[df["soil_quality_index"] < 72]
    condition = low_soil_quality_farms["crop_type"].isin(["rice", "wheat"])
    truth = condition.all()
    if truth:
        expl = f"All {len(low_soil_quality_farms)} farms with low soil quality index grow either rice or wheat."
    else:
        viol = low_soil_quality_farms[~condition]
        expl = f"{len(viol)} farms with low soil quality index violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))}, crops: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All farms with high fertilizer usage (> 900 kg) grow either corn or rice."""
    high_fertilizer_farms = df[df["fertilizer_kg"] > 900]
    condition = high_fertilizer_farms["crop_type"].isin(["corn", "rice"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fertilizer_farms)} farms with high fertilizer usage grow either corn or rice."
    else:
        viol = high_fertilizer_farms[~condition]
        expl = f"{len(viol)} farms with high fertilizer usage violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))}, crops: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a farm has a high acreage (> 120) and grows soybean, then it has a high yield tons (> 350)."""
    high_acreage_soybean_farms = df[(df["acreage"] > 120) & (df["crop_type"] == "soybean")]
    condition = high_acreage_soybean_farms["yield_tons"] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(high_acreage_soybean_farms)} farms with high acreage and growing soybean have a high yield tons."
    else:
        viol = high_acreage_soybean_farms[~condition]
        expl = f"{len(viol)} farms with high acreage and growing soybean violate the rule (farm_ids: {', '.join(map(str, viol['farm_id'].tolist()))}, yield tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_6.csv")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10), (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()