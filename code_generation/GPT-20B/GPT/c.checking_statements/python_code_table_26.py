import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all centers, points per game are at least 12.1."""
    centers = df[df["position"] == "center"]
    condition = centers["points_per_game"] >= 12.1
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have points per game >= 12.1."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all guards, rebounds per game are at least 6.6."""
    guards = df[df["position"] == "guard"]
    condition = guards["rebounds_per_game"] >= 6.6
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have rebounds per game >= 6.6."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All forwards have assists per game no more than 4.4."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["assists_per_game"] <= 4.4
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have assists per game <= 4.4."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players older than 30 have minutes per game no more than 34.9."""
    older = df[df["age"] > 30]
    condition = older["minutes_per_game"] <= 34.9
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} players older than 30 have minutes per game <= 34.9."
    else:
        viol = older[~condition]
        expl = f"{len(viol)} players older than 30 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most players have points per game greater than 14."""
    proportion = (df["points_per_game"] > 14).mean()
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% of players have points per game > 14."
    else:
        expl = f"{(1-proportion)*100:.1f}% of players have points per game <= 14."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Any player with rebounds per game of at least 10 also averages at least 22 points per game."""
    high_reb = df[df["rebounds_per_game"] >= 10]
    condition = high_reb["points_per_game"] >= 22
    truth = condition.all()
    if truth:
        expl = f"All {len(high_reb)} players with rebounds >= 10 have points per game >= 22."
    else:
        viol = high_reb[~condition]
        expl = f"{len(viol)} players with rebounds >= 10 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All players aged 25 or younger average at least 27.2 minutes per game."""
    young = df[df["age"] <= 25]
    condition = young["minutes_per_game"] >= 27.2
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} players aged 25 or younger have minutes per game >= 27.2."
    else:
        viol = young[~condition]
        expl = f"{len(viol)} players aged 25 or younger violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All guards average at least 20 points per game."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] >= 20
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have points per game >= 20."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_26.csv")

    # Convert numeric columns
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()