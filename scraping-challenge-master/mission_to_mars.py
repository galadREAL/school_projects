#!/usr/bin/env python
# coding: utf-8

ascii = '''
#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8
#?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&
#@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #

                   @@@@@@      @@@@@@@       @@@@@@       @@@@@@      @@@@@@@
                  @@@@@@@      @@@@@@@@     @@@@@@@@     @@@@@@@@     @@@@@@@@
                  !@@          @@!  @@@     @@!  @@@     @@!  @@@     @@!  @@@
                  !@!          !@!  @!@     !@!  @!@     !@!  @!@     !@!  @!@
                  !!@@!!       @!@@!@!      @!@!@!@!     @!@!@!@!     @!@!!@!
                   !!@!!!      !!@!!!       !!!@!!!!     !!!@!!!!     !!@!@!
                       !:!     !!:          !!:  !!!     !!:  !!!     !!: :!!
                      !:!      :!:          :!:  !:!     :!:  !:!     :!:  !:!
                  :::: ::       ::          ::   :::     ::   :::     ::   :::
                  :: : :        :            :   : :      :   : :      :   : :

# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*
#?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&?&
#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8
'''

print(ascii)

#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
# *                                                                                               * #
#? * * * * * * * * * * * * * * * * * * / Mission to Mars: Setup / * * * * * * * * * * * * * * * * * @
# *                                                                                               * #
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@
#? * * * * * * * * * * * * * * * / Dependencies + Decleration Methods / * * * * * * * * * * * * * * *@
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @

#* Dependencies needed for Method Libraries *#
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import os
import imgkit
import subprocess


#* Dependencies needed for Flask framework *#
from flask import Flask, redirect, url_for, render_template, g, request
from flask_pymongo import PyMongo
import colors
import time
import datetime
from rfc3339 import rfc3339




#* Inits needed for Method Libraries *#
def init_splinter():
    '''
        init_splinter() initializes and returns an automated Chrome web browser for us to use for
    scraping.
    '''
    print('Initizalizing Splinter Browser...\n')
    time.sleep(2)
    ############################################
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    ############################################
    return browser


def simmer_soup():
    '''
        simmer_soup() receives the Splinter browser and returns the current page's parsed html as
    "Soup".
    '''
    html = browser.html
    soup = bs(html, 'html.parser')
    ############################################
    return html, soup




#* Inits needed for Flask framework *#
def init_global_flask():
    '''
        init_global_flask() initializes Flask to be used globally as a const among other programs,
    it returns its app var out to main for use.
    '''
    app = Flask(__name__)
    ############################################
    return app


def init_mongoDB():
    '''
        init_mongoDB() initizalizes a connection to the local mongoDB entitled "mars" for use with
    PyMongo and Flask so that we can send and receive data.
    '''
    mongo = PyMongo(app, uri="mongodb://localhost:27017/mars")
    ############################################
    return mongo



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@
#? * * * * * * * * * * * * * * * * * / Initialization Of Constants / * * * * * * * * * * * * * * * * @
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @

browser = init_splinter()
browser.driver.minimize_window()


app = init_global_flask()


mongo = init_mongoDB()



#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
# *                                                                                               * #
#? * * * * * * * * * * * * * * * * * / Auxillary Method Library / * * * * * * * * * * * * * * * * * @
# *                                                                                               * #
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @
#? * * * * * * * * * / Scraping The Latest Mars-Related News Article From NASA / * * * * * * * * * *@
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@

def scrape_news():
    '''
        scrape_news() first scrapes NASA's Mars website for all data in dividers of class type
    "content_title". Next, the very first result, position [0], is casted to text and assigned the
    variable called "latest_title".
        Afterwards, the website is scraped for all data in dividers of class type
    "article_teaser_body".
        Again, the very first result, the most recent, is casted to text and assigned a variable
    called "latest_paragraph". Last, both of the new variables are appended to a new dictionary
    variable named "latest_mars_news" and then returned for later use.
    '''
    url = 'https://mars.nasa.gov/news/'
    print('Fetching Latest News...\n')
    browser.visit(url)
    time.sleep(2)
    ############################################
    html, soup = simmer_soup()
    titles = soup.find_all('div', class_='content_title')
    latest_title = titles[0].text
    ############################################
    paragraphs = soup.find_all('div', class_='article_teaser_body')
    latest_paragraph = paragraphs[0].text
    ############################################
    latest_mars_news = {'title': latest_title,
                        'paragraph': latest_paragraph}
    ############################################
    return latest_mars_news



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @
#? * * * * * * * / Scraping: The Currently Featured, Full-Sized Image Of Mars From JPL / * * * * *  @
#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @

def scrape_feature_image():
    '''
        scrape_feature_image() starts attempting to have the variable "image_data" returned from the
    nested function "spaghetti" (aptly named due to the spaghetti code this entire section is
    comprised of). A TypeError is expected to return for the first attempt, but after triel and
    error - a five second delay before retrying seems to do the trick.
        Now with our data contained inside of "image_data" safe in hand, we are next able to pull
    the image's full resolution source link out. We then assign it to its own variable as well
    as a variable that has the full source location's url string which we then return for later
    use.
    '''
    def spaghetti():
        '''
            spaghetti lives up to its namesake in that I have no idea why it behaves the way it
        does, but we've since formed a working relationship to accomplish our data analytics' goals.
        Our first execution is expected to fail, so we just wait for scrape_feature_image() to try
        again.
            Now that that's done, we can get started by navigating the browser through the link
        entitled "FULL IMAGE". Next we parse the html page we land on for only the first image tag
        that is of class type "fancybox-image". We assign that raw html data to a variable and
        return it back out to scrape_feature_image() for further use.
        '''
        url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url2)
        html, soup = simmer_soup()
        browser.click_link_by_partial_text('FULL IMAGE')
        ############################################
        html, soup = simmer_soup()
        image_data = soup.find('img', class_='fancybox-image')
        ############################################
        return image_data
    ############################################
    try:
        image_data = spaghetti()
    except:
        TypeError
    print('Fetching Latest Featured Image...\n')
    time.sleep(5)
    ############################################
    try:
        image_data = spaghetti()
    except:
        TypeError
    ############################################
    featured_base = 'https://www.jpl.nasa.gov'
    featured_end = image_data['src']
    featured_image_url = featured_base + featured_end
    ############################################
    return featured_image_url



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @
#? * * * / Scraping: The Latest Weather Report Via A Twitter Relay From The Curiosity Rover / * * * @
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @

def scrape_weather():
    '''
        scrape_weather() navigates to the "MarswxReport" Twitter relay account to scrape the most
    recent tweet sent directly from the REMS weather instrument aboard the Curiosity Rover!
        The page's html is parsed and the most recent divider of class type
    "js-tweet-text-container" is assigned the the variable "tweet_data". It is next chopped up so
    that the photo link no longer remains amongst the Martian weather data and returned back out to
    the main for later use.
    '''
    url3 = 'https://twitter.com/marswxreport?lang=en'
    print('Fetching Latest Weather...\n')
    browser.visit(url3)
    time.sleep(2)
    ############################################
    html, soup = simmer_soup()
    tweet_data = soup.find('div', class_='js-tweet-text-container')
    mars_weather = tweet_data.text[1:-27]
    ############################################
    return mars_weather



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @
#? * * * * * / Scraping: A Table Of Mars-Centric Facts From An Space Enthusiasts Site / * * * * * * @
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@

def scrape_facts():
    '''
        scrape_facts() was the most challenging part of the assignment for me. Without knowledge of
    JS, I was unable to find any sort of method across the internet to dynamically convert my
    DataFrame's "to_html()" data and then display its table string on an existing html document.
        What I *did* find, was an old medium.com article written by an absent github user of the
    last 3 years that went over and provided some very hacked together and incomplete incarnates of
    imgkit and wkhtmltopdf. It all behaves strangely enough and throws bizarre enough errors while
    in debug mode that I went on an "Are these rootkits?" adventure, but I digress.
        Behold! The funkiest, most roundabout way of displaying the Martian facts' table data
    scraped from the Space-Facts website.
        We first read the raw html into a Series, where we next fix the ValueErrors to turn it into
    a fully-fledged DataFrame. We immediately chuck it back out into an html table string where it
    then goes to sit in a variable called "mars_table_html_string". It will be returned back to the
    main, where it will eventually be locked up in my local MongoDB along with all the other pieces
    of data.
        Anyways, we next yeet out a .csv version of the Dataframe for good measure. Except we
    actually will get some good use out of it! Next I shoved that very .csv right back into a new
    DataFrame, wrote out a bunch of CSS styling that matches my current index html templates vibe.
        ...We then embark on the aforementioned hack-job of python, pandas, css, html, subsystem
    processes, IO writers and buffers, likely 0-day'd custom image munging modules, and sketchy,
    Anti-Virus warning inducing .pkgs....until....we actually end up with a heckin' decent,
    custom-sized, custom-quality-chosen, color-coordinating, .png of the original table we started
    way back at the top of these paragraphs with.
        I assign the output file's relative path into a variable and then send it off over to the
    folder called "static" since that seems to be the only place that Flask will let me host pics on
    my html pages from locally - As well as not output files into from a shell. If you try to run
    this on your local system, get ready for a chmod party btw.
        Last, we merge that mars_table_html_string along with the pretty .png picture of what the
    html table string could only hope to someday be into a dictionary, and werf it back out to main.
    '''
    url4 = 'http://space-facts.com/mars/'
    print('Fetching Latest Mars Facts...\n')
    browser.visit(url4)
    time.sleep(2)
    ############################################
    html, soup = simmer_soup()
    mars_table = pd.read_html(html)
    time.sleep(3)
    ############################################
    mars_table = mars_table[(len(mars_table) - 1)]
    mars_table_html_string = mars_table.to_html()
    ############################################
    mars_table.to_csv('mars_facts.csv')
    mars_table = pd.read_csv(open('mars_facts.csv', 'r'))
    ############################################
    mars_css = """
    <style type=\"text/css\">
    table {
    color: #FFFFFF;
    font-family: Helvetica, Arial, sans-serif;
    width: 640px;
    border-collapse:
    collapse;
    border-spacing: 0;
    }
    td, th {
    border: 1px solid transparent; /* No more visible border */
    height: 30px;
    }
    th {
    background: #343A40; /* Darken header a bit */
    color: #343A40;
    font-weight: bold;
    }
    td {
    background: #3D4449;
    text-align: center;
    }
    table tr:nth-child(odd) td{
    background-color: #343A40;
    }
    </style>
    """
    ############################################
    print('Rendering Fact Table Image...\n')
    # TODO Deconstruct this nested func()
    def DataFrame_to_image(data, css, outputfile="mars_facts.png", format="png"):
        '''
            I fully intend to deconstruct this to try and not have such a disgusting monstrosity of
        a method for you to have to wretch at...but let's face it, probs not gonna happen. If you're
        reading this I hope it has been amusing :)
            Anywho this thing takes in a DataFrame, a CSS styles string literal, and then you just
        pick out your output's filename and the format of it up there in the def line.
            A solid 1/4 of this had broken code in it straight from the author, but, alas it moves
        down the pipeline. It first makes up a temporary filename, and if a file already exists then
        that existing one gets nerfed. That new temp file is opened and then the arguments supplied
        are written into it. It's next shaken out into an html document, closed up, the .pngs
        rendering options I chose are applied, the variable holding the name of the temporary file
        is killed, and our glorious outputfile (just the filename) is returned out to scrape_facts()
        for further data manipulation.
        '''
        fn = str("holding" + ".html")
        try:
            os.remove(fn)
        except:
            None
        ############################################
        text_file = open(fn, "a")
        text_file.write(css)
        text_file.write(data.to_html())
        text_file.close()
        ############################################
        imgkitoptions = {"width": 652,
                         'quality': 100}
        ############################################
        imgkit.from_file(fn, outputfile, options=imgkitoptions)
        os.remove(fn)
        return outputfile
    ############################################
    outputfile = DataFrame_to_image(mars_table, mars_css)
    ############################################
    cwd = os.getcwd()
    outputfilepath = str(cwd + '/' + outputfile)
    subprocess.call('cp -rv mars_facts.png static/', shell=True)
    ############################################
    mars_facts = {'html_string': mars_table_html_string,
                  'table_image': outputfilepath}
    ############################################
    return mars_facts



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @
#? * * * * * / Scraping: Descriptors + Photos Of Martian Hemispheres From The U.S.G.S / * * * * * * @
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@

def scrape_hemispheres():
    '''
    scrape_hemispheres() scrapes out the images as well as the descriptors thereof for each of The Red
    Planet's hemispheres.
    "How?", you might ask?
    Well lemme tell you. The Splinter navigates onto the USGS' homebase where all link elements
    ("a") of class typle "itemLink" are dumped into a variable assignment called "links". Now since
    there were duplicate entries in our variable, we envoke a for-loop to append the distinct
    entries (their href data specifically) into a new, blank list. Each distinct entry is assigned
    out of the list and into another new variable as the "end" part of the full url src link. Next
    I made the "start" or "base" url variable and linked them all up so we had the pages for each
    Hemi.
    We next go to each Hemi's page and dump the raw html data into "Soups" which we then pick out
    the image and its descriptor, aptly named "wide-image" and "title" by our Federal compatriots.
    Along the way, each of the Hemi's sets are appended into their own dicts, at the end all of
    those dicts are appended to one big list of dicts called "mars_hemisphere_list" - I know, I'm
    super creative -, which is then yonked back out to the main for further use.
    '''
    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    print('\nFetching Latest Hemisphere Images and Titles...')
    browser.visit(url5)
    time.sleep(2)
    ############################################
    html, soup = simmer_soup()
    links = soup.find_all('a', class_='itemLink')
    ############################################
    links_list = []
    for link in links:
        href = link['href']
        if href not in links_list:
            links_list.append(href)
    ############################################
    cerberus_end = links_list[0]
    schiaparelli_end = links_list[1]
    syrtis_major_end = links_list[2]
    valles_marineris_end = links_list[3]
    ############################################
    links_start = 'https://astrogeology.usgs.gov'
    ############################################
    cerberus_full = links_start + cerberus_end
    schiaperelli_full = links_start + schiaparelli_end
    syrtis_major_full = links_start + syrtis_major_end
    valles_marineris_full = links_start + valles_marineris_end
    ############################################
    print('-----Cerberus...')
    browser.visit(cerberus_full)
    time.sleep(1)
    ############################################
    html, soup = simmer_soup()
    cerberus_pic_data = soup.find_all('img', class_="wide-image")
    cerberus_pic_end = cerberus_pic_data[0]['src']
    cerberus_picture_full = links_start + cerberus_pic_end
    ############################################
    cerberus_title_data = soup.find('h2', class_='title')
    cerberus_title_full = cerberus_title_data.text
    ############################################
    cerberus_dict = {'img_url': cerberus_picture_full,
                     'title': cerberus_title_full}
    ############################################
    print('-----Schiaperelli..')
    browser.visit(schiaperelli_full)
    time.sleep(1)
    ############################################
    html, soup = simmer_soup()
    schiaperelli_pic_data = soup.find_all('img', class_="wide-image")
    schiaperelli_pic_end = schiaperelli_pic_data[0]['src']
    schiaperelli_picture_full = links_start + schiaperelli_pic_end
    ############################################
    schiaperelli_title_data = soup.find('h2', class_='title')
    schiaperelli_title_full = schiaperelli_title_data.text
    ############################################
    schiaperelli_dict = {'img_url': schiaperelli_picture_full,
                         'title': schiaperelli_title_full}
    ############################################
    print('-----Syrtis Major...')
    browser.visit(syrtis_major_full)
    time.sleep(1)
    ############################################
    html, soup = simmer_soup()
    syrtis_major_pic_data = soup.find_all('img', class_="wide-image")
    syrtis_major_pic_end = syrtis_major_pic_data[0]['src']
    syrtis_major_picture_full = links_start + syrtis_major_pic_end
    ############################################
    syrtis_major_title_data = soup.find('h2', class_='title')
    syrtis_major_title_full = syrtis_major_title_data.text
    ############################################
    syrtis_major_dict = {'img_url': syrtis_major_picture_full,
                         'title': syrtis_major_title_full}
    ############################################
    print('-----Valles Marineris...\n')
    browser.visit(valles_marineris_full)
    time.sleep(1)
    ############################################
    html, soup = simmer_soup()
    valles_marineris_pic_data = soup.find_all('img', class_="wide-image")
    valles_marineris_pic_end = valles_marineris_pic_data[0]['src']
    valles_marineris_picture_full = links_start + valles_marineris_pic_end
    ############################################
    valles_marineris_title_data = soup.find('h2', class_='title')
    valles_marineris_title_full = valles_marineris_title_data.text
    ############################################
    valles_marineris_dict = {'img_url': valles_marineris_picture_full,
                             'title': valles_marineris_title_full}
    ############################################
    mars_hemisphere_list = []
    mars_hemisphere_list.append(cerberus_dict)
    mars_hemisphere_list.append(schiaperelli_dict)
    mars_hemisphere_list.append(syrtis_major_dict)
    mars_hemisphere_list.append(valles_marineris_dict)
    ############################################
    return mars_hemisphere_list



#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
# *                                                                                               * #
#? * * * * * * * * * * * * * * * * * / Primary Method Library / * * * * * * * * * * * * * * * * * * @
# *                                                                                               * #
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@
#? * * * * * * / Scraping: All Possible Data + Encompassing Dict Assembly For MongoDB / * * * * * * *@
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @

def scrape_all_and_assemble():
    '''
        scrape_all_and_assemble() does just that. Combining all of the newly refactored into single
    methods per query into one encompassing method. It even assembles all the data into one
    dictionary in preperation for MongoDB to receive it as the next and current standing entry.
    '''
    ############################################
    latest_mars_news = scrape_news()
    featured_image_url = scrape_feature_image()
    mars_weather = scrape_weather()
    mars_facts = scrape_facts()
    mars_hemisphere_list = scrape_hemispheres()
    ############################################
    biggus_dictus = {'mars_hemisphere_list': mars_hemisphere_list,
                                 'latest_mars_news': latest_mars_news,
                                 'featured_image_url': featured_image_url,
                                 'latest_mars_weather': mars_weather,
                                 'mars_facts': mars_facts}
    ############################################
    return biggus_dictus



#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
# *                                                                                               * #
#? * * * * * * * * * * * * * * * * * * / Flask Web Framewerkz / * * * * * * * * * * * * * * * * * * @
# *                                                                                               * #
# * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * # * #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8!8



#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@
#? * * * * * * * * * * * * * * * * * / Route Hooks Establishment / * * * * * * * * * * * * * * * * * @
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @

@app.route('/')
def home():
    '''
        home() pulls the data out of the local MongoDB and then renders it into the home index.html
    any and every time the user naigates there.
    '''
    mongo_data = mongo.db.collection.find_one()
    ############################################
    return render_template("index.html", data=mongo_data)


@app.route('/scrape')
def scrape():
    '''
        scrape() calls the scrape_all_and_assemble() function to scrape and return a dict of all
    known data sources for the elements needed. The completed dict dataset is then sent in to the
    local MongoDB to overwrite the existing information.
        The user is then redirected back to the homepage where the newly acquired data is rendered
    into the template for their dashboarding pleasure.
    '''
    mars_data = scrape_all_and_assemble()
    mongo.db.collection.replace_one({}, mars_data, upsert=True)
    ############################################
    return redirect("/", code=302)




#?- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -@
#? * * * * * * * * * * * * * * * * * * * / Debugging Stuffs / * * * * * * * * * * * * * * * * * * * *@
#? - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - @

@app.before_request
def start_timer():
    g.start = time.time()


@app.after_request
def log_request(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    ############################################
    now = time.time()
    duration = round(now - g.start, 2)
    dt = datetime.datetime.fromtimestamp(now)
    timestamp = rfc3339(dt, utc=True)
    ############################################
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.args)
    ############################################
    log_params = [('method', request.method, 'blue'),
                  ('path', request.path, 'blue'),
                  ('status', response.status_code, 'yellow'),
                  ('duration', duration, 'green'),
                  ('time', timestamp, 'magenta'), ('ip', ip, 'red'),
                  ('host', host, 'red'), ('params', args, 'blue')]
    ############################################
    request_id = request.headers.get('X-Request-ID')
    if request_id:
        log_params.append(('request_id', request_id, 'yellow'))
    ############################################
    parts = []
    for name, value, color in log_params:
        part = colors.color("{}={}".format(name, value), fg=color)
        parts.append(part)
    line = " ".join(parts)
    ############################################
    app.logger.info(line)
    ############################################
    return response


if __name__ == "__main__":
    app.run(debug=False)