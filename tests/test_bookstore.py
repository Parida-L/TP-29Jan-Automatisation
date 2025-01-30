import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import given, when, then, scenario
# Import the generate_unique_username function from the username_generator module
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.username_generator import generate_unique_username
from utils.password_generator import generate_secure_password
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

# Test Fixture
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# SCENARIO: 
@scenario('features/bookstore.feature', 'Create a user in the bookstore')
def test_tooltips():
    pass

@given('I navigate to the DemoQA website bookstore')
def navigate_to_bookstore(browser):
    # Open the DemoQA website bookstore 
    browser.get('https://demoqa.com/books')
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body")),
        message="DemoQA website is not accessible"
    )
    #Verify we are on the correct page and scroll to the bookstore section
    assert browser.title == "DEMOQA"
    bookstore_element = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[6]/span/div/div[1]')
    browser.execute_script("arguments[0].scrollIntoView();", bookstore_element)
     # Find and click on the Login section
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]')),
        message="Login button is not clickable"
    )
    login_button.click()
    time.sleep(2)

    # Wait until the login page is loaded and verify it
    login_page_title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/h1')),
        message="Login page did not load"
    )
    browser.execute_script("arguments[0].scrollIntoView();", login_page_title)
    assert login_page_title.text == "Login", "Login page title is incorrect"

@when('I create a new user')
def create_new_user(browser):
    # Navigate to the Register section
    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="newUser"]')),
        message="Register button is not clickable"
    )
    browser.execute_script("arguments[0].scrollIntoView();", register_button)
    register_button.click()
    time.sleep(1)
    # Verify we are on the Register page
    register_page_title = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/h1')),
        message="Register page did not load"
    )
    assert register_page_title.text == "Register", "Register page title is incorrect"
    # Fill in the registration form
    first_name = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="firstname"]')),
        message="First name field is not clickable"
    )
    first_name.send_keys("John")
    # Fill in the last name
    last_name = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="lastname"]')),
        message="Last name field is not clickable"
    )
    last_name.send_keys("J")
    # Generate a unique username
    unique_username = generate_unique_username()
    # Fill in the username
    username_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="userName"]')),
        message="Username field is not clickable"
    )
    username_input.send_keys(unique_username)
    # Fill in the password
    unique_password = generate_secure_password()
    password_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')),
        message="Password field is not clickable"
    )
    password_input.send_keys(unique_password)
    #Wait time to fill the capcha manually
    time.sleep(30)
    # Click on the Register button
    register_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="register"]')),
        message="Register button is not clickable"
    )
    browser.execute_script("arguments[0].scrollIntoView();", register_button)
    register_button.click()
    time.sleep(2)

@then('the user is created successfully')
def user_created(browser):
    # Wait for and handle the alert confirmation message
    WebDriverWait(browser, 5).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    assert alert.text == "User Register Successfully.", f"❌ Alert message incorrect: '{alert.text}'"
    alert.accept()