import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All guards have an average of less than 7 assists per game."""
    guards = df[df["position"] == "guard"]
    condition = guards["assists_per_game"] < 7
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have less than 7 assists per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a center, then their age is greater than or equal to 33."""
    centers = df[df["position"] == "center"]
    condition = centers["age"] >= 33
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers are aged 33 or older."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All players who are 30 years old or younger have a points per game average of less than 25."""
    young_players = df[df["age"] <= 30]
    condition = young_players["points_per_game"] < 25
    truth = condition.all()
    if truth:
        expl = f"All {len(young_players)} players aged 30 or younger have less than 25 points per game."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} young players violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one forward who has a rebounds per game average of greater than 11."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["rebounds_per_game"] > 11
    truth = condition.any()
    if truth:
        expl = f"At least one forward has more than 11 rebounds per game."
    else:
        expl = f"No forward has more than 11 rebounds per game."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all players with a minutes per game average of greater than 33, their age is less than 35."""
    high_minutes = df[df["minutes_per_game"] > 33]
    condition = high_minutes["age"] < 35
    truth = condition.all()
    if truth:
        expl = f"All {len(high_minutes)} players with >33 minutes per game are under 35."
    else:
        viol = high_minutes[~condition]
        expl = f"{len(viol)} players with >33 minutes violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All players who have a games played count of greater than 70 have a points per game average of less than 20."""
    many_games = df[df["games_played"] > 70]
    condition = many_games["points_per_game"] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(many_games)} players with >70 games played have less than 20 points per game."
    else:
        viol = many_games[~condition]
        expl = f"{len(viol)} players with >70 games violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a player is a guard, then their rebounds per game average is less than 9."""
    guards = df[df["position"] == "guard"]
    condition = guards["rebounds_per_game"] < 9
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have less than 9 rebounds per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most players have a points per game average of less than 20."""
    total = len(df)
    low_points = df[df["points_per_game"] < 20]
    truth = len(low_points) > total / 2
    if truth:
        expl = f"More than half ({len(low_points)}/{total}) of players have less than 20 points per game."
    else:
        expl = f"Less than half ({len(low_points)}/{total}) of players have less than 20 points per game."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All centers have a rebounds per game average of greater than 4."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have more than 4 rebounds per game."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. For all players with an age of greater than 30, their assists per game average is less than 7."""
    older_players = df[df["age"] > 30]
    condition = older_players["assists_per_game"] < 7
    truth = condition.all()
    if truth:
        expl = f"All {len(older_players)} players over 30 have less than 7 assists per game."
    else:
        viol = older_players[~condition]
        expl = f"{len(viol)} players over 30 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a player is a forward, then their points per game average is less than 22."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["points_per_game"] < 22
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have less than 22 points per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. There exists at least one guard who has a points per game average of greater than 24."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] > 24
    truth = condition.any()
    if truth:
        expl = f"At least one guard has more than 24 points per game."
    else:
        expl = f"No guard has more than 24 points per game."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All players who have a rebounds per game average of greater than 8 have a minutes per game average of greater than 30."""
    high_rebounds = df[df["rebounds_per_game"] > 8]
    condition = high_rebounds["minutes_per_game"] > 30
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >8 rebounds per game have >30 minutes per game."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} players with >8 rebounds violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. For all players with a points per game average of less than 15, their age is greater than 25."""
    low_points = df[df["points_per_game"] < 15]
    condition = low_points["age"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(low_points)} players with <15 points per game are over 25."
    else:
        viol = low_points[~condition]
        expl = f"{len(viol)} players with <15 points violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a player is a center, then their points per game average is greater than 16."""
    centers = df[df["position"] == "center"]
    condition = centers["points_per_game"] > 16
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have more than 16 points per game."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. Most players have a rebounds per game average of less than 9."""
    total = len(df)
    low_rebounds = df[df["rebounds_per_game"] < 9]
    truth = len(low_rebounds) > total / 2
    if truth:
        expl = f"More than half ({len(low_rebounds)}/{total}) of players have less than 9 rebounds per game."
    else:
        expl = f"Less than half ({len(low_rebounds)}/{total}) of players have less than 9 rebounds per game."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All players who have a minutes per game average of less than 30 have a points per game average of less than 18."""
    low_minutes = df[df["minutes_per_game"] < 30]
    condition = low_minutes["points_per_game"] < 18
    truth = condition.all()
    if truth:
        expl = f"All {len(low_minutes)} players with <30 minutes per game have <18 points per game."
    else:
        viol = low_minutes[~condition]
        expl = f"{len(viol)} players with <30 minutes violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. For all players with an age of less than 30, their assists per game average is greater than 3."""
    young_players = df[df["age"] < 30]
    condition = young_players["assists_per_game"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(young_players)} players under 30 have more than 3 assists per game."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} players under 30 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. If a player is a guard, then their points per game average is less than 25."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] < 25
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have less than 25 points per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. There exists at least one forward who has a points per game average of less than 11."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["points_per_game"] < 11
    truth = condition.any()
    if truth:
        expl = f"At least one forward has less than 11 points per game."
    else:
        expl = f"No forward has less than 11 points per game."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. All players who have a games played count of less than 70 have a rebounds per game average of less than 10."""
    few_games = df[df["games_played"] < 70]
    condition = few_games["rebounds_per_game"] < 10
    truth = condition.all()
    if truth:
        expl = f"All {len(few_games)} players with <70 games played have <10 rebounds per game."
    else:
        viol = few_games[~condition]
        expl = f"{len(viol)} players with <70 games violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. For all players with a rebounds per game average of less than 5, their age is less than 28."""
    low_rebounds = df[df["rebounds_per_game"] < 5]
    condition = low_rebounds["age"] < 28
    truth = condition.all()
    if truth:
        expl = f"All {len(low_rebounds)} players with <5 rebounds per game are under 28."
    else:
        viol = low_rebounds[~condition]
        expl = f"{len(viol)} players with <5 rebounds violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_23(df: pd.DataFrame):
    """23. If a player is a center, then their minutes per game average is greater than 30."""
    centers = df[df["position"] == "center"]
    condition = centers["minutes_per_game"] > 30
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have more than 30 minutes per game."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_24(df: pd.DataFrame):
    """24. Most players have a minutes per game average of less than 33."""
    total = len(df)
    low_minutes = df[df["minutes_per_game"] < 33]
    truth = len(low_minutes) > total / 2
    if truth:
        expl = f"More than half ({len(low_minutes)}/{total}) of players have <33 minutes per game."
    else:
        expl = f"Less than half ({len(low_minutes)}/{total}) of players have <33 minutes per game."
    return truth, expl

def stmt_25(df: pd.DataFrame):
    """25. All players who have a points per game average of greater than 20 have a rebounds per game average of greater than 5."""
    high_points = df[df["points_per_game"] > 20]
    condition = high_points["rebounds_per_game"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_points)} players with >20 points per game have >5 rebounds per game."
    else:
        viol = high_points[~condition]
        expl = f"{len(viol)} players with >20 points violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_26(df: pd.DataFrame):
    """26. For all players with an age of greater than 25, their assists per game average is less than 8."""
    older_players = df[df["age"] > 25]
    condition = older_players["assists_per_game"] < 8
    truth = condition.all()
    if truth:
        expl = f"All {len(older_players)} players over 25 have less than 8 assists per game."
    else:
        viol = older_players[~condition]
        expl = f"{len(viol)} players over 25 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_27(df: pd.DataFrame):
    """27. If a player is a forward, then their rebounds per game average is greater than 4."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["rebounds_per_game"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have more than 4 rebounds per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_28(df: pd.DataFrame):
    """28. There exists at least one guard who has a rebounds per game average of greater than 8."""
    guards = df[df["position"] == "guard"]
    condition = guards["rebounds_per_game"] > 8
    truth = condition.any()
    if truth:
        expl = f"At least one guard has more than 8 rebounds per game."
    else:
        expl = f"No guard has more than 8 rebounds per game."
    return truth, expl

def stmt_29(df: pd.DataFrame):
    """29. All players who have a minutes per game average of greater than 32 have a points per game average of less than 24."""
    high_minutes = df[df["minutes_per_game"] > 32]
    condition = high_minutes["points_per_game"] < 24
    truth = condition.all()
    if truth:
        expl = f"All {len(high_minutes)} players with >32 minutes per game have <24 points per game."
    else:
        viol = high_minutes[~condition]
        expl = f"{len(viol)} players with >32 minutes violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_30(df: pd.DataFrame):
    """30. For all players with a points per game average of less than 18, their age is greater than 22."""
    low_points = df[df["points_per_game"] < 18]
    condition = low_points["age"] > 22
    truth = condition.all()
    if truth:
        expl = f"All {len(low_points)} players with <18 points per game are over 22."
    else:
        viol = low_points[~condition]
        expl = f"{len(viol)} players with <18 points violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_31(df: pd.DataFrame):
    """31. If a player is a center, then their assists per game average is less than 8."""
    centers = df[df["position"] == "center"]
    condition = centers["assists_per_game"] < 8
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have less than 8 assists per game."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_32(df: pd.DataFrame):
    """32. Most players have a rebounds per game average of less than 8."""
    total = len(df)
    low_rebounds = df[df["rebounds_per_game"] < 8]
    truth = len(low_rebounds) > total / 2
    if truth:
        expl = f"More than half ({len(low_rebounds)}/{total}) of players have less than 8 rebounds per game."
    else:
        expl = f"Less than half ({len(low_rebounds)}/{total}) of players have less than 8 rebounds per game."
    return truth, expl

def stmt_33(df: pd.DataFrame):
    """33. All players who have a games played count of greater than 65 have a points per game average of less than 22."""
    many_games = df[df["games_played"] > 65]
    condition = many_games["points_per_game"] < 22
    truth = condition.all()
    if truth:
        expl = f"All {len(many_games)} players with >65 games played have <22 points per game."
    else:
        viol = many_games[~condition]
        expl = f"{len(viol)} players with >65 games violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_34(df: pd.DataFrame):
    """34. For all players with an age of less than 32, their rebounds per game average is greater than 4."""
    young_players = df[df["age"] < 32]
    condition = young_players["rebounds_per_game"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(young_players)} players under 32 have more than 4 rebounds per game."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} players under 32 violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_35(df: pd.DataFrame):
    """35. If a player is a guard, then their minutes per game average is less than 35."""
    guards = df[df["position"] == "guard"]
    condition = guards["minutes_per_game"] < 35
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have less than 35 minutes per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_36(df: pd.DataFrame):
    """36. There exists at least one forward who has a minutes per game average of greater than 34."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["minutes_per_game"] > 34
    truth = condition.any()
    if truth:
        expl = f"At least one forward has more than 34 minutes per game."
    else:
        expl = f"No forward has more than 34 minutes per game."
    return truth, expl

def stmt_37(df: pd.DataFrame):
    """37. All players who have a points per game average of greater than 18 have a rebounds per game average of greater than 4."""
    high_points = df[df["points_per_game"] > 18]
    condition = high_points["rebounds_per_game"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_points)} players with >18 points per game have >4 rebounds per game."
    else:
        viol = high_points[~condition]
        expl = f"{len(viol)} players with >18 points violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_38(df: pd.DataFrame):
    """38. For all players with a rebounds per game average of less than 6, their age is less than 29."""
    low_rebounds = df[df["rebounds_per_game"] < 6]
    condition = low_rebounds["age"] < 29
    truth = condition.all()
    if truth:
        expl = f"All {len(low_rebounds)} players with <6 rebounds per game are under 29."
    else:
        viol = low_rebounds[~condition]
        expl = f"{len(viol)} players with <6 rebounds violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_39(df: pd.DataFrame):
    """39. If a player is a center, then their points per game average is less than 23."""
    centers = df[df["position"] == "center"]
    condition = centers["points_per_game"] < 23
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have less than 23 points per game."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_40(df: pd.DataFrame):
    """40. Most players have a minutes per game average of less than 32."""
    total = len(df)
    low_minutes = df[df["minutes_per_game"] < 32]
    truth = len(low_minutes) > total / 2
    if truth:
        expl = f"More than half ({len(low_minutes)}/{total}) of players have <32 minutes per game."
    else:
        expl = f"Less than half ({len(low_minutes)}/{total}) of players have <32 minutes per game."
    return truth, expl

def stmt_41(df: pd.DataFrame):
    """41. All players who have a games played count of less than 75 have a rebounds per game average of less than 11."""
    few_games = df[df["games_played"] < 75]
    condition = few_games["rebounds_per_game"] < 11
    truth = condition.all()
    if truth:
        expl = f"All {len(few_games)} players with <75 games played have <11 rebounds per game."
    else:
        viol = few_games[~condition]
        expl = f"{len(viol)} players with <75 games violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_42(df: pd.DataFrame):
    """42. For all players with an age of greater than 26, their assists per game average is less than 7."""
    older_players = df[df["age"] > 26]
    condition = older_players["assists_per_game"] < 7
    truth = condition.all()
    if truth:
        expl = f"All {len(older_players)} players over 26 have less than 7 assists per game."
    else:
        viol = older_players[~condition]
        expl = f"{len(viol)} players over 26 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_43(df: pd.DataFrame):
    """43. If a player is a forward, then their points per game average is less than 21."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["points_per_game"] < 21
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have less than 21 points per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_44(df: pd.DataFrame):
    """44. There exists at least one guard who has a points per game average of less than 15."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] < 15
    truth = condition.any()
    if truth:
        expl = f"At least one guard has less than 15 points per game."
    else:
        expl = f"No guard has less than 15 points per game."
    return truth, expl

def stmt_45(df: pd.DataFrame):
    """45. All players who have a minutes per game average of greater than 31 have a points per game average of less than 23."""
    high_minutes = df[df["minutes_per_game"] > 31]
    condition = high_minutes["points_per_game"] < 23
    truth = condition.all()
    if truth:
        expl = f"All {len(high_minutes)} players with >31 minutes per game have <23 points per game."
    else:
        viol = high_minutes[~condition]
        expl = f"{len(viol)} players with >31 minutes violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_46(df: pd.DataFrame):
    """46. For all players with a points per game average of less than 19, their age is greater than 23."""
    low_points = df[df["points_per_game"] < 19]
    condition = low_points["age"] > 23
    truth = condition.all()
    if truth:
        expl = f"All {len(low_points)} players with <19 points per game are over 23."
    else:
        viol = low_points[~condition]
        expl = f"{len(viol)} players with <19 points violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_47(df: pd.DataFrame):
    """47. If a player is a center, then their rebounds per game average is greater than 5."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have more than 5 rebounds per game."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_48(df: pd.DataFrame):
    """48. Most players have a rebounds per game average of less than 7."""
    total = len(df)
    low_rebounds = df[df["rebounds_per_game"] < 7]
    truth = len(low_rebounds) > total / 2
    if truth:
        expl = f"More than half ({len(low_rebounds)}/{total}) of players have less than 7 rebounds per game."
    else:
        expl = f"Less than half ({len(low_rebounds)}/{total}) of players have less than 7 rebounds per game."
    return truth, expl

def stmt_49(df: pd.DataFrame):
    """49. All players who have a games played count of greater than 70 have a points per game average of less than 21."""
    many_games = df[df["games_played"] > 70]
    condition = many_games["points_per_game"] < 21
    truth = condition.all()
    if truth:
        expl = f"All {len(many_games)} players with >70 games played have <21 points per game."
    else:
        viol = many_games[~condition]
        expl = f"{len(viol)} players with >70 games violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_50(df: pd.DataFrame):
    """50. For all players with an age of less than 31, their assists per game average is greater than 3."""
    young_players = df[df["age"] < 31]
    condition = young_players["assists_per_game"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(young_players)} players under 31 have more than 3 assists per game."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} players under 31 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_51(df: pd.DataFrame):
    """51. If a player is a guard, then their rebounds per game average is less than 9."""
    guards = df[df["position"] == "guard"]
    condition = guards["rebounds_per_game"] < 9
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have less than 9 rebounds per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_52(df: pd.DataFrame):
    """52. There exists at least one forward who has a rebounds per game average of greater than 10."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["rebounds_per_game"] > 10
    truth = condition.any()
    if truth:
        expl = f"At least one forward has more than 10 rebounds per game."
    else:
        expl = f"No forward has more than 10 rebounds per game."
    return truth, expl

def stmt_53(df: pd.DataFrame):
    """53. All players who have a points per game average of greater than 19 have a rebounds per game average of greater than 5."""
    high_points = df[df["points_per_game"] > 19]
    condition = high_points["rebounds_per_game"] > 5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_points)} players with >19 points per game have >5 rebounds per game."
    else:
        viol = high_points[~condition]
        expl = f"{len(viol)} players with >19 points violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_54(df: pd.DataFrame):
    """54. For all players with a rebounds per game average of less than 5, their age is less than 27."""
    low_rebounds = df[df["rebounds_per_game"] < 5]
    condition = low_rebounds["age"] < 27
    truth = condition.all()
    if truth:
        expl = f"All {len(low_rebounds)} players with <5 rebounds per game are under 27."
    else:
        viol = low_rebounds[~condition]
        expl = f"{len(viol)} players with <5 rebounds violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_55(df: pd.DataFrame):
    """55. If a