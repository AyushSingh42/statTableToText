import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All organic farms have a soil quality index of at least 68.0."""
    organic_farms = df[df["organic"] == "yes"]
    condition = organic_farms["soil_quality_index"] >= 68.0
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality index >= 68.0."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All corn farms use at least 622 kg of fertilizer."""
    corn_farms = df[df["crop_type"] == "corn"]
    condition = corn_farms["fertilizer_kg"] >= 622
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms use at least 622 kg of fertilizer."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (fertilizer amounts: {', '.join(map(str, viol['fertilizer_kg'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all wheat farms, irrigation hours per week are between 13.2 and 20.1 inclusive."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = wheat_farms["irrigation_hours_week"].between(13.2, 20.1, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have irrigation hours between 13.2 and 20.1."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All rice farms have a total yield of at least 342.7 tons."""
    rice_farms = df[df["crop_type"] == "rice"]
    condition = rice_farms["yield_tons"] >= 342.7
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have yield >= 342.7 tons."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Soybean farms have acreage between 89 and 155 acres."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    condition = soybean_farms["acreage"].between(89, 155, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have acreage between 89 and 155."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (acreages: {', '.join(map(str, viol['acreage'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most farms (80% of the records) are certified organic."""
    total_farms = len(df)
    organic_count = (df["organic"] == "yes").sum()
    percentage = (organic_count / total_farms) * 100
    truth = percentage >= 80
    expl = f"{organic_count} out of {total_farms} farms ({percentage:.1f}%) are organic."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All non-organic farms receive at least 16.8 irrigation hours per week."""
    non_organic_farms = df[df["organic"] == "no"]
    condition = non_organic_farms["irrigation_hours_week"] >= 16.8
    truth = condition.all()
    if truth:
        expl = f"All {len(non_organic_farms)} non-organic farms receive at least 16.8 irrigation hours/week."
    else:
        viol = non_organic_farms[~condition]
        expl = f"{len(viol)} non-organic farms violate the rule (irrigation hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All non-rice farms have a yield per acre of no more than 3.842 tons."""
    non_rice_farms = df[df["crop_type"]!= "rice"]
    yield_per_acre = non_rice_farms["yield_tons"] / non_rice_farms["acreage"]
    condition = yield_per_acre <= 3.842
    truth = condition.all()
    if truth:
        expl = f"All {len(non_rice_farms)} non-rice farms have yield per acre <= 3.842 tons."
    else:
        viol = non_rice_farms[~condition]
        expl = f"{len(viol)} non-rice farms violate the rule (yield per acre: {', '.join(map(str, viol['yield_tons']/viol['acreage']).tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_88.csv")

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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()