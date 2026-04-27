import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 68."""
    organic_farms = df[df["organic"] == "yes"]
    condition = organic_farms["soil_quality_index"] > 68
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality > 68."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows rice, then its yield is greater than 300 tons."""
    rice_farms = df[df["crop_type"] == "rice"]
    condition = rice_farms["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have yield > 300 tons."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All farms with irrigation hours per week greater than 16 have a fertilizer usage greater than 700 kg."""
    irrig_farms = df[df["irrigation_hours_week"] > 16]
    condition = irrig_farms["fertilizer_kg"] > 700
    truth = condition.all()
    if truth:
        expl = f"All {len(irrig_farms)} farms with >16 irrigation hours use >700 kg fertilizer."
    else:
        viol = irrig_farms[~condition]
        expl = f"{len(viol)} farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one farm that grows soybean with an acreage greater than 150."""
    exists = ((df["crop_type"] == "soybean") & (df["acreage"] > 150)).any()
    if exists:
        expl = "At least one soybean farm has acreage > 150."
    else:
        expl = "No soybean farm has acreage > 150."
    return exists, expl

def stmt_5(df: pd.DataFrame):
    """5. If a farm grows corn, then its soil quality index is greater than 74."""
    corn_farms = df[df["crop_type"] == "corn"]
    condition = corn_farms["soil_quality_index"] > 74
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have soil quality > 74."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (soil quality: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All farms with a soil quality index greater than 78 have organic crops."""
    high_soil = df[df["soil_quality_index"] > 78]
    condition = high_soil["organic"] == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality > 78 are organic."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms with soil quality > 78 are not organic."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms have an irrigation hours per week between 11 and 19."""
    between = df[(df["irrigation_hours_week"] >= 11) & (df["irrigation_hours_week"] <= 19)]
    truth = len(between) > len(df) / 2
    if truth:
        expl = f"{len(between)} out of {len(df)} farms have irrigation hours between 11 and 19."
    else:
        expl = f"Only {len(between)} out of {len(df)} farms have irrigation hours between 11 and 19."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a farm grows wheat, then its yield is greater than 250 tons."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = wheat_farms["yield_tons"] > 250
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have yield > 250 tons."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All farms with an acreage greater than 120 have a fertilizer usage greater than 600 kg."""
    large_acre = df[df["acreage"] > 120]
    condition = large_acre["fertilizer_kg"] > 600
    truth = condition.all()
    if truth:
        expl = f"All {len(large_acre)} farms with acreage > 120 use >600 kg fertilizer."
    else:
        viol = large_acre[~condition]
        expl = f"{len(viol)} farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one farm that grows rice with an irrigation hours per week less than 13."""
    exists = ((df["crop_type"] == "rice") & (df["irrigation_hours_week"] < 13)).any()
    if exists:
        expl = "At least one rice farm has irrigation hours < 13."
    else:
        expl = "No rice farm has irrigation hours < 13."
    return exists, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm has organic crops, then its soil quality index is greater than 68."""
    # Same as stmt_1
    return stmt_1(df)

def stmt_12(df: pd.DataFrame):
    """12. All farms with a yield greater than 400 tons have an acreage greater than 100."""
    high_yield = df[df["yield_tons"] > 400]
    condition = high_yield["acreage"] > 100
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield)} farms with yield > 400 tons have acreage > 100."
    else:
        viol = high_yield[~condition]
        expl = f"{len(viol)} farms violate the rule (acreage: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most farms have a fertilizer usage greater than 600 kg."""
    high_fert = df[df["fertilizer_kg"] > 600]
    truth = len(high_fert) > len(df) / 2
    if truth:
        expl = f"{len(high_fert)} out of {len(df)} farms use >600 kg fertilizer."
    else:
        expl = f"Only {len(high_fert)} out of {len(df)} farms use >600 kg fertilizer."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a farm grows soybean, then its yield is greater than 300 tons."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    condition = soybean_farms["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have yield > 300 tons."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All farms with a soil quality index greater than 79 have an acreage greater than 90."""
    high_soil = df[df["soil_quality_index"] > 79]
    condition = high_soil["acreage"] > 90
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality > 79 have acreage > 90."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms violate the rule (acreage: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one farm that grows corn with a fertilizer usage less than 700 kg."""
    exists = ((df["crop_type"] == "corn") & (df["fertilizer_kg"] < 700)).any()
    if exists:
        expl = "At least one corn farm has fertilizer usage < 700 kg."
    else:
        expl = "No corn farm has fertilizer usage < 700 kg."
    return exists, expl

def stmt_17(df: pd.DataFrame):
    """17. If a farm has an irrigation hours per week greater than 15, then its yield is greater than 300 tons."""
    irrig_farms = df[df["irrigation_hours_week"] > 15]
    condition = irrig_farms["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(irrig_farms)} farms with >15 irrigation hours have yield > 300 tons."
    else:
        viol = irrig_farms[~condition]
        expl = f"{len(viol)} farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_88.csv")

    # Convert numeric columns
    for col in df.columns:
        if col!= "organic":
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()