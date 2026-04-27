import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All organic farms have irrigation hours per week of at least 13.2."""
    organic = df[df["organic"] == "yes"]
    condition = organic["irrigation_hours_week"] >= 13.2
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have >= 13.2 irrigation hours/week."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All wheat farms have irrigation hours per week no more than 17.3."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["irrigation_hours_week"] <= 17.3
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have <= 17.3 irrigation hours/week."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All farms with a soil quality index of at least 80 have a yield of at least 334.8 tons."""
    high_soil = df[df["soil_quality_index"] >= 80]
    condition = high_soil["yield_tons"] >= 334.8
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality >= 80 have >= 334.8 yield."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms with soil quality >= 80 violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All farms with an acreage under 80 acres grow wheat."""
    small = df[df["acreage"] < 80]
    condition = small["crop_type"] == "wheat"
    truth = condition.all()
    if truth:
        expl = f"All {len(small)} farms with acreage < 80 grow wheat."
    else:
        viol = small[~condition]
        expl = f"{len(viol)} farms with acreage < 80 do not grow wheat (crops: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All soybean farms have a soil quality index between 74.9 and 75.3 inclusive."""
    soybean = df[df["crop_type"] == "soybean"]
    condition = df["soil_quality_index"].between(74.9, 75.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean)} soybean farms have soil quality between 74.9 and 75.3."
    else:
        viol = soybean[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (soil quality: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All non-organic farms have a soil quality index of at most 81.6."""
    non_org = df[df["organic"] == "no"]
    condition = non_org["soil_quality_index"] <= 81.6
    truth = condition.all()
    if truth:
        expl = f"All {len(non_org)} non-organic farms have soil quality <= 81.6."
    else:
        viol = non_org[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (soil quality: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All rice farms have irrigation hours per week of at most 20.4."""
    rice = df[df["crop_type"] == "rice"]
    condition = rice["irrigation_hours_week"] <= 20.4
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have <= 20.4 irrigation hours/week."
    else:
        viol = rice[~condition]
        expl = f"{len(viol)} rice farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All farms that use at least 1000 kg of fertilizer grow either rice or wheat."""
    high_fert = df[df["fertilizer_kg"] >= 1000]
    condition = (high_fert["crop_type"] == "rice") | (high_fert["crop_type"] == "wheat")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} farms with >= 1000 kg fertilizer grow rice or wheat."
    else:
        viol = high_fert[~condition]
        expl = f"{len(viol)} farms with >= 1000 kg fertilizer do not grow rice or wheat (crops: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All farms with irrigation greater than 18 hours per week are either rice or soybean."""
    high_irr = df[df["irrigation_hours_week"] > 18]
    condition = (high_irr["crop_type"] == "rice") | (high_irr["crop_type"] == "soybean")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irr)} farms with > 18 irrigation hours are rice or soybean."
    else:
        viol = high_irr[~condition]
        expl = f"{len(viol)} farms with > 18 irrigation hours are neither rice nor soybean (crops: {', '.join(map(str, viol['crop_type'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All organic farms use at least 898 kg of fertilizer."""
    organic = df[df["organic"] == "yes"]
    condition = organic["fertilizer_kg"] >= 898
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms use >= 898 kg fertilizer."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_8.csv")

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
        (10, stmt_10)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()