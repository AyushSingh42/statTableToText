import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are centers have an age between 20 and 33 years."""
    centers = df[df["position"] == "center"]
    condition = centers["age"].between(20, 33, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers are aged 20-33."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a forward, then their age is between 20 and 33 years."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["age"].between(20, 33, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards are aged 20-33."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All players who are guards have an age between 24 and 29 years."""
    guards = df[df["position"] == "guard"]
    condition = guards["age"].between(24, 29, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards are aged 24-29."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all players with minutes per game greater than 30, their points per game is greater than 13."""
    high_minutes = df[df["minutes_per_game"] > 30]
    condition = high_minutes["points_per_game"] > 13
    truth = condition.all()
    if truth:
        expl = f"All {len(high_minutes)} players with minutes > 30 have points > 13."
    else:
        viol = high_minutes[~condition]
        expl = f"{len(viol)} players with minutes > 30 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a player has games played greater than 70, then their assists per game is greater than 4."""
    high_games = df[df["games_played"] > 70]
    condition = high_games["assists_per_game"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_games)} players with games > 70 have assists > 4."
    else:
        viol = high_games[~condition]
        expl = f"{len(viol)} players with games > 70 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All players who have rebounds per game greater than 10 are forwards."""
    high_rebounds = df[df["rebounds_per_game"] > 10]
    condition = high_rebounds["position"] == "forward"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with rebounds > 10 are forwards."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} players with rebounds > 10 are not forwards (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. For all players with age greater than 25, their points per game is greater than 17."""
    old_players = df[df["age"] > 25]
    condition = old_players["points_per_game"] > 17
    truth = condition.all()
    if truth:
        expl = f"All {len(old_players)} players with age > 25 have points > 17."
    else:
        viol = old_players[~condition]
        expl = f"{len(viol)} players with age > 25 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a player is a center, then their rebounds per game is greater than 3."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] > 3
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds > 3."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All players who have assists per game greater than 5 are guards or forwards."""
    high_assists = df[df["assists_per_game"] > 5]
    condition = (high_assists["position"] == "guard") | (high_assists["position"] == "forward")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_assists)} players with assists > 5 are guards or forwards."
    else:
        viol = high_assists[~condition]
        expl = f"{len(viol)} players with assists > 5 are neither guards nor forwards (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. For all players with minutes per game greater than 35, their rebounds per game is greater than 4."""
    high_minutes = df[df["minutes_per_game"] > 35]
    condition = high_minutes["rebounds_per_game"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(high_minutes)} players with minutes > 35 have rebounds > 4."
    else:
        viol = high_minutes[~condition]
        expl = f"{len(viol)} players with minutes > 35 violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Most players in the table have a points per game greater than 15."""
    total = len(df)
    high_points = len(df[df["points_per_game"] > 15])
    truth = high_points > total / 2
    expl = f"{high_points} out of {total} players have points > 15."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a player has age less than 25, then their rebounds per game is less than 8."""
    young_players = df[df["age"] < 25]
    condition = young_players["rebounds_per_game"] < 8
    truth = condition.all()
    if truth:
        expl = f"All {len(young_players)} players with age < 25 have rebounds < 8."
    else:
        viol = young_players[~condition]
        expl = f"{len(viol)} players with age < 25 violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All players who have games played greater than 60 have a minutes per game greater than 24."""
    high_games = df[df["games_played"] > 60]
    condition = high_games["minutes_per_game"] > 24
    truth = condition.all()
    if truth:
        expl = f"All {len(high_games)} players with games > 60 have minutes > 24."
    else:
        viol = high_games[~condition]
        expl = f"{len(viol)} players with games > 60 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. For all players with points per game greater than 20, their age is greater than 20."""
    high_points = df[df["points_per_game"] > 20]
    condition = high_points["age"] > 20
    truth = condition.all()
    if truth:
        expl = f"All {len(high_points)} players with points > 20 have age > 20."
    else:
        viol = high_points[~condition]
        expl = f"{len(viol)} players with points > 20 violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a player is a forward, then their points per game is greater than 14."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["points_per_game"] > 14
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have points > 14."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All players who have rebounds per game greater than 6 are forwards or centers."""
    high_rebounds = df[df["rebounds_per_game"] > 6]
    condition = (high_rebounds["position"] == "forward") | (high_rebounds["position"] == "center")
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with rebounds > 6 are forwards or centers."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} players with rebounds > 6 are neither forwards nor centers (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. For all players with assists per game greater than 4, their minutes per game is greater than 25."""
    high_assists = df[df["assists_per_game"] > 4]
    condition = high_assists["minutes_per_game"] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(high_assists)} players with assists > 4 have minutes > 25."
    else:
        viol = high_assists[~condition]
        expl = f"{len(viol)} players with assists > 4 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_6.csv")

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
        (8, stmt_8),
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()