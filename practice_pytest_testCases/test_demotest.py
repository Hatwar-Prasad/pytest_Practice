import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_ForgottenAccount:


    def test_forgottenAccount_Btn(self,setup_and_teardown):
        self.driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
        print("Forgotten Account test case")
