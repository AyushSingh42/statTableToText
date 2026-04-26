import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are centers have an average of at least 7 rebounds per game."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] >= 7
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have at least 7 rebounds per game."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a forward, then their age is between 21 and 31 years."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["age"].between(21, 31, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards are aged 21-31."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all players with an average of more than 30 minutes per game, their points per game are less than or equal to 24.4."""
    high_minutes = df[df["minutes_per_game"] > 30]
    condition = high_minutes["points_per_game"] <= 24.4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_minutes)} players with >30 minutes/game have <=24.4 points/game."
    else:
        viol = high_minutes[~condition]
        expl = f"{len(viol)} players violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one guard whose assists per game are greater than 6."""
    guards = df[df["position"] == "guard"]
    condition = guards["assists_per_game"] > 6
    truth = condition.any()
    if truth:
        expl = f"At least one guard ({len(guards[condition])}) has >6 assists/game."
    else:
        expl = f"No guards have >6 assists/game."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All players who are 28 years old or younger have an average of more than 10 points per game."""
    young_players = df[df["age"] <= 28]
    condition = young_players["points_per_game"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(young_players)} players aged 28 or younger have >10 points/game."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} players aged 28 or younger violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a player is a center aged over 30, then their rebounds per game are less than 11."""
    centers_over_30 = df[(df["position"] == "center") & (df["age"] > 30)]
    condition = centers_over_30["rebounds_per_game"] < 11
    truth = condition.all()
    if truth:
        expl = f"All {len(centers_over_30)} centers aged over 30 have <11 rebounds/game."
    else:
        viol = centers_over_30[~condition]
        expl = f"{len(viol)} centers aged over 30 violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all players with an average of more than 7 assists per game, their position is either center or forward."""
    high_assists = df[df["assists_per_game"] > 7]
    condition = high_assists["position"].isin(["center", "forward"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_assists)} players with >7 assists/game are center or forward."
    else:
        viol = high_assists[~condition]
        expl = f"{len(viol)} players with >7 assists/game are not center or forward (positions: {', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most players in the table have an average of more than 20 points per game."""
    total_players = len(df)
    high_points = df[df["points_per_game"] > 20]
    truth = len(high_points) > total_players / 2
    if truth:
        expl = f"{len(high_points)} out of {total_players} players have >20 points/game (more than half)."
    else:
        expl = f"{len(high_points)} out of {total_players} players have >20 points/game (not more than half)."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a player is a forward aged below 28, then their height is not provided in the data, but their average points per game are greater than 19."""
    # Note: This statement assumes 'height' column exists, which it doesn't in the sample data.
    # So we'll skip checking the height part and only check the points part.
    forwards_young = df[(df["position"] == "forward") & (df["age"] < 28)]
    condition = forwards_young["points_per_game"] > 19
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards_young)} forwards aged below 28 have >19 points/game."
    else:
        viol = forwards_young[~condition]
        expl = f"{len(viol)} forwards aged below 28 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Every player with an average of more than 10 rebounds per game has a position of either center or forward."""
    high_rebounds = df[df["rebounds_per_game"] > 10]
    condition = high_rebounds["position"].isin(["center", "forward"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >10 rebounds/game are center or forward."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} players with >10 rebounds/game are not center or forward (positions: {', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. For all players with an average of more than 70 games played, their minutes per game are less than or equal to 35.6."""
    high_games = df[df["games_played"] > 70]
    condition = high_games["minutes_per_game"] <= 35.6
    truth = condition.all()
    if truth:
        expl = f"All {len(high_games)} players with >70 games played have <=35.6 minutes/game."
    else:
        viol = high_games[~condition]
        expl = f"{len(viol)} players with >70 games played violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a player is a guard aged over 26, then their assists per game are less than 7."""
    guards_over_26 = df[(df["position"] == "guard") & (df["age"] > 26)]
    condition = guards_over_26["assists_per_game"] < 7
    truth = condition.all()
    if truth:
        expl = f"All {len(guards_over_26)} guards aged over 26 have <7 assists/game."
    else:
        viol = guards_over_26[~condition]
        expl = f"{len(viol)} guards aged over 26 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_56.csv")

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
        (12, stmt_12)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()