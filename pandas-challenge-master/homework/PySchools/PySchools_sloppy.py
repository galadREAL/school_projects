#!/usr/bin/env python
# coding: utf-8

# # PyCity Schools Analysis
#
# * As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (<\$585 per student).
#
# * As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).
#
# * As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school.

import pandas as pd
import numpy as np
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"
schoolData = pd.read_csv(school_data_to_load)
studentData = pd.read_csv(student_data_to_load)
allData = pd.merge(studentData, schoolData, how="left", on=["school_name", "school_name"])
#####Calculate the total number of schools
totalSchools = len(schoolData.index)
print(totalSchools)
#####Calculate the total number of students
totalStudents = len(studentData['student_name'])
totalStudentsPol = str("{:,}").format(totalStudents)
print(totalStudentsPol)
#####Calculate the total budget
totalBudget = schoolData['budget'].sum()
totalBudgetPol = str("${:,.2f}").format(totalBudget)
print(totalBudgetPol)
#####Calculate the average math score
avgMathScore = studentData['math_score'].mean()
avgMathScorePol = np.round(avgMathScore, decimals=2)
avgMathScorePol = str(f"{avgMathScorePol}%")
print(avgMathScorePol)
#####Calculate the average reading score
avgReadingScore = studentData['reading_score'].mean()
avgReadingScorePol = np.round(avgReadingScore, decimals=2)
avgReadingScorePol = str(f"{avgReadingScorePol}%")
print(avgReadingScorePol)
#* is the example wrong? should it be the num of passing students + passing students / 2?
#####Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
pctPassingBoth = (avgMathScore + avgReadingScore) / 2
pctPassingBothPol = np.round(pctPassingBoth, decimals=2)
pctPassingBothPol = str(f"{pctPassingBothPol}%")
print(pctPassingBothPol)
#####Calculate the percentage of students with a passing math score (70 or greater)
mathBins = [0, 69, 100]
mathBinsNames = ["Not Passing", "Passing"]
mathDF = pd.DataFrame(studentData)
mathDF["Maths Merit"] = pd.cut(mathDF['math_score'], mathBins, labels=mathBinsNames)
mathByMerit = mathDF["Maths Merit"].value_counts()
isnotPassingMath = mathByMerit[0]
isPassingMath = mathByMerit[1]
pctPassingMath = isPassingMath / totalStudents * 100
pctPassingMathPol = np.round(pctPassingMath, decimals=2)
pctPassingMathPol = str(f"{pctPassingMathPol}%")
print(pctPassingMathPol)
#####Calculate the percentage of students with a passing reading score (70 or greater)
readingBins = [0, 69, 100]
readingBinsNames = ["Not Passing", "Passing"]
readingDF = pd.DataFrame(studentData)
readingDF["Reading Merit"] = pd.cut(readingDF['reading_score'], readingBins, labels=readingBinsNames)
readingByMerit = readingDF["Reading Merit"].value_counts()
isnotPassingReading = readingByMerit[0]
isPassingReading = readingByMerit[1]
pctPassingReading = isPassingReading / totalStudents * 100
pctPassingReadingPol = np.round(pctPassingReading, decimals=2)
pctPassingReadingPol = str(f"{pctPassingReadingPol}%")
print(pctPassingReadingPol)
#####Create a dataframe to hold the above results
DistrictSummaryDF = pd.DataFrame(data={'Total Schools': [totalSchools],
                                      'Total Students': [totalStudentsPol],
                                      'Total Budget': [totalBudgetPol],
                                      'Average Math Score': [avgMathScorePol],
                                      'Average Reading Score': [avgReadingScorePol],
                                      '% Passing Math': [pctPassingMathPol],
                                      '% Passing Reading': [pctPassingReadingPol],
                                      '% Overall Passing Rate': [pctPassingBothPol]})
TopSchoolsDF = pd.DataFrame(allData)
TopSchoolsDF.columns = ["Student ID", "Student Name", "Gender", "Grade", "School Name", "Reading Score", "Math Score", "School ID", "Type", "Size", "Budget"]
#####################################################################################
######################### establish dataframes for each school
#####################################################################################
HuangDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Huang High School"]
FigueroaDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Figueroa High School"]
SheltonDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Shelton High School"]
HernandezDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Hernandez High School"]
GriffinDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Griffin High School"]
WilsonDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Wilson High School"]
CabreraDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Cabrera High School"]
BaileyDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Bailey High School"]
HoldenDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Holden High School"]
PenaDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Pena High School"]
WrightDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Wright High School"]
RodriguezDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Rodriguez High School"]
JohnsonDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Johnson High School"]
FordDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Ford High School"]
ThomasDF = TopSchoolsDF.loc[TopSchoolsDF['School Name'] == "Thomas High School"]
#####################################################################################
######################### establish total students per school
#####################################################################################
totalStudentsHuang = len(HuangDF.index)
totalStudentsHuangPol = str("{:,}").format(totalStudentsHuang)
totalStudentsFigueroa = len(FigueroaDF.index)
totalStudentsFigueroaPol = str("{:,}").format(totalStudentsFigueroa)
totalStudentsShelton = len(SheltonDF.index)
totalStudentsSheltonPol = str("{:,}").format(totalStudentsShelton)
totalStudentsHernandez = len(HernandezDF.index)
totalStudentsHernandezPol = str("{:,}").format(totalStudentsHernandez)
totalStudentsGriffin = len(GriffinDF.index)
totalStudentsGriffinPol = str("{:,}").format(totalStudentsGriffin)
totalStudentsWilson = len(WilsonDF.index)
totalStudentsWilsonPol = str("{:,}").format(totalStudentsWilson)
totalStudentsCabrera = len(CabreraDF.index)
totalStudentsCabreraPol = str("{:,}").format(totalStudentsCabrera)
totalStudentsBailey = len(BaileyDF.index)
totalStudentsBaileyPol = str("{:,}").format(totalStudentsBailey)
totalStudentsHolden = len(HoldenDF.index)
totalStudentsHoldenPol = str("{:,}").format(totalStudentsHolden)
totalStudentsPena = len(PenaDF.index)
totalStudentsPenaPol = str("{:,}").format(totalStudentsPena)
totalStudentsWright = len(WrightDF.index)
totalStudentsWrightPol = str("{:,}").format(totalStudentsWright)
totalStudentsRodriguez = len(RodriguezDF.index)
totalStudentsRodriguezPol = str("{:,}").format(totalStudentsRodriguez)
totalStudentsJohnson = len(JohnsonDF.index)
totalStudentsJohnsonPol = str("{:,}").format(totalStudentsJohnson)
totalStudentsFord = len(FordDF.index)
totalStudentsFordPol = str("{:,}").format(totalStudentsFord)
totalStudentsThomas = len(ThomasDF.index)
totalStudentsThomasPol = str("{:,}").format(totalStudentsThomas)
#####################################################################################
######################### establish budgets per school
#####################################################################################
budgetHuang = HuangDF['Budget'].max()
budgetHuangPol = str("${:,.2f}").format(budgetHuang)
budgetFigueroa = FigueroaDF['Budget'].max()
budgetFigueroaPol = str("${:,.2f}").format(budgetFigueroa)
budgetShelton = SheltonDF['Budget'].max()
budgetSheltonPol = str("${:,.2f}").format(budgetShelton)
budgetHernandez = HernandezDF['Budget'].max()
budgetHernandezPol = str("${:,.2f}").format(budgetHernandez)
budgetGriffin = GriffinDF['Budget'].max()
budgetGriffinPol = str("${:,.2f}").format(budgetGriffin)
budgetWilson = WilsonDF['Budget'].max()
budgetWilsonPol = str("${:,.2f}").format(budgetWilson)
budgetCabrera = CabreraDF['Budget'].max()
budgetCabreraPol = str("${:,.2f}").format(budgetCabrera)
budgetBailey = BaileyDF['Budget'].max()
budgetBaileyPol = str("${:,.2f}").format(budgetBailey)
budgetHolden = HoldenDF['Budget'].max()
budgetHoldenPol = str("${:,.2f}").format(budgetHolden)
budgetPena = PenaDF['Budget'].max()
budgetPenaPol = str("${:,.2f}").format(budgetPena)
budgetWright = WrightDF['Budget'].max()
budgetWrightPol = str("${:,.2f}").format(budgetWright)
budgetRodriguez = RodriguezDF['Budget'].max()
budgetRodriguezPol = str("${:,.2f}").format(budgetRodriguez)
budgetJohnson = JohnsonDF['Budget'].max()
budgetJohnsonPol = str("${:,.2f}").format(budgetJohnson)
budgetFord = FordDF['Budget'].max()
budgetFordPol = str("${:,.2f}").format(budgetFord)
budgetThomas = ThomasDF['Budget'].max()
budgetThomasPol = str("${:,.2f}").format(budgetThomas)
#####################################################################################
######################### establish per student budget per school
#####################################################################################
studentBudgetHuang = budgetHuang / totalStudentsHuang
studentBudgetHuangPol = str("${:,.2f}").format(studentBudgetHuang)
studentBudgetFigueroa = budgetFigueroa / totalStudentsFigueroa
studentBudgetFigueroaPol = str("${:,.2f}").format(studentBudgetFigueroa)
studentBudgetShelton = budgetShelton / totalStudentsShelton
studentBudgetSheltonPol = str("${:,.2f}").format(studentBudgetShelton)
studentBudgetHernandez = budgetHernandez / totalStudentsHernandez
studentBudgetHernandezPol = str("${:,.2f}").format(studentBudgetHernandez)
studentBudgetGriffin = budgetGriffin / totalStudentsGriffin
studentBudgetGriffinPol = str("${:,.2f}").format(studentBudgetGriffin)
studentBudgetWilson = budgetWilson / totalStudentsWilson
studentBudgetWilsonPol = str("${:,.2f}").format(studentBudgetWilson)
studentBudgetCabrera = budgetCabrera / totalStudentsCabrera
studentBudgetCabreraPol = str("${:,.2f}").format(studentBudgetCabrera)
studentBudgetBailey = budgetBailey / totalStudentsBailey
studentBudgetBaileyPol = str("${:,.2f}").format(studentBudgetBailey)
studentBudgetHolden = budgetHolden / totalStudentsHolden
studentBudgetHoldenPol = str("${:,.2f}").format(studentBudgetHolden)
studentBudgetPena = budgetPena / totalStudentsPena
studentBudgetPenaPol = str("${:,.2f}").format(studentBudgetPena)
studentBudgetWright = budgetWright / totalStudentsWright
studentBudgetWrightPol = str("${:,.2f}").format(studentBudgetWright)
studentBudgetRodriguez = budgetRodriguez / totalStudentsRodriguez
studentBudgetRodriguezPol = str("${:,.2f}").format(studentBudgetRodriguez)
studentBudgetJohnson = budgetJohnson / totalStudentsJohnson
studentBudgetJohnsonPol = str("${:,.2f}").format(studentBudgetJohnson)
studentBudgetFord = budgetFord / totalStudentsFord
studentBudgetFordPol = str("${:,.2f}").format(studentBudgetFord)
studentBudgetThomas = budgetThomas / totalStudentsThomas
studentBudgetThomasPol = str("${:,.2f}").format(studentBudgetThomas)
#####################################################################################
######################### establish avg math score per school
#####################################################################################
avgMathScoreHuang = HuangDF['Math Score'].mean()
avgMathScoreHuangPol = np.round(avgMathScoreHuang, decimals=2)
avgMathScoreHuangPol = str(f"{avgMathScoreHuangPol}%")
avgMathScoreFigueroa = FigueroaDF['Math Score'].mean()
avgMathScoreFigueroaPol = np.round(avgMathScoreFigueroa, decimals=2)
avgMathScoreFigueroaPol = str(f"{avgMathScoreFigueroaPol}%")
avgMathScoreShelton = SheltonDF['Math Score'].mean()
avgMathScoreSheltonPol = np.round(avgMathScoreShelton, decimals=2)
avgMathScoreSheltonPol = str(f"{avgMathScoreSheltonPol}%")
avgMathScoreHernandez = HernandezDF['Math Score'].mean()
avgMathScoreHernandezPol = np.round(avgMathScoreHernandez, decimals=2)
avgMathScoreHernandezPol = str(f"{avgMathScoreHernandezPol}%")
avgMathScoreGriffin = GriffinDF['Math Score'].mean()
avgMathScoreGriffinPol = np.round(avgMathScoreGriffin, decimals=2)
avgMathScoreGriffinPol = str(f"{avgMathScoreGriffinPol}%")
avgMathScoreWilson = WilsonDF['Math Score'].mean()
avgMathScoreWilsonPol = np.round(avgMathScoreWilson, decimals=2)
avgMathScoreWilsonPol = str(f"{avgMathScoreWilsonPol}%")
avgMathScoreCabrera = CabreraDF['Math Score'].mean()
avgMathScoreCabreraPol = np.round(avgMathScoreCabrera, decimals=2)
avgMathScoreCabreraPol = str(f"{avgMathScoreCabreraPol}%")
avgMathScoreBailey = BaileyDF['Math Score'].mean()
avgMathScoreBaileyPol = np.round(avgMathScoreBailey, decimals=2)
avgMathScoreBaileyPol = str(f"{avgMathScoreBaileyPol}%")
avgMathScoreHolden = HoldenDF['Math Score'].mean()
avgMathScoreHoldenPol = np.round(avgMathScoreHolden, decimals=2)
avgMathScoreHoldenPol = str(f"{avgMathScoreHoldenPol}%")
avgMathScorePena = PenaDF['Math Score'].mean()
avgMathScorePenaPol = np.round(avgMathScorePena, decimals=2)
avgMathScorePenaPol = str(f"{avgMathScorePenaPol}%")
avgMathScoreWright = WrightDF['Math Score'].mean()
avgMathScoreWrightPol = np.round(avgMathScoreWright, decimals=2)
avgMathScoreWrightPol = str(f"{avgMathScoreWrightPol}%")
avgMathScoreRodriguez = RodriguezDF['Math Score'].mean()
avgMathScoreRodriguezPol = np.round(avgMathScoreRodriguez, decimals=2)
avgMathScoreRodriguezPol = str(f"{avgMathScoreRodriguezPol}%")
avgMathScoreJohnson = JohnsonDF['Math Score'].mean()
avgMathScoreJohnsonPol = np.round(avgMathScoreJohnson, decimals=2)
avgMathScoreJohnsonPol = str(f"{avgMathScoreJohnsonPol}%")
avgMathScoreFord = FordDF['Math Score'].mean()
avgMathScoreFordPol = np.round(avgMathScoreFord, decimals=2)
avgMathScoreFordPol = str(f"{avgMathScoreFordPol}%")
avgMathScoreThomas = ThomasDF['Math Score'].mean()
avgMathScoreThomasPol = np.round(avgMathScoreThomas, decimals=2)
avgMathScoreThomasPol = str(f"{avgMathScoreThomasPol}%")
#####################################################################################
######################### establish avg reading score per school
#####################################################################################
avgReadingScoreHuang = HuangDF['Reading Score'].mean()
avgReadingScoreHuangPol = np.round(avgReadingScoreHuang, decimals=2)
avgReadingScoreHuangPol = str(f"{avgReadingScoreHuangPol}%")
avgReadingScoreFigueroa = FigueroaDF['Reading Score'].mean()
avgReadingScoreFigueroaPol = np.round(avgReadingScoreFigueroa, decimals=2)
avgReadingScoreFigueroaPol = str(f"{avgReadingScoreFigueroaPol}%")
avgReadingScoreShelton = SheltonDF['Reading Score'].mean()
avgReadingScoreSheltonPol = np.round(avgReadingScoreShelton, decimals=2)
avgReadingScoreSheltonPol = str(f"{avgReadingScoreSheltonPol}%")
avgReadingScoreHernandez = HernandezDF['Reading Score'].mean()
avgReadingScoreHernandezPol = np.round(avgReadingScoreHernandez, decimals=2)
avgReadingScoreHernandezPol = str(f"{avgReadingScoreHernandezPol}%")
avgReadingScoreGriffin = GriffinDF['Reading Score'].mean()
avgReadingScoreGriffinPol = np.round(avgReadingScoreGriffin, decimals=2)
avgReadingScoreGriffinPol = str(f"{avgReadingScoreGriffinPol}%")
avgReadingScoreWilson = WilsonDF['Reading Score'].mean()
avgReadingScoreWilsonPol = np.round(avgReadingScoreWilson, decimals=2)
avgReadingScoreWilsonPol = str(f"{avgReadingScoreWilsonPol}%")
avgReadingScoreCabrera = CabreraDF['Reading Score'].mean()
avgReadingScoreCabreraPol = np.round(avgReadingScoreCabrera, decimals=2)
avgReadingScoreCabreraPol = str(f"{avgReadingScoreCabreraPol}%")
avgReadingScoreBailey = BaileyDF['Reading Score'].mean()
avgReadingScoreBaileyPol = np.round(avgReadingScoreBailey, decimals=2)
avgReadingScoreBaileyPol = str(f"{avgReadingScoreBaileyPol}%")
avgReadingScoreHolden = HoldenDF['Reading Score'].mean()
avgReadingScoreHoldenPol = np.round(avgReadingScoreHolden, decimals=2)
avgReadingScoreHoldenPol = str(f"{avgReadingScoreHoldenPol}%")
avgReadingScorePena = PenaDF['Reading Score'].mean()
avgReadingScorePenaPol = np.round(avgReadingScorePena, decimals=2)
avgReadingScorePenaPol = str(f"{avgReadingScorePenaPol}%")
avgReadingScoreWright = WrightDF['Reading Score'].mean()
avgReadingScoreWrightPol = np.round(avgReadingScoreWright, decimals=2)
avgReadingScoreWrightPol = str(f"{avgReadingScoreWrightPol}%")
avgReadingScoreRodriguez = RodriguezDF['Reading Score'].mean()
avgReadingScoreRodriguezPol = np.round(avgReadingScoreRodriguez, decimals=2)
avgReadingScoreRodriguezPol = str(f"{avgReadingScoreRodriguezPol}%")
avgReadingScoreJohnson = JohnsonDF['Reading Score'].mean()
avgReadingScoreJohnsonPol = np.round(avgReadingScoreJohnson, decimals=2)
avgReadingScoreJohnsonPol = str(f"{avgReadingScoreJohnsonPol}%")
avgReadingScoreFord = FordDF['Reading Score'].mean()
avgReadingScoreFordPol = np.round(avgReadingScoreFord, decimals=2)
avgReadingScoreFordPol = str(f"{avgReadingScoreFordPol}%")
avgReadingScoreThomas = ThomasDF['Reading Score'].mean()
avgReadingScoreThomasPol = np.round(avgReadingScoreThomas, decimals=2)
avgReadingScoreThomasPol = str(f"{avgReadingScoreThomasPol}%")
#####################################################################################
######################### establish % passing math per school
#####################################################################################
HuangDF["Maths Merit"] = pd.cut(HuangDF['Math Score'], mathBins, labels=mathBinsNames)
HuangmathByMerit = HuangDF["Maths Merit"].value_counts()
HuangisnotPassingMath = HuangmathByMerit[0]
HuangisPassingMath = HuangmathByMerit[1]
HuangpctPassingMath = HuangisPassingMath / totalStudentsHuang * 100
HuangpctPassingMathPol = np.round(HuangpctPassingMath, decimals=2)
HuangpctPassingMathPol = str(f"{HuangpctPassingMathPol}%")
FigueroaDF["Maths Merit"] = pd.cut(FigueroaDF['Math Score'], mathBins, labels=mathBinsNames)
FigueroamathByMerit = FigueroaDF["Maths Merit"].value_counts()
FigueroaisnotPassingMath = FigueroamathByMerit[0]
FigueroaisPassingMath = FigueroamathByMerit[1]
FigueroapctPassingMath = FigueroaisPassingMath / totalStudentsFigueroa * 100
FigueroapctPassingMathPol = np.round(FigueroapctPassingMath, decimals=2)
FigueroapctPassingMathPol = str(f"{FigueroapctPassingMathPol}%")
SheltonDF["Maths Merit"] = pd.cut(SheltonDF['Math Score'], mathBins, labels=mathBinsNames)
SheltonmathByMerit = SheltonDF["Maths Merit"].value_counts()
SheltonisnotPassingMath = SheltonmathByMerit[0]
SheltonisPassingMath = SheltonmathByMerit[1]
SheltonpctPassingMath = SheltonisPassingMath / totalStudentsShelton * 100
SheltonpctPassingMathPol = np.round(SheltonpctPassingMath, decimals=2)
SheltonpctPassingMathPol = str(f"{SheltonpctPassingMathPol}%")
HernandezDF["Maths Merit"] = pd.cut(HernandezDF['Math Score'], mathBins, labels=mathBinsNames)
HernandezmathByMerit = HernandezDF["Maths Merit"].value_counts()
HernandezisnotPassingMath = HernandezmathByMerit[0]
HernandezisPassingMath = HernandezmathByMerit[1]
HernandezpctPassingMath = HernandezisPassingMath / totalStudentsHernandez * 100
HernandezpctPassingMathPol = np.round(HernandezpctPassingMath, decimals=2)
HernandezpctPassingMathPol = str(f"{HernandezpctPassingMathPol}%")
GriffinDF["Maths Merit"] = pd.cut(GriffinDF['Math Score'], mathBins, labels=mathBinsNames)
GriffinmathByMerit = GriffinDF["Maths Merit"].value_counts()
GriffinisnotPassingMath = GriffinmathByMerit[0]
GriffinisPassingMath = GriffinmathByMerit[1]
GriffinpctPassingMath = GriffinisPassingMath / totalStudentsGriffin * 100
GriffinpctPassingMathPol = np.round(GriffinpctPassingMath, decimals=2)
GriffinpctPassingMathPol = str(f"{GriffinpctPassingMathPol}%")
WilsonDF["Maths Merit"] = pd.cut(WilsonDF['Math Score'], mathBins, labels=mathBinsNames)
WilsonmathByMerit = WilsonDF["Maths Merit"].value_counts()
WilsonisnotPassingMath = WilsonmathByMerit[0]
WilsonisPassingMath = WilsonmathByMerit[1]
WilsonpctPassingMath = WilsonisPassingMath / totalStudentsWilson * 100
WilsonpctPassingMathPol = np.round(WilsonpctPassingMath, decimals=2)
WilsonpctPassingMathPol = str(f"{WilsonpctPassingMathPol}%")
CabreraDF["Maths Merit"] = pd.cut(CabreraDF['Math Score'], mathBins, labels=mathBinsNames)
CabreramathByMerit = CabreraDF["Maths Merit"].value_counts()
CabreraisnotPassingMath = CabreramathByMerit[0]
CabreraisPassingMath = CabreramathByMerit[1]
CabrerapctPassingMath = CabreraisPassingMath / totalStudentsCabrera * 100
CabrerapctPassingMathPol = np.round(CabrerapctPassingMath, decimals=2)
CabrerapctPassingMathPol = str(f"{CabrerapctPassingMathPol}%")
BaileyDF["Maths Merit"] = pd.cut(BaileyDF['Math Score'], mathBins, labels=mathBinsNames)
BaileymathByMerit = BaileyDF["Maths Merit"].value_counts()
BaileyisnotPassingMath = BaileymathByMerit[0]
BaileyisPassingMath = BaileymathByMerit[1]
BaileypctPassingMath = BaileyisPassingMath / totalStudentsBailey * 100
BaileypctPassingMathPol = np.round(BaileypctPassingMath, decimals=2)
BaileypctPassingMathPol = str(f"{BaileypctPassingMathPol}%")
HoldenDF["Maths Merit"] = pd.cut(HoldenDF['Math Score'], mathBins, labels=mathBinsNames)
HoldenmathByMerit = HoldenDF["Maths Merit"].value_counts()
HoldenisnotPassingMath = HoldenmathByMerit[0]
HoldenisPassingMath = HoldenmathByMerit[1]
HoldenpctPassingMath = HoldenisPassingMath / totalStudentsHolden * 100
HoldenpctPassingMathPol = np.round(HoldenpctPassingMath, decimals=2)
HoldenpctPassingMathPol = str(f"{HoldenpctPassingMathPol}%")
PenaDF["Maths Merit"] = pd.cut(PenaDF['Math Score'], mathBins, labels=mathBinsNames)
PenamathByMerit = PenaDF["Maths Merit"].value_counts()
PenaisnotPassingMath = PenamathByMerit[0]
PenaisPassingMath = PenamathByMerit[1]
PenapctPassingMath = PenaisPassingMath / totalStudentsPena * 100
PenapctPassingMathPol = np.round(PenapctPassingMath, decimals=2)
PenapctPassingMathPol = str(f"{PenapctPassingMathPol}%")
WrightDF["Maths Merit"] = pd.cut(WrightDF['Math Score'], mathBins, labels=mathBinsNames)
WrightmathByMerit = WrightDF["Maths Merit"].value_counts()
WrightisnotPassingMath = WrightmathByMerit[0]
WrightisPassingMath = WrightmathByMerit[1]
WrightpctPassingMath = WrightisPassingMath / totalStudentsWright * 100
WrightpctPassingMathPol = np.round(WrightpctPassingMath, decimals=2)
WrightpctPassingMathPol = str(f"{WrightpctPassingMathPol}%")
RodriguezDF["Maths Merit"] = pd.cut(RodriguezDF['Math Score'], mathBins, labels=mathBinsNames)
RodriguezmathByMerit = RodriguezDF["Maths Merit"].value_counts()
RodriguezisnotPassingMath = RodriguezmathByMerit[0]
RodriguezisPassingMath = RodriguezmathByMerit[1]
RodriguezpctPassingMath = RodriguezisPassingMath / totalStudentsRodriguez * 100
RodriguezpctPassingMathPol = np.round(RodriguezpctPassingMath, decimals=2)
RodriguezpctPassingMathPol = str(f"{RodriguezpctPassingMathPol}%")
JohnsonDF["Maths Merit"] = pd.cut(JohnsonDF['Math Score'], mathBins, labels=mathBinsNames)
JohnsonmathByMerit = JohnsonDF["Maths Merit"].value_counts()
JohnsonisnotPassingMath = JohnsonmathByMerit[0]
JohnsonisPassingMath = JohnsonmathByMerit[1]
JohnsonpctPassingMath = JohnsonisPassingMath / totalStudentsJohnson * 100
JohnsonpctPassingMathPol = np.round(JohnsonpctPassingMath, decimals=2)
JohnsonpctPassingMathPol = str(f"{JohnsonpctPassingMathPol}%")
FordDF["Maths Merit"] = pd.cut(FordDF['Math Score'], mathBins, labels=mathBinsNames)
FordmathByMerit = FordDF["Maths Merit"].value_counts()
FordisnotPassingMath = FordmathByMerit[0]
FordisPassingMath = FordmathByMerit[1]
FordpctPassingMath = FordisPassingMath / totalStudentsFord * 100
FordpctPassingMathPol = np.round(FordpctPassingMath, decimals=2)
FordpctPassingMathPol = str(f"{FordpctPassingMathPol}%")
ThomasDF["Maths Merit"] = pd.cut(ThomasDF['Math Score'], mathBins, labels=mathBinsNames)
ThomasmathByMerit = ThomasDF["Maths Merit"].value_counts()
ThomasisnotPassingMath = ThomasmathByMerit[0]
ThomasisPassingMath = ThomasmathByMerit[1]
ThomaspctPassingMath = ThomasisPassingMath / totalStudentsThomas * 100
ThomaspctPassingMathPol = np.round(ThomaspctPassingMath, decimals=2)
ThomaspctPassingMathPol = str(f"{ThomaspctPassingMathPol}%")
#####################################################################################
#########################establish % passing reading per school
#####################################################################################
HuangDF["Reading Merit"] = pd.cut(HuangDF['Reading Score'], readingBins, labels=readingBinsNames)
HuangreadingByMerit = HuangDF["Reading Merit"].value_counts()
HuangisnotPassingReading = HuangreadingByMerit[0]
HuangisPassingReading = HuangreadingByMerit[1]
HuangpctPassingReading = HuangisPassingReading / totalStudentsHuang * 100
HuangpctPassingReadingPol = np.round(HuangpctPassingReading, decimals=2)
HuangpctPassingReadingPol = str(f"{HuangpctPassingReadingPol}%")
FigueroaDF["Reading Merit"] = pd.cut(FigueroaDF['Reading Score'], readingBins, labels=readingBinsNames)
FigueroareadingByMerit = FigueroaDF["Reading Merit"].value_counts()
FigueroaisnotPassingReading = FigueroareadingByMerit[0]
FigueroaisPassingReading = FigueroareadingByMerit[1]
FigueroapctPassingReading = FigueroaisPassingReading / totalStudentsFigueroa * 100
FigueroapctPassingReadingPol = np.round(FigueroapctPassingReading, decimals=2)
FigueroapctPassingReadingPol = str(f"{FigueroapctPassingReadingPol}%")
SheltonDF["Reading Merit"] = pd.cut(SheltonDF['Reading Score'], readingBins, labels=readingBinsNames)
SheltonreadingByMerit = SheltonDF["Reading Merit"].value_counts()
SheltonisnotPassingReading = SheltonreadingByMerit[0]
SheltonisPassingReading = SheltonreadingByMerit[1]
SheltonpctPassingReading = SheltonisPassingReading / totalStudentsShelton * 100
SheltonpctPassingReadingPol = np.round(SheltonpctPassingReading, decimals=2)
SheltonpctPassingReadingPol = str(f"{SheltonpctPassingReadingPol}%")
HernandezDF["Reading Merit"] = pd.cut(HernandezDF['Reading Score'], readingBins, labels=readingBinsNames)
HernandezreadingByMerit = HernandezDF["Reading Merit"].value_counts()
HernandezisnotPassingReading = HernandezreadingByMerit[0]
HernandezisPassingReading = HernandezreadingByMerit[1]
HernandezpctPassingReading = HernandezisPassingReading / totalStudentsHernandez * 100
HernandezpctPassingReadingPol = np.round(HernandezpctPassingReading, decimals=2)
HernandezpctPassingReadingPol = str(f"{HernandezpctPassingReadingPol}%")
GriffinDF["Reading Merit"] = pd.cut(GriffinDF['Reading Score'], readingBins, labels=readingBinsNames)
GriffinreadingByMerit = GriffinDF["Reading Merit"].value_counts()
GriffinisnotPassingReading = GriffinreadingByMerit[0]
GriffinisPassingReading = GriffinreadingByMerit[1]
GriffinpctPassingReading = GriffinisPassingReading / totalStudentsGriffin * 100
GriffinpctPassingReadingPol = np.round(GriffinpctPassingReading, decimals=2)
GriffinpctPassingReadingPol = str(f"{GriffinpctPassingReadingPol}%")
WilsonDF["Reading Merit"] = pd.cut(WilsonDF['Reading Score'], readingBins, labels=readingBinsNames)
WilsonreadingByMerit = WilsonDF["Reading Merit"].value_counts()
WilsonisnotPassingReading = WilsonreadingByMerit[0]
WilsonisPassingReading = WilsonreadingByMerit[1]
WilsonpctPassingReading = WilsonisPassingReading / totalStudentsWilson * 100
WilsonpctPassingReadingPol = np.round(WilsonpctPassingReading, decimals=2)
WilsonpctPassingReadingPol = str(f"{WilsonpctPassingReadingPol}%")
CabreraDF["Reading Merit"] = pd.cut(CabreraDF['Reading Score'], readingBins, labels=readingBinsNames)
CabrerareadingByMerit = CabreraDF["Reading Merit"].value_counts()
CabreraisnotPassingReading = CabrerareadingByMerit[0]
CabreraisPassingReading = CabrerareadingByMerit[1]
CabrerapctPassingReading = CabreraisPassingReading / totalStudentsCabrera * 100
CabrerapctPassingReadingPol = np.round(CabrerapctPassingReading, decimals=2)
CabrerapctPassingReadingPol = str(f"{CabrerapctPassingReadingPol}%")
BaileyDF["Reading Merit"] = pd.cut(BaileyDF['Reading Score'], readingBins, labels=readingBinsNames)
BaileyreadingByMerit = BaileyDF["Reading Merit"].value_counts()
BaileyisnotPassingReading = BaileyreadingByMerit[0]
BaileyisPassingReading = BaileyreadingByMerit[1]
BaileypctPassingReading = BaileyisPassingReading / totalStudentsBailey * 100
BaileypctPassingReadingPol = np.round(BaileypctPassingReading, decimals=2)
BaileypctPassingReadingPol = str(f"{BaileypctPassingReadingPol}%")
HoldenDF["Reading Merit"] = pd.cut(HoldenDF['Reading Score'], readingBins, labels=readingBinsNames)
HoldenreadingByMerit = HoldenDF["Reading Merit"].value_counts()
HoldenisnotPassingReading = HoldenreadingByMerit[0]
HoldenisPassingReading = HoldenreadingByMerit[1]
HoldenpctPassingReading = HoldenisPassingReading / totalStudentsHolden * 100
HoldenpctPassingReadingPol = np.round(HoldenpctPassingReading, decimals=2)
HoldenpctPassingReadingPol = str(f"{HoldenpctPassingReadingPol}%")
PenaDF["Reading Merit"] = pd.cut(PenaDF['Reading Score'], readingBins, labels=readingBinsNames)
PenareadingByMerit = PenaDF["Reading Merit"].value_counts()
PenaisnotPassingReading = PenareadingByMerit[0]
PenaisPassingReading = PenareadingByMerit[1]
PenapctPassingReading = PenaisPassingReading / totalStudentsPena * 100
PenapctPassingReadingPol = np.round(PenapctPassingReading, decimals=2)
PenapctPassingReadingPol = str(f"{PenapctPassingReadingPol}%")
WrightDF["Reading Merit"] = pd.cut(WrightDF['Reading Score'], readingBins, labels=readingBinsNames)
WrightreadingByMerit = WrightDF["Reading Merit"].value_counts()
WrightisnotPassingReading = WrightreadingByMerit[0]
WrightisPassingReading = WrightreadingByMerit[1]
WrightpctPassingReading = WrightisPassingReading / totalStudentsWright * 100
WrightpctPassingReadingPol = np.round(WrightpctPassingReading, decimals=2)
WrightpctPassingReadingPol = str(f"{WrightpctPassingReadingPol}%")
RodriguezDF["Reading Merit"] = pd.cut(RodriguezDF['Reading Score'], readingBins, labels=readingBinsNames)
RodriguezreadingByMerit = RodriguezDF["Reading Merit"].value_counts()
RodriguezisnotPassingReading = RodriguezreadingByMerit[0]
RodriguezisPassingReading = RodriguezreadingByMerit[1]
RodriguezpctPassingReading = RodriguezisPassingReading / totalStudentsRodriguez * 100
RodriguezpctPassingReadingPol = np.round(RodriguezpctPassingReading, decimals=2)
RodriguezpctPassingReadingPol = str(f"{RodriguezpctPassingReadingPol}%")
JohnsonDF["Reading Merit"] = pd.cut(JohnsonDF['Reading Score'], readingBins, labels=readingBinsNames)
JohnsonreadingByMerit = JohnsonDF["Reading Merit"].value_counts()
JohnsonisnotPassingReading = JohnsonreadingByMerit[0]
JohnsonisPassingReading = JohnsonreadingByMerit[1]
JohnsonpctPassingReading = JohnsonisPassingReading / totalStudentsJohnson * 100
JohnsonpctPassingReadingPol = np.round(JohnsonpctPassingReading, decimals=2)
JohnsonpctPassingReadingPol = str(f"{JohnsonpctPassingReadingPol}%")
FordDF["Reading Merit"] = pd.cut(FordDF['Reading Score'], readingBins, labels=readingBinsNames)
FordreadingByMerit = FordDF["Reading Merit"].value_counts()
FordisnotPassingReading = FordreadingByMerit[0]
FordisPassingReading = FordreadingByMerit[1]
FordpctPassingReading = FordisPassingReading / totalStudentsFord * 100
FordpctPassingReadingPol = np.round(FordpctPassingReading, decimals=2)
FordpctPassingReadingPol = str(f"{FordpctPassingReadingPol}%")
ThomasDF["Reading Merit"] = pd.cut(ThomasDF['Reading Score'], readingBins, labels=readingBinsNames)
ThomasreadingByMerit = ThomasDF["Reading Merit"].value_counts()
ThomasisnotPassingReading = ThomasreadingByMerit[0]
ThomasisPassingReading = ThomasreadingByMerit[1]
ThomaspctPassingReading = ThomasisPassingReading / totalStudentsThomas * 100
ThomaspctPassingReadingPol = np.round(ThomaspctPassingReading, decimals=2)
ThomaspctPassingReadingPol = str(f"{ThomaspctPassingReadingPol}%")
#####################################################################################
######################### establish % passing overall per school
#####################################################################################
HuangpctPassingBoth = (HuangpctPassingMath + HuangpctPassingReading) / 2
HuangpctPassingBothPol = np.round(HuangpctPassingBoth, decimals=2)
HuangpctPassingBothPol = str(f"{HuangpctPassingBothPol}%")
FigueroapctPassingBoth = (FigueroapctPassingMath + FigueroapctPassingReading) / 2
FigueroapctPassingBothPol = np.round(FigueroapctPassingBoth, decimals=2)
FigueroapctPassingBothPol = str(f"{FigueroapctPassingBothPol}%")
SheltonpctPassingBoth = (SheltonpctPassingMath + SheltonpctPassingReading) / 2
SheltonpctPassingBothPol = np.round(SheltonpctPassingBoth, decimals=2)
SheltonpctPassingBothPol = str(f"{SheltonpctPassingBothPol}%")
HernandezpctPassingBoth = (HernandezpctPassingMath + HernandezpctPassingReading) / 2
HernandezpctPassingBothPol = np.round(HernandezpctPassingBoth, decimals=2)
HernandezpctPassingBothPol = str(f"{HernandezpctPassingBothPol}%")
GriffinpctPassingBoth = (GriffinpctPassingMath + GriffinpctPassingReading) / 2
GriffinpctPassingBothPol = np.round(GriffinpctPassingBoth, decimals=2)
GriffinpctPassingBothPol = str(f"{GriffinpctPassingBothPol}%")
WilsonpctPassingBoth = (WilsonpctPassingMath + WilsonpctPassingReading) / 2
WilsonpctPassingBothPol = np.round(WilsonpctPassingBoth, decimals=2)
WilsonpctPassingBothPol = str(f"{WilsonpctPassingBothPol}%")
CabrerapctPassingBoth = (CabrerapctPassingMath + CabrerapctPassingReading) / 2
CabrerapctPassingBothPol = np.round(CabrerapctPassingBoth, decimals=2)
CabrerapctPassingBothPol = str(f"{CabrerapctPassingBothPol}%")
BaileypctPassingBoth = (BaileypctPassingMath + BaileypctPassingReading) / 2
BaileypctPassingBothPol = np.round(BaileypctPassingBoth, decimals=2)
BaileypctPassingBothPol = str(f"{BaileypctPassingBothPol}%")
HoldenpctPassingBoth = (HoldenpctPassingMath + HoldenpctPassingReading) / 2
HoldenpctPassingBothPol = np.round(HoldenpctPassingBoth, decimals=2)
HoldenpctPassingBothPol = str(f"{HoldenpctPassingBothPol}%")
PenapctPassingBoth = (PenapctPassingMath + PenapctPassingReading) / 2
PenapctPassingBothPol = np.round(PenapctPassingBoth, decimals=2)
PenapctPassingBothPol = str(f"{PenapctPassingBothPol}%")
WrightpctPassingBoth = (WrightpctPassingMath + WrightpctPassingReading) / 2
WrightpctPassingBothPol = np.round(WrightpctPassingBoth, decimals=2)
WrightpctPassingBothPol = str(f"{WrightpctPassingBothPol}%")
RodriguezpctPassingBoth = (RodriguezpctPassingMath + RodriguezpctPassingReading) / 2
RodriguezpctPassingBothPol = np.round(RodriguezpctPassingBoth, decimals=2)
RodriguezpctPassingBothPol = str(f"{RodriguezpctPassingBothPol}%")
JohnsonpctPassingBoth = (JohnsonpctPassingMath + JohnsonpctPassingReading) / 2
JohnsonpctPassingBothPol = np.round(JohnsonpctPassingBoth, decimals=2)
JohnsonpctPassingBothPol = str(f"{JohnsonpctPassingBothPol}%")
FordpctPassingBoth = (FordpctPassingMath + FordpctPassingReading) / 2
FordpctPassingBothPol = np.round(FordpctPassingBoth, decimals=2)
FordpctPassingBothPol = str(f"{FordpctPassingBothPol}%")
ThomaspctPassingBoth = (ThomaspctPassingMath + ThomaspctPassingReading) / 2
ThomaspctPassingBothPol = np.round(ThomaspctPassingBoth, decimals=2)
ThomaspctPassingBothPol = str(f"{ThomaspctPassingBothPol}%")
#####################################################################################
######################### establish a dataframes containing above
#####################################################################################
HuangSORTING = pd.DataFrame(data={'School Name': [HuangDF.iloc[0, 4]],
                              'School Type': [HuangDF.iloc[0, 8]],
                              'Total Students': [totalStudentsHuangPol],
                              'Total School Budget': [budgetHuangPol],
                              'Per Student Budget': [studentBudgetHuangPol],
                              'Average Math Score': [avgMathScoreHuangPol],
                              'Average Reading Score': [avgReadingScoreHuangPol],
                              '% Passing Math': [HuangpctPassingMathPol],
                              '% Passing Reading': [HuangpctPassingReadingPol],
                              '% Overall Passing Rate': [HuangpctPassingBoth]})
FigueroaSORTING = pd.DataFrame(data={'School Name': [FigueroaDF.iloc[0, 4]],
                                'School Type': [FigueroaDF.iloc[0, 8]],
                                'Total Students': [totalStudentsFigueroaPol],
                                'Total School Budget': [budgetFigueroaPol],
                                'Per Student Budget': [studentBudgetFigueroaPol],
                                'Average Math Score': [avgMathScoreFigueroaPol],
                                'Average Reading Score': [avgReadingScoreFigueroaPol],
                                '% Passing Math': [FigueroapctPassingMathPol],
                                '% Passing Reading': [FigueroapctPassingReadingPol],
                                '% Overall Passing Rate': [FigueroapctPassingBoth]})
SheltonSORTING = pd.DataFrame(data={'School Name': [SheltonDF.iloc[0, 4]],
                                'School Type': [SheltonDF.iloc[0, 8]],
                                'Total Students': [totalStudentsSheltonPol],
                                'Total School Budget': [budgetSheltonPol],
                                'Per Student Budget': [studentBudgetSheltonPol],
                                'Average Math Score': [avgMathScoreSheltonPol],
                                'Average Reading Score': [avgReadingScoreSheltonPol],
                                '% Passing Math': [SheltonpctPassingMathPol],
                                '% Passing Reading': [SheltonpctPassingReadingPol],
                                '% Overall Passing Rate': [SheltonpctPassingBoth]})
HernandezSORTING = pd.DataFrame(data={'School Name': [HernandezDF.iloc[0, 4]],
                                'School Type': [HernandezDF.iloc[0, 8]],
                                'Total Students': [totalStudentsHernandezPol],
                                'Total School Budget': [budgetHernandezPol],
                                'Per Student Budget': [studentBudgetHernandezPol],
                                'Average Math Score': [avgMathScoreHernandezPol],
                                'Average Reading Score': [avgReadingScoreHernandezPol],
                                '% Passing Math': [HernandezpctPassingMathPol],
                                '% Passing Reading': [HernandezpctPassingReadingPol],
                                '% Overall Passing Rate': [HernandezpctPassingBoth]})
GriffinSORTING = pd.DataFrame(data={'School Name': [GriffinDF.iloc[0, 4]],
                                'School Type': [GriffinDF.iloc[0, 8]],
                                'Total Students': [totalStudentsGriffinPol],
                                'Total School Budget': [budgetGriffinPol],
                                'Per Student Budget': [studentBudgetGriffinPol],
                                'Average Math Score': [avgMathScoreGriffinPol],
                                'Average Reading Score': [avgReadingScoreGriffinPol],
                                '% Passing Math': [GriffinpctPassingMathPol],
                                '% Passing Reading': [GriffinpctPassingReadingPol],
                                '% Overall Passing Rate': [GriffinpctPassingBoth]})
WilsonSORTING = pd.DataFrame(data={'School Name': [WilsonDF.iloc[0, 4]],
                                'School Type': [WilsonDF.iloc[0, 8]],
                                'Total Students': [totalStudentsWilsonPol],
                                'Total School Budget': [budgetWilsonPol],
                                'Per Student Budget': [studentBudgetWilsonPol],
                                'Average Math Score': [avgMathScoreWilsonPol],
                                'Average Reading Score': [avgReadingScoreWilsonPol],
                                '% Passing Math': [WilsonpctPassingMathPol],
                                '% Passing Reading': [WilsonpctPassingReadingPol],
                                '% Overall Passing Rate': [WilsonpctPassingBoth]})
CabreraSORTING = pd.DataFrame(data={'School Name': [CabreraDF.iloc[0, 4]],
                                'School Type': [CabreraDF.iloc[0, 8]],
                                'Total Students': [totalStudentsCabreraPol],
                                'Total School Budget': [budgetCabreraPol],
                                'Per Student Budget': [studentBudgetCabreraPol],
                                'Average Math Score': [avgMathScoreCabreraPol],
                                'Average Reading Score': [avgReadingScoreCabreraPol],
                                '% Passing Math': [CabrerapctPassingMathPol],
                                '% Passing Reading': [CabrerapctPassingReadingPol],
                                '% Overall Passing Rate': [CabrerapctPassingBoth]})
BaileySORTING = pd.DataFrame(data={'School Name': [BaileyDF.iloc[0, 4]],
                                'School Type': [BaileyDF.iloc[0, 8]],
                                'Total Students': [totalStudentsBaileyPol],
                                'Total School Budget': [budgetBaileyPol],
                                'Per Student Budget': [studentBudgetBaileyPol],
                                'Average Math Score': [avgMathScoreBaileyPol],
                                'Average Reading Score': [avgReadingScoreBaileyPol],
                                '% Passing Math': [BaileypctPassingMathPol],
                                '% Passing Reading': [BaileypctPassingReadingPol],
                                '% Overall Passing Rate': [BaileypctPassingBoth]})
HoldenSORTING = pd.DataFrame(data={'School Name': [HoldenDF.iloc[0, 4]],
                                'School Type': [HoldenDF.iloc[0, 8]],
                                'Total Students': [totalStudentsHoldenPol],
                                'Total School Budget': [budgetHoldenPol],
                                'Per Student Budget': [studentBudgetHoldenPol],
                                'Average Math Score': [avgMathScoreHoldenPol],
                                'Average Reading Score': [avgReadingScoreHoldenPol],
                                '% Passing Math': [HoldenpctPassingMathPol],
                                '% Passing Reading': [HoldenpctPassingReadingPol],
                                '% Overall Passing Rate': [HoldenpctPassingBoth]})
PenaSORTING = pd.DataFrame(data={'School Name': [PenaDF.iloc[0, 4]],
                                'School Type': [PenaDF.iloc[0, 8]],
                                'Total Students': [totalStudentsPenaPol],
                                'Total School Budget': [budgetPenaPol],
                                'Per Student Budget': [studentBudgetPenaPol],
                                'Average Math Score': [avgMathScorePenaPol],
                                'Average Reading Score': [avgReadingScorePenaPol],
                                '% Passing Math': [PenapctPassingMathPol],
                                '% Passing Reading': [PenapctPassingReadingPol],
                                '% Overall Passing Rate': [PenapctPassingBoth]})
WrightSORTING = pd.DataFrame(data={'School Name': [WrightDF.iloc[0, 4]],
                                'School Type': [WrightDF.iloc[0, 8]],
                                'Total Students': [totalStudentsWrightPol],
                                'Total School Budget': [budgetWrightPol],
                                'Per Student Budget': [studentBudgetWrightPol],
                                'Average Math Score': [avgMathScoreWrightPol],
                                'Average Reading Score': [avgReadingScoreWrightPol],
                                '% Passing Math': [WrightpctPassingMathPol],
                                '% Passing Reading': [WrightpctPassingReadingPol],
                                '% Overall Passing Rate': [WrightpctPassingBoth]})
RodriguezSORTING = pd.DataFrame(data={'School Name': [RodriguezDF.iloc[0, 4]],
                                'School Type': [RodriguezDF.iloc[0, 8]],
                                'Total Students': [totalStudentsRodriguezPol],
                                'Total School Budget': [budgetRodriguezPol],
                                'Per Student Budget': [studentBudgetRodriguezPol],
                                'Average Math Score': [avgMathScoreRodriguezPol],
                                'Average Reading Score': [avgReadingScoreRodriguezPol],
                                '% Passing Math': [RodriguezpctPassingMathPol],
                                '% Passing Reading': [RodriguezpctPassingReadingPol],
                                '% Overall Passing Rate': [RodriguezpctPassingBoth]})
JohnsonSORTING = pd.DataFrame(data={'School Name': [JohnsonDF.iloc[0, 4]],
                                'School Type': [JohnsonDF.iloc[0, 8]],
                                'Total Students': [totalStudentsJohnsonPol],
                                'Total School Budget': [budgetJohnsonPol],
                                'Per Student Budget': [studentBudgetJohnsonPol],
                                'Average Math Score': [avgMathScoreJohnsonPol],
                                'Average Reading Score': [avgReadingScoreJohnsonPol],
                                '% Passing Math': [JohnsonpctPassingMathPol],
                                '% Passing Reading': [JohnsonpctPassingReadingPol],
                                '% Overall Passing Rate': [JohnsonpctPassingBoth]})
FordSORTING = pd.DataFrame(data={'School Name': [FordDF.iloc[0, 4]],
                                'School Type': [FordDF.iloc[0, 8]],
                                'Total Students': [totalStudentsFordPol],
                                'Total School Budget': [budgetFordPol],
                                'Per Student Budget': [studentBudgetFordPol],
                                'Average Math Score': [avgMathScoreFordPol],
                                'Average Reading Score': [avgReadingScoreFordPol],
                                '% Passing Math': [FordpctPassingMathPol],
                                '% Passing Reading': [FordpctPassingReadingPol],
                                '% Overall Passing Rate': [FordpctPassingBoth]})
ThomasSORTING = pd.DataFrame(data={'School Name': [ThomasDF.iloc[0, 4]],
                                'School Type': [ThomasDF.iloc[0, 8]],
                                'Total Students': [totalStudentsThomasPol],
                                'Total School Budget': [budgetThomasPol],
                                'Per Student Budget': [studentBudgetThomasPol],
                                'Average Math Score': [avgMathScoreThomasPol],
                                'Average Reading Score': [avgReadingScoreThomasPol],
                                '% Passing Math': [ThomaspctPassingMathPol],
                                '% Passing Reading': [ThomaspctPassingReadingPol],
                                '% Overall Passing Rate': [ThomaspctPassingBoth]})
#####################################################################################
######################### merge them all together
#####################################################################################
sortingDF = pd.concat([HuangSORTING, FigueroaSORTING, SheltonSORTING, HernandezSORTING, GriffinSORTING, WilsonSORTING, CabreraSORTING, BaileySORTING, HoldenSORTING, PenaSORTING, WrightSORTING, RodriguezSORTING, JohnsonSORTING, FordSORTING, ThomasSORTING, ])
sortingDF_TOP_all = sortingDF.sort_values(by="% Overall Passing Rate", ascending=False)
sortingDF_TOP_5 = sortingDF_TOP_all.head()
sortingDF_BOTTOM_all = sortingDF.sort_values(by="% Overall Passing Rate", ascending=True)
sortingDF_BOTTOM_5 = sortingDF_BOTTOM_all.head()
#####################################################################################
######################### establish avg math grade per grade per school
#####################################################################################
Huang_9 = HuangDF.loc[TopSchoolsDF['Grade'] == "9th"]
Huang_10 = HuangDF.loc[TopSchoolsDF['Grade'] == "10th"]
Huang_11 = HuangDF.loc[TopSchoolsDF['Grade'] == "11th"]
Huang_12 = HuangDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathHuang_9 = Huang_9['Math Score'].mean()
avgMathHuang_9Pol = np.round(avgMathHuang_9, decimals=2)
avgMathHuang_9Pol = str(f"{avgMathHuang_9Pol}%")
avgMathHuang_10 = Huang_10['Math Score'].mean()
avgMathHuang_10Pol = np.round(avgMathHuang_10, decimals=2)
avgMathHuang_10Pol = str(f"{avgMathHuang_10Pol}%")
avgMathHuang_11 = Huang_11['Math Score'].mean()
avgMathHuang_11Pol = np.round(avgMathHuang_11, decimals=2)
avgMathHuang_11Pol = str(f"{avgMathHuang_11Pol}%")
avgMathHuang_12 = Huang_12['Math Score'].mean()
avgMathHuang_12Pol = np.round(avgMathHuang_12, decimals=2)
avgMathHuang_12Pol = str(f"{avgMathHuang_12Pol}%")
Figueroa_9 = FigueroaDF.loc[TopSchoolsDF['Grade'] == "9th"]
Figueroa_10 = FigueroaDF.loc[TopSchoolsDF['Grade'] == "10th"]
Figueroa_11 = FigueroaDF.loc[TopSchoolsDF['Grade'] == "11th"]
Figueroa_12 = FigueroaDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathFigueroa_9 = Figueroa_9['Math Score'].mean()
avgMathFigueroa_9Pol = np.round(avgMathFigueroa_9, decimals=2)
avgMathFigueroa_9Pol = str(f"{avgMathFigueroa_9Pol}%")
avgMathFigueroa_10 = Figueroa_10['Math Score'].mean()
avgMathFigueroa_10Pol = np.round(avgMathFigueroa_10, decimals=2)
avgMathFigueroa_10Pol = str(f"{avgMathFigueroa_10Pol}%")
avgMathFigueroa_11 = Figueroa_11['Math Score'].mean()
avgMathFigueroa_11Pol = np.round(avgMathFigueroa_11, decimals=2)
avgMathFigueroa_11Pol = str(f"{avgMathFigueroa_11Pol}%")
avgMathFigueroa_12 = Figueroa_12['Math Score'].mean()
avgMathFigueroa_12Pol = np.round(avgMathFigueroa_12, decimals=2)
avgMathFigueroa_12Pol = str(f"{avgMathFigueroa_12Pol}%")
Shelton_9 = SheltonDF.loc[TopSchoolsDF['Grade'] == "9th"]
Shelton_10 = SheltonDF.loc[TopSchoolsDF['Grade'] == "10th"]
Shelton_11 = SheltonDF.loc[TopSchoolsDF['Grade'] == "11th"]
Shelton_12 = SheltonDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathShelton_9 = Shelton_9['Math Score'].mean()
avgMathShelton_9Pol = np.round(avgMathShelton_9, decimals=2)
avgMathShelton_9Pol = str(f"{avgMathShelton_9Pol}%")
avgMathShelton_10 = Shelton_10['Math Score'].mean()
avgMathShelton_10Pol = np.round(avgMathShelton_10, decimals=2)
avgMathShelton_10Pol = str(f"{avgMathShelton_10Pol}%")
avgMathShelton_11 = Shelton_11['Math Score'].mean()
avgMathShelton_11Pol = np.round(avgMathShelton_11, decimals=2)
avgMathShelton_11Pol = str(f"{avgMathShelton_11Pol}%")
avgMathShelton_12 = Shelton_12['Math Score'].mean()
avgMathShelton_12Pol = np.round(avgMathShelton_12, decimals=2)
avgMathShelton_12Pol = str(f"{avgMathShelton_12Pol}%")
Hernandez_9 = HernandezDF.loc[TopSchoolsDF['Grade'] == "9th"]
Hernandez_10 = HernandezDF.loc[TopSchoolsDF['Grade'] == "10th"]
Hernandez_11 = HernandezDF.loc[TopSchoolsDF['Grade'] == "11th"]
Hernandez_12 = HernandezDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathHernandez_9 = Hernandez_9['Math Score'].mean()
avgMathHernandez_9Pol = np.round(avgMathHernandez_9, decimals=2)
avgMathHernandez_9Pol = str(f"{avgMathHernandez_9Pol}%")
avgMathHernandez_10 = Hernandez_10['Math Score'].mean()
avgMathHernandez_10Pol = np.round(avgMathHernandez_10, decimals=2)
avgMathHernandez_10Pol = str(f"{avgMathHernandez_10Pol}%")
avgMathHernandez_11 = Hernandez_11['Math Score'].mean()
avgMathHernandez_11Pol = np.round(avgMathHernandez_11, decimals=2)
avgMathHernandez_11Pol = str(f"{avgMathHernandez_11Pol}%")
avgMathHernandez_12 = Hernandez_12['Math Score'].mean()
avgMathHernandez_12Pol = np.round(avgMathHernandez_12, decimals=2)
avgMathHernandez_12Pol = str(f"{avgMathHernandez_12Pol}%")
Griffin_9 = GriffinDF.loc[TopSchoolsDF['Grade'] == "9th"]
Griffin_10 = GriffinDF.loc[TopSchoolsDF['Grade'] == "10th"]
Griffin_11 = GriffinDF.loc[TopSchoolsDF['Grade'] == "11th"]
Griffin_12 = GriffinDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathGriffin_9 = Griffin_9['Math Score'].mean()
avgMathGriffin_9Pol = np.round(avgMathGriffin_9, decimals=2)
avgMathGriffin_9Pol = str(f"{avgMathGriffin_9Pol}%")
avgMathGriffin_10 = Griffin_10['Math Score'].mean()
avgMathGriffin_10Pol = np.round(avgMathGriffin_10, decimals=2)
avgMathGriffin_10Pol = str(f"{avgMathGriffin_10Pol}%")
avgMathGriffin_11 = Griffin_11['Math Score'].mean()
avgMathGriffin_11Pol = np.round(avgMathGriffin_11, decimals=2)
avgMathGriffin_11Pol = str(f"{avgMathGriffin_11Pol}%")
avgMathGriffin_12 = Griffin_12['Math Score'].mean()
avgMathGriffin_12Pol = np.round(avgMathGriffin_12, decimals=2)
avgMathGriffin_12Pol = str(f"{avgMathGriffin_12Pol}%")
Wilson_9 = WilsonDF.loc[TopSchoolsDF['Grade'] == "9th"]
Wilson_10 = WilsonDF.loc[TopSchoolsDF['Grade'] == "10th"]
Wilson_11 = WilsonDF.loc[TopSchoolsDF['Grade'] == "11th"]
Wilson_12 = WilsonDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathWilson_9 = Wilson_9['Math Score'].mean()
avgMathWilson_9Pol = np.round(avgMathWilson_9, decimals=2)
avgMathWilson_9Pol = str(f"{avgMathWilson_9Pol}%")
avgMathWilson_10 = Wilson_10['Math Score'].mean()
avgMathWilson_10Pol = np.round(avgMathWilson_10, decimals=2)
avgMathWilson_10Pol = str(f"{avgMathWilson_10Pol}%")
avgMathWilson_11 = Wilson_11['Math Score'].mean()
avgMathWilson_11Pol = np.round(avgMathWilson_11, decimals=2)
avgMathWilson_11Pol = str(f"{avgMathWilson_11Pol}%")
avgMathWilson_12 = Wilson_12['Math Score'].mean()
avgMathWilson_12Pol = np.round(avgMathWilson_12, decimals=2)
avgMathWilson_12Pol = str(f"{avgMathWilson_12Pol}%")
Cabrera_9 = CabreraDF.loc[TopSchoolsDF['Grade'] == "9th"]
Cabrera_10 = CabreraDF.loc[TopSchoolsDF['Grade'] == "10th"]
Cabrera_11 = CabreraDF.loc[TopSchoolsDF['Grade'] == "11th"]
Cabrera_12 = CabreraDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathCabrera_9 = Cabrera_9['Math Score'].mean()
avgMathCabrera_9Pol = np.round(avgMathCabrera_9, decimals=2)
avgMathCabrera_9Pol = str(f"{avgMathCabrera_9Pol}%")
avgMathCabrera_10 = Cabrera_10['Math Score'].mean()
avgMathCabrera_10Pol = np.round(avgMathCabrera_10, decimals=2)
avgMathCabrera_10Pol = str(f"{avgMathCabrera_10Pol}%")
avgMathCabrera_11 = Cabrera_11['Math Score'].mean()
avgMathCabrera_11Pol = np.round(avgMathCabrera_11, decimals=2)
avgMathCabrera_11Pol = str(f"{avgMathCabrera_11Pol}%")
avgMathCabrera_12 = Cabrera_12['Math Score'].mean()
avgMathCabrera_12Pol = np.round(avgMathCabrera_12, decimals=2)
avgMathCabrera_12Pol = str(f"{avgMathCabrera_12Pol}%")
Bailey_9 = BaileyDF.loc[TopSchoolsDF['Grade'] == "9th"]
Bailey_10 = BaileyDF.loc[TopSchoolsDF['Grade'] == "10th"]
Bailey_11 = BaileyDF.loc[TopSchoolsDF['Grade'] == "11th"]
Bailey_12 = BaileyDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathBailey_9 = Bailey_9['Math Score'].mean()
avgMathBailey_9Pol = np.round(avgMathBailey_9, decimals=2)
avgMathBailey_9Pol = str(f"{avgMathBailey_9Pol}%")
avgMathBailey_10 = Bailey_10['Math Score'].mean()
avgMathBailey_10Pol = np.round(avgMathBailey_10, decimals=2)
avgMathBailey_10Pol = str(f"{avgMathBailey_10Pol}%")
avgMathBailey_11 = Bailey_11['Math Score'].mean()
avgMathBailey_11Pol = np.round(avgMathBailey_11, decimals=2)
avgMathBailey_11Pol = str(f"{avgMathBailey_11Pol}%")
avgMathBailey_12 = Bailey_12['Math Score'].mean()
avgMathBailey_12Pol = np.round(avgMathBailey_12, decimals=2)
avgMathBailey_12Pol = str(f"{avgMathBailey_12Pol}%")
Holden_9 = HoldenDF.loc[TopSchoolsDF['Grade'] == "9th"]
Holden_10 = HoldenDF.loc[TopSchoolsDF['Grade'] == "10th"]
Holden_11 = HoldenDF.loc[TopSchoolsDF['Grade'] == "11th"]
Holden_12 = HoldenDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathHolden_9 = Holden_9['Math Score'].mean()
avgMathHolden_9Pol = np.round(avgMathHolden_9, decimals=2)
avgMathHolden_9Pol = str(f"{avgMathHolden_9Pol}%")
avgMathHolden_10 = Holden_10['Math Score'].mean()
avgMathHolden_10Pol = np.round(avgMathHolden_10, decimals=2)
avgMathHolden_10Pol = str(f"{avgMathHolden_10Pol}%")
avgMathHolden_11 = Holden_11['Math Score'].mean()
avgMathHolden_11Pol = np.round(avgMathHolden_11, decimals=2)
avgMathHolden_11Pol = str(f"{avgMathHolden_11Pol}%")
avgMathHolden_12 = Holden_12['Math Score'].mean()
avgMathHolden_12Pol = np.round(avgMathHolden_12, decimals=2)
avgMathHolden_12Pol = str(f"{avgMathHolden_12Pol}%")
Pena_9 = PenaDF.loc[TopSchoolsDF['Grade'] == "9th"]
Pena_10 = PenaDF.loc[TopSchoolsDF['Grade'] == "10th"]
Pena_11 = PenaDF.loc[TopSchoolsDF['Grade'] == "11th"]
Pena_12 = PenaDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathPena_9 = Pena_9['Math Score'].mean()
avgMathPena_9Pol = np.round(avgMathPena_9, decimals=2)
avgMathPena_9Pol = str(f"{avgMathPena_9Pol}%")
avgMathPena_10 = Pena_10['Math Score'].mean()
avgMathPena_10Pol = np.round(avgMathPena_10, decimals=2)
avgMathPena_10Pol = str(f"{avgMathPena_10Pol}%")
avgMathPena_11 = Pena_11['Math Score'].mean()
avgMathPena_11Pol = np.round(avgMathPena_11, decimals=2)
avgMathPena_11Pol = str(f"{avgMathPena_11Pol}%")
avgMathPena_12 = Pena_12['Math Score'].mean()
avgMathPena_12Pol = np.round(avgMathPena_12, decimals=2)
avgMathPena_12Pol = str(f"{avgMathPena_12Pol}%")
Wright_9 = WrightDF.loc[TopSchoolsDF['Grade'] == "9th"]
Wright_10 = WrightDF.loc[TopSchoolsDF['Grade'] == "10th"]
Wright_11 = WrightDF.loc[TopSchoolsDF['Grade'] == "11th"]
Wright_12 = WrightDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathWright_9 = Wright_9['Math Score'].mean()
avgMathWright_9Pol = np.round(avgMathWright_9, decimals=2)
avgMathWright_9Pol = str(f"{avgMathWright_9Pol}%")
avgMathWright_10 = Wright_10['Math Score'].mean()
avgMathWright_10Pol = np.round(avgMathWright_10, decimals=2)
avgMathWright_10Pol = str(f"{avgMathWright_10Pol}%")
avgMathWright_11 = Wright_11['Math Score'].mean()
avgMathWright_11Pol = np.round(avgMathWright_11, decimals=2)
avgMathWright_11Pol = str(f"{avgMathWright_11Pol}%")
avgMathWright_12 = Wright_12['Math Score'].mean()
avgMathWright_12Pol = np.round(avgMathWright_12, decimals=2)
avgMathWright_12Pol = str(f"{avgMathWright_12Pol}%")
Rodriguez_9 = RodriguezDF.loc[TopSchoolsDF['Grade'] == "9th"]
Rodriguez_10 = RodriguezDF.loc[TopSchoolsDF['Grade'] == "10th"]
Rodriguez_11 = RodriguezDF.loc[TopSchoolsDF['Grade'] == "11th"]
Rodriguez_12 = RodriguezDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathRodriguez_9 = Rodriguez_9['Math Score'].mean()
avgMathRodriguez_9Pol = np.round(avgMathRodriguez_9, decimals=2)
avgMathRodriguez_9Pol = str(f"{avgMathRodriguez_9Pol}%")
avgMathRodriguez_10 = Rodriguez_10['Math Score'].mean()
avgMathRodriguez_10Pol = np.round(avgMathRodriguez_10, decimals=2)
avgMathRodriguez_10Pol = str(f"{avgMathRodriguez_10Pol}%")
avgMathRodriguez_11 = Rodriguez_11['Math Score'].mean()
avgMathRodriguez_11Pol = np.round(avgMathRodriguez_11, decimals=2)
avgMathRodriguez_11Pol = str(f"{avgMathRodriguez_11Pol}%")
avgMathRodriguez_12 = Rodriguez_12['Math Score'].mean()
avgMathRodriguez_12Pol = np.round(avgMathRodriguez_12, decimals=2)
avgMathRodriguez_12Pol = str(f"{avgMathRodriguez_12Pol}%")
Johnson_9 = JohnsonDF.loc[TopSchoolsDF['Grade'] == "9th"]
Johnson_10 = JohnsonDF.loc[TopSchoolsDF['Grade'] == "10th"]
Johnson_11 = JohnsonDF.loc[TopSchoolsDF['Grade'] == "11th"]
Johnson_12 = JohnsonDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathJohnson_9 = Johnson_9['Math Score'].mean()
avgMathJohnson_9Pol = np.round(avgMathJohnson_9, decimals=2)
avgMathJohnson_9Pol = str(f"{avgMathJohnson_9Pol}%")
avgMathJohnson_10 = Johnson_10['Math Score'].mean()
avgMathJohnson_10Pol = np.round(avgMathJohnson_10, decimals=2)
avgMathJohnson_10Pol = str(f"{avgMathJohnson_10Pol}%")
avgMathJohnson_11 = Johnson_11['Math Score'].mean()
avgMathJohnson_11Pol = np.round(avgMathJohnson_11, decimals=2)
avgMathJohnson_11Pol = str(f"{avgMathJohnson_11Pol}%")
avgMathJohnson_12 = Johnson_12['Math Score'].mean()
avgMathJohnson_12Pol = np.round(avgMathJohnson_12, decimals=2)
avgMathJohnson_12Pol = str(f"{avgMathJohnson_12Pol}%")
Ford_9 = FordDF.loc[TopSchoolsDF['Grade'] == "9th"]
Ford_10 = FordDF.loc[TopSchoolsDF['Grade'] == "10th"]
Ford_11 = FordDF.loc[TopSchoolsDF['Grade'] == "11th"]
Ford_12 = FordDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathFord_9 = Ford_9['Math Score'].mean()
avgMathFord_9Pol = np.round(avgMathFord_9, decimals=2)
avgMathFord_9Pol = str(f"{avgMathFord_9Pol}%")
avgMathFord_10 = Ford_10['Math Score'].mean()
avgMathFord_10Pol = np.round(avgMathFord_10, decimals=2)
avgMathFord_10Pol = str(f"{avgMathFord_10Pol}%")
avgMathFord_11 = Ford_11['Math Score'].mean()
avgMathFord_11Pol = np.round(avgMathFord_11, decimals=2)
avgMathFord_11Pol = str(f"{avgMathFord_11Pol}%")
avgMathFord_12 = Ford_12['Math Score'].mean()
avgMathFord_12Pol = np.round(avgMathFord_12, decimals=2)
avgMathFord_12Pol = str(f"{avgMathFord_12Pol}%")
Thomas_9 = ThomasDF.loc[TopSchoolsDF['Grade'] == "9th"]
Thomas_10 = ThomasDF.loc[TopSchoolsDF['Grade'] == "10th"]
Thomas_11 = ThomasDF.loc[TopSchoolsDF['Grade'] == "11th"]
Thomas_12 = ThomasDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgMathThomas_9 = Thomas_9['Math Score'].mean()
avgMathThomas_9Pol = np.round(avgMathThomas_9, decimals=2)
avgMathThomas_9Pol = str(f"{avgMathThomas_9Pol}%")
avgMathThomas_10 = Thomas_10['Math Score'].mean()
avgMathThomas_10Pol = np.round(avgMathThomas_10, decimals=2)
avgMathThomas_10Pol = str(f"{avgMathThomas_10Pol}%")
avgMathThomas_11 = Thomas_11['Math Score'].mean()
avgMathThomas_11Pol = np.round(avgMathThomas_11, decimals=2)
avgMathThomas_11Pol = str(f"{avgMathThomas_11Pol}%")
avgMathThomas_12 = Thomas_12['Math Score'].mean()
avgMathThomas_12Pol = np.round(avgMathThomas_12, decimals=2)
avgMathThomas_12Pol = str(f"{avgMathThomas_12Pol}%")
#####################################################################################
######################### establish a dataframes containing above
#####################################################################################
HuangMath_byGrade = pd.DataFrame(data={'School Name': [HuangDF.iloc[0, 4]],
                                      '9th Grade': [avgMathHuang_9Pol],
                                      '10th Grade': [avgMathHuang_10Pol],
                                      '11th Grade': [avgMathHuang_11Pol],
                                      '12th Grade': [avgMathHuang_12Pol]})
FigueroaMath_byGrade = pd.DataFrame(data={'School Name': [FigueroaDF.iloc[0, 4]],
                                      '9th Grade': [avgMathFigueroa_9Pol],
                                      '10th Grade': [avgMathFigueroa_10Pol],
                                      '11th Grade': [avgMathFigueroa_11Pol],
                                      '12th Grade': [avgMathFigueroa_12Pol]})
SheltonMath_byGrade = pd.DataFrame(data={'School Name': [SheltonDF.iloc[0, 4]],
                                      '9th Grade': [avgMathShelton_9Pol],
                                      '10th Grade': [avgMathShelton_10Pol],
                                      '11th Grade': [avgMathShelton_11Pol],
                                      '12th Grade': [avgMathShelton_12Pol]})
HernandezMath_byGrade = pd.DataFrame(data={'School Name': [HernandezDF.iloc[0, 4]],
                                      '9th Grade': [avgMathHernandez_9Pol],
                                      '10th Grade': [avgMathHernandez_10Pol],
                                      '11th Grade': [avgMathHernandez_11Pol],
                                      '12th Grade': [avgMathHernandez_12Pol]})
GriffinMath_byGrade = pd.DataFrame(data={'School Name': [GriffinDF.iloc[0, 4]],
                                      '9th Grade': [avgMathGriffin_9Pol],
                                      '10th Grade': [avgMathGriffin_10Pol],
                                      '11th Grade': [avgMathGriffin_11Pol],
                                      '12th Grade': [avgMathGriffin_12Pol]})
WilsonMath_byGrade = pd.DataFrame(data={'School Name': [WilsonDF.iloc[0, 4]],
                                      '9th Grade': [avgMathWilson_9Pol],
                                      '10th Grade': [avgMathWilson_10Pol],
                                      '11th Grade': [avgMathWilson_11Pol],
                                      '12th Grade': [avgMathWilson_12Pol]})
CabreraMath_byGrade = pd.DataFrame(data={'School Name': [CabreraDF.iloc[0, 4]],
                                      '9th Grade': [avgMathCabrera_9Pol],
                                      '10th Grade': [avgMathCabrera_10Pol],
                                      '11th Grade': [avgMathCabrera_11Pol],
                                      '12th Grade': [avgMathCabrera_12Pol]})
BaileyMath_byGrade = pd.DataFrame(data={'School Name': [BaileyDF.iloc[0, 4]],
                                      '9th Grade': [avgMathBailey_9Pol],
                                      '10th Grade': [avgMathBailey_10Pol],
                                      '11th Grade': [avgMathBailey_11Pol],
                                      '12th Grade': [avgMathBailey_12Pol]})
HoldenMath_byGrade = pd.DataFrame(data={'School Name': [HoldenDF.iloc[0, 4]],
                                      '9th Grade': [avgMathHolden_9Pol],
                                      '10th Grade': [avgMathHolden_10Pol],
                                      '11th Grade': [avgMathHolden_11Pol],
                                      '12th Grade': [avgMathHolden_12Pol]})
PenaMath_byGrade = pd.DataFrame(data={'School Name': [PenaDF.iloc[0, 4]],
                                      '9th Grade': [avgMathPena_9Pol],
                                      '10th Grade': [avgMathPena_10Pol],
                                      '11th Grade': [avgMathPena_11Pol],
                                      '12th Grade': [avgMathPena_12Pol]})
WrightMath_byGrade = pd.DataFrame(data={'School Name': [WrightDF.iloc[0, 4]],
                                      '9th Grade': [avgMathWright_9Pol],
                                      '10th Grade': [avgMathWright_10Pol],
                                      '11th Grade': [avgMathWright_11Pol],
                                      '12th Grade': [avgMathWright_12Pol]})
RodriguezMath_byGrade = pd.DataFrame(data={'School Name': [RodriguezDF.iloc[0, 4]],
                                      '9th Grade': [avgMathRodriguez_9Pol],
                                      '10th Grade': [avgMathRodriguez_10Pol],
                                      '11th Grade': [avgMathRodriguez_11Pol],
                                      '12th Grade': [avgMathRodriguez_12Pol]})
JohnsonMath_byGrade = pd.DataFrame(data={'School Name': [JohnsonDF.iloc[0, 4]],
                                      '9th Grade': [avgMathJohnson_9Pol],
                                      '10th Grade': [avgMathJohnson_10Pol],
                                      '11th Grade': [avgMathJohnson_11Pol],
                                      '12th Grade': [avgMathJohnson_12Pol]})
FordMath_byGrade = pd.DataFrame(data={'School Name': [FordDF.iloc[0, 4]],
                                      '9th Grade': [avgMathFord_9Pol],
                                      '10th Grade': [avgMathFord_10Pol],
                                      '11th Grade': [avgMathFord_11Pol],
                                      '12th Grade': [avgMathFord_12Pol]})
ThomasMath_byGrade = pd.DataFrame(data={'School Name': [ThomasDF.iloc[0, 4]],
                                      '9th Grade': [avgMathThomas_9Pol],
                                      '10th Grade': [avgMathThomas_10Pol],
                                      '11th Grade': [avgMathThomas_11Pol],
                                      '12th Grade': [avgMathThomas_12Pol]})
#####################################################################################
######################### establish a DF containing all DFs above, sort alphabetically
#####################################################################################
AllSchoolsMath_byGrade = pd.concat([HuangMath_byGrade, FigueroaMath_byGrade, SheltonMath_byGrade, HernandezMath_byGrade, GriffinMath_byGrade, WilsonMath_byGrade, CabreraMath_byGrade, BaileyMath_byGrade, HoldenMath_byGrade, PenaMath_byGrade, WrightMath_byGrade, RodriguezMath_byGrade, JohnsonMath_byGrade, FordMath_byGrade, ThomasMath_byGrade])
AllSchoolsMath_byGrade = AllSchoolsMath_byGrade.sort_values(by="School Name", ascending=True)
#####################################################################################
######################### establish avg reading grade per grade per school
#####################################################################################
Huang_9 = HuangDF.loc[TopSchoolsDF['Grade'] == "9th"]
Huang_10 = HuangDF.loc[TopSchoolsDF['Grade'] == "10th"]
Huang_11 = HuangDF.loc[TopSchoolsDF['Grade'] == "11th"]
Huang_12 = HuangDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingHuang_9 = Huang_9['Reading Score'].mean()
avgReadingHuang_9Pol = np.round(avgReadingHuang_9, decimals=2)
avgReadingHuang_9Pol = str(f"{avgReadingHuang_9Pol}%")
avgReadingHuang_10 = Huang_10['Reading Score'].mean()
avgReadingHuang_10Pol = np.round(avgReadingHuang_10, decimals=2)
avgReadingHuang_10Pol = str(f"{avgReadingHuang_10Pol}%")
avgReadingHuang_11 = Huang_11['Reading Score'].mean()
avgReadingHuang_11Pol = np.round(avgReadingHuang_11, decimals=2)
avgReadingHuang_11Pol = str(f"{avgReadingHuang_11Pol}%")
avgReadingHuang_12 = Huang_12['Reading Score'].mean()
avgReadingHuang_12Pol = np.round(avgReadingHuang_12, decimals=2)
avgReadingHuang_12Pol = str(f"{avgReadingHuang_12Pol}%")
Figueroa_9 = FigueroaDF.loc[TopSchoolsDF['Grade'] == "9th"]
Figueroa_10 = FigueroaDF.loc[TopSchoolsDF['Grade'] == "10th"]
Figueroa_11 = FigueroaDF.loc[TopSchoolsDF['Grade'] == "11th"]
Figueroa_12 = FigueroaDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingFigueroa_9 = Figueroa_9['Reading Score'].mean()
avgReadingFigueroa_9Pol = np.round(avgReadingFigueroa_9, decimals=2)
avgReadingFigueroa_9Pol = str(f"{avgReadingFigueroa_9Pol}%")
avgReadingFigueroa_10 = Figueroa_10['Reading Score'].mean()
avgReadingFigueroa_10Pol = np.round(avgReadingFigueroa_10, decimals=2)
avgReadingFigueroa_10Pol = str(f"{avgReadingFigueroa_10Pol}%")
avgReadingFigueroa_11 = Figueroa_11['Reading Score'].mean()
avgReadingFigueroa_11Pol = np.round(avgReadingFigueroa_11, decimals=2)
avgReadingFigueroa_11Pol = str(f"{avgReadingFigueroa_11Pol}%")
avgReadingFigueroa_12 = Figueroa_12['Reading Score'].mean()
avgReadingFigueroa_12Pol = np.round(avgReadingFigueroa_12, decimals=2)
avgReadingFigueroa_12Pol = str(f"{avgReadingFigueroa_12Pol}%")
Shelton_9 = SheltonDF.loc[TopSchoolsDF['Grade'] == "9th"]
Shelton_10 = SheltonDF.loc[TopSchoolsDF['Grade'] == "10th"]
Shelton_11 = SheltonDF.loc[TopSchoolsDF['Grade'] == "11th"]
Shelton_12 = SheltonDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingShelton_9 = Shelton_9['Reading Score'].mean()
avgReadingShelton_9Pol = np.round(avgReadingShelton_9, decimals=2)
avgReadingShelton_9Pol = str(f"{avgReadingShelton_9Pol}%")
avgReadingShelton_10 = Shelton_10['Reading Score'].mean()
avgReadingShelton_10Pol = np.round(avgReadingShelton_10, decimals=2)
avgReadingShelton_10Pol = str(f"{avgReadingShelton_10Pol}%")
avgReadingShelton_11 = Shelton_11['Reading Score'].mean()
avgReadingShelton_11Pol = np.round(avgReadingShelton_11, decimals=2)
avgReadingShelton_11Pol = str(f"{avgReadingShelton_11Pol}%")
avgReadingShelton_12 = Shelton_12['Reading Score'].mean()
avgReadingShelton_12Pol = np.round(avgReadingShelton_12, decimals=2)
avgReadingShelton_12Pol = str(f"{avgReadingShelton_12Pol}%")
Hernandez_9 = HernandezDF.loc[TopSchoolsDF['Grade'] == "9th"]
Hernandez_10 = HernandezDF.loc[TopSchoolsDF['Grade'] == "10th"]
Hernandez_11 = HernandezDF.loc[TopSchoolsDF['Grade'] == "11th"]
Hernandez_12 = HernandezDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingHernandez_9 = Hernandez_9['Reading Score'].mean()
avgReadingHernandez_9Pol = np.round(avgReadingHernandez_9, decimals=2)
avgReadingHernandez_9Pol = str(f"{avgReadingHernandez_9Pol}%")
avgReadingHernandez_10 = Hernandez_10['Reading Score'].mean()
avgReadingHernandez_10Pol = np.round(avgReadingHernandez_10, decimals=2)
avgReadingHernandez_10Pol = str(f"{avgReadingHernandez_10Pol}%")
avgReadingHernandez_11 = Hernandez_11['Reading Score'].mean()
avgReadingHernandez_11Pol = np.round(avgReadingHernandez_11, decimals=2)
avgReadingHernandez_11Pol = str(f"{avgReadingHernandez_11Pol}%")
avgReadingHernandez_12 = Hernandez_12['Reading Score'].mean()
avgReadingHernandez_12Pol = np.round(avgReadingHernandez_12, decimals=2)
avgReadingHernandez_12Pol = str(f"{avgReadingHernandez_12Pol}%")
Griffin_9 = GriffinDF.loc[TopSchoolsDF['Grade'] == "9th"]
Griffin_10 = GriffinDF.loc[TopSchoolsDF['Grade'] == "10th"]
Griffin_11 = GriffinDF.loc[TopSchoolsDF['Grade'] == "11th"]
Griffin_12 = GriffinDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingGriffin_9 = Griffin_9['Reading Score'].mean()
avgReadingGriffin_9Pol = np.round(avgReadingGriffin_9, decimals=2)
avgReadingGriffin_9Pol = str(f"{avgReadingGriffin_9Pol}%")
avgReadingGriffin_10 = Griffin_10['Reading Score'].mean()
avgReadingGriffin_10Pol = np.round(avgReadingGriffin_10, decimals=2)
avgReadingGriffin_10Pol = str(f"{avgReadingGriffin_10Pol}%")
avgReadingGriffin_11 = Griffin_11['Reading Score'].mean()
avgReadingGriffin_11Pol = np.round(avgReadingGriffin_11, decimals=2)
avgReadingGriffin_11Pol = str(f"{avgReadingGriffin_11Pol}%")
avgReadingGriffin_12 = Griffin_12['Reading Score'].mean()
avgReadingGriffin_12Pol = np.round(avgReadingGriffin_12, decimals=2)
avgReadingGriffin_12Pol = str(f"{avgReadingGriffin_12Pol}%")
Wilson_9 = WilsonDF.loc[TopSchoolsDF['Grade'] == "9th"]
Wilson_10 = WilsonDF.loc[TopSchoolsDF['Grade'] == "10th"]
Wilson_11 = WilsonDF.loc[TopSchoolsDF['Grade'] == "11th"]
Wilson_12 = WilsonDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingWilson_9 = Wilson_9['Reading Score'].mean()
avgReadingWilson_9Pol = np.round(avgReadingWilson_9, decimals=2)
avgReadingWilson_9Pol = str(f"{avgReadingWilson_9Pol}%")
avgReadingWilson_10 = Wilson_10['Reading Score'].mean()
avgReadingWilson_10Pol = np.round(avgReadingWilson_10, decimals=2)
avgReadingWilson_10Pol = str(f"{avgReadingWilson_10Pol}%")
avgReadingWilson_11 = Wilson_11['Reading Score'].mean()
avgReadingWilson_11Pol = np.round(avgReadingWilson_11, decimals=2)
avgReadingWilson_11Pol = str(f"{avgReadingWilson_11Pol}%")
avgReadingWilson_12 = Wilson_12['Reading Score'].mean()
avgReadingWilson_12Pol = np.round(avgReadingWilson_12, decimals=2)
avgReadingWilson_12Pol = str(f"{avgReadingWilson_12Pol}%")
Cabrera_9 = CabreraDF.loc[TopSchoolsDF['Grade'] == "9th"]
Cabrera_10 = CabreraDF.loc[TopSchoolsDF['Grade'] == "10th"]
Cabrera_11 = CabreraDF.loc[TopSchoolsDF['Grade'] == "11th"]
Cabrera_12 = CabreraDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingCabrera_9 = Cabrera_9['Reading Score'].mean()
avgReadingCabrera_9Pol = np.round(avgReadingCabrera_9, decimals=2)
avgReadingCabrera_9Pol = str(f"{avgReadingCabrera_9Pol}%")
avgReadingCabrera_10 = Cabrera_10['Reading Score'].mean()
avgReadingCabrera_10Pol = np.round(avgReadingCabrera_10, decimals=2)
avgReadingCabrera_10Pol = str(f"{avgReadingCabrera_10Pol}%")
avgReadingCabrera_11 = Cabrera_11['Reading Score'].mean()
avgReadingCabrera_11Pol = np.round(avgReadingCabrera_11, decimals=2)
avgReadingCabrera_11Pol = str(f"{avgReadingCabrera_11Pol}%")
avgReadingCabrera_12 = Cabrera_12['Reading Score'].mean()
avgReadingCabrera_12Pol = np.round(avgReadingCabrera_12, decimals=2)
avgReadingCabrera_12Pol = str(f"{avgReadingCabrera_12Pol}%")
Bailey_9 = BaileyDF.loc[TopSchoolsDF['Grade'] == "9th"]
Bailey_10 = BaileyDF.loc[TopSchoolsDF['Grade'] == "10th"]
Bailey_11 = BaileyDF.loc[TopSchoolsDF['Grade'] == "11th"]
Bailey_12 = BaileyDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingBailey_9 = Bailey_9['Reading Score'].mean()
avgReadingBailey_9Pol = np.round(avgReadingBailey_9, decimals=2)
avgReadingBailey_9Pol = str(f"{avgReadingBailey_9Pol}%")
avgReadingBailey_10 = Bailey_10['Reading Score'].mean()
avgReadingBailey_10Pol = np.round(avgReadingBailey_10, decimals=2)
avgReadingBailey_10Pol = str(f"{avgReadingBailey_10Pol}%")
avgReadingBailey_11 = Bailey_11['Reading Score'].mean()
avgReadingBailey_11Pol = np.round(avgReadingBailey_11, decimals=2)
avgReadingBailey_11Pol = str(f"{avgReadingBailey_11Pol}%")
avgReadingBailey_12 = Bailey_12['Reading Score'].mean()
avgReadingBailey_12Pol = np.round(avgReadingBailey_12, decimals=2)
avgReadingBailey_12Pol = str(f"{avgReadingBailey_12Pol}%")
Holden_9 = HoldenDF.loc[TopSchoolsDF['Grade'] == "9th"]
Holden_10 = HoldenDF.loc[TopSchoolsDF['Grade'] == "10th"]
Holden_11 = HoldenDF.loc[TopSchoolsDF['Grade'] == "11th"]
Holden_12 = HoldenDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingHolden_9 = Holden_9['Reading Score'].mean()
avgReadingHolden_9Pol = np.round(avgReadingHolden_9, decimals=2)
avgReadingHolden_9Pol = str(f"{avgReadingHolden_9Pol}%")
avgReadingHolden_10 = Holden_10['Reading Score'].mean()
avgReadingHolden_10Pol = np.round(avgReadingHolden_10, decimals=2)
avgReadingHolden_10Pol = str(f"{avgReadingHolden_10Pol}%")
avgReadingHolden_11 = Holden_11['Reading Score'].mean()
avgReadingHolden_11Pol = np.round(avgReadingHolden_11, decimals=2)
avgReadingHolden_11Pol = str(f"{avgReadingHolden_11Pol}%")
avgReadingHolden_12 = Holden_12['Reading Score'].mean()
avgReadingHolden_12Pol = np.round(avgReadingHolden_12, decimals=2)
avgReadingHolden_12Pol = str(f"{avgReadingHolden_12Pol}%")
Pena_9 = PenaDF.loc[TopSchoolsDF['Grade'] == "9th"]
Pena_10 = PenaDF.loc[TopSchoolsDF['Grade'] == "10th"]
Pena_11 = PenaDF.loc[TopSchoolsDF['Grade'] == "11th"]
Pena_12 = PenaDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingPena_9 = Pena_9['Reading Score'].mean()
avgReadingPena_9Pol = np.round(avgReadingPena_9, decimals=2)
avgReadingPena_9Pol = str(f"{avgReadingPena_9Pol}%")
avgReadingPena_10 = Pena_10['Reading Score'].mean()
avgReadingPena_10Pol = np.round(avgReadingPena_10, decimals=2)
avgReadingPena_10Pol = str(f"{avgReadingPena_10Pol}%")
avgReadingPena_11 = Pena_11['Reading Score'].mean()
avgReadingPena_11Pol = np.round(avgReadingPena_11, decimals=2)
avgReadingPena_11Pol = str(f"{avgReadingPena_11Pol}%")
avgReadingPena_12 = Pena_12['Reading Score'].mean()
avgReadingPena_12Pol = np.round(avgReadingPena_12, decimals=2)
avgReadingPena_12Pol = str(f"{avgReadingPena_12Pol}%")
Wright_9 = WrightDF.loc[TopSchoolsDF['Grade'] == "9th"]
Wright_10 = WrightDF.loc[TopSchoolsDF['Grade'] == "10th"]
Wright_11 = WrightDF.loc[TopSchoolsDF['Grade'] == "11th"]
Wright_12 = WrightDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingWright_9 = Wright_9['Reading Score'].mean()
avgReadingWright_9Pol = np.round(avgReadingWright_9, decimals=2)
avgReadingWright_9Pol = str(f"{avgReadingWright_9Pol}%")
avgReadingWright_10 = Wright_10['Reading Score'].mean()
avgReadingWright_10Pol = np.round(avgReadingWright_10, decimals=2)
avgReadingWright_10Pol = str(f"{avgReadingWright_10Pol}%")
avgReadingWright_11 = Wright_11['Reading Score'].mean()
avgReadingWright_11Pol = np.round(avgReadingWright_11, decimals=2)
avgReadingWright_11Pol = str(f"{avgReadingWright_11Pol}%")
avgReadingWright_12 = Wright_12['Reading Score'].mean()
avgReadingWright_12Pol = np.round(avgReadingWright_12, decimals=2)
avgReadingWright_12Pol = str(f"{avgReadingWright_12Pol}%")
Rodriguez_9 = RodriguezDF.loc[TopSchoolsDF['Grade'] == "9th"]
Rodriguez_10 = RodriguezDF.loc[TopSchoolsDF['Grade'] == "10th"]
Rodriguez_11 = RodriguezDF.loc[TopSchoolsDF['Grade'] == "11th"]
Rodriguez_12 = RodriguezDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingRodriguez_9 = Rodriguez_9['Reading Score'].mean()
avgReadingRodriguez_9Pol = np.round(avgReadingRodriguez_9, decimals=2)
avgReadingRodriguez_9Pol = str(f"{avgReadingRodriguez_9Pol}%")
avgReadingRodriguez_10 = Rodriguez_10['Reading Score'].mean()
avgReadingRodriguez_10Pol = np.round(avgReadingRodriguez_10, decimals=2)
avgReadingRodriguez_10Pol = str(f"{avgReadingRodriguez_10Pol}%")
avgReadingRodriguez_11 = Rodriguez_11['Reading Score'].mean()
avgReadingRodriguez_11Pol = np.round(avgReadingRodriguez_11, decimals=2)
avgReadingRodriguez_11Pol = str(f"{avgReadingRodriguez_11Pol}%")
avgReadingRodriguez_12 = Rodriguez_12['Reading Score'].mean()
avgReadingRodriguez_12Pol = np.round(avgReadingRodriguez_12, decimals=2)
avgReadingRodriguez_12Pol = str(f"{avgReadingRodriguez_12Pol}%")
Johnson_9 = JohnsonDF.loc[TopSchoolsDF['Grade'] == "9th"]
Johnson_10 = JohnsonDF.loc[TopSchoolsDF['Grade'] == "10th"]
Johnson_11 = JohnsonDF.loc[TopSchoolsDF['Grade'] == "11th"]
Johnson_12 = JohnsonDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingJohnson_9 = Johnson_9['Reading Score'].mean()
avgReadingJohnson_9Pol = np.round(avgReadingJohnson_9, decimals=2)
avgReadingJohnson_9Pol = str(f"{avgReadingJohnson_9Pol}%")
avgReadingJohnson_10 = Johnson_10['Reading Score'].mean()
avgReadingJohnson_10Pol = np.round(avgReadingJohnson_10, decimals=2)
avgReadingJohnson_10Pol = str(f"{avgReadingJohnson_10Pol}%")
avgReadingJohnson_11 = Johnson_11['Reading Score'].mean()
avgReadingJohnson_11Pol = np.round(avgReadingJohnson_11, decimals=2)
avgReadingJohnson_11Pol = str(f"{avgReadingJohnson_11Pol}%")
avgReadingJohnson_12 = Johnson_12['Reading Score'].mean()
avgReadingJohnson_12Pol = np.round(avgReadingJohnson_12, decimals=2)
avgReadingJohnson_12Pol = str(f"{avgReadingJohnson_12Pol}%")
Ford_9 = FordDF.loc[TopSchoolsDF['Grade'] == "9th"]
Ford_10 = FordDF.loc[TopSchoolsDF['Grade'] == "10th"]
Ford_11 = FordDF.loc[TopSchoolsDF['Grade'] == "11th"]
Ford_12 = FordDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingFord_9 = Ford_9['Reading Score'].mean()
avgReadingFord_9Pol = np.round(avgReadingFord_9, decimals=2)
avgReadingFord_9Pol = str(f"{avgReadingFord_9Pol}%")
avgReadingFord_10 = Ford_10['Reading Score'].mean()
avgReadingFord_10Pol = np.round(avgReadingFord_10, decimals=2)
avgReadingFord_10Pol = str(f"{avgReadingFord_10Pol}%")
avgReadingFord_11 = Ford_11['Reading Score'].mean()
avgReadingFord_11Pol = np.round(avgReadingFord_11, decimals=2)
avgReadingFord_11Pol = str(f"{avgReadingFord_11Pol}%")
avgReadingFord_12 = Ford_12['Reading Score'].mean()
avgReadingFord_12Pol = np.round(avgReadingFord_12, decimals=2)
avgReadingFord_12Pol = str(f"{avgReadingFord_12Pol}%")
Thomas_9 = ThomasDF.loc[TopSchoolsDF['Grade'] == "9th"]
Thomas_10 = ThomasDF.loc[TopSchoolsDF['Grade'] == "10th"]
Thomas_11 = ThomasDF.loc[TopSchoolsDF['Grade'] == "11th"]
Thomas_12 = ThomasDF.loc[TopSchoolsDF['Grade'] == "12th"]
avgReadingThomas_9 = Thomas_9['Reading Score'].mean()
avgReadingThomas_9Pol = np.round(avgReadingThomas_9, decimals=2)
avgReadingThomas_9Pol = str(f"{avgReadingThomas_9Pol}%")
avgReadingThomas_10 = Thomas_10['Reading Score'].mean()
avgReadingThomas_10Pol = np.round(avgReadingThomas_10, decimals=2)
avgReadingThomas_10Pol = str(f"{avgReadingThomas_10Pol}%")
avgReadingThomas_11 = Thomas_11['Reading Score'].mean()
avgReadingThomas_11Pol = np.round(avgReadingThomas_11, decimals=2)
avgReadingThomas_11Pol = str(f"{avgReadingThomas_11Pol}%")
avgReadingThomas_12 = Thomas_12['Reading Score'].mean()
avgReadingThomas_12Pol = np.round(avgReadingThomas_12, decimals=2)
avgReadingThomas_12Pol = str(f"{avgReadingThomas_12Pol}%")
#####################################################################################
######################### establish a dataframes containing above
#####################################################################################
HuangReading_byGrade = pd.DataFrame(data={'School Name': [HuangDF.iloc[0, 4]],
'9th Grade': [avgReadingHuang_9Pol],
'10th Grade': [avgReadingHuang_10Pol],
'11th Grade': [avgReadingHuang_11Pol],
'12th Grade': [avgReadingHuang_12Pol]})
FigueroaReading_byGrade = pd.DataFrame(data={'School Name': [FigueroaDF.iloc[0, 4]],
'9th Grade': [avgReadingFigueroa_9Pol],
'10th Grade': [avgReadingFigueroa_10Pol],
'11th Grade': [avgReadingFigueroa_11Pol],
'12th Grade': [avgReadingFigueroa_12Pol]})
SheltonReading_byGrade = pd.DataFrame(data={'School Name': [SheltonDF.iloc[0, 4]],
'9th Grade': [avgReadingShelton_9Pol],
'10th Grade': [avgReadingShelton_10Pol],
'11th Grade': [avgReadingShelton_11Pol],
'12th Grade': [avgReadingShelton_12Pol]})
HernandezReading_byGrade = pd.DataFrame(data={'School Name': [HernandezDF.iloc[0, 4]],
'9th Grade': [avgReadingHernandez_9Pol],
'10th Grade': [avgReadingHernandez_10Pol],
'11th Grade': [avgReadingHernandez_11Pol],
'12th Grade': [avgReadingHernandez_12Pol]})
GriffinReading_byGrade = pd.DataFrame(data={'School Name': [GriffinDF.iloc[0, 4]],
'9th Grade': [avgReadingGriffin_9Pol],
'10th Grade': [avgReadingGriffin_10Pol],
'11th Grade': [avgReadingGriffin_11Pol],
'12th Grade': [avgReadingGriffin_12Pol]})
WilsonReading_byGrade = pd.DataFrame(data={'School Name': [WilsonDF.iloc[0, 4]],
'9th Grade': [avgReadingWilson_9Pol],
'10th Grade': [avgReadingWilson_10Pol],
'11th Grade': [avgReadingWilson_11Pol],
'12th Grade': [avgReadingWilson_12Pol]})
CabreraReading_byGrade = pd.DataFrame(data={'School Name': [CabreraDF.iloc[0, 4]],
'9th Grade': [avgReadingCabrera_9Pol],
'10th Grade': [avgReadingCabrera_10Pol],
'11th Grade': [avgReadingCabrera_11Pol],
'12th Grade': [avgReadingCabrera_12Pol]})
BaileyReading_byGrade = pd.DataFrame(data={'School Name': [BaileyDF.iloc[0, 4]],
'9th Grade': [avgReadingBailey_9Pol],
'10th Grade': [avgReadingBailey_10Pol],
'11th Grade': [avgReadingBailey_11Pol],
'12th Grade': [avgReadingBailey_12Pol]})
HoldenReading_byGrade = pd.DataFrame(data={'School Name': [HoldenDF.iloc[0, 4]],
'9th Grade': [avgReadingHolden_9Pol],
'10th Grade': [avgReadingHolden_10Pol],
'11th Grade': [avgReadingHolden_11Pol],
'12th Grade': [avgReadingHolden_12Pol]})
PenaReading_byGrade = pd.DataFrame(data={'School Name': [PenaDF.iloc[0, 4]],
'9th Grade': [avgReadingPena_9Pol],
'10th Grade': [avgReadingPena_10Pol],
'11th Grade': [avgReadingPena_11Pol],
'12th Grade': [avgReadingPena_12Pol]})
WrightReading_byGrade = pd.DataFrame(data={'School Name': [WrightDF.iloc[0, 4]],
'9th Grade': [avgReadingWright_9Pol],
'10th Grade': [avgReadingWright_10Pol],
'11th Grade': [avgReadingWright_11Pol],
'12th Grade': [avgReadingWright_12Pol]})
RodriguezReading_byGrade = pd.DataFrame(data={'School Name': [RodriguezDF.iloc[0, 4]],
'9th Grade': [avgReadingRodriguez_9Pol],
'10th Grade': [avgReadingRodriguez_10Pol],
'11th Grade': [avgReadingRodriguez_11Pol],
'12th Grade': [avgReadingRodriguez_12Pol]})
JohnsonReading_byGrade = pd.DataFrame(data={'School Name': [JohnsonDF.iloc[0, 4]],
'9th Grade': [avgReadingJohnson_9Pol],
'10th Grade': [avgReadingJohnson_10Pol],
'11th Grade': [avgReadingJohnson_11Pol],
'12th Grade': [avgReadingJohnson_12Pol]})
FordReading_byGrade = pd.DataFrame(data={'School Name': [FordDF.iloc[0, 4]],
'9th Grade': [avgReadingFord_9Pol],
'10th Grade': [avgReadingFord_10Pol],
'11th Grade': [avgReadingFord_11Pol],
'12th Grade': [avgReadingFord_12Pol]})
ThomasReading_byGrade = pd.DataFrame(data={'School Name': [ThomasDF.iloc[0, 4]],
'9th Grade': [avgReadingThomas_9Pol],
'10th Grade': [avgReadingThomas_10Pol],
'11th Grade': [avgReadingThomas_11Pol],
'12th Grade': [avgReadingThomas_12Pol]})
#####################################################################################
######################### establish a DF containing all DFs above, sort alphabetically
#####################################################################################
AllSchoolsReading_byGrade = pd.concat([HuangReading_byGrade, FigueroaReading_byGrade, SheltonReading_byGrade, HernandezReading_byGrade, GriffinReading_byGrade, WilsonReading_byGrade, CabreraReading_byGrade, BaileyReading_byGrade, HoldenReading_byGrade, PenaReading_byGrade, WrightReading_byGrade, RodriguezReading_byGrade, JohnsonReading_byGrade, FordReading_byGrade, ThomasReading_byGrade])
AllSchoolsReading_byGrade = AllSchoolsReading_byGrade.sort_values(by="School Name", ascending=True)
spendingBins = [0, 585, 615, 645, 675]
spendingBinsNames = ["<$585", "$585-615", "$615-645", "$645-675"]
#####################################################################################
######################### establish DFs of raw info by school
#####################################################################################
HuangSPENDING = pd.DataFrame(data={'School Name': [HuangDF.iloc[0, 4]],
                              'School Type': [HuangDF.iloc[0, 8]],
                              'Total Students': [totalStudentsHuang],
                              'Total School Budget': [budgetHuang],
                              'Per Student Budget': [studentBudgetHuang],
                              'Average Math Score': [avgMathScoreHuang],
                              'Average Reading Score': [avgReadingScoreHuang],
                              '% Passing Math': [HuangpctPassingMath],
                              '% Passing Reading': [HuangpctPassingReading],
                              '% Overall Passing Rate': [HuangpctPassingBoth]})
FigueroaSPENDING = pd.DataFrame(data={'School Name': [FigueroaDF.iloc[0, 4]],
                                'School Type': [FigueroaDF.iloc[0, 8]],
                                'Total Students': [totalStudentsFigueroa],
                                'Total School Budget': [budgetFigueroa],
                                'Per Student Budget': [studentBudgetFigueroa],
                                'Average Math Score': [avgMathScoreFigueroa],
                                'Average Reading Score': [avgReadingScoreFigueroa],
                                '% Passing Math': [FigueroapctPassingMath],
                                '% Passing Reading': [FigueroapctPassingReading],
                                '% Overall Passing Rate': [FigueroapctPassingBoth]})
SheltonSPENDING = pd.DataFrame(data={'School Name': [SheltonDF.iloc[0, 4]],
                                'School Type': [SheltonDF.iloc[0, 8]],
                                'Total Students': [totalStudentsShelton],
                                'Total School Budget': [budgetShelton],
                                'Per Student Budget': [studentBudgetShelton],
                                'Average Math Score': [avgMathScoreShelton],
                                'Average Reading Score': [avgReadingScoreShelton],
                                '% Passing Math': [SheltonpctPassingMath],
                                '% Passing Reading': [SheltonpctPassingReading],
                                '% Overall Passing Rate': [SheltonpctPassingBoth]})
HernandezSPENDING = pd.DataFrame(data={'School Name': [HernandezDF.iloc[0, 4]],
                                'School Type': [HernandezDF.iloc[0, 8]],
                                'Total Students': [totalStudentsHernandez],
                                'Total School Budget': [budgetHernandez],
                                'Per Student Budget': [studentBudgetHernandez],
                                'Average Math Score': [avgMathScoreHernandez],
                                'Average Reading Score': [avgReadingScoreHernandez],
                                '% Passing Math': [HernandezpctPassingMath],
                                '% Passing Reading': [HernandezpctPassingReading],
                                '% Overall Passing Rate': [HernandezpctPassingBoth]})
GriffinSPENDING = pd.DataFrame(data={'School Name': [GriffinDF.iloc[0, 4]],
                                'School Type': [GriffinDF.iloc[0, 8]],
                                'Total Students': [totalStudentsGriffin],
                                'Total School Budget': [budgetGriffin],
                                'Per Student Budget': [studentBudgetGriffin],
                                'Average Math Score': [avgMathScoreGriffin],
                                'Average Reading Score': [avgReadingScoreGriffin],
                                '% Passing Math': [GriffinpctPassingMath],
                                '% Passing Reading': [GriffinpctPassingReading],
                                '% Overall Passing Rate': [GriffinpctPassingBoth]})
WilsonSPENDING = pd.DataFrame(data={'School Name': [WilsonDF.iloc[0, 4]],
                                'School Type': [WilsonDF.iloc[0, 8]],
                                'Total Students': [totalStudentsWilson],
                                'Total School Budget': [budgetWilson],
                                'Per Student Budget': [studentBudgetWilson],
                                'Average Math Score': [avgMathScoreWilson],
                                'Average Reading Score': [avgReadingScoreWilson],
                                '% Passing Math': [WilsonpctPassingMath],
                                '% Passing Reading': [WilsonpctPassingReading],
                                '% Overall Passing Rate': [WilsonpctPassingBoth]})
CabreraSPENDING = pd.DataFrame(data={'School Name': [CabreraDF.iloc[0, 4]],
                                'School Type': [CabreraDF.iloc[0, 8]],
                                'Total Students': [totalStudentsCabrera],
                                'Total School Budget': [budgetCabrera],
                                'Per Student Budget': [studentBudgetCabrera],
                                'Average Math Score': [avgMathScoreCabrera],
                                'Average Reading Score': [avgReadingScoreCabrera],
                                '% Passing Math': [CabrerapctPassingMath],
                                '% Passing Reading': [CabrerapctPassingReading],
                                '% Overall Passing Rate': [CabrerapctPassingBoth]})
BaileySPENDING = pd.DataFrame(data={'School Name': [BaileyDF.iloc[0, 4]],
                                'School Type': [BaileyDF.iloc[0, 8]],
                                'Total Students': [totalStudentsBailey],
                                'Total School Budget': [budgetBailey],
                                'Per Student Budget': [studentBudgetBailey],
                                'Average Math Score': [avgMathScoreBailey],
                                'Average Reading Score': [avgReadingScoreBailey],
                                '% Passing Math': [BaileypctPassingMath],
                                '% Passing Reading': [BaileypctPassingReading],
                                '% Overall Passing Rate': [BaileypctPassingBoth]})
HoldenSPENDING = pd.DataFrame(data={'School Name': [HoldenDF.iloc[0, 4]],
                                'School Type': [HoldenDF.iloc[0, 8]],
                                'Total Students': [totalStudentsHolden],
                                'Total School Budget': [budgetHolden],
                                'Per Student Budget': [studentBudgetHolden],
                                'Average Math Score': [avgMathScoreHolden],
                                'Average Reading Score': [avgReadingScoreHolden],
                                '% Passing Math': [HoldenpctPassingMath],
                                '% Passing Reading': [HoldenpctPassingReading],
                                '% Overall Passing Rate': [HoldenpctPassingBoth]})
PenaSPENDING = pd.DataFrame(data={'School Name': [PenaDF.iloc[0, 4]],
                                'School Type': [PenaDF.iloc[0, 8]],
                                'Total Students': [totalStudentsPena],
                                'Total School Budget': [budgetPena],
                                'Per Student Budget': [studentBudgetPena],
                                'Average Math Score': [avgMathScorePena],
                                'Average Reading Score': [avgReadingScorePena],
                                '% Passing Math': [PenapctPassingMath],
                                '% Passing Reading': [PenapctPassingReading],
                                '% Overall Passing Rate': [PenapctPassingBoth]})
WrightSPENDING = pd.DataFrame(data={'School Name': [WrightDF.iloc[0, 4]],
                                'School Type': [WrightDF.iloc[0, 8]],
                                'Total Students': [totalStudentsWright],
                                'Total School Budget': [budgetWright],
                                'Per Student Budget': [studentBudgetWright],
                                'Average Math Score': [avgMathScoreWright],
                                'Average Reading Score': [avgReadingScoreWright],
                                '% Passing Math': [WrightpctPassingMath],
                                '% Passing Reading': [WrightpctPassingReading],
                                '% Overall Passing Rate': [WrightpctPassingBoth]})
RodriguezSPENDING = pd.DataFrame(data={'School Name': [RodriguezDF.iloc[0, 4]],
                                'School Type': [RodriguezDF.iloc[0, 8]],
                                'Total Students': [totalStudentsRodriguez],
                                'Total School Budget': [budgetRodriguez],
                                'Per Student Budget': [studentBudgetRodriguez],
                                'Average Math Score': [avgMathScoreRodriguez],
                                'Average Reading Score': [avgReadingScoreRodriguez],
                                '% Passing Math': [RodriguezpctPassingMath],
                                '% Passing Reading': [RodriguezpctPassingReading],
                                '% Overall Passing Rate': [RodriguezpctPassingBoth]})
JohnsonSPENDING = pd.DataFrame(data={'School Name': [JohnsonDF.iloc[0, 4]],
                                'School Type': [JohnsonDF.iloc[0, 8]],
                                'Total Students': [totalStudentsJohnson],
                                'Total School Budget': [budgetJohnson],
                                'Per Student Budget': [studentBudgetJohnson],
                                'Average Math Score': [avgMathScoreJohnson],
                                'Average Reading Score': [avgReadingScoreJohnson],
                                '% Passing Math': [JohnsonpctPassingMath],
                                '% Passing Reading': [JohnsonpctPassingReading],
                                '% Overall Passing Rate': [JohnsonpctPassingBoth]})
FordSPENDING = pd.DataFrame(data={'School Name': [FordDF.iloc[0, 4]],
                                'School Type': [FordDF.iloc[0, 8]],
                                'Total Students': [totalStudentsFord],
                                'Total School Budget': [budgetFord],
                                'Per Student Budget': [studentBudgetFord],
                                'Average Math Score': [avgMathScoreFord],
                                'Average Reading Score': [avgReadingScoreFord],
                                '% Passing Math': [FordpctPassingMath],
                                '% Passing Reading': [FordpctPassingReading],
                                '% Overall Passing Rate': [FordpctPassingBoth]})
ThomasSPENDING = pd.DataFrame(data={'School Name': [ThomasDF.iloc[0, 4]],
                                'School Type': [ThomasDF.iloc[0, 8]],
                                'Total Students': [totalStudentsThomas],
                                'Total School Budget': [budgetThomas],
                                'Per Student Budget': [studentBudgetThomas],
                                'Average Math Score': [avgMathScoreThomas],
                                'Average Reading Score': [avgReadingScoreThomas],
                                '% Passing Math': [ThomaspctPassingMath],
                                '% Passing Reading': [ThomaspctPassingReading],
                                '% Overall Passing Rate': [ThomaspctPassingBoth]})
#####################################################################################
######################### establish a DF containing above
#####################################################################################
sortingDF_rawPerStudent = pd.concat([HuangSPENDING, FigueroaSPENDING, SheltonSPENDING, HernandezSPENDING, GriffinSPENDING, WilsonSPENDING, CabreraSPENDING, BaileySPENDING, HoldenSPENDING, PenaSPENDING, WrightSPENDING, RodriguezSPENDING, JohnsonSPENDING, FordSPENDING, ThomasSPENDING])
#####################################################################################
######################### sort by spending level
#####################################################################################
spendingDF = pd.DataFrame(sortingDF_rawPerStudent)
spendingDF["Spending Level"] = pd.cut(spendingDF["Per Student Budget"], spendingBins, labels=spendingBinsNames)
#####################################################################################
######################### establish DFs by spending level
#####################################################################################
spendingGroup_1 = spendingDF.loc[spendingDF['Spending Level'] == "<$585"]
spendingGroup_2 = spendingDF.loc[spendingDF['Spending Level'] == "$585-615"]
spendingGroup_3 = spendingDF.loc[spendingDF['Spending Level'] == "$615-645"]
spendingGroup_4 = spendingDF.loc[spendingDF['Spending Level'] == "$645-675"]
#####################################################################################
######################### establish average math score by spending level
#####################################################################################
spendingGroup_1_MATH = spendingGroup_1['Average Math Score'].mean()
spendingGroup_1_MATHPol = np.round(spendingGroup_1_MATH, decimals=2)
spendingGroup_1_MATHPol = str(f"{spendingGroup_1_MATHPol}%")
spendingGroup_2_MATH = spendingGroup_2['Average Math Score'].mean()
spendingGroup_2_MATHPol = np.round(spendingGroup_2_MATH, decimals=2)
spendingGroup_2_MATHPol = str(f"{spendingGroup_2_MATHPol}%")
spendingGroup_3_MATH = spendingGroup_3['Average Math Score'].mean()
spendingGroup_3_MATHPol = np.round(spendingGroup_3_MATH, decimals=2)
spendingGroup_3_MATHPol = str(f"{spendingGroup_3_MATHPol}%")
spendingGroup_4_MATH = spendingGroup_4['Average Math Score'].mean()
spendingGroup_4_MATHPol = np.round(spendingGroup_4_MATH, decimals=2)
spendingGroup_4_MATHPol = str(f"{spendingGroup_4_MATHPol}%")
#####################################################################################
######################### establish average reading score by spending level
#####################################################################################
spendingGroup_1_READING = spendingGroup_1['Average Reading Score'].mean()
spendingGroup_1_READINGPol = np.round(spendingGroup_1_READING, decimals=2)
spendingGroup_1_READINGPol = str(f"{spendingGroup_1_READINGPol}%")
spendingGroup_2_READING = spendingGroup_2['Average Reading Score'].mean()
spendingGroup_2_READINGPol = np.round(spendingGroup_2_READING, decimals=2)
spendingGroup_2_READINGPol = str(f"{spendingGroup_2_READINGPol}%")
spendingGroup_3_READING = spendingGroup_3['Average Reading Score'].mean()
spendingGroup_3_READINGPol = np.round(spendingGroup_3_READING, decimals=2)
spendingGroup_3_READINGPol = str(f"{spendingGroup_3_READINGPol}%")
spendingGroup_4_READING = spendingGroup_4['Average Reading Score'].mean()
spendingGroup_4_READINGPol = np.round(spendingGroup_4_READING, decimals=2)
spendingGroup_4_READINGPol = str(f"{spendingGroup_4_READINGPol}%")
#####################################################################################
######################### establish average % passing math by spending level
#####################################################################################
spendingGroup_1_PassingMATH = spendingGroup_1['% Passing Math'].mean()
spendingGroup_1_PassingMATHPol = np.round(spendingGroup_1_PassingMATH, decimals=2)
spendingGroup_1_PassingMATHPol = str(f"{spendingGroup_1_PassingMATHPol}%")
spendingGroup_2_PassingMATH = spendingGroup_2['% Passing Math'].mean()
spendingGroup_2_PassingMATHPol = np.round(spendingGroup_2_PassingMATH, decimals=2)
spendingGroup_2_PassingMATHPol = str(f"{spendingGroup_2_PassingMATHPol}%")
spendingGroup_3_PassingMATH = spendingGroup_3['% Passing Math'].mean()
spendingGroup_3_PassingMATHPol = np.round(spendingGroup_3_PassingMATH, decimals=2)
spendingGroup_3_PassingMATHPol = str(f"{spendingGroup_3_PassingMATHPol}%")
spendingGroup_4_PassingMATH = spendingGroup_4['% Passing Math'].mean()
spendingGroup_4_PassingMATHPol = np.round(spendingGroup_4_PassingMATH, decimals=2)
spendingGroup_4_PassingMATHPol = str(f"{spendingGroup_4_PassingMATHPol}%")
#####################################################################################
######################### establish average % passing reading by spending level
#####################################################################################
spendingGroup_1_PassingREADING = spendingGroup_1['% Passing Reading'].mean()
spendingGroup_1_PassingREADINGPol = np.round(spendingGroup_1_PassingREADING, decimals=2)
spendingGroup_1_PassingREADINGPol = str(f"{spendingGroup_1_PassingREADINGPol}%")
spendingGroup_2_PassingREADING = spendingGroup_2['% Passing Reading'].mean()
spendingGroup_2_PassingREADINGPol = np.round(spendingGroup_2_PassingREADING, decimals=2)
spendingGroup_2_PassingREADINGPol = str(f"{spendingGroup_2_PassingREADINGPol}%")
spendingGroup_3_PassingREADING = spendingGroup_3['% Passing Reading'].mean()
spendingGroup_3_PassingREADINGPol = np.round(spendingGroup_3_PassingREADING, decimals=2)
spendingGroup_3_PassingREADINGPol = str(f"{spendingGroup_3_PassingREADINGPol}%")
spendingGroup_4_PassingREADING = spendingGroup_4['% Passing Reading'].mean()
spendingGroup_4_PassingREADINGPol = np.round(spendingGroup_4_PassingREADING, decimals=2)
spendingGroup_4_PassingREADINGPol = str(f"{spendingGroup_4_PassingREADINGPol}%")
#####################################################################################
######################### establish average % passing overall by spending level
#####################################################################################
spendingGroup_1_PassingBOTH = (spendingGroup_1_PassingMATH + spendingGroup_1_PassingREADING) / 2
spendingGroup_1_PassingBOTHPol = np.round(spendingGroup_1_PassingBOTH, decimals=2)
spendingGroup_1_PassingBOTHPol = str(f"{spendingGroup_1_PassingBOTHPol}%")
spendingGroup_2_PassingBOTH = (spendingGroup_2_PassingMATH + spendingGroup_2_PassingREADING) / 2
spendingGroup_2_PassingBOTHPol = np.round(spendingGroup_2_PassingBOTH, decimals=2)
spendingGroup_2_PassingBOTHPol = str(f"{spendingGroup_2_PassingBOTHPol}%")
spendingGroup_3_PassingBOTH = (spendingGroup_3_PassingMATH + spendingGroup_3_PassingREADING) / 2
spendingGroup_3_PassingBOTHPol = np.round(spendingGroup_3_PassingBOTH, decimals=2)
spendingGroup_3_PassingBOTHPol = str(f"{spendingGroup_3_PassingBOTHPol}%")
spendingGroup_4_PassingBOTH = (spendingGroup_4_PassingMATH + spendingGroup_4_PassingREADING) / 2
spendingGroup_4_PassingBOTHPol = np.round(spendingGroup_4_PassingBOTH, decimals=2)
spendingGroup_4_PassingBOTHPol = str(f"{spendingGroup_4_PassingBOTHPol}%")
#####################################################################################
######################### establish DFs for the above
#####################################################################################
spendingGroup_1DF = pd.DataFrame(data={'Spending Ranges (Per Student)': [spendingGroup_1.iloc[0, 10]],
                                      'Average Math Score': [spendingGroup_1_MATHPol],
                                      'Average Reading Score': [spendingGroup_1_READINGPol],
                                      '% Passing Math': [spendingGroup_1_PassingMATHPol],
                                      '% Passing Reading': [spendingGroup_1_PassingREADINGPol],
                                      '% Overall Passing Rate': [spendingGroup_1_PassingBOTHPol]})
spendingGroup_2DF = pd.DataFrame(data={'Spending Ranges (Per Student)': [spendingGroup_2.iloc[0, 10]],
                                      'Average Math Score': [spendingGroup_2_MATHPol],
                                      'Average Reading Score': [spendingGroup_2_READINGPol],
                                      '% Passing Math': [spendingGroup_2_PassingMATHPol],
                                      '% Passing Reading': [spendingGroup_2_PassingREADINGPol],
                                      '% Overall Passing Rate': [spendingGroup_2_PassingBOTHPol]})
spendingGroup_3DF = pd.DataFrame(data={'Spending Ranges (Per Student)': [spendingGroup_3.iloc[0, 10]],
                                      'Average Math Score': [spendingGroup_3_MATHPol],
                                      'Average Reading Score': [spendingGroup_3_READINGPol],
                                      '% Passing Math': [spendingGroup_3_PassingMATHPol],
                                      '% Passing Reading': [spendingGroup_3_PassingREADINGPol],
                                      '% Overall Passing Rate': [spendingGroup_3_PassingBOTHPol]})
spendingGroup_4DF = pd.DataFrame(data={'Spending Ranges (Per Student)': [spendingGroup_4.iloc[0, 10]],
                                      'Average Math Score': [spendingGroup_4_MATHPol],
                                      'Average Reading Score': [spendingGroup_4_READINGPol],
                                      '% Passing Math': [spendingGroup_4_PassingMATHPol],
                                      '% Passing Reading': [spendingGroup_4_PassingREADINGPol],
                                      '% Overall Passing Rate': [spendingGroup_4_PassingBOTHPol]})
#####################################################################################
######################### establish an encompassing DF for the above
#####################################################################################
SpendersSummaryDF = pd.concat([spendingGroup_1DF, spendingGroup_2DF, spendingGroup_3DF, spendingGroup_4DF])
##################################
sizeBins = [0, 1000, 2000, 5000]
sizeBinsNames = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
#####################################################################################
######################### establish a DF containing info with Schools' sizes
#####################################################################################
sizeDF = pd.DataFrame(sortingDF_rawPerStudent)
sizeDF["School Size"] = pd.cut(sizeDF["Total Students"], sizeBins, labels=sizeBinsNames)
#####################################################################################
######################### establish DFs by size level
#####################################################################################
sizeGroup_1 = spendingDF.loc[spendingDF['School Size'] == "Small (<1000)"]
sizeGroup_2 = spendingDF.loc[spendingDF['School Size'] == "Medium (1000-2000)"]
sizeGroup_3 = spendingDF.loc[spendingDF['School Size'] == "Large (2000-5000)"]
#####################################################################################
######################### establish average math score by size level
#####################################################################################
sizeGroup_1_MATH = sizeGroup_1['Average Math Score'].mean()
sizeGroup_1_MATHPol = np.round(sizeGroup_1_MATH, decimals=2)
sizeGroup_1_MATHPol = str(f"{sizeGroup_1_MATHPol}%")
sizeGroup_2_MATH = sizeGroup_2['Average Math Score'].mean()
sizeGroup_2_MATHPol = np.round(sizeGroup_2_MATH, decimals=2)
sizeGroup_2_MATHPol = str(f"{sizeGroup_2_MATHPol}%")
sizeGroup_3_MATH = sizeGroup_3['Average Math Score'].mean()
sizeGroup_3_MATHPol = np.round(sizeGroup_3_MATH, decimals=2)
sizeGroup_3_MATHPol = str(f"{sizeGroup_3_MATHPol}%")
#####################################################################################
######################### establish average reading score by size level
#####################################################################################
sizeGroup_1_READING = sizeGroup_1['Average Reading Score'].mean()
sizeGroup_1_READINGPol = np.round(sizeGroup_1_READING, decimals=2)
sizeGroup_1_READINGPol = str(f"{sizeGroup_1_READINGPol}%")
sizeGroup_2_READING = sizeGroup_2['Average Reading Score'].mean()
sizeGroup_2_READINGPol = np.round(sizeGroup_2_READING, decimals=2)
sizeGroup_2_READINGPol = str(f"{sizeGroup_2_READINGPol}%")
sizeGroup_3_READING = sizeGroup_3['Average Reading Score'].mean()
sizeGroup_3_READINGPol = np.round(sizeGroup_3_READING, decimals=2)
sizeGroup_3_READINGPol = str(f"{sizeGroup_3_READINGPol}%")
#####################################################################################
######################### establish average % passing math by size level
#####################################################################################
sizeGroup_1_PassingMATH = sizeGroup_1['% Passing Math'].mean()
sizeGroup_1_PassingMATHPol = np.round(sizeGroup_1_PassingMATH, decimals=2)
sizeGroup_1_PassingMATHPol = str(f"{sizeGroup_1_PassingMATHPol}%")
sizeGroup_2_PassingMATH = sizeGroup_2['% Passing Math'].mean()
sizeGroup_2_PassingMATHPol = np.round(sizeGroup_2_PassingMATH, decimals=2)
sizeGroup_2_PassingMATHPol = str(f"{sizeGroup_2_PassingMATHPol}%")
sizeGroup_3_PassingMATH = sizeGroup_3['% Passing Math'].mean()
sizeGroup_3_PassingMATHPol = np.round(sizeGroup_3_PassingMATH, decimals=2)
sizeGroup_3_PassingMATHPol = str(f"{sizeGroup_3_PassingMATHPol}%")
#####################################################################################
######################### establish average % passing reading by size level
#####################################################################################
sizeGroup_1_PassingREADING = sizeGroup_1['% Passing Reading'].mean()
sizeGroup_1_PassingREADINGPol = np.round(sizeGroup_1_PassingREADING, decimals=2)
sizeGroup_1_PassingREADINGPol = str(f"{sizeGroup_1_PassingREADINGPol}%")
sizeGroup_2_PassingREADING = sizeGroup_2['% Passing Reading'].mean()
sizeGroup_2_PassingREADINGPol = np.round(sizeGroup_2_PassingREADING, decimals=2)
sizeGroup_2_PassingREADINGPol = str(f"{sizeGroup_2_PassingREADINGPol}%")
sizeGroup_3_PassingREADING = sizeGroup_3['% Passing Reading'].mean()
sizeGroup_3_PassingREADINGPol = np.round(sizeGroup_3_PassingREADING, decimals=2)
sizeGroup_3_PassingREADINGPol = str(f"{sizeGroup_3_PassingREADINGPol}%")
#####################################################################################
######################### establish average % passing overall by size level
#####################################################################################
sizeGroup_1_PassingBOTH = (sizeGroup_1_PassingMATH + sizeGroup_1_PassingREADING) / 2
sizeGroup_1_PassingBOTHPol = np.round(sizeGroup_1_PassingBOTH, decimals=2)
sizeGroup_1_PassingBOTHPol = str(f"{sizeGroup_1_PassingBOTHPol}%")
sizeGroup_2_PassingBOTH = (sizeGroup_2_PassingMATH + sizeGroup_2_PassingREADING) / 2
sizeGroup_2_PassingBOTHPol = np.round(sizeGroup_2_PassingBOTH, decimals=2)
sizeGroup_2_PassingBOTHPol = str(f"{sizeGroup_2_PassingBOTHPol}%")
sizeGroup_3_PassingBOTH = (sizeGroup_3_PassingMATH + sizeGroup_3_PassingREADING) / 2
sizeGroup_3_PassingBOTHPol = np.round(sizeGroup_3_PassingBOTH, decimals=2)
sizeGroup_3_PassingBOTHPol = str(f"{sizeGroup_3_PassingBOTHPol}%")
#####################################################################################
######################### establish DFs for the above
#####################################################################################
sizeGroup_1DF = pd.DataFrame(data={'School Size': [sizeGroup_1.iloc[0, 11]],
                                      'Average Math Score': [sizeGroup_1_MATHPol],
                                      'Average Reading Score': [sizeGroup_1_READINGPol],
                                      '% Passing Math': [sizeGroup_1_PassingMATHPol],
                                      '% Passing Reading': [sizeGroup_1_PassingREADINGPol],
                                      '% Overall Passing Rate': [sizeGroup_1_PassingBOTHPol]})
sizeGroup_2DF = pd.DataFrame(data={'School Size': [sizeGroup_2.iloc[0, 11]],
                                      'Average Math Score': [sizeGroup_2_MATHPol],
                                      'Average Reading Score': [sizeGroup_2_READINGPol],
                                      '% Passing Math': [sizeGroup_2_PassingMATHPol],
                                      '% Passing Reading': [sizeGroup_2_PassingREADINGPol],
                                      '% Overall Passing Rate': [sizeGroup_2_PassingBOTHPol]})
sizeGroup_3DF = pd.DataFrame(data={'School Size': [sizeGroup_3.iloc[0, 11]],
                                      'Average Math Score': [sizeGroup_3_MATHPol],
                                      'Average Reading Score': [sizeGroup_3_READINGPol],
                                      '% Passing Math': [sizeGroup_3_PassingMATHPol],
                                      '% Passing Reading': [sizeGroup_3_PassingREADINGPol],
                                      '% Overall Passing Rate': [sizeGroup_3_PassingBOTHPol]})
#####################################################################################
######################### establish an encompassing DF for the above
#####################################################################################
SizeSummaryDF = pd.concat([sizeGroup_1DF, sizeGroup_2DF, sizeGroup_3DF])
#####################################################################################
######################### establish a DF containing info with Schools' types
#####################################################################################
typeDF = pd.DataFrame(sortingDF_rawPerStudent)
#####################################################################################
######################### establish DFs by type level
#####################################################################################
typeGroup_1 = spendingDF.loc[spendingDF['School Type'] == "Charter"]
typeGroup_2 = spendingDF.loc[spendingDF['School Type'] == "District"]
#####################################################################################
######################### establish average math score by type level
#####################################################################################
typeGroup_1_MATH = typeGroup_1['Average Math Score'].mean()
typeGroup_1_MATHPol = np.round(typeGroup_1_MATH, decimals=2)
typeGroup_1_MATHPol = str(f"{typeGroup_1_MATHPol}%")
typeGroup_2_MATH = typeGroup_2['Average Math Score'].mean()
typeGroup_2_MATHPol = np.round(typeGroup_2_MATH, decimals=2)
typeGroup_2_MATHPol = str(f"{typeGroup_2_MATHPol}%")
#####################################################################################
######################### establish average reading score by type level
#####################################################################################
typeGroup_1_READING = typeGroup_1['Average Reading Score'].mean()
typeGroup_1_READINGPol = np.round(typeGroup_1_READING, decimals=2)
typeGroup_1_READINGPol = str(f"{typeGroup_1_READINGPol}%")
typeGroup_2_READING = typeGroup_2['Average Reading Score'].mean()
typeGroup_2_READINGPol = np.round(typeGroup_2_READING, decimals=2)
typeGroup_2_READINGPol = str(f"{typeGroup_2_READINGPol}%")
#####################################################################################
######################### establish average % passing math by type level
#####################################################################################
typeGroup_1_PassingMATH = typeGroup_1['% Passing Math'].mean()
typeGroup_1_PassingMATHPol = np.round(typeGroup_1_PassingMATH, decimals=2)
typeGroup_1_PassingMATHPol = str(f"{typeGroup_1_PassingMATHPol}%")
typeGroup_2_PassingMATH = typeGroup_2['% Passing Math'].mean()
typeGroup_2_PassingMATHPol = np.round(typeGroup_2_PassingMATH, decimals=2)
typeGroup_2_PassingMATHPol = str(f"{typeGroup_2_PassingMATHPol}%")
#####################################################################################
######################### establish average % passing reading by type level
#####################################################################################
typeGroup_1_PassingREADING = typeGroup_1['% Passing Reading'].mean()
typeGroup_1_PassingREADINGPol = np.round(typeGroup_1_PassingREADING, decimals=2)
typeGroup_1_PassingREADINGPol = str(f"{typeGroup_1_PassingREADINGPol}%")
typeGroup_2_PassingREADING = typeGroup_2['% Passing Reading'].mean()
typeGroup_2_PassingREADINGPol = np.round(typeGroup_2_PassingREADING, decimals=2)
typeGroup_2_PassingREADINGPol = str(f"{typeGroup_2_PassingREADINGPol}%")
#####################################################################################
######################### establish average % passing overall by type level
#####################################################################################
typeGroup_1_PassingBOTH = (typeGroup_1_PassingMATH + typeGroup_1_PassingREADING) / 2
typeGroup_1_PassingBOTHPol = np.round(typeGroup_1_PassingBOTH, decimals=2)
typeGroup_1_PassingBOTHPol = str(f"{typeGroup_1_PassingBOTHPol}%")
typeGroup_2_PassingBOTH = (typeGroup_2_PassingMATH + typeGroup_2_PassingREADING) / 2
typeGroup_2_PassingBOTHPol = np.round(typeGroup_2_PassingBOTH, decimals=2)
typeGroup_2_PassingBOTHPol = str(f"{typeGroup_2_PassingBOTHPol}%")
#####################################################################################
######################### establish DFs for the above
#####################################################################################
typeGroup_1DF = pd.DataFrame(data={'School Type': [typeGroup_1.iloc[0, 1]],
'Average Math Score': [typeGroup_1_MATHPol],
'Average Reading Score': [typeGroup_1_READINGPol],
'% Passing Math': [typeGroup_1_PassingMATHPol],
'% Passing Reading': [typeGroup_1_PassingREADINGPol],
'% Overall Passing Rate': [typeGroup_1_PassingBOTHPol]})
typeGroup_2DF = pd.DataFrame(data={'School Type': [typeGroup_2.iloc[0, 1]],
'Average Math Score': [typeGroup_2_MATHPol],
'Average Reading Score': [typeGroup_2_READINGPol],
'% Passing Math': [typeGroup_2_PassingMATHPol],
'% Passing Reading': [typeGroup_2_PassingREADINGPol],
'% Overall Passing Rate': [typeGroup_2_PassingBOTHPol]})
#####################################################################################
######################### establish an encompassing DF for the above
#####################################################################################
TypeSummaryDF = pd.concat([typeGroup_1DF, typeGroup_2DF])
#*####################################################################################
#*####################################################################################
#*####################################################################################
#*####################################################################################
#*####################################################################################

print(DistrictSummaryDF)

#sortingDF_TOP_5
#
#sortingDF_BOTTOM_5
#
#AllSchoolsMath_byGrade
#
#AllSchoolsReading_byGrade
#
#SpendersSummaryDF
#
#SizeSummaryDF
#
#TypeSummaryDF
