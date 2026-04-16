

import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All industrial zone sensors have PM25 levels exceeding 30 µg/m³ and noise levels above 72 dB."""
    industrial = df[df['zone'] == 'industrial']
    cond = (industrial['pm25'] > 30) & (industrial['noise_db'] > 72)
    truth = cond.all() if not industrial.empty else True
    if truth:
        expl = f"All {len(industrial)} industrial sensors meet PM25>30 and noise>72."
    else:
        viol = industrial[~cond]
        expl = f"{len(viol)} industrial sensors violate the rule."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. In residential zones, PM25 levels are consistently below 14 µg/m³ and noise levels remain under 53 dB."""
    residential = df[df['zone'] =='residential']
    cond = (residential['pm25'] < 14) & (residential['noise_db'] < 53)
    truth = cond.all() if not residential.empty else True
    if truth:
        expl = f"All {len(residential)} residential sensors meet PM25<14 and noise<53."
    else:
        viol = residential[~cond]
        expl = f"{len(viol)} residential sensors violate the rule."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. If a sensor is located in a downtown zone, its foot traffic exceeds 1200 people per hour."""
    downtown = df[df['zone'] == 'downtown']
    cond = downtown['foot_traffic'] > 1200
    truth = cond.all() if not downtown.empty else True
    if truth:
        expl = f"All {len(downtown)} downtown sensors have foot traffic >1200."
    else:
        viol = downtown[~cond]
        expl = f"{len(viol)} downtown sensors violate the rule."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. Park zones exhibit the lowest power consumption (≤123.9 kWh) and the highest humidity levels (≥64.8%)."""
    park = df[df['zone'] == 'park']
    cond1 = park['power_use_kwh'] <= 123.9
    cond2 = park['avg_humidity'] >= 64.8
    truth = cond1.all() and cond2.all() if not park.empty else True
    if truth:
        expl = f"All {len(park)} park sensors meet power_use_kwh≤123.9 and humidity≥64.8."
    else:
        viol1 = park[~cond1] if not park.empty else pd.DataFrame()
        viol2 = park[~cond2] if not park.empty else pd.DataFrame()
        expl = f"{len(viol1)} park sensors violate power_use_kwh condition, {len(viol2)} violate humidity condition."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. For industrial sensors, power use increases as PM25 levels rise (r = 0.98 between PM25 and power use)."""
    industrial = df[df['zone'] == 'industrial']
    if industrial.empty:
        expl = "No industrial sensors to evaluate correlation."
        return True, expl
    pm25 = industrial['pm25']
    power = industrial['power_use_kwh']
    if len(pm25) < 2:
        expl = "Insufficient data points for correlation calculation."
        return False, expl
    corr = pm25.corr(power, method='pearson')
    truth = not pd.isna(corr) and corr >= 0.98
    expl = f"Correlation between PM25 and power use in industrial zones is {corr:.2f}."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. Downtown sensors have both higher average temperatures (>24.6°C) and higher foot traffic (>1240) compared to residential zones."""
    downtown = df[df['zone'] == 'downtown']
    cond_temp = downtown['avg_temp_c'] > 24.6
    cond_ft = downtown['foot_traffic'] > 1240
    truth = cond_temp.all() and cond_ft.all() if not downtown.empty else True
    if truth:
        expl = f"All {len(downtown)} downtown sensors meet temp>24.6 and ft>1240."
    else:
        viol_temp = downtown[~cond_temp] if not downtown.empty else pd.DataFrame()
        viol_ft = downtown[~cond_ft] if not downtown.empty else pd.DataFrame()
        expl = f"{len(viol_temp)} sensors violate temp condition, {len(viol_ft)} violate ft condition."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All sensors with PM25 > 30 µg/m³ belong exclusively to industrial zones."""
    high_pm25 = df[df['pm25'] > 30]
    cond = high_pm25['zone'] == 'industrial'
    truth = cond.all() if not high_pm25.empty else True
    if truth:
        expl = f"All {len(high_pm25)} sensors with PM25>30 are in industrial zones."
    else:
        viol = high_pm25[~cond]
        expl = f"{len(viol)} sensors with PM25>30 are not in industrial zones."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. Residential zones have the lowest average temperatures (≤24.2°C) but the highest humidity levels (≥60.3%)."""
    residential = df[df['zone'] =='residential']
    cond1 = residential['avg_temp_c'] <= 24.2
    cond2 = residential['avg_humidity'] >= 60.3
    truth = cond1.all() and cond2.all() if not residential.empty else True
    if truth:
        expl = f"All {len(residential)} residential sensors meet temp≤24.2 and humidity≥60.3."
    else:
        viol1 = residential[~cond1] if not residential.empty else pd.DataFrame()
        viol2 = residential[~cond2] if not residential.empty else pd.DataFrame()
        expl = f"{len(viol1)} sensors violate temp condition, {len(viol2)} violate humidity condition."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. If a sensor’s noise level exceeds 70 dB, it must belong to an industrial or downtown zone."""
    high_noise = df[df['noise_db'] > 70]
    cond = high_noise['zone'].isin(['industrial', 'downtown'])
    truth = cond.all() if not high_noise.empty else True
    if truth:
        expl = f"All {len(high_noise)} sensors with noise>70 are in industrial or downtown zones."
    else:
        viol = high_noise[~cond]
        expl = f"{len(viol)} sensors with noise>70 are not in industrial or downtown zones."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. In downtown zones, power use increases by approximately 0.1 kWh per additional foot traffic unit (r = 0.95)."""
    downtown = df[df['zone'] == 'downtown']
    if downtown.empty:
        expl = "No downtown sensors to evaluate correlation."
        return True, expl
    power = downtown['power_use_kwh']
    foot_traffic = downtown['foot_traffic']
    if len(power) < 2:
        expl = "Insufficient data points for correlation calculation."
        return False, expl
    corr = power.corr(foot_traffic, method='pearson')
    truth = not pd.isna(corr) and corr >= 0.95
    expl = f"Correlation between power use and foot traffic in downtown zones is {corr:.2f}."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Park sensors have the lowest PM25 levels (≤9.8 µg/m³) but higher foot traffic (≥689) than residential zones."""
    park = df[df['zone'] == 'park']
    residential = df[df['zone'] =='residential']
    cond1 = True
    cond2 = True
    if not park.empty:
        cond1 = (park['pm25'] <= 9.8).all()
        cond2 = (park['foot_traffic'] >= 689).all()
    cond3 = True
    if not park.empty and not residential.empty:
        park_min_ft = park['foot_traffic'].min()
        residential_max_ft = residential['foot_traffic'].max()
        cond3 = park_min_ft > residential_max_ft
    truth = cond1 and cond2 and cond3
    if truth:
        expl = f"All park sensors meet PM25≤9.8 and ft≥689, and their ft is higher than residential's max."
    else:
        viol1 = park[park['pm25'] > 9.8] if not park.empty else pd.DataFrame()
        viol2 = park[park['foot_traffic'] < 689] if not park.empty else pd.DataFrame()
        expl = f"PM25 violation count: {len(viol1)}, ft violation count: {len(viol2)}, ft comparison violation: {not cond3}"
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. Industrial zones exhibit the highest power use (>428.9 kWh) and the lowest humidity levels (≤53.6%)."""
    industrial = df[df['zone'] == 'industrial']
    cond1 = industrial['power_use_kwh'] > 428.9
    cond2 = industrial['avg_humidity'] <= 53.6
    truth = cond1.all() and cond2.all() if not industrial.empty else True
    if truth:
        expl = f"All {len(industrial)} industrial sensors meet power_use_kwh>428.9 and humidity≤53.6."
    else:
        viol1 = industrial[~cond1] if not industrial.empty else pd.DataFrame()
        viol2 = industrial[~cond2] if not industrial.empty else pd.DataFrame()
        expl = f"{len(viol1)} sensors violate power_use_kwh condition, {len(viol2)} violate humidity condition."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. For residential sensors, higher humidity (>61%) correlates with lower PM25 levels (<12.9 µg/m³)."""
    residential = df[df['zone'] =='residential']
    high_humidity = residential[residential['avg_humidity'] > 61]
    cond = high_humidity['pm25'] < 12.9
    truth = cond.all() if not high_humidity.empty else True
    if truth:
        expl = f"All {len(high_humidity)} residential sensors with humidity>61 have PM25<12.9."
    else:
        viol = high_humidity[~cond]
        expl = f"{len(viol)} residential sensors with humidity>61 have PM25≥12.9."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. All downtown sensors have noise levels exceeding 66 dB, while residential sensors remain below 53 dB."""
    downtown = df[df['zone'] == 'downtown']
    residential = df[df['zone'] =='residential']
    cond_downtown = downtown['noise_db'] > 66
    cond_residential = residential['noise_db'] < 53
    truth_downtown = cond_downtown.all() if not downtown.empty else True
    truth_residential = cond_residential.all() if not residential.empty else True
    truth = truth_downtown and truth_residential
    if truth:
        expl = f"All downtown sensors have noise>66 dB and all residential sensors have noise<53 dB."
    else:
        viol_downtown = downtown[~cond_downtown] if not downtown.empty else pd.DataFrame()
        viol_residential = residential[~cond_residential] if not residential.empty else pd.DataFrame()
        expl = f"{len(viol_downtown)} downtown sensors violate noise>66 dB, {len(viol_residential)} residential sensors violate noise<53 dB."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. Sensors with foot traffic exceeding 1300 people/hour are exclusively located in downtown zones."""
    high_ft = df[df['foot_traffic'] > 1300]
    cond = high_ft['zone'] == 'downtown'
    truth = cond.all() if not high_ft.empty else True
    if truth:
        expl = f"All {len(high_ft)} sensors with foot traffic>1300 are in downtown zones."
    else:
        viol = high_ft[~cond]
        expl = f"{len(viol)} sensors with foot traffic>1300 are not in downtown zones."
    return truth, expl

def main():
    df = pd.read_csv("tables/table_9.csv")
    numeric_cols = ['pm25', 'noise_db', 'foot_traffic', 'power_use_kwh', 'avg_temp_c', 'avg_humidity']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
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