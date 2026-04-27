import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All organic farms have irrigation hours per week of at least 13.2."""
    organic = df[df["organic"].str.lower() == "yes"]
    if organic.empty:
        return True, "No organic farms to check."
    condition = organic["irrigation_hours_week"] >= 13.2
    truth = condition.all()
    if truth:
        return True, f"All {len(organic)} organic farms have irrigation >= 13.2."
    viol = organic[~condition]
    viol_ids = viol["farm_id"].tolist()
    viol_vals = viol["irrigation_hours_week"].tolist()
    viol_str = ", ".join(f"{fid} ({val})" for fid, val in zip(viol_ids, viol_vals))
    return False, f"{len(viol)} organic farms violate the rule: {viol_str}."

def stmt_2(df: pd.DataFrame):
    """2. All wheat farms have irrigation hours per week no more than 17.3."""
    wheat = df[df["crop_type"].str.lower() == "wheat"]
    if wheat.empty:
        return True, "No wheat farms to check."
    condition = wheat["irrigation_hours_week"] <= 17.3
    truth = condition.all()
    if truth:
        return True, f"All {len(wheat)} wheat farms have irrigation <= 17.3."
    viol = wheat[~condition]
    viol_ids = viol["farm_id"].tolist()
    viol_vals = viol["irrigation_hours_week"].tolist()
    viol_str = ", ".join(f"{fid} ({val})" for fid, val in zip(viol_ids, viol_vals))
    return False, f"{len(viol)} wheat farms violate the rule: {viol_str}."

def stmt_3(df: pd.DataFrame):
    """3. All farms with a soil quality index of at least 80 have a yield of at least 334.8 tons."""
    high_soil = df[df["soil_quality_index"] >= 80]
    if high_soil.empty:
        return True, "No farms with soil quality index >= 80 to check."
    condition = high_soil["yield_tons"] >= 334.8
    truth = condition.all()
    if truth:
        return True, f"All {len(high_soil)} farms with soil_quality_index >= 80 have yield >= 334.8."
    viol = high_soil[~condition]
    viol_ids = viol["farm_id"].tolist()
    viol_vals = viol["yield_tons"].tolist()
    viol_str = ", ".join(f"{fid} ({val})" for fid, val in zip(viol_ids, viol_vals))
    return False, f"{len(viol)} farms violate the rule: {viol_str}."

def stmt_4(df: pd.DataFrame):
    """4. All farms with an acreage under 80 acres grow wheat."""
    small_acreage = df[df["acreage"] < 80]
    if small_acreage.empty:
        return True, "No farms with acreage < 80 to check."
    condition = small_acreage["crop_type"].str.lower() == "wheat"
    truth = condition.all()
    if truth:
        return True, f"All {len(small_acreage)} farms with acreage < 80 grow wheat."
    viol = small_acreage[~condition]
    viol_ids = viol["farm_id"].tolist()
    viol_crops = viol["crop_type"].tolist()
    viol_str = ", ".join(f"{fid} ({crop})" for fid, crop in zip(viol_ids, viol_crops))
    return False, f"{len(viol)} farms violate the rule: {viol_str}."

def stmt_5(df: pd.DataFrame):
    """5. All soybean farms have a soil quality index between 74.9 and 75.3 inclusive."""
    soy = df[df["crop_type"].str.lower() == "soybean"]
    if soy.empty:
        return True, "No soybean farms to check."
    condition = soy["soil_quality_index"].between(74.9, 75.3, inclusive="both")
    truth = condition.all()
    if truth:
        return True, f"All {len(soy)} soybean farms have soil_quality_index between 74.9 and 75.3."
    viol = soy[~condition]
    viol_ids = viol["farm_id"].tolist()
    viol_vals = viol["soil_quality_index"].tolist()
    viol_str = ", ".join(f"{fid} ({val})" for fid, val in zip(viol_ids, viol_vals))
    return False, f"{len(viol)} soybean farms violate the rule: {viol_str}."

def stmt_6(df: pd.DataFrame):
    """6. All non-organic farms have a soil quality index of at most 81.6."""
    non_org = df[df["organic"].str.lower() == "no"]
    if non_org.empty:
        return True, "No non-organic farms to check."
    condition = non_org["soil_quality_index"] <= 81.6
    truth = condition.all()
    if truth:
        return True, f"All {len(non_org)} non-organic farms have soil_quality_index <= 81.6."
    viol = non_org[~condition]
    viol_ids = viol["farm_id"].tolist()
    viol_vals = viol["soil_quality_index"].tolist()
    viol_str = ", ".join(f"{fid} ({val})" for fid, val in zip(viol_ids, viol_vals))
    return False, f"{len(viol)} non-organic farms violate the rule: {viol_str}."

def stmt_7(df: pd.DataFrame):
    """7. All rice farms have irrigation hours per week of at most 20.4."""
    rice = df[df["crop_type"].str.lower() == "rice"]
    if rice.empty:
        return True, "No rice farms to check."
    condition = rice["irrigation_hours_week"] <= 20.4
    truth = condition.all()
    if truth:
        return True, f"All {len(rice)} rice farms have irrigation <= 20.4."
    viol = rice[~condition]
    viol_ids = viol["farm_id"].tolist()
    viol_vals = viol["irrigation_hours_week"].tolist()
    viol_str = ", ".join(f"{fid} ({val})" for fid, val in zip(viol_ids, viol_vals))
    return False, f"{len(viol)} rice farms violate the rule: {viol_str}."

def stmt_8(df: pd.DataFrame):
    """8. All farms that use at least 1000 kg of fertilizer grow either rice or wheat."""
    high_fert = df[df["fertilizer_kg"] >= 1000]
    if high_fert.empty:
        return True, "No farms using >= 1000 kg fertilizer to check."
    condition = high_fert["crop_type"].str.lower().isin(["rice", "wheat"])
    truth = condition.all()
    if truth:
        return True, f"All {len(high_fert)} farms using >= 1000 kg fertilizer grow rice or wheat."
    viol = high_fert[~condition]
    viol_ids = viol["farm_id"].tolist()
    viol_crops = viol["crop_type"].tolist()
    viol_str = ", ".join(f"{fid} ({crop})" for fid, crop in zip(viol_ids, viol_crops))
    return False, f"{len(viol)} farms violate the rule: {viol_str}."

def stmt_9(df: pd.DataFrame):
    """9. All farms with irrigation greater than 18 hours per week are either rice or soybean."""
    high_irrig = df[df["irrigation_hours_week"] > 18]
    if high_irrig.empty:
        return True, "No farms with irrigation > 18 to check."
    condition = high_irrig["crop_type"].str.lower().isin(["rice", "soybean"])
    truth = condition.all()
    if truth:
        return True, f"All {len(high_irrig)} farms with irrigation > 18 grow rice or soybean."
    viol = high_irrig[~condition]
    viol_ids = viol["farm_id"].tolist()
    viol_crops = viol["crop_type"].tolist()
    viol_str = ", ".join(f"{fid} ({crop})" for fid, crop in zip(viol_ids, viol_crops))
    return False, f"{len(viol)} farms violate the rule: {viol_str}."

def stmt_10(df: pd.DataFrame):
    """10. All organic farms use at least 898 kg of fertilizer."""
    organic = df[df["organic"].str.lower() == "yes"]
    if organic.empty:
        return True, "No organic farms to check."
    condition = organic["fertilizer_kg"] >= 898
    truth = condition.all()
    if truth:
        return True, f"All {len(organic)} organic farms use >= 898 kg fertilizer."
    viol = organic[~condition]
    viol_ids = viol["farm_id"].tolist()
    viol_vals = viol["fertilizer_kg"].tolist()
    viol_str = ", ".join(f"{fid} ({val})" for fid, val in zip(viol_ids, viol_vals))
    return False, f"{len(viol)} organic farms violate the rule: {viol_str}."

def main():
    df = pd.read_csv("../inference_generation/tables/table_8.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()