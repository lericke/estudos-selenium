
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVE_EZEC = ROOT_FOLDER / 'drivers' / 'chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=str(CHROMEDRIVE_EZEC))
Chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options
)

Chrome_browser.get('https://www.google.com/')

time.sleep(30)