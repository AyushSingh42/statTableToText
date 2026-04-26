import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 72."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['soil_quality_index'] > 72
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality index > 72."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows soybean, then its yield is less than 460 tons."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['yield_tons'] < 460
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have yield < 460 tons."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm that grows wheat with an acreage less than 110."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    condition = wheat_farms['acreage'] < 110
    truth = condition.any()
    if truth:
        expl = f"At least one wheat farm has acreage < 110."
    else:
        expl = f"No wheat farms have acreage < 110."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with irrigation hours per week greater than 14, their fertilizer usage is greater than 900 kg."""
    high_irrigation_farms = df[df['irrigation_hours_week'] > 14]
    condition = high_irrigation_farms['fertilizer_kg'] > 900
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation_farms)} high irrigation farms have fertilizer > 900 kg."
    else:
        viol = high_irrigation_farms[~condition]
        expl = f"{len(viol)} high irrigation farms violate the rule (fertilizer usages: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms with corn crops have an acreage greater than 90."""
    corn_farms = df[df['crop_type'] == 'corn']
    condition = corn_farms['acreage'] > 90
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have acreage > 90."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a farm grows rice, then its soil quality index is less than 74."""
    rice_farms = df[df['crop_type'] == 'rice']
    condition = rice_farms['soil_quality_index'] < 74
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have soil quality index < 74."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms with organic crops have an acreage greater than 100."""
    organic_farms = df[df['organic'] == 'yes']
    if len(organic_farms) == 0:
        truth = True
        expl = "No organic farms exist."
    else:
        condition = organic_farms['acreage'] > 100
        count_greater = condition.sum()
        truth = count_greater > len(organic_farms) / 2
        if truth:
            expl = f"More than half ({count_greater}/{len(organic_farms)}) of organic farms have acreage > 100."
        else:
            expl = f"Less than half ({count_greater}/{len(organic_farms)}) of organic farms have acreage > 100."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all farms with yield greater than 400 tons, their irrigation hours per week are greater than 12."""
    high_yield_farms = df[df['yield_tons'] > 400]
    condition = high_yield_farms['irrigation_hours_week'] > 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield_farms)} high yield farms have irrigation hours > 12."
    else:
        viol = high_yield_farms[~condition]
        expl = f"{len(viol)} high yield farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm that grows soybean with an acreage less than 80."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['acreage'] < 80
    truth = condition.any()
    if truth:
        expl = f"At least one soybean farm has acreage < 80."
    else:
        expl = f"No soybean farms have acreage < 80."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with wheat crops have a fertilizer usage greater than 550 kg."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    condition = wheat_farms['fertilizer_kg'] > 550
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have fertilizer > 550 kg."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (fertilizer usages: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm has an acreage greater than 130, then its crop type is not rice."""
    large_acreage_farms = df[df['acreage'] > 130]
    condition = large_acreage_farms['crop_type']!= 'rice'
    truth = condition.all()
    if truth:
        expl = f"All {len(large_acreage_farms)} large acreage farms do not grow rice."
    else:
        viol = large_acreage_farms[~condition]
        expl = f"{len(viol)} large acreage farms grow rice (crop types: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all farms with soil quality index greater than 80, their organic status is yes."""
    high_soil_farms = df[df['soil_quality_index'] > 80]
    condition = high_soil_farms['organic'] == 'yes'
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_farms)} high soil quality farms are organic."
    else:
        viol = high_soil_farms[~condition]
        expl = f"{len(viol)} high soil quality farms are not organic (organic statuses: {', '.join(map(str, viol['organic'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most farms with corn crops have a yield less than 380 tons."""
    corn_farms = df[df['crop_type'] == 'corn']
    if len(corn_farms) == 0:
        truth = True
        expl = "No corn farms exist."
    else:
        condition = corn_farms['yield_tons'] < 380
        count_less = condition.sum()
        truth = count_less > len(corn_farms) / 2
        if truth:
            expl = f"More than half ({count_less}/{len(corn_farms)}) of corn farms have yield < 380 tons."
        else:
            expl = f"Less than half ({count_less}/{len(corn_farms)}) of corn farms have yield < 380 tons."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one farm that grows corn with an irrigation hours per week greater than 16."""
    corn_farms = df[df['crop_type'] == 'corn']
    condition = corn_farms['irrigation_hours_week'] > 16
    truth = condition.any()
    if truth:
        expl = f"At least one corn farm has irrigation hours > 16."
    else:
        expl = f"No corn farms have irrigation hours > 16."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All farms with fertilizer usage greater than 1000 kg have an organic status of no."""
    high_fert_farms = df[df['fertilizer_kg'] > 1000]
    condition = high_fert_farms['organic'] == 'no'
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert_farms)} high fertilizer farms are non-organic."
    else:
        viol = high_fert_farms[~condition]
        expl = f"{len(viol)} high fertilizer farms are organic (organic statuses: {', '.join(map(str, viol['organic'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a farm grows soybean, then its soil quality index is less than 80."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['soil_quality_index'] < 80
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have soil quality index < 80."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. For all farms with yield less than 300 tons, their crop type is not soybean."""
    low_yield_farms = df[df['yield_tons'] < 300]
    condition = low_yield_farms['crop_type']!='soybean'
    truth = condition.all()
    if truth:
        expl = f"All {len(low_yield_farms)} low yield farms do not grow soybean."
    else:
        viol = low_yield_farms[~condition]
        expl = f"{len(viol)} low yield farms grow soybean (crop types: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. There exists at least one farm that grows wheat with a yield greater than 440 tons."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    condition = wheat_farms['yield_tons'] > 440
    truth = condition.any()
    if truth:
        expl = f"At least one wheat farm has yield > 440 tons."
    else:
        expl = f"No wheat farms have yield > 440 tons."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All farms with irrigation hours per week less than 12 have a fertilizer usage less than 600 kg."""
    low_irrigation_farms = df[df['irrigation_hours_week'] < 12]
    condition = low_irrigation_farms['fertilizer_kg'] < 600
    truth = condition.all()
    if truth:
        expl = f"All {len(low_irrigation_farms)} low irrigation farms have fertilizer < 600 kg."
    else:
        viol = low_irrigation_farms[~condition]
        expl = f"{len(viol)} low irrigation farms violate the rule (fertilizer usages: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_58.csv")

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
        (19, stmt_19)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()