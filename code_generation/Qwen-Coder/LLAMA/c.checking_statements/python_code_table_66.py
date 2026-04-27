import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are centers have an age between 20 and 32 years."""
    centers = df[df["position"] == "center"]
    condition = centers["age"].between(20, 32, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers are aged 20-32."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a forward, then their age is between 23 and 32 years."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["age"].between(23, 32, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards are aged 23-32."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one guard who is 30 years old."""
    guards_30 = df[(df["position"] == "guard") & (df["age"] == 30)]
    truth = len(guards_30) > 0
    if truth:
        expl = f"There is at least one guard aged 30 ({len(guards_30)} such players)."
    else:
        expl = "No guard is 30 years old."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players who are 25 years old or younger have a position that is either center or guard."""
    young_players = df[df["age"] <= 25]
    valid_positions = young_players["position"].isin(["center", "guard"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(young_players)} players aged 25 or younger are centers or guards."
    else:
        viol = young_players[~valid_positions]
        expl = f"{len(viol)} players aged 25 or younger have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a player is a center, then their points per game is less than 25."""
    centers = df[df["position"] == "center"]
    condition = centers["points_per_game"] < 25
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers score less than 25 points per game."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers score 25 or more points per game ({', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All players who have played more than 70 games have an average of more than 25 minutes per game."""
    high_games = df[df["games_played"] > 70]
    condition = high_games["minutes_per_game"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(high_games)} players with >70 games average >25 minutes per game."
    else:
        viol = high_games[~condition]
        expl = f"{len(viol)} players with >70 games average <=25 minutes per game ({', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. There exists at least one forward who has played more than 75 games."""
    forwards_high_games = df[(df["position"] == "forward") & (df["games_played"] > 75)]
    truth = len(forwards_high_games) > 0
    if truth:
        expl = f"There is at least one forward with >75 games ({len(forwards_high_games)} such players)."
    else:
        expl = "No forward has played more than 75 games."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a player is a guard, then their rebounds per game is less than 8."""
    guards = df[df["position"] == "guard"]
    condition = guards["rebounds_per_game"] < 8
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have <8 rebounds per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards have >=8 rebounds per game ({', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All players who have an average of more than 7 assists per game have a position that is either forward or guard."""
    high_assists = df[df["assists_per_game"] > 7]
    valid_positions = high_assists["position"].isin(["forward", "guard"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_assists)} players with >7 assists are forwards or guards."
    else:
        viol = high_assists[~valid_positions]
        expl = f"{len(viol)} players with >7 assists have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Most players have an average of more than 15 points per game."""
    total_players = len(df)
    high_points = df[df["points_per_game"] > 15]
    truth = len(high_points) > total_players / 2
    if truth:
        expl = f"More than half ({len(high_points)}/{total_players}) of players score >15 points per game."
    else:
        expl = f"Less than half ({len(high_points)}/{total_players}) of players score >15 points per game."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a player is a center, then their age is less than 33 years."""
    centers = df[df["position"] == "center"]
    condition = centers["age"] < 33
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers are under 33 years old."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers are 33 or older ({', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All players who are 28 years old or older have a position that is either center or forward."""
    older_players = df[df["age"] >= 28]
    valid_positions = older_players["position"].isin(["center", "forward"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(older_players)} players aged 28+ are centers or forwards."
    else:
        viol = older_players[~valid_positions]
        expl = f"{len(viol)} players aged 28+ have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. There exists at least one player who is 32 years old and has played more than 60 games."""
    specific_player = df[(df["age"] == 32) & (df["games_played"] > 60)]
    truth = len(specific_player) > 0
    if truth:
        expl = f"There is at least one player aged 32 with >60 games ({len(specific_player)} such players)."
    else:
        expl = "No player is 32 years old and has played more than 60 games."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a player has an average of more than 18 points per game, then their position is either forward or guard."""
    high_points = df[df["points_per_game"] > 18]
    valid_positions = high_points["position"].isin(["forward", "guard"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_points)} players with >18 points are forwards or guards."
    else:
        viol = high_points[~valid_positions]
        expl = f"{len(viol)} players with >18 points have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All players who have an average of more than 6 rebounds per game have a position that is either center or forward."""
    high_rebounds = df[df["rebounds_per_game"] > 6]
    valid_positions = high_rebounds["position"].isin(["center", "forward"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >6 rebounds are centers or forwards."
    else:
        viol = high_rebounds[~valid_positions]
        expl = f"{len(viol)} players with >6 rebounds have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one player who is 25 years old or younger and has an average of more than 24 points per game."""
    young_high_points = df[(df["age"] <= 25) & (df["points_per_game"] > 24)]
    truth = len(young_high_points) > 0
    if truth:
        expl = f"There is at least one player aged 25 or younger with >24 points per game ({len(young_high_points)} such players)."
    else:
        expl = "No player aged 25 or younger scores more than 24 points per game."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a player has an average of more than 5 assists per game, then their position is either forward or guard."""
    high_assists = df[df["assists_per_game"] > 5]
    valid_positions = high_assists["position"].isin(["forward", "guard"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_assists)} players with >5 assists are forwards or guards."
    else:
        viol = high_assists[~valid_positions]
        expl = f"{len(viol)} players with >5 assists have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All players who have played more than 65 games have an average of more than 14 points per game."""
    high_games = df[df["games_played"] > 65]
    condition = high_games["points_per_game"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(high_games)} players with >65 games average >14 points per game."
    else:
        viol = high_games[~condition]
        expl = f"{len(viol)} players with >65 games average <=14 points per game ({', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. There exists at least one center who has an average of more than 23 points per game."""
    centers_high_points = df[(df["position"] == "center") & (df["points_per_game"] > 23)]
    truth = len(centers_high_points) > 0
    if truth:
        expl = f"There is at least one center with >23 points per game ({len(centers_high_points)} such players)."
    else:
        expl = "No center scores more than 23 points per game."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a player is a forward, then their average minutes per game is less than 35."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["minutes_per_game"] < 35
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards average <35 minutes per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards average >=35 minutes per game ({', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. All players who have an average of more than 7 rebounds per game have played more than 60 games."""
    high_rebounds = df[df["rebounds_per_game"] > 7]
    condition = high_rebounds["games_played"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >7 rebounds played >60 games."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} players with >7 rebounds played <=60 games ({', '.join(map(str, viol['games_played'].tolist()))})."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. There exists at least one guard who has an average of more than 17 points per game."""
    guards_high_points = df[(df["position"] == "guard") & (df["points_per_game"] > 17)]
    truth = len(guards_high_points) > 0
    if truth:
        expl = f"There is at least one guard with >17 points per game ({len(guards_high_points)} such players)."
    else:
        expl = "No guard scores more than 17 points per game."
    return truth, expl

def stmt_23(df: pd.DataFrame):
    """23. If a player has an average of more than 6 assists per game, then their position is either forward or guard."""
    high_assists = df[df["assists_per_game"] > 6]
    valid_positions = high_assists["position"].isin(["forward", "guard"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_assists)} players with >6 assists are forwards or guards."
    else:
        viol = high_assists[~valid_positions]
        expl = f"{len(viol)} players with >6 assists have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_24(df: pd.DataFrame):
    """24. All players who are 29 years old or younger have an average of more than 14 points per game."""
    young_players = df[df["age"] <= 29]
    condition = young_players["points_per_game"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(young_players)} players aged 29 or younger average >14 points per game."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} players aged 29 or younger average <=14 points per game ({', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_25(df: pd.DataFrame):
    """25. There exists at least one player who is 30 years old or older and has played more than 70 games."""
    older_high_games = df[(df["age"] >= 30) & (df["games_played"] > 70)]
    truth = len(older_high_games) > 0
    if truth:
        expl = f"There is at least one player aged 30+ with >70 games ({len(older_high_games)} such players)."
    else:
        expl = "No player aged 30+ has played more than 70 games."
    return truth, expl

def stmt_26(df: pd.DataFrame):
    """26. If a player has an average of more than 5 rebounds per game, then their position is either center or forward."""
    high_rebounds = df[df["rebounds_per_game"] > 5]
    valid_positions = high_rebounds["position"].isin(["center", "forward"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >5 rebounds are centers or forwards."
    else:
        viol = high_rebounds[~valid_positions]
        expl = f"{len(viol)} players with >5 rebounds have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_27(df: pd.DataFrame):
    """27. All players who have an average of more than 16 points per game have played more than 60 games."""
    high_points = df[df["points_per_game"] > 16]
    condition = high_points["games_played"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(high_points)} players with >16 points played >60 games."
    else:
        viol = high_points[~condition]
        expl = f"{len(viol)} players with >16 points played <=60 games ({', '.join(map(str, viol['games_played'].tolist()))})."
    return truth, expl

def stmt_28(df: pd.DataFrame):
    """28. There exists at least one center who has an average of more than 6 assists per game."""
    centers_high_assists = df[(df["position"] == "center") & (df["assists_per_game"] > 6)]
    truth = len(centers_high_assists) > 0
    if truth:
        expl = f"There is at least one center with >6 assists per game ({len(centers_high_assists)} such players)."
    else:
        expl = "No center has more than 6 assists per game."
    return truth, expl

def stmt_29(df: pd.DataFrame):
    """29. If a player is a guard, then their average points per game is less than 20."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards average <20 points per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards average >=20 points per game ({', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_30(df: pd.DataFrame):
    """30. All players who have played more than 70 games have an average of more than 25 minutes per game."""
    high_games = df[df["games_played"] > 70]
    condition = high_games["minutes_per_game"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(high_games)} players with >70 games average >25 minutes per game."
    else:
        viol = high_games[~condition]
        expl = f"{len(viol)} players with >70 games average <=25 minutes per game ({', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_31(df: pd.DataFrame):
    """31. There exists at least one forward who has an average of more than 18 points per game."""
    forwards_high_points = df[(df["position"] == "forward") & (df["points_per_game"] > 18)]
    truth = len(forwards_high_points) > 0
    if truth:
        expl = f"There is at least one forward with >18 points per game ({len(forwards_high_points)} such players)."
    else:
        expl = "No forward scores more than 18 points per game."
    return truth, expl

def stmt_32(df: pd.DataFrame):
    """32. If a player has an average of more than 7 assists per game, then their position is either forward or guard."""
    high_assists = df[df["assists_per_game"] > 7]
    valid_positions = high_assists["position"].isin(["forward", "guard"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_assists)} players with >7 assists are forwards or guards."
    else:
        viol = high_assists[~valid_positions]
        expl = f"{len(viol)} players with >7 assists have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_33(df: pd.DataFrame):
    """33. All players who have an average of more than 6 rebounds per game have played more than 60 games."""
    high_rebounds = df[df["rebounds_per_game"] > 6]
    condition = high_rebounds["games_played"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >6 rebounds played >60 games."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} players with >6 rebounds played <=60 games ({', '.join(map(str, viol['games_played'].tolist()))})."
    return truth, expl

def stmt_34(df: pd.DataFrame):
    """34. There exists at least one player who is 25 years old or younger and has an average of more than 24 points per game."""
    young_high_points = df[(df["age"] <= 25) & (df["points_per_game"] > 24)]
    truth = len(young_high_points) > 0
    if truth:
        expl = f"There is at least one player aged 25 or younger with >24 points per game ({len(young_high_points)} such players)."
    else:
        expl = "No player aged 25 or younger scores more than 24 points per game."
    return truth, expl

def stmt_35(df: pd.DataFrame):
    """35. If a player has an average of more than 5 assists per game, then their position is either forward or guard."""
    high_assists = df[df["assists_per_game"] > 5]
    valid_positions = high_assists["position"].isin(["forward", "guard"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_assists)} players with >5 assists are forwards or guards."
    else:
        viol = high_assists[~valid_positions]
        expl = f"{len(viol)} players with >5 assists have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_36(df: pd.DataFrame):
    """36. All players who have played more than 65 games have an average of more than 14 points per game."""
    high_games = df[df["games_played"] > 65]
    condition = high_games["points_per_game"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(high_games)} players with >65 games average >14 points per game."
    else:
        viol = high_games[~condition]
        expl = f"{len(viol)} players with >65 games average <=14 points per game ({', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_37(df: pd.DataFrame):
    """37. There exists at least one center who has an average of more than 23 points per game."""
    centers_high_points = df[(df["position"] == "center") & (df["points_per_game"] > 23)]
    truth = len(centers_high_points) > 0
    if truth:
        expl = f"There is at least one center with >23 points per game ({len(centers_high_points)} such players)."
    else:
        expl = "No center scores more than 23 points per game."
    return truth, expl

def stmt_38(df: pd.DataFrame):
    """38. If a player is a forward, then their average minutes per game is less than 35."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["minutes_per_game"] < 35
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards average <35 minutes per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards average >=35 minutes per game ({', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_39(df: pd.DataFrame):
    """39. All players who have an average of more than 7 rebounds per game have played more than 60 games."""
    high_rebounds = df[df["rebounds_per_game"] > 7]
    condition = high_rebounds["games_played"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >7 rebounds played >60 games."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} players with >7 rebounds played <=60 games ({', '.join(map(str, viol['games_played'].tolist()))})."
    return truth, expl

def stmt_40(df: pd.DataFrame):
    """40. There exists at least one guard who has an average of more than 17 points per game."""
    guards_high_points = df[(df["position"] == "guard") & (df["points_per_game"] > 17)]
    truth = len(guards_high_points) > 0
    if truth:
        expl = f"There is at least one guard with >17 points per game ({len(guards_high_points)} such players)."
    else:
        expl = "No guard scores more than 17 points per game."
    return truth, expl

def stmt_41(df: pd.DataFrame):
    """41. If a player has an average of more than 6 assists per game, then their position is either forward or guard."""
    high_assists = df[df["assists_per_game"] > 6]
    valid_positions = high_assists["position"].isin(["forward", "guard"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_assists)} players with >6 assists are forwards or guards."
    else:
        viol = high_assists[~valid_positions]
        expl = f"{len(viol)} players with >6 assists have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_42(df: pd.DataFrame):
    """42. All players who are 29 years old or younger have an average of more than 14 points per game."""
    young_players = df[df["age"] <= 29]
    condition = young_players["points_per_game"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(young_players)} players aged 29 or younger average >14 points per game."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} players aged 29 or younger average <=14 points per game ({', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_43(df: pd.DataFrame):
    """43. There exists at least one player who is 30 years old or older and has played more than 70 games."""
    older_high_games = df[(df["age"] >= 30) & (df["games_played"] > 70)]
    truth = len(older_high_games) > 0
    if truth:
        expl = f"There is at least one player aged 30+ with >70 games ({len(older_high_games)} such players)."
    else:
        expl = "No player aged 30+ has played more than 70 games."
    return truth, expl

def stmt_44(df: pd.DataFrame):
    """44. If a player has an average of more than 5 rebounds per game, then their position is either center or forward."""
    high_rebounds = df[df["rebounds_per_game"] > 5]
    valid_positions = high_rebounds["position"].isin(["center", "forward"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >5 rebounds are centers or forwards."
    else:
        viol = high_rebounds[~valid_positions]
        expl = f"{len(viol)} players with >5 rebounds have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_45(df: pd.DataFrame):
    """45. All players who have an average of more than 16 points per game have played more than 60 games."""
    high_points = df[df["points_per_game"] > 16]
    condition = high_points["games_played"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(high_points)} players with >16 points played >60 games."
    else:
        viol = high_points[~condition]
        expl = f"{len(viol)} players with >16 points played <=60 games ({', '.join(map(str, viol['games_played'].tolist()))})."
    return truth, expl

def stmt_46(df: pd.DataFrame):
    """46. There exists at least one center who has an average of more than 6 assists per game."""
    centers_high_assists = df[(df["position"] == "center") & (df["assists_per_game"] > 6)]
    truth = len(centers_high_assists) > 0
    if truth:
        expl = f"There is at least one center with >6 assists per game ({len(centers_high_assists)} such players)."
    else:
        expl = "No center has more than 6 assists per game."
    return truth, expl

def stmt_47(df: pd.DataFrame):
    """47. If a player is a guard, then their average points per game is less than 20."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards average <20 points per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards average >=20 points per game ({', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_48(df: pd.DataFrame):
    """48. All players who have played more than 70 games have an average of more than 25 minutes per game."""
    high_games = df[df["games_played"] > 70]
    condition = high_games["minutes_per_game"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(high_games)} players with >70 games average >25 minutes per game."
    else:
        viol = high_games[~condition]
        expl = f"{len(viol)} players with >70 games average <=25 minutes per game ({', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_49(df: pd.DataFrame):
    """49. There exists at least one forward who has an average of more than 18 points per game."""
    forwards_high_points = df[(df["position"] == "forward") & (df["points_per_game"] > 18)]
    truth = len(forwards_high_points) > 0
    if truth:
        expl = f"There is at least one forward with >18 points per game ({len(forwards_high_points)} such players)."
    else:
        expl = "No forward scores more than 18 points per game."
    return truth, expl

def stmt_50(df: pd.DataFrame):
    """50. If a player has an average of more than 7 assists per game, then their position is either forward or guard."""
    high_assists = df[df["assists_per_game"] > 7]
    valid_positions = high_assists["position"].isin(["forward", "guard"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_assists)} players with >7 assists are forwards or guards."
    else:
        viol = high_assists[~valid_positions]
        expl = f"{len(viol)} players with >7 assists have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_51(df: pd.DataFrame):
    """51. All players who have an average of more than 6 rebounds per game have played more than 60 games."""
    high_rebounds = df[df["rebounds_per_game"] > 6]
    condition = high_rebounds["games_played"] > 60
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >6 rebounds played >60 games."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} players with >6 rebounds played <=60 games ({', '.join(map(str, viol['games_played'].tolist()))})."
    return truth, expl

def stmt_52(df: pd.DataFrame):
    """52. There exists at least one player who is 25 years old or younger and has an average of more than 24 points per game."""
    young_high_points = df[(df["age"] <= 25) & (df["points_per_game"] > 24)]
    truth = len(young_high_points) > 0
    if truth:
        expl = f"There is at least one player aged 25 or younger with >24 points per game ({len(young_high_points)} such players)."
    else:
        expl = "No player aged 25 or younger scores more than 24 points per game."
    return truth, expl

def stmt_53(df: pd.DataFrame):
    """53. If a player has an average of more than 5 assists per game, then their position is either forward or guard."""
    high_assists = df[df["assists_per_game"] > 5]
    valid_positions = high_assists["position"].isin(["forward", "guard"])
    truth = valid_positions.all()
    if truth:
        expl = f"All {len(high_assists)} players with >5 assists are forwards or guards."
    else:
        viol = high_assists[~valid_positions]
        expl = f"{len(viol)} players with >5 assists have invalid positions ({', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_54(df: pd.DataFrame):
    """54. All players who have played more than 65 games have an average of more than 14 points per game."""
    high_games = df[df["games_played"] > 65]
    condition = high_games["points_per_game"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(high_games)}