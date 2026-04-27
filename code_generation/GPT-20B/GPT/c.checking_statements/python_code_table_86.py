import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All guards play at least 27.7 minutes per game."""
    guards = df[df["position"].str.lower() == "guard"]
    condition = guards["minutes_per_game"] >= 27.7
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards play at least 27.7 minutes per game."
    else:
        viol = guards[~condition]
        viol_ids = viol["player_id"].tolist()
        viol_minutes = viol["minutes_per_game"].tolist()
        expl = f"{len(viol)} guard(s) violate the rule (IDs: {', '.join(viol_ids)}; minutes: {', '.join(map(str, viol_minutes))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. All forwards score at most 25.5 points per game."""
    forwards = df[df["position"].str.lower() == "forward"]
    condition = forwards["points_per_game"] <= 25.5
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards score at most 25.5 points per game."
    else:
        viol = forwards[~condition]
        viol_ids = viol["player_id"].tolist()
        viol_points = viol["points_per_game"].tolist()
        expl = f"{len(viol)} forward(s) violate the rule (IDs: {', '.join(viol_ids)}; points: {', '.join(map(str, viol_points))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All centers record at least 5.4 rebounds per game."""
    centers = df[df["position"].str.lower() == "center"]
    condition = centers["rebounds_per_game"] >= 5.4
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers record at least 5.4 rebounds per game."
    else:
        viol = centers[~condition]
        viol_ids = viol["player_id"].tolist()
        viol_rebounds = viol["rebounds_per_game"].tolist()
        expl = f"{len(viol)} center(s) violate the rule (IDs: {', '.join(viol_ids)}; rebounds: {', '.join(map(str, viol_rebounds))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. All players aged 20 to 24 score at least 14.9 points per game."""
    age_mask = df["age"].between(20, 24, inclusive="both")
    subset = df[age_mask]
    condition = subset["points_per_game"] >= 14.9
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players aged 20-24 score at least 14.9 points per game."
    else:
        viol = subset[~condition]
        viol_ids = viol["player_id"].tolist()
        viol_points = viol["points_per_game"].tolist()
        expl = f"{len(viol)} player(s) aged 20-24 violate the rule (IDs: {', '.join(viol_ids)}; points: {', '.join(map(str, viol_points))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All players aged 30 or older play at most 35.1 minutes per game."""
    age_mask = df["age"] >= 30
    subset = df[age_mask]
    condition = subset["minutes_per_game"] <= 35.1
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players aged 30+ play at most 35.1 minutes per game."
    else:
        viol = subset[~condition]
        viol_ids = viol["player_id"].tolist()
        viol_minutes = viol["minutes_per_game"].tolist()
        expl = f"{len(viol)} player(s) aged 30+ violate the rule (IDs: {', '.join(viol_ids)}; minutes: {', '.join(map(str, viol_minutes))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Most players have at least 4 assists per game."""
    condition = df["assists_per_game"] >= 4
    count = condition.sum()
    total = len(df)
    proportion = count / total
    truth = proportion > 0.5
    if truth:
        expl = f"{proportion*100:.1f}% ({count}/{total}) of players have at least 4 assists per game."
    else:
        expl = f"Only {proportion*100:.1f}% ({count}/{total}) of players have at least 4 assists per game."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a player rebounds at least 9 per game, then they score at least 14.3 points per game."""
    mask = df["rebounds_per_game"] >= 9
    subset = df[mask]
    condition = subset["points_per_game"] >= 14.3
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players who rebound at least 9 per game score at least 14.3 points per game."
    else:
        viol = subset[~condition]
        viol_ids = viol["player_id"].tolist()
        viol_points = viol["points_per_game"].tolist()
        expl = f"{len(viol)} player(s) who rebound at least 9 per game violate the rule (IDs: {', '.join(viol_ids)}; points: {', '.join(map(str, viol_points))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All players who play more than 35 minutes per game score at least 12.0 points per game."""
    mask = df["minutes_per_game"] > 35
    subset = df[mask]
    condition = subset["points_per_game"] >= 12.0
    truth = condition.all()
    if truth:
        expl = f"All {len(subset)} players who play more than 35 minutes per game score at least 12.0 points per game."
    else:
        viol = subset[~condition]
        viol_ids = viol["player_id"].tolist()
        viol_points = viol["points_per_game"].tolist()
        expl = f"{len(viol)} player(s) who play more than 35 minutes per game violate the rule (IDs: {', '.join(viol_ids)}; points: {', '.join(map(str, viol_points))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_86.csv")

    # Convert numeric columns safely
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