# import youtube_dl

# ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', })

# with ydl:
#     ydl.download(['https://www.youtube.com/watch?v=YB8AueopGdU'])

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

driver = webdriver.Remote(
    "http://172.21.0.3:4444/wd/hub", DesiredCapabilities.CHROME)

content = requests.get("")

# print(content)
# wait = WebDriverWait(driver, 10)
# wait.until(EC.frame_to_be_available_and_switch_to_it(
#     (By.TAG_NAME, 'iframe')))
# soup = BeautifulSoup(content.text, 'html.parser')
# print(soup)

# time.sleep(10)

# driver.quit()
# try:
# wait = WebDriverWait(driver, 10)

# wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, 'iframe')))

# print('123')

# blockquotes = soup.find_element_by

# for blockquote in blockquotes:
#     print(blockquote)
