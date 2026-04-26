import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are guards have an average points per game of less than 25."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = True
        expl = "No guards in dataset."
    else:
        condition = guards["points_per_game"] < 25
        truth = condition.all()
        if truth:
            expl = f"All {len(guards)} guards have points per game < 25."
        else:
            viol = guards[~condition]
            expl = f"{len(viol)} guards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a forward, then their average rebounds per game is less than 12."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = True
        expl = "No forwards in dataset."
    else:
        condition = forwards["rebounds_per_game"] < 12
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards)} forwards have rebounds per game < 12."
        else:
            viol = forwards[~condition]
            expl = f"{len(viol)} forwards violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one player who is a center and has an average points per game of greater than 20."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = False
        expl = "No centers in dataset."
    else:
        condition = centers["points_per_game"] > 20
        truth = condition.any()
        if truth:
            expl = f"At least one center has points per game > 20."
        else:
            expl = f"No centers have points per game > 20."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players who are 30 years old or older have an average minutes per game of less than 35."""
    older = df[df["age"] >= 30]
    if older.empty:
        truth = True
        expl = "No players 30+ in dataset."
    else:
        condition = older["minutes_per_game"] < 35
        truth = condition.all()
        if truth:
            expl = f"All {len(older)} players 30+ have minutes per game < 35."
        else:
            viol = older[~condition]
            expl = f"{len(viol)} players 30+ violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a player is a guard, then their average assists per game is less than 5."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = True
        expl = "No guards in dataset."
    else:
        condition = guards["assists_per_game"] < 5
        truth = condition.all()
        if truth:
            expl = f"All {len(guards)} guards have assists per game < 5."
        else:
            viol = guards[~condition]
            expl = f"{len(viol)} guards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most players have an average games played of greater than 60."""
    condition = df["games_played"] > 60
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} players have games played > 60."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All players who are 25 years old or younger have an average points per game greater than 15."""
    young = df[df["age"] <= 25]
    if young.empty:
        truth = True
        expl = "No players 25 or younger in dataset."
    else:
        condition = young["points_per_game"] > 15
        truth = condition.all()
        if truth:
            expl = f"All {len(young)} players 25 or younger have points per game > 15."
        else:
            viol = young[~condition]
            expl = f"{len(viol)} players 25 or younger violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a player is a forward, then their average age is less than 30."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = True
        expl = "No forwards in dataset."
    else:
        condition = forwards["age"] < 30
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards)} forwards have age < 30."
        else:
            viol = forwards[~condition]
            expl = f"{len(viol)} forwards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one player who is a guard and has an average points per game of greater than 20."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["points_per_game"] > 20
        truth = condition.any()
        if truth:
            expl = f"At least one guard has points per game > 20."
        else:
            expl = f"No guards have points per game > 20."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All players who have an average points per game of greater than 20 have an average minutes per game of greater than 25."""
    high_points = df[df["points_per_game"] > 20]
    if high_points.empty:
        truth = True
        expl = "No players with points per game > 20."
    else:
        condition = high_points["minutes_per_game"] > 25
        truth = condition.all()
        if truth:
            expl = f"All {len(high_points)} players with points per game > 20 have minutes per game > 25."
        else:
            viol = high_points[~condition]
            expl = f"{len(viol)} players with points per game > 20 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a player is a center, then their average rebounds per game is greater than 3."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = True
        expl = "No centers in dataset."
    else:
        condition = centers["rebounds_per_game"] > 3
        truth = condition.all()
        if truth:
            expl = f"All {len(centers)} centers have rebounds per game > 3."
        else:
            viol = centers[~condition]
            expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Most players have an average points per game of less than 20."""
    condition = df["points_per_game"] < 20
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} players have points per game < 20."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All players who are 28 years old or older have an average assists per game of less than 7."""
    older = df[df["age"] >= 28]
    if older.empty:
        truth = True
        expl = "No players 28+ in dataset."
    else:
        condition = older["assists_per_game"] < 7
        truth = condition.all()
        if truth:
            expl = f"All {len(older)} players 28+ have assists per game < 7."
        else:
            viol = older[~condition]
            expl = f"{len(viol)} players 28+ violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a player is a forward, then their average points per game is greater than 12."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = True
        expl = "No forwards in dataset."
    else:
        condition = forwards["points_per_game"] > 12
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards)} forwards have points per game > 12."
        else:
            viol = forwards[~condition]
            expl = f"{len(viol)} forwards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one player who is a guard and has an average rebounds per game of less than 6."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["rebounds_per_game"] < 6
        truth = condition.any()
        if truth:
            expl = f"At least one guard has rebounds per game < 6."
        else:
            expl = f"No guards have rebounds per game < 6."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All players who have an average minutes per game of less than 30 have an average points per game of less than 18."""
    low_minutes = df[df["minutes_per_game"] < 30]
    if low_minutes.empty:
        truth = True
        expl = "No players with minutes per game < 30."
    else:
        condition = low_minutes["points_per_game"] < 18
        truth = condition.all()
        if truth:
            expl = f"All {len(low_minutes)} players with minutes per game < 30 have points per game < 18."
        else:
            viol = low_minutes[~condition]
            expl = f"{len(viol)} players with minutes per game < 30 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a player is a center, then their average age is greater than 25."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = True
        expl = "No centers in dataset."
    else:
        condition = centers["age"] > 25
        truth = condition.all()
        if truth:
            expl = f"All {len(centers)} centers have age > 25."
        else:
            viol = centers[~condition]
            expl = f"{len(viol)} centers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most players have an average rebounds per game of less than 10."""
    condition = df["rebounds_per_game"] < 10
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} players have rebounds per game < 10."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. All players who are 22 years old or younger have an average points per game of greater than 15."""
    young = df[df["age"] <= 22]
    if young.empty:
        truth = True
        expl = "No players 22 or younger in dataset."
    else:
        condition = young["points_per_game"] > 15
        truth = condition.all()
        if truth:
            expl = f"All {len(young)} players 22 or younger have points per game > 15."
        else:
            viol = young[~condition]
            expl = f"{len(viol)} players 22 or younger violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a player is a guard, then their average rebounds per game is less than 12."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = True
        expl = "No guards in dataset."
    else:
        condition = guards["rebounds_per_game"] < 12
        truth = condition.all()
        if truth:
            expl = f"All {len(guards)} guards have rebounds per game < 12."
        else:
            viol = guards[~condition]
            expl = f"{len(viol)} guards violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. There exists at least one player who is a forward and has an average points per game of greater than 22."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = False
        expl = "No forwards in dataset."
    else:
        condition = forwards["points_per_game"] > 22
        truth = condition.any()
        if truth:
            expl = f"At least one forward has points per game > 22."
        else:
            expl = f"No forwards have points per game > 22."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. All players who have an average assists per game of greater than 5 have an average minutes per game of greater than 28."""
    high_assists = df[df["assists_per_game"] > 5]
    if high_assists.empty:
        truth = True
        expl = "No players with assists per game > 5."
    else:
        condition = high_assists["minutes_per_game"] > 28
        truth = condition.all()
        if truth:
            expl = f"All {len(high_assists)} players with assists per game > 5 have minutes per game > 28."
        else:
            viol = high_assists[~condition]
            expl = f"{len(viol)} players with assists per game > 5 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_23(df: pd.DataFrame):
    """23. If a player is a center, then their average points per game is greater than 14."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = True
        expl = "No centers in dataset."
    else:
        condition = centers["points_per_game"] > 14
        truth = condition.all()
        if truth:
            expl = f"All {len(centers)} centers have points per game > 14."
        else:
            viol = centers[~condition]
            expl = f"{len(viol)} centers violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_24(df: pd.DataFrame):
    """24. Most players have an average assists per game of less than 6."""
    condition = df["assists_per_game"] < 6
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} players have assists per game < 6."
    return truth, expl

def stmt_25(df: pd.DataFrame):
    """25. All players who are 27 years old or older have an average rebounds per game of less than 11."""
    older = df[df["age"] >= 27]
    if older.empty:
        truth = True
        expl = "No players 27+ in dataset."
    else:
        condition = older["rebounds_per_game"] < 11
        truth = condition.all()
        if truth:
            expl = f"All {len(older)} players 27+ have rebounds per game < 11."
        else:
            viol = older[~condition]
            expl = f"{len(viol)} players 27+ violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_26(df: pd.DataFrame):
    """26. If a player is a forward, then their average age is less than 32."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = True
        expl = "No forwards in dataset."
    else:
        condition = forwards["age"] < 32
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards)} forwards have age < 32."
        else:
            viol = forwards[~condition]
            expl = f"{len(viol)} forwards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_27(df: pd.DataFrame):
    """27. There exists at least one player who is a guard and has an average points per game of less than 14."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["points_per_game"] < 14
        truth = condition.any()
        if truth:
            expl = f"At least one guard has points per game < 14."
        else:
            expl = f"No guards have points per game < 14."
    return truth, expl

def stmt_28(df: pd.DataFrame):
    """28. All players who have an average points per game of less than 18 have an average minutes per game of less than 32."""
    low_points = df[df["points_per_game"] < 18]
    if low_points.empty:
        truth = True
        expl = "No players with points per game < 18."
    else:
        condition = low_points["minutes_per_game"] < 32
        truth = condition.all()
        if truth:
            expl = f"All {len(low_points)} players with points per game < 18 have minutes per game < 32."
        else:
            viol = low_points[~condition]
            expl = f"{len(viol)} players with points per game < 18 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_29(df: pd.DataFrame):
    """29. If a player is a center, then their average assists per game is less than 4."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = True
        expl = "No centers in dataset."
    else:
        condition = centers["assists_per_game"] < 4
        truth = condition.all()
        if truth:
            expl = f"All {len(centers)} centers have assists per game < 4."
        else:
            viol = centers[~condition]
            expl = f"{len(viol)} centers violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_30(df: pd.DataFrame):
    """30. Most players have an average points per game of greater than 12."""
    condition = df["points_per_game"] > 12
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} players have points per game > 12."
    return truth, expl

def stmt_31(df: pd.DataFrame):
    """31. All players who are 24 years old or younger have an average rebounds per game of less than 12."""
    young = df[df["age"] <= 24]
    if young.empty:
        truth = True
        expl = "No players 24 or younger in dataset."
    else:
        condition = young["rebounds_per_game"] < 12
        truth = condition.all()
        if truth:
            expl = f"All {len(young)} players 24 or younger have rebounds per game < 12."
        else:
            viol = young[~condition]
            expl = f"{len(viol)} players 24 or younger violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_32(df: pd.DataFrame):
    """32. If a player is a guard, then their average points per game is less than 22."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = True
        expl = "No guards in dataset."
    else:
        condition = guards["points_per_game"] < 22
        truth = condition.all()
        if truth:
            expl = f"All {len(guards)} guards have points per game < 22."
        else:
            viol = guards[~condition]
            expl = f"{len(viol)} guards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_33(df: pd.DataFrame):
    """33. There exists at least one player who is a forward and has an average rebounds per game of greater than 10."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = False
        expl = "No forwards in dataset."
    else:
        condition = forwards["rebounds_per_game"] > 10
        truth = condition.any()
        if truth:
            expl = f"At least one forward has rebounds per game > 10."
        else:
            expl = f"No forwards have rebounds per game > 10."
    return truth, expl

def stmt_34(df: pd.DataFrame):
    """34. All players who have an average minutes per game of greater than 30 have an average points per game of greater than 16."""
    high_minutes = df[df["minutes_per_game"] > 30]
    if high_minutes.empty:
        truth = True
        expl = "No players with minutes per game > 30."
    else:
        condition = high_minutes["points_per_game"] > 16
        truth = condition.all()
        if truth:
            expl = f"All {len(high_minutes)} players with minutes per game > 30 have points per game > 16."
        else:
            viol = high_minutes[~condition]
            expl = f"{len(viol)} players with minutes per game > 30 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_35(df: pd.DataFrame):
    """35. If a player is a center, then their average age is less than 30."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = True
        expl = "No centers in dataset."
    else:
        condition = centers["age"] < 30
        truth = condition.all()
        if truth:
            expl = f"All {len(centers)} centers have age < 30."
        else:
            viol = centers[~condition]
            expl = f"{len(viol)} centers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_36(df: pd.DataFrame):
    """36. Most players have an average assists per game of less than 5."""
    condition = df["assists_per_game"] < 5
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} players have assists per game < 5."
    return truth, expl

def stmt_37(df: pd.DataFrame):
    """37. All players who are 26 years old or older have an average points per game of less than 21."""
    older = df[df["age"] >= 26]
    if older.empty:
        truth = True
        expl = "No players 26+ in dataset."
    else:
        condition = older["points_per_game"] < 21
        truth = condition.all()
        if truth:
            expl = f"All {len(older)} players 26+ have points per game < 21."
        else:
            viol = older[~condition]
            expl = f"{len(viol)} players 26+ violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_38(df: pd.DataFrame):
    """38. If a player is a forward, then their average rebounds per game is greater than 5."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = True
        expl = "No forwards in dataset."
    else:
        condition = forwards["rebounds_per_game"] > 5
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards)} forwards have rebounds per game > 5."
        else:
            viol = forwards[~condition]
            expl = f"{len(viol)} forwards violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_39(df: pd.DataFrame):
    """39. There exists at least one player who is a guard and has an average assists per game of greater than 4."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["assists_per_game"] > 4
        truth = condition.any()
        if truth:
            expl = f"At least one guard has assists per game > 4."
        else:
            expl = f"No guards have assists per game > 4."
    return truth, expl

def stmt_40(df: pd.DataFrame):
    """40. All players who have an average rebounds per game of less than 9 have an average minutes per game of less than 30."""
    low_rebounds = df[df["rebounds_per_game"] < 9]
    if low_rebounds.empty:
        truth = True
        expl = "No players with rebounds per game < 9."
    else:
        condition = low_rebounds["minutes_per_game"] < 30
        truth = condition.all()
        if truth:
            expl = f"All {len(low_rebounds)} players with rebounds per game < 9 have minutes per game < 30."
        else:
            viol = low_rebounds[~condition]
            expl = f"{len(viol)} players with rebounds per game < 9 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_41(df: pd.DataFrame):
    """41. If a player is a center, then their average points per game is less than 23."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = True
        expl = "No centers in dataset."
    else:
        condition = centers["points_per_game"] < 23
        truth = condition.all()
        if truth:
            expl = f"All {len(centers)} centers have points per game < 23."
        else:
            viol = centers[~condition]
            expl = f"{len(viol)} centers violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_42(df: pd.DataFrame):
    """42. Most players have an average points per game of less than 19."""
    condition = df["points_per_game"] < 19
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} players have points per game < 19."
    return truth, expl

def stmt_43(df: pd.DataFrame):
    """43. All players who are 23 years old or younger have an average assists per game of less than 7."""
    young = df[df["age"] <= 23]
    if young.empty:
        truth = True
        expl = "No players 23 or younger in dataset."
    else:
        condition = young["assists_per_game"] < 7
        truth = condition.all()
        if truth:
            expl = f"All {len(young)} players 23 or younger have assists per game < 7."
        else:
            viol = young[~condition]
            expl = f"{len(viol)} players 23 or younger violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_44(df: pd.DataFrame):
    """44. If a player is a guard, then their average rebounds per game is less than 11."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = True
        expl = "No guards in dataset."
    else:
        condition = guards["rebounds_per_game"] < 11
        truth = condition.all()
        if truth:
            expl = f"All {len(guards)} guards have rebounds per game < 11."
        else:
            viol = guards[~condition]
            expl = f"{len(viol)} guards violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_45(df: pd.DataFrame):
    """45. There exists at least one player who is a forward and has an average points per game of less than 19."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = False
        expl = "No forwards in dataset."
    else:
        condition = forwards["points_per_game"] < 19
        truth = condition.any()
        if truth:
            expl = f"At least one forward has points per game < 19."
        else:
            expl = f"No forwards have points per game < 19."
    return truth, expl

def stmt_46(df: pd.DataFrame):
    """46. All players who have an average minutes per game of less than 28 have an average points per game of less than 17."""
    low_minutes = df[df["minutes_per_game"] < 28]
    if low_minutes.empty:
        truth = True
        expl = "No players with minutes per game < 28."
    else:
        condition = low_minutes["points_per_game"] < 17
        truth = condition.all()
        if truth:
            expl = f"All {len(low_minutes)} players with minutes per game < 28 have points per game < 17."
        else:
            viol = low_minutes[~condition]
            expl = f"{len(viol)} players with minutes per game < 28 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_47(df: pd.DataFrame):
    """47. If a player is a center, then their average age is greater than 24."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        truth = True
        expl = "No centers in dataset."
    else:
        condition = centers["age"] > 24
        truth = condition.all()
        if truth:
            expl = f"All {len(centers)} centers have age > 24."
        else:
            viol = centers[~condition]
            expl = f"{len(viol)} centers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_48(df: pd.DataFrame):
    """48. Most players have an average rebounds per game of less than 9."""
    condition = df["rebounds_per_game"] < 9
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} players have rebounds per game < 9."
    return truth, expl

def stmt_49(df: pd.DataFrame):
    """49. All players who are 29 years old or older have an average assists per game of less than 6."""
    older = df[df["age"] >= 29]
    if older.empty:
        truth = True
        expl = "No players 29+ in dataset."
    else:
        condition = older["assists_per_game"] < 6
        truth = condition.all()
        if truth:
            expl = f"All {len(older)} players 29+ have assists per game < 6."
        else:
            viol = older[~condition]
            expl = f"{len(viol)} players 29+ violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_50(df: pd.DataFrame):
    """50. If a player is a forward, then their average points per game is greater than 13."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        truth = True
        expl = "No forwards in dataset."
    else:
        condition = forwards["points_per_game"] > 13
        truth = condition.all()
        if truth:
            expl = f"All {len(forwards)} forwards have points per game > 13."
        else:
            viol = forwards[~condition]
            expl = f"{len(viol)} forwards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_51(df: pd.DataFrame):
    """51. There exists at least one player who is a guard and has an average rebounds per game of greater than 5."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        truth = False
        expl = "No guards in dataset."
    else:
        condition = guards["rebounds_per_game"] > 5
        truth = condition.any()
        if truth:
            expl = f"At least one guard has rebounds per game > 5."
        else:
            expl = f"No guards have rebounds per game > 5."
    return truth, expl

def stmt_52(df: pd.DataFrame):
    """52. All players who have an average points per game