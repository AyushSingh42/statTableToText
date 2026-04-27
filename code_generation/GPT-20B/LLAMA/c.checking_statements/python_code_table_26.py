import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are centers have an age greater than or equal to 23 years."""
    centers = df[df["position"] == "center"]
    condition = centers["age"] >= 23
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have age >= 23."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a forward, then their age is less than or equal to 32 years."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["age"] <= 32
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have age <= 32."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one guard whose assists per game are less than 2."""
    guards = df[df["position"] == "guard"]
    exists = (guards["assists_per_game"] < 2).any()
    if exists:
        count = guards[guards["assists_per_game"] < 2].shape[0]
        expl = f"Found {count} guard(s) with assists per game less than 2."
    else:
        expl = "No guard with assists per game less than 2 found."
    return exists, expl

def stmt_4(df: pd.DataFrame):
    """4. For all players with minutes per game greater than 30, their points per game are greater than or equal to 12."""
    condition = df[df["minutes_per_game"] > 30]["points_per_game"] >= 12
    truth = condition.all()
    if truth:
        expl = f"All players with minutes per game > 30 have points per game >= 12."
    else:
        viol = df[(df["minutes_per_game"] > 30) & (df["points_per_game"] < 12)]
        expl = f"{len(viol)} player(s) violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))}, points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All players who are centers have a rebounds per game greater than or equal to 3."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds per game >= 3."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a player is a forward aged 25 or less, then their points per game are greater than or equal to 14."""
    forwards = df[df["position"] == "forward"]
    viol = forwards[(forwards["age"] <= 25) & (forwards["points_per_game"] < 14)]
    truth = viol.empty
    if truth:
        expl = f"All forwards aged <= 25 have points per game >= 14."
    else:
        expl = f"{len(viol)} forward(s) violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))}, points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most players in the table have a games played greater than or equal to 70."""
    total = len(df)
    count = df[df["games_played"] >= 70].shape[0]
    proportion = count / total
    truth = proportion > 0.5
    expl = f"{count} out of {total} players have games played >= 70 ({proportion*100:.1f}%)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all players with age greater than 30, their assists per game are greater than or equal to 2."""
    condition = df[df["age"] > 30]["assists_per_game"] >= 2
    truth = condition.all()
    if truth:
        expl = f"All players with age > 30 have assists per game >= 2."
    else:
        viol = df[(df["age"] > 30) & (df["assists_per_game"] < 2)]
        expl = f"{len(viol)} player(s) violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))}, assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one center whose points per game are greater than 25."""
    centers = df[df["position"] == "center"]
    exists = (centers["points_per_game"] > 25).any()
    if exists:
        count = centers[centers["points_per_game"] > 25].shape[0]
        expl = f"Found {count} center(s) with points per game > 25."
    else:
        expl = "No center with points per game > 25 found."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. If a player is a guard, then their rebounds per game are greater than or equal to 6."""
    guards = df[df["position"] == "guard"]
    viol = guards[guards["rebounds_per_game"] < 6]
    truth = viol.empty
    if truth:
        expl = f"All guards have rebounds per game >= 6."
    else:
        expl = f"{len(viol)} guard(s) violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All players who are forwards have a height that is not provided in the data, but based on the position, it can be inferred that their height is likely greater than 180 cm."""
    # Height data not present; cannot verify inference
    truth = False
    expl = "Height data not available; cannot verify inference."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all players with points per game greater than 20, their minutes per game are greater than or equal to 25."""
    condition = df[df["points_per_game"] > 20]["minutes_per_game"] >= 25
    truth = condition.all()
    if truth:
        expl = f"All players with points per game > 20 have minutes per game >= 25."
    else:
        viol = df[(df["points_per_game"] > 20) & (df["minutes_per_game"] < 25)]
        expl = f"{len(viol)} player(s) violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))}, minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most players in the table have an assists per game less than 5."""
    total = len(df)
    count = df[df["assists_per_game"] < 5].shape[0]
    proportion = count / total
    truth = proportion > 0.5
    expl = f"{count} out of {total} players have assists per game < 5 ({proportion*100:.1f}%)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a player is a center aged 30 or more, then their rebounds per game are greater than or equal to 10."""
    centers = df[df["position"] == "center"]
    viol = centers[(centers["age"] >= 30) & (centers["rebounds_per_game"] < 10)]
    truth = viol.empty
    if truth:
        expl = f"All centers aged >= 30 have rebounds per game >= 10."
    else:
        expl = f"{len(viol)} center(s) violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))}, rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one forward whose rebounds per game are greater than 6."""
    forwards = df[df["position"] == "forward"]
    exists = (forwards["rebounds_per_game"] > 6).any()
    if exists:
        count = forwards[forwards["rebounds_per_game"] > 6].shape[0]
        expl = f"Found {count} forward(s) with rebounds per game > 6."
    else:
        expl = "No forward with rebounds per game > 6 found."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. For all players with rebounds per game greater than 9, their position is guard."""
    condition = df[df["rebounds_per_game"] > 9]["position"] == "guard"
    truth = condition.all()
    if truth:
        expl = f"All players with rebounds per game > 9 are guards."
    else:
        viol = df[(df["rebounds_per_game"] > 9) & (df["position"]!= "guard")]
        expl = f"{len(viol)} player(s) violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))}, rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All players who are guards have a points per game greater than or equal to 20."""
    guards = df[df["position"] == "guard"]
    viol = guards[guards["points_per_game"] < 20]
    truth = viol.empty
    if truth:
        expl = f"All guards have points per game >= 20."
    else:
        expl = f"{len(viol)} guard(s) violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a player is a forward aged 25 or more, then their points per game are greater than or equal to 15."""
    forwards = df[df["position"] == "forward"]
    viol = forwards[(forwards["age"] >= 25) & (forwards["points_per_game"] < 15)]
    truth = viol.empty
    if truth:
        expl = f"All forwards aged >= 25 have points per game >= 15."
    else:
        expl = f"{len(viol)} forward(s) violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))}, points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_26.csv")
    # Convert numeric columns
    for col in df.columns:
        if col not in ["player_id", "position"]:
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
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()