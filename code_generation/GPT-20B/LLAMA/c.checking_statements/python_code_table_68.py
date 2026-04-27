import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 68."""
    organic = df[df["organic"] == "yes"]
    condition = organic["soil_quality_index"] > 68
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have soil quality index > 68."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows corn, then its yield is greater than 285 tons."""
    corn = df[df["crop_type"] == "corn"]
    condition = corn["yield_tons"] > 285
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms have yield > 285 tons."
    else:
        viol = corn[~condition]
        expl = f"{len(viol)} corn farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm that grows soybean with an irrigation time of less than 18 hours per week."""
    soy = df[(df["crop_type"] == "soybean") & (df["irrigation_hours_week"] < 18)]
    truth = not soy.empty
    if truth:
        expl = f"Found {len(soy)} soybean farm(s) with irrigation < 18 hours/week."
    else:
        expl = "No soybean farm with irrigation < 18 hours/week found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with a soil quality index greater than 80, their fertilizer usage is less than 800 kg."""
    high_soil = df[df["soil_quality_index"] > 80]
    condition = high_soil["fertilizer_kg"] < 800
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality > 80 have fertilizer < 800 kg."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a farm grows rice, then its acreage is less than 120."""
    rice = df[df["crop_type"] == "rice"]
    condition = rice["acreage"] < 120
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have acreage < 120."
    else:
        viol = rice[~condition]
        expl = f"{len(viol)} rice farms violate the rule (acres: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All farms with non-organic crops have a soil quality index less than 83."""
    non_org = df[df["organic"] == "no"]
    condition = non_org["soil_quality_index"] < 83
    truth = condition.all()
    if truth:
        expl = f"All {len(non_org)} non-organic farms have soil quality index < 83."
    else:
        viol = non_org[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms have an irrigation time of less than 20 hours per week."""
    total = len(df)
    less20 = df[df["irrigation_hours_week"] < 20]
    proportion = len(less20) / total
    truth = proportion > 0.5
    if truth:
        expl = f"{len(less20)} out of {total} farms ({proportion:.2%}) have irrigation < 20 hours/week."
    else:
        expl = f"Only {len(less20)} out of {total} farms ({proportion:.2%}) have irrigation < 20 hours/week."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a farm grows wheat, then its yield is greater than 315 tons."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["yield_tons"] > 315
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have yield > 315 tons."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm that grows corn with an irrigation time of greater than 20 hours per week."""
    corn_irrig = df[(df["crop_type"] == "corn") & (df["irrigation_hours_week"] > 20)]
    truth = not corn_irrig.empty
    if truth:
        expl = f"Found {len(corn_irrig)} corn farm(s) with irrigation > 20 hours/week."
    else:
        expl = "No corn farm with irrigation > 20 hours/week found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. For all farms with a fertilizer usage greater than 900 kg, their yield is greater than 400 tons."""
    high_fert = df[df["fertilizer_kg"] > 900]
    condition = high_fert["yield_tons"] > 400
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} farms with fertilizer > 900 kg have yield > 400 tons."
    else:
        viol = high_fert[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All farms with organic crops have an irrigation time of less than 20 hours per week."""
    organic = df[df["organic"] == "yes"]
    condition = organic["irrigation_hours_week"] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have irrigation < 20 hours/week."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (irrigation: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a farm grows soybean, then its acreage is greater than 100."""
    soy = df[df["crop_type"] == "soybean"]
    condition = soy["acreage"] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(soy)} soybean farms have acreage > 100."
    else:
        viol = soy[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (acres: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. There exists at least one farm that grows rice with a soil quality index greater than 80."""
    rice_high = df[(df["crop_type"] == "rice") & (df["soil_quality_index"] > 80)]
    truth = not rice_high.empty
    if truth:
        expl = f"Found {len(rice_high)} rice farm(s) with soil quality index > 80."
    else:
        expl = "No rice farm with soil quality index > 80 found."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. For all farms with a yield greater than 400 tons, their fertilizer usage is greater than 700 kg."""
    high_yield = df[df["yield_tons"] > 400]
    condition = high_yield["fertilizer_kg"] > 700
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield)} farms with yield > 400 tons have fertilizer > 700 kg."
    else:
        viol = high_yield[~condition]
        expl = f"{len(viol)} farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Most farms have a soil quality index greater than 70."""
    total = len(df)
    high_soil = df[df["soil_quality_index"] > 70]
    proportion = len(high_soil) / total
    truth = proportion > 0.5
    if truth:
        expl = f"{len(high_soil)} out of {total} farms ({proportion:.2%}) have soil quality index > 70."
    else:
        expl = f"Only {len(high_soil)} out of {total} farms ({proportion:.2%}) have soil quality index > 70."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a farm grows wheat, then its acreage is greater than 85."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["acreage"] > 85
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have acreage > 85."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (acres: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. There exists at least one farm that grows corn with a yield greater than 400 tons."""
    corn_yield = df[(df["crop_type"] == "corn") & (df["yield_tons"] > 400)]
    truth = not corn_yield.empty
    if truth:
        expl = f"Found {len(corn_yield)} corn farm(s) with yield > 400 tons."
    else:
        expl = "No corn farm with yield > 400 tons found."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. For all farms with an irrigation time of less than 15 hours per week, their yield is less than 350 tons."""
    low_irrig = df[df["irrigation_hours_week"] < 15]
    condition = low_irrig["yield_tons"] < 350
    truth = condition.all()
    if truth:
        expl = f"All {len(low_irrig)} farms with irrigation < 15 hours/week have yield < 350 tons."
    else:
        viol = low_irrig[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All farms with non-organic crops have a fertilizer usage greater than 600 kg."""
    non_org = df[df["organic"] == "no"]
    condition = non_org["fertilizer_kg"] > 600
    truth = condition.all()
    if truth:
        expl = f"All {len(non_org)} non-organic farms have fertilizer > 600 kg."
    else:
        viol = non_org[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_68.csv")

    # Convert numeric columns safely
    for col in ["acreage", "yield_tons", "irrigation_hours_week", "fertilizer_kg", "soil_quality_index"]:
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