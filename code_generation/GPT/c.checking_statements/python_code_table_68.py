import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All organic farms have soil_quality_index >= 68.9."""
    organic = df[df["organic"] == "yes"]
    condition = organic["soil_quality_index"] >= 68.9
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have soil quality index >= 68.9."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All non-organic farms have soil_quality_index <= 79.6."""
    non_organic = df[df["organic"] == "no"]
    condition = non_organic["soil_quality_index"] <= 79.6
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic)} non-organic farms have soil quality index <= 79.6."
    else:
        viol = non_organic[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (soil quality index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All corn farms have irrigation_hours_week >= 13.9."""
    corn = df[df["crop_type"] == "corn"]
    condition = corn["irrigation_hours_week"] >= 13.9
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms have irrigation hours per week >= 13.9."
    else:
        viol = corn[~condition]
        expl = f"{len(viol)} corn farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All wheat farms have yield_tons <= 405.1."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["yield_tons"] <= 405.1
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have yield tons <= 405.1."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yield tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All rice farms have acreage between 78 and 117 acres."""
    rice = df[df["crop_type"] == "rice"]
    condition = rice["acreage"].between(78, 117, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have acreage between 78 and 117 acres."
    else:
        viol = rice[~condition]
        expl = f"{len(viol)} rice farms violate the rule (acreage: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All soybean farms use fertilizer_kg <= 801."""
    soybean = df[df["crop_type"] == "soybean"]
    condition = soybean["fertilizer_kg"] <= 801
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean)} soybean farms use fertilizer kg <= 801."
    else:
        viol = soybean[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (fertilizer kg: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All farms with irrigation_hours_week > 18 have yield_tons >= 311.7."""
    high_irrigation = df[df["irrigation_hours_week"] > 18]
    condition = high_irrigation["yield_tons"] >= 311.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation)} farms with irrigation hours > 18 have yield tons >= 311.7."
    else:
        viol = high_irrigation[~condition]
        expl = f"{len(viol)} farms with irrigation hours > 18 violate the rule (yield tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All farms with soil_quality_index >= 80 are organic."""
    high_soil = df[df["soil_quality_index"] >= 80]
    condition = high_soil["organic"] == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil quality index >= 80 are organic."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms with soil quality index >= 80 are not organic (farm IDs: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most farms have soil_quality_index >= 70."""
    total_farms = len(df)
    condition = df["soil_quality_index"] >= 70
    count_ge_70 = condition.sum()
    truth = count_ge_70 > total_farms / 2
    if truth:
        expl = f"{count_ge_70} out of {total_farms} farms have soil quality index >= 70 (more than half)."
    else:
        expl = f"{count_ge_70} out of {total_farms} farms have soil quality index >= 70 (not more than half)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_68.csv")

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
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()