import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All guards score at least 13.7 points per game and no more than 25.3 points per game."""
    guards = df[df["position"] == "guard"]
    condition = (guards["points_per_game"] >= 13.7) & (guards["points_per_game"] <= 25.3)
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards score between 13.7 and 25.3 points per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All centers have rebounds per game no greater than 10.0."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] <= 10.0
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds per game ≤ 10.0."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All forwards who are 20 years old score at least 16.1 points per game."""
    forwards_20 = df[(df["position"] == "forward") & (df["age"] == 20)]
    condition = forwards_20["points_per_game"] >= 16.1
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards_20)} forwards aged 20 score ≥ 16.1 points per game."
    else:
        viol = forwards_20[~condition]
        expl = f"{len(viol)} forwards aged 20 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players who average more than 34 minutes per game score at least 18.6 points per game."""
    high_minutes = df[df["minutes_per_game"] > 34]
    condition = high_minutes["points_per_game"] >= 18.6
    truth = condition.all()
    if truth:
        expl = f"All {len(high_minutes)} players averaging >34 minutes score ≥ 18.6 points per game."
    else:
        viol = high_minutes[~condition]
        expl = f"{len(viol)} players averaging >34 minutes violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All players with rebounds per game exceeding 10 have assists per game no greater than 5.4."""
    high_rebounds = df[df["rebounds_per_game"] > 10]
    condition = high_rebounds["assists_per_game"] <= 5.4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with rebounds >10 have assists ≤ 5.4."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} players with rebounds >10 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most players average more than 25 minutes per game."""
    total_players = len(df)
    high_minutes = df[df["minutes_per_game"] > 25]
    truth = len(high_minutes) > total_players / 2
    if truth:
        expl = f"{len(high_minutes)} out of {total_players} players average >25 minutes per game."
    else:
        expl = f"{len(high_minutes)} out of {total_players} players average >25 minutes per game (less than half)."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All players with assists per game exceeding 6 score no more than 22.4 points per game."""
    high_assists = df[df["assists_per_game"] > 6]
    condition = high_assists["points_per_game"] <= 22.4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_assists)} players with assists >6 score ≤ 22.4 points per game."
    else:
        viol = high_assists[~condition]
        expl = f"{len(viol)} players with assists >6 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All forwards average at least 26.4 minutes per game."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["minutes_per_game"] >= 26.4
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards average ≥ 26.4 minutes per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_16.csv")

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