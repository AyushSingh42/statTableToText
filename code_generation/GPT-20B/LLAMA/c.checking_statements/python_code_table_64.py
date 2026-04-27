import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All households with monthly income greater than 8k have a household size greater than 1."""
    subset = df[df["monthly_income_k"] > 8]
    truth = (subset["household_size"] > 1).all()
    if truth:
        expl = f"All {len(subset)} households with income > 8k have size > 1."
    else:
        viol = subset[subset["household_size"] <= 1]
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a household is in an urban region, then their monthly income is greater than 4k."""
    urban = df[df["region"] == "urban"]
    truth = (urban["monthly_income_k"] > 4).all()
    if truth:
        expl = f"All {len(urban)} urban households have income > 4k."
    else:
        viol = urban[urban["monthly_income_k"] <= 4]
        expl = f"{len(viol)} urban households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one household in a rural region with a monthly income greater than 8k."""
    exists = ((df["region"] == "rural") & (df["monthly_income_k"] > 8)).any()
    if exists:
        row = df[(df["region"] == "rural") & (df["monthly_income_k"] > 8)].iloc[0]
        expl = f"Household {row['household_id']} satisfies the condition."
    else:
        expl = "No rural household has income > 8k."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. All households with a household size of 1 have a monthly income greater than 4k."""
    size1 = df[df["household_size"] == 1]
    truth = (size1["monthly_income_k"] > 4).all()
    if truth:
        expl = f"All {len(size1)} households of size 1 have income > 4k."
    else:
        viol = size1[size1["monthly_income_k"] <= 4]
        expl = f"{len(viol)} households of size 1 violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a household has a vehicle count of 3, then their monthly income is greater than 6k."""
    veh3 = df[df["vehicle_count"] == 3]
    truth = (veh3["monthly_income_k"] > 6).all()
    if truth:
        expl = f"All {len(veh3)} households with 3 vehicles have income > 6k."
    else:
        viol = veh3[veh3["monthly_income_k"] <= 6]
        expl = f"{len(viol)} households with 3 vehicles violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most households have a utility cost greater than 100."""
    proportion = (df["utility_cost"] > 100).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of households have utility cost > 100."
    else:
        expl = f"Only {proportion*100:.1f}% of households have utility cost > 100."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All households with a monthly income greater than 9k have a rent greater than 1k."""
    subset = df[df["monthly_income_k"] > 9]
    truth = (subset["rent_k"] > 1).all()
    if truth:
        expl = f"All {len(subset)} households with income > 9k have rent > 1k."
    else:
        viol = subset[subset["rent_k"] <= 1]
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a household has an internet type of fiber, then their monthly income is greater than 5k."""
    fiber = df[df["internet_type"] == "fiber"]
    truth = (fiber["monthly_income_k"] > 5).all()
    if truth:
        expl = f"All {len(fiber)} fiber households have income > 5k."
    else:
        viol = fiber[fiber["monthly_income_k"] <= 5]
        expl = f"{len(viol)} fiber households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one household in a suburban region with a monthly income greater than 9k."""
    exists = ((df["region"] == "suburban") & (df["monthly_income_k"] > 9)).any()
    if exists:
        row = df[(df["region"] == "suburban") & (df["monthly_income_k"] > 9)].iloc[0]
        expl = f"Household {row['household_id']} satisfies the condition."
    else:
        expl = "No suburban household has income > 9k."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All households with a household size greater than 5 have a vehicle count greater than 0."""
    subset = df[df["household_size"] > 5]
    truth = (subset["vehicle_count"] > 0).all()
    if truth:
        expl = f"All {len(subset)} households with size > 5 have vehicle count > 0."
    else:
        viol = subset[subset["vehicle_count"] <= 0]
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a household is in a rural region, then their utility cost is less than 200."""
    rural = df[df["region"] == "rural"]
    truth = (rural["utility_cost"] < 200).all()
    if truth:
        expl = f"All {len(rural)} rural households have utility cost < 200."
    else:
        viol = rural[rural["utility_cost"] >= 200]
        expl = f"{len(viol)} rural households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most households have a household size greater than 1."""
    proportion = (df["household_size"] > 1).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of households have size > 1."
    else:
        expl = f"Only {proportion*100:.1f}% of households have size > 1."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All households with a monthly income less than 5k have a household size greater than 1."""
    subset = df[df["monthly_income_k"] < 5]
    truth = (subset["household_size"] > 1).all()
    if truth:
        expl = f"All {len(subset)} households with income < 5k have size > 1."
    else:
        viol = subset[subset["household_size"] <= 1]
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a household has a rent greater than 2k, then their monthly income is greater than 8k."""
    high_rent = df[df["rent_k"] > 2]
    truth = (high_rent["monthly_income_k"] > 8).all()
    if truth:
        expl = f"All {len(high_rent)} households with rent > 2k have income > 8k."
    else:
        viol = high_rent[high_rent["monthly_income_k"] <= 8]
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one household with a vehicle count of 3 and a monthly income greater than 8k."""
    exists = ((df["vehicle_count"] == 3) & (df["monthly_income_k"] > 8)).any()
    if exists:
        row = df[(df["vehicle_count"] == 3) & (df["monthly_income_k"] > 8)].iloc[0]
        expl = f"Household {row['household_id']} satisfies the condition."
    else:
        expl = "No household with 3 vehicles has income > 8k."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. All households with an internet type of satellite have a monthly income less than 9k."""
    sat = df[df["internet_type"] == "satellite"]
    truth = (sat["monthly_income_k"] < 9).all()
    if truth:
        expl = f"All {len(sat)} satellite households have income < 9k."
    else:
        viol = sat[sat["monthly_income_k"] >= 9]
        expl = f"{len(viol)} satellite households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a household has a utility cost greater than 150, then their household size is greater than 1."""
    high_util = df[df["utility_cost"] > 150]
    truth = (high_util["household_size"] > 1).all()
    if truth:
        expl = f"All {len(high_util)} households with utility > 150 have size > 1."
    else:
        viol = high_util[high_util["household_size"] <= 1]
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most households have a monthly income greater than 5k."""
    proportion = (df["monthly_income_k"] > 5).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of households have income > 5k."
    else:
        expl = f"Only {proportion*100:.1f}% of households have income > 5k."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All households with a household size of 6 have a monthly income greater than 6k."""
    size6 = df[df["household_size"] == 6]
    truth = (size6["monthly_income_k"] > 6).all()
    if truth:
        expl = f"All {len(size6)} households of size 6 have income > 6k."
    else:
        viol = size6[size6["monthly_income_k"] <= 6]
        expl = f"{len(viol)} households of size 6 violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a household is in an urban region, then their utility cost is greater than 80."""
    urban = df[df["region"] == "urban"]
    truth = (urban["utility_cost"] > 80).all()
    if truth:
        expl = f"All {len(urban)} urban households have utility cost > 80."
    else:
        viol = urban[urban["utility_cost"] <= 80]
        expl = f"{len(viol)} urban households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one household in a rural region with a household size of 6."""
    exists = ((df["region"] == "rural") & (df["household_size"] == 6)).any()
    if exists:
        row = df[(df["region"] == "rural") & (df["household_size"] == 6)].iloc[0]
        expl = f"Household {row['household_id']} satisfies the condition."
    else:
        expl = "No rural household has size 6."
    return exists, expl

def stmt_22(df: pd.DataFrame):
    """22. All households with a monthly income greater than 10k have a rent greater than 1.5k."""
    subset = df[df["monthly_income_k"] > 10]
    truth = (subset["rent_k"] > 1.5).all()
    if truth:
        expl = f"All {len(subset)} households with income > 10k have rent > 1.5k."
    else:
        viol = subset[subset["rent_k"] <= 1.5]
        expl = f"{len(viol)} households violate the rule (ids: {', '.join(viol['household_id'])})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_64.csv")

    # Convert numeric columns safely
    for col in ["household_size", "monthly_income_k", "rent_k", "utility_cost", "vehicle_count"]:
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
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
        (18, stmt_18),
        (19, stmt_19),
        (20, stmt_20),
        (21, stmt_21),
        (22, stmt_22),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func