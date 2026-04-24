import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All organic farms grow soybean."""
    organic_farms = df[df["organic"] == True]
    condition = organic_farms["crop_type"] == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(organic_farms)} organic farms grow soybean."
    else:
        viol = organic_farms[~condition]
        expl = f"{len(viol)} organic farms do not grow soybean (crop types: {', '.join(viol['crop_type'].unique())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All soybean farms are organic."""
    soy_farms = df[df["crop_type"] == "soybean"]
    condition = soy_farms["organic"] == True
    truth = condition.all()
    if truth:
        expl = f"All {len(soy_farms)} soybean farms are organic."
    else:
        viol = soy_farms[~condition]
        expl = f"{len(viol)} soybean farms are not organic (farm IDs: {', '.join(map(str, viol['farm_id'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All wheat farms have irrigation between 13.7 and 14.8 hours per week."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["irrigation_hours_week"].between(13.7, 14.8, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms meet the irrigation range."
    else:
        viol = wheat[~condition]
        vals = viol["irrigation_hours_week"].round(2).tolist()
        expl = f"{len(viol)} wheat farms violate the range (values: {', '.join(map(str, vals))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All corn farms have irrigation between 16.5 and 17.4 hours per week."""
    corn = df[df["crop_type"] == "corn"]
    condition = corn["irrigation_hours_week"].between(16.5, 17.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms meet the irrigation range."
    else:
        viol = corn[~condition]
        vals = viol["irrigation_hours_week"].round(2).tolist()
        expl = f"{len(viol)} corn farms violate the range (values: {', '.join(map(str, vals))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All rice farms have irrigation between 19.2 and 20.5 hours per week."""
    rice = df[df["crop_type"] == "rice"]
    condition = rice["irrigation_hours_week"].between(19.2, 20.5, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms meet the irrigation range."
    else:
        viol = rice[~condition]
        vals = viol["irrigation_hours_week"].round(2).tolist()
        expl = f"{len(viol)} rice farms violate the range (values: {', '.join(map(str, vals))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All organic farms have a soil quality index of at least 78.1."""
    organic = df[df["organic"] == True]
    condition = organic["soil_quality_index"] >= 78.1
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic farms have soil_quality_index ≥ 78.1."
    else:
        viol = organic[~condition]
        vals = viol["soil_quality_index"].round(2).tolist()
        expl = f"{len(viol)} organic farms fall below the threshold (values: {', '.join(map(str, vals))})."
    return truth, expl

def _yield_per_acre(df: pd.DataFrame):
    # Helper to compute yield per acre, handling division by zero
    return df["yield_tons"] / df["acreage"].replace({0: pd.NA})

def stmt_7(df: pd.DataFrame):
    """7. All soybean farms have a yield per acre of at most 2.72 tons."""
    soy = df[df["crop_type"] == "soybean"]
    ypa = _yield_per_acre(soy)
    condition = ypa <= 2.72
    truth = condition.all()
    if truth:
        expl = f"All {len(soy)} soybean farms have yield/acre ≤ 2.72 tons."
    else:
        viol = soy[~condition]
        vals = (ypa[~condition].round(3)).tolist()
        expl = f"{len(viol)} soybean farms exceed the limit (yield/acre: {', '.join(map(str, vals))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All rice farms have a yield per acre of at least 4.166 tons."""
    rice = df[df["crop_type"] == "rice"]
    ypa = _yield_per_acre(rice)
    condition = ypa >= 4.166
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have yield/acre ≥ 4.166 tons."
    else:
        viol = rice[~condition]
        vals = (ypa[~condition].round(3)).tolist()
        expl = f"{len(viol)} rice farms fall below the threshold (yield/acre: {', '.join(map(str, vals))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All wheat farms have a yield per acre between 3.36 and 3.65 tons."""
    wheat = df[df["crop_type"] == "wheat"]
    ypa = _yield_per_acre(wheat)
    condition = ypa.between(3.36, 3.65, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms have yield/acre within 3.36–3.65 tons."
    else:
        viol = wheat[~condition]
        vals = (ypa[~condition].round(3)).tolist()
        expl = f"{len(viol)} wheat farms violate the range (yield/acre: {', '.join(map(str, vals))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All corn farms have a yield per acre between 3.48 and 4.09 tons."""
    corn = df[df["crop_type"] == "corn"]
    ypa = _yield_per_acre(corn)
    condition = ypa.between(3.48, 4.09, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn farms have yield/acre within 3.48–4.09 tons."
    else:
        viol = corn[~condition]
        vals = (ypa[~condition].round(3)).tolist()
        expl = f"{len(viol)} corn farms violate the range (yield/acre: {', '.join(map(str, vals))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_6.csv")
    # Convert numeric columns stored as strings to proper numeric types
    num_cols = ["acreage", "yield_tons", "irrigation_hours_week", "fertilizer_kg", "soil_quality_index"]
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    # Normalize organic column to boolean
    if df["organic"].dtype == object:
        df["organic"] = df["organic"].map({"True": True, "true": True, "False": False, "false": False, 1: True, 0: False})
    else:
        df["organic"] = df["organic"].astype(bool)

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