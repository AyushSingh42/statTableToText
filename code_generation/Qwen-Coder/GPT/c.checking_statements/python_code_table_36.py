import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All forwards play at least 27.4 minutes per game."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["minutes_per_game"] >= 27.4
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards play at least 27.4 minutes per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards play less than 27.4 minutes per game."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All centers have rebounds per game at most 8.5."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] <= 8.5
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds per game at most 8.5."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers have more than 8.5 rebounds per game."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All guards have rebounds per game of at least 5.5."""
    guards = df[df["position"] == "guard"]
    condition = guards["rebounds_per_game"] >= 5.5
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have rebounds per game of at least 5.5."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards have fewer than 5.5 rebounds per game."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players with rebounds per game of 9 or more score at most 22.9 points per game."""
    high_rebounders = df[df["rebounds_per_game"] >= 9]
    condition = high_rebounders["points_per_game"] <= 22.9
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounders)} players with 9+ rebounds per game score at most 22.9 points per game."
    else:
        viol = high_rebounders[~condition]
        expl = f"{len(viol)} players with 9+ rebounds per game score more than 22.9 points per game."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All guards aged 23 have points per game of at least 22.9."""
    guards_23 = df[(df["position"] == "guard") & (df["age"] == 23)]
    condition = guards_23["points_per_game"] >= 22.9
    truth = condition.all()
    if truth:
        expl = f"All {len(guards_23)} guards aged 23 have points per game of at least 22.9."
    else:
        viol = guards_23[~condition]
        expl = f"{len(viol)} guards aged 23 have fewer than 22.9 points per game."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. The highest points per game (24.3) is achieved by a guard."""
    max_points = df["points_per_game"].max()
    if max_points!= 24.3:
        return False, f"Highest points per game is {max_points}, not 24.3."
    top_player = df[df["points_per_game"] == 24.3]
    if top_player.empty or top_player.iloc[0]["position"]!= "guard":
        return False, f"Highest points per game ({max_points}) was not scored by a guard."
    return True, f"The highest points per game ({max_points}) was scored by a guard."

def stmt_7(df: pd.DataFrame):
    """7. All players older than 30 play at least 27.4 minutes per game."""
    old_players = df[df["age"] > 30]
    condition = old_players["minutes_per_game"] >= 27.4
    truth = condition.all()
    if truth:
        expl = f"All {len(old_players)} players older than 30 play at least 27.4 minutes per game."
    else:
        viol = old_players[~condition]
        expl = f"{len(viol)} players older than 30 play less than 27.4 minutes per game."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All players with assists per game of at least 6 score at most 22.9 points per game."""
    high_assisters = df[df["assists_per_game"] >= 6]
    condition = high_assisters["points_per_game"] <= 22.9
    truth = condition.all()
    if truth:
        expl = f"All {len(high_assisters)} players with 6+ assists per game score at most 22.9 points per game."
    else:
        viol = high_assisters[~condition]
        expl = f"{len(viol)} players with 6+ assists per game score more than 22.9 points per game."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_36.csv")

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