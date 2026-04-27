import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are guards have an average of more than 5 assists per game."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = True
        expl = "No guards in dataset."
    else:
        condition = guards["assists_per_game"] > 5
        truth = condition.all()
        if truth:
            expl = f"All {len(guards)} guards have more than 5 assists per game."
        else:
            viol = guards[~condition]
            expl = f"{len(viol)} guards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a center, then their average points per game is less than 23."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = True
        expl = "No centers in dataset."
    else:
        condition = centers["points_per_game"] < 23
        truth = condition.all()
        if truth:
            expl = f"All {len(centers)} centers have less than 23 points per game."
        else:
            viol = centers[~condition]
            expl = f"{len(viol)} centers violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one player who is a forward and has an average of more than 20 points per game."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = False
        expl = "No forwards in dataset."
    else:
        condition = forwards["points_per_game"] > 20
        truth = condition.any()
        if truth:
            expl = f"At least one forward ({len(forwards[condition])}) has more than 20 points per game."
        else:
            expl = f"No forwards have more than 20 points per game."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players who are 30 years old or younger have an average of more than 4 rebounds per game."""
    young_players = df[df["age"] <= 30]
    if young_players.empty:
        truth = True
        expl = "No players 30 or younger in dataset."
    else:
        condition = young_players["rebounds_per_game"] > 4
        truth = condition.all()
        if truth:
            expl = f"All {len(young_players)} players 30 or younger have more than 4 rebounds per game."
        else:
            viol = young_players[~condition]
            expl = f"{len(viol)} players 30 or younger violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a player is a center and is 25 years old or younger, then their average minutes per game is more than 30."""
    centers_young = df[(df["position"] == "center") & (df["age"] <= 25)]
    if centers_young.empty:
        truth = True
        expl = "No young centers in dataset."
    else:
        condition = centers_young["minutes_per_game"] > 30
        truth = condition.all()
        if truth:
            expl = f"All {len(centers_young)} young centers have more than 30 minutes per game."
        else:
            viol = centers_young[~condition]
            expl = f"{len(viol)} young centers violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most players have an average of more than 5 rebounds per game."""
    condition = df["rebounds_per_game"] > 5
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} players have more than 5 rebounds per game. {'Most' if truth else 'Not most'} have more than 5 rebounds."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All players who have an average of more than 30 minutes per game have an average of more than 15 points per game."""
    high_minutes = df[df["minutes_per_game"] > 30]
    if high_minutes.empty:
        truth = True
        expl = "No players with more than 30 minutes per game."
    else:
        condition = high_minutes["points_per_game"] > 15
        truth = condition.all()
        if truth:
            expl = f"All {len(high_minutes)} players with more than 30 minutes per game have more than 15 points per game."
        else:
            viol = high_minutes[~condition]
            expl = f"{len(viol)} players with more than 30 minutes per game violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a player is a guard and is 30 years old or younger, then their average assists per game is more than 5."""
    guards_young = df[(df["position"] == "guard") & (df["age"] <= 30)]
    if guards_young.empty:
        truth = True
        expl = "No young guards in dataset."
    else:
        condition = guards_young["assists_per_game"] > 5
        truth = condition.all()
        if truth:
            expl = f"All {len(guards_young)} young guards have more than 5 assists per game."
        else:
            viol = guards_young[~condition]
            expl = f"{len(viol)} young guards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one player who is a center and has an average of more than 10 rebounds per game."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = False
        expl = "No centers in dataset."
    else:
        condition = centers["rebounds_per_game"] > 10
        truth = condition.any()
        if truth:
            expl = f"At least one center ({len(centers[condition])}) has more than 10 rebounds per game."
        else:
            expl = f"No centers have more than 10 rebounds per game."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All players who are 25 years old or younger have an average of more than 20 points per game."""
    young_players = df[df["age"] <= 25]
    if young_players.empty:
        truth = True
        expl = "No players 25 or younger in dataset."
    else:
        condition = young_players["points_per_game"] > 20
        truth = condition.all()
        if truth:
            expl = f"All {len(young_players)} players 25 or younger have more than 20 points per game."
        else:
            viol = young_players[~condition]
            expl = f"{len(viol)} players 25 or younger violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a player is a forward and has an average of more than 30 minutes per game, then their average points per game is more than 15."""
    forwards_high_minutes = df[(df["position"] == "forward") & (df["minutes_per_game"] > 30)]
    if forwards_high_minutes.empty:
        truth = True
        expl = "No forwards with more than 30 minutes per game."
    else:
        condition = forwards_high_minutes["points_per_game"] > 15
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards_high_minutes)} forwards with more than 30 minutes per game have more than 15 points per game."
        else:
            viol = forwards_high_minutes[~condition]
            expl = f"{len(viol)} forwards with more than 30 minutes per game violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most players who are guards have an average of more than 20 points per game."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["points_per_game"] > 20
        count = condition.sum()
        total = len(guards)
        truth = count > total / 2
        expl = f"{count} out of {total} guards have more than 20 points per game. {'Most' if truth else 'Not most'} guards have more than 20 points."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All players who have an average of more than 5 assists per game have an average of more than 10 points per game."""
    high_assists = df[df["assists_per_game"] > 5]
    if high_assists.empty:
        truth = True
        expl = "No players with more than 5 assists per game."
    else:
        condition = high_assists["points_per_game"] > 10
        truth = condition.all()
        if truth:
            expl = f"All {len(high_assists)} players with more than 5 assists per game have more than 10 points per game."
        else:
            viol = high_assists[~condition]
            expl = f"{len(viol)} players with more than 5 assists per game violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a player is a center and has an average of more than 25 minutes per game, then their average rebounds per game is more than 5."""
    centers_high_minutes = df[(df["position"] == "center") & (df["minutes_per_game"] > 25)]
    if centers_high_minutes.empty:
        truth = True
        expl = "No centers with more than 25 minutes per game."
    else:
        condition = centers_high_minutes["rebounds_per_game"] > 5
        truth = condition.all()
        if truth:
            expl = f"All {len(centers_high_minutes)} centers with more than 25 minutes per game have more than 5 rebounds per game."
        else:
            viol = centers_high_minutes[~condition]
            expl = f"{len(viol)} centers with more than 25 minutes per game violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one player who is a guard and has an average of more than 35 minutes per game."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["minutes_per_game"] > 35
        truth = condition.any()
        if truth:
            expl = f"At least one guard ({len(guards[condition])}) has more than 35 minutes per game."
        else:
            expl = f"No guards have more than 35 minutes per game."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All players who are 30 years old or younger have an average of more than 10 points per game."""
    young_players = df[df["age"] <= 30]
    if young_players.empty:
        truth = True
        expl = "No players 30 or younger in dataset."
    else:
        condition = young_players["points_per_game"] > 10
        truth = condition.all()
        if truth:
            expl = f"All {len(young_players)} players 30 or younger have more than 10 points per game."
        else:
            viol = young_players[~condition]
            expl = f"{len(viol)} players 30 or younger violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a player is a forward and is 25 years old or younger, then their average assists per game is more than 3."""
    forwards_young = df[(df["position"] == "forward") & (df["age"] <= 25)]
    if forwards_young.empty:
        truth = True
        expl = "No young forwards in dataset."
    else:
        condition = forwards_young["assists_per_game"] > 3
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards_young)} young forwards have more than 3 assists per game."
        else:
            viol = forwards_young[~condition]
            expl = f"{len(viol)} young forwards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most players who are centers have an average of more than 5 rebounds per game."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = False
        expl = "No centers in dataset."
    else:
        condition = centers["rebounds_per_game"] > 5
        count = condition.sum()
        total = len(centers)
        truth = count > total / 2
        expl = f"{count} out of {total} centers have more than 5 rebounds per game. {'Most' if truth else 'Not most'} centers have more than 5 rebounds."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All players who have an average of more than 20 points per game have an average of more than 5 rebounds per game."""
    high_points = df[df["points_per_game"] > 20]
    if high_points.empty:
        truth = True
        expl = "No players with more than 20 points per game."
    else:
        condition = high_points["rebounds_per_game"] > 5
        truth = condition.all()
        if truth:
            expl = f"All {len(high_points)} players with more than 20 points per game have more than 5 rebounds per game."
        else:
            viol = high_points[~condition]
            expl = f"{len(viol)} players with more than 20 points per game violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a player is a guard and has an average of more than 20 points per game, then their average assists per game is more than 4."""
    guards_high_points = df[(df["position"] == "guard") & (df["points_per_game"] > 20)]
    if guards_high_points.empty:
        truth = True
        expl = "No guards with more than 20 points per game."
    else:
        condition = guards_high_points["assists_per_game"] > 4
        truth = condition.all()
        if truth:
            expl = f"All {len(guards_high_points)} guards with more than 20 points per game have more than 4 assists per game."
        else:
            viol = guards_high_points[~condition]
            expl = f"{len(viol)} guards with more than 20 points per game violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one player who is a center and has an average of more than 20 points per game."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = False
        expl = "No centers in dataset."
    else:
        condition = centers["points_per_game"] > 20
        truth = condition.any()
        if truth:
            expl = f"At least one center ({len(centers[condition])}) has more than 20 points per game."
        else:
            expl = f"No centers have more than 20 points per game."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. All players who are 25 years old or younger have an average of more than 5 assists per game."""
    young_players = df[df["age"] <= 25]
    if young_players.empty:
        truth = True
        expl = "No players 25 or younger in dataset."
    else:
        condition = young_players["assists_per_game"] > 5
        truth = condition.all()
        if truth:
            expl = f"All {len(young_players)} players 25 or younger have more than 5 assists per game."
        else:
            viol = young_players[~condition]
            expl = f"{len(viol)} players 25 or younger violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_23(df: pd.DataFrame):
    """23. If a player is a forward and has an average of more than 25 minutes per game, then their average points per game is more than 12."""
    forwards_high_minutes = df[(df["position"] == "forward") & (df["minutes_per_game"] > 25)]
    if forwards_high_minutes.empty:
        truth = True
        expl = "No forwards with more than 25 minutes per game."
    else:
        condition = forwards_high_minutes["points_per_game"] > 12
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards_high_minutes)} forwards with more than 25 minutes per game have more than 12 points per game."
        else:
            viol = forwards_high_minutes[~condition]
            expl = f"{len(viol)} forwards with more than 25 minutes per game violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_24(df: pd.DataFrame):
    """24. Most players who are guards have an average of more than 25 minutes per game."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["minutes_per_game"] > 25
        count = condition.sum()
        total = len(guards)
        truth = count > total / 2
        expl = f"{count} out of {total} guards have more than 25 minutes per game. {'Most' if truth else 'Not most'} guards have more than 25 minutes."
    return truth, expl

def stmt_25(df: pd.DataFrame):
    """25. All players who have an average of more than 15 points per game have an average of more than 4 rebounds per game."""
    high_points = df[df["points_per_game"] > 15]
    if high_points.empty:
        truth = True
        expl = "No players with more than 15 points per game."
    else:
        condition = high_points["rebounds_per_game"] > 4
        truth = condition.all()
        if truth:
            expl = f"All {len(high_points)} players with more than 15 points per game have more than 4 rebounds per game."
        else:
            viol = high_points[~condition]
            expl = f"{len(viol)} players with more than 15 points per game violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_26(df: pd.DataFrame):
    """26. If a player is a center and has an average of more than 30 minutes per game, then their average rebounds per game is more than 6."""
    centers_high_minutes = df[(df["position"] == "center") & (df["minutes_per_game"] > 30)]
    if centers_high_minutes.empty:
        truth = True
        expl = "No centers with more than 30 minutes per game."
    else:
        condition = centers_high_minutes["rebounds_per_game"] > 6
        truth = condition.all()
        if truth:
            expl = f"All {len(centers_high_minutes)} centers with more than 30 minutes per game have more than 6 rebounds per game."
        else:
            viol = centers_high_minutes[~condition]
            expl = f"{len(viol)} centers with more than 30 minutes per game violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_27(df: pd.DataFrame):
    """27. There exists at least one player who is a forward and has an average of more than 30 rebounds per game."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = False
        expl = "No forwards in dataset."
    else:
        condition = forwards["rebounds_per_game"] > 30
        truth = condition.any()
        if truth:
            expl = f"At least one forward ({len(forwards[condition])}) has more than 30 rebounds per game."
        else:
            expl = f"No forwards have more than 30 rebounds per game."
    return truth, expl

def stmt_28(df: pd.DataFrame):
    """28. All players who are 30 years old or younger have an average of more than 15 points per game."""
    young_players = df[df["age"] <= 30]
    if young_players.empty:
        truth = True
        expl = "No players 30 or younger in dataset."
    else:
        condition = young_players["points_per_game"] > 15
        truth = condition.all()
        if truth:
            expl = f"All {len(young_players)} players 30 or younger have more than 15 points per game."
        else:
            viol = young_players[~condition]
            expl = f"{len(viol)} players 30 or younger violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_29(df: pd.DataFrame):
    """29. If a player is a guard and is 25 years old or younger, then their average assists per game is more than 5."""
    guards_young = df[(df["position"] == "guard") & (df["age"] <= 25)]
    if guards_young.empty:
        truth = True
        expl = "No young guards in dataset."
    else:
        condition = guards_young["assists_per_game"] > 5
        truth = condition.all()
        if truth:
            expl = f"All {len(guards_young)} young guards have more than 5 assists per game."
        else:
            viol = guards_young[~condition]
            expl = f"{len(viol)} young guards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_30(df: pd.DataFrame):
    """30. Most players who are centers have an average of more than 20 minutes per game."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = False
        expl = "No centers in dataset."
    else:
        condition = centers["minutes_per_game"] > 20
        count = condition.sum()
        total = len(centers)
        truth = count > total / 2
        expl = f"{count} out of {total} centers have more than 20 minutes per game. {'Most' if truth else 'Not most'} centers have more than 20 minutes."
    return truth, expl

def stmt_31(df: pd.DataFrame):
    """31. All players who have an average of more than 10 rebounds per game have an average of more than 10 points per game."""
    high_rebounds = df[df["rebounds_per_game"] > 10]
    if high_rebounds.empty:
        truth = True
        expl = "No players with more than 10 rebounds per game."
    else:
        condition = high_rebounds["points_per_game"] > 10
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rebounds)} players with more than 10 rebounds per game have more than 10 points per game."
        else:
            viol = high_rebounds[~condition]
            expl = f"{len(viol)} players with more than 10 rebounds per game violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_32(df: pd.DataFrame):
    """32. If a player is a forward and has an average of more than 20 points per game, then their average assists per game is more than 3."""
    forwards_high_points = df[(df["position"] == "forward") & (df["points_per_game"] > 20)]
    if forwards_high_points.empty:
        truth = True
        expl = "No forwards with more than 20 points per game."
    else:
        condition = forwards_high_points["assists_per_game"] > 3
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards_high_points)} forwards with more than 20 points per game have more than 3 assists per game."
        else:
            viol = forwards_high_points[~condition]
            expl = f"{len(viol)} forwards with more than 20 points per game violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_33(df: pd.DataFrame):
    """33. There exists at least one player who is a guard and has an average of more than 25 rebounds per game."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["rebounds_per_game"] > 25
        truth = condition.any()
        if truth:
            expl = f"At least one guard ({len(guards[condition])}) has more than 25 rebounds per game."
        else:
            expl = f"No guards have more than 25 rebounds per game."
    return truth, expl

def stmt_34(df: pd.DataFrame):
    """34. All players who are 25 years old or younger have an average of more than 20 minutes per game."""
    young_players = df[df["age"] <= 25]
    if young_players.empty:
        truth = True
        expl = "No players 25 or younger in dataset."
    else:
        condition = young_players["minutes_per_game"] > 20
        truth = condition.all()
        if truth:
            expl = f"All {len(young_players)} players 25 or younger have more than 20 minutes per game."
        else:
            viol = young_players[~condition]
            expl = f"{len(viol)} players 25 or younger violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_35(df: pd.DataFrame):
    """35. If a player is a center and has an average of more than 25 points per game, then their average rebounds per game is more than 7."""
    centers_high_points = df[(df["position"] == "center") & (df["points_per_game"] > 25)]
    if centers_high_points.empty:
        truth = True
        expl = "No centers with more than 25 points per game."
    else:
        condition = centers_high_points["rebounds_per_game"] > 7
        truth = condition.all()
        if truth:
            expl = f"All {len(centers_high_points)} centers with more than 25 points per game have more than 7 rebounds per game."
        else:
            viol = centers_high_points[~condition]
            expl = f"{len(viol)} centers with more than 25 points per game violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_36(df: pd.DataFrame):
    """36. Most players who are guards have an average of more than 20 rebounds per game."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["rebounds_per_game"] > 20
        count = condition.sum()
        total = len(guards)
        truth = count > total / 2
        expl = f"{count} out of {total} guards have more than 20 rebounds per game. {'Most' if truth else 'Not most'} guards have more than 20 rebounds."
    return truth, expl

def stmt_37(df: pd.DataFrame):
    """37. All players who have an average of more than 15 rebounds per game have an average of more than 15 points per game."""
    high_rebounds = df[df["rebounds_per_game"] > 15]
    if high_rebounds.empty:
        truth = True
        expl = "No players with more than 15 rebounds per game."
    else:
        condition = high_rebounds["points_per_game"] > 15
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rebounds)} players with more than 15 rebounds per game have more than 15 points per game."
        else:
            viol = high_rebounds[~condition]
            expl = f"{len(viol)} players with more than 15 rebounds per game violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_38(df: pd.DataFrame):
    """38. If a player is a forward and has an average of more than 30 points per game, then their average assists per game is more than 4."""
    forwards_high_points = df[(df["position"] == "forward") & (df["points_per_game"] > 30)]
    if forwards_high_points.empty:
        truth = True
        expl = "No forwards with more than 30 points per game."
    else:
        condition = forwards_high_points["assists_per_game"] > 4
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards_high_points)} forwards with more than 30 points per game have more than 4 assists per game."
        else:
            viol = forwards_high_points[~condition]
            expl = f"{len(viol)} forwards with more than 30 points per game violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_39(df: pd.DataFrame):
    """39. There exists at least one player who is a center and has an average of more than 35 minutes per game."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = False
        expl = "No centers in dataset."
    else:
        condition = centers["minutes_per_game"] > 35
        truth = condition.any()
        if truth:
            expl = f"At least one center ({len(centers[condition])}) has more than 35 minutes per game."
        else:
            expl = f"No centers have more than 35 minutes per game."
    return truth, expl

def stmt_40(df: pd.DataFrame):
    """40. All players who are 30 years old or younger have an average of more than 25 points per game."""
    young_players = df[df["age"] <= 30]
    if young_players.empty:
        truth = True
        expl = "No players 30 or younger in dataset."
    else:
        condition = young_players["points_per_game"] > 25
        truth = condition.all()
        if truth:
            expl = f"All {len(young_players)} players 30 or younger have more than 25 points per game."
        else:
            viol = young_players[~condition]
            expl = f"{len(viol)} players 30 or younger violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_41(df: pd.DataFrame):
    """41. If a player is a guard and is 25 years old or younger, then their average points per game is more than 20."""
    guards_young = df[(df["position"] == "guard") & (df["age"] <= 25)]
    if guards_young.empty:
        truth = True
        expl = "No young guards in dataset."
    else:
        condition = guards_young["points_per_game"] > 20
        truth = condition.all()
        if truth:
            expl = f"All {len(guards_young)} young guards have more than 20 points per game."
        else:
            viol = guards_young[~condition]
            expl = f"{len(viol)} young guards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_42(df: pd.DataFrame):
    """42. Most players who are centers have an average of more than 25 minutes per game."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = False
        expl = "No centers in dataset."
    else:
        condition = centers["minutes_per_game"] > 25
        count = condition.sum()
        total = len(centers)
        truth = count > total / 2
        expl = f"{count} out of {total} centers have more than 25 minutes per game. {'Most' if truth else 'Not most'} centers have more than 25 minutes."
    return truth, expl

def stmt_43(df: pd.DataFrame):
    """43. All players who have an average of more than 20 rebounds per game have an average of more than 20 points per game."""
    high_rebounds = df[df["rebounds_per_game"] > 20]
    if high_rebounds.empty:
        truth = True
        expl = "No players with more than 20 rebounds per game."
    else:
        condition = high_rebounds["points_per_game"] > 20
        truth = condition.all()
        if truth:
            expl = f"All {len(high_rebounds)} players with more than 20 rebounds per game have more than 20 points per game."
        else:
            viol = high_rebounds[~condition]
            expl = f"{len(viol)} players with more than 20 rebounds per game violate the rule (points: {', '.join(map(str, viol['points