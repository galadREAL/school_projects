
import os
import csv
import pandas as pd
import numpy as np
import sys


data = os.path.join("BankCSV.csv")

# GetTotalNumbMonths returns the number of rows of the banking data


def GetTotalNumbMonths():
    totalMonths = int(0)
    with open(data, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvreader:
            totalMonths += int(1)
        print(f"Total Number of Months: {totalMonths}")
        return totalMonths

# GetTotalNetPL combines every row's profit/loss and returns the result


def GetTotalNetPL():
    totalPL = int(0)
    with open(data, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvreader:
            totalPL += int(row[1])
        print(f"Total Net of Profits/Losses: ${totalPL}")
        return totalPL

# GetAvgChangePL creates splices of the .csv's data for each column.
# Next it uses Pandas to create a Dataframe that finds the incremental
# difference between each value. Afterwards it find the mean of those
# results, and polishes it with NumPy's rounding to 2 decimals.
# Finally, it returns the splices of .csv data (months and P&L).


def GetAvgChangePL():
    allNums = []
    allMonths = []
    with open(data, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvreader:
            num = float(row[1])
            allNums.append(num)
            month = str(row[0])
            allMonths.append(month)
    numsSeries = pd.Series(allNums)
    allDiffsRaw = numsSeries.diff()
    avgDiffAll = allDiffsRaw.mean()
    polished = np.round(avgDiffAll, decimals=2)
    print(f"Average Monthly Change to P&L: ${polished}")
    return allDiffsRaw, allMonths, polished

# GetBiggestIncrease receives the splices of data created above,
# it converts them into Pandas' series and inserts them into
# a newly created Dataframe. Next, it sorts the Dataframe by
# descending order of the Profit/Loss differences. It then locates
# the top most result (greatest increase), and creates a string
# variable which is split by words. This is just so we can print
# a humanized message of information to the end user.


def GetBiggestIncrease(allDiffsRaw, allMonths):
    newDF = pd.DataFrame()
    diffsData = pd.Series(allDiffsRaw)
    monthsData = pd.Series(allMonths)
    newDF.insert(0, "diffs", diffsData)
    newDF.insert(1, "month", monthsData)
    newDF_dsc = newDF.sort_values(by='diffs', ascending=False)
    topResult = newDF_dsc.iloc[0]
    wholestring = topResult.to_string()
    splits = wholestring.split()
    print(
        f"Greatest Increase in profits was in {splits[3]}, with an amount of ${splits[1]}")
    return splits[3], splits[1]

# GetBiggestLoss receives the splices of data created above,
# it converts them into Pandas' series and inserts them into
# a newly created Dataframe. Next, it sorts the Dataframe by
# ascending order of the Profit/Loss differences. It then locates
# the top most result (greatest decrease), and creates a string
# variable which is split by words. This is just so we can print
# a humanized message of information to the end user.


def GetBiggestLoss(allDiffsRaw, allMonths):
    newDF = pd.DataFrame()
    diffsData = pd.Series(allDiffsRaw)
    monthsData = pd.Series(allMonths)
    newDF.insert(0, "diffs", diffsData)
    newDF.insert(1, "month", monthsData)
    newDF_dsc = newDF.sort_values(by='diffs', ascending=True)
    topResult = newDF_dsc.iloc[0]
    wholestring = topResult.to_string()
    splits = wholestring.split()
    print(
        f"Greatest Decrease in profits was in {splits[3]}, with an amount of ${splits[1]}")
    return splits[3], splits[1]


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def Prompt(totalMonths, totalPLs, avgPL, incMonth, incAmount, decMonth, decAmount):
    ans = str(input("Would you like to save these results to a text file? y/n "))
    if ans == "y":
        fileName = str(input("Please entitle your results' file: ") + ".txt")
        outputLoc = str(
            input("Please enter your result file's absolute path: "))
        fullPath = os.path.join(outputLoc, fileName)
        if os.path.exists(fullPath):
            ansOR = str(
                input(f"File: **{fileName}** already exists at: **{outputLoc}**, Overwrite? y/n "))
            if ansOR == "y":
                with open(fullPath, 'w+') as f:
                    f.write(f"Total Number of Months: {totalMonths}\nTotal Net of Profits/Losses: {totalPLs}\nAverage Monthly Change to P%L: {avgPL}\nGreatest Increase in profits was in {incMonth}, with an amount of: ${incAmount}\nGreatest Decrease in profits was in {decMonth}, with an amount of ${decAmount}")
                print(f"Result's file overwritten to {fullPath}")
                sys.exit()
            else:
                sys.exit("Exiting without overwriting..")
        else:
            with open(fullPath, 'w') as f:
                f.write(f"Total Number of Months: {totalMonths}\nTotal Net of Profits/Losses: {totalPLs}\nAverage Monthly Change to P%L: {avgPL}\nGreatest Increase in profits was in {incMonth}, with an amount of: ${incAmount}\nGreatest Decrease in profits was in {decMonth}, with an amount of ${decAmount}")
            print(f"Result's file written to {fullPath}")
            sys.exit()
    else:
        sys.exit("Exiting without saving results to file")


        ############################################################################################
print(color.BOLD + color.RED + 'Financial Analysis Homework by Spaar' + color.END)
print("")
totalMonths = GetTotalNumbMonths()
totalPLs = GetTotalNetPL()
allDiffsRaw, allMonths, avgPL = GetAvgChangePL()
incMonth, incAmount = GetBiggestIncrease(allDiffsRaw, allMonths)
decMonth, decAmount = GetBiggestLoss(allDiffsRaw, allMonths)
print("")
Prompt(totalMonths, totalPLs, avgPL, incMonth, incAmount, decMonth, decAmount)
