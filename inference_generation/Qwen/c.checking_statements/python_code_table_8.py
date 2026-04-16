

import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. Guards have higher average assists per game than forwards and centers combined."""
    guards = df[df['position'] == 'Guard']
    others = df[df['position'].isin(['Forward', 'Center'])]
    if guards.empty or others.empty:
        truth = False
    else:
        avg_guard = guards['assists_per_game'].mean()
        avg_others = others['assists_per_game'].mean()
        truth = avg_guard > avg_others
    if truth:
        expl = f"Guards' average assists ({guards['assists_per_game'].mean():.2f}) exceed others' ({others['assists_per_game'].mean():.2f})."
    else:
        expl = f"Guards' average assists ({guards['assists_per_game'].mean():.2f}) do not exceed others' ({others['assists_per_game'].mean():.2f})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Centers aged 26 or older have rebounds per game exceeding 10."""
    centers = df[(df['position'] == 'Center') & (df['age'] >= 26)]
    condition = centers['rebounds_per_game'] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers aged 26+ have rebounds_per_game >10."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers aged 26+ violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. Forwards with more than 70 games played have points per game above 19."""
    forwards = df[(df['position'] == 'Forward') & (df['games_played'] > 70)]
    condition = forwards['points_per_game'] > 19
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards with >70 games have points_per_game >19."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. If a player is a guard and under 25 years old, their minutes per game are between 26.9 and 32.1."""
    guards = df[(df['position'] == 'Guard') & (df['age'] < 25)]
    condition = guards['minutes_per_game'].between(26.9, 32.1, inclusive='both')
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards under 25 have minutes_per_game between 26.9 and 32.1."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards under 25 violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. All centers have higher rebounds per game than any forward."""
    centers = df[df['position'] == 'Center']
    forwards = df[df['position'] == 'Forward']
    if centers.empty:
        truth = True
        expl = "No centers in the dataset."
    elif forwards.empty:
        truth = True
        expl = "No forwards in the dataset."
    else:
        min_center = centers['rebounds_per_game'].min()
        max_forward = forwards['rebounds_per_game'].max()
        truth = min_center > max_forward
        if truth:
            expl = f"Minimum center rebounds ({min_center:.2f}) exceeds maximum forward rebounds ({max_forward:.2f})."
        else:
            expl = f"Minimum center rebounds ({min_center:.2f}) is not higher than maximum forward rebounds ({max_forward:.2f})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Players with over 30 minutes per game have points per game exceeding 17."""
    players = df[df['minutes_per_game'] > 30]
    condition = players['points_per_game'] > 17
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with >30 minutes have points_per_game >17."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. Guards have higher assists per game than any other position."""
    guards = df[df['position'] == 'Guard']
    others = df[df['position'].isin(['Forward', 'Center'])]
    if guards.empty:
        truth = True
        expl = "No guards in the dataset."
    elif others.empty:
        truth = True
        expl = "No other positions in the dataset."
    else:
        guards_min = guards['assists_per_game'].min()
        others_max = others['assists_per_game'].max()
        truth = guards_min > others_max
        if truth:
            expl = f"Minimum guard assists ({guards_min:.2f}) exceeds maximum of others ({others_max:.2f})."
        else:
            expl = f"Minimum guard assists ({guards_min:.2f}) is not higher than maximum of others ({others_max:.2f})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Forwards aged 29 or older have points per game exceeding 19."""
    forwards = df[(df['position'] == 'Forward') & (df['age'] >= 29)]
    condition = forwards['points_per_game'] > 19
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards aged 29+ have points_per_game >19."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards aged 29+ violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a player is a center and has played more than 70 games, their rebounds per game are above 10.5."""
    centers = df[(df['position'] == 'Center') & (df['games_played'] > 70)]
    condition = centers['rebounds_per_game'] > 10.5
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers with >70 games have rebounds_per_game >10.5."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. Guards under 25 years old have assists per game exceeding 5.8."""
    guards = df[(df['position'] == 'Guard') & (df['age'] < 25)]
    condition = guards['assists_per_game'] > 5.8
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards under 25 have assists_per_game >5.8."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards under 25 violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Centers aged between 26 and 32 have rebounds per game between 9.9 and 11.4."""
    centers = df[(df['position'] == 'Center') & df['age'].between(26, 32, inclusive='both')]
    condition = centers['rebounds_per_game'].between(9.9, 11.4, inclusive='both')
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers aged 26–32 have rebounds_per_game between 9.9 and 11.4."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Forwards with points per game above 20 have assists per game below 4."""
    forwards = df[(df['position'] == 'Forward') & (df['points_per_game'] > 20)]
    condition = forwards['assists_per_game'] < 4
    truth = condition.all()
    if truth:
        expl = f"All {len(forwards)} forwards with points >20 have assists_per_game <4."
    else:
        viol = forwards[~condition]
        expl = f"{len(viol)} forwards violate the rule (assists: {', '.join(map(str, viol['assists_per_game'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. If a player is a guard and has assists per game over 6, their points per game are below 20."""
    guards = df[(df['position'] == 'Guard') & (df['assists_per_game'] > 6)]
    condition = guards['points_per_game'] < 20
    truth = condition.all()
    if truth:
        expl = f"All {len(guards)} guards with assists >6 have points_per_game <20."
    else:
        viol = guards[~condition]
        expl = f"{len(viol)} guards violate the rule (points: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All players with more than 70 games played are either forwards or centers."""
    players = df[df['games_played'] > 70]
    condition = players['position'].isin(['Forward', 'Center'])
    truth = condition.all()
    if truth:
        expl = f"All {len(players)} players with >70 games are forwards or centers."
    else:
        viol = players[~condition]
        expl = f"{len(viol)} players violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Centers aged 28 or older have rebounds per game exceeding 10."""
    centers = df[(df['position'] == 'Center') & (df['age'] >= 28)]
    condition = centers['rebounds_per_game'] > 10
    truth = condition.all()
    if truth:
        expl = f"All {len(centers)} centers aged 28+ have rebounds_per_game >10."
    else:
        viol = centers[~condition]
        expl = f"{len(viol)} centers aged 28+ violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_8.csv")
    df['age'] = pd.to_numeric(df['age'], errors='coerce').astype('Int64')
    df['games_played'] = pd.to_numeric(df['games_played'], errors='coerce').astype('Int64')
    df['minutes_per_game'] = pd.to_numeric(df['minutes_per_game'], errors='coerce').astype('float64')
    df['points_per_game'] = pd.to_numeric(df['points_per_game'], errors='coerce').astype('float64')
    df['assists_per_game'] = pd.to_numeric(df['assists_per_game'], errors='coerce').astype('float64')
    df['rebounds_per_game'] = pd.to_numeric(df['rebounds_per_game'], errors='coerce').astype('float64')
    
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
    ]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()