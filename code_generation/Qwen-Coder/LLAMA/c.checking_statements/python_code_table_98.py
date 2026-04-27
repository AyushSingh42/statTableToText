import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 68."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['soil_quality_index'] > 68
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality > 68."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows soybean, then its yield is greater than 380 tons."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['yield_tons'] > 380
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have yield > 380 tons."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm with non-organic crops that has a soil quality index greater than 78."""
    non_organic_farms = df[df['organic'] == 'no']
    condition = non_organic_farms['soil_quality_index'] > 78
    truth = condition.any()
    if truth:
        found = non_organic_farms[condition]
        expl = f"Found {len(found)} non-organic farm(s) with soil quality > 78."
    else:
        expl = "No non-organic farms have soil quality > 78."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All farms with irrigation hours per week greater than 14 have a yield greater than 400 tons."""
    high_irrigation_farms = df[df['irrigation_hours_week'] > 14]
    condition = high_irrigation_farms['yield_tons'] > 400
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation_farms)} high irrigation farms have yield > 400 tons."
    else:
        viol = high_irrigation_farms[~condition]
        expl = f"{len(viol)} high irrigation farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a farm grows rice, then its acreage is less than 130."""
    rice_farms = df[df['crop_type'] == 'rice']
    condition = rice_farms['acreage'] < 130
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have acreage < 130."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most farms with organic crops have a fertilizer usage greater than 700 kg."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['fertilizer_kg'] > 700
    count = condition.sum()
    total = len(organic_farms)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of organic farms have fertilizer > 700 kg."
    else:
        expl = f"Less than half ({count}/{total}) of organic farms have fertilizer > 700 kg."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All farms with a soil quality index greater than 80 have organic crops."""
    high_soil_farms = df[df['soil_quality_index'] > 80]
    condition = high_soil_farms['organic'] == 'yes'
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_farms)} high soil quality farms are organic."
    else:
        viol = high_soil_farms[~condition]
        expl = f"{len(viol)} high soil quality farms are not organic (IDs: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a farm grows corn, then its fertilizer usage is greater than 800 kg."""
    corn_farms = df[df['crop_type'] == 'corn']
    condition = corn_farms['fertilizer_kg'] > 800
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have fertilizer > 800 kg."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (fertilizers: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm with non-organic crops that has a yield greater than 450 tons."""
    non_organic_farms = df[df['organic'] == 'no']
    condition = non_organic_farms['yield_tons'] > 450
    truth = condition.any()
    if truth:
        found = non_organic_farms[condition]
        expl = f"Found {len(found)} non-organic farm(s) with yield > 450 tons."
    else:
        expl = "No non-organic farms have yield > 450 tons."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with a yield greater than 420 tons have irrigation hours per week greater than 12."""
    high_yield_farms = df[df['yield_tons'] > 420]
    condition = high_yield_farms['irrigation_hours_week'] > 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield_farms)} high yield farms have irrigation > 12 hrs/week."
    else:
        viol = high_yield_farms[~condition]
        expl = f"{len(viol)} high yield farms violate the rule (irrigation: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm grows wheat, then its acreage is less than 150."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    condition = wheat_farms['acreage'] < 150
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have acreage < 150."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most farms with non-organic crops have a soil quality index less than 75."""
    non_organic_farms = df[df['organic'] == 'no']
    condition = non_organic_farms['soil_quality_index'] < 75
    count = condition.sum()
    total = len(non_organic_farms)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of non-organic farms have soil quality < 75."
    else:
        expl = f"Less than half ({count}/{total}) of non-organic farms have soil quality < 75."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All farms with a fertilizer usage greater than 900 kg have organic crops."""
    high_fert_farms = df[df['fertilizer_kg'] > 900]
    condition = high_fert_farms['organic'] == 'yes'
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert_farms)} high fertilizer farms are organic."
    else:
        viol = high_fert_farms[~condition]
        expl = f"{len(viol)} high fertilizer farms are not organic (IDs: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a farm has a soil quality index greater than 75, then its yield is greater than 350 tons."""
    high_soil_farms = df[df['soil_quality_index'] > 75]
    condition = high_soil_farms['yield_tons'] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_farms)} high soil quality farms have yield > 350 tons."
    else:
        viol = high_soil_farms[~condition]
        expl = f"{len(viol)} high soil quality farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one farm with organic crops that has a yield greater than 450 tons."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['yield_tons'] > 450
    truth = condition.any()
    if truth:
        found = organic_farms[condition]
        expl = f"Found {len(found)} organic farm(s) with yield > 450 tons."
    else:
        expl = "No organic farms have yield > 450 tons."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All farms with irrigation hours per week less than 12 have a yield less than 410 tons."""
    low_irrigation_farms = df[df['irrigation_hours_week'] < 12]
    condition = low_irrigation_farms['yield_tons'] < 410
    truth = condition.all()
    if truth:
        expl = f"All {len(low_irrigation_farms)} low irrigation farms have yield < 410 tons."
    else:
        viol = low_irrigation_farms[~condition]
        expl = f"{len(viol)} low irrigation farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a farm grows soybean, then its fertilizer usage is greater than 750 kg."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['fertilizer_kg'] > 750
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have fertilizer > 750 kg."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (fertilizers: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most farms with a yield greater than 400 tons have a soil quality index greater than 70."""
    high_yield_farms = df[df['yield_tons'] > 400]
    condition = high_yield_farms['soil_quality_index'] > 70
    count = condition.sum()
    total = len(high_yield_farms)
    truth = count > total / 2
    if truth:
        expl = f"More than half ({count}/{total}) of high yield farms have soil quality > 70."
    else:
        expl = f"Less than half ({count}/{total}) of high yield farms have soil quality > 70."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_98.csv")

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