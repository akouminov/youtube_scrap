from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# https://www.youtube.com/

#https://www.youtube.com/results?search_query=bbc

#https://www.youtube.com/user/TEDtalksDirector

#https://www.youtube.com/user/bbcnews

#need a way to quantify if a video is good or not
#ask about the software that lines up text
#would be nice to run this on a server that is continuously running this

driver = webdriver.Chrome()
driver.get("YOUR_LINK_HERE")