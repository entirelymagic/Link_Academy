from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/"""
chrome_path = 'C:/Windows/chromedriver.exe'
chrome_browser = webdriver.Chrome(chrome_path)

chrome_browser.maximize_window()

"""
Browser Arguments:

–headless

To open browser in headless mode. Works in both Chrome and Firefox browser

–start-maximized

To start browser maximized to screen. Requires only for Chrome browser. Firefox by default starts maximized

–incognito

To open private chrome browser

–disable-notifications

To disable notifications, works Only in Chrome browser
"""
options = Options()
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")
