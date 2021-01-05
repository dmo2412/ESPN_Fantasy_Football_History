# link = 'https://fantasy.espn.com/football/league?leagueId=1016052'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import time
import os
from xlsxwriter import Workbook
import xlsxwriter as xw
from selenium.webdriver.common.action_chains import ActionChains
from collections import defaultdict
from passwords import *


class ModalPopup:
    def __init__(self,):
        self.driver = webdriver.Chrome(
            '/Users/dannymorgan/Downloads/chromedriver')
        self.driver.get(
            'https://fantasy.espn.com/football/league?leagueId=1016052')
        # self.driver.get('https://my.ny.gov/LoginV4/login.xhtml')
        sleep(8)

        secret = Password()
        self.espn_password = secret.espn_password
        self.email = secret.email
        # self.handle_modal()

    def handle_modal(self,):
        # popup = self.driver.find_element_by_xpath(
        #     "//form[@class='ng-pristine ng-invalid ng-invalid-required ng-valid-pattern']")
        # print(popup)
        # ele = self.driver.switch_to.active_element
        # ele = self.driver.find_element_by_css_selector("input[type='email']")
        # ele.send_keys('Danny')
        self.driver.switch_to.frame("disneyid-iframe")
        self.driver.find_element_by_css_selector(
            "input[type = 'email']").send_keys(self.email)
        self.driver.find_element_by_css_selector(
            "input[type = 'password']").send_keys(self.espn_password)
        login = self.driver.find_element_by_xpath(
            "//button[@class='btn btn-primary btn-submit ng-isolate-scope']")
        login.click()
        sleep(10)
        self.driver.switch_to.default_content()
        sleep(3)
        roster = self.driver.find_element_by_xpath("//a[@class='AnchorLink']")
        roster.click()

        # alert_obj = self.driver.switch_to.alert
        # try:
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Username or Email Address"]' ))
        # )
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.presence_of_element_located(
        #     (By.Placeholder, 'loginform:username')))
        # element = WebDriverWait.until(self.driver, 10)(
        #     EC.visibility_of_element_located((By.CLASS_NAME, 'did-ui-view'))
        # )
        # element.click()
        # finally:
        # element.send_keys('danny')


if __name__ == '__main__':
    modal = ModalPopup()
