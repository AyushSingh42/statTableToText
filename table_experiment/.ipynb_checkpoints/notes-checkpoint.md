# Findings from the Table Prompting Experiment

The following models were used in this experiment:
- Gemma 4 31B
- Llama 3.1 70B
- Qwen 3 32B

The file structure for the directory is as follows:

table_experiment/
├── table_prompting.ipynb
├── table_tests/
│   ├── google/gemma-4-31B/
│   │   └──table_0-5.csv
│   ├── meta-llama/Llama-3.1-70B-Instruct
│   │   └──table_0-5.csv
│   └── Qwen/Qwen3-32B
│   │   └──table_0-5.csv
└── notes.md

Of the three, only Qwen is a thinking model and it was the only one to output thinking tokens (this did corrupt the table as something went wrong in parsing). All three models were asked to generate five tables in order to see if they would simply copy an example table if it was provided. For this process, the following prompt was used:

You are a careful researcher who generates clean, realistic synthetic statistical tables.
Generate exactly one synthetic statistical table in valid CSV format.

Requirements:
1. The table must have between 5 and 10 columns.
2. The table must contain exactly 15 data rows, plus 1 header row.
3. Invent realistic column names. Include a mix of:
   - numeric columns (integers and/or floats)
   - Numeric columns must contain only plain numbers (no $, commas, or % symbols)
   - categorical columns
4. Make the data look plausible for a real-world dataset.
5. Ensure values are varied across rows.
6. All rows must have the same number of columns as the header.
7. Do not include commas inside cell values.
8. Do not include explanations, markdown, code fences, titles, or any text before or after the CSV.
9. Output only the CSV table.

The dataset can be about any realistic domain such as health, education, business, transportation, or demographics.

Here is an example table in CSV format:
id,gender,age,height_cm,weight_kg,bmi,annual_income_$k,sleep_hours,resting_hr_bpm,avg_steps_day
P001,man,26,177.5,68.4,21.7,62.9,7.3,70,5542
P002,woman,42,151.2,55.1,24.1,50.9,7.3,58,6695
P003,woman,27,155.0,64.9,27.0,63.1,7.0,81,9534
P004,woman,21,164.2,80.6,29.9,20.1,6.8,78,4423
P005,man,56,181.2,76.5,23.3,53.2,5.6,78,8069
P006,man,35,177.2,77.6,24.7,73.0,6.6,61,10768
P007,man,39,175.2,62.9,20.5,135.3,6.7,84,3481
P008,woman,21,161.2,52.2,20.1,45.1,6.2,56,7962
P009,woman,31,154.1,69.3,29.2,38.5,6.8,76,8150
P010,woman,39,158.7,79.6,31.6,45.5,7.4,92,9455
P011,man,24,172.8,75.2,25.2,99.3,8.9,60,4408
P012,woman,43,169.3,86.0,30.0,71.9,7.2,64,4199
P013,woman,31,165.1,73.9,27.1,44.8,7.3,71,8805
P014,man,34,163.7,60.6,22.6,79.6,6.9,65,8242
P015,man,31,178.3,86.2,27.1,63.3,5.1,54,8126
P016,man,60,173.3,97.3,32.4,102.2,7.0,71,8366
P017,man,38,171.3,74.2,25.3,40.8,7.1,59,5800
P018,woman,25,166.7,90.3,32.5,50.1,9.5,75,8081
P019,man,48,183.2,58.7,17.5,48.4,6.8,61,8233
P020,man,23,182.5,97.3,29.2,26.8,7.3,85,5714


## Gemma 4 31B

This model failed at the task. All five tables that were generated were identical. It continued with the same categories as the example but it generated a "P021" as a continuation. The issue was that this additional data row was used as the header for all columns. Every row after that then had identical entries, meaning every single row in all five of Gemma's tables looked like this:

1	P022	man	25	171.2	75.1	25.7	101.1	7.1	61	5111

The number in P0xx would increase but all of the data were exactly the same. I am not quite ready to give up on Gemma 4 as I have heard that it is an extremely capable model but I do think it needs more testing when not provided with an example.

## Llama 3.1 70B

Llama performed much better at the task than Gemma, but still has a major shortcoming. Just like Gemma, it generated P021 but used that as a the column headers instead of having real ones and like Gemma it tried to continue the same type of table as the example. Unlike Gemma, all of the row entries are distinct so every person P0xx in the table is different and is a usable data point. Unfortunately, all five of Llama's tables are identical. This is better than all of the rows being identical but it is still not ideal.

## Qwen 3 32B

Qwen had very similar issues to Llama where it generated five of the same exact table but they were distinct tables. Unlike Llama, Qwen did generate unique data. Oddly enough, it started off by generating more people with IDs P021 - P030. For some reason, it then switched to generating data with a completely different sent of headers. It also started thinking again in the middle of generation but it did not mark this with thinking tags (<think> and </think>) so these were not parsed out. Another thing to note is that the "new" generation that Qwen did was the same North, South, East, and West categories that we have been seeing it generate the whole time.

# Summary

Overall, I do not think that Qwen can really generate tables with this prompt. There may be different results if an example is not provided as it would lead to the thinking traces not happening in the middle of generation. Gemma also seems very unfit for this as it generated tables that were the same thing over and over again. Llama did the best as it did generate novel data but it only did this once and then used the same generation in all five trials.

Further work will include repeated generation using a prompt that does not provide an example table. One thing that could be worth exploring is providing the model with a category and asking it to use that in order to generate data. 