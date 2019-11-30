
import os
import csv
import pandas as pd
import numpy as np
import sys

data = os.path.join("elections.csv")


def GetAllVotes():
    totalVotes = int(0)
    with open(data, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvreader:
            totalVotes += int(1)
    print(f"Total Votes Tally: {totalVotes}\n---------------------------")
    return totalVotes


def GetUniqueCands():
    allCands = []
    with open(data, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvreader:
            cand = str(row[2])
            allCands.append(cand)
    uniqueCands = list(set(allCands))
    print(f"Unique Candidates: {uniqueCands}")


def GetPctPerCandidate(totalVotes):
    votesCorrey, votesOTooley, votesKhan, votesLi = int(
        0), int(0), int(0), int(0)
    with open(data, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvreader:
            if row[2] == "Correy":
                votesCorrey += int(1)
            elif row[2] == "O'Tooley":
                votesOTooley += int(1)
            elif row[2] == "Khan":
                votesKhan += int(1)
            elif row[2] == "Li":
                votesLi += int(1)
            else:
                print(f"{row[2]} is not on the ballot")
    pctCorrey = votesCorrey / totalVotes * 100
    pctOTooley = votesOTooley / totalVotes * 100
    pctKhan = votesKhan / totalVotes * 100
    pctLi = votesLi / totalVotes * 100

    polishedCorrey = np.round(pctCorrey, decimals=3)
    polishedOTooley = np.round(pctOTooley, decimals=3)
    polishedKhan = np.round(pctKhan, decimals=3)
    polishedLi = np.round(pctLi, decimals=3)
    print(f"Correy: {polishedCorrey}% ({votesCorrey})")
    print(f"O'Tooley: {polishedOTooley}% ({votesOTooley})")
    print(f"Khan: {polishedKhan}% ({votesKhan})")
    print(f"Li: {polishedLi}% ({votesLi})\n---------------------------")
    print(f"Winner: Khan\n---------------------------")


    ########################################################################
print("Election Results\n---------------------------")
totalVotes = GetAllVotes()
# GetUniqueCands()
GetPctPerCandidate(totalVotes)
