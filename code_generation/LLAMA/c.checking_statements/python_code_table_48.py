import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with crop type 'wheat' have an acreage greater than 90."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = wheat_farms["acreage"] > 90
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have acreage > 90."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm has crop type 'rice', then its soil quality index is less than 82."""
    rice_farms = df[df["crop_type"] == "rice"]
    condition = rice_farms["soil_quality_index"] < 82
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have soil quality index < 82."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm with crop type'soybean' that has an organic status of 'yes'."""
    soybean_yes = df[(df["crop_type"] == "soybean") & (df["organic"] == "yes")]
    truth = len(soybean_yes) > 0
    if truth:
        expl = f"There are {len(soybean_yes)} soybean farms with organic status 'yes'."
    else:
        expl = "No soybean farms found with organic status 'yes'."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with irrigation hours per week greater than 15, their yield tons are greater than 300."""
    high_irrigation = df[df["irrigation_hours_week"] > 15]
    condition = high_irrigation["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation)} high irrigation farms have yield > 300."
    else:
        viol = high_irrigation[~condition]
        expl = f"{len(viol)} high irrigation farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms with fertilizer kg greater than 900 have a crop type of'soybean' or 'wheat'."""
    high_fert = df[df["fertilizer_kg"] > 900]
    condition = (high_fert["crop_type"] == "soybean") | (high_fert["crop_type"] == "wheat")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} high fertilizer farms have crop type'soybean' or 'wheat'."
    else:
        viol = high_fert[~condition]
        expl = f"{len(viol)} high fertilizer farms violate the rule (crop types: {', '.join(viol['crop_type'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a farm has an organic status of 'yes', then its soil quality index is greater than 68."""
    organic_farms = df[df["organic"] == "yes"]
    condition = organic_farms["soil_quality_index"] > 68
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality index > 68."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms have an acreage greater than 90."""
    total = len(df)
    high_acreage = df[df["acreage"] > 90]
    proportion = len(high_acreage) / total
    truth = proportion > 0.5
    if truth:
        expl = f"{len(high_acreage)}/{total} farms have acreage > 90 ({proportion:.2%})."
    else:
        expl = f"{len(high_acreage)}/{total} farms have acreage > 90 ({proportion:.2%})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all farms with crop type 'rice', if their irrigation hours per week are greater than 15, then their yield tons are greater than 300."""
    rice_farms = df[df["crop_type"] == "rice"]
    filtered = rice_farms[rice_farms["irrigation_hours_week"] > 15]
    condition = filtered["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} rice farms with high irrigation have yield > 300."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} rice farms with high irrigation violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm with crop type 'wheat' that has an organic status of 'no'."""
    wheat_no = df[(df["crop_type"] == "wheat") & (df["organic"] == "no")]
    truth = len(wheat_no) > 0
    if truth:
        expl = f"There are {len(wheat_no)} wheat farms with organic status 'no'."
    else:
        expl = "No wheat farms found with organic status 'no'."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with soil quality index greater than 78 have a crop type of'soybean'."""
    high_soil = df[df["soil_quality_index"] > 78]
    condition = high_soil["crop_type"] == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} high soil quality farms have crop type'soybean'."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} high soil quality farms violate the rule (crop types: {', '.join(viol['crop_type'].tolist())})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm has a crop type of'soybean', then its yield tons are less than 400."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    condition = soybean_farms["yield_tons"] < 400
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have yield < 400."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all farms with fertilizer kg greater than 700, their yield tons are greater than 250."""
    high_fert = df[df["fertilizer_kg"] > 700]
    condition = high_fert["yield_tons"] > 250
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} high fertilizer farms have yield > 250."
    else:
        viol = high_fert[~condition]
        expl = f"{len(viol)} high fertilizer farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All farms with irrigation hours per week less than 12 have a crop type of 'rice' or 'wheat'."""
    low_irrigation = df[df["irrigation_hours_week"] < 12]
    condition = (low_irrigation["crop_type"] == "rice") | (low_irrigation["crop_type"] == "wheat")
    truth = condition.all()
    if truth:
        expl = f"All {len(low_irrigation)} low irrigation farms have crop type 'rice' or 'wheat'."
    else:
        viol = low_irrigation[~condition]
        expl = f"{len(viol)} low irrigation farms violate the rule (crop types: {', '.join(viol['crop_type'].tolist())})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one farm with crop type 'rice' that has an acreage less than 100."""
    rice_low_acreage = df[(df["crop_type"] == "rice") & (df["acreage"] < 100)]
    truth = len(rice_low_acreage) > 0
    if truth:
        expl = f"There are {len(rice_low_acreage)} rice farms with acreage < 100."
    else:
        expl = "No rice farms found with acreage < 100."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. For all farms with crop type 'wheat', if their fertilizer kg are greater than 800, then their yield tons are greater than 400."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    filtered = wheat_farms[wheat_farms["fertilizer_kg"] > 800]
    condition = filtered["yield_tons"] > 400
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} wheat farms with high fertilizer have yield > 400."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} wheat farms with high fertilizer violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. Most farms with crop type'soybean' have an organic status of 'yes'."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    total_soybean = len(soybean_farms)
    organic_soybean = len(soybean_farms[soybean_farms["organic"] == "yes"])
    proportion = organic_soybean / total_soybean if total_soybean > 0 else 0
    truth = proportion > 0.5
    if truth:
        expl = f"{organic_soybean}/{total_soybean} soybean farms are organic ({proportion:.2%})."
    else:
        expl = f"{organic_soybean}/{total_soybean} soybean farms are organic ({proportion:.2%})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All farms with soil quality index less than 70 have a crop type of'soybean' or 'rice'."""
    low_soil = df[df["soil_quality_index"] < 70]
    condition = (low_soil["crop_type"] == "soybean") | (low_soil["crop_type"] == "rice")
    truth = condition.all()
    if truth:
        expl = f"All {len(low_soil)} low soil quality farms have crop type'soybean' or 'rice'."
    else:
        viol = low_soil[~condition]
        expl = f"{len(viol)} low soil quality farms violate the rule (crop types: {', '.join(viol['crop_type'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_48.csv")

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
        (17, stmt_17)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()