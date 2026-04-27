import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all players whose position is center, rebounds per game are at least 3.5."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] >= 3.5
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds per game >= 3.5."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all players whose position is forward, assists per game are at least 1.6."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["assists_per_game"] >= 1.6
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have assists per game >= 1.6."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all players whose position is guard, points per game are at least 16.4."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] >= 16.4
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have points per game >= 16.4."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all players aged 30 years or older, minutes per game are at least 25.9."""
    older = df[df["age"] >= 30]
    condition = older["minutes_per_game"] >= 25.9
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} players aged 30+ have minutes per game >= 25.9."
    else:
        viol = older[~condition]
        expl = f"{len(viol)} players aged 30+ violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all players with minutes per game greater than 34, points per game are at least 11.9."""
    high_minutes = df[df["minutes_per_game"] > 34]
    condition = high_minutes["points_per_game"] >= 11.9
    truth = condition.all()
    if truth:
        expl = f"All {len(high_minutes)} players with minutes > 34 have points per game >= 11.9."
    else:
        viol = high_minutes[~condition]
        expl = f"{len(viol)} players with minutes > 34 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all players with points per game of at least 22, rebounds per game are at least 7.1."""
    high_points = df[df["points_per_game"] >= 22]
    condition = high_points["rebounds_per_game"] >= 7.1
    truth = condition.all()
    if truth:
        expl = f"All {len(high_points)} players with points >= 22 have rebounds per game >= 7.1."
    else:
        viol = high_points[~condition]
        expl = f"{len(viol)} players with points >= 22 violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all players with assists per game of at least 7, points per game are at least 13.2."""
    high_assists = df[df["assists_per_game"] >= 7]
    condition = high_assists["points_per_game"] >= 13.2
    truth = condition.all()
    if truth:
        expl = f"All {len(high_assists)} players with assists >= 7 have points per game >= 13.2."
    else:
        viol = high_assists[~condition]
        expl = f"{len(viol)} players with assists >= 7 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Most players have rebounds per game of at least 7."""
    total_players = len(df)
    condition = df["rebounds_per_game"] >= 7
    count_meeting = condition.sum()
    truth = count_meeting > total_players / 2
    if truth:
        expl = f"{count_meeting} out of {total_players} players have rebounds per game >= 7 (more than half)."
    else:
        expl = f"{count_meeting} out of {total_players} players have rebounds per game >= 7 (not more than half)."
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
        (8, stmt_8)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()