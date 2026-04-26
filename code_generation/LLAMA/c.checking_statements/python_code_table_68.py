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
    """2. If a farm grows corn, then its yield is greater than 285 tons."""
    corn_farms = df[df['crop_type'] == 'corn']
    condition = corn_farms['yield_tons'] > 285
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have yield > 285 tons."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm that grows soybean with an irrigation time of less than 18 hours per week."""
    soybean_farms = df[(df['crop_type'] =='soybean') & (df['irrigation_hours_week'] < 18)]
    truth = len(soybean_farms) >= 1
    if truth:
        expl = f"There are {len(soybean_farms)} soybean farms with irrigation < 18 hours/week."
    else:
        expl = "No soybean farms found with irrigation < 18 hours/week."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with a soil quality index greater than 80, their fertilizer usage is less than 800 kg."""
    high_soil_farms = df[df['soil_quality_index'] > 80]
    condition = high_soil_farms['fertilizer_kg'] < 800
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_farms)} high-soil-quality farms use < 800 kg fertilizer."
    else:
        viol = high_soil_farms[~condition]
        expl = f"{len(viol)} high-soil-quality farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a farm grows rice, then its acreage is less than 120."""
    rice_farms = df[df['crop_type'] == 'rice']
    condition = rice_farms['acreage'] < 120
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have acreage < 120."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All farms with non-organic crops have a soil quality index less than 83."""
    non_organic_farms = df[df['organic'] == 'no']
    condition = non_organic_farms['soil_quality_index'] < 83
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic_farms)} non-organic farms have soil quality < 83."
    else:
        viol = non_organic_farms[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (soil quality: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms have an irrigation time of less than 20 hours per week."""
    total_farms = len(df)
    low_irrigation_farms = df[df['irrigation_hours_week'] < 20]
    truth = len(low_irrigation_farms) > total_farms / 2
    if truth:
        expl = f"{len(low_irrigation_farms)} out of {total_farms} farms have irrigation < 20 hours/week."
    else:
        expl = f"{len(low_irrigation_farms)} out of {total_farms} farms have irrigation < 20 hours/week (not majority)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a farm grows wheat, then its yield is greater than 315 tons."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    condition = wheat_farms['yield_tons'] > 315
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have yield > 315 tons."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm that grows corn with an irrigation time of greater than 20 hours per week."""
    corn_farms = df[(df['crop_type'] == 'corn') & (df['irrigation_hours_week'] > 20)]
    truth = len(corn_farms) >= 1
    if truth:
        expl = f"There are {len(corn_farms)} corn farms with irrigation > 20 hours/week."
    else:
        expl = "No corn farms found with irrigation > 20 hours/week."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. For all farms with a fertilizer usage greater than 900 kg, their yield is greater than 400 tons."""
    high_fert_farms = df[df['fertilizer_kg'] > 900]
    condition = high_fert_farms['yield_tons'] > 400
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert_farms)} high-fertilizer farms have yield > 400 tons."
    else:
        viol = high_fert_farms[~condition]
        expl = f"{len(viol)} high-fertilizer farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All farms with organic crops have an irrigation time of less than 20 hours per week."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['irrigation_hours_week'] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have irrigation < 20 hours/week."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (irrigation: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a farm grows soybean, then its acreage is greater than 100."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['acreage'] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have acreage > 100."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. There exists at least one farm that grows rice with a soil quality index greater than 80."""
    rice_farms = df[(df['crop_type'] == 'rice') & (df['soil_quality_index'] > 80)]
    truth = len(rice_farms) >= 1
    if truth:
        expl = f"There are {len(rice_farms)} rice farms with soil quality > 80."
    else:
        expl = "No rice farms found with soil quality > 80."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. For all farms with a yield greater than 400 tons, their fertilizer usage is greater than 700 kg."""
    high_yield_farms = df[df['yield_tons'] > 400]
    condition = high_yield_farms['fertilizer_kg'] > 700
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield_farms)} high-yield farms use > 700 kg fertilizer."
    else:
        viol = high_yield_farms[~condition]
        expl = f"{len(viol)} high-yield farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most farms have a soil quality index greater than 70."""
    total_farms = len(df)
    high_soil_farms = df[df['soil_quality_index'] > 70]
    truth = len(high_soil_farms) > total_farms / 2
    if truth:
        expl = f"{len(high_soil_farms)} out of {total_farms} farms have soil quality > 70."
    else:
        expl = f"{len(high_soil_farms)} out of {total_farms} farms have soil quality > 70 (not majority)."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a farm grows wheat, then its acreage is greater than 85."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    condition = wheat_farms['acreage'] > 85
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have acreage > 85."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. There exists at least one farm that grows corn with a yield greater than 400 tons."""
    corn_farms = df[(df['crop_type'] == 'corn') & (df['yield_tons'] > 400)]
    truth = len(corn_farms) >= 1
    if truth:
        expl = f"There are {len(corn_farms)} corn farms with yield > 400 tons."
    else:
        expl = "No corn farms found with yield > 400 tons."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. For all farms with an irrigation time of less than 15 hours per week, their yield is less than 350 tons."""
    low_irrigation_farms = df[df['irrigation_hours_week'] < 15]
    condition = low_irrigation_farms['yield_tons'] < 350
    truth = condition.all()
    if truth:
        expl = f"All {len(low_irrigation_farms)} low-irrigation farms have yield < 350 tons."
    else:
        viol = low_irrigation_farms[~condition]
        expl = f"{len(viol)} low-irrigation farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All farms with non-organic crops have a fertilizer usage greater than 600 kg."""
    non_organic_farms = df[df['organic'] == 'no']
    condition = non_organic_farms['fertilizer_kg'] > 600
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic_farms)} non-organic farms use > 600 kg fertilizer."
    else:
        viol = non_organic_farms[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_68.csv")

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