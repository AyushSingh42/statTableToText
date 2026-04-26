import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 70."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['soil_quality_index'] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality index > 70."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows corn, then its yield is greater than 250 tons."""
    corn_farms = df[df['crop_type'] == 'corn']
    condition = corn_farms['yield_tons'] > 250
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have yield > 250 tons."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm that grows soybean with an acreage less than 110."""
    soybean_farms = df[(df['crop_type'] =='soybean') & (df['acreage'] < 110)]
    truth = len(soybean_farms) > 0
    if truth:
        expl = f"There are {len(soybean_farms)} soybean farms with acreage < 110."
    else:
        expl = "No soybean farms found with acreage < 110."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with irrigation hours per week greater than 15, their fertilizer usage is greater than 800 kg."""
    high_irrigation_farms = df[df['irrigation_hours_week'] > 15]
    condition = high_irrigation_farms['fertilizer_kg'] > 800
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation_farms)} high irrigation farms have fertilizer usage > 800 kg."
    else:
        viol = high_irrigation_farms[~condition]
        expl = f"{len(viol)} high irrigation farms violate the rule (fertilizer usages: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms with wheat crops have an acreage greater than 70."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    condition = wheat_farms['acreage'] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have acreage > 70."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a farm grows soybean, then its yield is less than 400 tons."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['yield_tons'] < 400
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have yield < 400 tons."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms with organic crops have an acreage greater than 100."""
    organic_farms = df[df['organic'] == 'yes']
    if len(organic_farms) == 0:
        truth = True
        expl = "No organic farms found."
    else:
        condition = organic_farms['acreage'] > 100
        count = condition.sum()
        truth = count > len(organic_farms) / 2
        if truth:
            expl = f"More than half ({count}/{len(organic_farms)}) of organic farms have acreage > 100."
        else:
            expl = f"Less than half ({count}/{len(organic_farms)}) of organic farms have acreage > 100."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all farms with soil quality index greater than 80, their fertilizer usage is greater than 900 kg."""
    high_soil_farms = df[df['soil_quality_index'] > 80]
    condition = high_soil_farms['fertilizer_kg'] > 900
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_farms)} high soil quality farms have fertilizer usage > 900 kg."
    else:
        viol = high_soil_farms[~condition]
        expl = f"{len(viol)} high soil quality farms violate the rule (fertilizer usages: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm that grows corn with an irrigation hours per week less than 16."""
    corn_farms = df[(df['crop_type'] == 'corn') & (df['irrigation_hours_week'] < 16)]
    truth = len(corn_farms) > 0
    if truth:
        expl = f"There are {len(corn_farms)} corn farms with irrigation hours < 16."
    else:
        expl = "No corn farms found with irrigation hours < 16."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with non-organic crops have a soil quality index less than 82."""
    non_organic_farms = df[df['organic'] == 'no']
    condition = non_organic_farms['soil_quality_index'] < 82
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic_farms)} non-organic farms have soil quality index < 82."
    else:
        viol = non_organic_farms[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm grows wheat, then its yield is greater than 290 tons."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    condition = wheat_farms['yield_tons'] > 290
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have yield > 290 tons."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all farms with acreage greater than 120, their yield is greater than 350 tons."""
    large_acreage_farms = df[df['acreage'] > 120]
    condition = large_acreage_farms['yield_tons'] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(large_acreage_farms)} large acreage farms have yield > 350 tons."
    else:
        viol = large_acreage_farms[~condition]
        expl = f"{len(viol)} large acreage farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most farms with fertilizer usage greater than 700 kg have an irrigation hours per week greater than 12."""
    high_fert_farms = df[df['fertilizer_kg'] > 700]
    if len(high_fert_farms) == 0:
        truth = True
        expl = "No farms with fertilizer usage > 700 kg found."
    else:
        condition = high_fert_farms['irrigation_hours_week'] > 12
        count = condition.sum()
        truth = count > len(high_fert_farms) / 2
        if truth:
            expl = f"More than half ({count}/{len(high_fert_farms)}) of high fertilizer farms have irrigation hours > 12."
        else:
            expl = f"Less than half ({count}/{len(high_fert_farms)}) of high fertilizer farms have irrigation hours > 12."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. For all farms with soil quality index between 70 and 80, their yield is less than 450 tons."""
    mid_soil_farms = df[(df['soil_quality_index'] >= 70) & (df['soil_quality_index'] <= 80)]
    condition = mid_soil_farms['yield_tons'] < 450
    truth = condition.all()
    if truth:
        expl = f"All {len(mid_soil_farms)} mid soil quality farms have yield < 450 tons."
    else:
        viol = mid_soil_farms[~condition]
        expl = f"{len(viol)} mid soil quality farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one farm that grows soybean with a fertilizer usage greater than 1000 kg."""
    soybean_high_fert_farms = df[(df['crop_type'] =='soybean') & (df['fertilizer_kg'] > 1000)]
    truth = len(soybean_high_fert_farms) > 0
    if truth:
        expl = f"There are {len(soybean_high_fert_farms)} soybean farms with fertilizer usage > 1000 kg."
    else:
        expl = "No soybean farms found with fertilizer usage > 1000 kg."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All farms with organic crops have a yield greater than 240 tons."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['yield_tons'] > 240
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have yield > 240 tons."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a farm grows corn, then its irrigation hours per week is greater than 14."""
    corn_farms = df[df['crop_type'] == 'corn']
    condition = corn_farms['irrigation_hours_week'] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have irrigation hours > 14."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. For all farms with yield greater than 400 tons, their acreage is greater than 100."""
    high_yield_farms = df[df['yield_tons'] > 400]
    condition = high_yield_farms['acreage'] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield_farms)} high yield farms have acreage > 100."
    else:
        viol = high_yield_farms[~condition]
        expl = f"{len(viol)} high yield farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. Most farms with irrigation hours per week less than 18 have a fertilizer usage less than 900 kg."""
    low_irrigation_farms = df[df['irrigation_hours_week'] < 18]
    if len(low_irrigation_farms) == 0:
        truth = True
        expl = "No farms with irrigation hours < 18 found."
    else:
        condition = low_irrigation_farms['fertilizer_kg'] < 900
        count = condition.sum()
        truth = count > len(low_irrigation_farms) / 2
        if truth:
            expl = f"More than half ({count}/{len(low_irrigation_farms)}) of low irrigation farms have fertilizer usage < 900 kg."
        else:
            expl = f"Less than half ({count}/{len(low_irrigation_farms)}) of low irrigation farms have fertilizer usage < 900 kg."
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