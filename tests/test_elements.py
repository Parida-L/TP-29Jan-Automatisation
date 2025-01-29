import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import given, when, then, scenario

# Test Fixture
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

#Scenario 1 : 
@scenario('features/elements.feature', 'Open a new tab and close it')
def test_manage_windows_and_tabs(browser):
    pass 
