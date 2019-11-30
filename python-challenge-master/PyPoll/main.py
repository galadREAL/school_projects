
import os
import csv
import pandas as pd
import numpy as np
import sys

csvdata = os.path.join("elections.csv")

# ExecutePyPoll opens the polling data csv and populates lists and vars of
# total votes, vote by candidate, number of unique conadidates and then
# returns its findings.


def ExecutePyPoll():
    totalVotes, allVotesCand = int(0), []
    uniqueCands = list(set(allVotesCand))
    # for _ in uniqueCands make new int(0) var
    votesCorrey, votesOTooley, votesKhan, votesLi = int(
        0), int(0), int(0), int(0)
    with open(csvdata, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvfile)
        for row in csvreader:
            totalVotes += int(1)
            cand = str(row[2])
            # Match it to the created int(0) var instead
            if cand == "Correy":
                votesCorrey += int(1)
            elif cand == "O'Tooley":
                votesOTooley += int(1)
            elif cand == "Khan":
                votesKhan += int(1)
            elif cand == "Li":
                votesLi += int(1)
            else:
                print(f"Candidate: {cand} isn't on the Ballot")
    print(
        f"Total Votes: {totalVotes}\n----------------------------------------------")
    # return the created int() vars instead
    return votesCorrey, votesOTooley, votesKhan, votesLi, totalVotes

# CalculateBallots receives the info the ExecutePyPoll sends. It then
# creates a new DataFrame with that information, and sorts it by the number
# of votes descending. By location in the sorted DF, the rankings are
# established as an Alpha, Beta, Gamma, Delta var. They are further casted
# into strings and split by word so that we can pass the info around.


def CalculateBallots(vC, vO, vK, vL, tV):
    newDF = pd.DataFrame(
        data={'name': ["Correy", "O'Tooley", "Khan", "Li"], 'votes': [vC, vO, vK, vL], 'percentage': [vC / tV * 100, vO / tV * 100, vK / tV * 100, vL / tV * 100]})
    newDF_dsc = newDF.sort_values(by="votes", ascending=False)
    print(
        f"All Unique Candidates Descending by Votes Received:\n")
    alpha = newDF_dsc.iloc[0]
    alphaString = alpha.to_string()
    splitAlpha = alphaString.split()
    print(
        f"{splitAlpha[1]} had {splitAlpha[5]}% of the running with {splitAlpha[3]} votes cast")
    beta = newDF_dsc.iloc[1]
    betaString = beta.to_string()
    splitBeta = betaString.split()
    print(
        f"{splitBeta[1]} had {splitBeta[5]}% of the running with {splitBeta[3]} votes cast")
    gamma = newDF_dsc.iloc[2]
    gammaString = gamma.to_string()
    splitGamma = gammaString.split()
    print(
        f"{splitGamma[1]} had {splitGamma[5]}% of the running with {splitGamma[3]} votes cast")
    delta = newDF_dsc.iloc[3]
    deltaString = delta.to_string()
    splitDelta = deltaString.split()
    print(
        f"{splitDelta[1]} had {splitDelta[5]}% of the running with {splitDelta[3]} votes cast\n----------------------------------------------")
    print(f"Winner: {color.BOLD}{color.UNDERLINE}{splitAlpha[1]}{color.END}\n")
    return splitAlpha[1], splitAlpha[5], splitAlpha[3], splitBeta[1], splitBeta[5], splitBeta[3], splitGamma[1], splitGamma[5], splitGamma[3], splitDelta[1], splitDelta[5], splitDelta[3]

# Prompt asks the user if they would like to save the acquired data to a
# file on their local drive. Prompt receives all necessairy information from
# the other 2 functions and is able to write a report containing everything.


def Prompt(totalVotes, alphaName, alphaPct, alphaVotes, betaName, betaPct, betaVotes, gammaName, gammaPct, gammaVotes, deltaName, deltaPct, deltaVotes):
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
                    f.write(
                        f"Total Votes: {totalVotes}\n----------------------------------------------\nAll Unique Candidates Descending by Votes Received\n\n{alphaName} had {alphaPct}% of the running with {alphaVotes} votes cast\n{betaName} had {betaPct}% of the running with {betaVotes} votes cast\n{gammaName} had {gammaPct}% of the running with {gammaVotes} votes cast\n{deltaName} had {deltaPct}% of the running with {deltaVotes} votes cast\n----------------------------------------------\nWinner: {alphaName}")
                print(f"Result's file overwritten to {fullPath}")
                sys.exit()
            else:
                sys.exit("Exiting without overwriting..")
        else:
            with open(fullPath, 'w') as f:
                f.write(
                    f"Total Votes: {totalVotes}\n----------------------------------------------\nAll Unique Candidates Descending by Votes Received\n\n{alphaName} had {alphaPct}% of the running with {alphaVotes} votes cast\n{betaName} had {betaPct}% of the running with {betaVotes} votes cast\n{gammaName} had {gammaPct}% of the running with {gammaVotes} votes cast\n{deltaName} had {deltaPct}% of the running with {deltaVotes} votes cast\n----------------------------------------------\nWinner: {alphaName}")
            print(f"Result's file written to {fullPath}")
            sys.exit()
    else:
        sys.exit("Exiting without saving results to file")


class color:
    BOLD = '\033[1m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
###########################################################################
# main


print(color.BOLD + color.RED +
      'PyPoll Election Ballot Analysis by Spaar' + color.END)
print("\n----------------------------------------------")
vC, vO, vK, vL, tV = ExecutePyPoll()
alphaName, alphaPct, alphaVotes, betaName, betaPct, betaVotes, gammaName, gammaPct, gammaVotes, deltaName, deltaPct, deltaVotes = CalculateBallots(
    vC, vO, vK, vL, tV)
Prompt(tV, alphaName, alphaPct, alphaVotes, betaName, betaPct, betaVotes,
       gammaName, gammaPct, gammaVotes, deltaName, deltaPct, deltaVotes)
