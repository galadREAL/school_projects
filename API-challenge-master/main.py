#!/usr/bin/env python
# coding: utf-8
#*####################################################################################
# *                                  Dependencies
#*####################################################################################
from subprocess import call
from citipy import citipy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pprint import pprint
from pandas.io.json import json_normalize
from tqdm import tqdm
import requests, time, json, csv, getpass, sys, os
#*####################################################################################
# *                             CLI-esque Finesse
#*####################################################################################

# ANSI colors for pretty terminal formatting are declared.
class color:
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    PURPLE = '\033[35m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    REVERSED = '\u001b[7m'
    BLINK = '\033[5m'

# A multicolored line seperator is established.
lineSep = str(color.PURPLE + '◈' + color.END + '--<>--<>--<>--<>--<>--<>--<>--<>' + color.PURPLE +
              '---------------------------------------' + color.END + '<>--<>--<>--<>--<>--<>--<>--<>--' + color.PURPLE + '◈' + color.END)

# "WeatherPy" ASCII art is established.
disgustingASCII = '''
              .

              |
     .               /
      \       I
                  /
        \  ,g88R_
          d888(`  ).                   _
 -  --==  888(     ).=--           .+(`  )`.
)         Y8P(       '`.          :(   .    )
        .+(`(      .   )     .--  `.  (    ) )
       ((    (..__.:'-'   .=(   )   ` _`  ) )
`.     `(       ) )       (   .  )     (   )  ._
  )      ` __.:'   )     (   (   ))     `-'.:(`  )
)  )  ( )       --'       `- __.'         :(      ))
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'

                          ╦ ╦┌─┐┌─┐┌┬┐┬ ┬┌─┐┬─┐╔═╗╦ ╦
                          ║║║├┤ ├─┤ │ ├─┤├┤ ├┬┘╠═╝╚╦╝
                          ╚╩╝└─┘┴ ┴ ┴ ┴ ┴└─┘┴└─╩   ╩
--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.
'''

# 3 observable trends report is established.
trendsSummary = '''

         𝟏) As expected, the weather becomes significantly warmer as one approaches the
            equator(0 Deg. Latitude). More interestingly, however, is the fact that the
            southern hemisphere tends to be warmer this time of year than the northern
            hemisphere. This may be due to the tilt of the earth.

         𝟐) There is no strong relationship between latitude and cloudiness. However, it
            is interesting to see that a strong band of cities sits at 0, 80, and 100%
            cloudiness.

         𝟑) There is no strong relationship between latitude and wind speed. However, in
            northern hemispheres there is a flurry of cities with over 20 mph of wind.

'''


# All 5 options' headers are declared as vars or ease of use.
Header1 = str(lineSep + "\n" + color.PURPLE + color.BOLD + '                                          Latitude vs. Temperature ' + color.END + "\n" + lineSep + "\n")

Header2 = str(lineSep + "\n" + color.PURPLE + color.BOLD +
              '                                         Latitude vs. Humidity ' + color.END + "\n" + lineSep + "\n")

Header3 = str(lineSep + "\n" + color.PURPLE + color.BOLD +
              '                                          Latitude vs. Cloudiness ' + color.END + "\n" + lineSep + "\n")

Header4 = str(lineSep + "\n" + color.PURPLE + color.BOLD +
              '                                          Latitude vs. Windspeed ' + color.END + "\n" + lineSep + "\n")

Header6 = str(lineSep + "\n" + color.PURPLE + color.BOLD +
              '                                          Output all data to .csv ' + color.END + "\n" + lineSep + "\n")

HeaderTrends = str(lineSep + "\n\n" + '                                   ' + color.BOLD + color.UNDERLINE + '𝕆 𝕓 𝕤 𝕖 𝕣 𝕧 𝕒 𝕓 𝕝 𝕖   𝕋 𝕣 𝕖 𝕟 𝕕 𝕤 :' + color.END)


# OutputMenu stores all of the graph/csv generation options.
def OutputMenu():
    print(
        f" {color.BOLD}{color.UNDERLINE}Choices of 𝚆𝚎𝚊𝚝𝚑𝚎𝚛𝙿𝚢 Graphs to Generate{color.END}:\n\n ◉ Latitude vs. Temperature {color.PURPLE}[1]{color.END}")
    print(
        f" ◉ Latitude vs. Humidity    {color.PURPLE}[2]{color.END}")
    print(
        f" ◉ Latitude vs. Cloudiness  {color.PURPLE}[3]{color.END}")
    print(
        f" ◉ Latitude vs. Wind Speed  {color.PURPLE}[4]{color.END}")
    print(
        f" ◉ {color.BOLD}{color.UNDERLINE}ALL{color.END} of the above         {color.PURPLE}[5]{color.END}")
    print(
        f"\n ◉ Output all data to .csv  {color.PURPLE}[6]{color.END}")
    print("\n")
#*####################################################################################
# *                             Auxiliary Method Library
#*####################################################################################
# SpaarBar is the reverse colored horizontal bar with "Spaar" written in it.
def SpaarBar():
    print(color.PURPLE + color.REVERSED +
          '                                      Spaar            ' + color.END)

# PrintWelcome displays the WeatherPy ASCII art, SpaarBar, and executes Trends().
def PrintWelcome():
    clear()
    print(color.BOLD + disgustingASCII)
    SpaarBar()
    print("\n")
    Trends()

# PrintAgain resets the shell with only the WeatherPy ASCII art and the SpaarBar.
def PrintAgain():
    clear()
    print(color.BOLD + disgustingASCII)
    SpaarBar()
    print("\n")

def PrintCombo(Header):
    PrintAgain()
    print(Header)

# The warning given to a user when they input an invalid option.
def PrintElse():
    print(
        f" {color.RED}{color.BLINK}[!]{color.END} You must enter {color.BOLD}y{color.END} or {color.BOLD}n{color.END} to continue {color.RED}{color.BLINK}[!]{color.END} \n")
    time.sleep(4)


# Trends is the prompt that can generate my summary of the data (3 observable trends).
def Trends():
    trendsANS = None
    while trendsANS not in ("y", "n"):
        trendsANS = str(input(
            f" Would you like to view the 3 observable trends' summary first?: {color.REVERSED}{color.PURPLE}[y/n]{color.END} "))
        if trendsANS == "y":
            PrintAgain()
            print(HeaderTrends)
            print(trendsSummary)
            print(lineSep)
            contANS = None
            while contANS not in ("y", "n"):
                contANS = str(input(
                    f"\n Finished with the trends' summary?: {color.REVERSED}{color.PURPLE}[y/n]{color.END} "))
                if contANS == "y":
                    continue
                elif contANS == "n":
                    print("\n You've got 20 seconds...")
                    time.sleep(20)
                else:
                    PrintAgain()
                    PrintElse()
                    PrintAgain()
                    print(lineSep)
                    print(
                        f"\n                                   {color.BOLD}{color.UNDERLINE}𝕆 𝕓 𝕤 𝕖 𝕣 𝕧 𝕒 𝕓 𝕝 𝕖   𝕋 𝕣 𝕖 𝕟 𝕕 𝕤 :{color.END}")
                    print(trendsSummary)
                    print(lineSep)
            PrintAgain()
        elif trendsANS == "n":
            PrintAgain()
        else:
            PrintAgain()
            PrintElse()
            PrintAgain()

# clear clears the user's shell.
def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

#*####################################################################################
# *                      Primary Method Library: Data Retrieval
#*####################################################################################
# Execute calls Open Weather Maps' API every 1.01 seconds until all 500 of our unique
# and random cities' data have been fetched. The user can select verbose mode optionally.
def Execute(key, city_url, cities):
    execANS = None
    while execANS not in ("y", "n"):
        execANS = str(input(
            f" Execute the {len(cities)} enqueued API calls? {color.REVERSED}{color.PURPLE}[y/n]{color.END}: "))
        if execANS == "y":
            PrintAgain()
            echoANS = None
            while echoANS not in ("y", "n"):
                echoANS = str(input(
                    f" Would you like to see each call printed to the terminal (Enable verbose)? {color.REVERSED}{color.PURPLE}[y/n]{color.END}: "))
                if echoANS == "y":
                    PrintAgain()
                    print(" Calling Open Weather Maps' API...\n")
                    citiesCapped = CapCities(cities)
                    response_json = []
                    allCapped = len(citiesCapped)
                    for x in tqdm(range(len(citiesCapped))):
                        print(
                            f" ◉ Making request number: {color.BOLD}{color.PURPLE}{x+1}{color.END}/{allCapped} (City: {color.BOLD}{color.PURPLE}{citiesCapped[x]}{color.END})")
                        post_response = requests.get(
                            city_url + str(citiesCapped[x]) + key)
                        response_json.append(post_response.json())
                        time.sleep(1.01)
                    allPosts = len(response_json)
                    os.system('say "skeet skeet"')
                    return response_json, allCapped, allPosts
                elif echoANS == "n":
                    PrintAgain()
                    print(" Calling Open Weather Maps' API...\n")
                    citiesCapped = CapCities(cities)
                    response_json = []
                    allCapped = len(citiesCapped)
                    for x in tqdm(range(len(citiesCapped))):
                        post_response = requests.get(
                            city_url + str(citiesCapped[x]) + key)
                        response_json.append(post_response.json())
                        time.sleep(1.01)
                    allPosts = len(response_json)
                    os.system('say "skeet skeet"')
                    return response_json, allCapped, allPosts
                else:
                    PrintAgain()
                    PrintElse()
                    PrintAgain()
        elif execANS == "n":
            PrintAgain()
            print(" Exiting...")
            time.sleep(2)
            sys.exit()
        else:
            PrintAgain()
            PrintElse()
            PrintAgain()



# NewData is an initial prompt that asks the user to generate new cities + data,
# or use the most recent query's cache.
def NewData():
    PrintAgain()
    apiANS = None
    while apiANS not in ("y", "n"):
        apiANS = str(input(
            f" Would you like to generate {color.BOLD}{color.UNDERLINE}NEW{color.END} cities' data? (Enter {color.BOLD}n{color.END} to use cached data): {color.REVERSED}{color.PURPLE}[y/n]{color.END} "))
        if apiANS == "y":
            return "y"
            PrintAgain()
        elif apiANS == "n":
            return "n"
            PrintAgain()
        else:
            PrintAgain()
            PrintElse()
            PrintAgain()

# GetCreds obtains the user's API key and checks the validity.
def GetCreds():
    PrintAgain()
    keybase = "&APPID="
    secretkey = getpass.getpass(
        prompt=str(' Enter your Open Weather Maps' + color.BOLD + ' [Current Weather Data] ' + color.END + 'API key: '))
    key = keybase + secretkey
    city_url = "https://api.openweathermap.org/data/2.5/weather?q="
    conn = requests.get(city_url + key).json()
    conn = str(conn)
    conn = conn.split()
    conn = str(conn[1])
    if conn != "'400',":
        PrintAgain()
        print(
            f" {color.RED}{color.BLINK}[!]{color.END} {color.BOLD}{color.RED}Failed connection{color.END}: Ensure your API key is correct {color.RED}{color.BLINK}[!]{color.END} ")
        time.sleep(3)
        PrintAgain()
        print( f" If you don't have an API key, you can get it here: {color.BOLD}{color.UNDERLINE}home.openweathermap.org/users/sign_up{color.END}" )
        time.sleep(10)
        sys.exit()
    else:
        PrintAgain()
        print(f" {color.GREEN}Connection successfully established...{color.END}")
        time.sleep(2)
        PrintAgain()
        return key, city_url

# GetPostsRate checks to see if all calls were successful or not, and prints the findings.


def GetPostsRate(allCapped, allPosts):
    PrintAgain()
    if float(allCapped) == float(allPosts):
        print(
            f" {color.GREEN}{color.BOLD}100% success rate{color.END}, all posts received!")
        time.sleep(2)
    else:
        pctPosts = (float(allCapped) / float(allPosts) * 100)
        pctPosts = np.round(pctPosts, decimals=2)
        print(
            f" {color.RED}{color.BLINK}[!]{color.END} {color.BOLD}{pctPosts}%{color.END} success rate: {allPosts}/{allCapped} posts recevied {color.RED}{color.BLINK}[!]{color.END} ")
        time.sleep(2)

#*####################################################################################
# *                      Primary Method Library: Data Munging
#*####################################################################################
# RawJSONintoDF coverts the response json data into a DF. Along the way it deletes all
# irrelevant columns for this assignment, adds polished figures/naming, and adds in
# columns for the farenheit temperature as well as the wind speed in miles per hour.


def RawJSONintoDF(response_json):
    PrintAgain()
    print(" Converting and caching all received raw data into Pandas...")
    time.sleep(2)
    PrintAgain()
    with open('raw.json', 'w') as f:
        json.dump(response_json, f, ensure_ascii=False)
    with open('raw.json') as data_file:
        data = json.load(data_file)
    rawDF = json_normalize(data)
    unwantedCols = ['base',
                    'cod',
                    'main.grnd_level',
                    'main.pressure',
                    'main.sea_level',
                    'main.temp',
                    'main.temp_min',
                    'message',
                    'sys.message',
                    'sys.sunrise',
                    'sys.sunset',
                    'sys.type',
                    'visibility',
                    'wind.deg',
                    'wind.gust',
                    'id',
                    'rain.1h',
                    'rain.3h',
                    'sys.id',
                    'weather',
                    'snow.1h',
                    'snow.3h']
    for col in unwantedCols:
        try:
            rawDF = rawDF.drop([f'{col}'], axis=1)
        except KeyError:
            continue
    rawDF = rawDF.dropna()
    rawDF = rawDF.rename(columns={"clouds.all": "% Cloudiness",
                                  "coord.lat": "Latitude",
                                  "coord.lon": "Longitude",
                                  "dt": "Date (Raw)",
                                  "main.humidity": "% Humidity",
                                  "main.temp_max": "Max. Temp. (K)",
                                  "name": "City",
                                  "sys.country": "Country",
                                  "wind.speed": "Wind Speed (M/s)"})
    DatesDF = DateConv(rawDF)
    rawDF.insert(7, "Date (Polished)", DatesDF)
    FarenConversions = TempConv(rawDF)
    rawDF.insert(6, "Max. Temp. (F)", FarenConversions)
    MPHconvs = WindConv(rawDF)
    rawDF.insert(10, "Wind Speed (MPH)", MPHconvs)
    relDate = RelativeDateConv(rawDF)
    print(" All data converted to Pandas successfully...")
    time.sleep(2)
    rawDF.to_csv("temp_data/cached_city_data.csv", index=False)
    PrintAgain()
    return rawDF, relDate, FarenConversions

# LoadExisting loads the cached data last retrieved for use in graph/csv generation.
def LoadExisting():
    if os.path.exists("temp_data/cached_city_data.csv"):
        rawDF = pd.read_csv("temp_data/cached_city_data.csv")
        relDate = RelativeDateConv(rawDF)
        #todo Why doesn't this work? Is MPHConvs also affected?
        #FarenConversions = rawDF['Max. Temp. (F)']
        FarenConversions = TempConv(rawDF)
        return rawDF, relDate, FarenConversions
    else:
        print(
            f" \n {color.RED}{color.BLINK}[!]{color.END} {color.BOLD}{color.RED}No cached data found{color.END}: You must generate new data {color.RED}{color.BLINK}[!]{color.END} ")
        time.sleep(4)
        sys.exit()

# LoadData stages data for graph/csv generation.
def LoadData(newAns):
    if newANS == "y":
        key, city_url = GetCreds()
        cities = GenerateCities()
        response_json, allCapped, allPosts = Execute(key, city_url, cities)
        GetPostsRate(allCapped, allPosts)
        rawDF, relDate, FarenConversions = RawJSONintoDF(response_json)
        return rawDF, relDate, FarenConversions
    elif newANS == "n":
        rawDF, relDate, FarenConversions = LoadExisting()
        return rawDF, relDate, FarenConversions
#*####################################################################################
# *                      Primary Method Library: Data Conversions
#*####################################################################################
# GenerateCities generates 500 random cities to be called from OWM's API.
def GenerateCities():
    # Range of latitudes and longitudes.
    lat_range = (-90, 90)
    lng_range = (-180, 180)
    # Lists for holding lat_lngs and cities.
    lat_lngs, cities = [], []
    # Create a set of random lat and lng combinations.
    lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
    lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
    lat_lngs = zip(lats, lngs)
    # Identify nearest city for each lat, lng combination.
    for lat_lng in lat_lngs:
        city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
        # If the city is unique, then add it to a our cities list.
        if city not in cities and len(cities) < 500:
            cities.append(city)
        if len(cities) == 500:
            break
    return cities

# KtoF converts a series of Kelvin temperatures into Farenheit.


def KtoF(series):
    FarenConversions = []
    for kelvin in series:
        k = float(kelvin)
        c = k + 273
        f = ((9 * c) / 5) + 32
        FarenConversions.append(f)
    return FarenConversions
# MPStoMPH converts a series of Metres/second speeds into Miles/hour.


def MPStoMPH(series):
    MPHconvs = []
    for mps in series:
        metric = float(mps)
        imp = metric * 2.23694
        MPHconvs.append(imp)
    return MPHconvs

# CapCities capitalizes all of the generated city names.
def CapCities(cities):
    citiesCapped = []
    for city in cities:
        city = city.title()
        citiesCapped.append(city)
    return citiesCapped

# DateConv converts Unix time to a humanized form.
#todo optimize these
def DateConv(rawDF):
    DatesDF = pd.Series(rawDF['Date (Raw)'])
    DatesDF = pd.to_numeric(DatesDF.iloc[:])
    DatesDF = pd.DataFrame(DatesDF)
    DatesDF = pd.to_datetime(DatesDF['Date (Raw)'], unit='s')
    return DatesDF

# TempConv converts the Kelvin temps to Farenheit.
def TempConv(rawDF):
    FarenConversions = KtoF(rawDF['Max. Temp. (K)'])
    FarenConversions = np.round(FarenConversions, decimals=2)
    FarenConversions = pd.Series(FarenConversions)
    return FarenConversions

# WindConv converts the wind speed of M/s to MPH.
def WindConv(rawDF):
    MPHconvs = MPStoMPH(rawDF['Wind Speed (M/s)'])
    MPHconvs = np.round(MPHconvs, decimals=2)
    MPHconvs = pd.Series(MPHconvs)
    return MPHconvs

# RelativeDateConv returns the date of the data's readings
def RelativeDateConv(rawDF):
    relDate = rawDF.iloc[1, 8]
    relDate = str(relDate).split(" ", 1)
    return relDate

# HumidityConv excludes any glitched +100% humidity readings.
def HumidityConv(rawDF):
    humiditiesS = pd.to_numeric(rawDF['% Humidity'])
    humidityPlotData = []
    for each in humiditiesS:
            if each <= 100:
                humidityPlotData.append(each)
    return humidityPlotData

# CloudsConv excludes any glitched +100% cloudiness readings.
def CloudsConv(rawDF):
    cloudsS = pd.to_numeric(rawDF['% Cloudiness'])
    cloudsPlotData = []
    for each in cloudsS:
            if each <= 100:
                cloudsPlotData.append(each)
    return cloudsPlotData
#*####################################################################################
# *                      Primary Method Library: Data Output
#*####################################################################################
# Again allows for repeated graph generation within the same shell for the user.

def Again():
    PrintAgain()
    againANS = None
    while againANS not in ("y", "n"):
        againANS = str(input(
            f" Ready to generate new 𝚆𝚎𝚊𝚝𝚑𝚎𝚛𝙿𝚢 graphs? {color.REVERSED}{color.PURPLE}[y/n]{color.END}: "))
        if againANS == "y":
            return "y"
        elif againANS == "n":
            PrintAgain()
            print(" Exiting...")
            time.sleep(2)
            sys.exit()
        else:
            PrintAgain()
            PrintElse()
            PrintAgain()




# Prompt enables the user to view and/or save the graph generated to their local disk.
# If a file already exists with the same name and location, the user is prompted to
# either overwrite, or discard the graph. Skipping is also enabled.

def Prompt(Header):
    PrintCombo(Header)
    saveANS = None
    while saveANS not in ("s", "v", "b", "x"):
        saveANS = str(input(
            f" {color.BOLD}{color.UNDERLINE}Choices of Operation{color.END}:\n\n ◉ Save Graph to Local  {color.PURPLE}[s]{color.END}\n ◉ View Graph           {color.PURPLE}[v]{color.END}\n ◉ {color.BOLD}{color.UNDERLINE}Both{color.END}                 {color.PURPLE}[b]{color.END} \n\n ↓ Skip                 {color.PURPLE}[x]{color.END}\n\n\n Input your {color.PURPLE}[#]{color.END} Choice: "))
        PrintCombo(Header)
        if saveANS == "s":
            fileName = str(input(" Please entitle your graph: ") + ".png")
            PrintCombo(Header)
            outputLoc = str(
                input(" Please enter your desired absolute path to save it to: "))
            PrintCombo(Header)
            fullPath = os.path.join(outputLoc, fileName)
            if os.path.exists(fullPath):
                ansOR = None
                while ansOR not in ("y", "n"):
                    ansOR = str(input(
                        f" {color.RED}{color.BLINK}[!]{color.END} File: {color.BOLD}{color.UNDERLINE}{fileName}{color.END} already exists at: {color.BOLD}{color.UNDERLINE}{outputLoc}{color.END} {color.RED}{color.BLINK}[!]{color.END}\n\n Overwrite? {color.PURPLE}{color.BOLD}{color.REVERSED}[y/n]{color.END} "))
                    PrintCombo(Header)
                    if ansOR == "y":
                        plt.savefig(fullPath)
                        print(
                            f" Graph {color.BOLD}{fileName}{color.END} overwritten to {color.BOLD}{fullPath}{color.END}" )
                        time.sleep(2)
                        plt.clf()
                        PrintCombo(Header)
                    elif ansOR == "n":
                        print(" Continuing without overwriting...")
                        time.sleep(2)
                        plt.clf()
                        PrintCombo(Header)
                    else:
                        PrintElse()
                        PrintCombo(Header)
            else:
                plt.savefig(fullPath)
                print(
                    f" Graph {color.BOLD}{fileName}{color.END} saved to {color.BOLD}{fullPath}{color.END}" )
                time.sleep(2)
                plt.clf()
                PrintCombo(Header)
        elif saveANS == "v":
            print(" Loading Graph...")
            plt.show()
        elif saveANS == "b":
            fileName = str(input(" Please entitle your graph: ") + ".png")
            PrintCombo(Header)
            outputLoc = str(
                input(" Please enter your absolute path to save it to: "))
            fullPath = os.path.join(outputLoc, fileName)
            PrintCombo(Header)
            if os.path.exists(fullPath):
                ansOR = None
                while ansOR not in ("y", "n"):
                    ansOR = str(input(
                        f" {color.RED}{color.BLINK}[!]{color.END} File: {color.BOLD}{color.UNDERLINE}{fileName}{color.END} already exists at: {color.BOLD}{color.UNDERLINE}{outputLoc}{color.END} {color.RED}{color.BLINK}[!]{color.END}\n\n Overwrite? {color.PURPLE}{color.BOLD}{color.REVERSED}[y/n]{color.END} "))
                    PrintCombo(Header)
                    if ansOR == "y":
                        plt.savefig(fullPath)
                        print(
                            f" Graph {color.BOLD}{fileName}{color.END} overwritten to {color.BOLD}{fullPath}{color.END}" )
                        time.sleep(2)
                        PrintCombo(Header)
                    elif ansOR == "n":
                        print(" Continuing without overwriting...")
                        time.sleep(2)
                        PrintCombo(Header)
                    else:
                        PrintElse()
                        PrintCombo(Header)
            else:
                plt.savefig(fullPath)
                print(
                    f" Graph {color.BOLD}{fileName}{color.END} saved to {color.BOLD}{fullPath}{color.END}" )
                time.sleep(2)
                PrintCombo(Header)
            print(" Loading Graph...")
            plt.show()
        elif saveANS == "x":
            plt.clf()
            print(" Skipping...")
            time.sleep(2)
        else:
            plt.clf()
            PrintElse()
            PrintCombo(Header)
# ChoicePrompt can generate and save all 4 graphs assigned by the homework.
# It also can output your dataframes as .csv files.


def ChoicePrompt(rawDF, relDate, FarenConversions):
    OutputMenu()
    ans = None
    while ans not in ("1", "2", "3", "4", "5", "6"):
        ans = input(
            f" Input your {color.PURPLE}[#]{color.END} choice: ")
        #PrintAgain()
        if ans == "1":
            PrintCombo(Header1)
            plot1_x = rawDF['Latitude']
            plot1_y = FarenConversions
            plt.title(
                f"City Latitude vs. Max Temperature (~{relDate[0]})", fontweight='bold')
            plt.xlabel("Latitude", fontweight='bold')
            plt.ylabel("Max Temperature (F)", fontweight='bold')
            plt.scatter(plot1_x, plot1_y, facecolors="turquoise",
                        edgecolors="black", alpha=0.75, linewidths=1)
            plt.grid(b=True, color="lightgrey", linestyle="--")
            Prompt(Header1)
        elif ans == "2":
            PrintCombo(Header2)
            plot2_x = rawDF['Latitude']
            humidityPlotData = HumidityConv(rawDF)
            plot2_y = humidityPlotData
            plt.title(
                f"City Latitude vs. Humidity (~{relDate[0]})", fontweight='bold')
            plt.xlabel("Latitude", fontweight='bold')
            plt.ylabel("Humidity (%)", fontweight='bold')
            plt.scatter(plot2_x, plot2_y, facecolors="blue",
                        edgecolors="black", alpha=0.75, linewidths=1)
            plt.grid(b=True, color="lightgrey", linestyle="--")
            Prompt(Header2)
        elif ans == "3":
            PrintCombo(Header3)
            plot3_x = rawDF['Latitude']
            cloudsPlotData = CloudsConv(rawDF)
            plot3_y = cloudsPlotData
            plt.title(
                f"City Latitude vs. Cloudiness (~{relDate[0]})", fontweight='bold')
            plt.xlabel("Latitude", fontweight='bold')
            plt.ylabel("Cloudiness (%)", fontweight='bold')
            plt.scatter(plot3_x, plot3_y, facecolors="coral",
                        edgecolors="black", alpha=0.75, linewidths=1)
            plt.grid(b=True, color="lightgrey", linestyle="--")
            Prompt(Header3)
        elif ans == "4":
            PrintCombo(Header4)
            plot4_x = rawDF['Latitude']
            plot4_y = rawDF['Wind Speed (MPH)']
            plt.title(
                f"City Latitude vs. Wind Speed (~{relDate[0]})", fontweight='bold')
            plt.xlabel("Latitude", fontweight='bold')
            plt.ylabel("Wind Speed (MPH)", fontweight='bold')
            plt.scatter(plot4_x, plot4_y, facecolors="purple",
                        edgecolors="black", alpha=0.75, linewidths=1)
            plt.grid(b=True, color="lightgrey", linestyle="--")
            Prompt(Header4)
        elif ans == "5":
            # * [1] * #
            PrintCombo(Header1)
            plot1_x = rawDF['Latitude']
            plot1_y = FarenConversions
            plt.title(
                f"City Latitude vs. Max Temperature (~{relDate[0]})", fontweight='bold')
            plt.xlabel("Latitude", fontweight='bold')
            plt.ylabel("Max Temperature (F)", fontweight='bold')
            plt.scatter(plot1_x, plot1_y, facecolors="turquoise",
                        edgecolors="black", alpha=0.75, linewidths=1)
            plt.grid(b=True, color="lightgrey", linestyle="--")
            Prompt(Header1)
            # * [2] * #
            PrintCombo(Header2)
            plot2_x = rawDF['Latitude']
            humidityPlotData = HumidityConv(rawDF)
            plot2_y = humidityPlotData
            plt.title(
                f"City Latitude vs. Humidity (~{relDate[0]})", fontweight='bold')
            plt.xlabel("Latitude", fontweight='bold')
            plt.ylabel("Humidity (%)", fontweight='bold')
            plt.scatter(plot2_x, plot2_y, facecolors="blue",
                        edgecolors="black", alpha=0.75, linewidths=1)
            plt.grid(b=True, color="lightgrey", linestyle="--")
            Prompt(Header2)
            # * [3] * #
            PrintCombo(Header3)
            plot3_x = rawDF['Latitude']
            cloudsPlotData = CloudsConv(rawDF)
            plot3_y = cloudsPlotData
            plt.title(
                f"City Latitude vs. Cloudiness (~{relDate[0]})", fontweight='bold')
            plt.xlabel("Latitude", fontweight='bold')
            plt.ylabel("Cloudiness (%)", fontweight='bold')
            plt.scatter(plot3_x, plot3_y, facecolors="coral",
                        edgecolors="black", alpha=0.75, linewidths=1)
            plt.grid(b=True, color="lightgrey", linestyle="--")
            Prompt(Header3)
            # * [4] * #
            PrintCombo(Header4)
            plot4_x = rawDF['Latitude']
            plot4_y = rawDF['Wind Speed (MPH)']
            plt.title(
                f"City Latitude vs. Wind Speed (~{relDate[0]})", fontweight='bold')
            plt.xlabel("Latitude", fontweight='bold')
            plt.ylabel("Wind Speed (MPH)", fontweight='bold')
            plt.scatter(plot4_x, plot4_y, facecolors="purple",
                        edgecolors="black", alpha=0.75, linewidths=1)
            plt.grid(b=True, color="lightgrey", linestyle="--")
            Prompt(Header4)
        elif ans == "6":
            PrintCombo(Header6)
            csvName = str(input(" Please entitle your csv: ") + ".csv")
            PrintCombo(Header6)
            csvPath = str(
                input(" Please enter your absolute path to save it to: "))
            PrintCombo(Header6)
            csvOutput = os.path.join(csvPath, csvName)
            if os.path.exists(csvOutput):
                csvAnswerOR = None
                while csvAnswerOR not in ("y", "n"):
                    csvAnswerOR = str(input(
                        f" {color.RED}{color.BLINK}[!]{color.END} File: {color.BOLD}{color.UNDERLINE}{csvName}{color.END} already exists at: {color.BOLD}{color.UNDERLINE}{csvOutput}{color.END} {color.RED}{color.BLINK}[!]{color.END}\n\n Overwrite? {color.PURPLE}{color.BOLD}{color.REVERSED}[y/n]{color.END} "))
                    PrintCombo(Header6)
                    if csvAnswerOR == "y":
                        rawDF.to_csv(csvOutput, index=False)
                        print(
                            f" Output data {color.BOLD}{csvName}{color.END} overwritten to {color.BOLD}{csvOutput}{color.END}" )
                        time.sleep(2)
                        PrintCombo(Header6)
                    elif csvAnswerOR == "n":
                        print(" Continuing without overwriting..")
                        time.sleep(2)
                        PrintCombo(Header6)
                    else:
                        PrintElse()
                        PrintCombo(Header6)
            else:
                rawDF.to_csv(csvOutput, index=False)
                print(
                    f" Output data {color.BOLD}{csvName}{color.END} saved to {color.BOLD}{csvOutput}{color.END}\n" )
                time.sleep(2)
                PrintCombo(Header6)
        else:
            PrintAgain()
            PrintElse()
            PrintAgain()
            OutputMenu()


#*####################################################################################
# *                                     Main
#*####################################################################################
PrintWelcome()
newANS = NewData()
rawDF, relDate, FarenConversions = LoadData(newANS)
while Again() == "y":
    PrintAgain()
    ChoicePrompt(rawDF, relDate, FarenConversions)

