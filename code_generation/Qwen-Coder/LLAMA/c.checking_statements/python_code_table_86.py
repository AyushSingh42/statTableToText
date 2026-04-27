import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are guards have an average points per game of 15 or more, except for one player who is 32 years old and has an average points per game of 12."""
    guards = df[df["position"] == "guard"]
    condition = (guards["points_per_game"] >= 15) | ((guards["age"] == 32) & (guards["points_per_game"] == 12))
    truth = condition.all()
    if truth:
        expl = f"All guards meet the criteria (except one 32-year-old with 12 PPG)."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a forward, then their average minutes per game is greater than 30."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["minutes_per_game"] > 30
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have >30 MPG."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (MPG: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one player who is a center and has an average rebounds per game of 7 or more."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] >= 7
    truth = condition.any()
    if truth:
        expl = f"At least one center has ≥7 RPG."
    else:
        expl = f"No center has ≥7 RPG."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players who are 25 years old or younger have an average assists per game of 4 or more."""
    young_players = df[df["age"] <= 25]
    condition = young_players["assists_per_game"] >= 4
    truth = condition.all()
    if truth:
        expl = f"All players ≤25 have ≥4 APG."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} players ≤25 violate the rule (APG: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a player is a guard and has an average points per game of 20 or more, then their average minutes per game is greater than 30."""
    guards = df[df["position"] == "guard"]
    condition = (guards["points_per_game"] < 20) | (guards["minutes_per_game"] > 30)
    truth = condition.all()
    if truth:
        expl = f"All guards with ≥20 PPG have >30 MPG."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards with ≥20 PPG violate the rule (MPG: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most players in the table have an average games played of 70 or more."""
    condition = df["games_played"] >= 70
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have ≥70 GP."
    else:
        expl = f"{count} out of {total} players have ≥70 GP (less than half)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All players who are forwards have an average age of 25 or more, except for one player who is 23 years old."""
    forwards = df[df["position"] == "forward"]
    condition = (forwards["age"] >= 25) | (forwards["age"] == 23)
    truth = condition.all()
    if truth:
        expl = f"All forwards are ≥25 or exactly 23."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one player who is a guard and has an average rebounds per game of 11 or more."""
    guards = df[df["position"] == "guard"]
    condition = guards["rebounds_per_game"] >= 11
    truth = condition.any()
    if truth:
        expl = f"At least one guard has ≥11 RPG."
    else:
        expl = f"No guard has ≥11 RPG."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a player is a center, then their average points per game is less than 22."""
    centers = df[df["position"] == "center"]
    condition = centers["points_per_game"] < 22
    truth = condition.all()
    if truth:
        expl = f"All centers have <22 PPG."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All players who have an average minutes per game of 35 or more have an average points per game of 20 or more, except for one player who is 32 years old and has an average points per game of 12."""
    high_mpg = df[df["minutes_per_game"] >= 35]
    condition = (high_mpg["points_per_game"] >= 20) | ((high_mpg["age"] == 32) & (high_mpg["points_per_game"] == 12))
    truth = condition.all()
    if truth:
        expl = f"All players with ≥35 MPG have ≥20 PPG (except one 32-year-old with 12 PPG)."
    else:
        viol = high_mpg[~condition]
        expl = f"{len(viol)} players with ≥35 MPG violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Most players in the table have an average assists per game of 4 or more."""
    condition = df["assists_per_game"] >= 4
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have ≥4 APG."
    else:
        expl = f"{count} out of {total} players have ≥4 APG (less than half)."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All players who are 30 years old or older have an average rebounds per game of 7 or more, except for one player who is 32 years old and has an average rebounds per game of 3.3."""
    older_players = df[df["age"] >= 30]
    condition = (older_players["rebounds_per_game"] >= 7) | ((older_players["age"] == 32) & (older_players["rebounds_per_game"] == 3.3))
    truth = condition.all()
    if truth:
        expl = f"All players ≥30 have ≥7 RPG (except one 32-year-old with 3.3 RPG)."
    else:
        viol = older_players[~condition]
        expl = f"{len(viol)} players ≥30 violate the rule (RPG: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a player is a forward and has an average points per game of 20 or more, then their average minutes per game is greater than 30."""
    forwards = df[df["position"] == "forward"]
    condition = (forwards["points_per_game"] < 20) | (forwards["minutes_per_game"] > 30)
    truth = condition.all()
    if truth:
        expl = f"All forwards with ≥20 PPG have >30 MPG."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards with ≥20 PPG violate the rule (MPG: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. There exists at least one player who is a guard and has an average assists per game of 6 or more."""
    guards = df[df["position"] == "guard"]
    condition = guards["assists_per_game"] >= 6
    truth = condition.any()
    if truth:
        expl = f"At least one guard has ≥6 APG."
    else:
        expl = f"No guard has ≥6 APG."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All players who have an average rebounds per game of 9 or more have an average points per game of 20 or more, except for one player who is 25 years old and has an average points per game of 14.3."""
    high_rpg = df[df["rebounds_per_game"] >= 9]
    condition = (high_rpg["points_per_game"] >= 20) | ((high_rpg["age"] == 25) & (high_rpg["points_per_game"] == 14.3))
    truth = condition.all()
    if truth:
        expl = f"All players with ≥9 RPG have ≥20 PPG (except one 25-year-old with 14.3 PPG)."
    else:
        viol = high_rpg[~condition]
        expl = f"{len(viol)} players with ≥9 RPG violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. Most players in the table have an average points per game of 15 or more."""
    condition = df["points_per_game"] >= 15
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have ≥15 PPG."
    else:
        expl = f"{count} out of {total} players have ≥15 PPG (less than half)."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All players who are centers have an average age of 25 or more, except for one player who is 21 years old."""
    centers = df[df["position"] == "center"]
    condition = (centers["age"] >= 25) | (centers["age"] == 21)
    truth = condition.all()
    if truth:
        expl = f"All centers are ≥25 or exactly 21."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a player is a guard and has an average rebounds per game of 9 or more, then their average minutes per game is greater than 30."""
    guards = df[df["position"] == "guard"]
    condition = (guards["rebounds_per_game"] < 9) | (guards["minutes_per_game"] > 30)
    truth = condition.all()
    if truth:
        expl = f"All guards with ≥9 RPG have >30 MPG."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards with ≥9 RPG violate the rule (MPG: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. There exists at least one player who is a forward and has an average assists per game of 7 or more."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["assists_per_game"] >= 7
    truth = condition.any()
    if truth:
        expl = f"At least one forward has ≥7 APG."
    else:
        expl = f"No forward has ≥7 APG."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. All players who have an average minutes per game of 30 or more have an average games played of 60 or more."""
    high_mpg = df[df["minutes_per_game"] >= 30]
    condition = high_mpg["games_played"] >= 60
    truth = condition.all()
    if truth:
        expl = f"All players with ≥30 MPG have ≥60 GP."
    else:
        viol = high_mpg[~condition]
        expl = f"{len(viol)} players with ≥30 MPG violate the rule (GP: {', '.join(map(str, viol['games_played'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. Most players in the table have an average rebounds per game of 5 or more."""
    condition = df["rebounds_per_game"] >= 5
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have ≥5 RPG."
    else:
        expl = f"{count} out of {total} players have ≥5 RPG (less than half)."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. All players who are 28 years old or older have an average points per game of 15 or more, except for one player who is 32 years old and has an average points per game of 12."""
    older_players = df[df["age"] >= 28]
    condition = (older_players["points_per_game"] >= 15) | ((older_players["age"] == 32) & (older_players["points_per_game"] == 12))
    truth = condition.all()
    if truth:
        expl = f"All players ≥28 have ≥15 PPG (except one 32-year-old with 12 PPG)."
    else:
        viol = older_players[~condition]
        expl = f"{len(viol)} players ≥28 violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_23(df: pd.DataFrame):
    """23. If a player is a center and has an average points per game of 15 or more, then their average minutes per game is greater than 30."""
    centers = df[df["position"] == "center"]
    condition = (centers["points_per_game"] < 15) | (centers["minutes_per_game"] > 30)
    truth = condition.all()
    if truth:
        expl = f"All centers with ≥15 PPG have >30 MPG."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers with ≥15 PPG violate the rule (MPG: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_24(df: pd.DataFrame):
    """24. There exists at least one player who is a guard and has an average points per game of 24 or more."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] >= 24
    truth = condition.any()
    if truth:
        expl = f"At least one guard has ≥24 PPG."
    else:
        expl = f"No guard has ≥24 PPG."
    return truth, expl

def stmt_25(df: pd.DataFrame):
    """25. All players who have an average assists per game of 5 or more have an average points per game of 20 or more, except for one player who is 25 years old and has an average points per game of 14.3."""
    high_apg = df[df["assists_per_game"] >= 5]
    condition = (high_apg["points_per_game"] >= 20) | ((high_apg["age"] == 25) & (high_apg["points_per_game"] == 14.3))
    truth = condition.all()
    if truth:
        expl = f"All players with ≥5 APG have ≥20 PPG (except one 25-year-old with 14.3 PPG)."
    else:
        viol = high_apg[~condition]
        expl = f"{len(viol)} players with ≥5 APG violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_26(df: pd.DataFrame):
    """26. Most players in the table have an average games played of 70 or more."""
    condition = df["games_played"] >= 70
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have ≥70 GP."
    else:
        expl = f"{count} out of {total} players have ≥70 GP (less than half)."
    return truth, expl

def stmt_27(df: pd.DataFrame):
    """27. All players who are forwards have an average age of 25 or more, except for two players who are 23 years old."""
    forwards = df[df["position"] == "forward"]
    condition = (forwards["age"] >= 25) | (forwards["age"] == 23)
    truth = condition.all()
    if truth:
        expl = f"All forwards are ≥25 or exactly 23."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_28(df: pd.DataFrame):
    """28. If a player is a guard and has an average rebounds per game of 10 or more, then their average minutes per game is greater than 30."""
    guards = df[df["position"] == "guard"]
    condition = (guards["rebounds_per_game"] < 10) | (guards["minutes_per_game"] > 30)
    truth = condition.all()
    if truth:
        expl = f"All guards with ≥10 RPG have >30 MPG."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards with ≥10 RPG violate the rule (MPG: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_29(df: pd.DataFrame):
    """29. There exists at least one player who is a center and has an average assists per game of 5 or more."""
    centers = df[df["position"] == "center"]
    condition = centers["assists_per_game"] >= 5
    truth = condition.any()
    if truth:
        expl = f"At least one center has ≥5 APG."
    else:
        expl = f"No center has ≥5 APG."
    return truth, expl

def stmt_30(df: pd.DataFrame):
    """30. All players who have an average minutes per game of 35 or more have an average rebounds per game of 7 or more, except for one player who is 32 years old and has an average rebounds per game of 3.3."""
    high_mpg = df[df["minutes_per_game"] >= 35]
    condition = (high_mpg["rebounds_per_game"] >= 7) | ((high_mpg["age"] == 32) & (high_mpg["rebounds_per_game"] == 3.3))
    truth = condition.all()
    if truth:
        expl = f"All players with ≥35 MPG have ≥7 RPG (except one 32-year-old with 3.3 RPG)."
    else:
        viol = high_mpg[~condition]
        expl = f"{len(viol)} players with ≥35 MPG violate the rule (RPG: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_31(df: pd.DataFrame):
    """31. Most players in the table have an average points per game of 18 or more."""
    condition = df["points_per_game"] >= 18
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have ≥18 PPG."
    else:
        expl = f"{count} out of {total} players have ≥18 PPG (less than half)."
    return truth, expl

def stmt_32(df: pd.DataFrame):
    """32. All players who are 25 years old or younger have an average rebounds per game of 5 or more."""
    young_players = df[df["age"] <= 25]
    condition = young_players["rebounds_per_game"] >= 5
    truth = condition.all()
    if truth:
        expl = f"All players ≤25 have ≥5 RPG."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} players ≤25 violate the rule (RPG: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_33(df: pd.DataFrame):
    """33. If a player is a forward and has an average assists per game of 6 or more, then their average minutes per game is greater than 30."""
    forwards = df[df["position"] == "forward"]
    condition = (forwards["assists_per_game"] < 6) | (forwards["minutes_per_game"] > 30)
    truth = condition.all()
    if truth:
        expl = f"All forwards with ≥6 APG have >30 MPG."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards with ≥6 APG violate the rule (MPG: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_34(df: pd.DataFrame):
    """34. There exists at least one player who is a guard and has an average points per game of 25 or more."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] >= 25
    truth = condition.any()
    if truth:
        expl = f"At least one guard has ≥25 PPG."
    else:
        expl = f"No guard has ≥25 PPG."
    return truth, expl

def stmt_35(df: pd.DataFrame):
    """35. All players who have an average rebounds per game of 10 or more have an average points per game of 20 or more, except for one player who is 25 years old and has an average points per game of 14.3."""
    high_rpg = df[df["rebounds_per_game"] >= 10]
    condition = (high_rpg["points_per_game"] >= 20) | ((high_rpg["age"] == 25) & (high_rpg["points_per_game"] == 14.3))
    truth = condition.all()
    if truth:
        expl = f"All players with ≥10 RPG have ≥20 PPG (except one 25-year-old with 14.3 PPG)."
    else:
        viol = high_rpg[~condition]
        expl = f"{len(viol)} players with ≥10 RPG violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_36(df: pd.DataFrame):
    """36. Most players in the table have an average assists per game of 5 or more."""
    condition = df["assists_per_game"] >= 5
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have ≥5 APG."
    else:
        expl = f"{count} out of {total} players have ≥5 APG (less than half)."
    return truth, expl

def stmt_37(df: pd.DataFrame):
    """37. All players who are centers have an average rebounds per game of 7 or more, except for one player who is 21 years old and has an average rebounds per game of 7.9."""
    centers = df[df["position"] == "center"]
    condition = (centers["rebounds_per_game"] >= 7) | ((centers["age"] == 21) & (centers["rebounds_per_game"] == 7.9))
    truth = condition.all()
    if truth:
        expl = f"All centers have ≥7 RPG (except one 21-year-old with 7.9 RPG)."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (RPG: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_38(df: pd.DataFrame):
    """38. If a player is a guard and has an average points per game of 20 or more, then their average rebounds per game is 8 or more, except for one player who is 32 years old and has an average rebounds per game of 4.3."""
    guards = df[df["position"] == "guard"]
    condition = (guards["points_per_game"] < 20) | (guards["rebounds_per_game"] >= 8) | ((guards["age"] == 32) & (guards["rebounds_per_game"] == 4.3))
    truth = condition.all()
    if truth:
        expl = f"All guards with ≥20 PPG have ≥8 RPG (except one 32-year-old with 4.3 RPG)."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards with ≥20 PPG violate the rule (RPG: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_39(df: pd.DataFrame):
    """39. There exists at least one player who is a forward and has an average rebounds per game of 10 or more."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["rebounds_per_game"] >= 10
    truth = condition.any()
    if truth:
        expl = f"At least one forward has ≥10 RPG."
    else:
        expl = f"No forward has ≥10 RPG."
    return truth, expl

def stmt_40(df: pd.DataFrame):
    """40. All players who have an average minutes per game of 30 or more have an average points per game of 15 or more."""
    high_mpg = df[df["minutes_per_game"] >= 30]
    condition = high_mpg["points_per_game"] >= 15
    truth = condition.all()
    if truth:
        expl = f"All players with ≥30 MPG have ≥15 PPG."
    else:
        viol = high_mpg[~condition]
        expl = f"{len(viol)} players with ≥30 MPG violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_41(df: pd.DataFrame):
    """41. Most players in the table have an average rebounds per game of 6 or more."""
    condition = df["rebounds_per_game"] >= 6
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have ≥6 RPG."
    else:
        expl = f"{count} out of {total} players have ≥6 RPG (less than half)."
    return truth, expl

def stmt_42(df: pd.DataFrame):
    """42. All players who are 30 years old or older have an average assists per game of 4 or more, except for one player who is 32 years old and has an average assists per game of 1.7."""
    older_players = df[df["age"] >= 30]
    condition = (older_players["assists_per_game"] >= 4) | ((older_players["age"] == 32) & (older_players["assists_per_game"] == 1.7))
    truth = condition.all()
    if truth:
        expl = f"All players ≥30 have ≥4 APG (except one 32-year-old with 1.7 APG)."
    else:
        viol = older_players[~condition]
        expl = f"{len(viol)} players ≥30 violate the rule (APG: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_43(df: pd.DataFrame):
    """43. If a player is a center and has an average rebounds per game of 8 or more, then their average minutes per game is greater than 30."""
    centers = df[df["position"] == "center"]
    condition = (centers["rebounds_per_game"] < 8) | (centers["minutes_per_game"] > 30)
    truth = condition.all()
    if truth:
        expl = f"All centers with ≥8 RPG have >30 MPG."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers with ≥8 RPG violate the rule (MPG: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_44(df: pd.DataFrame):
    """44. There exists at least one player who is a guard and has an average rebounds per game of 12 or more."""
    guards = df[df["position"] == "guard"]
    condition = guards["rebounds_per_game"] >= 12
    truth = condition.any()
    if truth:
        expl = f"At least one guard has ≥12 RPG."
    else:
        expl = f"No guard has ≥12 RPG."
    return truth, expl

def stmt_45(df: pd.DataFrame):
    """45. All players who have an average assists per game of 6 or more have an average points per game of 20 or more, except for one player who is 25 years old and has an average points per game of 14.3."""
    high_apg = df[df["assists_per_game"] >= 6]
    condition = (high_apg["points_per_game"] >= 20) | ((high_apg["age"] == 25) & (high_apg["points_per_game"] == 14.3))
    truth = condition.all()
    if truth:
        expl = f"All players with ≥6 APG have ≥20 PPG (except one 25-year-old with 14.3 PPG)."
    else:
        viol = high_apg[~condition]
        expl = f"{len(viol)} players with ≥6 APG violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_46(df: pd.DataFrame):
    """46. Most players in the table have an average games played of 75 or more."""
    condition = df["games_played"] >= 75
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have ≥75 GP."
    else:
        expl = f"{count} out of {total} players have ≥75 GP (less than half)."
    return truth, expl

def stmt_47(df: pd.DataFrame):
    """47. All players who are forwards have an average rebounds per game of 6 or more, except for one player who is 23 years old and has an average rebounds per game of 4.5."""
    forwards = df[df["position"] == "forward"]
    condition = (forwards["rebounds_per_game"] >= 6) | ((forwards["age"] == 23) & (forwards["rebounds_per_game"] == 4.5))
    truth = condition.all()
    if truth:
        expl = f"All forwards have ≥6 RPG (except one 23-year-old with 4.5 RPG)."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (RPG: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_48(df: pd.DataFrame):
    """48. If a player is a guard and has an average points per game of 22 or more, then their average minutes per game is greater than 30."""
    guards = df[df["position"] == "guard"]
    condition = (guards["points_per_game"] < 22) | (guards["minutes_per_game"] > 30)
    truth = condition.all()
    if truth:
        expl = f"All guards with ≥22 PPG have >30 MPG."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards with ≥22 PPG violate the rule (MPG: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_49(df: pd.DataFrame):
    """49. There exists at least one player who is a center and has an average points per game of 18 or more."""
    centers = df[df["position"] == "center"]
    condition = centers["points_per_game"] >= 18
    truth = condition.any()
    if truth:
        expl = f"At least one center has ≥18 PPG."
    else:
        expl = f"No center has ≥18 PPG."
    return truth, expl

def stmt_50(df: pd.DataFrame):
    """50. All players who have an average minutes per game of 35 or more have an average assists per game of 5 or more, except for one player who is 32 years old and has an average assists per game of 1.7."""
    high_mpg = df[df["minutes_per_game"] >= 35]
    condition = (high_mpg["assists_per_game"] >= 5) | ((high_mpg["age"] == 32) & (high_mpg["assists_per_game"] == 1.7))
    truth = condition.all()
    if truth:
        expl = f"All players with ≥3