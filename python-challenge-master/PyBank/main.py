# Refactored version of PyBank_sloppy.py

import os
import csv
import pandas as pd
import numpy as np
import sys

data = os.path.join("BankCSV.csv")

# Prompt asks the user if they would like to save the acquired data to a
# file on their local drive. Prompt receives all necessairy information from
# the other 2 functions and is able to write a report containing everything.


def Prompt(totalMonths, totalPLs, avgPL, incMonth, incAmount, decMonth, decAmount):
    ans = str(input("Would you like to save these results to a text file? y/n "))
    if ans == "y":
        fileName = str(input("Please entitle your results' file: ") + ".txt")
        outputLoc = str(
            input("Please enter your result file's absolute path: "))
        fullPath = os.path.join(outputLoc, fileName)
        if os.path.exists(fullPath):
            ansOR = str(
                input(f"File: {color.BOLD}{color.UNDERLINE}{fileName}{color.END} already exists at: {color.BOLD}{outputLoc}{color.END}, {color.RED}{color.BOLD}Overwrite?{color.END} y/n "))
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

# ExecutePyBank opens the banking data csv and populates lists and vars of
# all date ranges + their totals, all profit/loss figures + their totals. It
# next casts these figures into new DataFrames where it then is able to sort
# and calculate the incremental averages, means, and relay all information
# required.


def ExecutePyBank():
    allNums, allMonths = [], []
    totalMonths, totalPL = int(0), int(0)
    with open(data, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvreader:
            num = float(row[1])
            allNums.append(num)
            month = str(row[0])
            allMonths.append(month)
            totalMonths += int(1)
            totalPL += int(row[1])
    numsSeries = pd.Series(allNums)
    allDiffsRaw = numsSeries.diff()
    avgDiffAll = allDiffsRaw.mean()
    polished = np.round(avgDiffAll, decimals=2)
    newDF = pd.DataFrame()
    diffsData = pd.Series(allDiffsRaw)
    monthsData = pd.Series(allMonths)
    newDF.insert(0, "diffs", diffsData)
    newDF.insert(1, "month", monthsData)
    newDF_dsc = newDF.sort_values(by='diffs', ascending=False)
    topResult_dsc = newDF_dsc.iloc[0]
    winnerString_dsc = topResult_dsc.to_string()
    splits_dsc = winnerString_dsc.split()
    newDF_asc = newDF.sort_values(by='diffs', ascending=True)
    topResult_asc = newDF_asc.iloc[0]
    winnerString_asc = topResult_asc.to_string()
    splits_asc = winnerString_asc.split()
    return totalMonths, totalPL, polished, splits_dsc[3], float(splits_dsc[1]), splits_asc[3], float(splits_asc[1])


class color:
    BOLD = '\033[1m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'


###########################################################################
# main
totalMonths, totalPLs, avgPL, incMonth, incAmount, decMonth, decAmount = ExecutePyBank()
print(color.BOLD + color.RED + 'PyBank Financial Analysis by Spaar' + color.END)
print("")
print("----------------------------------------------")
print("Total Months: {}".format(totalMonths))
print("Total: ${}".format(totalPLs))
print("AverageChange: ${}".format(avgPL))
print("GreatestIncrease in Profits: {} (${:,.0f})".format(incMonth, incAmount))
print("Greatest Decrease in Profits: {} (${:,.0f})".format(decMonth, decAmount))
print("")
Prompt(totalMonths, totalPLs, avgPL, incMonth, incAmount, decMonth, decAmount)
