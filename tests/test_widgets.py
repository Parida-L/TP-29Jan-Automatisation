import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import given, when, then, scenario
from selenium.webdriver import ActionChains

# Test Fixture
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# SCENARIO: Test the Tool Tips on the Widgets Page
@scenario('features/widgets.feature', 'Test the Tool Tips on the Widgets Page')
def test_tooltips():
    pass

@given('I am on the Tool Tips Page')
def tool_tips(browser):
    browser.get('https://demoqa.com/tool-tips')
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body")),
        message="DemoQA website is not accessible"
    )
    #Verify we are on the correct page and scroll to the title
    assert browser.title == "DEMOQA"
    title_element = browser.find_element(By.XPATH, '//*[@id="toopTipContainer"]/h1')
    browser.execute_script("arguments[0].scrollIntoView();", title_element)
    assert title_element.text == 'Tool Tips', "Title does not match"

@when('I hover over the Tool Tips')
def hover_tooltips(browser):
    action = ActionChains(browser)

    #Verify the button tooltip is accessible and scroll to it and hover over it
    button_tooltip = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="toolTipButton"]')),
        message="Button Tool Tip is not accessible"
    )
    browser.execute_script("arguments[0].scrollIntoView();", button_tooltip)
    action.move_to_element(button_tooltip).perform()
    time.sleep(1)

    #Verify the field tooltip is accessible and scroll to it and hover over it
    field_tooltip = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="toolTipTextField"]')),
        message="Field Tool Tip is not accessible"
    )
    browser.execute_script("arguments[0].scrollIntoView();", field_tooltip)
    action.move_to_element(field_tooltip).perform()
    time.sleep(1)

    # Verify tooltip message for first hyperlink and hover over it
    tooltip_text = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="texToolTopContainer"]/a[1]')),
        message="First Hyperlink Tool Tip is not accessible"
    )
    browser.execute_script("arguments[0].scrollIntoView();", tooltip_text)
    action.move_to_element(tooltip_text).perform()
    time.sleep(1)

    # Verify tooltip message for second hyperlink and hover over it
    tooltip_text_2 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="texToolTopContainer"]/a[2]')),
        message="Tooltip for second hyperlink is not displayed"
    )
    browser.execute_script("arguments[0].scrollIntoView();", tooltip_text_2)
    action.move_to_element(tooltip_text_2).perform()
    time.sleep(1)

@then('I should see the corresponding Tool Tips message')
def verify_tooltips(browser):
    action = ActionChains(browser)

    # Verify tooltip message for button
    action.move_to_element(browser.find_element(By.XPATH, '//*[@id="toolTipButton"]')).perform()
    time.sleep(1)
    # Verify tooltip message for button
    tooltip_text = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tooltip-inner')),
        message="Tooltip for button is not displayed"
    )
    assert tooltip_text.text == "You hovered over the Button", f"Unexpected tooltip message: {tooltip_text.text}"
    time.sleep(1)

    # Verify tooltip message for text field
    action.move_to_element(browser.find_element(By.XPATH, '//*[@id="toolTipTextField"]')).perform()
    time.sleep(1)
    # Verify tooltip message for text field
    tooltip_text = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tooltip-inner')),
        message="Tooltip for text field is not displayed"
    )
    assert tooltip_text.text == "You hovered over the text field", f"Unexpected tooltip message: {tooltip_text.text}"
    time.sleep(1)

    # Verify tooltip message for first hyperlink
    action.move_to_element(browser.find_element(By.XPATH, '//*[@id="texToolTopContainer"]/a[1]')).perform()
    time.sleep(1)
    # Verify tooltip message for first hyperlink
    tooltip_text = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tooltip-inner')),
        message="Tooltip for first hyperlink is not displayed"
    )
    assert tooltip_text.text == "You hovered over the Contrary", f"Unexpected tooltip message: {tooltip_text.text}"
    time.sleep(1)

    # Verify tooltip message for second hyperlink
    action.move_to_element(browser.find_element(By.XPATH, '//*[@id="texToolTopContainer"]/a[2]')).perform()
    time.sleep(1)
    # Verify tooltip message for second hyperlink
    tooltip_text = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'tooltip-inner')),
        message="Tooltip for second hyperlink is not displayed"
    )
    assert tooltip_text.text == "You hovered over the 1.10.32", f"Unexpected tooltip message: {tooltip_text.text}"
    time.sleep(1)

    