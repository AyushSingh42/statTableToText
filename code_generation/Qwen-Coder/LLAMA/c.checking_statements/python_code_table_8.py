import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 78."""
    organic_farms = df[df['organic'] == 'yes']
    condition = organic_farms['soil_quality_index'] > 78
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality index > 78."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows rice, then its irrigation hours per week are less than 21."""
    rice_farms = df[df['crop_type'] == 'rice']
    if len(rice_farms) == 0:
        return True, "No farms grow rice."
    condition = rice_farms['irrigation_hours_week'] < 21
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have irrigation hours < 21."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm that grows soybean with an acreage greater than 140."""
    soybean_farms = df[(df['crop_type'] =='soybean') & (df['acreage'] > 140)]
    truth = len(soybean_farms) > 0
    if truth:
        expl = f"There are {len(soybean_farms)} soybean farms with acreage > 140."
    else:
        expl = "No soybean farms have acreage > 140."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with wheat crops, if the acreage is greater than 100, then the yield is less than 350 tons."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    if len(wheat_farms) == 0:
        return True, "No farms grow wheat."
    condition = (wheat_farms['acreage'] <= 100) | (wheat_farms['yield_tons'] < 350)
    truth = condition.all()
    if truth:
        expl = f"All wheat farms satisfy the condition."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (acreage > 100 but yield >= 350)."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms with fertilizer usage greater than 900 kg have a yield greater than 300 tons."""
    high_fert_farms = df[df['fertilizer_kg'] > 900]
    if len(high_fert_farms) == 0:
        return True, "No farms have fertilizer usage > 900 kg."
    condition = high_fert_farms['yield_tons'] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert_farms)} high-fertilizer farms have yield > 300 tons."
    else:
        viol = high_fert_farms[~condition]
        expl = f"{len(viol)} high-fertilizer farms violate the rule (yield <= 300)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a farm grows rice and has an acreage greater than 100, then its yield is greater than 300 tons."""
    rice_farms = df[(df['crop_type'] == 'rice') & (df['acreage'] > 100)]
    if len(rice_farms) == 0:
        return True, "No rice farms have acreage > 100."
    condition = rice_farms['yield_tons'] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms with acreage > 100 have yield > 300 tons."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms with acreage > 100 violate the rule (yield <= 300)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms with organic crops have a fertilizer usage greater than 900 kg."""
    organic_farms = df[df['organic'] == 'yes']
    if len(organic_farms) == 0:
        return True, "No organic farms exist."
    high_fert_count = (organic_farms['fertilizer_kg'] > 900).sum()
    total_count = len(organic_farms)
    truth = high_fert_count > total_count / 2
    if truth:
        expl = f"More than half ({high_fert_count}/{total_count}) of organic farms have fertilizer > 900 kg."
    else:
        expl = f"Less than half ({high_fert_count}/{total_count}) of organic farms have fertilizer > 900 kg."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all farms with soybean crops, if the acreage is greater than 90, then the yield is greater than 250 tons."""
    soybean_farms = df[df['crop_type'] =='soybean']
    if len(soybean_farms) == 0:
        return True, "No farms grow soybean."
    condition = (soybean_farms['acreage'] <= 90) | (soybean_farms['yield_tons'] > 250)
    truth = condition.all()
    if truth:
        expl = f"All soybean farms satisfy the condition."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (acreage > 90 but yield <= 250)."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm that grows wheat with an irrigation hours per week less than 14."""
    wheat_farms = df[(df['crop_type'] == 'wheat') & (df['irrigation_hours_week'] < 14)]
    truth = len(wheat_farms) > 0
    if truth:
        expl = f"There are {len(wheat_farms)} wheat farms with irrigation hours < 14."
    else:
        expl = "No wheat farms have irrigation hours < 14."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with a soil quality index greater than 80 have a yield greater than 250 tons."""
    high_soil_farms = df[df['soil_quality_index'] > 80]
    if len(high_soil_farms) == 0:
        return True, "No farms have soil quality index > 80."
    condition = high_soil_farms['yield_tons'] > 250
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_farms)} high-soil-quality farms have yield > 250 tons."
    else:
        viol = high_soil_farms[~condition]
        expl = f"{len(viol)} high-soil-quality farms violate the rule (yield <= 250)."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm grows rice and has an irrigation hours per week greater than 16, then its yield is greater than 350 tons."""
    rice_farms = df[(df['crop_type'] == 'rice') & (df['irrigation_hours_week'] > 16)]
    if len(rice_farms) == 0:
        return True, "No rice farms have irrigation hours > 16."
    condition = rice_farms['yield_tons'] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms with irrigation hours > 16 have yield > 350 tons."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms with irrigation hours > 16 violate the rule (yield <= 350)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all farms with wheat crops, if the fertilizer usage is greater than 700 kg, then the yield is greater than 300 tons."""
    wheat_farms = df[df['crop_type'] == 'wheat']
    if len(wheat_farms) == 0:
        return True, "No farms grow wheat."
    condition = (wheat_farms['fertilizer_kg'] <= 700) | (wheat_farms['yield_tons'] > 300)
    truth = condition.all()
    if truth:
        expl = f"All wheat farms satisfy the condition."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (fertilizer > 700 but yield <= 300)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most farms with non-organic crops have a soil quality index less than 80."""
    non_organic_farms = df[df['organic'] == 'no']
    if len(non_organic_farms) == 0:
        return True, "No non-organic farms exist."
    low_soil_count = (non_organic_farms['soil_quality_index'] < 80).sum()
    total_count = len(non_organic_farms)
    truth = low_soil_count > total_count / 2
    if truth:
        expl = f"More than half ({low_soil_count}/{total_count}) of non-organic farms have soil quality index < 80."
    else:
        expl = f"Less than half ({low_soil_count}/{total_count}) of non-organic farms have soil quality index < 80."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one farm that grows soybean with a fertilizer usage greater than 900 kg."""
    soybean_farms = df[(df['crop_type'] =='soybean') & (df['fertilizer_kg'] > 900)]
    truth = len(soybean_farms) > 0
    if truth:
        expl = f"There are {len(soybean_farms)} soybean farms with fertilizer > 900 kg."
    else:
        expl = "No soybean farms have fertilizer > 900 kg."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All farms with an acreage greater than 120 have a yield greater than 300 tons."""
    large_farms = df[df['acreage'] > 120]
    if len(large_farms) == 0:
        return True, "No farms have acreage > 120."
    condition = large_farms['yield_tons'] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(large_farms)} large farms have yield > 300 tons."
    else:
        viol = large_farms[~condition]
        expl = f"{len(viol)} large farms violate the rule (yield <= 300)."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a farm grows wheat and has an acreage greater than 80, then its yield is greater than 250 tons."""
    wheat_farms = df[(df['crop_type'] == 'wheat') & (df['acreage'] > 80)]
    if len(wheat_farms) == 0:
        return True, "No wheat farms have acreage > 80."
    condition = wheat_farms['yield_tons'] > 250
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms with acreage > 80 have yield > 250 tons."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms with acreage > 80 violate the rule (yield <= 250)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_8.csv")

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
        (16, stmt_16)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()