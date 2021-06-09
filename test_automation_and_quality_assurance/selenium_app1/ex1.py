import logging
import os
import keyboard
import time
import datetime
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from sensitive import user_password, user_name

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s:[%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.WARNING,
    # filename='logs.txt',
)
logger = logging.getLogger("test_logger")
# logger.info('This will not show up')
# logger.warning('This will.')

PATH = "C:\Program Files (x86)\chromedriver.exe"

option = webdriver.ChromeOptions()
# option.add_argument("headless")
driver = webdriver.Chrome(PATH, options=option)

# driver = webdriver.Chrome(PATH)

driver.get("https://www1.link-elearning.com/linkdl/portal/signIn.php?hSajt=d279b124aa8dbdbc4efc1263f2c46ef9&notice=3")


class RecordSession:
    def __init__(self):
        self.uname = ''
        self.upass = ''

    def login(self):
        """
        Actions that will be made the first time the program will run, log in and take basic information
        """

        self.login_id = WebDriverWait(driver, 2).until(
            lambda x: x.find_element_by_xpath('//*[@id="username"]')
        )
        self.pass_id = WebDriverWait(driver, 2).until(
            lambda x: x.find_element_by_xpath('//*[@id="password"]')
        )
        self.submit_btn = WebDriverWait(driver, 2).until(
            lambda x: x.find_element_by_xpath('//*[@id="submit"]')
        )

        self.pass_id.send_keys(user_password)
        self.login_id.send_keys(user_name)
        self.submit_btn.send_keys(Keys.ENTER)

    def open_newest_live_class(self):
        self.newest_class = WebDriverWait(driver, 4).until(
            lambda x: x.find_element_by_xpath(
                '/html/body/div[2]/main/div/div/div[1]/div[1]/div/div[1]/div/div[2]/ul/li[1]/a'
            ))

        self.newest_class.click()
        self.play_btn = WebDriverWait(driver, 4).until(
            lambda x: x.find_element_by_xpath(
                '//*[@id="stream_dialog"]/div[7]'
            ))
        self.play_btn.click()


player = RecordSession()
player.login()
time.sleep(3)
player.open_newest_live_class()
