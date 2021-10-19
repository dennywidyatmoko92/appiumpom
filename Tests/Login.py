from appium import webdriver
import time
import unittest
import sys
import os
from SampleProjects.Pages.loginPage import LoginPage
from SampleProjects.TestData.TestData import TestDatasbs

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desire_cap = {
            "platformName": "android",
            "platformVersion": "10.0.0",
            "deviceName": "MGMRK19109013419",
            "appPackage": "com.sebangsa.sebangsa",
            "appActivity": "com.sebangsa.sebangsa.SplashScreenActivity"
        }
        cls.webdriver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
        cls.webdriver.implicitly_wait(10)

    def test_login(self):
        webdriver = self.webdriver
        login = LoginPage(webdriver)
        login.click_signin()
        login.enter_username(TestDatasbs.username)
        login.enter_password(TestDatasbs.password)
        login.click_masuk()


    @classmethod
    def tearDownClass(self):
        self.webdriver.quit()


