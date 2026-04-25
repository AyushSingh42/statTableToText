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
    older_players = df[df["age"] > 30]
    condition = older_players["minutes_per_game"] <= 34.9
    truth = condition.all()
    if truth:
        expl = f"All {len(older_players)} players older than 30 have minutes per game <= 34.9."
    else:
        viol = older_players[~condition]
        expl = f"{len(viol)} players older than 30 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most players have points per game greater than 14."""
    condition = df["points_per_game"] > 14
    count_above = condition.sum()
    total = len(df)
    truth = count_above > total / 2
    if truth:
        expl = f"{count_above} out of {total} players have points per game > 14 (more than half)."
    else:
        expl = f"{count_above} out of {total} players have points per game > 14 (not more than half)."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Any player with rebounds per game of at least 10 also averages at least 22 points per game."""
    high_rebounders = df[df["rebounds_per_game"] >= 10]
    condition = high_rebounders["points_per_game"] >= 22
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounders)} players with rebounds >= 10 also have points >= 22."
    else:
        viol = high_rebounders[~condition]
        expl = f"{len(viol)} players with rebounds >= 10 do not have points >= 22 (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All players aged 25 or younger average at least 27.2 minutes per game."""
    young_players = df[df["age"] <= 25]
    condition = young_players["minutes_per_game"] >= 27.2
    truth = condition.all()
    if truth:
        expl = f"All {len(young_players)} players aged 25 or younger have minutes per game >= 27.2."
    else:
        viol = young_players[~condition]
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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()