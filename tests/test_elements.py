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
@scenario('features/elements.feature', 'Test all API calls links')
def test_all_api_calls_links():
    pass

@given('I am on the Links Elements page')
def i_am_on_the_links_elements_page(browser):
    #Navigate to the demoqa.com/links page
    browser.get('https://demoqa.com/links')
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body")),
        message="DemoQA website is not accessible"
    )
    #Verify the page title
    assert browser.title == "DEMOQA"
    element = browser.find_element(By.XPATH, '//strong[.="Following links will send an api call"]')
    browser.execute_script("arguments[0].scrollIntoView();", element)
    assert element.text == 'Following links will send an api call', "Header does not match"

@when('I test all API calls links')
def i_test_all_the_api_calls_links(browser):
        # Refactorisation as all api links have same structure as below : 
        # browser.find_element(By.XPATH, '//*[@id="created"]').click()
        # linkResponse = WebDriverWait(browser, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="linkResponse"]')),
        #     message="Link response is not displayed"
        # )
        # assert linkResponse.text == 'Link has responded with staus 201 and status text Created', "Link response does not match"
        # time.sleep(2)

        # Dictionary to store responses for validation (and use after for the THEN)
        global link_responses  
        link_responses = {}

        # Dictionary of link IDs and expected responses
        links_to_test = {
            "created": "Link has responded with staus 201 and status text Created",
            "no-content": "Link has responded with staus 204 and status text No Content",
            "moved": "Link has responded with staus 301 and status text Moved Permanently",
            "bad-request": "Link has responded with staus 400 and status text Bad Request",
            "unauthorized": "Link has responded with staus 401 and status text Unauthorized",
            "forbidden": "Link has responded with staus 403 and status text Forbidden",
            "invalid-url": "Link has responded with staus 404 and status text Not Found",
        }

        # Loop through each link, click it, and store the response
        for link_id, expected_text in links_to_test.items():
            browser.find_element(By.XPATH, f'//*[@id="{link_id}"]').click()
            time.sleep(2)  # Replace with explicit wait if necessary
            response_element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="linkResponse"]')),
                message=f"Response for {link_id} is not displayed"
            )
            link_responses[link_id] = response_element.text  # Store response for validation

@then('I should receive the corresponding status code')
def i_should_receive_the_corresponding_status_code():
    # Dictionary of expected responses
    expected_responses = {
        "created": "Link has responded with staus 201 and status text Created",
        "no-content": "Link has responded with staus 204 and status text No Content",
        "moved": "Link has responded with staus 301 and status text Moved Permanently",
        "bad-request": "Link has responded with staus 400 and status text Bad Request",
        "unauthorized": "Link has responded with staus 401 and status text Unauthorized",
        "forbidden": "Link has responded with staus 403 and status text Forbidden",
        "invalid-url": "Link has responded with staus 404 and status text Not Found",
    }

    # Validate the responses
    for link_id, expected_text in expected_responses.items():
        assert link_responses[link_id] == expected_text, f"Mismatch for {link_id}: {link_responses[link_id]}"
