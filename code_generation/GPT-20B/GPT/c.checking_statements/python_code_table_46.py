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
        expl = f"All {len(forwards)} forwards meet the requirement."
    else:
        viol = forwards[~condition]
        viol_vals = ", ".join(map(str, viol["minutes_per_game"].tolist()))
        expl = f"{len(viol)} forwards violate the rule (minutes per game: {viol_vals})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. For all centers, assists per game are at least 5.7."""
    centers = df[df["position"] == "center"]
    condition = centers["assists_per_game"] >= 5.7
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers meet the requirement."
    else:
        viol = centers[~condition]
        viol_vals = ", ".join(map(str, viol["assists_per_game"].tolist()))
        expl = f"{len(viol)} centers violate the rule (assists per game: {viol_vals})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. For all guards, rebounds per game are at most 9.4."""
    guards = df[df["position"] == "guard"]
    condition = guards["rebounds_per_game"] <= 9.4
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards meet the requirement."
    else:
        viol = guards[~condition]
        viol_vals = ", ".join(map(str, viol["rebounds_per_game"].tolist()))
        expl = f"{len(viol)} guards violate the rule (rebounds per game: {viol_vals})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all players with minutes per game at least 33, points per game are at least 16.2."""
    subset = df[df["minutes_per_game"] >= 33]
    condition = subset["points_per_game"] >= 16.2
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with minutes >= 33 meet the requirement."
    else:
        viol = subset[~condition]
        viol_vals = ", ".join(map(str, viol["points_per_game"].tolist()))
        expl = f"{len(viol)} players violate the rule (points per game: {viol_vals})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For all players with rebounds per game at least 10, points per game are at most 16.5."""
    subset = df[df["rebounds_per_game"] >= 10]
    condition = subset["points_per_game"] <= 16.5
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with rebounds >= 10 meet the requirement."
    else:
        viol = subset[~condition]
        viol_vals = ", ".join(map(str, viol["points_per_game"].tolist()))
        expl = f"{len(viol)} players violate the rule (points per game: {viol_vals})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. For all players with assists per game at least 7, points per game are at most 20.4."""
    subset = df[df["assists_per_game"] >= 7]
    condition = subset["points_per_game"] <= 20.4
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with assists >= 7 meet the requirement."
    else:
        viol = subset[~condition]
        viol_vals = ", ".join(map(str, viol["points_per_game"].tolist()))
        expl = f"{len(viol)} players violate the rule (points per game: {viol_vals})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all players aged between 21 and 23 inclusive, minutes per game are at least 26.7."""
    subset = df[(df["age"] >= 21) & (df["age"] <= 23)]
    condition = subset["minutes_per_game"] >= 26.7
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players aged 21-23 meet the requirement."
    else:
        viol = subset[~condition]
        viol_vals = ", ".join(map(str, viol["minutes_per_game"].tolist()))
        expl = f"{len(viol)} players violate the rule (minutes per game: {viol_vals})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all players who have played at least 75 games, points per game are at least 14.6."""
    subset = df[df["games_played"] >= 75]
    condition = subset["points_per_game"] >= 14.6
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with games played >= 75 meet the requirement."
    else:
        viol = subset[~condition]
        viol_vals = ", ".join(map(str, viol["points_per_game"].tolist()))
        expl = f"{len(viol)} players violate the rule (points per game: {viol_vals})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_46.csv")

    # Convert numeric columns
    for col in df.columns:
        if col not in ["player_id", "position"]:
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