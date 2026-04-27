import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are guards have an average of less than 6 assists per game."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = True
        expl = "No guards in dataset."
    else:
        condition = guards["assists_per_game"] < 6
        truth = condition.all()
        if truth:
            expl = f"All {len(guards)} guards have less than 6 assists per game."
        else:
            viol = guards[~condition]
            expl = f"{len(viol)} guards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a forward, then their average points per game is greater than 14."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = True
        expl = "No forwards in dataset."
    else:
        condition = forwards["points_per_game"] > 14
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards)} forwards have more than 14 points per game."
        else:
            viol = forwards[~condition]
            expl = f"{len(viol)} forwards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All players who are centers have an average of more than 9 rebounds per game."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = True
        expl = "No centers in dataset."
    else:
        condition = centers["rebounds_per_game"] > 9
        truth = condition.all()
        if truth:
            expl = f"All {len(centers)} centers have more than 9 rebounds per game."
        else:
            viol = centers[~condition]
            expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one player who is a guard and has an average of more than 20 points per game."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["points_per_game"] > 20
        truth = condition.any()
        if truth:
            found = guards[condition]
            expl = f"Found {len(found)} guard(s) with more than 20 points per game (points: {', '.join(map(str, found['points_per_game'].tolist()))})."
        else:
            expl = "No guards have more than 20 points per game."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a player is a forward aged 28 or older, then their average minutes per game is greater than 29."""
    forwards_old = df[(df["position"] == "forward") & (df["age"] >= 28)]
    if forwards_old.empty:
        truth = True
        expl = "No forwards aged 28 or older in dataset."
    else:
        condition = forwards_old["minutes_per_game"] > 29
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards_old)} forwards aged 28+ have more than 29 minutes per game."
        else:
            viol = forwards_old[~condition]
            expl = f"{len(viol)} forwards aged 28+ violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All players who have played more than 70 games have an average of more than 5 assists per game."""
    players_many_games = df[df["games_played"] > 70]
    if players_many_games.empty:
        truth = True
        expl = "No players with more than 70 games."
    else:
        condition = players_many_games["assists_per_game"] > 5
        truth = condition.all()
        if truth:
            expl = f"All {len(players_many_games)} players with more than 70 games have more than 5 assists per game."
        else:
            viol = players_many_games[~condition]
            expl = f"{len(viol)} players with more than 70 games violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most players have an average of more than 15 points per game."""
    condition = df["points_per_game"] > 15
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have more than 15 points per game."
    else:
        expl = f"{count} out of {total} players have more than 15 points per game (less than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a player is a center aged 26 or older, then their average rebounds per game is greater than 9."""
    centers_old = df[(df["position"] == "center") & (df["age"] >= 26)]
    if centers_old.empty:
        truth = True
        expl = "No centers aged 26 or older in dataset."
    else:
        condition = centers_old["rebounds_per_game"] > 9
        truth = condition.all()
        if truth:
            expl = f"All {len(centers_old)} centers aged 26+ have more than 9 rebounds per game."
        else:
            viol = centers_old[~condition]
            expl = f"{len(viol)} centers aged 26+ violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one player who is a forward and has an average of more than 22 points per game."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = False
        expl = "No forwards in dataset."
    else:
        condition = forwards["points_per_game"] > 22
        truth = condition.any()
        if truth:
            found = forwards[condition]
            expl = f"Found {len(found)} forward(s) with more than 22 points per game (points: {', '.join(map(str, found['points_per_game'].tolist()))})."
        else:
            expl = "No forwards have more than 22 points per game."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All players who have an average of more than 30 minutes per game have an average of more than 14 points per game."""
    players_high_minutes = df[df["minutes_per_game"] > 30]
    if players_high_minutes.empty:
        truth = True
        expl = "No players with more than 30 minutes per game."
    else:
        condition = players_high_minutes["points_per_game"] > 14
        truth = condition.all()
        if truth:
            expl = f"All {len(players_high_minutes)} players with more than 30 minutes per game have more than 14 points per game."
        else:
            viol = players_high_minutes[~condition]
            expl = f"{len(viol)} players with more than 30 minutes per game violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a player is a guard aged 24 or younger, then their average assists per game is less than 6."""
    guards_young = df[(df["position"] == "guard") & (df["age"] <= 24)]
    if guards_young.empty:
        truth = True
        expl = "No guards aged 24 or younger in dataset."
    else:
        condition = guards_young["assists_per_game"] < 6
        truth = condition.all()
        if truth:
            expl = f"All {len(guards_young)} guards aged 24- have less than 6 assists per game."
        else:
            viol = guards_young[~condition]
            expl = f"{len(viol)} guards aged 24- violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most players who are forwards have an average of more than 16 points per game."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = False
        expl = "No forwards in dataset."
    else:
        condition = forwards["points_per_game"] > 16
        count = condition.sum()
        total = len(forwards)
        truth = count > total / 2
        if truth:
            expl = f"{count} out of {total} forwards have more than 16 points per game."
        else:
            expl = f"{count} out of {total} forwards have more than 16 points per game (less than half)."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All players who have an average of more than 9 rebounds per game have an average of more than 14 points per game."""
    players_high_rebounds = df[df["rebounds_per_game"] > 9]
    if players_high_rebounds.empty:
        truth = True
        expl = "No players with more than 9 rebounds per game."
    else:
        condition = players_high_rebounds["points_per_game"] > 14
        truth = condition.all()
        if truth:
            expl = f"All {len(players_high_rebounds)} players with more than 9 rebounds per game have more than 14 points per game."
        else:
            viol = players_high_rebounds[~condition]
            expl = f"{len(viol)} players with more than 9 rebounds per game violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a player is a center aged 29 or older, then their average points per game is greater than 14."""
    centers_old = df[(df["position"] == "center") & (df["age"] >= 29)]
    if centers_old.empty:
        truth = True
        expl = "No centers aged 29 or older in dataset."
    else:
        condition = centers_old["points_per_game"] > 14
        truth = condition.all()
        if truth:
            expl = f"All {len(centers_old)} centers aged 29+ have more than 14 points per game."
        else:
            viol = centers_old[~condition]
            expl = f"{len(viol)} centers aged 29+ violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one player who is a guard and has an average of more than 9 rebounds per game."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["rebounds_per_game"] > 9
        truth = condition.any()
        if truth:
            found = guards[condition]
            expl = f"Found {len(found)} guard(s) with more than 9 rebounds per game (rebounds: {', '.join(map(str, found['rebounds_per_game'].tolist()))})."
        else:
            expl = "No guards have more than 9 rebounds per game."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All players who have played more than 60 games have an average of more than 5 rebounds per game."""
    players_many_games = df[df["games_played"] > 60]
    if players_many_games.empty:
        truth = True
        expl = "No players with more than 60 games."
    else:
        condition = players_many_games["rebounds_per_game"] > 5
        truth = condition.all()
        if truth:
            expl = f"All {len(players_many_games)} players with more than 60 games have more than 5 rebounds per game."
        else:
            viol = players_many_games[~condition]
            expl = f"{len(viol)} players with more than 60 games violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a player is a forward aged 26 or older, then their average points per game is greater than 16."""
    forwards_old = df[(df["position"] == "forward") & (df["age"] >= 26)]
    if forwards_old.empty:
        truth = True
        expl = "No forwards aged 26 or older in dataset."
    else:
        condition = forwards_old["points_per_game"] > 16
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards_old)} forwards aged 26+ have more than 16 points per game."
        else:
            viol = forwards_old[~condition]
            expl = f"{len(viol)} forwards aged 26+ violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most players who are guards have an average of less than 7 assists per game."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["assists_per_game"] < 7
        count = condition.sum()
        total = len(guards)
        truth = count > total / 2
        if truth:
            expl = f"{count} out of {total} guards have less than 7 assists per game."
        else:
            expl = f"{count} out of {total} guards have less than 7 assists per game (less than half)."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All players who have an average of more than 25 minutes per game have an average of more than 13 points per game."""
    players_high_minutes = df[df["minutes_per_game"] > 25]
    if players_high_minutes.empty:
        truth = True
        expl = "No players with more than 25 minutes per game."
    else:
        condition = players_high_minutes["points_per_game"] > 13
        truth = condition.all()
        if truth:
            expl = f"All {len(players_high_minutes)} players with more than 25 minutes per game have more than 13 points per game."
        else:
            viol = players_high_minutes[~condition]
            expl = f"{len(viol)} players with more than 25 minutes per game violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a player is a center aged 28 or older, then their average rebounds per game is greater than 10."""
    centers_old = df[(df["position"] == "center") & (df["age"] >= 28)]
    if centers_old.empty:
        truth = True
        expl = "No centers aged 28 or older in dataset."
    else:
        condition = centers_old["rebounds_per_game"] > 10
        truth = condition.all()
        if truth:
            expl = f"All {len(centers_old)} centers aged 28+ have more than 10 rebounds per game."
        else:
            viol = centers_old[~condition]
            expl = f"{len(viol)} centers aged 28+ violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one player who is a forward and has an average of more than 10 rebounds per game."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = False
        expl = "No forwards in dataset."
    else:
        condition = forwards["rebounds_per_game"] > 10
        truth = condition.any()
        if truth:
            found = forwards[condition]
            expl = f"Found {len(found)} forward(s) with more than 10 rebounds per game (rebounds: {', '.join(map(str, found['rebounds_per_game'].tolist()))})."
        else:
            expl = "No forwards have more than 10 rebounds per game."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_46.csv")

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
        (21, stmt_21)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()