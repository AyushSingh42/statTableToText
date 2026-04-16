

import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All urban households with monthly income exceeding 5.5 have rent costs above 1.8."""
    urban_high_income = df[(df['region'] == 'urban') & (df['monthly_income_k'] > 5.5)]
    condition = urban_high_income['rent_k'] > 1.8
    truth = condition.all() if not urban_high_income.empty else True
    if truth:
        expl = f"All {len(urban_high_income)} urban high-income households have rent above 1.8."
    else:
        viol = urban_high_income[~condition]
        expl = f"{len(viol)} households violate the rule (rent: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Suburban households with fiber internet have higher monthly incomes than those with cable internet."""
    suburban_fiber = df[(df['region'] =='suburban') & (df['internet_type'] == 'fiber')]
    suburban_cable = df[(df['region'] =='suburban') & (df['internet_type'] == 'cable')]
    min_fiber = suburban_fiber['monthly_income_k'].min() if not suburban_fiber.empty else float('inf')
    max_cable = suburban_cable['monthly_income_k'].max() if not suburban_cable.empty else float('-inf')
    truth = (min_fiber > max_cable) if (not suburban_fiber.empty and not suburban_cable.empty) else True
    if truth:
        expl = f"All suburban fiber incomes ({min_fiber:.2f}+) are higher than suburban cable max ({max_cable:.2f})."
    else:
        expl = f"Suburban fiber min income ({min_fiber:.2f}) is not higher than suburban cable max ({max_cable:.2f})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Rural households with satellite internet have utility costs exceeding 150, while those with DSL have utility costs below 120."""
    rural_satellite = df[(df['region'] == 'rural') & (df['internet_type'] =='satellite')]
    rural_dsl = df[(df['region'] == 'rural') & (df['internet_type'] == 'DSL')]
    cond_satellite = rural_satellite['utility_cost'] > 150
    cond_dsl = rural_dsl['utility_cost'] < 120
    truth_satellite = cond_satellite.all() if not rural_satellite.empty else True
    truth_dsl = cond_dsl.all() if not rural_dsl.empty else True
    truth = truth_satellite and truth_dsl
    if truth:
        expl = "All rural satellite households have utility >150 and rural DSL households have utility <120."
    else:
        viol_satellite = rural_satellite[~cond_satellite]
        viol_dsl = rural_dsl[~cond_dsl]
        parts = []
        if not viol_satellite.empty:
            parts.append(f"{len(viol_satellite)} rural satellite households have utility ≤150.")
        if not viol_dsl.empty:
            parts.append(f"{len(viol_dsl)} rural DSL households have utility ≥120.")
        expl = "Violations: " + "; ".join(parts)
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Households with more than 2 vehicles exclusively use fiber or satellite internet."""
    many_vehicles = df[df['vehicle_count'] > 2]
    valid_internet = many_vehicles['internet_type'].isin(['fiber','satellite'])
    truth = valid_internet.all() if not many_vehicles.empty else True
    if truth:
        expl = f"All {len(many_vehicles)} households with >2 vehicles use fiber or satellite internet."
    else:
        viol = many_vehicles[~valid_internet]
        expl = f"{len(viol)} households use non-fiber/satellite internet (types: {', '.join(viol['internet_type'].unique())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Urban households have higher rent-to-income ratios (≥29%) compared to suburban (≤28%) or rural (≤22%) households."""
    df['rent_to_income'] = df['rent_k'] / df['monthly_income_k']
    urban_ratio = df[df['region'] == 'urban']['rent_to_income'] >= 0.29
    suburban_ratio = df[df['region'] =='suburban']['rent_to_income'] <= 0.28
    rural_ratio = df[df['region'] == 'rural']['rent_to_income'] <= 0.22
    truth_urban = urban_ratio.all() if not urban_ratio.empty else True
    truth_suburban = suburban_ratio.all() if not suburban_ratio.empty else True
    truth_rural = rural_ratio.all() if not rural_ratio.empty else True
    truth = truth_urban and truth_suburban and truth_rural
    if truth:
        expl = "All urban, suburban, and rural households meet their respective rent-to-income ratio conditions."
    else:
        viol_urban = df[(df['region'] == 'urban') & (~urban_ratio)]
        viol_suburban = df[(df['region'] =='suburban') & (~suburban_ratio)]
        viol_rural = df[(df['region'] == 'rural') & (~rural_ratio)]
        parts = []
        if not viol_urban.empty:
            parts.append(f"{len(viol_urban)} urban households have rent-to-income ratio <29%.")
        if not viol_suburban.empty:
            parts.append(f"{len(viol_suburban)} suburban households have ratio >28%.")
        if not viol_rural.empty:
            parts.append(f"{len(viol_rural)} rural households have ratio >22%.")
        expl = "Violations: " + "; ".join(parts)
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Suburban households with 5 or more members have monthly incomes exceeding 10.0."""
    suburban_large = df[(df['region'] =='suburban') & (df['household_size'] >= 5)]
    condition = suburban_large['monthly_income_k'] > 10.0
    truth = condition.all() if not suburban_large.empty else True
    if truth:
        expl = f"All {len(suburban_large)} suburban large households have income >10.0."
    else:
        viol = suburban_large[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Households with utility costs above 190 are exclusively suburban or urban."""
    high_utility = df[df['utility_cost'] > 190]
    valid_region = high_utility['region'].isin(['suburban', 'urban'])
    truth = valid_region.all() if not high_utility.empty else True
    if truth:
        expl = f"All {len(high_utility)} high-utility households are suburban or urban."
    else:
        viol = high_utility[~valid_region]
        expl = f"{len(viol)} households are rural but have utility cost >190."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Rural households with DSL internet have fewer than 2 vehicles."""
    rural_dsl = df[(df['region'] == 'rural') & (df['internet_type'] == 'DSL')]
    condition = rural_dsl['vehicle_count'] < 2
    truth = condition.all() if not rural_dsl.empty else True
    if truth:
        expl = f"All {len(rural_dsl)} rural DSL households have <2 vehicles."
    else:
        viol = rural_dsl[~condition]
        expl = f"{len(viol)} households violate the rule (vehicles: {', '.join(map(str, viol['vehicle_count'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a household has satellite internet, its utility cost exceeds 150 and its region is rural."""
    satellite_households = df[df['internet_type'] =='satellite']
    condition = (satellite_households['utility_cost'] > 150) & (satellite_households['region'] == 'rural')
    truth = condition.all() if not satellite_households.empty else True
    if truth:
        expl = f"All {len(satellite_households)} satellite internet households meet the conditions."
    else:
        viol = satellite_households[~condition]
        parts = []
        if (viol['utility_cost'] <= 150).any():
            parts.append(f"{len(viol[viol['utility_cost'] <= 150])} have utility cost ≤150.")
        if (viol['region']!= 'rural').any():
            parts.append(f"{len(viol[viol['region']!= 'rural'])} are not in rural region.")
        expl = "Violations: " + "; ".join(parts)
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Suburban households with monthly incomes between 7.0 and 8.0 have rent costs between 1.7 and 2.2."""
    suburban_income = df[(df['region'] =='suburban') & (df['monthly_income_k'].between(7.0, 8.0, inclusive='both'))]
    condition = suburban_income['rent_k'].between(1.7, 2.2, inclusive='both')
    truth = condition.all() if not suburban_income.empty else True
    if truth:
        expl = f"All {len(suburban_income)} suburban households meet rent cost conditions."
    else:
        viol = suburban_income[~condition]
        expl = f"{len(viol)} households violate the rule (rent: {', '.join(map(str, viol['rent_k'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Urban households with fiber internet have utility costs exceeding 130 but less than 195."""
    urban_fiber = df[(df['region'] == 'urban') & (df['internet_type'] == 'fiber')]
    condition = urban_fiber['utility_cost'].between(130, 195, inclusive='neither')
    truth = condition.all() if not urban_fiber.empty else True
    if truth:
        expl = f"All {len(urban_fiber)} urban fiber households meet utility cost conditions."
    else:
        viol = urban_fiber[~condition]
        expl = f"{len(viol)} households violate the rule (utility: {', '.join(map(str, viol['utility_cost'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Households with more than 3 members have utility costs exceeding 150, except rural households with DSL internet."""
    large_households = df[df['household_size'] > 3]
    condition = (
        ((large_households['region'] == 'rural') & (large_households['internet_type'] == 'DSL') & (large_households['utility_cost'] <= 150)) |
        ((large_households['region']!= 'rural') | (large_households['internet_type']!= 'DSL')) & (large_households['utility_cost'] > 150)
    )
    truth = condition.all() if not large_households.empty else True
    if truth:
        expl = f"All {len(large_households)} large households meet the utility cost condition."
    else:
        viol = large_households[~condition]
        expl = f"{len(viol)} households violate the rule."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All suburban households with cable internet have monthly incomes between 6.0 and 7.2."""
    suburban_cable = df[(df['region'] =='suburban') & (df['internet_type'] == 'cable')]
    condition = suburban_cable['monthly_income_k'].between(6.0, 7.2, inclusive='both')
    truth = condition.all() if not suburban_cable.empty else True
    if truth:
        expl = f"All {len(suburban_cable)} suburban cable households meet income conditions."
    else:
        viol = suburban_cable[~condition]
        expl = f"{len(viol)} households violate the rule (incomes: {', '.join(map(str, viol['monthly_income_k'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Rural households with monthly incomes above 5.0 have vehicle counts ≥2."""
    rural_high_income = df[(df['region'] == 'rural') & (df['monthly_income_k'] > 5.0)]
    condition = rural_high_income['vehicle_count'] >= 2
    truth = condition.all() if not rural_high_income.empty else True
    if truth:
        expl = f"All {len(rural_high_income)} rural high-income households have ≥2 vehicles."
    else:
        viol = rural_high_income[~condition]
        expl = f"{len(viol)} households violate the rule (vehicles: {', '.join(map(str, viol['vehicle_count'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Households with internet types other than fiber or satellite are exclusively rural or suburban."""
    non_fiber_satellite = df[~df['internet_type'].isin(['fiber','satellite'])]
    valid_region = non_fiber_satellite['region'].isin(['rural','suburban'])
    truth = valid_region.all() if not non_fiber_satellite.empty else True
    if truth:
        expl = f"All {len(non_fiber_satellite)} non-fiber/satellite households are rural or suburban."
    else:
        viol = non_fiber_satellite[~valid_region]
        expl = f"{len(viol)} households are urban but have non-fiber/satellite internet."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_5.csv")
    numeric_cols = ['monthly_income_k','rent_k', 'utility_cost','vehicle_count']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    checks = [
        (1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5),
        (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10),
        (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()