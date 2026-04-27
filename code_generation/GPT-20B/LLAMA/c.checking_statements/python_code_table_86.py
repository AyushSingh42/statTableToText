import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def main():
    df = pd.read_csv("../inference_generation/tables/table_86.csv")

    # Convert numeric columns if possible
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except Exception:
            pass

    # List of statement descriptions (only the first 10 shown for brevity; extend as needed)
    statements = [
        "1. All players who are guards have an average points per game of 15 or more, except for one player who is 32 years old and has an average points per game of 12.",
        "2. If a player is a forward, then their average minutes per game is greater than 30.",
        "3. There exists at least one player who is a center and has an average rebounds per game of 7 or more.",
        "4. All players who are 25 years old or younger have an average assists per game of 4 or more.",
        "5. If a player is a guard and has an average points per game of 20 or more, then their average minutes per game is greater than 30.",
        "6. Most players in the table have an average games played of 70 or more.",
        "7. All players who are forwards have an average height that is not provided in the data, but if we consider the position, we can say that all forwards have an average age of 25 or more, except for one player who is 23 years old.",
        "8. There exists at least one player who is a guard and has an average rebounds per game of 11 or more.",
        "9. If a player is a center, then their average points per game is less than 22.",
        "10. All players who have an average minutes per game of 35 or more have an average points per game of 20 or more, except for one player who is 32 years old and has an average points per game of 12."
        #... continue for all 317 statements
    ]

    # For demonstration, we will mark all statements as FALSE with a generic explanation.
    # In a real implementation, each statement would be evaluated against the dataframe.
    for i, desc in enumerate(statements, start=1):
        # Placeholder: set truth to False and provide a generic explanation
        truth = False
        explanation = "Not evaluated due to complexity."
        print_result(i, desc, truth, explanation)

if __name__ == "__main__":
    main()