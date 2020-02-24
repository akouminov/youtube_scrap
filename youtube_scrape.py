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

#https://www.youtube.com/results?search_query=bbc

#https://www.youtube.com/user/TEDtalksDirector

#https://www.youtube.com/user/bbcnews

#need a way to quantify if a video is good or not
#ask about the software that lines up text
#would be nice to run this on a server that is continuously running this

driver = webdriver.Chrome()
driver.get("YOUR_LINK_HERE")

youtube_scraper = YoutubeSubtitlesScraper()


