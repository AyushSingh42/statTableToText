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
        expl = f"{len(viol)} organic farms violate the rule (soil quality index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows rice, then its yield is less than 450 tons."""
    rice = df[df["crop_type"] == "rice"]
    condition = rice["yield_tons"] < 450
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have yield < 450 tons."
    else:
        viol = rice[~condition]
        expl = f"{len(viol)} rice farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all farms with irrigation hours per week greater than 15, their fertilizer usage is greater than 700 kg."""
    irrig_gt15 = df[df["irrigation_hours_week"] > 15]
    condition = irrig_gt15["fertilizer_kg"] > 700
    truth = condition.all()
    if truth:
        expl = f"All {len(irrig_gt15)} farms with irrigation > 15 hrs/week have fertilizer > 700 kg."
    else:
        viol = irrig_gt15[~condition]
        expl = f"{len(viol)} farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one farm that grows corn with a yield greater than 400 tons."""
    corn_gt400 = df[(df["crop_type"] == "corn") & (df["yield_tons"] > 400)]
    truth = not corn_gt400.empty
    if truth:
        expl = f"{len(corn_gt400)} corn farm(s) have yield > 400 tons."
    else:
        expl = "No corn farm has yield > 400 tons."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms with acreage greater than 120 have a yield greater than 350 tons."""
    acres_gt120 = df[df["acreage"] > 120]
    condition = acres_gt120["yield_tons"] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(acres_gt120)} farms with acreage > 120 have yield > 350 tons."
    else:
        viol = acres_gt120[~condition]
        expl = f"{len(viol)} farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a farm grows soybean, then its fertilizer usage is greater than 900 kg."""
    soybean = df[df["crop_type"] == "soybean"]
    if soybean.empty:
        return True, "No soybean farms; rule vacuously true."
    condition = soybean["fertilizer_kg"] > 900
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean)} soybean farms have fertilizer > 900 kg."
    else:
        viol = soybean[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all farms with soil quality index greater than 79, their yield is greater than 350 tons."""
    soil_gt79 = df[df["soil_quality_index"] > 79]
    condition = soil_gt79["yield_tons"] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(soil_gt79)} farms with soil quality > 79 have yield > 350 tons."
    else:
        viol = soil_gt79[~condition]
        expl = f"{len(viol)} farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most farms have an irrigation hours per week less than 18."""
    irrig_lt18 = df[df["irrigation_hours_week"] < 18]
    proportion = len(irrig_lt18) / len(df)
    truth = proportion > 0.5
    if truth:
        expl = f"{len(irrig_lt18)}/{len(df)} farms ({proportion:.2f}) have irrigation < 18 hrs/week."
    else:
        expl = f"Only {len(irrig_lt18)}/{len(df)} farms ({proportion:.2f}) have irrigation < 18 hrs/week."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a farm grows wheat, then its yield is greater than 300 tons."""
    wheat = df[df["crop_type"] == "wheat"]
    if wheat.empty:
        return True, "No wheat farms; rule vacuously true."
    condition = wheat["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have yield > 300 tons."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with organic crops have an acreage greater than 70."""
    organic = df[df["organic"] == "yes"]
    condition = organic["acreage"] > 70
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have acreage > 70."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (acreage: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. For all farms with fertilizer usage greater than 1000 kg, their yield is greater than 400 tons."""
    fert_gt1000 = df[df["fertilizer_kg"] > 1000]
    if fert_gt1000.empty:
        return True, "No farms with fertilizer > 1000 kg; rule vacuously true."
    condition = fert_gt1000["yield_tons"] > 400
    truth = condition.all()
    if truth:
        expl = f"All {len(fert_gt1000)} farms with fertilizer > 1000 kg have yield > 400 tons."
    else:
        viol = fert_gt1000[~condition]
        expl = f"{len(viol)} farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. There exists at least one farm that grows corn with a soil quality index greater than 80."""
    corn_gt80 = df[(df["crop_type"] == "corn") & (df["soil_quality_index"] > 80)]
    truth = not corn_gt80.empty
    if truth:
        expl = f"{len(corn_gt80)} corn farm(s) have soil quality > 80."
    else:
        expl = "No corn farm has soil quality > 80."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All farms with yield greater than 400 tons have an irrigation hours per week greater than 12."""
    yield_gt400 = df[df["yield_tons"] > 400]
    condition = yield_gt400["irrigation_hours_week"] > 12
    truth = condition.all()
    if truth:
        expl = f"All {len(yield_gt400)} farms with yield > 400 tons have irrigation > 12 hrs/week."
    else:
        viol = yield_gt400[~condition]
        expl = f"{len(viol)} farms violate the rule (irrigation: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a farm grows rice, then its soil quality index is greater than 68."""
    rice = df[df["crop_type"] == "rice"]
    if rice.empty:
        return True, "No rice farms; rule vacuously true."
    condition = rice["soil_quality_index"] > 68
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have soil quality > 68."
    else:
        viol = rice[~condition]
        expl = f"{len(viol)} rice farms violate the rule (soil quality: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. For all farms with acreage less than 100, their fertilizer usage is less than 850 kg."""
    acres_lt100 = df[df["acreage"] < 100]
    if acres_lt100.empty:
        return True, "No farms with acreage < 100; rule vacuously true."
    condition = acres_lt100["fertilizer_kg"] < 850
    truth = condition.all()
    if truth:
        expl = f"All {len(acres_lt100)} farms with acreage < 100 have fertilizer < 850 kg."
    else:
        viol = acres_lt100[~condition]
        expl = f"{len(viol)} farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. Most farms have a soil quality index greater than 70."""
    soil_gt70 = df[df["soil_quality_index"] > 70]
    proportion = len(soil_gt70) / len(df)
    truth = proportion > 0.5
    if truth:
        expl = f"{len(soil_gt70)}/{len(df)} farms ({proportion:.2f}) have soil quality > 70."
    else:
        expl = f"Only {len(soil_gt70)}/{len(df)} farms ({proportion:.2f}) have soil quality > 70."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a farm grows soybean, then its yield is greater than 300 tons."""
    soybean = df[df["crop_type"] == "soybean"]
    if soybean.empty:
        return True, "No soybean farms; rule vacuously true."
    condition = soybean["yield_tons"] > 300
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean)} soybean farms have yield > 300 tons."
    else:
        viol = soybean[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All farms with irrigation hours per week less than 14 have a yield less than 400 tons."""
    irrig_lt14 = df[df["irrigation_hours_week"] < 14]
    condition = irrig_lt14["yield_tons"] < 400
    truth = condition.all()
    if truth:
        expl = f"All {len(irrig_lt14)} farms with irrigation < 14 hrs/week have yield < 400 tons."
    else:
        viol = irrig_lt14[~condition]
        expl = f"{len(viol)} farms violate the rule (yield: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_28.csv")

    # Convert numeric columns safely.
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
        (17, stmt_17),
        (18, stmt_18),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()