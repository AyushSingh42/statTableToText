import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all organic farms, the soil quality index is at least 72.4."""
    organic_farms = df[df["organic"] == "yes"]
    condition = organic_farms["soil_quality_index"] >= 72.4
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms have soil quality index >= 72.4."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms violate the rule (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all corn farms, the soil quality index is at least 72.3."""
    corn_farms = df[df["crop_type"] == "corn"]
    condition = corn_farms["soil_quality_index"] >= 72.3
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_farms)} corn farms have soil quality index >= 72.3."
    else:
        viol = corn_farms[~condition]
        expl = f"{len(viol)} corn farms violate the rule (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all wheat farms, irrigation hours per week are at least 12.6."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = wheat_farms["irrigation_hours_week"] >= 12.6
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms have irrigation hours >= 12.6."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all rice farms, irrigation hours per week do not exceed 18.3."""
    rice_farms = df[df["crop_type"] == "rice"]
    condition = rice_farms["irrigation_hours_week"] <= 18.3
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have irrigation hours <= 18.3."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms violate the rule (hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all farms irrigating at least 15 hours per week, the yield is at least 260.7 tons."""
    high_irrigation = df[df["irrigation_hours_week"] >= 15]
    condition = high_irrigation["yield_tons"] >= 260.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation)} high-irrigation farms have yield >= 260.7 tons."
    else:
        viol = high_irrigation[~condition]
        expl = f"{len(viol)} high-irrigation farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all farms that use more than 1000 kg of fertilizer, the yield is at least 304.7 tons."""
    high_fert = df[df["fertilizer_kg"] > 1000]
    condition = high_fert["yield_tons"] >= 304.7
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} high-fertilizer farms have yield >= 304.7 tons."
    else:
        viol = high_fert[~condition]
        expl = f"{len(viol)} high-fertilizer farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. The soybean farm with 78 acres has the highest yield per acre (about 5.9 tons per acre) among all farms."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    soybean_78 = soybean_farms[soybean_farms["acreage"] == 78]
    if len(soybean_78) == 0:
        return False, "No soybean farm with 78 acres found."

    yield_per_acre_78 = soybean_78.iloc[0]["yield_tons"] / soybean_78.iloc[0]["acreage"]
    max_yield_per_acre = (df["yield_tons"] / df["acreage"]).max()

    truth = abs(yield_per_acre_78 - max_yield_per_acre) < 0.1  # Allow small floating point difference
    if truth:
        expl = f"Soybean farm with 78 acres has yield per acre ({yield_per_acre_78:.1f}) which matches maximum yield per acre ({max_yield_per_acre:.1f})."
    else:
        expl = f"Soybean farm with 78 acres has yield per acre ({yield_per_acre_78:.1f}), but maximum yield per acre is ({max_yield_per_acre:.1f})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all soybean farms, yield per acre exceeds 2.8 tons."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    yield_per_acre = soybean_farms["yield_tons"] / soybean_farms["acreage"]
    condition = yield_per_acre > 2.8
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms have yield per acre > 2.8 tons."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yield per acre: {', '.join([f'{(r[1].yield_tons/r[1].acreage):.1f}' for r in viol.iterrows()])})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_58.csv")

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