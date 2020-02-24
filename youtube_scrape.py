import sys
import time
import urllib.request

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from YoutubeSubtitleScrapper import YoutubeSubtitlesScraper

# https://www.youtube.com/
# https://www.analyticsvidhya.com/blog/2019/05/scraping-classifying-youtube-video-data-python-selenium/
# https://codereview.stackexchange.com/questions/166010/scraping-all-closed-captions-subtitles-of-a-youtubes-creators-video-library

#https://www.youtube.com/results?search_query=bbc

#https://www.youtube.com/user/TEDtalksDirector

#https://www.youtube.com/user/bbcnews

#need a way to quantify if a video is good or not
#ask about the software that lines up text
#would be nice to run this on a server that is continuously running this

driver = webdriver.Chrome()
driver.get("YOUR_LINK_HERE")

ted_talk_youtube_scraper = YoutubeSubtitlesScraper('https://www.youtube.com/user/TEDtalksDirector')


def create_file(filename, link, subtitles):
    """Creates file for the subtitle."""
    title = "".join([c for c in filename if c.isalpha() or c.isdigit() or c == ' ']).rstrip()
    with open(title + '.txt', 'w') as subtitles_file:
        subtitles_file.write('LINK: ' + link + '\n')
        subtitles_file.write(subtitles)


with ted_talk_youtube_scraper as scraper:
    for filename, link, content in scraper.subtitles():
        try:
            create_file(filename, link, content)
        except:
            print("Can't create file for: " + filename + " : " + link)

