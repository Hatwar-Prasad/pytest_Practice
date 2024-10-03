# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# # @pytest.mark.regression
# @pytest.mark.parametrize("username,password",[("raj","raj1234"),("prasad","prasad1234"),("ram","rohit1234")]) # parameterized
# def test_testCase1(username,password):
#
#     print("this is simple test case1")
#     driver=webdriver.Chrome()
#     driver.get("https://www.facebook.com/")
#     driver.implicitly_wait(10)
#     # expectedTitle="Facebook – log in or sign up"   #assertion
#     # assert expectedTitle==driver.title
#     driver.find_element(By.ID,"email").send_keys(username)
#     driver.find_element(By.ID,"pass").send_keys(password)
#
#     time.sleep(5)
#
#
#
# # def test_testCase2():
# #     print("this is simple test case2")
# #
# #
# # def test_testCase3():
# #     print("this is simple test case3")