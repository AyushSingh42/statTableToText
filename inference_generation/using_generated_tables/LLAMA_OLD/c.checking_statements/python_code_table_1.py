import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. Cities with a Bachelor's degree as the Education Level have a lower Unemployment Rate than those with Some college or High school."""
    bachelors = df[df["Education Level"] == "Bachelor's degree"]
    others = df[df["Education Level"]!= "Bachelor's degree"]
    truth = bachelors["Unemployment Rate"].mean() < others["Unemployment Rate"].mean()
    if truth:
        expl = f"Cities with a Bachelor's degree have a lower average Unemployment Rate ({bachelors['Unemployment Rate'].mean():.2f}) than others ({others['Unemployment Rate'].mean():.2f})."
    else:
        expl = f"Cities with a Bachelor's degree do not have a lower average Unemployment Rate ({bachelors['Unemployment Rate'].mean():.2f}) than others ({others['Unemployment Rate'].mean():.2f})."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a city has a Median Income above 60000, then it is located in the West or Northeast region."""
    high_income = df[df["Median Income"] > 60000]
    truth = (high_income["Region"] == "West").any() or (high_income["Region"] == "Northeast").any()
    if truth:
        expl = f"All cities with a Median Income above 60000 are located in the West or Northeast region."
    else:
        viol = high_income[~((high_income["Region"] == "West") | (high_income["Region"] == "Northeast"))]
        expl = f"{len(viol)} cities with a Median Income above 60000 are not located in the West or Northeast region (regions: {', '.join(map(str, viol['Region'].tolist()))})."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. All cities with a Job Type of Management have a higher Median Income than those with a Job Type of Service."""
    management = df[df["Job Type"] == "Management"]
    service = df[df["Job Type"] == "Service"]
    truth = management["Median Income"].mean() > service["Median Income"].mean()
    if truth:
        expl = f"Cities with a Job Type of Management have a higher average Median Income ({management['Median Income'].mean():.2f}) than those with a Job Type of Service ({service['Median Income'].mean():.2f})."
    else:
        expl = f"Cities with a Job Type of Management do not have a higher average Median Income ({management['Median Income'].mean():.2f}) than those with a Job Type of Service ({service['Median Income'].mean():.2f})."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Cities with a Commute Time of 45 have a higher Median Income than those with a Commute Time of 30 or 35."""
    commute_45 = df[df["Commute Time"] == 45]
    commute_30_35 = df[(df["Commute Time"] == 30) | (df["Commute Time"] == 35)]
    truth = commute_45["Median Income"].mean() > commute_30_35["Median Income"].mean()
    if truth:
        expl = f"Cities with a Commute Time of 45 have a higher average Median Income ({commute_45['Median Income'].mean():.2f}) than those with a Commute Time of 30 or 35 ({commute_30_35['Median Income'].mean():.2f})."
    else:
        expl = f"Cities with a Commute Time of 45 do not have a higher average Median Income ({commute_45['Median Income'].mean():.2f}) than those with a Commute Time of 30 or 35 ({commute_30_35['Median Income'].mean():.2f})."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. The South region has a higher proportion of cities with a Job Type of Service than the other regions."""
    south = df[df["Region"] == "South"]
    service_south = south[south["Job Type"] == "Service"]
    proportion_south = len(service_south) / len(south)
    other_regions = df[df["Region"]!= "South"]
    service_other = other_regions[other_regions["Job Type"] == "Service"]
    proportion_other = len(service_other) / len(other_regions)
    truth = proportion_south > proportion_other
    if truth:
        expl = f"The South region has a higher proportion ({proportion_south:.2f}) of cities with a Job Type of Service than the other regions ({proportion_other:.2f})."
    else:
        expl = f"The South region does not have a higher proportion ({proportion_south:.2f}) of cities with a Job Type of Service than the other regions ({proportion_other:.2f})."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Cities with a Population above 2000000 have a lower Unemployment Rate than those with a Population below 2000000."""
    large_population = df[df["Population"] > 2000000]
    small_population = df[df["Population"] <= 2000000]
    truth = large_population["Unemployment Rate"].mean() < small_population["Unemployment Rate"].mean()
    if truth:
        expl = f"Cities with a Population above 2000000 have a lower average Unemployment Rate ({large_population['Unemployment Rate'].mean():.2f}) than those with a Population below 2000000 ({small_population['Unemployment Rate'].mean():.2f})."
    else:
        expl = f"Cities with a Population above 2000000 do not have a lower average Unemployment Rate ({large_population['Unemployment Rate'].mean():.2f}) than those with a Population below 2000000 ({small_population['Unemployment Rate'].mean():.2f})."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. If a city has a Median Income above 70000, then it is located in the West region."""
    high_income = df[df["Median Income"] > 70000]
    truth = (high_income["Region"] == "West").all()
    if truth:
        expl = f"All cities with a Median Income above 70000 are located in the West region."
    else:
        viol = high_income[~(high_income["Region"] == "West")]
        expl = f"{len(viol)} cities with a Median Income above 70000 are not located in the West region (regions: {', '.join(map(str, viol['Region'].tolist()))})."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. All cities with a Job Type of Sales have a Commute Time of 30."""
    sales = df[df["Job Type"] == "Sales"]
    truth = (sales["Commute Time"] == 30).all()
    if truth:
        expl = f"All cities with a Job Type of Sales have a Commute Time of 30."
    else:
        viol = sales[~(sales["Commute Time"] == 30)]
        expl = f"{len(viol)} cities with a Job Type of Sales do not have a Commute Time of 30 (commute times: {', '.join(map(str, viol['Commute Time'].tolist()))})."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. Cities with a Bachelor's degree as the Education Level have a higher Median Income than those with Some college or High school."""
    bachelors = df[df["Education Level"] == "Bachelor's degree"]
    others = df[df["Education Level"]!= "Bachelor's degree"]
    truth = bachelors["Median Income"].mean() > others["Median Income"].mean()
    if truth:
        expl = f"Cities with a Bachelor's degree have a higher average Median Income ({bachelors['Median Income'].mean():.2f}) than others ({others['Median Income'].mean():.2f})."
    else:
        expl = f"Cities with a Bachelor's degree do not have a higher average Median Income ({bachelors['Median Income'].mean():.2f}) than others ({others['Median Income'].mean():.2f})."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. The Northeast region has a higher proportion of cities with a Job Type of Management than the other regions."""
    northeast = df[df["Region"] == "Northeast"]
    management_northeast = northeast[northeast["Job Type"] == "Management"]
    proportion_northeast = len(management_northeast) / len(northeast)
    other_regions = df[df["Region"]!= "Northeast"]
    management_other = other_regions[other_regions["Job Type"] == "Management"]
    proportion_other = len(management_other) / len(other_regions)
    truth = proportion_northeast > proportion_other
    if truth:
        expl = f"The Northeast region has a higher proportion ({proportion_northeast:.2f}) of cities with a Job Type of Management than the other regions ({proportion_other:.2f})."
    else:
        expl = f"The Northeast region does not have a higher proportion ({proportion_northeast:.2f}) of cities with a Job Type of Management than the other regions ({proportion_other:.2f})."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Cities with a Unemployment Rate below 4 have a higher Median Income than those with a Unemployment Rate above 4."""
    low_unemployment = df[df["Unemployment Rate"] < 4]
    high_unemployment = df[df["Unemployment Rate"] >= 4]
    truth = low_unemployment["Median Income"].mean() > high_unemployment["Median Income"].mean()
    if truth:
        expl = f"Cities with a Unemployment Rate below 4 have a higher average Median Income ({low_unemployment['Median Income'].mean():.2f}) than those with a Unemployment Rate above 4 ({high_unemployment['Median Income'].mean():.2f})."
    else:
        expl = f"Cities with a Unemployment Rate below 4 do not have a higher average Median Income ({low_unemployment['Median Income'].mean():.2f}) than those with a Unemployment Rate above 4 ({high_unemployment['Median Income'].mean():.2f})."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. If a city has a Population above 1500000 and a Job Type of Management, then it is located in the West or Northeast region."""
    large_population = df[df["Population"] > 1500000]
    management = large_population[large_population["Job Type"] == "Management"]
    truth = (management["Region"] == "West").any() or (management["Region"] == "Northeast").any()
    if truth:
        expl = f"All cities with a Population above 1500000 and a Job Type of Management are located in the West or Northeast region."
    else:
        viol = management[~((management["Region"] == "West") | (management["Region"] == "Northeast"))]
        expl = f"{len(viol)} cities with a Population above 1500000 and a Job Type of Management are not located in the West or Northeast region (regions: {', '.join(map(str, viol['Region'].tolist()))})."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. All cities with a Commute Time of 45 have a Job Type of Management."""
    commute_45 = df[df["Commute Time"] == 45]
    truth = (commute_45["Job Type"] == "Management").all()
    if truth:
        expl = f"All cities with a Commute Time of 45 have a Job Type of Management."
    else:
        viol = commute_45[~(commute_45["Job Type"] == "Management")]
        expl = f"{len(viol)} cities with a Commute Time of 45 do not have a Job Type of Management (job types: {', '.join(map(str, viol['Job Type'].tolist()))})."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. Cities with a Median Income above 50000 have a lower Unemployment Rate than those with a Median Income below 50000."""
    high_income = df[df["Median Income"] > 50000]
    low_income = df[df["Median Income"] <= 50000]
    truth = high_income["Unemployment Rate"].mean() < low_income["Unemployment Rate"].mean()
    if truth:
        expl = f"Cities with a Median Income above 50000 have a lower average Unemployment Rate ({high_income['Unemployment Rate'].mean():.2f}) than those with a Median Income below 50000 ({low_income['Unemployment Rate'].mean():.2f})."
    else:
        expl = f"Cities with a Median Income above 50000 do not have a lower average Unemployment Rate ({high_income['Unemployment Rate'].mean():.2f}) than those with a Median Income below 50000 ({low_income['Unemployment Rate'].mean():.2f})."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. The West region has a higher proportion of cities with a Job Type of Sales than the other regions."""
    west = df[df["Region"] == "West"]
    sales_west = west[west["Job Type"] == "Sales"]
    proportion_west = len(sales_west) / len(west)
    other_regions = df[df["Region"]!= "West"]
    sales_other = other_regions[other_regions["Job Type"] == "Sales"]
    proportion_other = len(sales_other) / len(other_regions)
    truth = proportion_west > proportion_other
    if truth:
        expl = f"The West region has a higher proportion ({proportion_west:.2f}) of cities with a Job Type of Sales than the other regions ({proportion_other:.2f})."
    else:
        expl = f"The West region does not have a higher proportion ({proportion_west:.2f}) of cities with a Job Type of Sales than the other regions ({proportion_other:.2f})."
    return truth, expl

def main():
    df = pd.read_csv("a.LLM_Tables/table_1.csv")
    checks = [(1, stmt_1), (2, stmt_2), (3, stmt_3), (4, stmt_4), (5, stmt_5), (6, stmt_6), (7, stmt_7), (8, stmt_8), (9, stmt_9), (10, stmt_10), (11, stmt_11), (12, stmt_12), (13, stmt_13), (14, stmt_14), (15, stmt_15)]
    for num, func in checks:
        truth, explanation = func(df)
        print_result(num, func.__doc__.strip(), truth, explanation)

if __name__ == "__main__":
    main()