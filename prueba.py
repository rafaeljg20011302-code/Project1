import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.google.com")
    print("Título:", driver.title)
    time.sleep(5)
finally:
    driver.quit()