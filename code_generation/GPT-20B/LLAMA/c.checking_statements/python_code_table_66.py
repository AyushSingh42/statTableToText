import pandas as pd
import re

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

# Helper functions for each pattern
def all_position_age_between(df, pos, min_age, max_age):
    subset = df[df["position"] == pos]
    cond = subset["age"].between(min_age, max_age, inclusive="both")
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} {pos}s are aged {min_age}-{max_age}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} {pos}s violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def if_position_age_between(df, pos, min_age, max_age):
    subset = df[df["position"] == pos]
    cond = subset["age"].between(min_age, max_age, inclusive="both")
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} {pos}s have age between {min_age} and {max_age}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} {pos}s violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def exists_position_age(df, pos, age):
    subset = df[(df["position"] == pos) & (df["age"] == age)]
    truth = not subset.empty
    if truth:
        expl = f"Found {len(subset)} {pos} aged {age}."
    else:
        expl = f"No {pos} aged {age} found."
    return truth, expl

def all_age_or_younger_position(df, age, positions):
    subset = df[df["age"] <= age]
    cond = subset["position"].isin(positions)
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} players aged <= {age} are in {positions}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} players aged <= {age} violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def if_position_ppg_less(df, pos, max_ppg):
    subset = df[df["position"] == pos]
    cond = subset["points_per_game"] < max_ppg
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} {pos}s have PPG < {max_ppg}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} {pos}s violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def all_games_more_minutes(df, games, minutes):
    subset = df[df["games_played"] > games]
    cond = subset["minutes_per_game"] > minutes
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} players with >{games} games have minutes > {minutes}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} players violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def exists_position_games(df, pos, games):
    subset = df[(df["position"] == pos) & (df["games_played"] > games)]
    truth = not subset.empty
    if truth:
        expl = f"Found {len(subset)} {pos} with >{games} games."
    else:
        expl = f"No {pos} with >{games} games found."
    return truth, expl

def if_position_rebounds_less(df, pos, max_reb):
    subset = df[df["position"] == pos]
    cond = subset["rebounds_per_game"] < max_reb
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} {pos}s have rebounds < {max_reb}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} {pos}s violate the rule (rebounds: {', '.join(map(str, viol['rebounds_per_game'].tolist()))})."
    return truth, expl

def all_assists_position(df, min_assists, positions):
    subset = df[df["assists_per_game"] > min_assists]
    cond = subset["position"].isin(positions)
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} players with assists > {min_assists} are in {positions}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} players violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def most_ppg(df, min_ppg):
    count = (df["points_per_game"] > min_ppg).sum()
    truth = count > len(df) / 2
    if truth:
        expl = f"{count} out of {len(df)} players have PPG > {min_ppg}."
    else:
        expl = f"Only {count} out of {len(df)} players have PPG > {min_ppg}."
    return truth, expl

def if_position_age_less(df, pos, max_age):
    subset = df[df["position"] == pos]
    cond = subset["age"] < max_age
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} {pos}s have age < {max_age}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} {pos}s violate the rule (ages: {', '.join(map(str, viol['age'].tolist()))})."
    return truth, expl

def all_age_or_older_position(df, age, positions):
    subset = df[df["age"] >= age]
    cond = subset["position"].isin(positions)
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} players aged >= {age} are in {positions}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} players aged >= {age} violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def exists_age_games(df, age, games):
    subset = df[(df["age"] == age) & (df["games_played"] > games)]
    truth = not subset.empty
    if truth:
        expl = f"Found {len(subset)} players aged {age} with >{games} games."
    else:
        expl = f"No players aged {age} with >{games} games found."
    return truth, expl

def if_ppg_position(df, min_ppg, positions):
    subset = df[df["points_per_game"] > min_ppg]
    cond = subset["position"].isin(positions)
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} players with PPG > {min_ppg} are in {positions}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} players violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def all_rebounds_position(df, min_reb, positions):
    subset = df[df["rebounds_per_game"] > min_reb]
    cond = subset["position"].isin(positions)
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} players with rebounds > {min_reb} are in {positions}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} players violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def exists_age_assists(df, age, min_assists):
    subset = df[(df["age"] <= age) & (df["assists_per_game"] > min_assists)]
    truth = not subset.empty
    if truth:
        expl = f"Found {len(subset)} players aged <= {age} with assists > {min_assists}."
    else:
        expl = f"No players aged <= {age} with assists > {min_assists} found."
    return truth, expl

def if_assists_position(df, min_assists, positions):
    subset = df[df["assists_per_game"] > min_assists]
    cond = subset["position"].isin(positions)
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} players with assists > {min_assists} are in {positions}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} players violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def all_games_ppg(df, games, min_ppg):
    subset = df[df["games_played"] > games]
    cond = subset["points_per_game"] > min_ppg
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} players with >{games} games have PPG > {min_ppg}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} players violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def exists_center_ppg(df, min_ppg):
    subset = df[(df["position"] == "center") & (df["points_per_game"] > min_ppg)]
    truth = not subset.empty
    if truth:
        expl = f"Found {len(subset)} centers with PPG > {min_ppg}."
    else:
        expl = f"No centers with PPG > {min_ppg} found."
    return truth, expl

def if_position_minutes_less(df, pos, max_minutes):
    subset = df[df["position"] == pos]
    cond = subset["minutes_per_game"] < max_minutes
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} {pos}s have minutes < {max_minutes}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} {pos}s violate the rule (minutes: {', '.join(map(str, viol['minutes_per_game'].tolist()))})."
    return truth, expl

def all_rebounds_games(df, min_reb, min_games):
    subset = df[df["rebounds_per_game"] > min_reb]
    cond = subset["games_played"] > min_games
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} players with rebounds > {min_reb} have >{min_games} games."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} players violate the rule (games: {', '.join(map(str, viol['games_played'].tolist()))})."
    return truth, expl

def exists_guard_ppg(df, min_ppg):
    subset = df[(df["position"] == "guard") & (df["points_per_game"] > min_ppg)]
    truth = not subset.empty
    if truth:
        expl = f"Found {len(subset)} guards with PPG > {min_ppg}."
    else:
        expl = f"No guards with PPG > {min_ppg} found."
    return truth, expl

def all_age_or_younger_ppg(df, age, min_ppg):
    subset = df[df["age"] <= age]
    cond = subset["points_per_game"] > min_ppg
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} players aged <= {age} have PPG > {min_ppg}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} players violate the rule (PPG: {', '.join(map(str, viol['points_per_game'].tolist()))})."
    return truth, expl

def exists_age_or_older_games(df, age, min_games):
    subset = df[(df["age"] >= age) & (df["games_played"] > min_games)]
    truth = not subset.empty
    if truth:
        expl = f"Found {len(subset)} players aged >= {age} with >{min_games} games."
    else:
        expl = f"No players aged >= {age} with >{min_games} games found."
    return truth, expl

def if_rebounds_position(df, min_reb, positions):
    subset = df[df["rebounds_per_game"] > min_reb]
    cond = subset["position"].isin(positions)
    truth = cond.all()
    if truth:
        expl = f"All {len(subset)} players with rebounds > {min_reb} are in {positions}."
    else:
        viol = subset[~cond]
        expl = f"{len(viol)} players violate the rule (positions: {', '.join(map(str, viol['position'].tolist()))})."
    return truth, expl

def all_ppg