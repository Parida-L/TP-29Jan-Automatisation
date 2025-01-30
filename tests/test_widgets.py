import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytest_bdd import given, when, then, scenario
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

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

# SCENARIO: Test Select Menu on the Widgets Page
@scenario('features/widgets.feature', 'Test Select Menu on the Widgets Page')
def test_select_menu():
    pass

@given('I navigate to the select menu widget')
def select_menu(browser):
    browser.get('https://demoqa.com/select-menu')
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body")),
        message="DemoQA website is not accessible"
    )
    #Verify we are on the correct page and scroll to the title
    assert browser.title == "DEMOQA"
    title_element = browser.find_element(By.XPATH, '//*[@id="selectMenuContainer"]/h1')
    browser.execute_script("arguments[0].scrollIntoView();", title_element)
    assert title_element.text == 'Select Menu', "Title does not match"

@when('I select "Option 1" in the "Select value" dropdown')
def select_another_root_option(browser):
    # Select the "Select value" dropdown
    select_value_dropdown_locator = (By.XPATH, "//*[@id='withOptGroup']/div/div[1]")
    select_value_dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(select_value_dropdown_locator),
        message="Select value dropdown is not found on the page"
    )
    select_value_dropdown.click()
    time.sleep(1)
    # Select the Option 1 (Another root option) from the dropdown
    another_root_option_locator = (By.ID, "react-select-2-option-3")  
    another_root_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(another_root_option_locator),
        message="Another root option is not found in the dropdown"
    )
    browser.execute_script("arguments[0].scrollIntoView(true);", another_root_option)
    time.sleep(1)
    another_root_option.click()
    

@when('I select "Option 2" in the "Select one" dropdown')
def select_other_option(browser):
    # Select the "Select one" dropdown
    select_one_dropdown_locator = (By.XPATH, '//*[@id="selectOne"]/div/div[1]')
    select_one_dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(select_one_dropdown_locator),
        message="Select one dropdown is not found on the page"
    )
    time.sleep(1)
    select_one_dropdown.click()
    time.sleep(1)
    # Select the Option 2 (Other) from the dropdown
    other_option_locator = (By.XPATH, '//div[@id="selectOne"]/div[2]/div/div/div[2]/div[6]')  
    other_option = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(other_option_locator),
        message="Other option is not found in the dropdown"
    )
    time.sleep(1)
    other_option.click()

@when('I select "Option 3" in "Old Style Select Menu" dropdown')
def select_aqua_option(browser):
    # Select the "Old Style Select Menu" dropdown
    old_style_select_menu_locator = (By.ID, "oldSelectMenu")
    old_style_select_menu = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(old_style_select_menu_locator),
        message="Old Style Select Menu dropdown is not found on the page"
    )
    # Use the Select class to interact with the dropdown
    select_menu = Select(old_style_select_menu)  # Initialize Select on the <select> element
    time.sleep(1)
    select_menu.select_by_visible_text("Aqua")  # Select the "Aqua" option by visible text
    time.sleep(1)

@when('I select all options in "Multi Select Drop Down" dropdown')
def select_all_colors_option(browser):
    # Select the "Multi Select Drop Down" dropdown
    multi_select_dropdown_locator = (By.XPATH, '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[1]')
    multi_select_dropdown = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(multi_select_dropdown_locator),
        message="Multi Select Drop Down is not found on the page"
    )
    time.sleep(1)
    multi_select_dropdown.click()
    
    # List of options to select (Red, Black, Green, Blue)
    color_options = {
        "Blue": "react-select-4-option-0",
        "Green": "react-select-4-option-1",
        "Red": "react-select-4-option-2",
        "Black": "react-select-4-option-3",
    }
    # Select each color option from the dropdown
    for color, option_id in color_options.items():
        option_locator = (By.ID, option_id)
        option = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(option_locator),
            message=f"{color} option is not found in the dropdown"
        )
        time.sleep(1)  # Delay to prevent issues with dropdown closing
        option.click()

@when('I select "Option 4" in "Standard multi select"')
def select_option_4(browser):
    #Verify the standard multi select dropdown is accessible
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cars"]')),
        message="Standard multi select is not found on the page"
    )
    # Select the Option 4 from the selection list
    option_4_locator = (By.XPATH, "//*[@id='cars']/option[4]")  
    option_4 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(option_4_locator),
        message="Option 4 is not found in the dropdown"
    )
    time.sleep(1)
    option_4.click()

@then('the selected values should be displayed')
def verify_selected_values(browser):
    #Verify Select Value
    select_value_selected = browser.find_element(By.XPATH, '//*[@id="withOptGroup"]/div/div[1]/div[1]')
    assert select_value_selected.text == "Another root option", f"Expected selected value to be 'Another root option', but got '{select_value_selected.text}'"
    
    #Verify Select One
    select_one_selected = browser.find_element(By.XPATH, '//*[@id="selectOne"]/div/div[1]/div[1]')
    assert select_one_selected.text == "Other", f"Expected selected value to be 'Other', but got '{select_one_selected.text}'"

    #Verify Old Style Select Menu
    old_style_select_menu = browser.find_element(By.ID, "oldSelectMenu")
    select_menu = Select(old_style_select_menu) # Initialize Select on the <select> element
    # Assert the selected option is "Aqua"
    selected_option = select_menu.first_selected_option
    assert selected_option.text == "Aqua", f"Expected selected value to be 'Aqua', but got '{selected_option.text}'"

    # Dictionary of selected colors with their corresponding XPATHs
    selected_colors = {
        "Blue": '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[1]/div[2]/div/div[1]',
        "Black": '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[1]/div[3]/div/div[1]',
        "Red": '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[1]/div[4]/div/div[1]',
        "Green": '//*[@id="selectMenuContainer"]/div[7]/div/div/div/div[1]/div[1]/div/div[1]'
    }
    # Loop through each color in the multi-select dropdown
    for color, xpath in selected_colors.items():
        element = browser.find_element(By.XPATH, xpath)
        # Assert that the selected text matches the expected color
        assert element.text == color, f"❌ ERROR: Expected '{color}',but got'{element.text}'"
