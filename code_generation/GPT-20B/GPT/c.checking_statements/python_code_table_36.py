import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All forwards play at least 27.4 minutes per game."""
    forwards = df[df["position"] == "forward"]
    if forwards.empty:
        return True, "No forwards in the data."
    condition = forwards["minutes_per_game"] >= 27.4
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards play at least 27.4 minutes per game."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forward(s) violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All centers have rebounds per game at most 8.5."""
    centers = df[df["position"] == "center"]
    if centers.empty:
        return True, "No centers in the data."
    condition = centers["rebounds_per_game"] <= 8.5
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds per game at most 8.5."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} center(s) violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All guards have rebounds per game of at least 5.5."""
    guards = df[df["position"] == "guard"]
    if guards.empty:
        return True, "No guards in the data."
    condition = guards["rebounds_per_game"] >= 5.5
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have rebounds per game of at least 5.5."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guard(s) violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players with rebounds per game of 9 or more score at most 22.9 points per game."""
    high_reb = df[df["rebounds_per_game"] >= 9]
    if high_reb.empty:
        return True, "No players with rebounds per game >= 9."
    condition = high_reb["points_per_game"] <= 22.9
    truth = condition.all()
    if truth:
        expl = f"All {len(high_reb)} players with rebounds >= 9 score at most 22.9 points per game."
    else:
        viol = high_reb[~condition]
        expl = f"{len(viol)} player(s) violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All guards aged 23 have points per game of at least 22.9."""
    guards_23 = df[(df["position"] == "guard") & (df["age"] == 23)]
    if guards_23.empty:
        return True, "No guards aged 23 in the data."
    condition = guards_23["points_per_game"] >= 22.9
    truth = condition.all()
    if truth:
        expl = f"All {len(guards_23)} guards aged 23 have points per game >= 22.9."
    else:
        viol = guards_23[~condition]
        expl = f"{len(viol)} guard(s) aged 23 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. The highest points per game (24.3) is achieved by a guard."""
    if df.empty:
        return True, "Dataframe is empty."
    max_ppg = df["points_per_game"].max()
    if max_ppg!= 24.3:
        return False, f"Maximum points per game is {max_ppg}, not 24.3."
    max_rows = df[df["points_per_game"] == 24.3]
    if all(max_rows["position"] == "guard"):
        return True, f"All players with 24.3 points per game are guards."
    else:
        viol = max_rows[~(max_rows["position"] == "guard")]
        return False, f"Players with 24.3 points per game include non-guards: {', '.join(viol['player_id'].tolist())}."

def stmt_7(df: pd.DataFrame):
    """7. All players older than 30 play at least 27.4 minutes per game."""
    older = df[df["age"] > 30]
    if older.empty:
        return True, "No players older than 30 in the data."
    condition = older["minutes_per_game"] >= 27.4
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} players older than 30 play at least 27.4 minutes per game."
    else:
        viol = older[~condition]
        expl = f"{len(viol)} player(s) older than 30 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All players with assists per game of at least 6 score at most 22.9 points per game."""
    high_assists = df[df["assists_per_game"] >= 6]
    if high_assists.empty:
        return True, "No players with assists per game >= 6."
    condition = high_assists["points_per_game"] <= 22.9
    truth = condition.all()
    if truth:
        expl = f"All {len(high_assists)} players with assists >= 6 score at most 22.9 points per game."
    else:
        viol = high_assists[~condition]
        expl = f"{len(viol)} player(s) violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_36.csv")

    # Convert numeric columns safely
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')

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