import time
import urllib.request

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class YoutubeSubtitlesScraper:

    def __init__(self, start_url):
        self.driver = webdriver.Chrome("C:/Users/koumi/bin/chromedriver.exe")

        self.wait = WebDriverWait(self.driver, 10)
        #start_url = 'https://www.youtube.com/user/TEDtalksDirector/videos'
        self.driver.get(start_url)
        self.display_all_videos()

    def __exit__(self):
        self.driver.close()

    def display_all_videos(self):
        """Clicks on "Load More" button to display all users videos."""
        while True:
            try:
                element = self.wait.until(EC.element_to_be_clickable((By.ID, "show-more-button")))
                element.click()
            except TimeoutException:
                break

    def subtitles(self):
        """Visits video's page, enables 'CC' to scrape the subtitles and generates filename, link and the subtitles content."""
        videos = [(video.text, video.get_attribute("href"))
                  for video in self.driver.find_elements_by_class_name("yt-simple endpoint")]

        for filename, link in videos:
            self.driver.get(link)
            self.enable_subtitles()

            link = self.get_subtitles_link()
            yield filename, link, self.scrape_subtitles(link) if link else "No Closed Caption"

    def enable_subtitles(self):
        """Clicks on CC(Closed Caption) button in YouTube video."""
        show_subtitles_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-subtitles-button")))
        show_subtitles_button.click()

    def toggle_sub_panel(self):
        """Clicks on more button to open the subtitle panel"""
        show_panel_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='More actions']")))
        show_panel_button.click()
        show_panel_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[text()[contains(.,'Open transcript')]]")))
        show_panel_button.click()

    def get_transcript(self):
        """scraps for transcript"""
        time.sleep(1)
        transcript = self.driver.find_elements_by_id("body")

    def get_subtitles_link(self):
        """Finds string in performance timings that contains the substring 'srv3' which is the subtitles link."""
        time.sleep(1)
        timings = self.driver.execute_script("return window.performance.getEntries();")

        for timing in timings:
            for value in timing.values():
                if "srv3" in str(value):
                    return value
        return ""

    def scrape_subtitles(self, subtitle_link):
        """HTML parses subtitles."""
        response = urllib.request.urlopen(subtitle_link)
        soup = BeautifulSoup(response, "lxml")
        return soup.get_text(strip=True)