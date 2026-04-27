import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all organic farms, soil quality index is at least 69.6."""
    organic = df[df["organic"].str.lower() == "yes"]
    condition = organic["soil_quality_index"] >= 69.6
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have soil quality index >= 69.6."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all non-organic farms, soil quality index does not exceed 81.0."""
    non_organic = df[df["organic"].str.lower() == "no"]
    condition = non_organic["soil_quality_index"] <= 81.0
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic)} non-organic farms have soil quality index <= 81.0."
    else:
        viol = non_organic[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All corn farms use between 626 and 817 kg of fertilizer."""
    corn = df[df["crop_type"].str.lower() == "corn"]
    condition = corn["fertilizer_kg"].between(626, 817, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms use fertilizer between 626 and 817 kg."
    else:
        viol = corn[~condition]
        expl = f"{len(viol)} corn farms violate the rule (fertilizer: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All wheat farms have soil quality index of at least 71.5."""
    wheat = df[df["crop_type"].str.lower() == "wheat"]
    condition = wheat["soil_quality_index"] >= 71.5
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have soil quality index >= 71.5."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All wheat farms yield at most 458.9 tons."""
    wheat = df[df["crop_type"].str.lower() == "wheat"]
    condition = wheat["yield_tons"] <= 458.9
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have yield <= 458.9 tons."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All rice farms have acreage of at least 101 acres."""
    rice = df[df["crop_type"].str.lower() == "rice"]
    condition = rice["acreage"] >= 101
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have acreage >= 101 acres."
    else:
        viol = rice[~condition]
        expl = f"{len(viol)} rice farms violate the rule (acres: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All farms irrigating more than 18 hours per week yield at least 382.4 tons."""
    irrig = df[df["irrigation_hours_week"] > 18]
    condition = irrig["yield_tons"] >= 382.4
    truth = condition.all()
    if truth:
        expl = f"All {len(irrig)} farms with >18 irrigation hours have yield >= 382.4 tons."
    else:
        viol = irrig[~condition]
        expl = f"{len(viol)} farms with >18 irrigation hours violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most soybean farms irrigate less than 16 hours per week."""
    soybean = df[df["crop_type"].str.lower() == "soybean"]
    if len(soybean) == 0:
        return True, "No soybean farms present; statement vacuously true."
    count_less = soybean[soybean["irrigation_hours_week"] < 16].shape[0]
    proportion = count_less / len(soybean)
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of soybean farms irrigate <16 hours."
    else:
        expl = f"Only {proportion*100:.1f}% of soybean farms irrigate <16 hours."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most farms have soil quality index greater than 70."""
    if df.shape[0] == 0:
        return True, "No farms present; statement vacuously true."
    count_gt = df[df["soil_quality_index"] > 70].shape[0]
    proportion = count_gt / df.shape[0]
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of farms have soil quality index > 70."
    else:
        expl = f"Only {proportion*100:.1f}% of farms have soil quality index > 70."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_18.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()