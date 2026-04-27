import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players have points per game at least 14.1."""
    condition = df["points_per_game"] >= 14.1
    truth = condition.all()
    if truth:
        expl = f"All {len(df)} players have points per game >= 14.1."
    else:
        viol = df[~condition]
        expl = f"{len(viol)} players violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All centers have rebounds per game at least 3.8."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] >= 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds per game >= 3.8."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All forwards have points per game at most 19.9."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["points_per_game"] <= 19.9
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have points per game <= 19.9."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All guards have assists per game at least 4.7."""
    guards = df[df["position"] == "guard"]
    condition = guards["assists_per_game"] >= 4.7
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have assists per game >= 4.7."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All players aged 30 or older have minutes per game at least 24.0."""
    older_players = df[df["age"] >= 30]
    condition = older_players["minutes_per_game"] >= 24.0
    truth = condition.all()
    if truth:
        expl = f"All {len(older_players)} players aged 30+ have minutes per game >= 24.0."
    else:
        viol = older_players[~condition]
        expl = f"{len(viol)} players aged 30+ violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All players who average more than 30 minutes per game have points per game at least 15.5."""
    high_minutes = df[df["minutes_per_game"] > 30]
    condition = high_minutes["points_per_game"] >= 15.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_minutes)} players with >30 minutes/game have points per game >= 15.5."
    else:
        viol = high_minutes[~condition]
        expl = f"{len(viol)} players with >30 minutes/game violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All players with rebounds per game greater than 8 have points per game at least 17.3."""
    high_rebounds = df[df["rebounds_per_game"] > 8]
    condition = high_rebounds["points_per_game"] >= 17.3
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >8 rebounds/game have points per game >= 17.3."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} players with >8 rebounds/game violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All players younger than 25 have assists per game at least 4.7."""
    young_players = df[df["age"] < 25]
    condition = young_players["assists_per_game"] >= 4.7
    truth = condition.all()
    if truth:
        expl = f"All {len(young_players)} players under 25 have assists per game >= 4.7."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} players under 25 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All centers have points per game at most 24.0."""
    centers = df[df["position"] == "center"]
    condition = centers["points_per_game"] <= 24.0
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have points per game <= 24.0."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. All guards have minutes per game at least 25.3."""
    guards = df[df["position"] == "guard"]
    condition = guards["minutes_per_game"] >= 25.3
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have minutes per game >= 25.3."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_66.csv")

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
        (10, stmt_10)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()