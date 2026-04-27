import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All players who are guards have an average of less than 25 points per game."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] < 25
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards have points per game < 25."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guard(s) violate the rule (points per game: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a player is a forward, then their age is between 26 and 34 years."""
    forwards = df[df["position"] == "forward"]
    condition = forwards["age"].between(26, 34, inclusive="both")
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards have age between 26 and 34."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forward(s) violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All players who are centers have an average of more than 4 rebounds per game."""
    centers = df[df["position"] == "center"]
    condition = centers["rebounds_per_game"] > 4
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers have rebounds per game > 4."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} center(s) violate the rule (rebounds per game: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. There exists at least one player who is a guard and has an average of more than 20 points per game."""
    guards = df[df["position"] == "guard"]
    condition = guards["points_per_game"] > 20
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"{count} guard(s) satisfy the condition (points per game > 20)."
    else:
        expl = "No guard satisfies the condition."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. If a player is a forward aged over 30, then their average minutes per game is more than 33."""
    forwards_over30 = df[(df["position"] == "forward") & (df["age"] > 30)]
    condition = forwards_over30["minutes_per_game"] > 33
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards_over30)} forwards aged >30 have minutes per game > 33."
    else:
        viol = forwards_over30[~condition]
        expl = f"{len(viol)} forward(s) aged >30 violate the rule (minutes per game: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. All players who have an average of more than 6 assists per game are forwards."""
    high_assists = df[df["assists_per_game"] > 6]
    condition = high_assists["position"] == "forward"
    truth = condition.all()
    if truth:
        expl = f"All {len(high_assists)} players with >6 assists are forwards."
    else:
        viol = high_assists[~condition]
        expl = f"{len(viol)} player(s) with >6 assists are not forwards (positions: {', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Most players have an average of more than 5 rebounds per game."""
    total = len(df)
    count = (df["rebounds_per_game"] > 5).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} players have >5 rebounds per game."
    else:
        expl = f"Only {count} out of {total} players have >5 rebounds per game."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. If a player is a center aged below 30, then their average points per game is more than 15."""
    centers_under30 = df[(df["position"] == "center") & (df["age"] < 30)]
    condition = centers_under30["points_per_game"] > 15
    truth = condition.all()
    if truth:
        expl = f"All {len(centers_under30)} centers aged <30 have points per game > 15."
    else:
        viol = centers_under30[~condition]
        expl = f"{len(viol)} center(s) aged <30 violate the rule (points per game: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. All players who have an average of more than 8 rebounds per game are forwards or centers."""
    high_rebounds = df[df["rebounds_per_game"] > 8]
    condition = high_rebounds["position"].isin(["forward", "center"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >8 rebounds are forwards or centers."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} player(s) with >8 rebounds are not forwards or centers (positions: {', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. There exists at least one player who is a guard and has an average of less than 30 minutes per game."""
    guards = df[df["position"] == "guard"]
    condition = guards["minutes_per_game"] < 30
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"{count} guard(s) satisfy the condition (minutes per game < 30)."
    else:
        expl = "No guard satisfies the condition."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. If a player is a forward aged below 30, then their average points per game is more than 12."""
    forwards_under30 = df[(df["position"] == "forward") & (df["age"] < 30)]
    condition = forwards_under30["points_per_game"] > 12
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards_under30)} forwards aged <30 have points per game > 12."
    else:
        viol = forwards_under30[~condition]
        expl = f"{len(viol)} forward(s) aged <30 violate the rule (points per game: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All players who have an average of more than 7 assists per game are forwards aged over 30."""
    high_assists = df[df["assists_per_game"] > 7]
    condition = (high_assists["position"] == "forward") & (high_assists["age"] > 30)
    truth = condition.all()
    if truth:
        expl = f"All {len(high_assists)} players with >7 assists are forwards aged >30."
    else:
        viol = high_assists[~condition]
        expl = f"{len(viol)} player(s) with >7 assists are not forwards aged >30 (positions: {', '.join(viol['position'].tolist())}, ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. Most players who are guards have an average of less than 11 points per game."""
    guards = df[df["position"] == "guard"]
    total = len(guards)
    if total == 0:
        return True, "No guards in dataset, statement considered True."
    count = (guards["points_per_game"] < 11).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} guards have points per game < 11."
    else:
        expl = f"Only {count} out of {total} guards have points per game < 11."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. If a player is a center aged over 25, then their average rebounds per game is more than 6."""
    centers_over25 = df[(df["position"] == "center") & (df["age"] > 25)]
    condition = centers_over25["rebounds_per_game"] > 6
    truth = condition.all()
    if truth:
        expl = f"All {len(centers_over25)} centers aged >25 have rebounds per game > 6."
    else:
        viol = centers_over25[~condition]
        expl = f"{len(viol)} center(s) aged >25 violate the rule (rebounds per game: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. All players who have an average of more than 9 rebounds per game are forwards or guards."""
    high_rebounds = df[df["rebounds_per_game"] > 9]
    condition = high_rebounds["position"].isin(["forward", "guard"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >9 rebounds are forwards or guards."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} player(s) with >9 rebounds are not forwards or guards (positions: {', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. There exists at least one player who is a center and has an average of more than 5 assists per game."""
    centers = df[df["position"] == "center"]
    condition = centers["assists_per_game"] > 5
    truth = condition.any()
    if truth:
        count = condition.sum()
        expl = f"{count} center(s) satisfy the condition (assists per game > 5)."
    else:
        expl = "No center satisfies the condition."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. If a player is a forward aged over 25, then their average minutes per game is more than 30."""
    forwards_over25 = df[(df["position"] == "forward") & (df["age"] > 25)]
    condition = forwards_over25["minutes_per_game"] > 30
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards_over25)} forwards aged >25 have minutes per game > 30."
    else:
        viol = forwards_over25[~condition]
        expl = f"{len(viol)} forward(s) aged >25 violate the rule (minutes per game: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. All players who have an average of more than 8 points per game are forwards or guards."""
    high_points = df[df["points_per_game"] > 8]
    condition = high_points["position"].isin(["forward", "guard"])
    truth = condition.all()
    if truth:
        expl = f"All {len(high_points)} players with >8 points are forwards or guards."
    else:
        viol = high_points[~condition]
        expl = f"{len(viol)} player(s) with >8 points are not forwards or guards (positions: {', '.join(viol['position'].tolist())})."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. Most players who are forwards have an average of more than 5 assists per game."""
    forwards = df[df["position"] == "forward"]
    total = len(forwards)
    if total == 0:
        return True, "No forwards in dataset, statement considered True."
    count = (forwards["assists_per_game"] > 5).sum()
    truth = count > total / 2
    if truth:
        expl = f"{count} out of {total} forwards have assists per game > 5."
    else:
        expl = f"Only {count} out of {total} forwards have assists per game > 5."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. If a player is a guard aged below 30, then their average points per game is more than 20."""
    guards_under30 = df[(df["position"] == "guard") & (df["age"] < 30)]
    condition = guards_under30["points_per_game"] > 20
    truth = condition.all()
    if truth:
        expl = f"All {len(guards_under30)} guards aged <30 have points per game > 20."
    else:
        viol = guards_under30[~condition]
        expl = f"{len(viol)} guard(s) aged <30 violate the rule (points per game: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. All players who have an average of more than 7 rebounds per game are forwards or centers aged over 25."""
    high_rebounds = df[df["rebounds_per_game"] > 7]
    condition = high_rebounds["position"].isin(["forward", "center"]) & (high_rebounds["age"] > 25)
    truth = condition.all()
    if truth:
        expl = f"All {len(high_rebounds)} players with >7 rebounds are forwards or centers aged >25."
    else:
        viol = high_rebounds[~condition]
        expl = f"{len(viol)} player(s) with >7 rebounds are not forwards or centers aged >25 (positions: {', '.join(viol['position'].tolist())}, ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("../inference_generation/tables/table_36.csv")

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
        (9, stmt_9),
        (10, stmt_10),
        (11, stmt_11),
        (12, stmt_12),
        (13, stmt_13),
        (14, stmt_14),
        (15, stmt_15),
        (16, stmt_16),
        (17, stmt_17),
        (18, stmt_18),
        (19, stmt_19),
        (20, stmt_20),
        (21, stmt_21),
    ]

    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()