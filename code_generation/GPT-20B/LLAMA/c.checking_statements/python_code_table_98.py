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
        expl = f"{len(viol)} organic farms violate the rule (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a farm grows soybean, then its yield is greater than 380 tons."""
    soy = df[df["crop_type"] == "soybean"]
    condition = soy["yield_tons"] > 380
    truth = condition.all()
    if truth:
        expl = f"All {len(soy)} soybean farms have yield > 380 tons."
    else:
        viol = soy[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one farm with non-organic crops that has a soil quality index greater than 78."""
    exists = df[(df["organic"] == "no") & (df["soil_quality_index"] > 78)].shape[0] > 0
    truth = exists
    if truth:
        expl = "At least one non-organic farm has soil quality index > 78."
    else:
        expl = "No non-organic farm has soil quality index > 78."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All farms with irrigation hours per week greater than 14 have a yield greater than 400 tons."""
    irrig = df[df["irrigation_hours_week"] > 14]
    condition = irrig["yield_tons"] > 400
    truth = condition.all()
    if truth:
        expl = f"All {len(irrig)} farms with irrigation > 14h have yield > 400 tons."
    else:
        viol = irrig[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a farm grows rice, then its acreage is less than 130."""
    rice = df[df["crop_type"] == "rice"]
    condition = rice["acreage"] < 130
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have acreage < 130."
    else:
        viol = rice[~condition]
        expl = f"{len(viol)} rice farms violate the rule (acres: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most farms with organic crops have a fertilizer usage greater than 700 kg."""
    organic = df[df["organic"] == "yes"]
    if organic.empty:
        truth = True
        expl = "No organic farms to evaluate; vacuously true."
    else:
        count = organic.shape[0]
        good = (organic["fertilizer_kg"] > 700).sum()
        proportion = good / count
        truth = proportion > 0.5
        if truth:
            expl = f"{good}/{count} organic farms (>{proportion:.2f}) have fertilizer > 700 kg."
        else:
            expl = f"{good}/{count} organic farms (={proportion:.2f}) do not exceed 700 kg."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All farms with a soil quality index greater than 80 have organic crops."""
    high_soil = df[df["soil_quality_index"] > 80]
    condition = high_soil["organic"] == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality > 80 are organic."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms violate the rule (organic: {', '.join(viol['organic'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a farm grows corn, then its fertilizer usage is greater than 800 kg."""
    corn = df[df["crop_type"] == "corn"]
    condition = corn["fertilizer_kg"] > 800
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms have fertilizer > 800 kg."
    else:
        viol = corn[~condition]
        expl = f"{len(viol)} corn farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one farm with non-organic crops that has a yield greater than 450 tons."""
    exists = df[(df["organic"] == "no") & (df["yield_tons"] > 450)].shape[0] > 0
    truth = exists
    if truth:
        expl = "At least one non-organic farm has yield > 450 tons."
    else:
        expl = "No non-organic farm has yield > 450 tons."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All farms with a yield greater than 420 tons have irrigation hours per week greater than 12."""
    high_yield = df[df["yield_tons"] > 420]
    condition = high_yield["irrigation_hours_week"] > 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield)} farms with yield > 420 have irrigation > 12h."
    else:
        viol = high_yield[~condition]
        expl = f"{len(viol)} farms violate the rule (irrigation: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a farm grows wheat, then its acreage is less than 150."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["acreage"] < 150
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have acreage < 150."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (acres: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most farms with non-organic crops have a soil quality index less than 75."""
    non_org = df[df["organic"] == "no"]
    if non_org.empty:
        truth = True
        expl = "No non-organic farms to evaluate; vacuously true."
    else:
        count = non_org.shape[0]
        good = (non_org["soil_quality_index"] < 75).sum()
        proportion = good / count
        truth = proportion > 0.5
        if truth:
            expl = f"{good}/{count} non-organic farms (>{proportion:.2f}) have soil quality < 75."
        else:
            expl = f"{good}/{count} non-organic farms (={proportion:.2f}) do not meet the threshold."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All farms with a fertilizer usage greater than 900 kg have organic crops."""
    high_fert = df[df["fertilizer_kg"] > 900]
    condition = high_fert["organic"] == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} farms with fertilizer > 900 kg are organic."
    else:
        viol = high_fert[~condition]
        expl = f"{len(viol)} farms violate the rule (organic: {', '.join(viol['organic'].tolist())})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a farm has a soil quality index greater than 75, then its yield is greater than 350 tons."""
    high_soil = df[df["soil_quality_index"] > 75]
    condition = high_soil["yield_tons"] > 350
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality > 75 have yield > 350 tons."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one farm with organic crops that has a yield greater than 450 tons."""
    exists = df[(df["organic"] == "yes") & (df["yield_tons"] > 450)].shape[0] > 0
    truth = exists
    if truth:
        expl = "At least one organic farm has yield > 450 tons."
    else:
        expl = "No organic farm has yield > 450 tons."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All farms with irrigation hours per week less than 12 have a yield less than 410 tons."""
    low_irrig = df[df["irrigation_hours_week"] < 12]
    condition = low_irrig["yield_tons"] < 410
    truth = condition.all()
    if truth:
        expl = f"All {len(low_irrig)} farms with irrigation < 12h have yield < 410 tons."
    else:
        viol = low_irrig[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a farm grows soybean, then its fertilizer usage is greater than 750 kg."""
    soy = df[df["crop_type"] == "soybean"]
    condition = soy["fertilizer_kg"] > 750
    truth = condition.all()
    if truth:
        expl = f"All {len(soy)} soybean farms have fertilizer > 750 kg."
    else:
        viol = soy[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most farms with a yield greater than 400 tons have a soil quality index greater than 70."""
    high_yield = df[df["yield_tons"] > 400]
    if high_yield.empty:
        truth = True
        expl = "No farms with yield > 400 to evaluate; vacuously true."
    else:
        count = high_yield.shape[0]
        good = (high_yield["soil_quality_index"] > 70).sum()
        proportion = good / count
        truth = proportion > 0.5
        if truth:
            expl = f"{good}/{count} farms with yield > 400 have soil quality > 70 (>{proportion:.2f})."
        else:
            expl = f"{good}/{count} farms with yield > 400 have soil quality > 70 (={proportion:.2f})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_98.csv")

    # Convert numeric columns safely
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