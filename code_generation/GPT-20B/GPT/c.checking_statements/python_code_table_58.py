import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all organic farms, the soil quality index is at least 72.4."""
    organic = df[df["organic"] == "yes"]
    if organic.empty:
        return True, "No organic farms present; statement vacuously true."
    condition = organic["soil_quality_index"] >= 72.4
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have soil quality index >= 72.4."
    else:
        viol = organic[~condition]
        expl = f"{len(viol)} organic farms violate the rule (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all corn farms, the soil quality index is at least 72.3."""
    corn = df[df["crop_type"] == "corn"]
    if corn.empty:
        return True, "No corn farms present; statement vacuously true."
    condition = corn["soil_quality_index"] >= 72.3
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms have soil quality index >= 72.3."
    else:
        viol = corn[~condition]
        expl = f"{len(viol)} corn farms violate the rule (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all wheat farms, irrigation hours per week are at least 12.6."""
    wheat = df[df["crop_type"] == "wheat"]
    if wheat.empty:
        return True, "No wheat farms present; statement vacuously true."
    condition = wheat["irrigation_hours_week"] >= 12.6
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have irrigation hours >= 12.6."
    else:
        viol = wheat[~condition]
        expl = f"{len(viol)} wheat farms violate the rule (hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all rice farms, irrigation hours per week do not exceed 18.3."""
    rice = df[df["crop_type"] == "rice"]
    if rice.empty:
        return True, "No rice farms present; statement vacuously true."
    condition = rice["irrigation_hours_week"] <= 18.3
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have irrigation hours <= 18.3."
    else:
        viol = rice[~condition]
        expl = f"{len(viol)} rice farms violate the rule (hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all farms irrigating at least 15 hours per week, the yield is at least 260.7 tons."""
    irrig = df[df["irrigation_hours_week"] >= 15]
    if irrig.empty:
        return True, "No farms irrigate >= 15 hours/week; statement vacuously true."
    condition = irrig["yield_tons"] >= 260.7
    truth = condition.all()
    if truth:
        expl = f"All {len(irrig)} farms with >=15 irrigation hours have yield >= 260.7 tons."
    else:
        viol = irrig[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all farms that use more than 1000 kg of fertilizer, the yield is at least 304.7 tons."""
    fert = df[df["fertilizer_kg"] > 1000]
    if fert.empty:
        return True, "No farms use >1000 kg fertilizer; statement vacuously true."
    condition = fert["yield_tons"] >= 304.7
    truth = condition.all()
    if truth:
        expl = f"All {len(fert)} farms with >1000 kg fertilizer have yield >= 304.7 tons."
    else:
        viol = fert[~condition]
        expl = f"{len(viol)} farms violate the rule (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. The soybean farm with 78 acres has the highest yield per acre (about 5.9 tons per acre) among all farms."""
    soy_78 = df[(df["crop_type"] == "soybean") & (df["acreage"] == 78)]
    if soy_78.empty:
        return False, "No soybean farm with 78 acres found."
    # compute yield per acre for all farms
    df["yield_per_acre"] = df["yield_tons"] / df["acreage"]
    max_yield_per_acre = df["yield_per_acre"].max()
    target_yield_per_acre = soy_78["yield_per_acre"].iloc[0]
    truth = target_yield_per_acre == max_yield_per_acre
    if truth:
        expl = f"Soybean farm with 78 acres has yield per acre {target_yield_per_acre:.2f} which is the maximum."
    else:
        expl = f"Soybean farm with 78 acres has yield per acre {target_yield_per_acre:.2f}, but the maximum is {max_yield_per_acre:.2f}."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all soybean farms, yield per acre exceeds 2.8 tons."""
    soy = df[df["crop_type"] == "soybean"]
    if soy.empty:
        return True, "No soybean farms present; statement vacuously true."
    soy["yield_per_acre"] = soy["yield_tons"] / soy["acreage"]
    condition = soy["yield_per_acre"] > 2.8
    truth = condition.all()
    if truth:
        expl = f"All {len(soy)} soybean farms have yield per acre > 2.8 tons."
    else:
        viol = soy[~condition]
        expl = f"{len(viol)} soybean farms violate the rule (yields per acre: {', '.join(map(str, viol['yield_per_acre'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_58.csv")

    # Convert numeric columns safely
    for col in df.columns:
        if col not in ["crop_type", "organic"]:
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
        truth, explanation = func(df.copy())
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()