import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All wheat farms are non-organic."""
    wheat = df[df["crop_type"] == "wheat"]
    condition = wheat["organic"] == "no"
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat farms are non-organic."
    else:
        viol = wheat[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} wheat farms are organic (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All rice farms receive at least 10.9 irrigation hours per week."""
    rice = df[df["crop_type"] == "rice"]
    condition = rice["irrigation_hours_week"] >= 10.9
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms receive at least 10.9 hours."
    else:
        viol = rice[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} rice farms receive less than 10.9 hours (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All soybean farms produce at least 284.6 tons of yield."""
    soy = df[df["crop_type"] == "soybean"]
    condition = soy["yield_tons"] >= 284.6
    truth = condition.all()
    if truth:
        expl = f"All {len(soy)} soybean farms produce at least 284.6 tons."
    else:
        viol = soy[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} soybean farms produce less than 284.6 tons (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All farms with soil_quality_index of at least 80 are either wheat or rice."""
    high_sqi = df[df["soil_quality_index"] >= 80]
    condition = high_sqi["crop_type"].isin(["wheat", "rice"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_sqi)} farms with SQI ≥ 80 grow wheat or rice."
    else:
        viol = high_sqi[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} farms with SQI ≥ 80 grow other crops (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All farms irrigated more than 18 hours per week grow either rice or soybean."""
    high_irrig = df[df["irrigation_hours_week"] > 18]
    condition = high_irrig["crop_type"].isin(["rice", "soybean"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_irrig)} farms with >18 hrs/week irrigation grow rice or soybean."
    else:
        viol = high_irrig[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} farms with >18 hrs/week irrigation grow other crops (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All farms using more than 1000 kg of fertilizer cultivate wheat or rice."""
    high_fert = df[df["fertilizer_kg"] > 1000]
    condition = high_fert["crop_type"].isin(["wheat", "rice"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fert)} farms using >1000 kg fertilizer grow wheat or rice."
    else:
        viol = high_fert[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} farms using >1000 kg fertilizer grow other crops (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All farms larger than 130 acres cultivate wheat or corn."""
    large_acre = df[df["acreage"] > 130]
    condition = large_acre["crop_type"].isin(["wheat", "corn"])
    truth = condition.all()
    if truth:
        expl = f"All {len(large_acre)} farms >130 acres grow wheat or corn."
    else:
        viol = large_acre[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} farms >130 acres grow other crops (IDs: {', '.join(viol_ids)})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All rice farms have a yield per acre between 2.35 and 4.96 tons."""
    rice = df[df["crop_type"] == "rice"]
    yield_per_acre = rice["yield_tons"] / rice["acreage"]
    condition = yield_per_acre.between(2.35, 4.96, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice farms have yield per acre between 2.35 and 4.96 tons."
    else:
        viol = rice[~condition]
        viol_ids = viol["farm_id"].tolist()
        expl = f"{len(viol)} rice farms violate the yield per acre range (IDs: {', '.join(viol_ids)})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_48.csv")

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()