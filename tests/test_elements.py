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
    #CREATED
    browser.find_element(By.XPATH, '//a[.="Created"]').click()
    linkResponse = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="linkResponse"]')),
        message="Link response is not displayed"
    )
    assert linkResponse.text == 'Link has responded with staus 201 and status text Created', "Link response does not match"
    time.sleep(2)
    # #NO CONTENT
    browser.find_element(By.XPATH, '//*[@id="no-content"]').click()
    time.sleep(2)
    linkResponse = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="linkResponse"]')),
        message="Link response is not displayed"
    )
    assert linkResponse.text == 'Link has responded with staus 204 and status text No Content', "Link response does not match"
    #MOVED
    browser.find_element(By.XPATH, '//*[@id="moved"]').click()
    time.sleep(2)
    linkResponse = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="linkResponse"]')),
        message="Link response is not displayed"
    )
    assert linkResponse.text == 'Link has responded with staus 301 and status text Moved Permanently', "Link response does not match"
    #BAD REQUEST
    browser.find_element(By.XPATH, '//*[@id="bad-request"]').click()
    time.sleep(2)
    linkResponse = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="linkResponse"]')),
        message="Link response is not displayed"
    )
    assert linkResponse.text == 'Link has responded with staus 400 and status text Bad Request', "Link response does not match"
    #UNAUTHORIZED
    browser.find_element(By.XPATH, '//*[@id="unauthorized"]').click()
    time.sleep(2)
    linkResponse = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="linkResponse"]')),
        message="Link response is not displayed"
    )
    assert linkResponse.text == 'Link has responded with staus 401 and status text Unauthorized', "Link response does not match"
    #FORBIDDEN
    browser.find_element(By.XPATH, '//*[@id="forbidden"]').click()
    time.sleep(2)
    linkResponse = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="linkResponse"]')),
        message="Link response is not displayed"
    )
    assert linkResponse.text == 'Link has responded with staus 403 and status text Forbidden', "Link response does not match"
    #NOT FOUND
    browser.find_element(By.XPATH, '//*[@id="invalid-url"]').click()
    time.sleep(2)
    linkResponse = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="linkResponse"]')),
        message="Link response is not displayed"
    )
    assert linkResponse.text == 'Link has responded with staus 404 and status text Not Found', "Link response does not match"
