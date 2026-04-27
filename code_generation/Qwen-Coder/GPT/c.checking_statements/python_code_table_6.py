import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All centers have rebounds per game at least 3.8."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] >= 3.8
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds per game >= 3.8."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All guards have assists per game at least 5.2."""
    guards = df[df["position"] == "guard"]
    condition = guards["assists_per_game"] >= 5.2
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have assists per game >= 5.2."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All forwards play at most 35.6 minutes per game."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["minutes_per_game"] <= 35.6
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards play <= 35.6 minutes per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players aged 22 or younger play at least 24.3 minutes per game."""
    young_players = df[df["age"] <= 22]
    condition = young_players["minutes_per_game"] >= 24.3
    truth = condition.all()
    if truth:
        expl = f"All {len(young_players)} players aged 22 or younger play >= 24.3 minutes per game."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} young players violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All forwards have rebounds per game at least 3.4."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["rebounds_per_game"] >= 3.4
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have rebounds per game >= 3.4."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a player is a guard, then they score at most 21.3 points per game."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] <= 21.3
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards score <= 21.3 points per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a player is a center, then they play at least 24.8 minutes per game."""
    centers = df[df["position"] == "center"]
    condition = centers["minutes_per_game"] >= 24.8
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers play >= 24.8 minutes per game."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists a forward with rebounds per game exceeding 11."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["rebounds_per_game"] > 11
    truth = condition.any()
    if truth:
        found = forwards[condition]
        expl = f"There is at least one forward with rebounds per game > 11 ({found.iloc[0]['rebounds_per_game']} for player ID {found.iloc[0]['player_id']})."
    else:
        expl = "No forward has rebounds per game > 11."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Most players score more than 14 points per game."""
    condition = df["points_per_game"] > 14
    count_above = condition.sum()
    total = len(df)
    truth = count_above > total / 2
    if truth:
        expl = f"More than half of players ({count_above}/{total}) score > 14 points per game."
    else:
        expl = f"Less than or equal to half of players ({count_above}/{total}) score > 14 points per game."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_6.csv")

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
        (9, stmt_9)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()