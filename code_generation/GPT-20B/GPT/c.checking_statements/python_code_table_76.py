import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All centers have at least 4.6 rebounds per game."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] >= 4.6
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have at least 4.6 rebounds per game."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} center(s) violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All guards play at least 24.3 minutes per game."""
    guards = df[df["position"] == "guard"]
    condition = guards["minutes_per_game"] >= 24.3
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards play at least 24.3 minutes per game."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guard(s) violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All forwards score at most 21.1 points per game."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["points_per_game"] <= 21.1
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards score at most 21.1 points per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forward(s) violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Most players average more than 25 minutes per game."""
    total = len(df)
    count = (df["minutes_per_game"] > 25).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} of {total} players (>{total/2}) average more than 25 minutes per game."
    else:
        expl = f"{count} of {total} players average more than 25 minutes per game, which is not a majority."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most players score more than 12 points per game."""
    total = len(df)
    count = (df["points_per_game"] > 12).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} of {total} players (>{total/2}) score more than 12 points per game."
    else:
        expl = f"{count} of {total} players score more than 12 points per game, which is not a majority."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a guard scores at least 24 points per game, then they have at least 7.5 rebounds per game."""
    guards = df[df["position"] == "guard"]
    condition = (guards["points_per_game"] < 24) | (guards["rebounds_per_game"] >= 7.5)
    truth = condition.all()
    if truth:
        expl = "All guards who score at least 24 points also have at least 7.5 rebounds."
    else:
        viol = guards[(guards["points_per_game"] >= 24) & (guards["rebounds_per_game"] < 7.5)]
        expl = f"{len(viol)} guard(s) score >=24 points but have <7.5 rebounds (points: {', '.join(map(str, viol['points_per_game'].tolist()))}, rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. There exists at least one guard who averages at least 9.6 rebounds per game."""
    guards = df[df["position"] == "guard"]
    exists = (guards["rebounds_per_game"] >= 9.6).any()
    truth = exists
    if truth:
        first = guards[guards["rebounds_per_game"] >= 9.6].iloc[0]
        expl = f"Guard {first['player_id']} averages {first['rebounds_per_game']} rebounds per game."
    else:
        expl = "No guard averages at least 9.6 rebounds per game."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one center with assists per game greater than 6."""
    centers = df[df["position"] == "center"]
    exists = (centers["assists_per_game"] > 6).any()
    truth = exists
    if truth:
        first = centers[centers["assists_per_game"] > 6].iloc[0]
        expl = f"Center {first['player_id']} has {first['assists_per_game']} assists per game."
    else:
        expl = "No center has assists per game greater than 6."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_76.csv")

    # Convert numeric columns safely
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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()