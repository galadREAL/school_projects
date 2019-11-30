#!/usr/bin/env python
# coding: utf-8

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Dependencies
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import os
import imgkit
import subprocess

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Browser Setup
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Links up chrome to this notebook
print('Initizalizing Splinter Browser...\n')
time.sleep(2)
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: NASA Mars News
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Provided url is assigned and a browser is sent to visit the page
url = 'https://mars.nasa.gov/news/'
print('Fetching Latest News...\n')
browser.visit(url)
time.sleep(2)

# Stick the url's html into a soup object to parse
html = browser.html
soup = bs(html, 'html.parser')

# Gather up all the content_title and assign the [0] position one to latest_title
titles = soup.find_all('div', class_='content_title')
latest_title = titles[0].text

# Gather up all the article_teaser_body and assign the [0] position one to latest_paragraph
paragraphs = soup.find_all('div', class_='article_teaser_body')
latest_paragraph = paragraphs[0].text

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: JPL Mars Space Images - Featured Image
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


def test():
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    # Read in current page as soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Click the full image link
    browser.click_link_by_partial_text('FULL IMAGE')

    # Read in current page as soup
    html = browser.html
    soup = bs(html, 'html.parser')

    # Gather up the fancy-box image data
    image_data = soup.find('img', class_='fancybox-image')
    return image_data


# TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO
# @NOTE #* Don't change this, it will break without failing, waiting, and redoing..
try:
    image_data = test()
except:
    TypeError
print('Fetching Latest Featured Image...\n')
time.sleep(5)
try:
    image_data = test()
except:
    TypeError
# TODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODOTODO

# Assign the base starting url
featured_base = 'https://www.jpl.nasa.gov'

# Assign the src field ending url
featured_end = image_data['src']

# Assign the full url with the base and the end
featured_image_url = featured_base + featured_end


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: Mars Weather
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Provided url is assigned and a browser is sent to visit the page
url3 = 'https://twitter.com/marswxreport?lang=en'
print('Fetching Latest Weather...\n')
browser.visit(url3)
time.sleep(2)

# Read in current page as soup
html = browser.html
soup = bs(html, 'html.parser')

# Gather up tweet data
tweet_data = soup.find('div', class_='js-tweet-text-container')

# This takes off the tweet's picture link
mars_weather = tweet_data.text[1:-27]

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: Mars Facts
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Provided url is assigned and a browser is sent to visit the page
url4 = 'http://space-facts.com/mars/'
print('Fetching Latest Mars Facts...')
browser.visit(url4)
time.sleep(2)

# Read in current page as soup
html = browser.html
soup = bs(html, 'html.parser')

mars_table = pd.read_html(html)
time.sleep(3)
mars_table = mars_table[(len(mars_table) - 1)]

mars_table_html_string = mars_table.to_html()

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Can't beat 'em, Join 'em:
# * Mars Facts df to .csv to .png
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Convert the raw html's dataframe into a .csv
mars_table.to_csv('mars_facts.csv')

# https://medium.com/@andy.lane/convert-pandas-dataframes-to-images-using-imgkit-5da7e5108d55


def DataFrame_to_image(data, css, outputfile="mars_facts.png", format="png"):
    fn = str("holding" + ".html")
    try:
        os.remove(fn)
    except:
        None
    text_file = open(fn, "a")
    text_file.write(css)
    text_file.write(data.to_html())
    text_file.close()
    imgkitoptions = {"width": 652,
                     'quality': 100}
    imgkit.from_file(fn, outputfile, options=imgkitoptions)
    os.remove(fn)
    return outputfile


# Read the facts table output csv back into a df
mars_table = pd.read_csv(open('mars_facts.csv', 'r'))

# Declare css styling that will match the index.html
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

# Execute the df to image method and assign the path of the output image
outputfile = DataFrame_to_image(mars_table, mars_css)
cwd = os.getcwd()
outputfilepath = str(cwd + '/' + outputfile)
# facts_move = str(f'cp'+' '+'-r'+' ' +
#                 {outputfilepath}+' '+{cwd}+'/static'+{outputfile})
subprocess.call('cp -rv mars_facts.png static/', shell=True)
print(cwd)
print('\n')

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: Mars Hemispheres
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Provided url is assigned and a browser is sent to visit the page
url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
print('Fetching Latest Hemisphere Images and Titles...')
browser.visit(url5)
time.sleep(2)

# Read in current page as soup
html = browser.html
soup = bs(html, 'html.parser')

# Gather all link data
links = soup.find_all('a', class_='itemLink')

# Create an empty list to hold each hemisphere's link
links_list = []

# Append each hemisphere's link to the links_list if it doesn't already exist (delete dupes)
for link in links:
    href = link['href']
    if href not in links_list:
        links_list.append(href)

# Assign vars for each one
cerberus_end = links_list[0]
schiaparelli_end = links_list[1]
syrtis_major_end = links_list[2]
valles_marineris_end = links_list[3]

# Assign the base url to use with the hemipshere's links
links_start = 'https://astrogeology.usgs.gov'

# Assign vars for full links (base + hemisphere)
cerberus_full = links_start + cerberus_end
schiaperelli_full = links_start + schiaparelli_end
syrtis_major_full = links_start + syrtis_major_end
valles_marineris_full = links_start + valles_marineris_end

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: Mars Hemispheres - Cerberus
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Navigate the browser to the hemisphere's url
print('-----Cerebus...')
browser.visit(cerberus_full)
time.sleep(1)

# Read in current page as soup
html = browser.html
soup = bs(html, 'html.parser')

# Gather the wide-image class' source url and assign to a var
cerberus_pic_data = soup.find_all('img', class_="wide-image")
cerberus_pic_end = cerberus_pic_data[0]['src']

# Assign a var for the full url (base + hemisphere)
cerberus_picture_full = links_start + cerberus_pic_end

# Gather the first h2 header of title class and assign the text output to a var
cerberus_title_data = soup.find('h2', class_='title')
cerberus_title_full = cerberus_title_data.text

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: Mars Hemispheres - Schiaperelli
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Navigate the browser to the hemisphere's url
print('-----Schiaperelli..')
browser.visit(schiaperelli_full)
time.sleep(1)

# Read in current page as soup
html = browser.html
soup = bs(html, 'html.parser')

# Gather the wide-image class' source url and assign to a var
schiaperelli_pic_data = soup.find_all('img', class_="wide-image")
schiaperelli_pic_end = schiaperelli_pic_data[0]['src']

# Assign a var for the full url (base + hemisphere)
schiaperelli_picture_full = links_start + schiaperelli_pic_end

# Gather the first h2 header of title class and assign the text output to a var
schiaperelli_title_data = soup.find('h2', class_='title')
schiaperelli_title_full = schiaperelli_title_data.text

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: Mars Hemispheres - Syrtis Major
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Navigate the browser to the hemisphere's url
print('-----Syrtis Major...')
browser.visit(syrtis_major_full)
time.sleep(1)

# Read in current page as soup
html = browser.html
soup = bs(html, 'html.parser')

# Gather the wide-image class' source url and assign to a var
syrtis_major_pic_data = soup.find_all('img', class_="wide-image")
syrtis_major_pic_end = syrtis_major_pic_data[0]['src']

# Assign a var for the full url (base + hemisphere)
syrtis_major_picture_full = links_start + syrtis_major_pic_end

# Gather the first h2 header of title class and assign the text output to a var
syrtis_major_title_data = soup.find('h2', class_='title')
syrtis_major_title_full = syrtis_major_title_data.text

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: Mars Hemispheres - Valles Marineris
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Navigate the browser to the hemisphere's url
print('-----Valles Marineris...\n')
browser.visit(valles_marineris_full)
time.sleep(1)

# Read in current page as soup
html = browser.html
soup = bs(html, 'html.parser')

# Gather the wide-image class' source url and assign to a var
valles_marineris_pic_data = soup.find_all('img', class_="wide-image")
valles_marineris_pic_end = valles_marineris_pic_data[0]['src']

# Assign a var for the full url (base + hemisphere)
valles_marineris_picture_full = links_start + valles_marineris_pic_end

# Gather the first h2 header of title class and assign the text output to a var
valles_marineris_title_data = soup.find('h2', class_='title')
valles_marineris_title_full = valles_marineris_title_data.text

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Data Munging: Hemisphere dictionaries with scraped image url and title
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Use a Python dictionary to store the data using the keys img_url and title.
cerberus_dict = {'img_url': cerberus_picture_full,
                 'title': cerberus_title_full}
schiaperelli_dict = {'img_url': schiaperelli_picture_full,
                     'title': schiaperelli_title_full}
syrtis_major_dict = {'img_url': syrtis_major_picture_full,
                     'title': syrtis_major_title_full}
valles_marineris_dict = {'img_url': valles_marineris_picture_full,
                         'title': valles_marineris_title_full}

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Data Munging: Append all hemisphere dictionaries to a list
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# Append the dictionary with the image url string and the hemisphere title to a list.
# This list will contain one dictionary for each hemisphere.
mars_hemisphere_list = []
mars_hemisphere_list.append(cerberus_dict)
mars_hemisphere_list.append(schiaperelli_dict)
mars_hemisphere_list.append(syrtis_major_dict)
mars_hemisphere_list.append(valles_marineris_dict)
mars_hemisphere_list


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Method Library
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

browser.quit()

# Scrape is a method required by the homework that is to execute all of my scraping code above and
# return one Python dictionary containing all of the scraped data.


def scrape():
    latest_mars_news = {'title': latest_title,
                        'paragraph': latest_paragraph}
    mars_facts = {'html_string': mars_table_html_string,
                  'table_image': outputfilepath}
    one_dict_to_rule_them_all = {'mars_hemisphere_list': mars_hemisphere_list,
                                 'latest_mars_news': latest_mars_news,
                                 'featured_image_url': featured_image_url,
                                 'latest_mars_weather': mars_weather,
                                 'mars_facts': mars_facts}
    return one_dict_to_rule_them_all
