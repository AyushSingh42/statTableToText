import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all guards, points per game are between 12.1 and 24.7."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"].between(12.1, 24.7, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have points per game between 12.1 and 24.7."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All centers have rebounds per game between 4.5 and 11.2."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"].between(4.5, 11.2, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds per game between 4.5 and 11.2."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All forwards play at least 25.5 minutes per game."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["minutes_per_game"] >= 25.5
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards play at least 25.5 minutes per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Most players have rebounds per game at least 5."""
    condition = df["rebounds_per_game"] >= 5
    count = condition.sum()
    total = len(df)
    truth = count > total / 2
    expl = f"{count} out of {total} players have rebounds per game at least 5."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All players with minutes per game greater than 34 have points per game at least 12.5."""
    players = df[df["minutes_per_game"] > 34]
    condition = players["points_per_game"] >= 12.5
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with minutes > 34 have points >= 12.5."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players with minutes > 34 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All centers older than 33 have rebounds per game at least 6.1."""
    centers = df[(df["position"] == "center") & (df["age"] > 33)]
    condition = centers["rebounds_per_game"] >= 6.1
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers older than 33 have rebounds >= 6.1."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers older than 33 violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All players with rebounds per game at least 10 have minutes per game at least 30."""
    players = df[df["rebounds_per_game"] >= 10]
    condition = players["minutes_per_game"] >= 30
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with rebounds >= 10 have minutes >= 30."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players with rebounds >= 10 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All guards have assists per game no more than 7.3."""
    guards = df[df["position"] == "guard"]
    condition = guards["assists_per_game"] <= 7.3
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have assists per game <= 7.3."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_96.csv")

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