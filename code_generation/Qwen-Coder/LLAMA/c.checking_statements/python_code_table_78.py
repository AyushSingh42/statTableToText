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
        expl = f"{len(viol)} organic farms violate the rule (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows soybean, then its yield is less than 450 tons."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['yield_tons'] < 450
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have yield < 450 tons."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm that grows rice with an acreage greater than 120."""
    rice_farms = df[(df['crop_type'] == 'rice') & (df['acreage'] > 120)]
    truth = len(rice_farms) >= 1
    if truth:
        expl = f"There are {len(rice_farms)} rice farms with acreage > 120."
    else:
        expl = "No rice farms found with acreage > 120."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with irrigation hours per week greater than 15, their fertilizer usage is greater than 800 kg."""
    high_irrigation_farms = df[df['irrigation_hours_week'] > 15]
    condition = high_irrigation_farms['fertilizer_kg'] > 800
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation_farms)} high irrigation farms have fertilizer > 800 kg."
    else:
        viol = high_irrigation_farms[~condition]
        expl = f"{len(viol)} high irrigation farms violate the rule (fertilizers: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
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
    """6. If a farm grows corn, then its yield is less than 370 tons."""
    corn_farms = df[df['crop_type'] == 'corn']
    condition = corn_farms['yield_tons'] < 370
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have yield < 370 tons."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all farms with organic crops, their soil quality index is greater than 72."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['soil_quality_index'] > 72
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality index > 72."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one farm that grows soybean with an acreage less than 100 and yield greater than 280 tons."""
    soybean_farms = df[(df['crop_type'] =='soybean') & (df['acreage'] < 100) & (df['yield_tons'] > 280)]
    truth = len(soybean_farms) >= 1
    if truth:
        expl = f"There are {len(soybean_farms)} soybean farms with acreage < 100 and yield > 280 tons."
    else:
        expl = "No soybean farms found with acreage < 100 and yield > 280 tons."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All farms with rice crops have a fertilizer usage greater than 890 kg."""
    rice_farms = df[df['crop_type'] == 'rice']
    condition = rice_farms['fertilizer_kg'] > 890
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have fertilizer > 890 kg."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (fertilizers: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a farm has an acreage greater than 140, then its crop type is either soybean or wheat."""
    large_acreage_farms = df[df['acreage'] > 140]
    condition = large_acreage_farms['crop_type'].isin(['soybean', 'wheat'])
    truth = condition.all()
    if truth:
        expl = f"All {len(large_acreage_farms)} large acreage farms have crop type soybean or wheat."
    else:
        viol = large_acreage_farms[~condition]
        expl = f"{len(viol)} large acreage farms violate the rule (crop types: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. For all farms with irrigation hours per week less than 12, their yield is less than 300 tons."""
    low_irrigation_farms = df[df['irrigation_hours_week'] < 12]
    condition = low_irrigation_farms['yield_tons'] < 300
    truth = condition.all()
    if truth:
        expl = f"All {len(low_irrigation_farms)} low irrigation farms have yield < 300 tons."
    else:
        viol = low_irrigation_farms[~condition]
        expl = f"{len(viol)} low irrigation farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most farms have a soil quality index between 70 and 80."""
    in_range = df[(df['soil_quality_index'] >= 70) & (df['soil_quality_index'] <= 80)]
    total = len(df)
    truth = len(in_range) > total / 2
    if truth:
        expl = f"{len(in_range)} out of {total} farms have soil quality index between 70 and 80."
    else:
        expl = f"{len(in_range)} out of {total} farms have soil quality index between 70 and 80 (less than half)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a farm grows wheat, then its yield is greater than 350 tons."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    condition = wheat_farms['yield_tons'] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have yield > 350 tons."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one farm that grows corn with an acreage greater than 140 and yield less than 300 tons."""
    corn_farms = df[(df['crop_type'] == 'corn') & (df['acreage'] > 140) & (df['yield_tons'] < 300)]
    truth = len(corn_farms) >= 1
    if truth:
        expl = f"There are {len(corn_farms)} corn farms with acreage > 140 and yield < 300 tons."
    else:
        expl = "No corn farms found with acreage > 140 and yield < 300 tons."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All farms with organic crops have an irrigation hours per week greater than 14."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['irrigation_hours_week'] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have irrigation hours > 14."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. For all farms with fertilizer usage greater than 900 kg, their crop type is either rice or corn."""
    high_fertilizer_farms = df[df['fertilizer_kg'] > 900]
    condition = high_fertilizer_farms['crop_type'].isin(['rice', 'corn'])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fertilizer_farms)} high fertilizer farms have crop type rice or corn."
    else:
        viol = high_fertilizer_farms[~condition]
        expl = f"{len(viol)} high fertilizer farms violate the rule (crop types: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a farm has a soil quality index greater than 80, then its crop type is wheat."""
    high_soil_farms = df[df['soil_quality_index'] > 80]
    condition = high_soil_farms['crop_type'] == 'wheat'
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_farms)} high soil quality farms have crop type wheat."
    else:
        viol = high_soil_farms[~condition]
        expl = f"{len(viol)} high soil quality farms violate the rule (crop types: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. There exists at least one farm that grows soybean with a yield greater than 420 tons and acreage less than 120."""
    soybean_farms = df[(df['crop_type'] =='soybean') & (df['yield_tons'] > 420) & (df['acreage'] < 120)]
    truth = len(soybean_farms) >= 1
    if truth:
        expl = f"There are {len(soybean_farms)} soybean farms with yield > 420 tons and acreage < 120."
    else:
        expl = "No soybean farms found with yield > 420 tons and acreage < 120."
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
        (18, stmt_18)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()