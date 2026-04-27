import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All wheat farms are non-organic."""
    wheat_farms = df[df["crop_type"] == "wheat"]
    condition = (wheat_farms["organic"] == "no")
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat_farms)} wheat farms are non-organic."
    else:
        viol = wheat_farms[~condition]
        expl = f"{len(viol)} wheat farms are organic (IDs: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All rice farms receive at least 10.9 irrigation hours per week."""
    rice_farms = df[df["crop_type"] == "rice"]
    condition = (rice_farms["irrigation_hours_week"] >= 10.9)
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms receive at least 10.9 irrigation hours per week."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms receive less than 10.9 irrigation hours per week (IDs: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All soybean farms produce at least 284.6 tons of yield."""
    soybean_farms = df[df["crop_type"] == "soybean"]
    condition = (soybean_farms["yield_tons"] >= 284.6)
    truth = condition.all()
    if truth:
        expl = f"All {len(soybean_farms)} soybean farms produce at least 284.6 tons of yield."
    else:
        viol = soybean_farms[~condition]
        expl = f"{len(viol)} soybean farms produce less than 284.6 tons of yield (IDs: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All farms with soil_quality_index of at least 80 are either wheat or rice."""
    high_soil_farms = df[df["soil_quality_index"] >= 80]
    condition = (high_soil_farms["crop_type"].isin(["wheat", "rice"]))
    truth = condition.all()
    if truth:
        expl = f"All {len(high_soil_farms)} farms with soil quality index >= 80 are wheat or rice."
    else:
        viol = high_soil_farms[~condition]
        expl = f"{len(viol)} farms with soil quality index >= 80 are not wheat or rice (IDs: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms irrigated more than 18 hours per week grow either rice or soybean."""
    high_irrigation_farms = df[df["irrigation_hours_week"] > 18]
    condition = (high_irrigation_farms["crop_type"].isin(["rice", "soybean"]))
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrigation_farms)} farms irrigated more than 18 hours per week grow rice or soybean."
    else:
        viol = high_irrigation_farms[~condition]
        expl = f"{len(viol)} farms irrigated more than 18 hours per week do not grow rice or soybean (IDs: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All farms using more than 1000 kg of fertilizer cultivate wheat or rice."""
    high_fert_farms = df[df["fertilizer_kg"] > 1000]
    condition = (high_fert_farms["crop_type"].isin(["wheat", "rice"]))
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert_farms)} farms using more than 1000 kg of fertilizer cultivate wheat or rice."
    else:
        viol = high_fert_farms[~condition]
        expl = f"{len(viol)} farms using more than 1000 kg of fertilizer do not cultivate wheat or rice (IDs: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All farms larger than 130 acres cultivate wheat or corn."""
    large_farms = df[df["acreage"] > 130]
    condition = (large_farms["crop_type"].isin(["wheat", "corn"]))
    truth = condition.all()
    if truth:
        expl = f"All {len(large_farms)} farms larger than 130 acres cultivate wheat or corn."
    else:
        viol = large_farms[~condition]
        expl = f"{len(viol)} farms larger than 130 acres do not cultivate wheat or corn (IDs: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All rice farms have a yield per acre between 2.35 and 4.96 tons."""
    rice_farms = df[df["crop_type"] == "rice"]
    yield_per_acre = rice_farms["yield_tons"] / rice_farms["acreage"]
    condition = yield_per_acre.between(2.35, 4.96, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(rice_farms)} rice farms have yield per acre between 2.35 and 4.96 tons."
    else:
        viol = rice_farms[~condition]
        expl = f"{len(viol)} rice farms have yield per acre outside 2.35-4.96 tons range (IDs: {', '.join(viol['farm_id'].tolist())})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_48.csv")

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