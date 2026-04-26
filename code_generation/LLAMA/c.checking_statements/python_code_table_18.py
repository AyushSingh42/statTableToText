import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 69."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['soil_quality_index'] > 69
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality index > 69."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows soybean, then its yield is greater than 347 tons."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['yield_tons'] > 347
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have yield > 347 tons."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All farms with irrigation hours per week greater than 15 have a fertilizer usage greater than 700 kg."""
    high_irrigation_farms = df[df['irrigation_hours_week'] > 15]
    condition = high_irrigation_farms['fertilizer_kg'] > 700
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation_farms)} high irrigation farms have fertilizer usage > 700 kg."
    else:
        viol = high_irrigation_farms[~condition]
        expl = f"{len(viol)} high irrigation farms violate the rule (fertilizer usages: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one farm that grows wheat with an acreage less than 120."""
    wheat_farms = df[(df['crop_type'] == 'wheat') & (df['acreage'] < 120)]
    truth = len(wheat_farms) > 0
    if truth:
        expl = f"There are {len(wheat_farms)} wheat farms with acreage < 120."
    else:
        expl = "No wheat farms found with acreage < 120."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a farm grows corn, then its yield is less than 422 tons."""
    corn_farms = df[df['crop_type'] == 'corn']
    condition = corn_farms['yield_tons'] < 422
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have yield < 422 tons."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All farms with a soil quality index greater than 80 have organic crops."""
    high_soil_farms = df[df['soil_quality_index'] > 80]
    condition = high_soil_farms['organic'] == 'yes'
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_farms)} high soil quality farms have organic crops."
    else:
        viol = high_soil_farms[~condition]
        expl = f"{len(viol)} high soil quality farms violate the rule (organic status: {', '.join(map(str, viol['organic'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms have an irrigation hours per week less than 18."""
    total_farms = len(df)
    low_irrigation_farms = df[df['irrigation_hours_week'] < 18]
    truth = len(low_irrigation_farms) > total_farms / 2
    if truth:
        expl = f"{len(low_irrigation_farms)} out of {total_farms} farms have irrigation < 18 hours/week."
    else:
        expl = f"{len(low_irrigation_farms)} out of {total_farms} farms have irrigation < 18 hours/week (less than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a farm grows rice, then its yield is greater than 255 tons."""
    rice_farms = df[df['crop_type'] == 'rice']
    condition = rice_farms['yield_tons'] > 255
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have yield > 255 tons."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All farms with fertilizer usage greater than 1000 kg have a soil quality index greater than 80."""
    high_fert_farms = df[df['fertilizer_kg'] > 1000]
    condition = high_fert_farms['soil_quality_index'] > 80
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert_farms)} high fertilizer farms have soil quality index > 80."
    else:
        viol = high_fert_farms[~condition]
        expl = f"{len(viol)} high fertilizer farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one farm that grows soybean with an acreage less than 120."""
    soybean_farms = df[(df['crop_type'] =='soybean') & (df['acreage'] < 120)]
    truth = len(soybean_farms) > 0
    if truth:
        expl = f"There are {len(soybean_farms)} soybean farms with acreage < 120."
    else:
        expl = "No soybean farms found with acreage < 120."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm grows wheat, then its yield is less than 464 tons."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    condition = wheat_farms['yield_tons'] < 464
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have yield < 464 tons."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All farms with organic crops have a fertilizer usage greater than 626 kg."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['fertilizer_kg'] > 626
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have fertilizer usage > 626 kg."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (fertilizer usages: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most farms have an acreage greater than 100."""
    total_farms = len(df)
    large_acreage_farms = df[df['acreage'] > 100]
    truth = len(large_acreage_farms) > total_farms / 2
    if truth:
        expl = f"{len(large_acreage_farms)} out of {total_farms} farms have acreage > 100."
    else:
        expl = f"{len(large_acreage_farms)} out of {total_farms} farms have acreage > 100 (less than half)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a farm grows corn, then its irrigation hours per week is greater than 11."""
    corn_farms = df[df['crop_type'] == 'corn']
    condition = corn_farms['irrigation_hours_week'] > 11
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have irrigation > 11 hours/week."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All farms with a yield greater than 400 tons have a soil quality index greater than 70."""
    high_yield_farms = df[df['yield_tons'] > 400]
    condition = high_yield_farms['soil_quality_index'] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield_farms)} high yield farms have soil quality index > 70."
    else:
        viol = high_yield_farms[~condition]
        expl = f"{len(viol)} high yield farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one farm that grows rice with an acreage less than 150."""
    rice_farms = df[(df['crop_type'] == 'rice') & (df['acreage'] < 150)]
    truth = len(rice_farms) > 0
    if truth:
        expl = f"There are {len(rice_farms)} rice farms with acreage < 150."
    else:
        expl = "No rice farms found with acreage < 150."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a farm grows soybean, then its soil quality index is greater than 69."""
    soybean_farms = df[df['crop_type'] =='soybean']
    condition = soybean_farms['soil_quality_index'] > 69
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have soil quality index > 69."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All farms with a soil quality index greater than 75 have a fertilizer usage greater than 700 kg."""
    high_soil_farms = df[df['soil_quality_index'] > 75]
    condition = high_soil_farms['fertilizer_kg'] > 700
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_farms)} high soil quality farms have fertilizer usage > 700 kg."
    else:
        viol = high_soil_farms[~condition]
        expl = f"{len(viol)} high soil quality farms violate the rule (fertilizer usages: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_18.csv")

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