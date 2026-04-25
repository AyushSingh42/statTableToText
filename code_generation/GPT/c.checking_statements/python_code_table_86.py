import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All guards play at least 27.7 minutes per game."""
    guards = df[df["position"] == "guard"]
    condition = guards["minutes_per_game"] >= 27.7
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards play at least 27.7 minutes per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards play less than 27.7 minutes per game."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All forwards score at most 25.5 points per game."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["points_per_game"] <= 25.5
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards score at most 25.5 points per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards score more than 25.5 points per game."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All centers record at least 5.4 rebounds per game."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] >= 5.4
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers record at least 5.4 rebounds per game."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers record less than 5.4 rebounds per game."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players aged 20 to 24 score at least 14.9 points per game."""
    players_20_to_24 = df[(df["age"] >= 20) & (df["age"] <= 24)]
    condition = players_20_to_24["points_per_game"] >= 14.9
    truth = condition.all()
    if truth:
        expl = f"All {len(players_20_to_24)} players aged 20-24 score at least 14.9 points per game."
    else:
        viol = players_20_to_24[~condition]
        expl = f"{len(viol)} players aged 20-24 score less than 14.9 points per game."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All players aged 30 or older play at most 35.1 minutes per game."""
    players_30_or_older = df[df["age"] >= 30]
    condition = players_30_or_older["minutes_per_game"] <= 35.1
    truth = condition.all()
    if truth:
        expl = f"All {len(players_30_or_older)} players aged 30 or older play at most 35.1 minutes per game."
    else:
        viol = players_30_or_older[~condition]
        expl = f"{len(viol)} players aged 30 or older play more than 35.1 minutes per game."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most players have at least 4 assists per game."""
    condition = df["assists_per_game"] >= 4
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have at least 4 assists per game (more than half)."
    else:
        expl = f"{count} out of {total} players have at least 4 assists per game (not more than half)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a player rebounds at least 9 per game, then they score at least 14.3 points per game."""
    condition = (df["rebounds_per_game"] >= 9) & (df["points_per_game"] < 14.3)
    viol = df[condition]
    truth = len(viol) == 0
    if truth:
        expl = "No player who rebounds at least 9 per game scores less than 14.3 points per game."
    else:
        expl = f"{len(viol)} players rebound at least 9 per game but score less than 14.3 points per game."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All players who play more than 35 minutes per game score at least 12.0 points per game."""
    players_more_than_35 = df[df["minutes_per_game"] > 35]
    condition = players_more_than_35["points_per_game"] >= 12.0
    truth = condition.all()
    if truth:
        expl = f"All {len(players_more_than_35)} players who play more than 35 minutes per game score at least 12.0 points per game."
    else:
        viol = players_more_than_35[~condition]
        expl = f"{len(viol)} players who play more than 35 minutes per game score less than 12.0 points per game."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_86.csv")

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