#!/usr/bin/env python3

"""It's simple. We all hate the Gordon Wellness check ROFL"""

import time
import schedule
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# DON'T SHARE THESE WITH OTHER PEOPLE!
USERNAME = "WRITE YOUR USERNAME INSIDE THESE QUOTES"
PASSWORD = "WRITE YOUR PASSWORD INSIDE THESE QUOTES"
RETRY = 0

def click_button():
    """The main function :D"""
    # Drivers
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_position(-10000, 10000)
    driver.set_page_load_timeout("5")
    driver.get("https://360.gordon.edu/")
    try:
        # Log in with test software
        driver.find_element_by_xpath("(//input[@id='username'])").send_keys(USERNAME)
        driver.find_element_by_xpath("(//input[@id='password'])").send_keys(PASSWORD)
        time.sleep(1)
        driver.find_element_by_xpath("//span[text()='Log in']").click()
        time.sleep(1)

        # click radio button
        driver.find_element_by_xpath("//input[@type='radio' and @value='No']").click()
        time.sleep(1)

        # Click submit button
        driver.find_element_by_xpath("//span[text()='Submit']").click()
        time.sleep(1)
        driver.quit()
        RETRY = 0
    except:
        if retry < 2:
            click_button()
            RETRY+=1

schedule.every().day.at("07:00:02").do(click_button) #You can change this time to whatever you would like (HH:MM:SS)

while True:
    schedule.run_pending()
    time.sleep(1)
