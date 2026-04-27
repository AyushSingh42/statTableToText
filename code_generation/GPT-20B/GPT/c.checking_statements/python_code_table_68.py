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
        expl = f"All {len(organic)} organic farms satisfy the condition."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil_quality_index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All non-organic farms have soil_quality_index <= 79.6."""
    non_organic = df[df["organic"] == "no"]
    condition = non_organic["soil_quality_index"] <= 79.6
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic)} non-organic farms satisfy the condition."
    else:
        viol = non_organic[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (soil_quality_index: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All corn farms have irrigation_hours_week >= 13.9."""
    corn = df[df["crop_type"] == "corn"]
    condition = corn["irrigation_hours_week"] >= 13.9
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms satisfy the condition."
    else:
        viol = corn[~condition]
        expl = f"{len(viol)} corn farms violate the rule (irrigation_hours_week: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All wheat farms have yield_tons <= 405.1."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["yield_tons"] <= 405.1
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms satisfy the condition."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (yield_tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All rice farms have acreage between 78 and 117 acres."""
    rice = df[df["crop_type"] == "rice"]
    condition = rice["acreage"].between(78, 117, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms satisfy the condition."
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
        expl = f"All {len(soybean)} soybean farms satisfy the condition."
    else:
        viol = soybean[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (fertilizer_kg: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All farms with irrigation_hours_week > 18 have yield_tons >= 311.7."""
    high_irrig = df[df["irrigation_hours_week"] > 18]
    condition = high_irrig["yield_tons"] >= 311.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrig)} farms with irrigation_hours_week > 18 satisfy the condition."
    else:
        viol = high_irrig[~condition]
        expl = f"{len(viol)} farms violate the rule (yield_tons: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All farms with soil_quality_index >= 80 are organic."""
    high_soil = df[df["soil_quality_index"] >= 80]
    condition = high_soil["organic"] == "yes"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil)} farms with soil_quality_index >= 80 are organic."
    else:
        viol = high_soil[~condition]
        expl = f"{len(viol)} farms violate the rule (organic: {', '.join(map(str, viol['organic'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most farms have soil_quality_index >= 70."""
    total = len(df)
    count = df[df["soil_quality_index"] >= 70].shape[0]
    proportion = count / total
    truth = proportion > 0.5
    percent = round(proportion * 100, 1)
    if truth:
        expl = f"{count} out of {total} farms have soil_quality_index >= 70 ({percent}%)."
    else:
        expl = f"Only {count} out of {total} farms have soil_quality_index >= 70 ({percent}%)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_68.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()