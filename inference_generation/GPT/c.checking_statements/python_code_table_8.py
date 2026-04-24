import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def _prepare_df(df: pd.DataFrame) -> pd.DataFrame:
    # Convert numeric columns that may be stored as strings
    num_cols = ["age", "games_played", "minutes_per_game",
                "points_per_game", "assists_per_game", "rebounds_per_game"]
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    # Standardise position strings
    if "position" in df.columns:
        df["position"] = df["position"].astype(str).str.lower()
    return df

def stmt_1(df: pd.DataFrame):
    """1. For all guards, assists per game are at least 5.0."""
    guards = df[df["position"] == "guard"]
    condition = guards["assists_per_game"] >= 5.0
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have assists_per_game ≥ 5.0."
    else:
        viol = guards[~condition]
        expl = (f"{len(viol)} guard(s) violate the rule: "
                f"assists_per_game values = {', '.join(map(str, viol['assists_per_game'].tolist()))}.")
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All centers have rebounds per game of at least 9.9."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] >= 9.9
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds_per_game ≥ 9.9."
    else:
        viol = centers[~condition]
        expl = (f"{len(viol)} center(s) violate the rule: "
                f"rebounds_per_game values = {', '.join(map(str, viol['rebounds_per_game'].tolist()))}.")
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All forwards have points per game of at least 15.6."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["points_per_game"] >= 15.6
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have points_per_game ≥ 15.6."
    else:
        viol = forwards[~condition]
        expl = (f"{len(viol)} forward(s) violate the rule: "
                f"points_per_game values = {', '.join(map(str, viol['points_per_game'].tolist()))}.")
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all players who played at least 74 games, points per game exceed 18."""
    subset = df[df["games_played"] >= 74]
    condition = subset["points_per_game"] > 18
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players with ≥74 games have points_per_game > 18."
    else:
        viol = subset[~condition]
        expl = (f"{len(viol)} player(s) violate the rule: "
                f"points_per_game values = {', '.join(map(str, viol['points_per_game'].tolist()))}.")
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most players have points per game greater than 15."""
    total = len(df)
    count = (df["points_per_game"] > 15).sum()
    truth = count > total / 2
    expl = f"{count} out of {total} players ({count/total:.1%}) have points_per_game > 15."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All centers have assists per game below 2.5."""
    centers = df[df["position"] == "center"]
    condition = centers["assists_per_game"] < 2.5
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have assists_per_game < 2.5."
    else:
        viol = centers[~condition]
        expl = (f"{len(viol)} center(s) violate the rule: "
                f"assists_per_game values = {', '.join(map(str, viol['assists_per_game'].tolist()))}.")
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All forwards have rebounds per game at least 6.8."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["rebounds_per_game"] >= 6.8
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have rebounds_per_game ≥ 6.8."
    else:
        viol = forwards[~condition]
        expl = (f"{len(viol)} forward(s) violate the rule: "
                f"rebounds_per_game values = {', '.join(map(str, viol['rebounds_per_game'].tolist()))}.")
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a player is younger than 25, their points per game do not exceed 18.7."""
    young = df[df["age"] < 25]
    condition = young["points_per_game"] <= 18.7
    truth = condition.all()
    if truth:
        expl = f"All {len(young)} players younger than 25 have points_per_game ≤ 18.7."
    else:
        viol = young[~condition]
        expl = (f"{len(viol)} young player(s) violate the rule: "
                f"points_per_game values = {', '.join(map(str, viol['points_per_game'].tolist()))}.")
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. For all players with minutes per game greater than 33, points per game exceed 20."""
    high_min = df[df["minutes_per_game"] > 33]
    condition = high_min["points_per_game"] > 20
    truth = condition.all()
    if truth:
        expl = f"All {len(high_min)} players with minutes_per_game > 33 have points_per_game > 20."
    else:
        viol = high_min[~condition]
        expl = (f"{len(viol)} player(s) violate the rule: "
                f"points_per_game values = {', '.join(map(str, viol['points_per_game'].tolist()))}.")
    return truth, expl

def main():
    df = pd.read_csv("tables/table_8.csv")
    df = _prepare_df(df)

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
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()