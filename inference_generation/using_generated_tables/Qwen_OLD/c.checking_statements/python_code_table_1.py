<think>
Okay, I need to write Python code using pandas to check each of the 15 statements against the given dataset. Let me start by understanding each statement and figuring out how to translate them into conditions.

First, the dataset has columns: District ID, District Name, State, Number of Students, Average Class Size, Percentage Free Lunch, Average Math Score, Average Reading Score, Funding Per Student. The CSV is already at the specified path.

The main steps are:

1. Read the CSV into a DataFrame.
2. Convert any numeric columns stored as strings to integers. Wait, the user mentioned converting numbers stored as strings. Which columns are numeric? Probably Number of Students, Average Class Size, Percentage Free Lunch, Average Math Score, Average Reading Score, Funding Per Student. So I need to check each of these columns and convert them to numeric types if they're strings. For example, pd.to_numeric with errors='coerce' maybe.

Wait, the user says "convert any turn numbers stored as strings into integers". Wait, maybe it's a typo and they mean "convert numbers stored as strings into integers". So I need to process columns like Number of Students, Funding Per Student, etc., converting them from string to numeric types. So in the code, after reading the CSV, I should loop through these columns and convert them. Let me note that.

So in the main function, after reading the CSV, I'll do something like:

df['Number of Students'] = pd.to_numeric(df['Number of Students'], errors='coerce').astype(int)
Similarly for other numeric columns. Wait, but some might be floats. For example, Average Class Size could be a float. But the user says to convert to integers? Wait, maybe the user meant convert to numeric types (float or int) if they are stored as strings. Because the problem says "convert any turn numbers stored as strings into integers"—probably a typo. Let me assume that the columns like Number of Students should be integers, Funding Per Student could be float. So perhaps convert them to numeric types.

But the user's instruction says to convert numbers stored as strings into integers. Maybe they want all numeric columns to be integers. Hmm. Well, perhaps the correct approach is to convert each relevant column to numeric type. For example:

columns_to_convert = [
    'Number of Students',
    'Average Class Size',
    'Percentage Free Lunch',
    'Average Math Score',
    'Average Reading Score',
    'Funding Per Student'
]

for col in columns_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

But maybe some columns like Average Class Size can be float. So converting them to numeric (float) is better. But the user says integers. Wait, maybe the user made a mistake. Let me proceed with converting to numeric types, not necessarily integers. Because for example, Percentage Free Lunch is a percentage and could be a float. So I'll convert those columns to numeric, handling any string representations.

Once the data is properly formatted, then proceed to check each statement.

Now, let's go through each statement one by one and create functions for them.

Statement 1: All districts with funding per student exceeding $12,000 have average math scores above 600.

So filter districts where Funding Per Student > 12000. Check if all of them have Average Math Score > 600.

Statement 2: Districts in California with funding per student above $12,000 have average math scores higher than those with funding below $10,000.

So for California districts, compare those with funding >12000 vs funding <10000. Check if the average math scores of the former are higher than the latter.

But how to compare? Maybe take the average math scores of each group and see if all in the first group are higher than all in the second? Or compare the minimum of the first group to the maximum of the second? Or perhaps compare the average? The statement says "have average math scores higher than..." which could be interpreted as each district in the first group has a higher score than each in the second. But that's probably not feasible. Alternatively, maybe the average of the first group is higher than the average of the second. But the wording is ambiguous. However, the original example uses "all" conditions. Let me check the original example for statement 1: the example uses.all() on the condition. So perhaps for statement 2, the correct approach is to compare each district in California with funding >12k has a higher math score than each district in California with funding <10k. But that's a pairwise comparison which is not feasible. Alternatively, perhaps the statement is that for California districts, the average math score of those with funding >12k is higher than those with funding <10k. But the wording says "have average math scores higher than..." which could be interpreted as each district in the first group has a higher score than each in the second. But that's too strict. Alternatively, maybe the average of the first group is higher than the average of the second. But the problem says to check whether the statement is true. So perhaps the correct way is to check for each district in California, if funding is >12k, then their math score is higher than any district in California with funding <10k. But how to check that? For example, the minimum math score of the first group is higher than the maximum math score of the second group. That would ensure that all districts in the first group have higher scores than all in the second. So for statement 2, the condition would be min(math_scores_group1) > max(math_scores_group2). Let me proceed with that approach.

Statement 3: If a district’s average class size exceeds 25, its percentage free lunch is always above 25%.

So filter districts where Average Class Size >25. Check if all of them have Percentage Free Lunch >25.

Statement 4: For districts in Texas, average math scores are consistently below 600, while districts in New York have scores above 610.

So two conditions: Texas districts have math scores <600, and New York districts have math scores >610. Both must be true.

Statement 5: Districts with funding per student below $9,000 have average math scores lower than districts with funding above $10,000.

This is similar to statement 2. So compare the math scores of districts with funding <9000 vs those with funding >10000. Again, perhaps check if the max of the first group is less than the min of the second group.

Statement 6: In districts where percentage free lunch exceeds 30%, average math scores are strictly below 570.

Filter districts where Percentage Free Lunch >30%, check if all have math scores <570.

Statement 7: All districts with average class sizes below 23 have funding per student exceeding $10,000.

Check if all districts with Average Class Size <23 have Funding Per Student >10000.

Statement 8: For districts in Illinois, average math scores are inversely correlated with percentage free lunch (higher free lunch percentages correspond to lower scores).

This is a correlation check. The correlation between percentage free lunch and math scores should be negative. But how to check this? Compute the Pearson correlation coefficient and check if it's negative. However, the statement says "inversely correlated", which could mean a negative correlation. But since it's a sample, we need to check if the correlation is negative. However, if there are only a few data points, maybe we can check if for all pairs, higher percentage free lunch corresponds to lower math scores. But that's not feasible. So perhaps compute the correlation coefficient and check if it's negative. But how to handle cases where there are zero or one data points? Maybe skip if there are not enough data.

Statement 9: Districts with over 20,000 students have average math scores below 570, while districts with fewer than 10,000 students have scores above 580.

Two conditions: districts with Number of Students >20000 have math scores <570, and districts with Number of Students <10000 have math scores >580.

Statement 10: If a district’s funding per student is between $10,000 and $12,000, its average math score is between 590 and 610.

Check if all districts with Funding Per Student between 10k and 12k (inclusive?) have math scores between 590 and 610. Need to clarify if inclusive. The original statement says "between $10,000 and $12,000"—probably inclusive. Similarly for math scores between 590 and 610.

Statement 11: Districts in Ohio with funding per student above $11,000 have average math scores exceeding 600, while those with lower funding have scores below 600.

Two groups: Ohio districts with funding >11000 have math scores >600, and those with funding <=11000 have math scores <600.

Statement 12: For districts where average class size is between 24 and 26, funding per student is positively correlated with average math scores.

Check if within districts with Average Class Size between 24 and 26, the correlation between Funding Per Student and Math Score is positive. Again, Pearson correlation coefficient.

Statement 13: All districts with average reading scores above 630 have funding per student exceeding $12,000.

Check if all districts with Average Reading Score >630 have Funding Per Student >12000.

Statement 14: Districts in Pennsylvania with average class sizes above 26 have average math scores below 590.

Check if all PA districts with Average Class Size >26 have Math Score <590.

Statement 15: Districts with percentage free lunch below 15% have average math scores exceeding 610, while those with percentages above 30% have scores below 550.

Two conditions: for districts with % free lunch <15% → math score >610; and for those with % free lunch >30% → math score <550.

Now, I need to create functions for each statement, similar to the example provided.

Let me start writing the code.

First, the main function reads the CSV, converts the necessary columns to numeric.

Then, for each statement, a function is called that returns truth and explanation.

Let me think about possible issues:

- Handling NaN values. For example, if a column has missing data, when converting to numeric, it becomes NaN. So when filtering, need to drop NaNs or handle them. But the problem says to check the statements, so perhaps assume that the data is complete. Or handle cases where there are no entries for a certain condition (e.g., if there are no districts in California with funding above 12k, then the statement is vacuously true? Or maybe considered as not applicable, but according to the example, if all women are aged 21-43, even if there are zero women, it's true.)

But in practice, if there are no districts meeting the condition, then the statement is considered true? For example, statement 1: if there are no districts with funding >12k, then the statement is vacuously true.

But need to handle that in the code.

Now, let's proceed to code each statement.

For example, statement 1:

def stmt_1(df):
    """1. All districts with funding per student exceeding $12,000 have average math scores above 600."""
    # Filter districts with funding >12000
    high_funding = df[df['Funding Per Student'] > 12000]
    # Check if all have math scores >600
    condition = high_funding['Average Math Score'] > 600
    truth = condition.all()
    if truth:
        expl = f"All {len(high_funding)} districts with funding >$12,000 have math scores above 600."
    else:
        viol = high_funding[~condition]
        expl = f"{len(viol)} districts violate the rule (math scores: {', '.join(map(str, viol['Average Math Score'].tolist()))})."
    return truth, expl

But need to make sure that columns are correctly named. Also, need to convert the columns to numeric first.

Now, for statement 2:

def stmt_2(df):
    """2. Districts in California with funding per student above $12,000 have average math scores higher than those with funding below $10,000."""
    # Filter California districts
    ca_df = df[df['State'] == 'California']
    # Get high funding and low funding groups
    high_funding = ca_df[ca_df['Funding Per Student'] > 12000]
    low_funding = ca_df[ca_df['Funding Per Student'] < 10000]
    # Check if all high funding math scores are higher than all low funding math scores
    if high_funding.empty or low_funding.empty:
        # If either group is empty, vacuously true? Or depends on the statement's wording.
        # If no districts in high funding, then the statement is vacuously true.
        # If no districts in low funding, then the condition is automatically true.
        # But need to think about the logic.
        # For example, if there are no low funding districts, then the statement is true because there are no districts to compare against.
        # Similarly if no high funding districts, then the statement is vacuously true.
        truth = True
        expl = "No applicable districts in one or both groups."
    else:
        max_low = low_funding['Average Math Score'].max()
        min_high = high_funding['Average Math Score'].min()
        truth = (min_high > max_low)
        if truth:
            expl = f"Minimum math score in high funding group ({min_high}) exceeds maximum in low funding group ({max_low})."
        else:
            expl = f"Minimum high funding math score ({min_high}) is not higher than maximum low funding math score ({max_low})."
    return truth, expl

But need to handle cases where there are no districts in California. Then, the statement would be vacuously true? Or false? Well, according to logic, if there are no districts in California, then the statement is vacuously true because there are no counterexamples.

Similarly for other statements.

Now, statement 3:

def stmt_3(df):
    """3. If a district’s average class size exceeds 25, its percentage free lunch is always above 25%."""
    large_class = df[df['Average Class Size'] > 25]
    condition = large_class['Percentage Free Lunch'] > 25
    truth = condition.all()
    if truth:
        expl = f"All {len(large_class)} districts with class size >25 have free lunch >25%."
    else:
        viol = large_class[~condition]
        expl = f"{len(viol)} districts violate the rule (free lunch percentages: {', '.join(map(str, viol['Percentage Free Lunch'].tolist()))})."
    return truth, expl

Statement 4:

def stmt_4(df):
    """4. For districts in Texas, average math scores are consistently below 600, while districts in New York have scores above 610."""
    texas = df[df['State'] == 'Texas']
    new_york = df[df['State'] == 'New York']
    # Check Texas condition
    texas_condition = texas['Average Math Score'] < 600
    texas_truth = texas_condition.all() if not texas.empty else True
    # Check New York condition
    ny_condition = new_york['Average Math Score'] > 610
    ny_truth = ny_condition.all() if not new_york.empty else True
    overall_truth = texas_truth and ny_truth
    expl_parts = []
    if not texas_truth:
        viol_texas = texas[~texas_condition]
        expl_parts.append(f"Texas: {len(viol_texas)} districts have math scores >=600 (e.g., {', '.join(map(str, viol_texas['Average Math Score'].tolist()))}).")
    if not ny_truth:
        viol_ny = new_york[~ny_condition]
        expl_parts.append(f"New York: {len(viol_ny)} districts have math scores <=610 (e.g., {', '.join(map(str, viol_ny['Average Math Score'].tolist()))}).")
    if not expl_parts:
        expl = "All Texas districts have math scores <600 and all New York districts have scores >610."
    else:
        expl = "Violations found: " + "; ".join(expl_parts)
    return overall_truth, expl

Statement 5:

def stmt_5(df):
    """5. Districts with funding per student below $9,000 have average math scores lower than districts with funding above $10,000."""
    low_funding = df[df['Funding Per Student'] < 9000]
    high_funding = df[df['Funding Per Student'] > 10000]
    if low_funding.empty or high_funding.empty:
        truth = True
        expl = "No applicable districts in one or both groups."
    else:
        max_low = low_funding['Average Math Score'].max()
        min_high = high_funding['Average Math Score'].min()
        truth = (max_low < min_high)
        if truth:
            expl = f"Maximum math score in low funding group ({max_low}) is less than minimum in high funding group ({min_high})."
        else:
            expl = f"Maximum low funding math score ({max_low}) is not less than minimum high funding math score ({min_high})."
    return truth, expl

Statement 6:

def stmt_6(df):
    """6. In districts where percentage free lunch exceeds 30%, average math scores are strictly below 570."""
    high_free_lunch = df[df['Percentage Free Lunch'] > 30]
    condition = high_free_lunch['Average Math Score'] < 570
    truth = condition.all() if not high_free_lunch.empty else True
    if truth:
        expl = f"All {len(high_free_lunch)} districts with free lunch >30% have math scores <570."
    else:
        viol = high_free_lunch[~condition]
        expl = f"{len(viol)} districts violate the rule (math scores: {', '.join(map(str, viol['Average Math Score'].tolist()))})."
    return truth, expl

Statement 7:

def stmt_7(df):
    """7. All districts with average class sizes below 23 have funding per student exceeding $10,000."""
    small_class = df[df['Average Class Size'] < 23]
    condition = small_class['Funding Per Student'] > 10000
    truth = condition.all() if not small_class.empty else True
    if truth:
        expl = f"All {len(small_class)} districts with class size <23 have funding >$10,000."
    else:
        viol = small_class[~condition]
        expl = f"{len(viol)} districts violate the rule (funding: {', '.join(map(str, viol['Funding Per Student'].tolist()))})."
    return truth, expl

Statement 8:

def stmt_8(df):
    """8. For districts in Illinois, average math scores are inversely correlated with percentage free lunch (higher free lunch percentages correspond to lower scores)."""
    illinois = df[df['State'] == 'Illinois']
    if illinois.empty:
        truth = True
        expl = "No districts in Illinois."
        return truth, expl
    # Check if the correlation is negative
    corr = illinois['Percentage Free Lunch'].corr(illinois['Average Math Score'], method='pearson')
    # Check if correlation is negative
    truth = corr < 0
    if truth:
        expl = f"Pearson correlation between free lunch and math scores in Illinois is {corr:.2f}, which is negative."
    else:
        expl = f"Pearson correlation in Illinois is {corr:.2f}, not negative."
    return truth, expl

But need to handle cases where there's only one district (correlation can't be computed). In that case, maybe consider it as true? Or false? Well, if there's only one district, there's no way to determine correlation. But according to the problem statement, perhaps treat it as true since there's no data to contradict the statement.

But in pandas, corr() returns NaN if there's only one data point. So need to handle that.

So modifying the code:

def stmt_8(df):
    """8. For districts in Illinois, average math scores are inversely correlated with percentage free lunch (higher free lunch percentages correspond to lower scores)."""
    illinois = df[df['State'] == 'Illinois']
    if illinois.empty:
        truth = True
        expl = "No districts in Illinois."
        return truth, expl
    if len(illinois) < 2:
        truth = True
        expl = "Only one district in Illinois; insufficient data to determine correlation."
        return truth, expl
    corr = illinois['Percentage Free Lunch'].corr(illinois['Average Math Score'], method='pearson')
    truth = corr < 0
    if truth:
        expl = f"Pearson correlation between free lunch and math scores in Illinois is {corr:.2f}, which is negative."
    else:
        expl = f"Pearson correlation in Illinois is {corr:.2f}, not negative."
    return truth, expl

Statement 9:

def stmt_9(df):
    """9. Districts with over 20,000 students have average math scores below 570, while districts with fewer than 10,000 students have scores above 580."""
    large_districts = df[df['Number of Students'] > 20000]
    small_districts = df[df['Number of Students'] < 10000]
    # Check large districts
    large_condition = large_districts['Average Math Score'] < 570
    large_truth = large_condition.all() if not large_districts.empty else True
    # Check small districts
    small_condition = small_districts['Average Math Score'] > 580
    small_truth = small_condition.all() if not small_districts.empty else True
    overall_truth = large_truth and small_truth
    expl_parts = []
    if not large_truth:
        viol_large = large_districts[~large_condition]
        expl_parts.append(f"Large districts: {len(viol_large)} have math scores >=570 (e.g., {', '.join(map(str, viol_large['Average Math Score'].tolist()))}).")
    if not small_truth:
        viol_small = small_districts[~small_condition]
        expl_parts.append(f"Small districts: {len(viol_small)} have math scores <=580 (e.g., {', '.join(map(str, viol_small['Average Math Score'].tolist()))}).")
    if not expl_parts:
        expl = "All large districts have math scores <570 and all small districts have scores >580."
    else:
        expl = "Violations found: " + "; ".join(expl_parts)
    return overall_truth, expl

Statement 10:

def stmt_10(df):
    """10. If a district’s funding per student is between $10,000 and $12,000, its average math score is between 590 and 610."""
    mid_funding = df[(df['Funding Per Student'] >= 10000) & (df['Funding Per Student'] <= 12000)]
    condition = mid_funding['Average Math Score'].between(590, 610, inclusive="both")
    truth = condition.all() if not mid_funding.empty else True
    if truth:
        expl = f"All {len(mid_funding)} districts with funding between $10k–$12k have math scores between 590–610."
    else:
        viol = mid_funding[~condition]
        expl = f"{len(viol)} districts violate the rule (math scores: {', '.join(map(str, viol['Average Math Score'].tolist()))})."
    return truth, expl

Statement 11:

def stmt_11(df):
    """11. Districts in Ohio with funding per student above $11,000 have average math scores exceeding 600, while those with lower funding have scores below 600."""
    ohio = df[df['State'] == 'Ohio']
    high_funding = ohio[ohio['Funding Per Student'] > 11000]
    low_funding = ohio[ohio['Funding Per Student'] <= 11000]
    # Check high funding
    high_condition = high_funding['Average Math Score'] > 600
    high_truth = high_condition.all() if not high_funding.empty else True
    # Check low funding
    low_condition = low_funding['Average Math Score'] < 600
    low_truth = low_condition.all() if not low_funding.empty else True
    overall_truth = high_truth and low_truth
    expl_parts = []
    if not high_truth:
        viol_high = high_funding[~high_condition]
        expl_parts.append(f"High funding Ohio districts: {len(viol_high)} have math scores <=600 (e.g., {', '.join(map(str, viol_high['Average Math Score'].tolist()))}).")
    if not low_truth:
        viol_low = low_funding[~low_condition]
        expl_parts.append(f"Low funding Ohio districts: {len(viol_low)} have math scores >=600 (e.g., {', '.join(map(str, viol_low['Average Math Score'].tolist()))}).")
    if not expl_parts:
        expl = "All Ohio districts with high funding have math scores >600 and low funding have scores <600."
    else:
        expl = "Violations found: " + "; ".join(expl_parts)
    return overall_truth, expl

Statement 12:

def stmt_12(df):
    """12. For districts where average class size is between 24 and 26, funding per student is positively correlated with average math scores."""
    mid_class = df[(df['Average Class Size'] >= 24) & (df['Average Class Size'] <= 26)]
    if mid_class.empty:
        truth = True
        expl = "No districts with average class size between 24–26."
        return truth, expl
    if len(mid_class) < 2:
        truth = True
        expl = "Only one district in the class size range; insufficient data for correlation."
        return truth, expl
    corr = mid_class['Funding Per Student'].corr(mid_class['Average Math Score'], method='pearson')
    truth = corr > 0
    if truth:
        expl = f"Pearson correlation between funding and math scores is {corr:.2f}, which is positive."
    else:
        expl = f"Pearson correlation is {corr:.2f}, not positive."
    return truth, expl

Statement 13:

def stmt_13(df):
    """13. All districts with average reading scores above 630 have funding per student exceeding $12,000."""
    high_reading = df[df['Average Reading Score'] > 630]
    condition = high_reading['Funding Per Student'] > 12000
    truth = condition.all() if not high_reading.empty else True
    if truth:
        expl = f"All {len(high_reading)} districts with reading scores >630 have funding >$12,000."
    else:
        viol = high_reading[~condition]
        expl = f"{len(viol)} districts violate the rule (funding: {', '.join(map(str, viol['Funding Per Student'].tolist()))})."
    return truth, expl

Statement 14:

def stmt_14(df):
    """14. Districts in Pennsylvania with average class sizes above 26 have average math scores below 590."""
    pa_districts = df[df['State'] == 'Pennsylvania']
    large_class_pa = pa_districts[pa_districts['Average Class Size'] > 26]
    condition = large_class_pa['Average Math Score'] < 590
    truth = condition.all() if not large_class_pa.empty else True
    if truth:
        expl = f"All {len(large_class_pa)} Pennsylvania districts with class size >26 have math scores <590."
    else:
        viol = large_class_pa[~condition]
        expl = f"{len(viol)} districts violate the rule (math scores: {', '.join(map(str, viol['Average Math Score'].tolist()))})."
    return truth, expl

Statement 15:

def stmt_15(df):
    """15. Districts with percentage free lunch below 15% have average math scores exceeding 610, while those with percentages above 30% have scores below 550."""
    low_free_lunch = df[df['Percentage Free Lunch'] < 15]
    high_free_lunch = df[df['Percentage Free Lunch'] > 30]
    # Check low free lunch
    low_condition = low_free_lunch['Average Math Score'] > 610
    low_truth = low_condition.all() if not low_free_lunch.empty else True
    # Check high free lunch
    high_condition = high_free_lunch['Average Math Score'] < 550
    high_truth = high_condition.all() if not high_free_lunch.empty else True
    overall_truth = low_truth and high_truth
    expl_parts = []
    if not low_truth:
        viol_low = low_free_lunch[~low_condition]
        expl_parts.append(f"Low free lunch districts: {len(viol_low)} have math scores <=610 (e.g., {', '.join(map(str, viol_low['Average Math Score'].tolist()))}).")
    if not high_truth:
        viol_high = high_free_lunch[~high_condition]
        expl_parts.append(f"High free lunch districts: {len(viol_high)} have math scores >=550 (e.g., {', '.join(map(str, viol_high['Average Math Score'].tolist()))}).")
    if not expl_parts:
        expl = "All low free lunch districts have math scores >610 and high free lunch districts have scores <550."
    else:
        expl = "Violations found: " + "; ".join(expl_parts)
    return overall_truth, expl

Now, putting all these functions into the code.

Also, in the main function, after reading the CSV, convert the necessary columns to numeric.

So in the main function:

def main():
    df = pd.read_csv("Qwen/a.LLM_Tables/table_1.csv")
    # Convert numeric columns
    numeric_cols = [
        'Number of Students',
        'Average Class Size',
        'Percentage Free Lunch',
        'Average Math Score',
        'Average Reading Score',
        'Funding Per Student'
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    # Drop rows with NaN in relevant columns? Or proceed as is?
    # Assuming that the data is clean, but if there are NaNs, they will be handled in the checks.
    # For example, if a district has NaN in Funding Per Student, it will be excluded from the checks.
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

But need to make sure that the functions are defined correctly.

Now, putting all together.

Also, the print_result function is as given in the example.

Now, the code should handle all statements.

Potential issues:

- The columns must be named exactly as specified. For example, 'Funding Per Student' must match the CSV's column name. Also, the code uses 'State' to filter for California, Texas, etc.

- The code uses 'Average Math Score' and 'Average Reading Score' columns.

- The code uses 'Percentage Free Lunch' column.

- The code uses 'Average Class Size'.

- The code uses 'Number of Students'.

Now, the code is written.
</think>

import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All districts with funding per student exceeding $12,000 have average math scores above 600."""
    high_funding = df[df["Funding Per Student"] > 12000]
    condition = high_funding["Average Math Score"] > 600
    truth = condition.all() if not high_funding.empty else True
    if truth:
        expl = f"All {len(high_funding)} districts with funding >$12,000 have math scores above 600."
    else:
        viol = high_funding[~condition]
        expl = f"{len(viol)} districts violate the rule (math scores: {', '.join(map(str, viol['Average Math Score'].tolist()))})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. Districts in California with funding per student above $12,000 have average math scores higher than those with funding below $10,000."""
    ca_df = df[df["State"] == "California"]
    high_funding = ca_df[ca_df["Funding Per Student"] > 12000]
    low_funding = ca_df[ca_df["Funding Per Student"] < 10000]
    if high_funding.empty or low_funding.empty:
        truth = True
        expl = "No applicable districts in one or both groups."
    else:
        max_low = low_funding["Average Math Score"].max()
        min_high = high_funding["Average Math Score"].min()
        truth = min_high > max_low
        if truth:
            expl = f"Minimum math score in high funding group ({min_high}) exceeds maximum in low funding group ({max_low})."
        else:
            expl = f"Minimum high funding math score ({min_high}) is not higher than maximum low funding math score ({max_low})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a district’s average class size exceeds 25, its percentage free lunch is always above 25%."""
    large_class = df[df["Average Class Size"] > 25]
    condition = large_class["Percentage Free Lunch"] > 25
    truth = condition.all() if not large_class.empty else True
    if truth:
        expl = f"All {len(large_class)} districts with class size >25 have free lunch >25%."
    else:
        viol = large_class[~condition]
        expl = f"{len(viol)} districts violate the rule (free lunch percentages: {', '.join(map(str, viol['Percentage Free Lunch'].tolist()))})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For districts in Texas, average math scores are consistently below 600, while districts in New York have scores above 610."""
    texas = df[df["State"] == "Texas"]
    new_york = df[df["State"] == "New York"]
    texas_condition = texas["Average Math Score"] < 600
    ny_condition = new_york["Average Math Score"] > 610
    texas_truth = texas_condition.all() if not texas.empty else True
    ny_truth = ny_condition.all() if not new_york.empty else True
    overall_truth = texas_truth and ny_truth
    expl_parts = []
    if not texas_truth:
        viol_texas = texas[~texas_condition]
        expl_parts.append(f"Texas: {len(viol_texas)} districts have math scores >=600 (e.g., {', '.join(map(str, viol_texas['Average Math Score'].tolist()))}).")
    if not ny_truth:
        viol_ny = new_york[~ny_condition]
        expl_parts.append(f"New York: {len(viol_ny)} districts have math scores <=610 (e.g., {', '.join(map(str, viol_ny['Average Math Score'].tolist()))}).")
    if not expl_parts:
        expl = "All Texas districts have math scores <600 and all New York districts have scores >610."
    else:
        expl = "Violations found: " + "; ".join(expl_parts)
    return overall_truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Districts with funding per student below $9,000 have average math scores lower than districts with funding above $10,000."""
    low_funding = df[df["Funding Per Student"] < 9000]
    high_funding = df[df["Funding Per Student"] > 10000]
    if low_funding.empty or high_funding.empty:
        truth = True
        expl = "No applicable districts in one or both groups."
    else:
        max_low = low_funding["Average Math Score"].max()
        min_high = high_funding["Average Math Score"].min()
        truth = max_low < min_high
        if truth:
            expl = f"Maximum math score in low funding group ({max_low}) is less than minimum in high funding group ({min_high})."
        else:
            expl = f"Maximum low funding math score ({max_low}) is not less than minimum high funding math score ({min_high})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. In districts where percentage free lunch exceeds 30%, average math scores are strictly below 570."""
    high_free_lunch = df[df["Percentage Free Lunch"] > 30]
    condition = high_free_lunch["Average Math Score"] < 570
    truth = condition.all() if not high_free_lunch.empty else True
    if truth:
        expl = f"All {len(high_free_lunch)} districts with free lunch >30% have math scores <570."
    else:
        viol = high_free_lunch[~condition]
        expl = f"{len(viol)} districts violate the rule (math scores: {', '.join(map(str, viol['Average Math Score'].tolist()))})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All districts with average class sizes below 23 have funding per student exceeding $10,000."""
    small_class = df[df["Average Class Size"] < 23]
    condition = small_class["Funding Per Student"] > 10000
    truth = condition.all() if not small_class.empty else True
    if truth:
        expl = f"All {len(small_class)} districts with class size <23 have funding >$10,000."
    else:
        viol = small_class[~condition]
        expl = f"{len(viol)} districts violate the rule (funding: {', '.join(map(str, viol['Funding Per Student'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. For districts in Illinois, average math scores are inversely correlated with percentage free lunch (higher free lunch percentages correspond to lower scores)."""
    illinois = df[df["State"] == "Illinois"]
    if illinois.empty:
        truth = True
        expl = "No districts in Illinois."
        return truth, expl
    if len(illinois) < 2:
        truth = True
        expl = "Only one district in Illinois; insufficient data to determine correlation."
        return truth, expl
    corr = illinois["Percentage Free Lunch"].corr(illinois["Average Math Score"], method="pearson")
    truth = corr < 0
    if truth:
        expl = f"Pearson correlation between free lunch and math scores in Illinois is {corr:.2f}, which is negative."
    else:
        expl = f"Pearson correlation in Illinois is {corr:.2f}, not negative."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Districts with over 20,000 students have average math scores below 570, while districts with fewer than 10,000 students have scores above 580."""
    large_districts = df[df["Number of Students"] > 20000]
    small_districts = df[df["Number of Students"] < 10000]
    large_condition = large_districts["Average Math Score"] < 570
    small_condition = small_districts["Average Math Score"] > 580
    large_truth = large_condition.all() if not large_districts.empty else True
    small_truth = small_condition.all() if not small_districts.empty else True
    overall_truth = large_truth and small_truth
    expl_parts = []
    if not large_truth:
        viol_large = large_districts[~large_condition]
        expl_parts.append(f"Large districts: {len(viol_large)} have math scores >=570 (e.g., {', '.join(map(str, viol_large['Average Math Score'].tolist()))}).")
    if not small_truth:
        viol_small = small_districts[~small_condition]
        expl_parts.append(f"Small districts: {len(viol_small)} have math scores <=580 (e.g., {', '.join(map(str, viol_small['Average Math Score'].tolist()))}).")
    if not expl_parts:
        expl = "All large districts have math scores <570 and all small districts have scores >580."
    else:
        expl = "Violations found: " + "; ".join(expl_parts)
    return overall_truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a district’s funding per student is between $10,000 and $12,000, its average math score is between 590 and 610."""
    mid_funding = df[(df["Funding Per Student"] >= 10000) & (df["Funding Per Student"] <= 12000)]
    condition = mid_funding["Average Math Score"].between(590, 610, inclusive="both")
    truth = condition.all() if not mid_funding.empty else True
    if truth:
        expl = f"All {len(mid_funding)} districts with funding between $10k–$12k have math scores between 590–610."
    else:
        viol = mid_funding[~condition]
        expl = f"{len(viol)} districts violate the rule (math scores: {', '.join(map(str, viol['Average Math Score'].tolist()))})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Districts in Ohio with funding per student above $11,000 have average math scores exceeding 600, while those with lower funding have scores below 600."""
    ohio = df[df["State"] == "Ohio"]
    high_funding = ohio[ohio["Funding Per Student"] > 11000]
    low_funding = ohio[ohio["Funding Per Student"] <= 11000]
    high_condition = high_funding["Average Math Score"] > 600
    low_condition = low_funding["Average Math Score"] < 600
    high_truth = high_condition.all() if not high_funding.empty else True
    low_truth = low_condition.all() if not low_funding.empty else True
    overall_truth = high_truth and low_truth
    expl_parts = []
    if not high_truth:
        viol_high = high_funding[~high_condition]
        expl_parts.append(f"High funding Ohio districts: {len(viol_high)} have math scores <=600 (e.g., {', '.join(map(str, viol_high['Average Math Score'].tolist()))}).")
    if not low_truth:
        viol_low = low_funding[~low_condition]
        expl_parts.append(f"Low funding Ohio districts: {len(viol_low)} have math scores >=600 (e.g., {', '.join(map(str, viol_low['Average Math Score'].tolist()))}).")
    if not expl_parts:
        expl = "All Ohio districts with high funding have math scores >600 and low funding have scores <600."
    else:
        expl = "Violations found: " + "; ".join(expl_parts)
    return overall_truth, expl

def stmt_12(df: pd.DataFrame):
    """12. For districts where average class size is between 24 and 26, funding per student is positively correlated with average math scores."""
    mid_class = df[(df["Average Class Size"] >= 24) & (df["Average Class Size"] <= 26)]
    if mid_class.empty:
        truth = True
        expl = "No districts with average class size between 24–26."
        return truth, expl
    if len(mid_class) < 2:
        truth = True
        expl = "Only one district in the class size range; insufficient data for correlation."
        return truth, expl
    corr = mid_class["Funding Per Student"].corr(mid_class["Average Math Score"], method="pearson")
    truth = corr > 0
    if truth:
        expl = f"Pearson correlation between funding and math scores is {corr:.2f}, which is positive."
    else:
        expl = f"Pearson correlation is {corr:.2f}, not positive."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All districts with average reading scores above 630 have funding per student exceeding $12,000."""
    high_reading = df[df["Average Reading Score"] > 630]
    condition = high_reading["Funding Per Student"] > 12000
    truth = condition.all() if not high_reading.empty else True
    if truth:
        expl = f"All {len(high_reading)} districts with reading scores >630 have funding >$12,000."
    else:
        viol = high_reading[~condition]
        expl = f"{len(viol)} districts violate the rule (funding: {', '.join(map(str, viol['Funding Per Student'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Districts in Pennsylvania with average class sizes above 26 have average math scores below 590."""
    pa_districts = df[df["State"] == "Pennsylvania"]
    large_class_pa = pa_districts[pa_districts["Average Class Size"] > 26]
    condition = large_class_pa["Average Math Score"] < 590
    truth = condition.all() if not large_class_pa.empty else True
    if truth:
        expl = f"All {len(large_class_pa)} Pennsylvania districts with class size >26 have math scores <590."
    else:
        viol = large_class_pa[~condition]
        expl = f"{len(viol)} districts violate the rule (math scores: {', '.join(map(str, viol['Average Math Score'].tolist()))})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Districts with percentage free lunch below 15% have average math scores exceeding 610, while those with percentages above 30% have scores below 550."""
    low_free_lunch = df[df["Percentage Free Lunch"] < 15]
    high_free_lunch = df[df["Percentage Free Lunch"] > 30]
    low_condition = low_free_lunch["Average Math Score"] > 610
    high_condition = high_free_lunch["Average Math Score"] < 550
    low_truth = low_condition.all() if not low_free_lunch.empty else True
    high_truth = high_condition.all() if not high_free_lunch.empty else True
    overall_truth = low_truth and high_truth
    expl_parts = []
    if not low_truth:
        viol_low = low_free_lunch[~low_condition]
        expl_parts.append(f"Low free lunch districts: {len(viol_low)} have math scores <=610 (e.g., {', '.join(map(str, viol_low['Average Math Score'].tolist()))}).")
    if not high_truth:
        viol_high = high_free_lunch[~high_condition]
        expl_parts.append(f"High free lunch districts: {len(viol_high)} have math scores >=550 (e.g., {', '.join(map(str, viol_high['Average Math Score'].tolist()))}).")
    if not expl_parts:
        expl = "All low free lunch districts have math scores >610 and high free lunch districts have scores <550."
    else:
        expl = "Violations found: " + "; ".join(expl_parts)
    return overall_truth, expl

def main():
    df = pd.read_csv("Qwen/a.LLM_Tables/table_1.csv")
    numeric_cols = [
        "Number of Students",
        "Average Class Size",
        "Percentage Free Lunch",
        "Average Math Score",
        "Average Reading Score",
        "Funding Per Student"
    ]
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