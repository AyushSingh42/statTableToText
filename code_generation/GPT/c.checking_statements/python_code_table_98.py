import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All rice fields have a soil quality index between 69.2 and 78.4."""
    rice_fields = df[df["crop_type"] == "rice"]
    condition = rice_fields["soil_quality_index"].between(69.2, 78.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_fields)} rice fields have soil quality index between 69.2 and 78.4."
    else:
        viol = rice_fields[~condition]
        expl = f"{len(viol)} rice fields violate the rule (soil quality indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a field’s yield exceeds 440 tons, the crop type is soybean."""
    high_yield = df[df["yield_tons"] > 440]
    condition = high_yield["crop_type"] == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield)} fields with yield > 440 tons are soybean."
    else:
        viol = high_yield[~condition]
        expl = f"{len(viol)} fields with yield > 440 tons are not soybean (crop types: {', '.join(viol['crop_type'].tolist())})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For fields with acreage of at least 140 acres, the yield does not exceed 414.5 tons."""
    large_acreage = df[df["acreage"] >= 140]
    condition = large_acreage["yield_tons"] <= 414.5
    truth = condition.all()
    if truth:
        expl = f"All {len(large_acreage)} fields with acreage >= 140 acres have yield <= 414.5 tons."
    else:
        viol = large_acreage[~condition]
        expl = f"{len(viol)} fields with acreage >= 140 acres exceed yield limit (yields: {', '.join(map(str, viol['yield_tons'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All wheat fields receive no more than 13.2 irrigation hours per week."""
    wheat_fields = df[df["crop_type"] == "wheat"]
    condition = wheat_fields["irrigation_hours_week"] <= 13.2
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_fields)} wheat fields receive <= 13.2 irrigation hours/week."
    else:
        viol = wheat_fields[~condition]
        expl = f"{len(viol)} wheat fields exceed irrigation limit (hours: {', '.join(map(str, viol['irrigation_hours_week'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a field is organic, its soil quality index is at least 68.2."""
    organic_fields = df[df["organic"] == "yes"]
    condition = organic_fields["soil_quality_index"] >= 68.2
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_fields)} organic fields have soil quality index >= 68.2."
    else:
        viol = organic_fields[~condition]
        expl = f"{len(viol)} organic fields have soil quality index < 68.2 (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Corn fields have a soil quality index ranging from 69.5 to 82.0."""
    corn_fields = df[df["crop_type"] == "corn"]
    condition = corn_fields["soil_quality_index"].between(69.5, 82.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(corn_fields)} corn fields have soil quality index between 69.5 and 82.0."
    else:
        viol = corn_fields[~condition]
        expl = f"{len(viol)} corn fields violate the range (indices: {', '.join(map(str, viol['soil_quality_index'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a field uses more than 1000 kg of fertilizer, the crop is soybean."""
    high_fert = df[df["fertilizer_kg"] > 1000]
    condition = high_fert["crop_type"] == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} fields with fertilizer > 1000 kg are soybean."
    else:
        viol = high_fert[~condition]
        expl = f"{len(viol)} fields with fertilizer > 1000 kg are not soybean (crop types: {', '.join(viol['crop_type'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most fields have a yield per acre below 4.0 tons."""
    df["yield_per_acre"] = df["yield_tons"] / df["acreage"]
    low_yield = df[df["yield_per_acre"] < 4.0]
    truth = len(low_yield) > len(df) / 2
    if truth:
        expl = f"{len(low_yield)} out of {len(df)} fields have yield per acre < 4.0 tons (more than half)."
    else:
        expl = f"{len(low_yield)} out of {len(df)} fields have yield per acre < 4.0 tons (not more than half)."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_98.csv")

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