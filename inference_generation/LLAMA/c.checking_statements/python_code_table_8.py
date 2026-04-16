import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players with age greater than 28 have rebounds per game greater than 7."""
    players = df[df["age"] > 28]
    condition = players["rebounds_per_game"] > 7
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with age > 28 have rebounds per game > 7."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))}, rebounds per game: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a center, then their minutes per game are less than 35."""
    centers = df[df["position"] == "center"]
    condition = centers["minutes_per_game"] < 35
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have minutes per game < 35."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (minutes per game: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Every player with points per game greater than 20 has assists per game greater than 3."""
    players = df[df["points_per_game"] > 20]
    condition = players["assists_per_game"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with points per game > 20 have assists per game > 3."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players violate the rule (points per game: {', '.join(map(str, viol['points_per_game'].tolist()))}, assists per game: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All guards with age less than 25 have points per game less than 18."""
    guards = df[(df["position"] == "guard") & (df["age"] < 25)]
    condition = guards["points_per_game"] < 18
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards with age < 25 have points per game < 18."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))}, points per game: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a player has games played greater than 70, then their rebounds per game are greater than 6."""
    players = df[df["games_played"] > 70]
    condition = players["rebounds_per_game"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with games played > 70 have rebounds per game > 6."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players violate the rule (games played: {', '.join(map(str, viol['games_played'].tolist()))}, rebounds per game: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All players with minutes per game greater than 32 have points per game greater than 16."""
    players = df[df["minutes_per_game"] > 32]
    condition = players["points_per_game"] > 16
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with minutes per game > 32 have points per game > 16."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players violate the rule (minutes per game: {', '.join(map(str, viol['minutes_per_game'].tolist()))}, points per game: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Centers with age greater than 29 have rebounds per game greater than 10."""
    centers = df[(df["position"] == "center") & (df["age"] > 29)]
    condition = centers["rebounds_per_game"] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers with age > 29 have rebounds per game > 10."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))}, rebounds per game: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a player is a forward, then their assists per game are less than 5."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["assists_per_game"] < 5
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have assists per game < 5."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (assists per game: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Every player with rebounds per game greater than 9 has points per game less than 22."""
    players = df[df["rebounds_per_game"] > 9]
    condition = players["points_per_game"] < 22
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with rebounds per game > 9 have points per game < 22."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players violate the rule (rebounds per game: {', '.join(map(str, viol['rebounds_per_game'].tolist()))}, points per game: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All players with age less than 24 have minutes per game less than 30."""
    players = df[df["age"] < 24]
    condition = players["minutes_per_game"] < 30
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with age < 24 have minutes per game < 30."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))}, minutes per game: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a player has points per game greater than 19, then their assists per game are greater than 2."""
    players = df[df["points_per_game"] > 19]
    condition = players["assists_per_game"] > 2
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with points per game > 19 have assists per game > 2."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players violate the rule (points per game: {', '.join(map(str, viol['points_per_game'].tolist()))}, assists per game: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Guards with games played greater than 65 have points per game greater than 15."""
    guards = df[(df["position"] == "guard") & (df["games_played"] > 65)]
    condition = guards["points_per_game"] > 15
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards with games played > 65 have points per game > 15."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (games played: {', '.join(map(str, viol['games_played'].tolist()))}, points per game: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All players with rebounds per game less than 5 have minutes per game less than 28."""
    players = df[df["rebounds_per_game"] < 5]
    condition = players["minutes_per_game"] < 28
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with rebounds per game < 5 have minutes per game < 28."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players violate the rule (rebounds per game: {', '.join(map(str, viol['rebounds_per_game'].tolist()))}, minutes per game: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a player is a center, then their points per game are less than 19."""
    centers = df[df["position"] == "center"]
    condition = centers["points_per_game"] < 19
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have points per game < 19."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (points per game: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Every player with assists per game greater than 6 has points per game greater than 18."""
    players = df[df["assists_per_game"] > 6]
    condition = players["points_per_game"] > 18
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with assists per game > 6 have points per game > 18."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players violate the rule (assists per game: {', '.join(map(str, viol['assists_per_game'].tolist()))}, points per game: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_8.csv")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10), (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()