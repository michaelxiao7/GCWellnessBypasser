#!/usr/bin/env python

"""It's simple. We all hate the Gordon Wellness check ROFL"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# DON'T SHARE THESE WITH OTHER PEOPLE!
USERNAME = "EDIT THIS VALUE" #first.last@gordon.edu
PASSWORD = "EDIT THIS VALUE"

def click_button():
    """The main function :D"""
    # Drivers
    driver = webdriver.Chrome(ChromeDriverManager().install())
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
    except:
        print("Something went wrong: Check your credentials or if your browser timed out")

click_button()
