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

# SCENARIO: User can submit a form
@scenario('features/forms.feature', 'Test the Practice Form')
def test_practise_form():
    pass

@given('I am on the Practice Form Page')
def practice_form(browser):
    browser.get('https://demoqa.com/automation-practice-form')
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body")),
        message="DemoQA website is not accessible"
    )
    #Verify we are on the correct page and scroll to the title
    assert browser.title == "DEMOQA"
    title_element = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/h1')
    browser.execute_script("arguments[0].scrollIntoView();", title_element)
    assert title_element.text == 'Practice Form', "Title does not match"
    
@when('I fill in the form')
def fill_form(browser):
    #Verify the first name field is accessible and scroll to it
    firstName = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="firstName"]')),
        message="First Name field is not accessible"
    )        
    browser.execute_script("arguments[0].scrollIntoView();", firstName)
    # fill the first name field
    firstName.send_keys('John')

    #Verify the last name field is accessible 
    lastName = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="lastName"]')),
        message="Last Name field is not accessible"
    )
    # fill the last name field
    lastName.send_keys('J')

    #Verify the email field is accessible
    email = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="userEmail"]')),
        message="Email field is not accessible"
    )
    # fill the email field
    email.send_keys('john@j.com')

    #Verify the gender radio button is accessible
    radio_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]')),
        message="Gender radio button is not accessible"
    )
    # fill the email field
    radio_button.click()

    #Verify the mobile number field is accessible
    mobile_number = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="userNumber"]')),
        message="Mobile number field is not accessible"
    )
    browser.execute_script("arguments[0].scrollIntoView();", mobile_number)
    # fill the mobile number field
    mobile_number.send_keys('1234567890')

    #Verify the submit button is accessible
    submit_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="submit"]')),
        message="Submit button is not accessible"
    )
    # click the submit button
    submit_button.click()
    time.sleep(2)

@then('I have confirmation of registration')
def form_submitted(browser):
    # Wait for the confirmation message to appear
    confirmation = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="example-modal-sizes-title-lg"]')),
        message="Form was not submitted"
    )

    # Assert that the confirmation text is correct
    assert confirmation.text == 'Thanks for submitting the form', "Form was not submitted"

    # Wait for the table inside the modal
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="table-responsive"]')),
        message="Recap table did not appear"
    )

    # Assert that the submitted values appear in the table
    recap_data = {
        "Student Name": "John J",
        "Student Email": "john@j.com",
        "Gender": "Male",
        "Mobile": "1234567890"
    }

    # Check that the recap data in the modal matches the submitted values
    for key, expected_value in recap_data.items():
        cell_xpath = f"//td[contains(text(), '{key}')]/following-sibling::td"
        actual_value = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, cell_xpath))
        ).text
        # Assert that the actual value matches the expected value
        assert actual_value == expected_value, f"Expected {key} to be '{expected_value}', but got '{actual_value}'"