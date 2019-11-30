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
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

# * * * * * * * * * * * * * * * * *   Auxillary Method Library   * * * * * * * * * * * * * * * * * #

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Splinter and Beautiful Soup Setup
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


def init_splinter():
    print('Initizalizing Splinter Browser...\n')
    time.sleep(2)
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser


def simmer_soup(browser):
    html = browser.html
    soup = bs(html, 'html.parser')
    return html, soup

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: NASA Mars News
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


@ C R I T I C A L   R E T U R N @
def scrape_news(browser):
    url = 'https://mars.nasa.gov/news/'
    print('Fetching Latest News...\n')
    browser.visit(url)
    time.sleep(2)
    html, soup = simmer_soup(browser)
    titles = soup.find_all('div', class_='content_title')
    latest_title = titles[0].text
    paragraphs = soup.find_all('div', class_='article_teaser_body')
    latest_paragraph = paragraphs[0].text
    latest_mars_news = {'title': latest_title,
                        'paragraph': latest_paragraph}
    return latest_mars_news

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: JPL Mars Space Images - Featured Image
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# def scrape_featured_image_data(browser):
#     url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
#     browser.visit(url2)
#     html, soup = simmer_soup(browser)
#     browser.click_link_by_partial_text('FULL IMAGE')
#     html, soup = simmer_soup(browser)
#     image_data = soup.find('img', class_='fancybox-image')
#     return image_data
#
#
# @NOTE this was the janky af one in * scrape_mars.py *
# def scrape_featured_image_hackyboi(browser):
#     try:
#         image_data = scrape_featured_image_data(browser)
#     except:
#         TypeError
#     print('Fetching Latest Featured Image...\n')
#     time.sleep(5)
#     try:
#         image_data = scrape_featured_image_data(browser)
#     except:
#         TypeError
#     # above 2 can be combined into fodder, bottom one should be a func called scrape_featured_image
#     featured_base = 'https://www.jpl.nasa.gov'
#     featured_end = image_data['src']
#     featured_image_url = featured_base + featured_end
#     return featured_image_url

# TODO attempted combining of the above is below, we'll see what happens


@ C R I T I C A L   R E T U R N @
def scrape_feature_image(browser):
    def spaghetti(browser):
        url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url2)
        html, soup = simmer_soup(browser)
        browser.click_link_by_partial_text('FULL IMAGE')
        html, soup = simmer_soup(browser)
        image_data = soup.find('img', class_='fancybox-image')
        return image_data
    try:
        image_data = spaghetti(browser)
    except:
        TypeError
    print('Fetching Latest Featured Image...\n')
    time.sleep(5)
    try:
        image_data = spaghetti(browser)
    except:
        TypeError
    featured_base = 'https://www.jpl.nasa.gov'
    featured_end = image_data['src']
    featured_image_url = featured_base + featured_end
    return featured_image_url

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: Mars Weather
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


@ C R I T I C A L   R E T U R N @
def scrape_weather(browser):
    url3 = 'https://twitter.com/marswxreport?lang=en'
    print('Fetching Latest Weather...\n')
    browser.visit(url3)
    time.sleep(2)
    html, soup = simmer_soup(browser)
    tweet_data = soup.find('div', class_='js-tweet-text-container')
    mars_weather = tweet_data.text[1:-27]
    return mars_weather


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: Mars Facts
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


# def scrape_facts_data(browser):
#     url4 = 'http://space-facts.com/mars/'
#     print('Fetching Latest Mars Facts...')
#     browser.visit(url4)
#     time.sleep(2)
#     html, soup = simmer_soup(browser)
#     mars_table = pd.read_html(html)
#     time.sleep(3)
#     mars_table = mars_table[(len(mars_table) - 1)]
#     mars_table_html_string = mars_table.to_html()
#     mars_table.to_csv('mars_facts.csv')
#     return mars_table_html_string, mars_table
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# # * Can't beat 'em, Join 'em:
# # * Mars Facts df to .csv to .png
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#
# def DataFrame_to_image(data, css, outputfile="mars_facts.png", format="png"):
#     fn = str("holding" + ".html")
#     try:
#         os.remove(fn)
#     except:
#         None
#     text_file = open(fn, "a")
#     text_file.write(css)
#     text_file.write(data.to_html())
#     text_file.close()
#     imgkitoptions = {"width": 652,
#                      'quality': 100}
#     imgkit.from_file(fn, outputfile, options=imgkitoptions)
#     os.remove(fn)
#     return outputfile
#
#
# def assemble_table_arguments():
#     mars_table = pd.read_csv(open('mars_facts.csv', 'r'))
#     mars_css = """
#     <style type=\"text/css\">
#     table {
#     color: #FFFFFF;
#     font-family: Helvetica, Arial, sans-serif;
#     width: 640px;
#     border-collapse:
#     collapse;
#     border-spacing: 0;
#     }
#     td, th {
#     border: 1px solid transparent; /* No more visible border */
#     height: 30px;
#     }
#     th {
#     background: #343A40; /* Darken header a bit */
#     color: #343A40;
#     font-weight: bold;
#     }
#     td {
#     background: #3D4449;
#     text-align: center;
#     }
#     table tr:nth-child(odd) td{
#     background-color: #343A40;
#     }
#     </style>
#     """
#     return mars_table, mars_css
#
# # combine these and figure out how to silence subprocesses' console logs
#
#
# def export_facts_table_img(mars_table, mars_css):
#     outputfile = DataFrame_to_image(mars_table, mars_css)
#     cwd = os.getcwd()
#     outputfilepath = str(cwd + '/' + outputfile)
#     subprocess.call('cp -rv mars_facts.png static/', shell=True)
#     return outputfilepath
#     print('\n')


@ C R I T I C A L   R E T U R N @
def scrape_facts(browser):
    url4 = 'http://space-facts.com/mars/'
    print('Fetching Latest Mars Facts...')
    browser.visit(url4)
    time.sleep(2)
    html, soup = simmer_soup(browser)
    mars_table = pd.read_html(html)
    time.sleep(3)
    mars_table = mars_table[(len(mars_table) - 1)]
    mars_table_html_string = mars_table.to_html()
    mars_table.to_csv('mars_facts.csv')
    # FIXME return mars_table_html_string, mars_table
    mars_table = pd.read_csv(open('mars_facts.csv', 'r'))
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
    # TODO Deconstruct this nested function()

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
    outputfile = DataFrame_to_image(mars_table, mars_css)
    cwd = os.getcwd()
    outputfilepath = str(cwd + '/' + outputfile)
    subprocess.call('cp -rv mars_facts.png static/', shell=True)
    mars_facts = {'html_string': mars_table_html_string,
                  'table_image': outputfilepath}
    return mars_facts

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * Scraping: Mars Hemispheres
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

# def scrape_hemisphere_data(browser):
#     url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#     print('Fetching Latest Hemisphere Images and Titles...')
#     browser.visit(url5)
#     time.sleep(2)
#     html, soup = simmer_soup(browser)
#     links = soup.find_all('a', class_='itemLink')
#     links_list = []
#     for link in links:
#         href = link['href']
#         if href not in links_list:
#             links_list.append(href)
#     cerberus_end = links_list[0]
#     schiaparelli_end = links_list[1]
#     syrtis_major_end = links_list[2]
#     valles_marineris_end = links_list[3]
#     links_start = 'https://astrogeology.usgs.gov'
#     cerberus_full = links_start + cerberus_end
#     schiaperelli_full = links_start + schiaparelli_end
#     syrtis_major_full = links_start + syrtis_major_end
#     valles_marineris_full = links_start + valles_marineris_end
#     return links_start, cerberus_full, schiaperelli_full, syrtis_major_full, valles_marineris_full
#
# # make a big one for each hem - possibly including above
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# # * Scraping: Mars Hemispheres - Cerberus
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#
#
# def scrape_cerberus(browser, links_start, cerberus_full):
#     print('-----Cerberus...')
#     browser.visit(cerberus_full)
#     time.sleep(1)
#     html, soup = simmer_soup(browser)
#     cerberus_pic_data = soup.find_all('img', class_="wide-image")
#     cerberus_pic_end = cerberus_pic_data[0]['src']
#     cerberus_picture_full = links_start + cerberus_pic_end
#     cerberus_title_data = soup.find('h2', class_='title')
#     cerberus_dict = {'img_url': cerberus_picture_full,
#     cerberus_title_full = cerberus_title_data.text
#
#                      'title': cerberus_title_full}
#     return cerberus_dict
#
# # * Scraping: Mars Hemispheres - Schiaperelli
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# def scrape_schiaperelli(browser, links_start, schiaperelli_full):
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#     browser.visit(schiaperelli_full)
#     print('-----Schiaperelli..')
#     html, soup = simmer_soup(browser)
#     time.sleep(1)
#     schiaperelli_pic_end = schiaperelli_pic_data[0]['src']
#     schiaperelli_pic_data = soup.find_all('img', class_="wide-image")
#     schiaperelli_title_data = soup.find('h2', class_='title')
#     schiaperelli_picture_full = links_start + schiaperelli_pic_end
#     schiaperelli_dict = {'img_url': schiaperelli_picture_full,
#     schiaperelli_title_full = schiaperelli_title_data.text
#
#                          'title': schiaperelli_title_full}
#     return schiaperelli_dict
# # * Scraping: Mars Hemispheres - Syrtis Major
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# def scrape_syrtis_major(browser, links_start, syrtis_major_full)
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#     browser.visit(syrtis_major_full)
#     print('-----Syrtis Major...')
#     html, soup = simmer_soup(browser)
#     time.sleep(1)
#     syrtis_major_pic_end = syrtis_major_pic_data[0]['src']
#     syrtis_major_pic_data = soup.find_all('img', class_="wide-image")
#     syrtis_major_title_data = soup.find('h2', class_='title')
#     syrtis_major_picture_full = links_start + syrtis_major_pic_end
#     syrtis_major_dict = {'img_url': syrtis_major_picture_full,
#     syrtis_major_title_full = syrtis_major_title_data.text
#
#                          'title': syrtis_major_title_full}
#     return syrtis_major_dict
# # * Scraping: Mars Hemispheres - Valles Marineris
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# def scrape_syrtis_major(browser, links_start, valles_marineris_full):
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#     browser.visit(valles_marineris_full)
#     print('-----Valles Marineris...\n')
#     html, soup = simmer_soup(browser)
#     time.sleep(1)
#     valles_marineris_pic_end = valles_marineris_pic_data[0]['src']
#     valles_marineris_pic_data = soup.find_all('img', class_="wide-image")
#     valles_marineris_title_data = soup.find('h2', class_='title')
#     valles_marineris_picture_full = links_start + valles_marineris_pic_end
#     valles_marineris_dict = {'img_url': valles_marineris_picture_full,
#     valles_marineris_title_full = valles_marineris_title_data.text
#
#                              'title': valles_marineris_title_full}
#     return valles_marineris_dict
#
#
#
#
# # * Append all hemisphere dicts to a list
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# def combine_hemisphere_dicts_into_list():
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#     mars_hemisphere_list.append(cerberus_dict)
#     mars_hemisphere_list = []
#     mars_hemisphere_list.append(syrtis_major_dict)
#     mars_hemisphere_list.append(schiaperelli_dict)
#     return mars_hemisphere_list
    mars_hemisphere_list.append(valles_marineris_dict)


@ C R I T I C A L   R E T U R N @
def scrape_hemispheres(browser):
    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    print('Fetching Latest Hemisphere Images and Titles...')
    browser.visit(url5)
    time.sleep(2)
    html, soup = simmer_soup(browser)
    links = soup.find_all('a', class_='itemLink')
    links_list = []
    for link in links:
        href = link['href']
        if href not in links_list:
            links_list.append(href)
    cerberus_end = links_list[0]
    schiaparelli_end = links_list[1]
    syrtis_major_end = links_list[2]
    valles_marineris_end = links_list[3]
    links_start = 'https://astrogeology.usgs.gov'
    cerberus_full = links_start + cerberus_end
    schiaperelli_full = links_start + schiaparelli_end
    syrtis_major_full = links_start + syrtis_major_end
    valles_marineris_full = links_start + valles_marineris_end
    print('-----Cerberus...')
    browser.visit(cerberus_full)
    time.sleep(1)
    html, soup = simmer_soup(browser)
    cerberus_pic_data = soup.find_all('img', class_="wide-image")
    cerberus_pic_end = cerberus_pic_data[0]['src']
    cerberus_picture_full = links_start + cerberus_pic_end
    cerberus_title_data = soup.find('h2', class_='title')
    cerberus_title_full = cerberus_title_data.text
    cerberus_dict = {'img_url': cerberus_picture_full,
                     'title': cerberus_title_full}
    print('-----Schiaperelli..')
    browser.visit(schiaperelli_full)
    time.sleep(1)
    html, soup = simmer_soup(browser)
    schiaperelli_pic_data = soup.find_all('img', class_="wide-image")
    schiaperelli_pic_end = schiaperelli_pic_data[0]['src']
    schiaperelli_picture_full = links_start + schiaperelli_pic_end
    schiaperelli_title_data = soup.find('h2', class_='title')
    schiaperelli_title_full = schiaperelli_title_data.text
    schiaperelli_dict = {'img_url': schiaperelli_picture_full,
                         'title': schiaperelli_title_full}
    print('-----Syrtis Major...')
    browser.visit(syrtis_major_full)
    time.sleep(1)
    html, soup = simmer_soup(browser)
    syrtis_major_pic_data = soup.find_all('img', class_="wide-image")
    syrtis_major_pic_end = syrtis_major_pic_data[0]['src']
    syrtis_major_picture_full = links_start + syrtis_major_pic_end
    syrtis_major_title_data = soup.find('h2', class_='title')
    syrtis_major_title_full = syrtis_major_title_data.text
    syrtis_major_dict = {'img_url': syrtis_major_picture_full,
                         'title': syrtis_major_title_full}
    print('-----Valles Marineris...\n')
    browser.visit(valles_marineris_full)
    time.sleep(1)
    html, soup = simmer_soup(browser)
    valles_marineris_pic_data = soup.find_all('img', class_="wide-image")
    valles_marineris_pic_end = valles_marineris_pic_data[0]['src']
    valles_marineris_picture_full = links_start + valles_marineris_pic_end
    valles_marineris_title_data = soup.find('h2', class_='title')
    valles_marineris_title_full = valles_marineris_title_data.text
    valles_marineris_dict = {'img_url': valles_marineris_picture_full,
                             'title': valles_marineris_title_full}
    mars_hemisphere_list = []
    mars_hemisphere_list.append(cerberus_dict)
    mars_hemisphere_list.append(schiaperelli_dict)
    mars_hemisphere_list.append(syrtis_major_dict)
    mars_hemisphere_list.append(valles_marineris_dict)
    return mars_hemisphere_list

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

# * * * * * * * * * * * * * * * * *   Primary Method Library   * * * * * * * * * * * * * * * * * #

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# browser.quit()


def assemble_all_scraped_data_into_dict(mars_hemisphere_list, latest_mars_news, featured_image_url, mars_weather, mars_facts):
    one_dict_to_rule_them_all = {'mars_hemisphere_list': mars_hemisphere_list,
                                 'latest_mars_news': latest_mars_news,
                                 'featured_image_url': featured_image_url,
                                 'latest_mars_weather': mars_weather,
                                 'mars_facts': mars_facts}
    return one_dict_to_rule_them_all
