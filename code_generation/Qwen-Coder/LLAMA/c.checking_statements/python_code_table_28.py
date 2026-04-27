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
        expl = f"All {len(organic_farms)} organic farms have soil quality index > 68."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows rice, then its yield is less than 450 tons."""
    rice_farms = df[df['crop_type'] == 'rice']
    condition = rice_farms['yield_tons'] < 450
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have yield < 450 tons."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all farms with irrigation hours per week greater than 15, their fertilizer usage is greater than 700 kg."""
    high_irrigation = df[df['irrigation_hours_week'] > 15]
    condition = high_irrigation['fertilizer_kg'] > 700
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation)} farms with irrigation > 15 hrs/week have fertilizer > 700 kg."
    else:
        viol = high_irrigation[~condition]
        expl = f"{len(viol)} farms with irrigation > 15 hrs/week violate the rule (fertilizer usages: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one farm that grows corn with a yield greater than 400 tons."""
    corn_high_yield = df[(df['crop_type'] == 'corn') & (df['yield_tons'] > 400)]
    truth = len(corn_high_yield) >= 1
    if truth:
        expl = f"There are {len(corn_high_yield)} corn farms with yield > 400 tons."
    else:
        expl = "No corn farms found with yield > 400 tons."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms with acreage greater than 120 have a yield greater than 350 tons."""
    large_acreage = df[df['acreage'] > 120]
    condition = large_acreage['yield_tons'] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(large_acreage)} farms with acreage > 120 have yield > 350 tons."
    else:
        viol = large_acreage[~condition]
        expl = f"{len(viol)} farms with acreage > 120 violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a farm grows soybean, then its fertilizer usage is greater than 900 kg."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['fertilizer_kg'] > 900
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have fertilizer > 900 kg."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (fertilizer usages: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all farms with soil quality index greater than 79, their yield is greater than 350 tons."""
    high_soil = df[df['soil_quality_index'] > 79]
    condition = high_soil['yield_tons'] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality index > 79 have yield > 350 tons."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms with soil quality index > 79 violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most farms have an irrigation hours per week less than 18."""
    low_irrigation = df[df['irrigation_hours_week'] < 18]
    truth = len(low_irrigation) / len(df) > 0.5
    if truth:
        expl = f"{len(low_irrigation)} out of {len(df)} farms have irrigation < 18 hrs/week (>50% of total)."
    else:
        expl = f"{len(low_irrigation)} out of {len(df)} farms have irrigation < 18 hrs/week (≤50% of total)."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a farm grows wheat, then its yield is greater than 300 tons."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    condition = wheat_farms['yield_tons'] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have yield > 300 tons."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with organic crops have an acreage greater than 70."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['acreage'] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have acreage > 70."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. For all farms with fertilizer usage greater than 1000 kg, their yield is greater than 400 tons."""
    high_fert = df[df['fertilizer_kg'] > 1000]
    condition = high_fert['yield_tons'] > 400
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} farms with fertilizer > 1000 kg have yield > 400 tons."
    else:
        viol = high_fert[~condition]
        expl = f"{len(viol)} farms with fertilizer > 1000 kg violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. There exists at least one farm that grows corn with a soil quality index greater than 80."""
    corn_high_soil = df[(df['crop_type'] == 'corn') & (df['soil_quality_index'] > 80)]
    truth = len(corn_high_soil) >= 1
    if truth:
        expl = f"There are {len(corn_high_soil)} corn farms with soil quality index > 80."
    else:
        expl = "No corn farms found with soil quality index > 80."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All farms with yield greater than 400 tons have an irrigation hours per week greater than 12."""
    high_yield = df[df['yield_tons'] > 400]
    condition = high_yield['irrigation_hours_week'] > 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield)} farms with yield > 400 tons have irrigation > 12 hrs/week."
    else:
        viol = high_yield[~condition]
        expl = f"{len(viol)} farms with yield > 400 tons violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a farm grows rice, then its soil quality index is greater than 68."""
    rice_farms = df[df['crop_type'] == 'rice']
    condition = rice_farms['soil_quality_index'] > 68
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have soil quality index > 68."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. For all farms with acreage less than 100, their fertilizer usage is less than 850 kg."""
    small_acreage = df[df['acreage'] < 100]
    condition = small_acreage['fertilizer_kg'] < 850
    truth = condition.all()
    if truth:
        expl = f"All {len(small_acreage)} farms with acreage < 100 have fertilizer < 850 kg."
    else:
        viol = small_acreage[~condition]
        expl = f"{len(viol)} farms with acreage < 100 violate the rule (fertilizer usages: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. Most farms have a soil quality index greater than 70."""
    high_soil = df[df['soil_quality_index'] > 70]
    truth = len(high_soil) / len(df) > 0.5
    if truth:
        expl = f"{len(high_soil)} out of {len(df)} farms have soil quality index > 70 (>50% of total)."
    else:
        expl = f"{len(high_soil)} out of {len(df)} farms have soil quality index > 70 (≤50% of total)."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a farm grows soybean, then its yield is greater than 300 tons."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['yield_tons'] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have yield > 300 tons."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All farms with irrigation hours per week less than 14 have a yield less than 400 tons."""
    low_irrigation = df[df['irrigation_hours_week'] < 14]
    condition = low_irrigation['yield_tons'] < 400
    truth = condition.all()
    if truth:
        expl = f"All {len(low_irrigation)} farms with irrigation < 14 hrs/week have yield < 400 tons."
    else:
        viol = low_irrigation[~condition]
        expl = f"{len(viol)} farms with irrigation < 14 hrs/week violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_28.csv")

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