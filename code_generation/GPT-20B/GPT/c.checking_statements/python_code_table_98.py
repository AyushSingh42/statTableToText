import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All rice fields have a soil quality index between 69.2 and 78.4."""
    rice = df[df["crop_type"] == "rice"]
    if rice.empty:
        return True, "No rice fields present; condition holds vacuously."
    condition = rice["soil_quality_index"].between(69.2, 78.4, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(rice)} rice fields satisfy the soil quality index range."
    else:
        viol = rice[~condition]
        viol_indices = viol.index.tolist()
        viol_values = viol["soil_quality_index"].tolist()
        expl = f"{len(viol)} rice fields violate the range (indices {viol_indices}, values {viol_values})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a field’s yield exceeds 440 tons, the crop type is soybean."""
    high_yield = df[df["yield_tons"] > 440]
    if high_yield.empty:
        return True, "No fields exceed 440 tons; condition holds vacuously."
    condition = high_yield["crop_type"] == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_yield)} high-yield fields are soybean."
    else:
        viol = high_yield[~condition]
        viol_indices = viol.index.tolist()
        viol_crops = viol["crop_type"].tolist()
        expl = f"{len(viol)} high-yield fields are not soybean (indices {viol_indices}, crops {viol_crops})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For fields with acreage of at least 140 acres, the yield does not exceed 414.5 tons."""
    large_acreage = df[df["acreage"] >= 140]
    if large_acreage.empty:
        return True, "No fields with acreage >= 140; condition holds vacuously."
    condition = large_acreage["yield_tons"] <= 414.5
    truth = condition.all()
    if truth:
        expl = f"All {len(large_acreage)} large-acreage fields have yield <= 414.5 tons."
    else:
        viol = large_acreage[~condition]
        viol_indices = viol.index.tolist()
        viol_yields = viol["yield_tons"].tolist()
        expl = f"{len(viol)} large-acreage fields exceed 414.5 tons (indices {viol_indices}, yields {viol_yields})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All wheat fields receive no more than 13.2 irrigation hours per week."""
    wheat = df[df["crop_type"] == "wheat"]
    if wheat.empty:
        return True, "No wheat fields present; condition holds vacuously."
    condition = wheat["irrigation_hours_week"] <= 13.2
    truth = condition.all()
    if truth:
        expl = f"All {len(wheat)} wheat fields have irrigation <= 13.2 hours."
    else:
        viol = wheat[~condition]
        viol_indices = viol.index.tolist()
        viol_hours = viol["irrigation_hours_week"].tolist()
        expl = f"{len(viol)} wheat fields exceed 13.2 hours (indices {viol_indices}, hours {viol_hours})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a field is organic, its soil quality index is at least 68.2."""
    organic = df[df["organic"].str.lower() == "yes"]
    if organic.empty:
        return True, "No organic fields present; condition holds vacuously."
    condition = organic["soil_quality_index"] >= 68.2
    truth = condition.all()
    if truth:
        expl = f"All {len(organic)} organic fields have soil quality index >= 68.2."
    else:
        viol = organic[~condition]
        viol_indices = viol.index.tolist()
        viol_values = viol["soil_quality_index"].tolist()
        expl = f"{len(viol)} organic fields violate the threshold (indices {viol_indices}, values {viol_values})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Corn fields have a soil quality index ranging from 69.5 to 82.0."""
    corn = df[df["crop_type"] == "corn"]
    if corn.empty:
        return True, "No corn fields present; condition holds vacuously."
    condition = corn["soil_quality_index"].between(69.5, 82.0, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(corn)} corn fields satisfy the soil quality index range."
    else:
        viol = corn[~condition]
        viol_indices = viol.index.tolist()
        viol_values = viol["soil_quality_index"].tolist()
        expl = f"{len(viol)} corn fields violate the range (indices {viol_indices}, values {viol_values})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a field uses more than 1000 kg of fertilizer, the crop is soybean."""
    high_fertilizer = df[df["fertilizer_kg"] > 1000]
    if high_fertilizer.empty:
        return True, "No fields use >1000 kg fertilizer; condition holds vacuously."
    condition = high_fertilizer["crop_type"] == "soybean"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_fertilizer)} high-fertilizer fields are soybean."
    else:
        viol = high_fertilizer[~condition]
        viol_indices = viol.index.tolist()
        viol_crops = viol["crop_type"].tolist()
        expl = f"{len(viol)} high-fertilizer fields are not soybean (indices {viol_indices}, crops {viol_crops})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most fields have a yield per acre below 4.0 tons."""
    df = df.copy()
    df["yield_per_acre"] = df["yield_tons"] / df["acreage"]
    condition = df["yield_per_acre"] < 4.0
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of fields have yield per acre < 4.0 tons."
    else:
        expl = f"Only {proportion*100:.1f}% of fields have yield per acre < 4.0 tons; condition fails."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_98.csv")

    # Convert numeric columns safely
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