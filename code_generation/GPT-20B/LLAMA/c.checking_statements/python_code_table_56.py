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
        expl = f"All {len(centers)} centers have rebounds >= 7."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} center(s) violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
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
        expl = f"{len(viol)} forward(s) violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all players with an average of more than 30 minutes per game, their points per game are less than or equal to 24.4."""
    players = df[df["minutes_per_game"] > 30]
    condition = players["points_per_game"] <= 24.4
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with >30 min have points <= 24.4."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} player(s) violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one guard whose assists per game are greater than 6."""
    guards = df[(df["position"] == "guard") & (df["assists_per_game"] > 6)]
    truth = not guards.empty
    if truth:
        expl = f"Found {len(guards)} guard(s) with assists > 6."
    else:
        expl = "No guard with assists > 6 found."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All players who are 28 years old or younger have an average of more than 10 points per game."""
    young = df[df["age"] <= 28]
    condition = young["points_per_game"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} players aged <=28 have points > 10."
    else:
        viol = young[~condition]
        expl = f"{len(viol)} player(s) violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a player is a center aged over 30, then their rebounds per game are less than 11."""
    centers_over30 = df[(df["position"] == "center") & (df["age"] > 30)]
    condition = centers_over30["rebounds_per_game"] < 11
    truth = condition.all()
    if truth:
        expl = f"All {len(centers_over30)} centers aged >30 have rebounds < 11."
    else:
        viol = centers_over30[~condition]
        expl = f"{len(viol)} center(s) violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all players with an average of more than 7 assists per game, their position is either center or forward."""
    players = df[df["assists_per_game"] > 7]
    condition = players["position"].isin(["center", "forward"])
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with >7 assists are center or forward."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} player(s) violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most players in the table have an average of more than 20 points per game."""
    total = len(df)
    count = df[df["points_per_game"] > 20].shape[0]
    truth = count > total / 2
    if truth:
        expl = f"{count} of {total} players have points > 20."
    else:
        expl = f"Only {count} of {total} players have points > 20."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a player is a forward aged below 28, then their height is not provided in the data, but their average points per game are greater than 19."""
    forwards_below28 = df[(df["position"] == "forward") & (df["age"] < 28)]
    # Height column not present; assume not provided.
    condition = forwards_below28["points_per_game"] > 19
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards_below28)} forwards aged <28 have points > 19."
    else:
        viol = forwards_below28[~condition]
        expl = f"{len(viol)} forward(s) violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Every player with an average of more than 10 rebounds per game has a position of either center or forward."""
    players = df[df["rebounds_per_game"] > 10]
    condition = players["position"].isin(["center", "forward"])
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with >10 rebounds are center or forward."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} player(s) violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. For all players with an average of more than 70 games played, their minutes per game are less than or equal to 35.6."""
    players = df[df["games_played"] > 70]
    condition = players["minutes_per_game"] <= 35.6
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with >70 games have minutes <= 35.6."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} player(s) violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a player is a guard aged over 26, then their assists per game are less than 7."""
    guards_over26 = df[(df["position"] == "guard") & (df["age"] > 26)]
    condition = guards_over26["assists_per_game"] < 7
    truth = condition.all()
    if truth:
        expl = f"All {len(guards_over26)} guards aged >26 have assists < 7."
    else:
        viol = guards_over26[~condition]
        expl = f"{len(viol)} guard(s) violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_56.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()