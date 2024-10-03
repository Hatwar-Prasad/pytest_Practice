import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_LoginPage:

# @pytest.mark.regression
    @pytest.mark.parametrize("username,password",
                         [("raj", "raj1234"), ("prasad", "prasad1234"), ("rohit", "rohit1234")])  # parameterized
    def test_login(self,setup_and_teardown,username, password):
        print("this is login test case")

    # expectedTitle="Facebook – log in or sign up"   #assertion
    # assert expectedTitle==driver.title
        self.driver.find_element(By.ID, "email").send_keys(username)
        self.driver.find_element(By.ID, "pass").send_keys(password)




    def test_create_newAccount(self,setup_and_teardown):
        print("this is create new account test case")

        self.driver.find_element(By.LINK_TEXT, "Create new account").click()

