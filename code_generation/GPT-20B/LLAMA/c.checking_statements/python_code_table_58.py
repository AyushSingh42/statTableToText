import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 72."""
    organic_farms = df[df["organic"] == "yes"]
    condition = organic_farms["soil_quality_index"] > 72
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality index > 72."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows soybean, then its yield is less than 460 tons."""
    soy_farms = df[df["crop_type"] == "soybean"]
    condition = soy_farms["yield_tons"] < 460
    truth = condition.all()
    if truth:
        expl = f"All {len(soy_farms)} soybean farms have yield < 460 tons."
    else:
        viol = soy_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm that grows wheat with an acreage less than 110."""
    wheat_small = df[(df["crop_type"] == "wheat") & (df["acreage"] < 110)]
    truth = not wheat_small.empty
    if truth:
        expl = f"Found {len(wheat_small)} wheat farm(s) with acreage < 110 (IDs: {', '.join(map(str, wheat_small['farm_id']))})."
    else:
        expl = "No wheat farm with acreage < 110 found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with irrigation hours per week greater than 14, their fertilizer usage is greater than 900 kg."""
    high_irrig = df[df["irrigation_hours_week"] > 14]
    condition = high_irrig["fertilizer_kg"] > 900
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrig)} farms with irrigation > 14 hrs have fertilizer > 900 kg."
    else:
        viol = high_irrig[~condition]
        expl = f"{len(viol)} farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms with corn crops have an acreage greater than 90."""
    corn_farms = df[df["crop_type"] == "corn"]
    condition = corn_farms["acreage"] > 90
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have acreage > 90."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (acres: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a farm grows rice, then its soil quality index is less than 74."""
    rice_farms = df[df["crop_type"] == "rice"]
    condition = rice_farms["soil_quality_index"] < 74
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have soil quality index < 74."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms with organic crops have an acreage greater than 100."""
    organic_farms = df[df["organic"] == "yes"]
    total = len(organic_farms)
    if total == 0:
        truth = False
        expl = "No organic farms to evaluate."
    else:
        count = (organic_farms["acreage"] > 100).sum()
        ratio = count / total
        truth = ratio > 0.5
        expl = f"{count} out of {total} organic farms have acreage > 100 (ratio: {ratio:.2f})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all farms with yield greater than 400 tons, their irrigation hours per week are greater than 12."""
    high_yield = df[df["yield_tons"] > 400]
    condition = high_yield["irrigation_hours_week"] > 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield)} farms with yield > 400 tons have irrigation > 12 hrs."
    else:
        viol = high_yield[~condition]
        expl = f"{len(viol)} farms violate the rule (irrigation: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm that grows soybean with an acreage less than 80."""
    soy_small = df[(df["crop_type"] == "soybean") & (df["acreage"] < 80)]
    truth = not soy_small.empty
    if truth:
        expl = f"Found {len(soy_small)} soybean farm(s) with acreage < 80 (IDs: {', '.join(map(str, soy_small['farm_id']))})."
    else:
        expl = "No soybean farm with acreage < 80 found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with wheat crops have a fertilizer usage greater than 550 kg."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = wheat_farms["fertilizer_kg"] > 550
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have fertilizer > 550 kg."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm has an acreage greater than 130, then its crop type is not rice."""
    large_farms = df[df["acreage"] > 130]
    condition = large_farms["crop_type"]!= "rice"
    truth = condition.all()
    if truth:
        expl = f"All {len(large_farms)} farms with acreage > 130 are not rice."
    else:
        viol = large_farms[~condition]
        expl = f"{len(viol)} farms violate the rule (crop types: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all farms with soil quality index greater than 80, their organic status is yes."""
    high_soil = df[df["soil_quality_index"] > 80]
    condition = high_soil["organic"] == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality index > 80 have organic status yes."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms violate the rule (organic statuses: {', '.join(map(str, viol['organic'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most farms with corn crops have a yield less than 380 tons."""
    corn_farms = df[df["crop_type"] == "corn"]
    total = len(corn_farms)
    if total == 0:
        truth = False
        expl = "No corn farms to evaluate."
    else:
        count = (corn_farms["yield_tons"] < 380).sum()
        ratio = count / total
        truth = ratio > 0.5
        expl = f"{count} out of {total} corn farms have yield < 380 tons (ratio: {ratio:.2f})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one farm that grows corn with an irrigation hours per week greater than 16."""
    corn_high_irrig = df[(df["crop_type"] == "corn") & (df["irrigation_hours_week"] > 16)]
    truth = not corn_high_irrig.empty
    if truth:
        expl = f"Found {len(corn_high_irrig)} corn farm(s) with irrigation > 16 hrs (IDs: {', '.join(map(str, corn_high_irrig['farm_id']))})."
    else:
        expl = "No corn farm with irrigation > 16 hrs found."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All farms with fertilizer usage greater than 1000 kg have an organic status of no."""
    high_fert = df[df["fertilizer_kg"] > 1000]
    condition = high_fert["organic"] == "no"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} farms with fertilizer > 1000 kg have organic status no."
    else:
        viol = high_fert[~condition]
        expl = f"{len(viol)} farms violate the rule (organic statuses: {', '.join(map(str, viol['organic'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a farm grows soybean, then its soil quality index is less than 80."""
    soy_farms = df[df["crop_type"] == "soybean"]
    condition = soy_farms["soil_quality_index"] < 80
    truth = condition.all()
    if truth:
        expl = f"All {len(soy_farms)} soybean farms have soil quality index < 80."
    else:
        viol = soy_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. For all farms with yield less than 300 tons, their crop type is not soybean."""
    low_yield = df[df["yield_tons"] < 300]
    condition = low_yield["crop_type"]!= "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(low_yield)} farms with yield < 300 tons are not soybean."
    else:
        viol = low_yield[~condition]
        expl = f"{len(viol)} farms violate the rule (crop types: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. There exists at least one farm that grows wheat with a yield greater than 440 tons."""
    wheat_high_yield = df[(df["crop_type"] == "wheat") & (df["yield_tons"] > 440)]
    truth = not wheat_high_yield.empty
    if truth:
        expl = f"Found {len(wheat_high_yield)} wheat farm(s) with yield > 440 tons (IDs: {', '.join(map(str, wheat_high_yield['farm_id']))})."
    else:
        expl = "No wheat farm with yield > 440 tons found."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All farms with irrigation hours per week less than 12 have a fertilizer usage less than 600 kg."""
    low_irrig = df[df["irrigation_hours_week"] < 12]
    condition = low_irrig["fertilizer_kg"] < 600
    truth = condition.all()
    if truth:
        expl = f"All {len(low_irrig)} farms with irrigation < 12 hrs have fertilizer < 600 kg."
    else:
        viol = low_irrig[~condition]
        expl = f"{len(viol)} farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_58.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col not in ["farm_id", "crop_type", "organic"]:
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
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
        (18, stmt_18),
        (19, stmt_19),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()