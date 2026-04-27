import pandas as pd

def print_result(statement_no: int, description: str, truth: bool, explanation: str):
    status = "TRUE" if truth else "FALSE"
    print(f"\nStatement {statement_no}: {status}")
    print(f"  - {description}")
    print(f"  - Explanation: {explanation}")

def stmt_1(df: pd.DataFrame):
    """1. All students with a test score greater than 90 have a study time of 4 hours or more per week."""
    condition = (df['test_score'] > 90) & (df['study_hours_week'] < 4)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "No students with test score >90 have study time <4 hours/week."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_2(df: pd.DataFrame):
    """2. If a student is a club member, then their attendance rate is greater than 84%."""
    condition = (df['club_member'] == 'yes') & (df['attendance_rate'] <= 84)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All club members have attendance rate >84%."
    else:
        expl = f"{len(violations)} club members violate the rule."
    return truth, expl

def stmt_3(df: pd.DataFrame):
    """3. There exists at least one student in the 9th grade with a test score greater than 95."""
    condition = (df['grade_level'] == 9) & (df['test_score'] > 95)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 9th grade with test score >95."
    else:
        expl = "No student in 9th grade has test score >95."
    return truth, expl

def stmt_4(df: pd.DataFrame):
    """4. For all students with a study time of 8 hours or more per week, their test score is greater than 78."""
    condition = (df['study_hours_week'] >= 8) & (df['test_score'] <= 78)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with study time >=8 hours have test score >78."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_5(df: pd.DataFrame):
    """5. Most students in the 10th grade have an attendance rate greater than 90%."""
    ten_grade = df[df['grade_level'] == 10]
    if len(ten_grade) == 0:
        truth = False
        expl = "No students in 10th grade."
    else:
        high_attendance = ten_grade[ten_grade['attendance_rate'] > 90]
        proportion = len(high_attendance) / len(ten_grade)
        truth = proportion > 0.5
        expl = f"{len(high_attendance)}/{len(ten_grade)} ({proportion:.2%}) of 10th graders have attendance >90%."
    return truth, expl

def stmt_6(df: pd.DataFrame):
    """6. If a student is in the 12th grade, then their test score is greater than 62."""
    condition = (df['grade_level'] == 12) & (df['test_score'] <= 62)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All 12th graders have test score >62."
    else:
        expl = f"{len(violations)} 12th graders violate the rule."
    return truth, expl

def stmt_7(df: pd.DataFrame):
    """7. All students with a test score less than 80 have a study time of 5 hours or less per week."""
    condition = (df['test_score'] < 80) & (df['study_hours_week'] > 5)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with test score <80 have study time <=5 hours/week."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_8(df: pd.DataFrame):
    """8. There exists at least one student in the 11th grade with a study time of 2 hours or less per week."""
    condition = (df['grade_level'] == 11) & (df['study_hours_week'] <= 2)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 11th grade with study time <=2 hours/week."
    else:
        expl = "No student in 11th grade has study time <=2 hours/week."
    return truth, expl

def stmt_9(df: pd.DataFrame):
    """9. For all students with an attendance rate greater than 95%, their test score is greater than 80."""
    condition = (df['attendance_rate'] > 95) & (df['test_score'] <= 80)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with attendance >95% have test score >80."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_10(df: pd.DataFrame):
    """10. If a student is a club member, then their test score is greater than 80."""
    condition = (df['club_member'] == 'yes') & (df['test_score'] <= 80)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All club members have test score >80."
    else:
        expl = f"{len(violations)} club members violate the rule."
    return truth, expl

def stmt_11(df: pd.DataFrame):
    """11. Most students have a study time of 5 hours or more per week."""
    high_study = df[df['study_hours_week'] >= 5]
    proportion = len(high_study) / len(df)
    truth = proportion > 0.5
    expl = f"{len(high_study)}/{len(df)} ({proportion:.2%}) of students have study time >=5 hours/week."
    return truth, expl

def stmt_12(df: pd.DataFrame):
    """12. All students with a test score greater than 95 have an attendance rate greater than 86%."""
    condition = (df['test_score'] > 95) & (df['attendance_rate'] <= 86)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with test score >95 have attendance >86%."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_13(df: pd.DataFrame):
    """13. There exists at least one student in the 10th grade with a study time of 11 hours or more per week."""
    condition = (df['grade_level'] == 10) & (df['study_hours_week'] >= 11)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 10th grade with study time >=11 hours/week."
    else:
        expl = "No student in 10th grade has study time >=11 hours/week."
    return truth, expl

def stmt_14(df: pd.DataFrame):
    """14. For all students with a study time of 4 hours or less per week, their test score is greater than 77."""
    condition = (df['study_hours_week'] <= 4) & (df['test_score'] <= 77)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with study time <=4 hours have test score >77."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_15(df: pd.DataFrame):
    """15. If a student is in the 9th grade, then their test score is greater than 62."""
    condition = (df['grade_level'] == 9) & (df['test_score'] <= 62)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All 9th graders have test score >62."
    else:
        expl = f"{len(violations)} 9th graders violate the rule."
    return truth, expl

def stmt_16(df: pd.DataFrame):
    """16. All students with an attendance rate greater than 90% have a test score greater than 70."""
    condition = (df['attendance_rate'] > 90) & (df['test_score'] <= 70)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with attendance >90% have test score >70."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_17(df: pd.DataFrame):
    """17. There exists at least one student in the 12th grade with a study time of 9 hours or more per week."""
    condition = (df['grade_level'] == 12) & (df['study_hours_week'] >= 9)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 12th grade with study time >=9 hours/week."
    else:
        expl = "No student in 12th grade has study time >=9 hours/week."
    return truth, expl

def stmt_18(df: pd.DataFrame):
    """18. Most students in the 11th grade have a study time of 6 hours or more per week."""
    eleven_grade = df[df['grade_level'] == 11]
    if len(eleven_grade) == 0:
        truth = False
        expl = "No students in 11th grade."
    else:
        high_study = eleven_grade[eleven_grade['study_hours_week'] >= 6]
        proportion = len(high_study) / len(eleven_grade)
        truth = proportion > 0.5
        expl = f"{len(high_study)}/{len(eleven_grade)} ({proportion:.2%}) of 11th graders have study time >=6 hours/week."
    return truth, expl

def stmt_19(df: pd.DataFrame):
    """19. If a student is a club member, then their attendance rate is greater than 88%."""
    condition = (df['club_member'] == 'yes') & (df['attendance_rate'] <= 88)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All club members have attendance rate >88%."
    else:
        expl = f"{len(violations)} club members violate the rule."
    return truth, expl

def stmt_20(df: pd.DataFrame):
    """20. For all students with a test score less than 85, their study time is 5 hours or less per week."""
    condition = (df['test_score'] < 85) & (df['study_hours_week'] > 5)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with test score <85 have study time <=5 hours/week."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_21(df: pd.DataFrame):
    """21. All students with a study time of 10 hours or more per week have a test score greater than 70."""
    condition = (df['study_hours_week'] >= 10) & (df['test_score'] <= 70)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with study time >=10 hours have test score >70."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_22(df: pd.DataFrame):
    """22. There exists at least one student in the 10th grade with a test score greater than 95."""
    condition = (df['grade_level'] == 10) & (df['test_score'] > 95)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 10th grade with test score >95."
    else:
        expl = "No student in 10th grade has test score >95."
    return truth, expl

def stmt_23(df: pd.DataFrame):
    """23. Most students have an attendance rate greater than 85%."""
    high_attendance = df[df['attendance_rate'] > 85]
    proportion = len(high_attendance) / len(df)
    truth = proportion > 0.5
    expl = f"{len(high_attendance)}/{len(df)} ({proportion:.2%}) of students have attendance >85%."
    return truth, expl

def stmt_24(df: pd.DataFrame):
    """24. If a student is in the 12th grade, then their study time is 8 hours or more per week."""
    condition = (df['grade_level'] == 12) & (df['study_hours_week'] < 8)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All 12th graders have study time >=8 hours/week."
    else:
        expl = f"{len(violations)} 12th graders violate the rule."
    return truth, expl

def stmt_25(df: pd.DataFrame):
    """25. All students with an attendance rate greater than 96% have a test score greater than 93."""
    condition = (df['attendance_rate'] > 96) & (df['test_score'] <= 93)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with attendance >96% have test score >93."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_26(df: pd.DataFrame):
    """26. There exists at least one student in the 9th grade with a study time of 7 hours or more per week."""
    condition = (df['grade_level'] == 9) & (df['study_hours_week'] >= 7)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 9th grade with study time >=7 hours/week."
    else:
        expl = "No student in 9th grade has study time >=7 hours/week."
    return truth, expl

def stmt_27(df: pd.DataFrame):
    """27. For all students with a study time of 3 hours or less per week, their test score is greater than 86."""
    condition = (df['study_hours_week'] <= 3) & (df['test_score'] <= 86)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with study time <=3 hours have test score >86."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_28(df: pd.DataFrame):
    """28. If a student is a club member, then their study time is 4 hours or more per week."""
    condition = (df['club_member'] == 'yes') & (df['study_hours_week'] < 4)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All club members have study time >=4 hours/week."
    else:
        expl = f"{len(violations)} club members violate the rule."
    return truth, expl

def stmt_29(df: pd.DataFrame):
    """29. Most students in the 10th grade have a study time of 5 hours or more per week."""
    ten_grade = df[df['grade_level'] == 10]
    if len(ten_grade) == 0:
        truth = False
        expl = "No students in 10th grade."
    else:
        high_study = ten_grade[ten_grade['study_hours_week'] >= 5]
        proportion = len(high_study) / len(ten_grade)
        truth = proportion > 0.5
        expl = f"{len(high_study)}/{len(ten_grade)} ({proportion:.2%}) of 10th graders have study time >=5 hours/week."
    return truth, expl

def stmt_30(df: pd.DataFrame):
    """30. All students with a test score greater than 96 have a study time of 4 hours or more per week."""
    condition = (df['test_score'] > 96) & (df['study_hours_week'] < 4)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with test score >96 have study time >=4 hours/week."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_31(df: pd.DataFrame):
    """31. There exists at least one student in the 11th grade with a test score greater than 96."""
    condition = (df['grade_level'] == 11) & (df['test_score'] > 96)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 11th grade with test score >96."
    else:
        expl = "No student in 11th grade has test score >96."
    return truth, expl

def stmt_32(df: pd.DataFrame):
    """32. For all students with an attendance rate greater than 90%, their study time is 4 hours or more per week."""
    condition = (df['attendance_rate'] > 90) & (df['study_hours_week'] < 4)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with attendance >90% have study time >=4 hours/week."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_33(df: pd.DataFrame):
    """33. If a student is in the 9th grade, then their attendance rate is greater than 84%."""
    condition = (df['grade_level'] == 9) & (df['attendance_rate'] <= 84)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All 9th graders have attendance rate >84%."
    else:
        expl = f"{len(violations)} 9th graders violate the rule."
    return truth, expl

def stmt_34(df: pd.DataFrame):
    """34. All students with a study time of 11 hours or more per week have a test score greater than 70."""
    condition = (df['study_hours_week'] >= 11) & (df['test_score'] <= 70)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with study time >=11 hours have test score >70."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_35(df: pd.DataFrame):
    """35. There exists at least one student in the 12th grade with a test score greater than 93."""
    condition = (df['grade_level'] == 12) & (df['test_score'] > 93)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 12th grade with test score >93."
    else:
        expl = "No student in 12th grade has test score >93."
    return truth, expl

def stmt_36(df: pd.DataFrame):
    """36. Most students have a study time of 4 hours or more per week."""
    high_study = df[df['study_hours_week'] >= 4]
    proportion = len(high_study) / len(df)
    truth = proportion > 0.5
    expl = f"{len(high_study)}/{len(df)} ({proportion:.2%}) of students have study time >=4 hours/week."
    return truth, expl

def stmt_37(df: pd.DataFrame):
    """37. If a student is a club member, then their attendance rate is greater than 90%."""
    condition = (df['club_member'] == 'yes') & (df['attendance_rate'] <= 90)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All club members have attendance rate >90%."
    else:
        expl = f"{len(violations)} club members violate the rule."
    return truth, expl

def stmt_38(df: pd.DataFrame):
    """38. For all students with a test score less than 80, their attendance rate is greater than 90%."""
    condition = (df['test_score'] < 80) & (df['attendance_rate'] <= 90)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with test score <80 have attendance rate >90%."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_39(df: pd.DataFrame):
    """39. All students with an attendance rate greater than 97% have a test score greater than 86."""
    condition = (df['attendance_rate'] > 97) & (df['test_score'] <= 86)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with attendance >97% have test score >86."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_40(df: pd.DataFrame):
    """40. There exists at least one student in the 10th grade with a study time of 4 hours or less per week."""
    condition = (df['grade_level'] == 10) & (df['study_hours_week'] <= 4)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 10th grade with study time <=4 hours/week."
    else:
        expl = "No student in 10th grade has study time <=4 hours/week."
    return truth, expl

def stmt_41(df: pd.DataFrame):
    """41. Most students in the 12th grade have a study time of 8 hours or more per week."""
    twelve_grade = df[df['grade_level'] == 12]
    if len(twelve_grade) == 0:
        truth = False
        expl = "No students in 12th grade."
    else:
        high_study = twelve_grade[twelve_grade['study_hours_week'] >= 8]
        proportion = len(high_study) / len(twelve_grade)
        truth = proportion > 0.5
        expl = f"{len(high_study)}/{len(twelve_grade)} ({proportion:.2%}) of 12th graders have study time >=8 hours/week."
    return truth, expl

def stmt_42(df: pd.DataFrame):
    """42. If a student is in the 11th grade, then their test score is greater than 78."""
    condition = (df['grade_level'] == 11) & (df['test_score'] <= 78)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All 11th graders have test score >78."
    else:
        expl = f"{len(violations)} 11th graders violate the rule."
    return truth, expl

def stmt_43(df: pd.DataFrame):
    """43. All students with a study time of 9 hours or more per week have a test score greater than 67."""
    condition = (df['study_hours_week'] >= 9) & (df['test_score'] <= 67)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with study time >=9 hours have test score >67."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_44(df: pd.DataFrame):
    """44. There exists at least one student in the 9th grade with a test score greater than 93."""
    condition = (df['grade_level'] == 9) & (df['test_score'] > 93)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 9th grade with test score >93."
    else:
        expl = "No student in 9th grade has test score >93."
    return truth, expl

def stmt_45(df: pd.DataFrame):
    """45. For all students with an attendance rate greater than 95%, their study time is 5 hours or more per week."""
    condition = (df['attendance_rate'] > 95) & (df['study_hours_week'] < 5)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with attendance >95% have study time >=5 hours/week."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_46(df: pd.DataFrame):
    """46. If a student is a club member, then their test score is greater than 93."""
    condition = (df['club_member'] == 'yes') & (df['test_score'] <= 93)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All club members have test score >93."
    else:
        expl = f"{len(violations)} club members violate the rule."
    return truth, expl

def stmt_47(df: pd.DataFrame):
    """47. Most students have an attendance rate greater than 90%."""
    high_attendance = df[df['attendance_rate'] > 90]
    proportion = len(high_attendance) / len(df)
    truth = proportion > 0.5
    expl = f"{len(high_attendance)}/{len(df)} ({proportion:.2%}) of students have attendance >90%."
    return truth, expl

def stmt_48(df: pd.DataFrame):
    """48. All students with a test score greater than 97 have a study time of 7 hours or more per week."""
    condition = (df['test_score'] > 97) & (df['study_hours_week'] < 7)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with test score >97 have study time >=7 hours/week."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_49(df: pd.DataFrame):
    """49. There exists at least one student in the 11th grade with a study time of 8 hours or more per week."""
    condition = (df['grade_level'] == 11) & (df['study_hours_week'] >= 8)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 11th grade with study time >=8 hours/week."
    else:
        expl = "No student in 11th grade has study time >=8 hours/week."
    return truth, expl

def stmt_50(df: pd.DataFrame):
    """50. For all students with a study time of 10 hours or more per week, their attendance rate is greater than 88%."""
    condition = (df['study_hours_week'] >= 10) & (df['attendance_rate'] <= 88)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with study time >=10 hours have attendance >88%."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_51(df: pd.DataFrame):
    """51. If a student is in the 10th grade, then their test score is greater than 62."""
    condition = (df['grade_level'] == 10) & (df['test_score'] <= 62)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All 10th graders have test score >62."
    else:
        expl = f"{len(violations)} 10th graders violate the rule."
    return truth, expl

def stmt_52(df: pd.DataFrame):
    """52. All students with an attendance rate greater than 92% have a test score greater than 79."""
    condition = (df['attendance_rate'] > 92) & (df['test_score'] <= 79)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with attendance >92% have test score >79."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_53(df: pd.DataFrame):
    """53. There exists at least one student in the 12th grade with a test score greater than 80."""
    condition = (df['grade_level'] == 12) & (df['test_score'] > 80)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 12th grade with test score >80."
    else:
        expl = "No student in 12th grade has test score >80."
    return truth, expl

def stmt_54(df: pd.DataFrame):
    """54. Most students in the 9th grade have a study time of 5 hours or more per week."""
    nine_grade = df[df['grade_level'] == 9]
    if len(nine_grade) == 0:
        truth = False
        expl = "No students in 9th grade."
    else:
        high_study = nine_grade[nine_grade['study_hours_week'] >= 5]
        proportion = len(high_study) / len(nine_grade)
        truth = proportion > 0.5
        expl = f"{len(high_study)}/{len(nine_grade)} ({proportion:.2%}) of 9th graders have study time >=5 hours/week."
    return truth, expl

def stmt_55(df: pd.DataFrame):
    """55. If a student is a club member, then their attendance rate is greater than 91%."""
    condition = (df['club_member'] == 'yes') & (df['attendance_rate'] <= 91)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All club members have attendance rate >91%."
    else:
        expl = f"{len(violations)} club members violate the rule."
    return truth, expl

def stmt_56(df: pd.DataFrame):
    """56. For all students with a test score less than 85, their study time is 4 hours or less per week."""
    condition = (df['test_score'] < 85) & (df['study_hours_week'] > 4)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with test score <85 have study time <=4 hours/week."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_57(df: pd.DataFrame):
    """57. All students with a study time of 11 hours or more per week have a test score greater than 70."""
    condition = (df['study_hours_week'] >= 11) & (df['test_score'] <= 70)
    violations = df[condition]
    truth = len(violations) == 0
    if truth:
        expl = "All students with study time >=11 hours have test score >70."
    else:
        expl = f"{len(violations)} students violate the rule."
    return truth, expl

def stmt_58(df: pd.DataFrame):
    """58. There exists at least one student in the 10th grade with a test score greater than 86."""
    condition = (df['grade_level'] == 10) & (df['test_score'] > 86)
    found = df[condition]
    truth = len(found) >= 1
    if truth:
        expl = f"Found {len(found)} student(s) in 10th grade with test score >86."
    else:
        expl = "No student in 10th grade has test score >86."
    return truth, expl

def stmt_59(df: pd.DataFrame):
    """59. Most students have a study time of 5 hours or more per week."""
    high_study = df[df['study_hours_week'] >= 5]
    proportion = len(high_study) / len(df)
    truth = proportion > 0.5
    expl = f"{len(high_study)}/{len(df)} ({proportion:.2%}) of students have study time >=5 hours/week."
    return truth, expl

def stmt_60(df: pd.DataFrame):
    """60. If a student is in the 11th grade, then their attendance rate is greater than 84%."""
    condition = (