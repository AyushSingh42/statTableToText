import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All farms with organic crops have a soil quality index greater than 70."""
    organic = df[df["organic"] == "yes"]
    if organic.empty:
        return True, "No organic farms to evaluate."
    condition = organic["soil_quality_index"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have soil quality >70."
    else:
        viol = organic[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} organic farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows soybean, then its yield is less than 450 tons."""
    soy = df[df["crop_type"] == "soybean"]
    if soy.empty:
        return True, "No soybean farms to evaluate."
    condition = soy["yield_tons"] < 450
    truth = condition.all()
    if truth:
        expl = f"All {len(soy)} soybean farms have yield <450 tons."
    else:
        viol = soy[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} soybean farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm that grows rice with an acreage greater than 120."""
    rice = df[(df["crop_type"] == "rice") & (df["acreage"] > 120)]
    truth = not rice.empty
    if truth:
        ids = rice["farm_id"].tolist()
        expl = f"Found {len(rice)} rice farm(s) with acreage >120 (farm_ids: {', '.join(ids)})."
    else:
        expl = "No rice farms with acreage >120 found."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all farms with irrigation hours per week greater than 15, their fertilizer usage is greater than 800 kg."""
    irrig = df[df["irrigation_hours_week"] > 15]
    if irrig.empty:
        return True, "No farms with irrigation >15 to evaluate."
    condition = irrig["fertilizer_kg"] > 800
    truth = condition.all()
    if truth:
        expl = f"All {len(irrig)} farms with irrigation >15 have fertilizer >800 kg."
    else:
        viol = irrig[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms with wheat crops have an acreage greater than 70."""
    wheat = df[df["crop_type"] == "wheat"]
    if wheat.empty:
        return True, "No wheat farms to evaluate."
    condition = wheat["acreage"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have acreage >70."
    else:
        viol = wheat[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} wheat farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a farm grows corn, then its yield is less than 370 tons."""
    corn = df[df["crop_type"] == "corn"]
    if corn.empty:
        return True, "No corn farms to evaluate."
    condition = corn["yield_tons"] < 370
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms have yield <370 tons."
    else:
        viol = corn[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} corn farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all farms with organic crops, their soil quality index is greater than 72."""
    organic = df[df["organic"] == "yes"]
    if organic.empty:
        return True, "No organic farms to evaluate."
    condition = organic["soil_quality_index"] > 72
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have soil quality >72."
    else:
        viol = organic[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} organic farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one farm that grows soybean with an acreage less than 100 and yield greater than 280 tons."""
    soy = df[(df["crop_type"] == "soybean") & (df["acreage"] < 100) & (df["yield_tons"] > 280)]
    truth = not soy.empty
    if truth:
        ids = soy["farm_id"].tolist()
        expl = f"Found {len(soy)} soybean farm(s) with acreage <100 and yield >280 (farm_ids: {', '.join(ids)})."
    else:
        expl = "No soybean farms with acreage <100 and yield >280 found."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All farms with rice crops have a fertilizer usage greater than 890 kg."""
    rice = df[df["crop_type"] == "rice"]
    if rice.empty:
        return True, "No rice farms to evaluate."
    condition = rice["fertilizer_kg"] > 890
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have fertilizer >890 kg."
    else:
        viol = rice[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} rice farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a farm has an acreage greater than 140, then its crop type is either soybean or wheat."""
    large = df[df["acreage"] > 140]
    if large.empty:
        return True, "No farms with acreage >140 to evaluate."
    condition = large["crop_type"].isin(["soybean", "wheat"])
    truth = condition.all()
    if truth:
        expl = f"All {len(large)} farms with acreage >140 have crop type soybean or wheat."
    else:
        viol = large[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. For all farms with irrigation hours per week less than 12, their yield is less than 300 tons."""
    irrig = df[df["irrigation_hours_week"] < 12]
    if irrig.empty:
        return True, "No farms with irrigation <12 to evaluate."
    condition = irrig["yield_tons"] < 300
    truth = condition.all()
    if truth:
        expl = f"All {len(irrig)} farms with irrigation <12 have yield <300 tons."
    else:
        viol = irrig[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most farms have a soil quality index between 70 and 80."""
    between = df["soil_quality_index"].between(70, 80, inclusive="both")
    count = between.sum()
    total = len(df)
    truth = count > total / 2
    percent = count / total * 100
    if truth:
        expl = f"{count} out of {total} farms ({percent:.1f}%) have soil quality between 70 and 80."
    else:
        expl = f"Only {count} out of {total} farms ({percent:.1f}%) have soil quality between 70 and 80."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a farm grows wheat, then its yield is greater than 350 tons."""
    wheat = df[df["crop_type"] == "wheat"]
    if wheat.empty:
        return True, "No wheat farms to evaluate."
    condition = wheat["yield_tons"] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have yield >350 tons."
    else:
        viol = wheat[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} wheat farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one farm that grows corn with an acreage greater than 140 and yield less than 300 tons."""
    corn = df[(df["crop_type"] == "corn") & (df["acreage"] > 140) & (df["yield_tons"] < 300)]
    truth = not corn.empty
    if truth:
        ids = corn["farm_id"].tolist()
        expl = f"Found {len(corn)} corn farm(s) with acreage >140 and yield <300 (farm_ids: {', '.join(ids)})."
    else:
        expl = "No corn farms with acreage >140 and yield <300 found."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All farms with organic crops have an irrigation hours per week greater than 14."""
    organic = df[df["organic"] == "yes"]
    if organic.empty:
        return True, "No organic farms to evaluate."
    condition = organic["irrigation_hours_week"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have irrigation >14 hours/week."
    else:
        viol = organic[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} organic farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. For all farms with fertilizer usage greater than 900 kg, their crop type is either rice or corn."""
    high_fert = df[df["fertilizer_kg"] > 900]
    if high_fert.empty:
        return True, "No farms with fertilizer >900 to evaluate."
    condition = high_fert["crop_type"].isin(["rice", "corn"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} farms with fertilizer >900 kg have crop type rice or corn."
    else:
        viol = high_fert[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a farm has a soil quality index greater than 80, then its crop type is wheat."""
    high_soil = df[df["soil_quality_index"] > 80]
    if high_soil.empty:
        return True, "No farms with soil quality >80 to evaluate."
    condition = high_soil["crop_type"] == "wheat"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality >80 have crop type wheat."
    else:
        viol = high_soil[~condition]
        ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} farms violate the rule (farm_ids: {', '.join(ids)})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. There exists at least one farm that grows soybean with a yield greater than 420 tons and acreage less than 120."""
    soy = df[(df["crop_type"] == "soybean") & (df["yield_tons"] > 420) & (df["acreage"] < 120)]
    truth = not soy.empty
    if truth:
        ids = soy["farm_id"].tolist()
        expl = f"Found {len(soy)} soybean farm(s) with yield >420 and acreage <120 (farm_ids: {', '.join(ids)})."
    else:
        expl = "No soybean farms with yield >420 and acreage <120 found."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_78.csv")

    # Convert numeric columns
    for col in df.columns:
        if col not in ["farm_id", "crop_type", "organic"]:
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()