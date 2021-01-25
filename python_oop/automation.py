from selenium import webdriver

"""http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/"""
chrome_path = 'C:/Windows/chromedriver.exe'
chrome_browser = webdriver.Chrome(chrome_path)

chrome_browser.maximize_window()
