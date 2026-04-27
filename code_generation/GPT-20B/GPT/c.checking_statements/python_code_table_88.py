import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All organic farms have a soil quality index of at least 68.0."""
    organic = df[df["organic"] == "yes"]
    condition = organic["soil_quality_index"] >= 68.0
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms meet the soil quality requirement."
    else:
        viol = organic[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} organic farms violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All corn farms use at least 622 kg of fertilizer."""
    corn = df[df["crop_type"] == "corn"]
    condition = corn["fertilizer_kg"] >= 622
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms use at least 622 kg of fertilizer."
    else:
        viol = corn[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} corn farms violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all wheat farms, irrigation hours per week are between 13.2 and 20.1 inclusive."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["irrigation_hours_week"].between(13.2, 20.1, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have irrigation hours within the specified range."
    else:
        viol = wheat[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} wheat farms violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All rice farms have a total yield of at least 342.7 tons."""
    rice = df[df["crop_type"] == "rice"]
    condition = rice["yield_tons"] >= 342.7
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms meet the yield requirement."
    else:
        viol = rice[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} rice farms violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Soybean farms have acreage between 89 and 155 acres."""
    soybean = df[df["crop_type"] == "soybean"]
    condition = soybean["acreage"].between(89, 155, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean)} soybean farms have acreage within the specified range."
    else:
        viol = soybean[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} soybean farms violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most farms (80% of the records) are certified organic."""
    total = len(df)
    organic_count = (df["organic"] == "yes").sum()
    proportion = organic_count / total
    truth = proportion >= 0.8
    if truth:
        expl = f"{organic_count}/{total} farms ({proportion:.2%}) are organic."
    else:
        expl = f"{organic_count}/{total} farms ({proportion:.2%}) are organic, which is less than 80%."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All non-organic farms receive at least 16.8 irrigation hours per week."""
    non_organic = df[df["organic"] == "no"]
    condition = non_organic["irrigation_hours_week"] >= 16.8
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic)} non-organic farms meet the irrigation requirement."
    else:
        viol = non_organic[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} non-organic farms violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All non-rice farms have a yield per acre of no more than 3.842 tons."""
    non_rice = df[df["crop_type"]!= "rice"].copy()
    non_rice["yield_per_acre"] = non_rice["yield_tons"] / non_rice["acreage"]
    condition = non_rice["yield_per_acre"] <= 3.842
    truth = condition.all()
    if truth:
        expl = f"All {len(non_rice)} non-rice farms have yield per acre <= 3.842."
    else:
        viol = non_rice[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} non-rice farms violate the rule (IDs: {', '.join(viol_ids)})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_88.csv")

    # Convert numeric columns
    for col in df.columns:
        if col not in ["organic", "crop_type", "farm_id"]:
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()