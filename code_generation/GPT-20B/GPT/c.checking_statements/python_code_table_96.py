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
        viol_points = viol["points_per_game"].tolist()
        expl = f"{len(viol)} guard(s) violate the rule (points: {', '.join(map(str, viol_points))})."
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
        viol_reb = viol["rebounds_per_game"].tolist()
        expl = f"{len(viol)} center(s) violate the rule (rebounds: {', '.join(map(str, viol_reb))})."
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
        viol_min = viol["minutes_per_game"].tolist()
        expl = f"{len(viol)} forward(s) violate the rule (minutes: {', '.join(map(str, viol_min))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Most players have rebounds per game at least 5."""
    total = len(df)
    at_least_5 = df["rebounds_per_game"] >= 5
    count = at_least_5.sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players (>{total/2}) have rebounds per game at least 5."
    else:
        expl = f"Only {count} out of {total} players (≤{total/2}) have rebounds per game at least 5."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All players with minutes per game greater than 34 have points per game at least 12.5."""
    high_min = df[df["minutes_per_game"] > 34]
    condition = high_min["points_per_game"] >= 12.5
    truth = condition.all()
    if truth:
        expl = f"All {len(high_min)} players with >34 minutes per game have points per game at least 12.5."
    else:
        viol = high_min[~condition]
        viol_pts = viol["points_per_game"].tolist()
        expl = f"{len(viol)} player(s) with >34 minutes per game violate the rule (points: {', '.join(map(str, viol_pts))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All centers older than 33 have rebounds per game at least 6.1."""
    centers = df[df["position"] == "center"]
    older = centers[centers["age"] > 33]
    condition = older["rebounds_per_game"] >= 6.1
    truth = condition.all()
    if truth:
        expl = f"All {len(older)} centers older than 33 have rebounds per game at least 6.1."
    else:
        viol = older[~condition]
        viol_reb = viol["rebounds_per_game"].tolist()
        expl = f"{len(viol)} center(s) older than 33 violate the rule (rebounds: {', '.join(map(str, viol_reb))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All players with rebounds per game at least 10 have minutes per game at least 30."""
    high_reb = df[df["rebounds_per_game"] >= 10]
    condition = high_reb["minutes_per_game"] >= 30
    truth = condition.all()
    if truth:
        expl = f"All {len(high_reb)} players with rebounds per game ≥10 have minutes per game at least 30."
    else:
        viol = high_reb[~condition]
        viol_min = viol["minutes_per_game"].tolist()
        expl = f"{len(viol)} player(s) with rebounds ≥10 violate the rule (minutes: {', '.join(map(str, viol_min))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All guards have assists per game no more than 7.3."""
    guards = df[df["position"] == "guard"]
    condition = guards["assists_per_game"] <= 7.3
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have assists per game no more than 7.3."
    else:
        viol = guards[~condition]
        viol_assists = viol["assists_per_game"].tolist()
        expl = f"{len(viol)} guard(s) violate the rule (assists: {', '.join(map(str, viol_assists))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_96.csv")

    # Convert numeric columns where possible
    for col in df.columns:
        if col!= "position":
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