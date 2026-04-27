import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 78."""
    organic = df[df["organic"] == "yes"]
    condition = organic["soil_quality_index"] > 78
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have soil quality index > 78."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (indices: {', '.join(map(str, viol['soil_quality_index']))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows rice, then its irrigation hours per week are less than 21."""
    rice = df[df["crop_type"] == "rice"]
    condition = rice["irrigation_hours_week"] < 21
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have irrigation hours < 21."
    else:
        viol = rice[~condition]
        expl = f"{len(viol)} rice farms violate the rule (hours: {', '.join(map(str, viol['irrigation_hours_week']))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm that grows soybean with an acreage greater than 140."""
    soy = df[(df["crop_type"] == "soybean") & (df["acreage"] > 140)]
    truth = not soy.empty
    if truth:
        expl = f"Found {len(soy)} soybean farm(s) with acreage > 140."
    else:
        expl = "No soybean farm with acreage > 140 found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with wheat crops, if the acreage is greater than 100, then the yield is less than 350 tons."""
    wheat = df[df["crop_type"] == "wheat"]
    subset = wheat[wheat["acreage"] > 100]
    condition = subset["yield_tons"] < 350
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} wheat farms with acreage > 100 have yield < 350 tons."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons']))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms with fertilizer usage greater than 900 kg have a yield greater than 300 tons."""
    high_fert = df[df["fertilizer_kg"] > 900]
    condition = high_fert["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} farms with fertilizer > 900 kg have yield > 300 tons."
    else:
        viol = high_fert[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons']))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a farm grows rice and has an acreage greater than 100, then its yield is greater than 300 tons."""
    rice_big = df[(df["crop_type"] == "rice") & (df["acreage"] > 100)]
    condition = rice_big["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_big)} rice farms with acreage > 100 have yield > 300 tons."
    else:
        viol = rice_big[~condition]
        expl = f"{len(viol)} rice farms violate the rule (yields: {', '.join(map(str, viol['yield_tons']))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms with organic crops have a fertilizer usage greater than 900 kg."""
    organic = df[df["organic"] == "yes"]
    if organic.empty:
        truth = True
        expl = "No organic farms to evaluate; vacuously true."
    else:
        count = len(organic)
        good = (organic["fertilizer_kg"] > 900).sum()
        truth = good / count > 0.5
        if truth:
            expl = f"{good}/{count} organic farms have fertilizer > 900 kg (>{good/count:.2%})."
        else:
            expl = f"{good}/{count} organic farms have fertilizer > 900 kg (>{good/count:.2%}), which is not a majority."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all farms with soybean crops, if the acreage is greater than 90, then the yield is greater than 250 tons."""
    soy = df[df["crop_type"] == "soybean"]
    subset = soy[soy["acreage"] > 90]
    condition = subset["yield_tons"] > 250
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} soybean farms with acreage > 90 have yield > 250 tons."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields: {', '.join(map(str, viol['yield_tons']))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm that grows wheat with an irrigation hours per week less than 14."""
    wheat_low_irrig = df[(df["crop_type"] == "wheat") & (df["irrigation_hours_week"] < 14)]
    truth = not wheat_low_irrig.empty
    if truth:
        expl = f"Found {len(wheat_low_irrig)} wheat farm(s) with irrigation < 14 hours/week."
    else:
        expl = "No wheat farm with irrigation < 14 hours/week found."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with a soil quality index greater than 80 have a yield greater than 250 tons."""
    high_soil = df[df["soil_quality_index"] > 80]
    condition = high_soil["yield_tons"] > 250
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality > 80 have yield > 250 tons."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons']))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm grows rice and has an irrigation hours per week greater than 16, then its yield is greater than 350 tons."""
    rice_irrig = df[(df["crop_type"] == "rice") & (df["irrigation_hours_week"] > 16)]
    condition = rice_irrig["yield_tons"] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_irrig)} rice farms with irrigation > 16 hours/week have yield > 350 tons."
    else:
        viol = rice_irrig[~condition]
        expl = f"{len(viol)} rice farms violate the rule (yields: {', '.join(map(str, viol['yield_tons']))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all farms with wheat crops, if the fertilizer usage is greater than 700 kg, then the yield is greater than 300 tons."""
    wheat = df[df["crop_type"] == "wheat"]
    subset = wheat[wheat["fertilizer_kg"] > 700]
    condition = subset["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} wheat farms with fertilizer > 700 kg have yield > 300 tons."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons']))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most farms with non-organic crops have a soil quality index less than 80."""
    non_organic = df[df["organic"] == "no"]
    if non_organic.empty:
        truth = True
        expl = "No non-organic farms to evaluate; vacuously true."
    else:
        count = len(non_organic)
        good = (non_organic["soil_quality_index"] < 80).sum()
        truth = good / count > 0.5
        if truth:
            expl = f"{good}/{count} non-organic farms have soil quality < 80 (>{good/count:.2%})."
        else:
            expl = f"{good}/{count} non-organic farms have soil quality < 80 (>{good/count:.2%}), which is not a majority."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one farm that grows soybean with a fertilizer usage greater than 900 kg."""
    soy_fert = df[(df["crop_type"] == "soybean") & (df["fertilizer_kg"] > 900)]
    truth = not soy_fert.empty
    if truth:
        expl = f"Found {len(soy_fert)} soybean farm(s) with fertilizer > 900 kg."
    else:
        expl = "No soybean farm with fertilizer > 900 kg found."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All farms with an acreage greater than 120 have a yield greater than 300 tons."""
    large_acre = df[df["acreage"] > 120]
    condition = large_acre["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(large_acre)} farms with acreage > 120 have yield > 300 tons."
    else:
        viol = large_acre[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons']))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. If a farm grows wheat and has an acreage greater than 80, then its yield is greater than 250 tons."""
    wheat_big = df[(df["crop_type"] == "wheat") & (df["acreage"] > 80)]
    condition = wheat_big["yield_tons"] > 250
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_big)} wheat farms with acreage > 80 have yield > 250 tons."
    else:
        viol = wheat_big[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons']))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_8.csv")

    # Convert numeric columns
    numeric_cols = ["acreage", "yield_tons", "irrigation_hours_week", "fertilizer_kg", "soil_quality_index"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Normalize organic column
    df["organic"] = df["organic"].str.lower()

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()