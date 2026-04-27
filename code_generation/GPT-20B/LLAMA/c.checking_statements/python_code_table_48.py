import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with crop type 'wheat' have an acreage greater than 90."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["acreage"] > 90
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have acreage > 90."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (acreage: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm has crop type 'rice', then its soil quality index is less than 82."""
    rice = df[df["crop_type"] == "rice"]
    condition = rice["soil_quality_index"] < 82
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have soil quality index < 82."
    else:
        viol = rice[~condition]
        expl = f"{len(viol)} rice farms violate the rule (soil quality index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm with crop type'soybean' that has an organic status of 'yes'."""
    soy_yes = df[(df["crop_type"] == "soybean") & (df["organic"] == "yes")]
    truth = not soy_yes.empty
    if truth:
        expl = f"Found {len(soy_yes)} soybean farm(s) with organic yes."
    else:
        expl = "No soybean farm with organic yes found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with irrigation hours per week greater than 15, their yield tons are greater than 300."""
    cond = df[df["irrigation_hours_week"] > 15]
    condition = cond["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(cond)} farms with irrigation > 15 have yield > 300."
    else:
        viol = cond[~condition]
        expl = f"{len(viol)} farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms with fertilizer kg greater than 900 have a crop type of'soybean' or 'wheat'."""
    cond = df[df["fertilizer_kg"] > 900]
    condition = cond["crop_type"].isin(["soybean", "wheat"])
    truth = condition.all()
    if truth:
        expl = f"All {len(cond)} farms with fertilizer > 900 have crop type soybean or wheat."
    else:
        viol = cond[~condition]
        expl = f"{len(viol)} farms violate the rule (crop type: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a farm has an organic status of 'yes', then its soil quality index is greater than 68."""
    cond = df[df["organic"] == "yes"]
    condition = cond["soil_quality_index"] > 68
    truth = condition.all()
    if truth:
        expl = f"All {len(cond)} organic farms have soil quality index > 68."
    else:
        viol = cond[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms have an acreage greater than 90."""
    total = len(df)
    count = df[df["acreage"] > 90].shape[0]
    proportion = count / total if total > 0 else 0
    truth = proportion > 0.5
    expl = f"{count} out of {total} farms have acreage > 90 ({proportion*100:.1f}%)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all farms with crop type 'rice', if their irrigation hours per week are greater than 15, then their yield tons are greater than 300."""
    cond = df[(df["crop_type"] == "rice") & (df["irrigation_hours_week"] > 15)]
    condition = cond["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(cond)} rice farms with irrigation > 15 have yield > 300."
    else:
        viol = cond[~condition]
        expl = f"{len(viol)} rice farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm with crop type 'wheat' that has an organic status of 'no'."""
    wheat_no = df[(df["crop_type"] == "wheat") & (df["organic"] == "no")]
    truth = not wheat_no.empty
    if truth:
        expl = f"Found {len(wheat_no)} wheat farm(s) with organic no."
    else:
        expl = "No wheat farm with organic no found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with soil quality index greater than 78 have a crop type of'soybean'."""
    cond = df[df["soil_quality_index"] > 78]
    condition = cond["crop_type"] == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(cond)} farms with soil quality > 78 have crop type soybean."
    else:
        viol = cond[~condition]
        expl = f"{len(viol)} farms violate the rule (crop type: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm has a crop type of'soybean', then its yield tons are less than 400."""
    cond = df[df["crop_type"] == "soybean"]
    condition = cond["yield_tons"] < 400
    truth = condition.all()
    if truth:
        expl = f"All {len(cond)} soybean farms have yield < 400."
    else:
        viol = cond[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all farms with fertilizer kg greater than 700, their yield tons are greater than 250."""
    cond = df[df["fertilizer_kg"] > 700]
    condition = cond["yield_tons"] > 250
    truth = condition.all()
    if truth:
        expl = f"All {len(cond)} farms with fertilizer > 700 have yield > 250."
    else:
        viol = cond[~condition]
        expl = f"{len(viol)} farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All farms with irrigation hours per week less than 12 have a crop type of 'rice' or 'wheat'."""
    cond = df[df["irrigation_hours_week"] < 12]
    condition = cond["crop_type"].isin(["rice", "wheat"])
    truth = condition.all()
    if truth:
        expl = f"All {len(cond)} farms with irrigation < 12 have crop type rice or wheat."
    else:
        viol = cond[~condition]
        expl = f"{len(viol)} farms violate the rule (crop type: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one farm with crop type 'rice' that has an acreage less than 100."""
    rice_lt_100 = df[(df["crop_type"] == "rice") & (df["acreage"] < 100)]
    truth = not rice_lt_100.empty
    if truth:
        expl = f"Found {len(rice_lt_100)} rice farm(s) with acreage < 100."
    else:
        expl = "No rice farm with acreage < 100 found."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. For all farms with crop type 'wheat', if their fertilizer kg are greater than 800, then their yield tons are greater than 400."""
    cond = df[(df["crop_type"] == "wheat") & (df["fertilizer_kg"] > 800)]
    condition = cond["yield_tons"] > 400
    truth = condition.all()
    if truth:
        expl = f"All {len(cond)} wheat farms with fertilizer > 800 have yield > 400."
    else:
        viol = cond[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. Most farms with crop type'soybean' have an organic status of 'yes'."""
    cond = df[df["crop_type"] == "soybean"]
    total = len(cond)
    if total == 0:
        truth = True
        expl = "No soybean farms, so statement is vacuously true."
    else:
        count_yes = cond[cond["organic"] == "yes"].shape[0]
        proportion = count_yes / total
        truth = proportion > 0.5
        expl = f"{count_yes} out of {total} soybean farms have organic yes ({proportion*100:.1f}%)."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All farms with soil quality index less than 70 have a crop type of'soybean' or 'rice'."""
    cond = df[df["soil_quality_index"] < 70]
    condition = cond["crop_type"].isin(["soybean", "rice"])
    truth = condition.all()
    if truth:
        expl = f"All {len(cond)} farms with soil quality < 70 have crop type soybean or rice."
    else:
        viol = cond[~condition]
        expl = f"{len(viol)} farms violate the rule (crop type: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_48.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()