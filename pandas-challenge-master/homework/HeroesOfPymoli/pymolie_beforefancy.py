#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
#*###########################################################################################################################
                                                     #* Dependencies #*
#*###########################################################################################################################
import pandas as pd
import numpy as np
import csv
import time

#*###########################################################################################################################
                                                  #* Primary Method Library #*
#*###########################################################################################################################
file_to_load = "Resources/purchase_data.csv"
data = pd.read_csv(file_to_load)

# GetUniquePlayers returns the count of unique players' screen names
# based off purchase data csv.


def GetUniquePlayers():
    unqPlayers = str(data['SN'].nunique())
    return unqPlayers

# GetPurchasingAnalysis_Total returns a table of:
# -Number of Unique Items
# -Average Price
# -Number of Purchases
# -Total Revenue
# based off the purchase data csv.


def GetPurchasingAnalysis_Total(unqPlayers):
    unqItems = data['Item ID'].nunique()
    avgPrice = data['Price'].mean()
    avgPrice = np.round(avgPrice, decimals=2)
    avgPricePol = str(f"${avgPrice}")
    totalPurchases = len(data.index)
    totalRev = data['Price'].sum()
    totalRev = np.round(totalRev, decimals=2)
    totalRevPol = str("${:,}").format(totalRev)
    purchasingSummaryDF = pd.DataFrame(data={'Number of Unique Items': [unqItems], 'Average Price': [
        avgPricePol], 'Number of Purchases': [totalPurchases], 'Total Revenue': [totalRevPol]})
    return purchasingSummaryDF

# GetGenderDemographics returns a table of:
# -Total Count
# -Percentage of Players
# based off the players' gender selection.


def GetGenderDemographics():
    cleanUnqData = data.drop_duplicates('SN')
    allGenders = cleanUnqData['Gender'].value_counts()
    maleGenders = allGenders["Male"]
    femaleGenders = allGenders["Female"]
    unknownGenders = allGenders["Other / Non-Disclosed"]
    malePct = float(maleGenders) / float(unqPlayers) * 100
    malePct = np.round(malePct, decimals=2)
    femalePct = float(femaleGenders) / float(unqPlayers) * 100
    femalePct = np.round(femalePct, decimals=2)
    unknownPct = float(unknownGenders) / float(unqPlayers) * 100
    unknownPct = np.round(unknownPct, decimals=2)
    genderDemographicsDF = pd.DataFrame(data={'Gender': ["Male", "Female", "Other / Non-Disclosed"], 'Total Count': [
                                        maleGenders, femaleGenders, unknownGenders], 'Percentage of Players': [malePct, femalePct, unknownPct]})
    return genderDemographicsDF, maleGenders, femaleGenders, unknownGenders, cleanUnqData

# GetPurchasingAnalysis_Gender returns a table of:
# -Purchase Count
# -Average Purchase Price
# -Total Purchase Value
# -Average Purchase per Person
# based off the players' genders.


def GetPurchasingAnalysis_Gender(maleGenders, femaleGenders, unkownGenders):
    maleStats = pd.DataFrame(data.loc[data['Gender'] == "Male"])
    femaleStats = pd.DataFrame(data.loc[data['Gender'] == "Female"])
    unknownStats = pd.DataFrame(
        data.loc[data['Gender'] == "Other / Non-Disclosed"])
    malePurchaseCount = len(maleStats.index)
    femalePurchaseCount = len(femaleStats.index)
    unknownPurchaseCount = len(unknownStats.index)
    maleAvgPurchase = maleStats['Price'].mean()
    maleAvgPurchase = np.round(maleAvgPurchase, decimals=2)
    maleAvgPurchasePol = str("${:.2f}").format(maleAvgPurchase)
    femaleAvgPurchase = femaleStats['Price'].mean()
    femaleAvgPurchase = np.round(femaleAvgPurchase, decimals=2)
    femaleAvgPurchasePol = str("${:.2f}").format(femaleAvgPurchase)
    unknownAvgPurchase = unknownStats['Price'].mean()
    unknownAvgPurchase = np.round(unknownAvgPurchase, decimals=2)
    unknownAvgPurchasePol = str("${:.2f}").format(unknownAvgPurchase)
    maleTotalPurchases = maleStats['Price'].sum()
    maleTotalPurchasesPol = str("${:.2f}").format(maleTotalPurchases)
    femaleTotalPurchases = femaleStats['Price'].sum()
    femaleTotalPurchasesPol = str("${:.2f}").format(femaleTotalPurchases)
    unknownTotalPurchases = unknownStats['Price'].sum()
    unknownTotalPurchasesPol = str("${:.2f}").format(unknownTotalPurchases)
    maleAvgPlayerPurchase = float(maleTotalPurchases) / float(maleGenders)
    maleAvgPlayerPurchase = np.round(maleAvgPlayerPurchase, decimals=2)
    maleAvgPlayerPurchasePol = str("${:.2f}").format(maleAvgPlayerPurchase)
    femaleAvgPlayerPurchase = float(
        femaleTotalPurchases) / float(femaleGenders)
    femaleAvgPlayerPurchase = np.round(femaleAvgPlayerPurchase, decimals=2)
    femaleAvgPlayerPurchasePol = str("${:.2f}").format(femaleAvgPlayerPurchase)
    unknownAvgPlayerPurchase = float(
        unknownTotalPurchases) / float(unknownGenders)
    unknownAvgPlayerPurchase = np.round(unknownAvgPlayerPurchase, decimals=2)
    unknownAvgPlayerPurchasePol = str(
        "${:.2f}").format(unknownAvgPlayerPurchase)
    genderPurchasingDF = pd.DataFrame(data={'Gender': ["Male", "Female", "Other / Non-Disclosed"], 'Purchase Count': [malePurchaseCount, femalePurchaseCount, unknownPurchaseCount], 'Average Purchase Price': [maleAvgPurchasePol, femaleAvgPurchasePol,
                                                                                                                                                                                                                unknownAvgPurchasePol], 'Total Purchase Value': [maleTotalPurchasesPol, femaleTotalPurchasesPol, unknownTotalPurchasesPol], 'Avg Total Purchase per Person': [maleAvgPlayerPurchasePol, femaleAvgPlayerPurchasePol, unknownAvgPlayerPurchasePol]})
    return genderPurchasingDF

# GetAgeDemographics returns a table of:
# -Total Count
# -Percentage of Players
# based off common age groups.


def GetAgeDemographics(cleanUnqData):
    bins = [0, 9, 14, 19, 24, 29, 34, 39, 100]
    binNames = ["<10", "10-14", "15-19", "20-24",
                "25-29", "30-34", "35-39", "40+"]
    ageDF = pd.DataFrame(data=cleanUnqData)
    ageDF["Total Count"] = pd.cut(ageDF["Age"], bins, labels=binNames)
    ageByBin = ageDF["Total Count"].value_counts()
    ageByBinDF = pd.DataFrame(ageByBin, index=[
        "<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"])
    ageByBinDF.insert(1, "key", [0, 1, 2, 3, 4, 5, 6, 7])
    pctData = []
    count0 = ageByBinDF.iloc[0]
    pct0 = count0 / float(unqPlayers) * 100
    pct0 = np.round(pct0, decimals=2).to_string().split()
    pct0 = pct0[2]
    pctData.append(pct0)
    count1 = ageByBinDF.iloc[1]
    pct1 = count1 / float(unqPlayers) * 100
    pct1 = np.round(pct1, decimals=2).to_string().split()
    pct1 = pct1[2]
    pctData.append(pct1)
    count2 = ageByBinDF.iloc[2]
    pct2 = count2 / float(unqPlayers) * 100
    pct2 = np.round(pct2, decimals=2).to_string().split()
    pct2 = pct2[2]
    pctData.append(pct2)
    count3 = ageByBinDF.iloc[3]
    pct3 = count3 / float(unqPlayers) * 100
    pct3 = np.round(pct3, decimals=2).to_string().split()
    pct3 = pct3[2]
    pctData.append(pct3)
    count4 = ageByBinDF.iloc[4]
    pct4 = count4 / float(unqPlayers) * 100
    pct4 = np.round(pct4, decimals=2).to_string().split()
    pct4 = pct4[2]
    pctData.append(pct4)
    count5 = ageByBinDF.iloc[5]
    pct5 = count5 / float(unqPlayers) * 100
    pct5 = np.round(pct5, decimals=2).to_string().split()
    pct5 = pct5[2]
    pctData.append(pct5)
    count6 = ageByBinDF.iloc[6]
    pct6 = count6 / float(unqPlayers) * 100
    pct6 = np.round(pct6, decimals=2).to_string().split()
    pct6 = pct6[2]
    pctData.append(pct6)
    count7 = ageByBinDF.iloc[7]
    pct7 = count7 / float(unqPlayers) * 100
    pct7 = np.round(pct7, decimals=2).to_string().split()
    pct7 = pct7[2]
    pctData.append(pct7)
    pctDataDF = pd.DataFrame()
    pctDataSeries = pd.Series(pctData)
    pctDataDF.insert(0, "Percentage of Players", pctDataSeries)
    ageDemographicsDF = ageByBinDF.join(pctDataDF, on='key')
    ageDemographicsDF = ageDemographicsDF.drop(['key'], axis=1)
    return ageDemographicsDF, bins, binNames

# GetPurchasingAnalysis_Age returns a table of:
# -Purchase Count
# -Average Purchase Price
# -Total Purchase Value
# -Average Total Purchase per Person
# based off common age groups.


def GetPurchasingAnalysis_Age(bins, binNames):
    purchaseCountsDF = pd.DataFrame(data=data)
    purchaseCountsDF["Age Group"] = pd.cut(
        purchaseCountsDF["Age"], bins, labels=binNames)
    # stats_ holds all the info for the age group
    stats0 = pd.DataFrame(
        purchaseCountsDF.loc[purchaseCountsDF['Age Group'] == "<10"])
    # stats_PurchaseCount is just the number of purchases in the age group
    stats0PurchaseCount = len(stats0.index)
    stats1 = pd.DataFrame(
        purchaseCountsDF.loc[purchaseCountsDF['Age Group'] == "10-14"])
    stats1PurchaseCount = len(stats1.index)
    stats2 = pd.DataFrame(
        purchaseCountsDF.loc[purchaseCountsDF['Age Group'] == "15-19"])
    stats2PurchaseCount = len(stats2.index)
    stats3 = pd.DataFrame(
        purchaseCountsDF.loc[purchaseCountsDF['Age Group'] == "20-24"])
    stats3PurchaseCount = len(stats3.index)
    stats4 = pd.DataFrame(
        purchaseCountsDF.loc[purchaseCountsDF['Age Group'] == "25-29"])
    stats4PurchaseCount = len(stats4.index)
    stats5 = pd.DataFrame(
        purchaseCountsDF.loc[purchaseCountsDF['Age Group'] == "30-34"])
    stats5PurchaseCount = len(stats5.index)
    stats6 = pd.DataFrame(
        purchaseCountsDF.loc[purchaseCountsDF['Age Group'] == "35-39"])
    stats6PurchaseCount = len(stats6.index)
    stats7 = pd.DataFrame(
        purchaseCountsDF.loc[purchaseCountsDF['Age Group'] == "40+"])
    stats7PurchaseCount = len(stats7.index)
    # These are the average purchase prices for each age group
    avgPurchasePrice0 = stats0['Price'].mean()
    avgPurchasePrice0 = str("${:.2f}").format(avgPurchasePrice0)
    avgPurchasePrice1 = stats1['Price'].mean()
    avgPurchasePrice1 = str("${:.2f}").format(avgPurchasePrice1)
    avgPurchasePrice2 = stats2['Price'].mean()
    avgPurchasePrice2 = str("${:.2f}").format(avgPurchasePrice2)
    avgPurchasePrice3 = stats3['Price'].mean()
    avgPurchasePrice3 = str("${:.2f}").format(avgPurchasePrice3)
    avgPurchasePrice4 = stats4['Price'].mean()
    avgPurchasePrice4 = str("${:.2f}").format(avgPurchasePrice4)
    avgPurchasePrice5 = stats5['Price'].mean()
    avgPurchasePrice5 = str("${:.2f}").format(avgPurchasePrice5)
    avgPurchasePrice6 = stats6['Price'].mean()
    avgPurchasePrice6 = str("${:.2f}").format(avgPurchasePrice6)
    avgPurchasePrice7 = stats7['Price'].mean()
    avgPurchasePrice7 = str("${:.2f}").format(avgPurchasePrice7)
    # Total Purchase value for each age group
    totalPurchases0raw = stats0['Price'].sum()
    totalPurchases0 = str("${:.2f}").format(totalPurchases0raw)
    totalPurchases1raw = stats1['Price'].sum()
    totalPurchases1 = str("${:.2f}").format(totalPurchases1raw)
    totalPurchases2raw = stats2['Price'].sum()
    totalPurchases2 = str("${:.2f}").format(totalPurchases2raw)
    totalPurchases3raw = stats3['Price'].sum()
    totalPurchases3 = str("${:,}").format(totalPurchases3raw)
    totalPurchases4raw = stats4['Price'].sum()
    totalPurchases4 = str("${:.2f}").format(totalPurchases4raw)
    totalPurchases5raw = stats5['Price'].sum()
    totalPurchases5 = str("${:.2f}").format(totalPurchases5raw)
    totalPurchases6raw = stats6['Price'].sum()
    totalPurchases6 = str("${:.2f}").format(totalPurchases6raw)
    totalPurchases7raw = stats7['Price'].sum()
    totalPurchases7 = str("${:.2f}").format(totalPurchases7raw)
    # Average total purchase per person per age group
    unqCount0 = str(stats0['SN'].nunique())
    avgUnqPlayerPurchase0raw = float(totalPurchases0raw) / float(unqCount0)
    avgUnqPlayerPurchase0 = str("${:.2f}").format(avgUnqPlayerPurchase0raw)
    unqCount1 = str(stats1['SN'].nunique())
    avgUnqPlayerPurchase1raw = float(totalPurchases1raw) / float(unqCount1)
    avgUnqPlayerPurchase1 = str("${:.2f}").format(avgUnqPlayerPurchase1raw)
    unqCount2 = str(stats2['SN'].nunique())
    avgUnqPlayerPurchase2raw = float(totalPurchases2raw) / float(unqCount2)
    avgUnqPlayerPurchase2 = str("${:.2f}").format(avgUnqPlayerPurchase2raw)
    unqCount3 = str(stats3['SN'].nunique())
    avgUnqPlayerPurchase3raw = float(totalPurchases3raw) / float(unqCount3)
    avgUnqPlayerPurchase3 = str("${:.2f}").format(avgUnqPlayerPurchase3raw)
    unqCount4 = str(stats4['SN'].nunique())
    avgUnqPlayerPurchase4raw = float(totalPurchases4raw) / float(unqCount4)
    avgUnqPlayerPurchase4 = str("${:.2f}").format(avgUnqPlayerPurchase4raw)
    unqCount5 = str(stats5['SN'].nunique())
    avgUnqPlayerPurchase5raw = float(totalPurchases5raw) / float(unqCount5)
    avgUnqPlayerPurchase5 = str("${:.2f}").format(avgUnqPlayerPurchase5raw)
    unqCount6 = str(stats6['SN'].nunique())
    avgUnqPlayerPurchase6raw = float(totalPurchases6raw) / float(unqCount6)
    avgUnqPlayerPurchase6 = str("${:.2f}").format(avgUnqPlayerPurchase6raw)
    unqCount7 = str(stats7['SN'].nunique())
    avgUnqPlayerPurchase7raw = float(totalPurchases7raw) / float(unqCount7)
    avgUnqPlayerPurchase7 = str("${:.2f}").format(avgUnqPlayerPurchase7raw)
    ageGroupPurchasingDF = pd.DataFrame(data={'Age Groups': ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"], 'Purchase Count': [stats0PurchaseCount, stats1PurchaseCount, stats2PurchaseCount, stats3PurchaseCount, stats4PurchaseCount, stats5PurchaseCount, stats6PurchaseCount, stats7PurchaseCount], 'Average Purchase Price': [avgPurchasePrice0, avgPurchasePrice1, avgPurchasePrice2, avgPurchasePrice3, avgPurchasePrice4,
                                                                                                                                                                                                                                                                                                                                                         avgPurchasePrice5, avgPurchasePrice6, avgPurchasePrice7], 'Total Purchase Value': [totalPurchases0, totalPurchases1, totalPurchases2, totalPurchases3, totalPurchases4, totalPurchases5, totalPurchases6, totalPurchases7], 'Avg Total Purchase per Person': [avgUnqPlayerPurchase0, avgUnqPlayerPurchase1, avgUnqPlayerPurchase2, avgUnqPlayerPurchase3, avgUnqPlayerPurchase4, avgUnqPlayerPurchase5, avgUnqPlayerPurchase6, avgUnqPlayerPurchase7]})
    return ageGroupPurchasingDF

# GetTopSpenders returns a [sorted by: Total Purchase Value] table of:
# -Purchase Count
# -Average Purchase Price
# -Total Purchase Value
# based off the 5 specified players' screen names.


def GetTopSpenders():
    spendersDF = pd.DataFrame(data=data)
    # raw DFs for each player
    statsLisosia93 = pd.DataFrame(
        spendersDF.loc[spendersDF['SN'] == "Lisosia93"])
    statsIdastidru52 = pd.DataFrame(
        spendersDF.loc[spendersDF['SN'] == "Idastidru52"])
    statsChamjask73 = pd.DataFrame(
        spendersDF.loc[spendersDF['SN'] == "Chamjask73"])
    statsIral74 = pd.DataFrame(spendersDF.loc[spendersDF['SN'] == "Iral74"])
    statsIskadarya95 = pd.DataFrame(
        spendersDF.loc[spendersDF['SN'] == "Iskadarya95"])
    # Purchase counts for each player
    purchaseCountLisosia93 = len(statsLisosia93.index)
    purchaseCountIdastidru52 = len(statsIdastidru52.index)
    purchaseCountChamjask73 = len(statsChamjask73.index)
    purchaseCountIral74 = len(statsIral74.index)
    purchaseCountIskadarya95 = len(statsIskadarya95.index)
    # Avg Purchase price per player
    avgPurchaseLisosia93 = statsLisosia93['Price'].mean()
    avgPurchaseLisosia93 = str("${:.2f}").format(avgPurchaseLisosia93)
    avgPurchaseIdastidru52 = statsIdastidru52['Price'].mean()
    avgPurchaseIdastidru52 = str("${:.2f}").format(avgPurchaseIdastidru52)
    avgPurchaseChamjask73 = statsChamjask73['Price'].mean()
    avgPurchaseChamjask73 = str("${:.2f}").format(avgPurchaseChamjask73)
    avgPurchaseIral74 = statsIral74['Price'].mean()
    avgPurchaseIral74 = str("${:.2f}").format(avgPurchaseIral74)
    avgPurchaseIskadarya95 = statsIskadarya95['Price'].mean()
    avgPurchaseIskadarya95 = str("${:.2f}").format(avgPurchaseIskadarya95)
    # total purchases per player
    totalPurchasesLisosia93 = statsLisosia93['Price'].sum()
    totalPurchasesLisosia93 = str("${:.2f}").format(totalPurchasesLisosia93)
    totalPurchasesIdastidru52 = statsIdastidru52['Price'].sum()
    totalPurchasesIdastidru52 = str(
        "${:.2f}").format(totalPurchasesIdastidru52)
    totalPurchasesChamjask73 = statsChamjask73['Price'].sum()
    totalPurchasesChamjask73 = str("${:.2f}").format(totalPurchasesChamjask73)
    totalPurchasesIral74 = statsIral74['Price'].sum()
    totalPurchasesIral74 = str("${:.2f}").format(totalPurchasesIral74)
    totalPurchasesIskadarya95 = statsIskadarya95['Price'].sum()
    totalPurchasesIskadarya95 = str(
        "${:.2f}").format(totalPurchasesIskadarya95)
    spendersSummaryDF = pd.DataFrame(data={'SN': ["Lisosia93", "Idastidru52", "Chamjask73", "Iral74", "Iskadarya95"], 'Purchase Count': [purchaseCountLisosia93, purchaseCountIdastidru52, purchaseCountChamjask73, purchaseCountIral74, purchaseCountIskadarya95], 'Average Purchase Price': [
                                     avgPurchaseLisosia93, avgPurchaseIdastidru52, avgPurchaseChamjask73, avgPurchaseIral74, avgPurchaseIskadarya95], 'Total Purchase Value': [totalPurchasesLisosia93, totalPurchasesIdastidru52, totalPurchasesChamjask73, totalPurchasesIral74, totalPurchasesIskadarya95]})
    spendersSummaryDFsorted = spendersSummaryDF.sort_values(
        by='Total Purchase Value', ascending=False)
    return spendersSummaryDFsorted

# GetMostPopularItems returns a [sorted by: Purchase Count] table of:
# -Item Name
# -Purchase Count
# -Item Price
# -Total Purchase Value
# based off the specified items' IDs.


def GetMostPopularItems():
    popItemsDF = pd.DataFrame(data=data)
    # rawDFs by specified Item ID
    stats178 = pd.DataFrame(popItemsDF.loc[popItemsDF['Item ID'] == 178])
    stats145 = pd.DataFrame(popItemsDF.loc[popItemsDF['Item ID'] == 145])
    stats108 = pd.DataFrame(popItemsDF.loc[popItemsDF['Item ID'] == 108])
    stats82 = pd.DataFrame(popItemsDF.loc[popItemsDF['Item ID'] == 82])
    stats19 = pd.DataFrame(popItemsDF.loc[popItemsDF['Item ID'] == 19])
    # names of each item per ID
    name178 = stats178.iloc[1, 5]
    name145 = stats145.iloc[1, 5]
    name108 = stats108.iloc[1, 5]
    name82 = stats82.iloc[1, 5]
    name19 = stats19.iloc[1, 5]
    # Purchase counts per item
    purchases178 = len(stats178.index)
    purchases145 = len(stats145.index)
    purchases108 = len(stats108.index)
    purchases82 = len(stats82.index)
    purchases19 = len(stats19.index)
    # Item Prices per ID
    price178raw = stats178.iloc[1, 6]
    price178 = str("${:.2f}").format(price178raw)
    price145raw = stats145.iloc[1, 6]
    price145 = str("${:.2f}").format(price145raw)
    price108raw = stats108.iloc[1, 6]
    price108 = str("${:.2f}").format(price108raw)
    price82raw = stats82.iloc[1, 6]
    price82 = str("${:.2f}").format(price82raw)
    price19raw = stats19.iloc[1, 6]
    price19 = str("${:.2f}").format(price19raw)
    # Total Purchase Value Per ID
    rawTotals = []
    total178raw = stats178['Price'].sum()
    rawTotals.append(total178raw)
    total178 = str("${:.2f}").format(total178raw)
    total145raw = stats145['Price'].sum()
    rawTotals.append(total145raw)
    total145 = str("${:.2f}").format(total145raw)
    total108raw = stats108['Price'].sum()
    rawTotals.append(total108raw)
    total108 = str("${:.2f}").format(total108raw)
    total82raw = stats82['Price'].sum()
    rawTotals.append(total82raw)
    total82 = str("${:.2f}").format(total82raw)
    total19raw = stats19['Price'].sum()
    rawTotals.append(total19raw)
    total19 = str("${:.2f}").format(total19raw)
    mostPopularItemsDF = pd.DataFrame(data={'Item ID': ["178", "145", "108", "82", "19"], 'Item Name': [name178, name145, name108, name82, name19], 'Purchase Count': [
                                      purchases178, purchases145, purchases108, purchases82, purchases19], 'Item Price': [price178, price145, price108, price82, price19], 'Total Purchase Value': [total178, total145, total108, total82, total19]})
    mostPopularItemsDFsorted = mostPopularItemsDF.sort_values(
        by='Purchase Count', ascending=False)
    return mostPopularItemsDFsorted, rawTotals, mostPopularItemsDF

# GetMostProfitableItems returns a [sorted by: Purchase Value] table of:
# -Item Name
# -Purchase Count
# -Item Price
# -Total Purchase Value
# based off the specified items' IDs.


def GetMostProfitableItems(rawTotals, mostPopularItemsDF):
    rawTotalsDF = pd.DataFrame()
    rawTotalsSeries = pd.Series(rawTotals)
    rawTotalsDF.insert(0, "rawsForSorting", rawTotalsSeries)
    rawTotalsDF

    lastTable = mostPopularItemsDF.join(rawTotalsDF)
    lastTableSorted = lastTable.sort_values(
        by='rawsForSorting', ascending=False)
    lastTableSorted = lastTableSorted.drop(['rawsForSorting'], axis=1)
    return lastTableSorted

#*###########################################################################################################################
                                                #* Auxillary Method Library #*
#*###########################################################################################################################

#*###########################################################################################################################
                                                        #* Finesse #*
#*###########################################################################################################################

class color:
    BOLD = '\033[1m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'


lineSep = str(
    '+***********************************' + color.RED + '---------------------------------------' + color.END + '*************************************+')

disgustingASCII = '''
 __ __    ___  ____    ___     ___  _____      ___   _____      ____  __ __  ___ ___   ___   _      ____
|  T  T  /  _]|    \  /   \   /  _]/ ___/     /   \ |     |    |    \|  T  T|   T   T /   \ | T    l    j
|  l  | /  [_ |  D  )Y     Y /  [_(   \_     Y     Y|   __j    |  o  )  |  || _   _ |Y     Y| |     |  T
|  _  |Y    _]|    / |  O  |Y    _]\__  T    |  O  ||  l_      |   _/|  ~  ||  \_/  ||  O  || l___  |  |
|  |  ||   [_ |    \ |     ||   [_ /  \ |    |     ||   _]     |  |  l___, ||   |   ||     ||     T |  |
|  |  ||     T|  .  Yl     !|     T\    |    l     !|  T       |  |  |     !|   |   |l     !|     | j  l
l__j__jl_____jl__j\_j \___/ l_____j \___j     \___/ l__j       l__j  l____/ l___j___j \___/ l_____j|____j

'''
#*###########################################################################################################################
                                                        #* Main #*
#*###########################################################################################################################
print(disgustingASCII)
print(color.RED + color.BOLD +
      '                                                                                                   Spaar' + color.END)
print("\n")
time.sleep(1)
unqPlayers = GetUniquePlayers()
PurchasingAnalysis_Total___Summary = GetPurchasingAnalysis_Total(unqPlayers)
print(lineSep)
print(color.RED + '+**********************************| ' + color.END + color.BOLD +
      ' Purchasing Analysis (Total) Summary:' + color.END + color.RED + ' |************************************+' + color.END)
print(lineSep + "\n")
print(PurchasingAnalysis_Total___Summary.to_string(index=False))
time.sleep(1)
GenderDemographics___Summary, maleGenders, femaleGenders, unknownGenders, cleanUnqData = GetGenderDemographics()
print("\n" + lineSep)
print(color.RED + '+**********************************| ' + color.END + color.BOLD +
      '     Gender Demographics Summary:    ' + color.END + color.RED + ' |************************************+' + color.END)
print(lineSep + "\n")
print(GenderDemographics___Summary.to_string(index=False))
time.sleep(1)
PurchasingAnalysis_Gender___Summary = GetPurchasingAnalysis_Gender(
    maleGenders, femaleGenders, unknownGenders)
print("\n" + lineSep)
print(color.RED + '+**********************************| ' + color.END + color.BOLD +
      'Purchasing Analysis (Gender) Summary:' + color.END + color.RED + ' |************************************+' + color.END)
print(lineSep + "\n")
print(PurchasingAnalysis_Gender___Summary.to_string(index=False))
time.sleep(1)
AgeDemographics___Summary, bins, binNames = GetAgeDemographics(cleanUnqData)
print("\n" + lineSep)
print(color.RED + '+**********************************| ' + color.END + color.BOLD +
      '       Age Demographics Summary:     ' + color.END + color.RED + ' |************************************+' + color.END)
print(lineSep + "\n")
print(AgeDemographics___Summary.to_string(index=False))
time.sleep(1)
PurchasingAnalysis_Age___Summary = GetPurchasingAnalysis_Age(bins, binNames)
print("\n" + lineSep)
print(color.RED + '+**********************************| ' + color.END + color.BOLD +
      '  Purchasing Analysis (Age) Summary: ' + color.END + color.RED + ' |************************************+' + color.END)
print(lineSep + "\n")
print(PurchasingAnalysis_Age___Summary.to_string(index=False))
time.sleep(1)
TopSpenders___Summary = GetTopSpenders()
print("\n" + lineSep)
print(color.RED + '+**********************************| ' + color.END + color.BOLD +
      '         Top Spenders Summary:       ' + color.END + color.RED + ' |************************************+' + color.END)
print(lineSep + "\n")
print(TopSpenders___Summary.to_string(index=False))
time.sleep(1)
MostPopularItems___Summary, rawTotals, mostPopularItemsDF = GetMostPopularItems()
print("\n" + lineSep)
print(color.RED + '+**********************************| ' + color.END + color.BOLD +
      '      Most Popular Items Summary:    ' + color.END + color.RED + ' |************************************+' + color.END)
print(lineSep + "\n")
print(MostPopularItems___Summary.to_string(index=False))
time.sleep(1)
MostProfitableItems___Summary = GetMostProfitableItems(
    rawTotals, mostPopularItemsDF)
print("\n" + lineSep)
print(color.RED + '+**********************************| ' + color.END + color.BOLD +
      '    Most Profitable Items Summary:   ' + color.END + color.RED + ' |************************************+' + color.END)
print(lineSep + "\n")
print(MostProfitableItems___Summary.to_string(index=False))
