import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are centers have an age between 20 and 33 years."""
    centers = df[df["position"] == "center"]
    condition = centers["age"].between(20, 33, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers are aged 20-33."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a forward, then their age is between 20 and 33 years."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["age"].between(20, 33, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards are aged 20-33."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All players who are guards have an age between 24 and 29 years."""
    guards = df[df["position"] == "guard"]
    condition = guards["age"].between(24, 29, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards are aged 24-29."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all players with minutes per game greater than 30, their points per game is greater than 13."""
    subset = df[df["minutes_per_game"] > 30]
    condition = subset["points_per_game"] > 13
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with >30 MPG have >13 PPG."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} players violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a player has games played greater than 70, then their assists per game is greater than 4."""
    subset = df[df["games_played"] > 70]
    condition = subset["assists_per_game"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with >70 GP have >4 APG."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} players violate the rule (APG: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All players who have rebounds per game greater than 10 are forwards."""
    subset = df[df["rebounds_per_game"] > 10]
    condition = subset["position"] == "forward"
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with >10 RPG are forwards."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} players violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all players with age greater than 25, their points per game is greater than 17."""
    subset = df[df["age"] > 25]
    condition = subset["points_per_game"] > 17
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with >25 age have >17 PPG."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} players violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a player is a center, then their rebounds per game is greater than 3."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have >3 RPG."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (RPG: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All players who have assists per game greater than 5 are guards or forwards."""
    subset = df[df["assists_per_game"] > 5]
    condition = subset["position"].isin(["guard", "forward"])
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with >5 APG are guards or forwards."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} players violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. For all players with minutes per game greater than 35, their rebounds per game is greater than 4."""
    subset = df[df["minutes_per_game"] > 35]
    condition = subset["rebounds_per_game"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with >35 MPG have >4 RPG."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} players violate the rule (RPG: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Most players in the table have a points per game greater than 15."""
    condition = df["points_per_game"] > 15
    truth = condition.mean() > 0.5
    if truth:
        expl = f"{condition.sum()} out of {len(df)} players have >15 PPG."
    else:
        expl = f"{condition.sum()} out of {len(df)} players have >15 PPG."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a player has age less than 25, then their rebounds per game is less than 8."""
    subset = df[df["age"] < 25]
    condition = subset["rebounds_per_game"] < 8
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with <25 age have <8 RPG."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} players violate the rule (RPG: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All players who have games played greater than 60 have a minutes per game greater than 24."""
    subset = df[df["games_played"] > 60]
    condition = subset["minutes_per_game"] > 24
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with >60 GP have >24 MPG."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} players violate the rule (MPG: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. For all players with points per game greater than 20, their age is greater than 20."""
    subset = df[df["points_per_game"] > 20]
    condition = subset["age"] > 20
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with >20 PPG have >20 age."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} players violate the rule (age: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a player is a forward, then their points per game is greater than 14."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["points_per_game"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have >14 PPG."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All players who have rebounds per game greater than 6 are forwards or centers."""
    subset = df[df["rebounds_per_game"] > 6]
    condition = subset["position"].isin(["forward", "center"])
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with >6 RPG are forwards or centers."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} players violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. For all players with assists per game greater than 4, their minutes per game is greater than 25."""
    subset = df[df["assists_per_game"] > 4]
    condition = subset["minutes_per_game"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with >4 APG have >25 MPG."
    else:
        viol = subset[~condition]
        expl = f"{len(viol)} players violate the rule (MPG: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_6.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()