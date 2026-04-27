import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All guards score at least 13.7 points per game and no more than 25.3 points per game."""
    guards = df[df["position"].str.lower() == "guard"]
    if guards.empty:
        return True, "No guards in the dataset; statement vacuously true."
    condition = guards["points_per_game"].between(13.7, 25.3, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have points per game between 13.7 and 25.3."
    else:
        viol = guards[~condition]
        viol_points = viol["points_per_game"].tolist()
        expl = f"{len(viol)} guard(s) violate the rule (points per game: {', '.join(map(str, viol_points))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All centers have rebounds per game no greater than 10.0."""
    centers = df[df["position"].str.lower() == "center"]
    if centers.empty:
        return True, "No centers in the dataset; statement vacuously true."
    condition = centers["rebounds_per_game"] <= 10.0
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds per game <= 10.0."
    else:
        viol = centers[~condition]
        viol_rebounds = viol["rebounds_per_game"].tolist()
        expl = f"{len(viol)} center(s) violate the rule (rebounds per game: {', '.join(map(str, viol_rebounds))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All forwards who are 20 years old score at least 16.1 points per game."""
    forwards_20 = df[(df["position"].str.lower() == "forward") & (df["age"] == 20)]
    if forwards_20.empty:
        return True, "No 20‑year‑old forwards in the dataset; statement vacuously true."
    condition = forwards_20["points_per_game"] >= 16.1
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards_20)} 20‑year‑old forwards score >= 16.1 points per game."
    else:
        viol = forwards_20[~condition]
        viol_points = viol["points_per_game"].tolist()
        expl = f"{len(viol)} 20‑year‑old forward(s) violate the rule (points per game: {', '.join(map(str, viol_points))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players who average more than 34 minutes per game score at least 18.6 points per game."""
    high_min = df[df["minutes_per_game"] > 34]
    if high_min.empty:
        return True, "No players average >34 minutes per game; statement vacuously true."
    condition = high_min["points_per_game"] >= 18.6
    truth = condition.all()
    if truth:
        expl = f"All {len(high_min)} players with >34 minutes per game score >= 18.6 points per game."
    else:
        viol = high_min[~condition]
        viol_points = viol["points_per_game"].tolist()
        expl = f"{len(viol)} player(s) with >34 minutes per game violate the rule (points per game: {', '.join(map(str, viol_points))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All players with rebounds per game exceeding 10 have assists per game no greater than 5.4."""
    high_reb = df[df["rebounds_per_game"] > 10]
    if high_reb.empty:
        return True, "No players have rebounds per game >10; statement vacuously true."
    condition = high_reb["assists_per_game"] <= 5.4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_reb)} players with >10 rebounds per game have assists per game <= 5.4."
    else:
        viol = high_reb[~condition]
        viol_assists = viol["assists_per_game"].tolist()
        expl = f"{len(viol)} player(s) with >10 rebounds per game violate the rule (assists per game: {', '.join(map(str, viol_assists))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most players average more than 25 minutes per game."""
    total = len(df)
    if total == 0:
        return True, "No players in the dataset; statement vacuously true."
    count_over_25 = df[df["minutes_per_game"] > 25].shape[0]
    proportion = count_over_25 / total
    truth = proportion > 0.5
    if truth:
        expl = f"{count_over_25} out of {total} players ({proportion*100:.1f}%) average >25 minutes per game."
    else:
        expl = f"Only {count_over_25} out of {total} players ({proportion*100:.1f}%) average >25 minutes per game."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All players with assists per game exceeding 6 score no more than 22.4 points per game."""
    high_assists = df[df["assists_per_game"] > 6]
    if high_assists.empty:
        return True, "No players have assists per game >6; statement vacuously true."
    condition = high_assists["points_per_game"] <= 22.4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_assists)} players with >6 assists per game score <= 22.4 points per game."
    else:
        viol = high_assists[~condition]
        viol_points = viol["points_per_game"].tolist()
        expl = f"{len(viol)} player(s) with >6 assists per game violate the rule (points per game: {', '.join(map(str, viol_points))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All forwards average at least 26.4 minutes per game."""
    forwards = df[df["position"].str.lower() == "forward"]
    if forwards.empty:
        return True, "No forwards in the dataset; statement vacuously true."
    condition = forwards["minutes_per_game"] >= 26.4
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards average >= 26.4 minutes per game."
    else:
        viol = forwards[~condition]
        viol_minutes = viol["minutes_per_game"].tolist()
        expl = f"{len(viol)} forward(s) violate the rule (minutes per game: {', '.join(map(str, viol_minutes))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_16.csv")

    # Convert numeric columns safely
    numeric_cols = ["age", "games_played", "minutes_per_game",
                    "points_per_game", "assists_per_game", "rebounds_per_game"]
    for col in numeric_cols:
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