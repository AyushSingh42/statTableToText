import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 69."""
    organic_farms = df[df["organic"] == "yes"]
    condition = organic_farms["soil_quality_index"] > 69
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality index > 69."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows soybean, then its yield is greater than 347 tons."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    condition = soybean_farms["yield_tons"] > 347
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have yield > 347 tons."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All farms with irrigation hours per week greater than 15 have a fertilizer usage greater than 700 kg."""
    high_irrigation = df[df["irrigation_hours_week"] > 15]
    condition = high_irrigation["fertilizer_kg"] > 700
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation)} farms with irrigation > 15 have fertilizer > 700 kg."
    else:
        viol = high_irrigation[~condition]
        expl = f"{len(viol)} farms with irrigation > 15 violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one farm that grows wheat with an acreage less than 120."""
    matches = df[(df["crop_type"] == "wheat") & (df["acreage"] < 120)]
    truth = not matches.empty
    if truth:
        expl = f"Found {len(matches)} wheat farm(s) with acreage < 120 (farm_ids: {', '.join(matches['farm_id'].tolist())})."
    else:
        expl = "No wheat farms with acreage < 120 found."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a farm grows corn, then its yield is less than 422 tons."""
    corn_farms = df[df["crop_type"] == "corn"]
    condition = corn_farms["yield_tons"] < 422
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have yield < 422 tons."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All farms with a soil quality index greater than 80 have organic crops."""
    high_soil = df[df["soil_quality_index"] > 80]
    condition = high_soil["organic"] == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality index > 80 have organic crops."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms with soil quality index > 80 violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most farms have an irrigation hours per week less than 18."""
    total = len(df)
    count = df[df["irrigation_hours_week"] < 18].shape[0]
    truth = count > total / 2
    if truth:
        expl = f"{count} of {total} farms have irrigation < 18 hours/week (more than half)."
    else:
        expl = f"{count} of {total} farms have irrigation < 18 hours/week (not more than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a farm grows rice, then its yield is greater than 255 tons."""
    rice_farms = df[df["crop_type"] == "rice"]
    condition = rice_farms["yield_tons"] > 255
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have yield > 255 tons."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All farms with fertilizer usage greater than 1000 kg have a soil quality index greater than 80."""
    high_fertilizer = df[df["fertilizer_kg"] > 1000]
    condition = high_fertilizer["soil_quality_index"] > 80
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fertilizer)} farms with fertilizer > 1000 kg have soil quality index > 80."
    else:
        viol = high_fertilizer[~condition]
        expl = f"{len(viol)} farms with fertilizer > 1000 kg violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one farm that grows soybean with an acreage less than 120."""
    matches = df[(df["crop_type"] == "soybean") & (df["acreage"] < 120)]
    truth = not matches.empty
    if truth:
        expl = f"Found {len(matches)} soybean farm(s) with acreage < 120 (farm_ids: {', '.join(matches['farm_id'].tolist())})."
    else:
        expl = "No soybean farms with acreage < 120 found."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm grows wheat, then its yield is less than 464 tons."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = wheat_farms["yield_tons"] < 464
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have yield < 464 tons."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All farms with organic crops have a fertilizer usage greater than 626 kg."""
    organic_farms = df[df["organic"] == "yes"]
    condition = organic_farms["fertilizer_kg"] > 626
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have fertilizer > 626 kg."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most farms have an acreage greater than 100."""
    total = len(df)
    count = df[df["acreage"] > 100].shape[0]
    truth = count > total / 2
    if truth:
        expl = f"{count} of {total} farms have acreage > 100 (more than half)."
    else:
        expl = f"{count} of {total} farms have acreage > 100 (not more than half)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a farm grows corn, then its irrigation hours per week is greater than 11."""
    corn_farms = df[df["crop_type"] == "corn"]
    condition = corn_farms["irrigation_hours_week"] > 11
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have irrigation > 11 hours/week."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All farms with a yield greater than 400 tons have a soil quality index greater than 70."""
    high_yield = df[df["yield_tons"] > 400]
    condition = high_yield["soil_quality_index"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield)} farms with yield > 400 tons have soil quality index > 70."
    else:
        viol = high_yield[~condition]
        expl = f"{len(viol)} farms with yield > 400 tons violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one farm that grows rice with an acreage less than 150."""
    matches = df[(df["crop_type"] == "rice") & (df["acreage"] < 150)]
    truth = not matches.empty
    if truth:
        expl = f"Found {len(matches)} rice farm(s) with acreage < 150 (farm_ids: {', '.join(matches['farm_id'].tolist())})."
    else:
        expl = "No rice farms with acreage < 150 found."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a farm grows soybean, then its soil quality index is greater than 69."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    condition = soybean_farms["soil_quality_index"] > 69
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have soil quality index > 69."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All farms with a soil quality index greater than 75 have a fertilizer usage greater than 700 kg."""
    high_soil = df[df["soil_quality_index"] > 75]
    condition = high_soil["fertilizer_kg"] > 700
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality index > 75 have fertilizer > 700 kg."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms with soil quality index > 75 violate the rule (farm_ids: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_18.csv")

    # Convert numeric columns safely
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
        (17, stmt_17),
        (18, stmt_18),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()