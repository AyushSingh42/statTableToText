

import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All organic farms are soybean farms, and all soybean farms are organic."""
    organic = df[df['organic'] == True]
    soybean = df[df['crop_type'] =='soybean']
    cond1 = organic['crop_type'] =='soybean'
    cond2 = soybean['organic'] == True
    truth1 = cond1.all() if not organic.empty else True
    truth2 = cond2.all() if not soybean.empty else True
    truth = truth1 and truth2
    viol1 = organic[~cond1] if not organic.empty else pd.DataFrame()
    viol2 = soybean[~cond2] if not soybean.empty else pd.DataFrame()
    expl = ""
    if not truth1:
        expl += f"{len(viol1)} organic farms are not soybean."
    if not truth2:
        if expl:
            expl += " "
        expl += f"{len(viol2)} soybean farms are not organic."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For non-organic corn farms, higher fertilizer usage correlates with higher yield per acre (r ≈ 0.98)."""
    non_organic_corn = df[(df['crop_type'] == 'corn') & (df['organic'] == False)]
    if non_organic_corn.empty:
        return True, "No non-organic corn farms exist."
    yield_per_acre = non_organic_corn['yield_tons'] / non_organic_corn['acreage']
    corr = yield_per_acre.corr(non_organic_corn['fertilizer_kg'])
    if len(non_organic_corn) < 2:
        return True, "Insufficient data points."
    truth = abs(corr - 0.98) < 0.01
    expl = f"Correlation is {corr:.2f}, {'≈0.98' if truth else 'not ≈0.98'}."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Rice farms require the most irrigation hours per week (≥19.2) compared to any other crop type."""
    rice = df[df['crop_type'] == 'rice']
    others = df[df['crop_type']!= 'rice']
    cond1 = rice['irrigation_hours_week'] >= 19.2
    cond2 = others['irrigation_hours_week'] < 19.2
    truth1 = cond1.all() if not rice.empty else True
    truth2 = cond2.all() if not others.empty else True
    viol1 = rice[~cond1] if not rice.empty else pd.DataFrame()
    viol2 = others[~cond2] if not others.empty else pd.DataFrame()
    expl = ""
    if not truth1:
        expl += f"{len(viol1)} rice farms have <19.2 irrigation hours."
    if not truth2:
        if expl:
            expl += " "
        expl += f"{len(viol2)} non-rice farms have ≥19.2 irrigation hours."
    return truth1 and truth2, expl

def stmt_4(df: pd.DataFrame):
    """4. If a farm uses more than 900 kg of fertilizer, it must be either corn or rice."""
    high_fertilizer = df[df['fertilizer_kg'] > 900]
    valid_crops = high_fertilizer['crop_type'].isin(['corn', 'rice'])
    truth = valid_crops.all() if not high_fertilizer.empty else True
    viol = high_fertilizer[~valid_crops] if not high_fertilizer.empty else pd.DataFrame()
    expl = f"{len(viol)} farms violate the rule." if not truth else "All high-fertilizer farms are corn/rice."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Soybean farms have the lowest yield per acre (≤2.72) among all crops."""
    soybean = df[df['crop_type'] =='soybean']
    others = df[df['crop_type']!='soybean']
    soybean_yield = soybean['yield_tons'] / soybean['acreage']
    cond1 = soybean_yield <= 2.72
    truth1 = cond1.all() if not soybean.empty else True
    if not truth1:
        viol = soybean[~cond1] if not soybean.empty else pd.DataFrame()
        return False, f"{len(viol)} soybean farms exceed 2.72 yield per acre."
    soybean_max = soybean_yield.max()
    others_yield = others['yield_tons'] / others['acreage']
    cond2 = others_yield > soybean_max
    truth2 = cond2.all() if not others.empty else True
    viol = others[~cond2] if not others.empty else pd.DataFrame()
    expl = "Soybean max yield per acre is ≤2.72 and others are higher." if truth2 else f"{len(viol)} other crops have yield per acre ≤{soybean_max:.2f}."
    return truth1 and truth2, expl

def stmt_6(df: pd.DataFrame):
    """6. All farms with soil quality index >80 are organic soybean farms."""
    high_soil = df[df['soil_quality_index'] > 80]
    cond1 = high_soil['organic'] == True
    cond2 = high_soil['crop_type'] =='soybean'
    truth1 = cond1.all() if not high_soil.empty else True
    truth2 = cond2.all() if not high_soil.empty else True
    viol = high_soil[(~cond1) | (~cond2)] if not high_soil.empty else pd.DataFrame()
    expl = f"{len(viol)} farms violate the condition." if not truth1 or not truth2 else "All high-soil farms are organic soybean."
    return truth1 and truth2, expl

def stmt_7(df: pd.DataFrame):
    """7. For non-organic wheat farms, yield per acre decreases as irrigation hours drop below 14."""
    non_organic_wheat = df[(df['crop_type'] == 'wheat') & (df['organic'] == False)]
    low_irrigation = non_organic_wheat[non_organic_wheat['irrigation_hours_week'] < 14]
    if low_irrigation.empty:
        return True, "No non-organic wheat farms with irrigation <14."
    yield_per_acre = low_irrigation['yield_tons'] / low_irrigation['acreage']
    corr = yield_per_acre.corr(low_irrigation['irrigation_hours_week'])
    truth = corr < 0 if len(low_irrigation) >= 2 else True
    expl = f"Correlation is {corr:.2f}, {'negative' if truth else 'not negative'}."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. The highest fertilizer usage (1015 kg) occurs in a corn farm with the highest yield among its crop type."""
    max_fertilizer = df['fertilizer_kg'].max()
    if max_fertilizer!= 1015:
        return False, "Highest fertilizer is not 1015 kg."
    high_fertilizer_farm = df[df['fertilizer_kg'] == 1015]
    cond_crop = high_fertilizer_farm['crop_type'] == 'corn'
    if not cond_crop.all():
        return False, "Highest fertilizer farm is not corn."
    corn_farms = df[df['crop_type'] == 'corn']
    max_yield_corn = corn_farms['yield_tons'].max()
    high_fertilizer_yield = high_fertilizer_farm['yield_tons'].values[0]
    truth = high_fertilizer_yield == max_yield_corn
    expl = "Highest fertilizer corn farm has highest yield." if truth else "Highest fertilizer corn farm does not have highest yield."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Organic soybean farms have higher soil quality indices than non-organic corn farms."""
    organic_soybean = df[(df['crop_type'] =='soybean') & (df['organic'] == True)]
    non_organic_corn = df[(df['crop_type'] == 'corn') & (df['organic'] == False)]
    if organic_soybean.empty or non_organic_corn.empty:
        return True, "No data to compare."
    cond = organic_soybean['soil_quality_index'].min() > non_organic_corn['soil_quality_index'].max()
    truth = cond
    expl = "All organic soybean soil indices are higher than non-organic corn's." if truth else "Some organic soybean soil indices are ≤ non-organic corn's max."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a farm’s irrigation hours exceed 18, it must be a rice farm."""
    high_irrigation = df[df['irrigation_hours_week'] > 18]
    cond = high_irrigation['crop_type'] == 'rice'
    truth = cond.all() if not high_irrigation.empty else True
    viol = high_irrigation[~cond] if not high_irrigation.empty else pd.DataFrame()
    expl = f"{len(viol)} farms violate the rule." if not truth else "All high-irrigation farms are rice."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Non-organic rice farms have the lowest soil quality indices (≤70.2) among all non-organic crops."""
    non_organic_rice = df[(df['crop_type'] == 'rice') & (df['organic'] == False)]
    other_non_organic = df[(df['organic'] == False) & (df['crop_type']!= 'rice')]
    cond1 = non_organic_rice['soil_quality_index'] <= 70.2
    cond2 = other_non_organic['soil_quality_index'] > 70.2
    truth1 = cond1.all() if not non_organic_rice.empty else True
    truth2 = cond2.all() if not other_non_organic.empty else True
    viol1 = non_organic_rice[~cond1] if not non_organic_rice.empty else pd.DataFrame()
    viol2 = other_non_organic[~cond2] if not other_non_organic.empty else pd.DataFrame()
    expl = ""
    if not truth1:
        expl += f"{len(viol1)} non-organic rice farms have soil >70.2."
    if not truth2:
        if expl:
            expl += " "
        expl += f"{len(viol2)} other non-organic farms have soil ≤70.2."
    return truth1 and truth2, expl

def stmt_12(df: pd.DataFrame):
    """12. For soybean farms, yield per acre increases with irrigation hours (r ≈ 0.91)."""
    soybean = df[df['crop_type'] =='soybean']
    if soybean.empty:
        return True, "No soybean farms."
    yield_per_acre = soybean['yield_tons'] / soybean['acreage']
    corr = yield_per_acre.corr(soybean['irrigation_hours_week'])
    truth = abs(corr - 0.91) < 0.01 if len(soybean) >= 2 else True
    expl = f"Correlation is {corr:.2f}, {'≈0.91' if truth else 'not ≈0.91'}."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All corn farms with fertilizer usage >940 kg have yields exceeding 415 tons."""
    corn = df[df['crop_type'] == 'corn']
    high_fertilizer = corn[corn['fertilizer_kg'] > 940]
    cond = high_fertilizer['yield_tons'] > 415
    truth = cond.all() if not high_fertilizer.empty else True
    viol = high_fertilizer[~cond] if not high_fertilizer.empty else pd.DataFrame()
    expl = f"{len(viol)} farms violate the rule." if not truth else "All high-fertilizer corn farms exceed 415 tons."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. The two highest-yielding farms (corn and rice) both use ≥17.1 irrigation hours/week."""
    top_yield = df.nlargest(2, 'yield_tons')
    if len(top_yield) < 2:
        return False, "Less than two farms exist."
    crop_types = top_yield['crop_type'].unique()
    if set(crop_types)!= {'corn', 'rice'}:
        return False, "Top two farms are not corn and rice."
    cond = top_yield['irrigation_hours_week'] >= 17.1
    truth = cond.all()
    viol = top_yield[~cond] if not truth else pd.DataFrame()
    expl = "Top two farms are corn/rice with ≥17.1 irrigation." if truth else f"{len(viol)} top farms have irrigation <17.1."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Organic farms have lower yield per acre than non-organic farms across all crop types."""
    crop_types = df['crop_type'].unique()
    for crop in crop_types:
        organic = df[(df['crop_type'] == crop) & (df['organic'] == True)]
        non_organic = df[(df['crop_type'] == crop) & (df['organic'] == False)]
        if organic.empty or non_organic.empty:
            continue
        organic_yield = organic['yield_tons'] / organic['acreage']
        non_organic_yield = non_organic['yield_tons'] / non_organic['acreage']
        max_organic = organic_yield.max()
        min_non_organic = non_organic_yield.min()
        if max_organic >= min_non_organic:
            return False, f"Organic {crop} has yield ≥ non-organic {crop}."
    return True, "Organic farms have lower yield per acre than non-organic across all crops."

def main():
    df = pd.read_csv("tables/table_6.csv")
    df['acreage'] = pd.to_numeric(df['acreage'], errors='coerce')
    df['yield_tons'] = pd.to_numeric(df['yield_tons'], errors='coerce')
    df['irrigation_hours_week'] = pd.to_numeric(df['irrigation_hours_week'], errors='coerce')
    df['fertilizer_kg'] = pd.to_numeric(df['fertilizer_kg'], errors='coerce')
    df['soil_quality_index'] = pd.to_numeric(df['soil_quality_index'], errors='coerce')
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
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()