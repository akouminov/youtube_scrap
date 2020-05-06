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

# is in english
# contains talking face, 50 %
# timestamps where model recognizes
# list of urls from which to get the videos

# https://www.youtube.com/results?search_query=bbc

# https://www.youtube.com/user/TEDtalksDirector

# https://www.youtube.com/user/bbcnews

#need a way to quantify if a video is good or not
#ask about the software that lines up text
#would be nice to run this on a server that is continuously running this

#driver = webdriver.Chrome()
#driver.get("YOUR_LINK_HERE")


def create_file(filename, link, subtitles):
    """Creates file for the subtitle."""
    title = "".join([c for c in filename if c.isalpha() or c.isdigit() or c == ' ']).rstrip()
    with open(title + '.txt', 'w') as subtitles_file:
        subtitles_file.write('LINK: ' + link + '\n')
        subtitles_file.write(subtitles)


start_url = 'https://www.youtube.com/user/TEDtalksDirector/videos'

scrapper = YoutubeSubtitlesScraper(start_url)
scrapper.display_all_videos()

videos = [(video.text, video.get_attribute("href"))
          for video in scrapper.driver.find_elements_by_id("video-title")]

for filename, link in videos:
    scrapper.driver.get(link)
    scrapper.enable_subtitles()
    scrapper.toggle_sub_panel()

    link = scrapper.get_subtitles_link()

# if __name__ == "__main__":
#     start_url = 'https://www.youtube.com/user/TEDtalksDirector/videos'
#     with YoutubeSubtitlesScraper() as scraper:
#         for filename, link, content in scraper.subtitles():
#             try:
#                 create_file(filename, link, content)
#             except Exception:
#                 print("Can't create file for: " + filename + " : " + link)

