#!/usr/bin/env python
# coding: utf-8
# * Note:
# The instructions were to save each graph to the user's local disk --- I turned off
# that function being automated, instead the user is prompted to view, save, or both
# for each of their graphs in CLI-esque menu of options.
#
# My 3 observable trends are available via the first prompt in the program.
#
# To get started, run all cells then navigate towards the bottom of the "In [ ]:"
# shells list where you'll find a prompt waiting for input.
#*####################################################################################
# *                                   Dependencies
#*####################################################################################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import time
#*####################################################################################
# *                                  .csv >> pd.DF
#*####################################################################################
# Declare both csv files' locations as variables.
city_data_to_load = "data/city_data.csv"
ride_data_to_load = "data/ride_data.csv"
# Create a DF for each file.
cityData = pd.read_csv(city_data_to_load)
rideData = pd.read_csv(ride_data_to_load)
# Merge both of the DFs together on the cities.
allData = pd.merge(cityData, rideData, how="left", on=["city", "city"])
#*####################################################################################
# *                                  DF data allocation
#*####################################################################################
# All data is split into new DF by its type of city.
urbanDF = allData.loc[allData['type'] == "Urban"]
suburbanDF = allData.loc[allData['type'] == "Suburban"]
ruralDF = allData.loc[allData['type'] == "Rural"]
# Total trips column is added with an int(1) to aid calculating sum of trips per
# [urban] city later.
urbanDF.insert(1, "Total Trips", 1)
# Minor renaming  a e s t h e t i c s.
urbanDF = urbanDF.rename(
    columns={"city": "City", "driver_count": "Driver Count"})
# Average fare per [urban] city is calculated.
urban_cityfaresAVG = urbanDF.groupby('City')['fare'].mean()
# Sum of trips per [urban] city is calculated.
urban_citytripsSUM = urbanDF.groupby('City')['Total Trips'].sum()
# Average fare and sum of trips merged together into a new DF on the [urban] cities.
urban_FaresTripsAVG = pd.merge(
    urban_cityfaresAVG, urban_citytripsSUM, how="left", on=["City"])
# Minor renaming  a e s t h e t i c s.
urban_FaresTripsAVG = urban_FaresTripsAVG.rename(
    columns={"fare": "Average Fare"})
# Average driver count per [urban] city is calculated.
urban_citydriversAVG = urbanDF.groupby('City')['Driver Count'].mean()
# Average driver count per city is merged into the new DF containing average fare and
# sum of rides per [urban] city.
urban_Ex1 = pd.merge(urban_FaresTripsAVG,
                     urban_citydriversAVG, how="left", on=["City"])
urban_Ex1 = urban_Ex1.sort_values(by='Driver Count')
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# Total trips column is added with an int(1) to aid calculating sum of trips per
# [suburban] city later.
suburbanDF.insert(1, "Total Trips", 1)
# Minor renaming  a e s t h e t i c s.
suburbanDF = suburbanDF.rename(
    columns={"city": "City", "driver_count": "Driver Count"})
# Average fare per [suburban] city is calculated.
suburban_cityfaresAVG = suburbanDF.groupby('City')['fare'].mean()
# Sum of trips per [suburban] city is calculated.
suburban_citytripsSUM = suburbanDF.groupby('City')['Total Trips'].sum()
# Average fare and sum of trips merged together into a new DF on the [suburban] cities.
suburban_FaresTripsAVG = pd.merge(
    suburban_cityfaresAVG, suburban_citytripsSUM, how="left", on=["City"])
# Minor renaming  a e s t h e t i c s.
suburban_FaresTripsAVG = suburban_FaresTripsAVG.rename(
    columns={"fare": "Average Fare"})
# Average driver count per [suburban] city is calculated.
suburban_citydriversAVG = suburbanDF.groupby('City')['Driver Count'].mean()
# Average driver count per city is merged into the new DF containing average fare and
# sum of rides per [suburban] city.
suburban_Ex1 = pd.merge(suburban_FaresTripsAVG,
                        suburban_citydriversAVG, how="left", on=["City"])
suburban_Ex1 = suburban_Ex1.sort_values(by='Driver Count')
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# Total trips column is added with an int(1) to aid calculating sum of trips per
# [rural] city later.
ruralDF.insert(1, "Total Trips", 1)
# Minor renaming  a e s t h e t i c s.
ruralDF = ruralDF.rename(
    columns={"city": "City", "driver_count": "Driver Count"})
# Average fare per [rural] city is calculated.
rural_cityfaresAVG = ruralDF.groupby('City')['fare'].mean()
# Sum of trips per [rural] city is calculated.
rural_citytripsSUM = ruralDF.groupby('City')['Total Trips'].sum()
# Average fare and sum of trips merged together into a new DF on the [rural] cities.
rural_FaresTripsAVG = pd.merge(
    rural_cityfaresAVG, rural_citytripsSUM, how="left", on=["City"])
# Minor renaming  a e s t h e t i c s.
rural_FaresTripsAVG = rural_FaresTripsAVG.rename(
    columns={"fare": "Average Fare"})
# Average driver count per [rural] city is calculated
rural_citydriversAVG = ruralDF.groupby('City')['Driver Count'].mean()
# Average driver count per city is merged into the new DF containing average fare and
# sum of rides per [rural city.
rural_Ex1 = pd.merge(rural_FaresTripsAVG,
                     rural_citydriversAVG, how="left", on=["City"])
rural_Ex1 = rural_Ex1.sort_values(by='Driver Count')
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# Duplicates of cities dropped for use with the last pie graph.
urbanDF_dropdupes = pd.DataFrame(urbanDF.drop_duplicates('City'))
suburbanDF_dropdupes = pd.DataFrame(suburbanDF.drop_duplicates('City'))
ruralDF_dropdupes = pd.DataFrame(ruralDF.drop_duplicates('City'))
#*####################################################################################
# *                    Bubble/Scatter Plots' Global Constants
#*####################################################################################
# The X + Y axes, and S value is set to this particular [urban] city's drivers * 10.
urbanX = urban_Ex1['Total Trips']
urbanY = urban_Ex1['Average Fare']
urbanS = 10 * (pd.Series(urban_Ex1['Driver Count'].values.tolist()))
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# The X + Y axes, and S value is set to this particular [suburban] city's drivers * 10.
suburbanX = suburban_Ex1['Total Trips']
suburbanY = suburban_Ex1['Average Fare']
suburbanS = 10 * (pd.Series(suburban_Ex1['Driver Count'].values.tolist()))
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# The X + Y axes, and S value is set to this particular [rural] city's drivers * 10.
ruralX = rural_Ex1['Total Trips']
ruralY = rural_Ex1['Average Fare']
ruralS = 10 * (pd.Series(rural_Ex1['Driver Count'].values.tolist()))
#*####################################################################################
# *                           Pie Graphs' Global Constants
#*####################################################################################
# Explode is set up for all future Pie graphs so the 1st item is distinguished.
explode = (0.1, 0, 0)
# The colors for all future Pie graphs are set to Coral, Light Sky Blue, and Gold per
# instructions on the homework's README.md.
colors = ["coral", "lightskyblue", "gold"]
# All unique city types for all future Pie graphs are cast into an array.
pieCityTypes = allData['type'].unique()
#*####################################################################################
# *                             Total Fares by City Type
#*####################################################################################
# The sum of all fares per city type are calculated and cast into an array.
pieCityData_Fares = [urbanDF['fare'].sum(
), suburbanDF['fare'].sum(), ruralDF['fare'].sum()]
#*####################################################################################
# *                             Total Rides by City Type
#*####################################################################################
# The sum of all rides per city type are calculated and cast into an array.
pieCityData_Rides = [urbanDF['Total Trips'].sum(
), suburbanDF['Total Trips'].sum(), ruralDF['Total Trips'].sum()]
#*####################################################################################
# *                    Driver Percentage Allocation by City Type
#*####################################################################################
# The sum of all drivers per city type are calculated and cast into an array.
pieCityData_Drivers = [urbanDF_dropdupes['Driver Count'].sum(
), suburbanDF_dropdupes['Driver Count'].sum(), ruralDF_dropdupes['Driver Count'].sum()]
#*####################################################################################
# *                             CLI-esque Finesse
#*####################################################################################
# ANSI colors for pretty terminal formatting are declared.


class color:
    BOLD = '\033[1m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    REVERSED = '\u001b[7m'
    BLINK = '\033[5m'


# A multicolored line seperator is established
lineSep = str(
    '+***********************************' + color.RED + '---------------------------------------' + color.END + '*************************************+')
# "Pyber" ASCII art is established.
disgustingASCII = '''
    '||''|.           '||
     ||   || .... ...  || ...    ....  ... ..
     ||...|'  '|.  |   ||'  || .|...||  ||' ''
     ||        '|.|    ||    | ||       ||
    .||.        '|     '|...'   '|...' .||.
             .. |
              ''
'''

trendsSummary = '''

                         𝕆 𝕓 𝕤 𝕖 𝕣 𝕧 𝕒 𝕓 𝕝 𝕖   𝕋 𝕣 𝕖 𝕟 𝕕 𝕤 :



 𝟏) Over 2/3 of all rides (68.4%) are given by over 4/5 of all drivers (80.9%) in
    Urban city types, yet these rides produce the least amount in gross fares
    (avg: $24.52/ea), the least amount grossed per driver (avg: $16.57/ea), and it
    is saturated to the point of there being fewer rides than drivers as a whole
    (.68 rides/ea).

 𝟐) Suburban city types claim 16.5% of all drivers, but produce nearly 1/3 of gross
    fare revenue (30.5%) with average fares of $30.97 each. Unlike their Urban
    counterparts, Suburban drivers can expect at least 1 ride each (1.28 rides/ea)!
    which will gross them on average $39.50 a piece.

 𝟑) Rural drivers have got it made out there in the sticks with the highest average
    of rides per driver (1.6 rides/ea), the highest fares (avg: $34.62/ea), and the
    highest grossing revenue per driver(avg: $55.49/ea)! If I were to start driving
    for Pyber, I would definitely commute to a Rural area.
'''
#*####################################################################################
# *                             Auxiliary Method Library
#*####################################################################################
# PrintWelcome displays the Pyber ASCII art, my last name, and executes Trends().


def PrintWelcome():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(color.BOLD + disgustingASCII)
    print(color.RED + color.REVERSED +
          '                                 Spaar            ' + color.END)
    print("\n")
    Trends()

# Trends is the prompt that can generate my summary of the data (3 observable trends).


def Trends():
    trendsANS = str(input(
        f" {color.BOLD}Would you like to view my 3 observable trends summary first?: {color.REVERSED}{color.RED}[y/n]{color.END} "))
    if trendsANS == "y":
        print(
            f"\n\n\n\n\n\n\n\n\n\n\n\n{color.BOLD}--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--{color.END}")
        print(trendsSummary)
        print(
            f"\n\n\n\n{color.BOLD}--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--{color.END}")
        contANS = str(input(
            f"\n\n\n {color.BOLD}Ready to continue to the 𝑷𝒚𝒃𝒆𝒓 graph generator?: {color.REVERSED}{color.RED}[y/n]{color.END} "))
        if contANS == "y":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        else:
            time.sleep(60)
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# Again is the prompt that allows the user to restart the program from within the shell.


def Again():
    print(color.BOLD + disgustingASCII)
    print(color.RED + color.REVERSED +
          '                                 Spaar            ' + color.END)
    print("\n")
    againANS = str(input(
        f"{color.BOLD} Would you like to generate new 𝑷𝒚𝒃𝒆𝒓 graphs? {color.REVERSED}{color.RED}[y/n]{color.END}: "))
    if againANS == "y":
        return "y"
    else:
        return None
#*####################################################################################
# *                             Primary Method Library
#*####################################################################################
# ChoicePrompt lists and can generate all 7 types of graphs the homework assigned.


def ChoicePrompt():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(color.BOLD + disgustingASCII)
    print(color.RED + color.REVERSED +
          '                                 Spaar            ' + color.END)
    print("\n")
    print(
        f" {color.BOLD}{color.UNDERLINE}Choices of 𝑷𝒚𝒃𝒆𝒓 Graphs to Generate{color.END}:\n\n • Urban Cities (Bubble Plot)                {color.RED}[1]{color.END}")
    print(
        f" • Suburban Cities (Bubble Plot)             {color.RED}[2]{color.END}")
    print(
        f" • Rural Cities (Bubble Plot)                {color.RED}[3]{color.END}")
    print(
        f" • All Cities Combined (Bubble Plot)         {color.RED}[4]{color.END}")
    print(
        f" • Total Fares by City Type (Pie Graph)      {color.RED}[5]{color.END}")
    print(
        f" • Total Rides by City Type (Pie Graph)      {color.RED}[6]{color.END}")
    print(
        f" • Driver Percents by City Type (Pie Graph)  {color.RED}[7]{color.END}")
    print(
        f" • {color.BOLD}{color.UNDERLINE}ALL{color.END} of the above                          {color.RED}[8]{color.END}")
    print("\n")
    ans = int(input(
        f"{color.BOLD} Input your {color.RED}[#]{color.END} {color.BOLD}Choice:{color.END} "))
    print("")
    if ans == 1:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(lineSep)
        print(color.RED + '+**********************************| ' + color.END + color.BOLD +
              '      Urban Cities (Bubble Plot)     ' + color.END + color.RED + ' |************************************+' + color.END)
        print(lineSep + "\n")
        # The new Bubble/Scatter plot is set up with a general title, axes titles, and a note
        # about the s values (larger markers) correlating to number of drivers.
        plt.title("Urban Cities (Bubble Plot)", fontweight='bold')
        plt.xlabel(
            "Total Number of Rides (Per City)", fontweight='bold')
        plt.ylabel("Average Fare ($)", fontweight='bold')
        plt.text(13.5, 30.25, 'Note:', fontsize=13,
                 fontweight='bold', color='red', style='italic')
        plt.text(
            17, 30.25, 'Circle size correlates with driver count per city.', fontsize=10)
        plt.scatter(urbanX, urbanY, facecolors="coral",
                    edgecolors="black", alpha=0.75, s=urbanS, linewidths=1)
        # A light grey grid with dashes is initialized over the plot figure.
        plt.grid(b=True, color="lightgrey", linestyle="--")
        Prompt()
    elif ans == 2:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n" + lineSep)
        print(color.RED + '+**********************************| ' + color.END + color.BOLD +
              '    Suburban Cities (Bubble Plot)    ' + color.END + color.RED + ' |************************************+' + color.END)
        print(lineSep + "\n")
        # The new Bubble/Scatter plot is set up with a general title, axes titles, and a note
        # about the s values (larger markers) correlating to number of drivers.
        plt.title("Subrban Cities (Bubble Plot)", fontweight='bold')
        plt.xlabel(
            "Total Number of Rides (Per City)", fontweight='bold')
        plt.ylabel("Average Fare ($)", fontweight='bold')
        plt.text(10.5, 38.1, 'Note:', fontsize=13,
                 fontweight='bold', color='red', style='italic')
        plt.text(
            13, 38.1, 'Circle size correlates with driver count per city.', fontsize=10)
        plt.scatter(suburbanX, suburbanY, facecolors="lightskyblue",
                    edgecolors="black", alpha=0.75, s=suburbanS, linewidths=1)
        # A light grey grid with dashes is initialized over the plot figure.
        plt.grid(b=True, color="lightgrey", linestyle="--")
        Prompt()
    elif ans == 3:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n" + lineSep)
        print(color.RED + '+**********************************| ' + color.END + color.BOLD +
              '     Rural Cities (Bubble Plot)      ' + color.END + color.RED + ' |************************************+' + color.END)
        print(lineSep + "\n")
        # The new Bubble/Scatter plot is set up with a general title, axes titles, and a note
        # about the s values (larger markers) correlating to number of drivers.
        plt.title("Rural Cities (Bubble Plot)", fontweight='bold')
        plt.xlabel(
            "Total Number of Rides (Per City)", fontweight='bold')
        plt.ylabel("Average Fare ($)", fontweight='bold')
        plt.text(3.85, 46, 'Note:', fontsize=13,
                 fontweight='bold', color='red', style='italic')
        plt.text(
            5, 46, 'Circle size correlates with driver count per city.', fontsize=10)
        plt.scatter(ruralX, ruralY, facecolors="gold",
                    edgecolors="black", alpha=0.75, s=ruralS, linewidths=1)
        # A light grey grid with dashes is initialized over the plot figure.
        plt.grid(b=True, color="lightgrey", linestyle="--")
        Prompt()
    elif ans == 4:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n" + lineSep)
        print(color.RED + '+**********************************| ' + color.END + color.BOLD +
              '  All Cities Combined (Bubble Plot)  ' + color.END + color.RED + ' |************************************+' + color.END)
        print(lineSep + "\n")
        # The new Bubble/Scatter plot is set up with a general title, axes titles, and a note
        # about the s values (larger markers) correlating to number of drivers.
        # plt.figure(figsize=(50, 42))
        plt.title("Pyber Ride Sharing Data (2016)")
        plt.xlabel("Total Number of Rides (Per City)")
        plt.ylabel("Average Fare ($)")
        plt.text(6, 46.55, 'Note:', fontsize=13,
                 fontweight='bold', color='red', style='italic')
        plt.text(
            11, 46.55, 'Circle size correlates with driver count per city.', fontsize=10)
        # The [urban] cities' data is plotted.
        plt.scatter(urbanX, urbanY, facecolors="coral",
                    edgecolors="black", alpha=0.75, s=urbanS, linewidths=1, label="Urban")
        # The [suburban] cities' data is plotted.
        plt.scatter(suburbanX, suburbanY, facecolors="lightskyblue",
                    edgecolors="black", alpha=0.75, s=suburbanS, linewidths=1, label="Suburban")
        # The [rural] cities' data is plotted.
        plt.scatter(ruralX, ruralY, facecolors="gold",
                    edgecolors="black", alpha=0.75, s=ruralS, linewidths=1, label="Rural")
        # A legend is created in the "best" location of the plot figure.
        plt.legend(loc="best", fontsize="small", fancybox=True,
                   title="Types of Cities", shadow=True, framealpha=.95, labelspacing=1.5)
        # A light grey grid with dashes is initialized over the plot figure.
        plt.grid(b=True, color="lightgrey", linestyle="--")
        Prompt()
    elif ans == 5:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n" + lineSep)
        print(color.RED + '+********************************| ' + color.END + color.BOLD +
              '  Total Fares by City Type (Pie Graph)  ' + color.END + color.RED + ' |***********************************+' + color.END)
        print(lineSep + "\n")
        # The new Pie graph is set up with a general title, pie "slice" titles, and use the
        # previously define specifications for Explode and Colors. It also has a shadow
        # enabled, its starting angle set to 40º, and rounds the percentages off.
        plt.title("% of Total Fares by City Type")
        plt.pie(pieCityData_Fares, explode=explode, labels=pieCityTypes,
                colors=colors, autopct="%1.1f%%", shadow=True, startangle=240)
        plt.axis("equal")
        Prompt()
    elif ans == 6:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n" + lineSep)
        print(color.RED + '+********************************| ' + color.END + color.BOLD +
              '  Total Rides by City Type (Pie Graph)  ' + color.END + color.RED + ' |***********************************+' + color.END)
        print(lineSep + "\n")
        # The new Pie graph is set up with a general title, pie "slice" titles, and use the
        # previously define specifications for Explode and Colors. It also has a shadow
        # enabled, its starting angle set to 40º, and rounds the percentages off.
        plt.title("% of Total Rides by City Type")
        plt.pie(pieCityData_Rides, explode=explode, labels=pieCityTypes,
                colors=colors, autopct="%1.1f%%", shadow=True, startangle=240)
        plt.axis("equal")
        Prompt()
    elif ans == 7:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n" + lineSep)
        print(color.RED + '+*******************************| ' + color.END + color.BOLD +
              '  Driver Percents by City Type (Pie Graph)  ' + color.END + color.RED + ' |********************************+' + color.END)
        print(lineSep + "\n")
        # The new Pie graph is set up with a general title, pie "slice" titles, and use the
        # previously define specifications for Explode and Colors. It also has a shadow
        # enabled, its starting angle set to 40º, and rounds the percentages off.
        plt.title("% of Total Drivers by City Type")
        plt.pie(pieCityData_Drivers, explode=explode, labels=pieCityTypes,
                colors=colors, autopct="%1.1f%%", shadow=True, startangle=240)
        plt.axis("equal")
        Prompt()
    elif ans == 8:
        # All of the ^above^ 7 options are executed.
        # *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* Graph 1
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(lineSep)
        print(color.RED + '+**********************************| ' + color.END + color.BOLD +
              '      Urban Cities (Bubble Plot)     ' + color.END + color.RED + ' |************************************+' + color.END)
        print(lineSep + "\n")
        plt.title("Urban Cities (Bubble Plot)", fontweight='bold')
        plt.xlabel(
            "Total Number of Rides (Per City)", fontweight='bold')
        plt.ylabel("Average Fare ($)", fontweight='bold')
        plt.text(13.5, 30.25, 'Note:', fontsize=13,
                 fontweight='bold', color='red', style='italic')
        plt.text(
            17, 30.25, 'Circle size correlates with driver count per city.', fontsize=10)
        plt.scatter(urbanX, urbanY, facecolors="coral",
                    edgecolors="black", alpha=0.75, s=urbanS, linewidths=1)
        plt.grid(b=True, color="lightgrey", linestyle="--")
        Prompt()
        # *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* Graph 2
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n")
        print("\n" + lineSep)
        print(color.RED + '+**********************************| ' + color.END + color.BOLD +
              '    Suburban Cities (Bubble Plot)    ' + color.END + color.RED + ' |************************************+' + color.END)
        print(lineSep + "\n")
        plt.title("Subrban Cities (Bubble Plot)", fontweight='bold')
        plt.xlabel(
            "Total Number of Rides (Per City)", fontweight='bold')
        plt.ylabel("Average Fare ($)", fontweight='bold')
        plt.text(10.5, 38.1, 'Note:', fontsize=13,
                 fontweight='bold', color='red', style='italic')
        plt.text(
            13, 38.1, 'Circle size correlates with driver count per city.', fontsize=10)
        plt.scatter(suburbanX, suburbanY, facecolors="lightskyblue",
                    edgecolors="black", alpha=0.75, s=suburbanS, linewidths=1)
        plt.grid(b=True, color="lightgrey", linestyle="--")
        Prompt()
        # *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* Graph 3
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n")
        print("\n" + lineSep)
        print(color.RED + '+**********************************| ' + color.END + color.BOLD +
              '     Rural Cities (Bubble Plot)      ' + color.END + color.RED + ' |************************************+' + color.END)
        print(lineSep + "\n")
        plt.title("Rural Cities (Bubble Plot)", fontweight='bold')
        plt.xlabel(
            "Total Number of Rides (Per City)", fontweight='bold')
        plt.ylabel("Average Fare ($)", fontweight='bold')
        plt.text(3.85, 46, 'Note:', fontsize=13,
                 fontweight='bold', color='red', style='italic')
        plt.text(
            5, 46, 'Circle size correlates with driver count per city.', fontsize=10)
        plt.scatter(ruralX, ruralY, facecolors="gold",
                    edgecolors="black", alpha=0.75, s=ruralS, linewidths=1)
        plt.grid(b=True, color="lightgrey", linestyle="--")
        Prompt()
        # *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* Graph 4
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n")
        print("\n" + lineSep)
        print(color.RED + '+**********************************| ' + color.END + color.BOLD +
              '  All Cities Combined (Bubble Plot)  ' + color.END + color.RED + ' |************************************+' + color.END)
        print(lineSep + "\n")
        plt.title("Pyber Ride Sharing Data (2016)")
        plt.xlabel("Total Number of Rides (Per City)")
        plt.ylabel("Average Fare ($)")
        plt.text(6, 46.55, 'Note:', fontsize=13,
                 fontweight='bold', color='red', style='italic')
        plt.text(
            11, 46.55, 'Circle size correlates with driver count per city.', fontsize=10)
        # The [urban] cities' data is plotted.
        plt.scatter(urbanX, urbanY, facecolors="coral",
                    edgecolors="black", alpha=0.75, s=urbanS, linewidths=1, label="Urban")
        # The [suburban] cities' data is plotted.
        plt.scatter(suburbanX, suburbanY, facecolors="lightskyblue",
                    edgecolors="black", alpha=0.75, s=suburbanS, linewidths=1, label="Suburban")
        # The [rural] cities' data is plotted.
        plt.scatter(ruralX, ruralY, facecolors="gold",
                    edgecolors="black", alpha=0.75, s=ruralS, linewidths=1, label="Rural")
        # A legend is created in the "best" location of the plot figure.
        plt.legend(loc="best", fontsize="small", fancybox=True,
                   title="Types of Cities", shadow=True, framealpha=.95, labelspacing=1.5)
        # A light grey grid with dashes is initialized over the plot figure.
        plt.grid(b=True, color="lightgrey", linestyle="--")
        # The plot is displayed to the user.
        Prompt()
        # *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* Graph 5
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n")
        print("\n" + lineSep)
        print(color.RED + '+********************************| ' + color.END + color.BOLD +
              '  Total Fares by City Type (Pie Graph)  ' + color.END + color.RED + ' |***********************************+' + color.END)
        print(lineSep + "\n")
        plt.title("% of Total Fares by City Type")
        plt.pie(pieCityData_Fares, explode=explode, labels=pieCityTypes,
                colors=colors, autopct="%1.1f%%", shadow=True, startangle=40)
        plt.axis("equal")
        Prompt()
        # *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* Graph 6
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n")
        print("\n" + lineSep)
        print(color.RED + '+********************************| ' + color.END + color.BOLD +
              '  Total Rides by City Type (Pie Graph)  ' + color.END + color.RED + ' |***********************************+' + color.END)
        print(lineSep + "\n")
        plt.title("% of Total Rides by City Type")
        plt.pie(pieCityData_Rides, explode=explode, labels=pieCityTypes,
                colors=colors, autopct="%1.1f%%", shadow=True, startangle=40)
        plt.axis("equal")
        Prompt()
        # *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#* Graph 7
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n")
        print("\n" + lineSep)
        print(color.RED + '+*******************************| ' + color.END + color.BOLD +
              '  Driver Percents by City Type (Pie Graph)  ' + color.END + color.RED + ' |********************************+' + color.END)
        print(lineSep + "\n")
        plt.title("% of Total Drivers by City Type")
        plt.pie(pieCityData_Drivers, explode=explode, labels=pieCityTypes,
                colors=colors, autopct="%1.1f%%", shadow=True, startangle=40)
        plt.axis("equal")
        Prompt()
        print("\n\n")
# Prompt enables the user to view and/or save the graph generated to their local disk.
# If a file already exists with the same name and location, the user is prompted to
# either overwrite, or discard the graph.


def Prompt():
    saveANS = str(input(
        f" {color.BOLD}{color.UNDERLINE}Choices of Operation{color.END}:\n\n • Save Graph to Local  {color.RED}[s]{color.END}\n • View Graph           {color.RED}[v]{color.END}\n • {color.BOLD}{color.UNDERLINE}Both{color.END}                 {color.RED}[b]{color.END} \n ↓ Skip                 {color.RED}[x]{color.END}\n\n{color.BOLD} Input your {color.RED}[#]{color.END} {color.BOLD}Choice:{color.END} "))
    if saveANS == "s":
        fileName = str(input("\n Please entitle your graph: ") + ".png")
        outputLoc = str(
            input(" Please enter your absolute path to save it to: "))
        fullPath = os.path.join(outputLoc, fileName)
        if os.path.exists(fullPath):
            ansOR = str(input(
                f"\n [!] File: {color.BOLD}{color.UNDERLINE}{fileName}{color.END} already exists at: {color.BOLD}{color.UNDERLINE}{outputLoc}{color.END} [!]\n -----------------------------------------------------{color.BOLD}Overwrite?{color.END} {color.RED}{color.BOLD}{color.REVERSED}[y/n]{color.END} "))
            if ansOR == "y":
                plt.savefig(fullPath)
                print(
                    f"\n Graph {color.BOLD}{fileName}{color.END} overwritten to {color.BOLD}{fullPath}{color.END}")
                time.sleep(1)
                plt.clf()
            else:
                plt.clf()
        else:
            plt.savefig(fullPath)
            print(
                f"\n Graph {color.BOLD}{fileName}{color.END} saved to {color.BOLD}{fullPath}{color.END}")
            time.sleep(1)
            plt.clf()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    elif saveANS == "v":
        print("\n Loading Graph..")
        time.sleep(1)
        plt.show()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    elif saveANS == "b":
        fileName = str(input("\n Please entitle your graph: ") + ".png")
        outputLoc = str(
            input(" Please enter your absolute path to save it to: "))
        fullPath = os.path.join(outputLoc, fileName)
        if os.path.exists(fullPath):
            ansOR = str(input(
                f"\n [!] File: {color.BOLD}{color.UNDERLINE}{fileName}{color.END} already exists at: {color.BOLD}{color.UNDERLINE}{outputLoc}{color.END} [!]\n -----------------------------------------------------{color.BOLD}Overwrite?{color.END} {color.REVERSED}{color.RED}{color.BOLD}[y/n]{color.END} "))
            if ansOR == "y":
                plt.savefig(fullPath)
                print(
                    f"\n Graph {color.BOLD}{fileName}{color.END} overwritten to {color.BOLD}{fullPath}{color.END}")
                time.sleep(1)
            else:
                print("")
        else:
            plt.savefig(fullPath)
            print(
                f"\n Graph {color.BOLD}{fileName}{color.END} saved to {color.BOLD}{fullPath}{color.END}")
        print("\n Loading Graph..")
        time.sleep(1)
        plt.show()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    elif saveANS == "x":
        plt.clf()
        print("\n Skipping..")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


#*####################################################################################
# *                                     Main
#*####################################################################################
PrintWelcome()
while Again() == "y":
    ChoicePrompt()
