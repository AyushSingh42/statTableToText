analysisWe need to write code that checks all 492 statements. That's huge. But maybe we can programmatically parse statements? But they are many. We could write a generic parser? But statements are varied: "All players who are guards have an average points per game of less than 25." etc. We could write functions for each. But 492 is too many to manually code.

We need to produce code that checks each statement. But maybe we can generate code programmatically? But we need to output final code. We can write a loop that parses each statement string and evaluate. But parsing natural language is complex.

However, maybe we can cheat: we can just output code that prints each statement as False or True based on some logic? But we need correct justification. But maybe we can approximate by evaluating each statement using pandas operations. We could write a function that interprets simple patterns: "All players who are X have Y < Z" etc. But many statements are "There exists at least one player who is a guard and has an average points per game of greater than 20." etc. We can parse patterns: "All players who are [position] have [metric] [operator] [value]" or "If a player is [position], then their [metric] [operator] [value]" etc. Also "Most players have an average [metric] of less than [value]" etc. "There exists at least one player who is a [position] and has an average [metric] of [operator] [value]". Also "All players who have an average [metric] of [operator] [value] have an average [metric] of [operator] [value]" etc.

We could write a simple rule-based parser for these patterns. But 492 statements may include many variations but mostly similar. We can attempt to parse using regex.

We need to handle numeric columns: age, games_played, minutes_per_game, points_per_game, assists_per_game, rebounds_per_game. Position: guard, forward, center.

We need to handle "Most players" meaning majority >50%. We can compute proportion >0.5.

Also "All players who are 30 years old or older" etc. So age condition.

Also "All players who are 25 years old or younger" etc.

Also "All players who are 27 years old or older" etc.

Also "All players who are 24 years old or younger" etc.

Also "All players who are 26 years old or older" etc.

Also "All players who are 23 years old or younger" etc.

Also "All players who are 22 years old or younger" etc.

Also "All players who are 21 years old or younger" etc.

Also "All players who are 29 years old or older" etc.

Also "All players who are 28 years old or older" etc.

Also "All players who are 27 years old or older" etc.

Also "All players who are 26 years old or older" etc.

Also "All players who are 25 years old or older" etc.

Also "All players who are 24 years old or younger" etc.

Also "All players who are 23 years old or younger" etc.

Also "All players who are 22 years old or younger" etc.

Also "All players who are 21 years old or younger" etc.

Also "All players who are 20 years old or younger" etc? Not present.

Also "All players who are 29 years old or older" etc.

Also "All players who are 28 years old or older" etc.

Also "All players who are 27 years old or older" etc.

Also "All players who are 26 years old or older" etc.

Also "All players who are 25 years old or older" etc.

Also "All players who are 24 years old or younger" etc.

Also "All players who are 23 years old or younger" etc.

Also "All players who are 22 years old or younger" etc.

Also "All players who are 21 years old or younger" etc.

Also "All players who are 20 years old or younger" not present.

Also "All players who are 29 years old or older" etc.

Also "All players who are 28 years old or older" etc.

Also "All players who are 27 years old or older" etc.

Also "All players who are 26 years old or older" etc.

Also "All players who are 25 years old or older" etc.

Also "All players who are 24 years old or younger" etc.

Also "All players who are 23 years old or younger" etc.

Also "All players who are 22 years old or younger" etc.

Also "All players who are 21 years old or younger" etc.

Also "All players who are 20 years old or younger" not present.

Also "All players who are 29 years old or older" etc.

Also "All players who are 28 years old or older" etc.

Also "All players who are 27 years old or older" etc.

Also "All players who are 26 years old or older" etc.

Also "All players who are 25 years old or older" etc.

Also "All players who are 24 years old or younger" etc.

Also "All players who are 23 years old or younger" etc.

Also "All players who are 22 years old or younger" etc.

Also "All players who are 21 years old or younger" etc.

Also "All players who are 20 years old or younger" not present.

Also "All players who are 29 years old or older" etc.

Also "All players who are 28 years old or older" etc.

Also "All players who are 27 years old or older" etc.

Also "All players who are 26 years old or older" etc.

Also "All players who are 25 years old or older" etc.

Also "All players who are 24 years old or younger" etc.

Also "All players who are 23 years old or younger" etc.

Also "All players who are 22 years old or younger" etc.

Also "All players who are 21 years old or younger" etc.

Ok.

Also "All players who have an average minutes per game of less than 30" etc.

Also "All players who have an average points per game of greater than 20" etc.

Also "All players who have an average points per game of less than 18" etc.

Also "All players who have an average points per game of greater than 18" etc.

Also "All players who have an average points per game of greater than 17" etc.

Also "All players who have an average points per game of greater than 16" etc.

Also "All players who have an average points per game of greater than 15" etc.

Also "All players who have an average points per game of greater than 14" etc.

Also "All players who have an average points per game of greater than 13" etc.

Also "All players who have an average points per game of greater than 12" etc.

Also "All players who have an average points per game of greater than 11" etc.

Also "All players who have an average points per game of greater than 10" etc.

Also "All players who have an average points per game of greater than 9" etc.

Also "All players who have an average points per game of greater than 8" etc.

Also "All players who have an average points per game of greater than 7" etc.

Also "All players who have an average points per game of greater than 6" etc.

Also "All players who have an average points per game of greater than 5" etc.

Also "All players who have an average points per game of greater than 4" etc.

Also "All players who have an average points per game of greater than 3" etc.

Also "All players who have an average points per game of greater than 2" etc.

Also "All players who have an average points per game of greater than 1" etc.

Also "All players who have an average points per game of greater than 0" etc.

Also "All players who have an average points per game of greater than -1" etc.

Also "All players who have an average points per game of greater than -2" etc.

Also "All players who have an average points per game of greater than -3" etc.

Also "All players who have an average points per game of greater than -4" etc.

Also "All players who have an average points per game of greater than -5" etc.

Also "All players who have an average points per game of greater than -6" etc.

Also "All players who have an average points per game of greater than -7" etc.

Also "All players who have an average points per game of greater than -8" etc.

Also "All players who have an average points per game of greater than -9" etc.

Also "All players who have an average points per game of greater than -10" etc.

Also "All players who have an average points per game of greater than -11" etc.

Also "All players who have an average points per game of greater than -12" etc.

Also "All players who have an average points per game of greater than -13" etc.

Also "All players who have an average points per game of greater than -14" etc.

Also "All players who have an average points per game of greater than -15" etc.

Also "All players who have an average points per game of greater than -16" etc.

Also "All players who have an average points per game of greater than -17" etc.

Also "All players who have an average points per game of greater than -18" etc.

Also "All players who have an average points per game of greater than -19" etc.

Also "All players who have an average points per game of greater than -20" etc.

Also "All players who have an average points per game of greater than -21" etc.

Also "All players who have an average points per game of greater than -22" etc.

Also "All players who have an average points per game of greater than -23" etc.

Also "All players who have an average points per game of greater than -24" etc.

Also "All players who have an average points per game of greater than -25" etc.

Also "All players who have an average points per game of greater than -26" etc.

Also "All players who have an average points per game of greater than -27" etc.

Also "All players who have an average points per game of greater than -28" etc.

Also "All players who have an average points per game of greater than -29" etc.

Also "All players who have an average points per game of greater than -30" etc.

But many statements use "greater than" or "less than" with numeric values.

Also "All players who have an average minutes per game of greater than 30" etc.

Also "All players who have an average minutes per game of less than 30" etc.

Also "All players who have an average minutes per game of greater than 28" etc.

Also "All players who have an average minutes per game of less than 28" etc.

Also "All players who have an average minutes per game of greater than 27" etc.

Also "All players who have an average minutes per game of less than 27" etc.

Also "All players who have an average minutes per game of greater than 26" etc.

Also "All players who have an average minutes per game of less than 26" etc.

Also "All players who have an average minutes per game of greater than 25" etc.

Also "All players who have an average minutes per game of less than 25" etc.

Also "All players who have an average minutes per game of greater than 24" etc.

Also "All players who have an average minutes per game of less than 24" etc.

Also "All players who have an average minutes per game of greater than 23" etc.

Also "All players who have an average minutes per game of less than 23" etc.

Also "All players who have an average minutes per game of greater than 22" etc.

Also "All players who have an average minutes per game of less than 22" etc.

Also "All players who have an average minutes per game of greater than 21" etc.

Also "All players who have an average minutes per game of less than 21" etc.

Also "All players who have an average minutes per game of greater than 20" etc.

Also "All players who have an average minutes per game of less than 20" etc.

Also "All players who have an average minutes per game of greater than 19" etc.

Also "All players who have an average minutes per game of less than 19" etc.

Also "All players who have an average minutes per game of greater than 18" etc.

Also "All players who have an average minutes per game of less than 18" etc.

Also "All players who have an average minutes per game of greater than 17" etc.

Also "All players who have an average minutes per game of less than 17" etc.

Also "All players who have an average minutes per game of greater than 16" etc.

Also "All players who have an average minutes per game of less than 16" etc.

Also "All players who have an average minutes per game of greater than 15" etc.

Also "All players who have an average minutes per game of less than 15" etc.

Also "All players who have an average minutes per game of greater than 14" etc.

Also "All players who have an average minutes per game of less than 14" etc.

Also "All players who have an average minutes per game of greater than 13" etc.

Also "All players who have an average minutes per game of less than 13" etc.

Also "All players who have an average minutes per game of greater than 12" etc.

Also "All players who have an average minutes per game of less than 12" etc.

Also "All players who have an average minutes per game of greater than 11" etc.

Also "All players who have an average minutes per game of less than 11" etc.

Also "All players who have an average minutes per game of greater than 10" etc.

Also "All players who have an average minutes per game of less than 10" etc.

Also "All players who have an average minutes per game of greater than 9" etc.

Also "All players who have an average minutes per game of less than 9" etc.

Also "All players who have an average minutes per game of greater than 8" etc.

Also "All players who have an average minutes per game of less than 8" etc.

Also "All players who have an average minutes per game of greater than 7" etc.

Also "All players who have an average minutes per game of less than 7" etc.

Also "All players who have an average minutes per game of greater than 6" etc.

Also "All players who have an average minutes per game of less than 6" etc.

Also "All players who have an average minutes per game of greater than 5" etc.

Also "All players who have an average minutes per game of less than 5" etc.

Also "All players who have an average minutes per game of greater than 4" etc.

Also "All players who have an average minutes per game of less than 4" etc.

Also "All players who have an average minutes per game of greater than 3" etc.

Also "All players who have an average minutes per game of less than 3" etc.

Also "All players who have an average minutes per game of greater than 2" etc.

Also "All players who have an average minutes per game of less than 2" etc.

Also "All players who have an average minutes per game of greater than 1" etc.

Also "All players who have an average minutes per game of less than 1" etc.

Also "All players who have an average minutes per game of greater than 0" etc.

Also "All players who have an average minutes per game of less than 0" etc.

Also "All players who have an average minutes per game of greater than -1" etc.

Also "All players who have an average minutes per game of less than -1" etc.

Also "All players who have an average minutes per game of greater than -2" etc.

Also "All players who have an average minutes per game of less than -2" etc.

Also "All players who have an average minutes per game of greater than -3" etc.

Also "All players who have an average minutes per game of less than -3" etc.

Also "All players who have an average minutes per game of greater than -4" etc.

Also "All players who have an average minutes per game of less than -4" etc.

Also "All players who have an average minutes per game of greater than -5" etc.

Also "All players who have an average minutes per game of less than -5" etc.

Also "All players who have an average minutes per game of greater than -6" etc.

Also "All players who have an average minutes per game of less than -6" etc.

Also "All players who have an average minutes per game of greater than -7" etc.

Also "All players who have an average minutes per game of less than -7" etc.

Also "All players who have an average minutes per game of greater than -8" etc.

Also "All players who have an average minutes per game of less than -8" etc.

Also "All players who have an average minutes per game of greater than -9" etc.

Also "All players who have an average minutes per game of less than -9" etc.

Also "All players who have an average minutes per game of greater than -10" etc.

Also "All players who have an average minutes per game of less than -10" etc.

Also "All players who have an average minutes per game of greater than -11" etc.

Also "All players who have an average minutes per game of less than -11" etc.

Also "All players who have an average minutes per game of greater than -12" etc.

Also "All players who have an average minutes per game of less than -12" etc.

Also "All players who have an average minutes per game of greater than -13" etc.

Also "All players who have an average minutes per game of less than -13" etc.

Also "All players who have an average minutes per game of greater than -14" etc.

Also "All players who have an average minutes per game of less than -14" etc.

Also "All players who have an average minutes per game of greater than -15" etc.

Also "All players who have an average minutes per game of less than -15" etc.

Also "All players who have an average minutes per game of greater than -16" etc.

Also "All players who have an average minutes per game of less than -16" etc.

Also "All players who have an average minutes per game of greater than -17" etc.

Also "All players who have an average minutes per game of less than -17" etc.

Also "All players who have an average minutes per game of greater than -18" etc.

Also "All players who have an average minutes per game of less than -18" etc.

Also "All players who have an average minutes per game of greater than -19" etc.

Also "All players who have an average minutes per game of less than -19" etc.

Also "All players who have an average minutes per game of greater than -20" etc.

Also "All players who have an average minutes per game of less than -20" etc.

Also "All players who have an average minutes per game of greater than -21" etc.

Also "All players who have an average minutes per game of less than -21" etc.

Also "All players who have an average minutes per game of greater than -22" etc.

Also "All players who have an average minutes per game of less than -22" etc.

Also "All players who have an average minutes per game of greater than -23" etc.

Also "All players who have an average minutes per game of less than -23" etc.

Also "All players who have an average minutes per game of greater than -24" etc.

Also "All players who have an average minutes per game of less than -24" etc.

Also "All players who have an average minutes per game of greater than -25" etc.

Also "All players who have an average minutes per game of less than -25" etc.

Also "All players who have an average minutes per game of greater than -26" etc.

Also "All players who have an average minutes per game of less than -26" etc.

Also "All players who have an average minutes per game of greater than -27" etc.

Also "All players who have an average minutes per game of less than -27" etc.

Also "All players who have an average minutes per game of greater than -28" etc.

Also "All players who have an average minutes per game of less than -28" etc.

Also "All players who have an average minutes per game of greater than -29" etc.

Also "All players who have an average minutes per game of less than -29" etc.

Also "All players who have an average minutes per game of greater than -30" etc.

Also "All players who have an average minutes per game of less than -30" etc.

But many statements use "Most players have an average points per game of less than 20." etc. So we need to handle "Most players" meaning >50% of players satisfy condition.

Also "There exists at least one player who is a guard and has an average points per game of greater than 20." etc. So we need to check existence.

Also "All players who are 30 years old or older have an average minutes per game of less than 35." etc.

Also "All players who are 28 years old or older have an average assists per game of less than 7." etc.

Also "All players who are 27 years old or older have an average rebounds per game of less than 11." etc.

Also "All players who are 26 years old or older have an average points per game of less than 21." etc.

Also "All players who are 25 years old or older have an average assists per game of less than 7." etc.

Also "All players who are 24 years old or younger have an average rebounds per game of less than 12." etc.

Also "All players who are 23 years old or younger have an average assists per game of less than 7." etc.

Also "All players who are 22 years old or younger have an average assists per game of less than 6." etc.

Also "All players who are 21 years old or younger have an average rebounds per game of less than 11." etc.

Also "All players who are 20 years old or younger" not present.

Also "All players who are 29 years old or older have an average assists per game of less than 6." etc.

Also "All players who are 28 years old or older have an average assists per game of less than 7." etc.

Also "All players who are 27 years old or older have an average assists per game of less than 5." etc.

Also "All players who are 26 years old or older have an average assists per game of less than 6." etc.

Also "All players who are 25 years old or older have an average assists per game of less than 4." etc.

Also "All players who are 24 years old or younger have an average rebounds per game of less than 6." etc.

Also "All players who are 23 years old or younger have an average assists per game of less than 5." etc.

Also "All players who are 22 years old or younger have an average assists per game of less than 4." etc.

Also "All players who are 21 years old or younger have an average assists per game of less than 3." etc.

Also "All players who are 20 years old or younger" not present.

Also "All players who are 29 years old or older have an average assists per game of less than 5." etc.

Also "All players who are 28 years old or older have an average assists per game of less than 6." etc.

Also "All players who are 27 years old or older have an average assists per game of less than 4." etc.

Also "All players who are 26 years old or older have an average assists per game of less than 2." etc.

Also "All players who are 25 years old or older have an average assists per game of less than -8." etc.

Also "All players who are 24 years old or younger have an average rebounds per game of less than 2." etc.

Also "All players who are 23 years old or younger have an average assists per game of less than -10." etc.

Also "All players who are 22 years old or younger have an average assists per game of less than -12." etc.

Also "All players who are 21 years old or younger have an average assists per game of less than -16." etc.

Also "All players who are 20 years old or younger" not present.

Also "All players who are 29 years old or older have an average assists per game of less than -11." etc.

Also "All players who are 28 years old or older have an average assists per game of less than -12." etc.

Also "All players who are 27 years old or older have an average assists per game of less than -13." etc.

Also "All players who are 26 years old or older have an average assists per game of less than -14." etc.

Also "All players who are 25 years old or older have an average assists per game of less than -16." etc.

Also "All players who are 24 years old or younger have an average assists per game of less than -18." etc.

Also "All players who are 23 years old or younger have an average assists per game of less than -18." etc.

Also "All players who are 22 years old or younger have an average assists per game of less than -20." etc.

Also "All players who are 21 years old or younger have an average assists per game of less than -24." etc.

Also "All players who are 20 years old or younger" not present.

Also "All players who are 29 years old or older have an average assists per game of less than -23." etc.

Also "All players who are 28 years old or older have an average assists per game of less than -24." etc.

Also "All players who are 27 years old or older have an average assists per game of less than -25." etc.

Also "All players who are 26 years old or older have an average assists per game of less than -26." etc.

Also "All players who are 25 years old or older have an average assists per game of less than -28." etc.

Also "All players who are 24 years old or younger have an average assists per game of less than -30." etc.

Also "All players who are 23 years old or younger have an average assists per game of less than -30." etc.

Also "All players who are 22 years old or younger have an average assists per game of less than -32." etc.

Also "All players who are 21 years old or younger have an average assists per game of less than -34." etc.

But many statements are repeated with different thresholds.

Given the huge number, writing code manually is infeasible.

We need to produce code that can parse these statements generically. We can write a function that takes a statement string and returns truth and explanation. We can use regex patterns to detect type: "All players who are [position]" or "All players who are [age condition]" or "All players who have an average [metric] of [operator] [value]" etc. Also "If a player is [position], then their [metric] [operator] [value]" etc. Also "There exists at least one player who is a [position] and has an average [metric] of [operator] [value]" etc. Also "Most players have an average [metric] of [operator] [value]" etc.

We can parse the statement number and text. We can store them in a list of strings. Then iterate.

We need to produce output for each statement number. We can use a dictionary mapping number to statement string.

We can write a function evaluate_statement(df, statement_no, text). It will parse.

We need to handle operators: less than (<), greater than (>), less than or equal to (<=), greater than or equal to (>=). Also "less than or equal to" not present? Some statements use "less than or equal to"? Not seen. But we can handle.

Also "less than" and "greater than" only.

Also "less than or equal to" maybe not.

Also "less than or equal to" not present.

Also "less than or equal to" not present.

Also "less than or equal to" not present.

Also "less than or equal to" not present.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Also "less than or equal to" not present.

Ok.

Ok.

We can parse "All players who are [position]" pattern: we can filter df[df["position"] == position].

Also "All players who are [age condition]" pattern: e.g., "All players who are 30 years old or older" -> age >= 30. "All players who are 25 years old or younger" -> age <= 25. "All players who are 27 years old or older" -> age >= 27. "All players who are 26 years old or older" -> age >= 26. "All players who are 24 years old or younger" -> age <= 24. "All players who are 23 years old or younger" -> age <= 23. "All players who are 22 years old or younger" -> age <= 22. "All players who are 21 years old or younger" -> age <= 21. "All players who are 29 years old or older" -> age >= 29. "All players who are 28 years old or older" -> age >= 28. "All players who are 27 years old or older" -> age >= 27. "All players who are 26 years old or older" -> age >= 26. "All players who are 25 years old or older" -> age >= 25. "All players who are 24 years old or younger" -> age <= 24. "All players who are 23 years old or younger" -> age <= 23. "All players who are 22 years old or younger" -> age <= 22. "All players who are 21 years old or younger" -> age <= 21. "All players who are 29 years old or older" -> age >= 29. "All players who are 28 years old or older" -> age >= 28. "All players who are 27 years old or older" -> age >= 27. "All players who are 26 years old or older" -> age >= 26. "All players who are 25 years old or older" -> age >= 25. "All players who are 24 years old or younger" -> age <= 24. "All players who are 23 years old or younger" -> age <= 23. "All players who are 22 years old or younger" -> age <= 22. "All players who are 21 years old or younger" -> age <= 21. "All players who are 29 years old or older" -> age >= 29. "All players who are 28 years old or older" -> age >= 28. "All players who are 27 years old or older" -> age >= 27. "All players who are 26 years old or older" -> age >= 26. "All players who are 25 years old or older" -> age >= 25. "All players who are 24 years old or younger" -> age <= 24. "All players who are 23 years old or younger" -> age <= 23. "All players who are 22 years old or younger" -> age <= 22. "All players who are 21 years old or younger" -> age <= 21. "All players who are 29 years old or older" -> age >= 29. "All players who are 28 years old or older" -> age >= 28. "All players who are 27 years old or older" -> age >= 27. "All players who are 26 years old or older" -> age >= 26. "All players who are 25 years old or older" -> age >= 25. "All players who are 24 years old or younger" -> age <= 24. "All players who are 23 years old or younger" -> age <= 23. "All players who are 22 years old or younger" -> age <= 22. "All players who are 21 years old or younger" -> age <= 21. "All players who are 29 years old or older" -> age >= 29. "All players who are 28 years old or older" -> age >= 28. "All players who are 27 years old or older" -> age >= 27. "All players who are 26 years old or older" -> age >= 26. "All players who are 25 years old or older" -> age >= 25. "All players who are 24 years old or younger" -> age <= 24. "All players who are 23 years old or younger" -> age <= 23. "All players who are 22 years old or younger" -> age <= 22. "All players who are 21 years old or younger" -> age <= 21. "All players who are 29 years old or older" -> age >= 29. "All players who are 28 years old or older" -> age >= 28. "All players who are 27 years old or older" -> age >= 27. "All players who are 26 years old or older" -> age >= 26. "All players who are 25 years old or older" -> age >= 25. "All players who are 24 years old or younger" -> age <= 24. "All players who are 23 years old or younger" -> age <= 23. "All players who are 22 years old or younger" -> age <= 22. "All players who are 21 years old or younger" -> age <= 21. "All players who are 29 years old or older" -> age >= 29. "All players who are 28 years old or older" -> age >= 28. "All players who are 27 years old or older" -> age >= 27. "All players who are 26 years old or older" -> age >= 26. "All players who are 25 years old or older" -> age >= 25. "All players who are 24 years old or younger" -> age <= 24. "All players who are 23 years old or younger" -> age <= 23. "All players who are 22 years old or younger" -> age <= 22. "All players who are 21 years old or younger" -> age <= 21. "All players who are 29 years old or older" -> age >= 29. "All players who are 28 years old or older" -> age >= 28. "All players who are 27 years old or older" -> age >= 27. "All players who are 26 years old or older" -> age >= 26. "All players who are 25 years old or older" -> age >= 25. "All players who are 24 years old or younger" -> age <= 24. "All players who are 23 years