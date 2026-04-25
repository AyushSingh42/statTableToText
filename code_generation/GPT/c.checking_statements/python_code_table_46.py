import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. For all forwards, minutes per game are at least 25.3."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["minutes_per_game"] >= 25.3
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have minutes per game >= 25.3."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all centers, assists per game are at least 5.7."""
    centers = df[df["position"] == "center"]
    condition = centers["assists_per_game"] >= 5.7
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have assists per game >= 5.7."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all guards, rebounds per game are at most 9.4."""
    guards = df[df["position"] == "guard"]
    condition = guards["rebounds_per_game"] <= 9.4
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have rebounds per game <= 9.4."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all players with minutes per game at least 33, points per game are at least 16.2."""
    filtered = df[df["minutes_per_game"] >= 33]
    condition = filtered["points_per_game"] >= 16.2
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} players with minutes >= 33 have points per game >= 16.2."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} players violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all players with rebounds per game at least 10, points per game are at most 16.5."""
    filtered = df[df["rebounds_per_game"] >= 10]
    condition = filtered["points_per_game"] <= 16.5
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} players with rebounds >= 10 have points per game <= 16.5."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} players violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all players with assists per game at least 7, points per game are at most 20.4."""
    filtered = df[df["assists_per_game"] >= 7]
    condition = filtered["points_per_game"] <= 20.4
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} players with assists >= 7 have points per game <= 20.4."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} players violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all players aged between 21 and 23 inclusive, minutes per game are at least 26.7."""
    filtered = df[(df["age"] >= 21) & (df["age"] <= 23)]
    condition = filtered["minutes_per_game"] >= 26.7
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} players aged 21-23 have minutes per game >= 26.7."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} players violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all players who have played at least 75 games, points per game are at least 14.6."""
    filtered = df[df["games_played"] >= 75]
    condition = filtered["points_per_game"] >= 14.6
    truth = condition.all()
    if truth:
        expl = f"All {len(filtered)} players with games played >= 75 have points per game >= 14.6."
    else:
        viol = filtered[~condition]
        expl = f"{len(viol)} players violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_46.csv")

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