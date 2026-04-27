import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are guards have an average of less than 6 assists per game."""
    guards = df[df["position"] == "guard"]
    condition = guards["assists_per_game"] < 6
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have assists < 6."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guard(s) violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a forward, then their average points per game is greater than 14."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["points_per_game"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have points > 14."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forward(s) violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All players who are centers have an average of more than 9 rebounds per game."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] > 9
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds > 9."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} center(s) violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one player who is a guard and has an average of more than 20 points per game."""
    guards = df[df["position"] == "guard"]
    exists = (guards["points_per_game"] > 20).any()
    if exists:
        viol = guards[guards["points_per_game"] > 20]
        expl = f"Found {len(viol)} guard(s) with points > 20 (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    else:
        expl = "No guard has points > 20."
    return exists, expl

def stmt_5(df: pd.DataFrame):
    """5. If a player is a forward aged 28 or older, then their average minutes per game is greater than 29."""
    forwards = df[(df["position"] == "forward") & (df["age"] >= 28)]
    condition = forwards["minutes_per_game"] > 29
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards aged ≥28 have minutes > 29."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forward(s) aged ≥28 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All players who have played more than 70 games have an average of more than 5 assists per game."""
    players = df[df["games_played"] > 70]
    condition = players["assists_per_game"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with >70 games have assists > 5."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} player(s) with >70 games violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most players have an average of more than 15 points per game."""
    condition = df["points_per_game"] > 15
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of players have points > 15."
    else:
        expl = f"Only {proportion*100:.1f}% of players have points > 15."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a player is a center aged 26 or older, then their average rebounds per game is greater than 9."""
    centers = df[(df["position"] == "center") & (df["age"] >= 26)]
    condition = centers["rebounds_per_game"] > 9
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers aged ≥26 have rebounds > 9."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} center(s) aged ≥26 violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one player who is a forward and has an average of more than 22 points per game."""
    forwards = df[df["position"] == "forward"]
    exists = (forwards["points_per_game"] > 22).any()
    if exists:
        viol = forwards[forwards["points_per_game"] > 22]
        expl = f"Found {len(viol)} forward(s) with points > 22 (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    else:
        expl = "No forward has points > 22."
    return exists, expl

def stmt_10(df: pd.DataFrame):
    """10. All players who have an average of more than 30 minutes per game have an average of more than 14 points per game."""
    players = df[df["minutes_per_game"] > 30]
    condition = players["points_per_game"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with >30 minutes have points > 14."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} player(s) with >30 minutes violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a player is a guard aged 24 or younger, then their average assists per game is less than 6."""
    guards = df[(df["position"] == "guard") & (df["age"] <= 24)]
    condition = guards["assists_per_game"] < 6
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards aged ≤24 have assists < 6."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guard(s) aged ≤24 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most players who are forwards have an average of more than 16 points per game."""
    forwards = df[df["position"] == "forward"]
    if len(forwards) == 0:
        return True, "No forwards in dataset; vacuously true."
    condition = forwards["points_per_game"] > 16
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of forwards have points > 16."
    else:
        expl = f"Only {proportion*100:.1f}% of forwards have points > 16."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All players who have an average of more than 9 rebounds per game have an average of more than 14 points per game."""
    players = df[df["rebounds_per_game"] > 9]
    condition = players["points_per_game"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with rebounds > 9 have points > 14."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} player(s) with rebounds > 9 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a player is a center aged 29 or older, then their average points per game is greater than 14."""
    centers = df[(df["position"] == "center") & (df["age"] >= 29)]
    condition = centers["points_per_game"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers aged ≥29 have points > 14."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} center(s) aged ≥29 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one player who is a guard and has an average of more than 9 rebounds per game."""
    guards = df[df["position"] == "guard"]
    exists = (guards["rebounds_per_game"] > 9).any()
    if exists:
        viol = guards[guards["rebounds_per_game"] > 9]
        expl = f"Found {len(viol)} guard(s) with rebounds > 9 (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    else:
        expl = "No guard has rebounds > 9."
    return exists, expl

def stmt_16(df: pd.DataFrame):
    """16. All players who have played more than 60 games have an average of more than 5 rebounds per game."""
    players = df[df["games_played"] > 60]
    condition = players["rebounds_per_game"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with >60 games have rebounds > 5."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} player(s) with >60 games violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a player is a forward aged 26 or older, then their average points per game is greater than 16."""
    forwards = df[(df["position"] == "forward") & (df["age"] >= 26)]
    condition = forwards["points_per_game"] > 16
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards aged ≥26 have points > 16."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forward(s) aged ≥26 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most players who are guards have an average of less than 7 assists per game."""
    guards = df[df["position"] == "guard"]
    if len(guards) == 0:
        return True, "No guards in dataset; vacuously true."
    condition = guards["assists_per_game"] < 7
    proportion = condition.mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of guards have assists < 7."
    else:
        expl = f"Only {proportion*100:.1f}% of guards have assists < 7."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All players who have an average of more than 25 minutes per game have an average of more than 13 points per game."""
    players = df[df["minutes_per_game"] > 25]
    condition = players["points_per_game"] > 13
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with >25 minutes have points > 13."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} player(s) with >25 minutes violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a player is a center aged 28 or older, then their average rebounds per game is greater than 10."""
    centers = df[(df["position"] == "center") & (df["age"] >= 28)]
    condition = centers["rebounds_per_game"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers aged ≥28 have rebounds > 10."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} center(s) aged ≥28 violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one player who is a forward and has an average of more than 10 rebounds per game."""
    forwards = df[df["position"] == "forward"]
    exists = (forwards["rebounds_per_game"] > 10).any()
    if exists:
        viol = forwards[forwards["rebounds_per_game"] > 10]
        expl = f"Found {len(viol)} forward(s) with rebounds > 10 (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    else:
        expl = "No forward has rebounds > 10."
    return exists, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_46.csv")

    # Convert numeric columns safely
    numeric_cols = ["age", "games_played", "minutes_per_game", "points_per_game", "assists_per_game", "rebounds_per_game"]
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()