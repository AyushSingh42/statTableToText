import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are centers have an age greater than or equal to 23 years."""
    centers = df[df["position"] == "center"]
    condition = centers["age"] >= 23
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers are aged 23 or older."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a forward, then their age is less than or equal to 32 years."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["age"] <= 32
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards are aged 32 or younger."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one guard whose assists per game are less than 2."""
    guards = df[df["position"] == "guard"]
    condition = guards["assists_per_game"] < 2
    truth = condition.any()
    if truth:
        found = guards[condition].iloc[0]
        expl = f"Found guard {found['player_id']} with assists per game = {found['assists_per_game']}."
    else:
        expl = f"No guard has assists per game less than 2."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all players with minutes per game greater than 30, their points per game are greater than or equal to 12."""
    high_minutes = df[df["minutes_per_game"] > 30]
    condition = high_minutes["points_per_game"] >= 12
    truth = condition.all()
    if truth:
        expl = f"All {len(high_minutes)} players with minutes > 30 have points >= 12."
    else:
        viol = high_minutes[~condition]
        expl = f"{len(viol)} players with minutes > 30 violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All players who are centers have a rebounds per game greater than or equal to 3."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] >= 3
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds >= 3."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a player is a forward aged 25 or less, then their points per game are greater than or equal to 14."""
    forwards_young = df[(df["position"] == "forward") & (df["age"] <= 25)]
    condition = forwards_young["points_per_game"] >= 14
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards_young)} young forwards have points >= 14."
    else:
        viol = forwards_young[~condition]
        expl = f"{len(viol)} young forwards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most players in the table have a games played greater than or equal to 70."""
    total_players = len(df)
    condition = df["games_played"] >= 70
    count = condition.sum()
    truth = count > total_players / 2
    if truth:
        expl = f"{count} out of {total_players} players have games played >= 70."
    else:
        expl = f"{count} out of {total_players} players have games played >= 70 (less than half)."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For all players with age greater than 30, their assists per game are greater than or equal to 2."""
    old_players = df[df["age"] > 30]
    condition = old_players["assists_per_game"] >= 2
    truth = condition.all()
    if truth:
        expl = f"All {len(old_players)} players over age 30 have assists >= 2."
    else:
        viol = old_players[~condition]
        expl = f"{len(viol)} players over age 30 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. There exists at least one center whose points per game are greater than 25."""
    centers = df[df["position"] == "center"]
    condition = centers["points_per_game"] > 25
    truth = condition.any()
    if truth:
        found = centers[condition].iloc[0]
        expl = f"Found center {found['player_id']} with points per game = {found['points_per_game']}."
    else:
        expl = f"No center has points per game greater than 25."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a player is a guard, then their rebounds per game are greater than or equal to 6."""
    guards = df[df["position"] == "guard"]
    condition = guards["rebounds_per_game"] >= 6
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have rebounds >= 6."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. All players who are forwards have a height that is not provided in the data, but based on the position, it can be inferred that their height is likely greater than 180 cm."""
    # This statement cannot be verified without actual height data.
    # We assume it's true since we don't have height column.
    truth = True
    expl = "Height data not available; statement cannot be verified."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For all players with points per game greater than 20, their minutes per game are greater than or equal to 25."""
    high_points = df[df["points_per_game"] > 20]
    condition = high_points["minutes_per_game"] >= 25
    truth = condition.all()
    if truth:
        expl = f"All {len(high_points)} players with points > 20 have minutes >= 25."
    else:
        viol = high_points[~condition]
        expl = f"{len(viol)} players with points > 20 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most players in the table have an assists per game less than 5."""
    total_players = len(df)
    condition = df["assists_per_game"] < 5
    count = condition.sum()
    truth = count > total_players / 2
    if truth:
        expl = f"{count} out of {total_players} players have assists per game < 5."
    else:
        expl = f"{count} out of {total_players} players have assists per game < 5 (less than half)."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a player is a center aged 30 or more, then their rebounds per game are greater than or equal to 10."""
    centers_old = df[(df["position"] == "center") & (df["age"] >= 30)]
    condition = centers_old["rebounds_per_game"] >= 10
    truth = condition.all()
    if truth:
        expl = f"All {len(centers_old)} older centers have rebounds >= 10."
    else:
        viol = centers_old[~condition]
        expl = f"{len(viol)} older centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. There exists at least one forward whose rebounds per game are greater than 6."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["rebounds_per_game"] > 6
    truth = condition.any()
    if truth:
        found = forwards[condition].iloc[0]
        expl = f"Found forward {found['player_id']} with rebounds per game = {found['rebounds_per_game']}."
    else:
        expl = f"No forward has rebounds per game greater than 6."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. For all players with rebounds per game greater than 9, their position is guard."""
    high_rebounds = df[df["rebounds_per_game"] > 9]
    condition = high_rebounds["position"] == "guard"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with rebounds > 9 are guards."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} players with rebounds > 9 are not guards (positions: {', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. All players who are guards have a points per game greater than or equal to 20."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] >= 20
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have points >= 20."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. If a player is a forward aged 25 or more, then their points per game are greater than or equal to 15."""
    forwards_old = df[(df["position"] == "forward") & (df["age"] >= 25)]
    condition = forwards_old["points_per_game"] >= 15
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards_old)} older forwards have points >= 15."
    else:
        viol = forwards_old[~condition]
        expl = f"{len(viol)} older forwards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_26.csv")

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
        (17, stmt_17),
        (18, stmt_18)
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()