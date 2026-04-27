import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 70."""
    organic = df[df["organic"] == "yes"]
    condition = organic["soil_quality_index"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have soil quality index > 70."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows corn, then its yield is greater than 250 tons."""
    corn = df[df["crop_type"] == "corn"]
    condition = corn["yield_tons"] > 250
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms have yield > 250 tons."
    else:
        viol = corn[~condition]
        expl = f"{len(viol)} corn farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm that grows soybean with an acreage less than 110."""
    soy = df[(df["crop_type"] == "soybean") & (df["acreage"] < 110)]
    truth = not soy.empty
    if truth:
        expl = f"Found {len(soy)} soybean farm(s) with acreage < 110 (ids: {', '.join(soy['farm_id'].tolist())})."
    else:
        expl = "No soybean farm with acreage < 110 found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with irrigation hours per week greater than 15, their fertilizer usage is greater than 800 kg."""
    irrig = df[df["irrigation_hours_week"] > 15]
    condition = irrig["fertilizer_kg"] > 800
    truth = condition.all()
    if truth:
        expl = f"All {len(irrig)} farms with irrigation > 15 hrs have fertilizer > 800 kg."
    else:
        viol = irrig[~condition]
        expl = f"{len(viol)} farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms with wheat crops have an acreage greater than 70."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["acreage"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have acreage > 70."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (acres: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a farm grows soybean, then its yield is less than 400 tons."""
    soy = df[df["crop_type"] == "soybean"]
    condition = soy["yield_tons"] < 400
    truth = condition.all()
    if truth:
        expl = f"All {len(soy)} soybean farms have yield < 400 tons."
    else:
        viol = soy[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms with organic crops have an acreage greater than 100."""
    organic = df[df["organic"] == "yes"]
    if organic.empty:
        truth = True
        expl = "No organic farms to evaluate; statement considered true."
    else:
        condition = organic["acreage"] > 100
        count_true = condition.sum()
        truth = count_true > len(organic) / 2
        if truth:
            expl = f"{count_true} out of {len(organic)} organic farms have acreage > 100 (>{len(organic)/2})."
        else:
            expl = f"Only {count_true} out of {len(organic)} organic farms have acreage > 100."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all farms with soil quality index greater than 80, their fertilizer usage is greater than 900 kg."""
    high_sqi = df[df["soil_quality_index"] > 80]
    condition = high_sqi["fertilizer_kg"] > 900
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sqi)} farms with soil quality index > 80 have fertilizer > 900 kg."
    else:
        viol = high_sqi[~condition]
        expl = f"{len(viol)} farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm that grows corn with an irrigation hours per week less than 16."""
    corn_irrig = df[(df["crop_type"] == "corn") & (df["irrigation_hours_week"] < 16)]
    truth = not corn_irrig.empty
    if truth:
        expl = f"Found {len(corn_irrig)} corn farm(s) with irrigation < 16 hrs (ids: {', '.join(corn_irrig['farm_id'].tolist())})."
    else:
        expl = "No corn farm with irrigation < 16 hrs found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with non-organic crops have a soil quality index less than 82."""
    non_organic = df[df["organic"] == "no"]
    condition = non_organic["soil_quality_index"] < 82
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic)} non-organic farms have soil quality index < 82."
    else:
        viol = non_organic[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm grows wheat, then its yield is greater than 290 tons."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["yield_tons"] > 290
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have yield > 290 tons."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all farms with acreage greater than 120, their yield is greater than 350 tons."""
    large_acre = df[df["acreage"] > 120]
    condition = large_acre["yield_tons"] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(large_acre)} farms with acreage > 120 have yield > 350 tons."
    else:
        viol = large_acre[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most farms with fertilizer usage greater than 700 kg have an irrigation hours per week greater than 12."""
    high_fert = df[df["fertilizer_kg"] > 700]
    if high_fert.empty:
        truth = True
        expl = "No farms with fertilizer > 700 kg; statement considered true."
    else:
        condition = high_fert["irrigation_hours_week"] > 12
        count_true = condition.sum()
        truth = count_true > len(high_fert) / 2
        if truth:
            expl = f"{count_true} out of {len(high_fert)} farms with fertilizer > 700 kg have irrigation > 12 hrs."
        else:
            expl = f"Only {count_true} out of {len(high_fert)} farms with fertilizer > 700 kg have irrigation > 12 hrs."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. For all farms with soil quality index between 70 and 80, their yield is less than 450 tons."""
    sqi_range = df[(df["soil_quality_index"] >= 70) & (df["soil_quality_index"] <= 80)]
    condition = sqi_range["yield_tons"] < 450
    truth = condition.all()
    if truth:
        expl = f"All {len(sqi_range)} farms with soil quality index 70-80 have yield < 450 tons."
    else:
        viol = sqi_range[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one farm that grows soybean with a fertilizer usage greater than 1000 kg."""
    soy_fert = df[(df["crop_type"] == "soybean") & (df["fertilizer_kg"] > 1000)]
    truth = not soy_fert.empty
    if truth:
        expl = f"Found {len(soy_fert)} soybean farm(s) with fertilizer > 1000 kg (ids: {', '.join(soy_fert['farm_id'].tolist())})."
    else:
        expl = "No soybean farm with fertilizer > 1000 kg found."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All farms with organic crops have a yield greater than 240 tons."""
    organic = df[df["organic"] == "yes"]
    condition = organic["yield_tons"] > 240
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have yield > 240 tons."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a farm grows corn, then its irrigation hours per week is greater than 14."""
    corn = df[df["crop_type"] == "corn"]
    condition = corn["irrigation_hours_week"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms have irrigation > 14 hrs."
    else:
        viol = corn[~condition]
        expl = f"{len(viol)} corn farms violate the rule (irrigation hrs: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. For all farms with yield greater than 400 tons, their acreage is greater than 100."""
    high_yield = df[df["yield_tons"] > 400]
    condition = high_yield["acreage"] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield)} farms with yield > 400 tons have acreage > 100."
    else:
        viol = high_yield[~condition]
        expl = f"{len(viol)} farms violate the rule (acreage: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. Most farms with irrigation hours per week less than 18 have a fertilizer usage less than 900 kg."""
    low_irrig = df[df["irrigation_hours_week"] < 18]
    if low_irrig.empty:
        truth = True
        expl = "No farms with irrigation < 18 hrs; statement considered true."
    else:
        condition = low_irrig["fertilizer_kg"] < 900
        count_true = condition.sum()
        truth = count_true > len(low_irrig) / 2
        if truth:
            expl = f"{count_true} out of {len(low_irrig)} farms with irrigation < 18 hrs have fertilizer < 900 kg."
        else:
            expl = f"Only {count_true} out of {len(low_irrig)} farms with irrigation < 18 hrs have fertilizer < 900 kg."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_38.csv")

    # Convert numeric columns
    numeric_cols = ["acreage", "yield_tons", "irrigation_hours_week", "fertilizer_kg", "soil_quality_index"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

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
        (19, stmt_19),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()