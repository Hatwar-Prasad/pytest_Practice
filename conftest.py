import pytest
from selenium import webdriver
import time


# @pytest.fixture(params=["chrome","edge"])
@pytest.fixture(params=["chrome"])
def setup_and_teardown(request):
    global driver
    if request.param=="chrome":
        driver = webdriver.Chrome()
    # elif request.param=="edge":
    #     driver=webdriver.Edge()

    driver.get("https://www.facebook.com/")
    driver.implicitly_wait(10)

    request.cls.driver=driver

    yield
    time.sleep(3)
    driver.quit()
    print("end of execution")