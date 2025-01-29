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

#SCENARIO 1 : API CALLS LINKS TEST
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
            time.sleep(1)  # Replace with explicit wait if necessary
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

#SCENARIO 2 : RADIO BUTTONS TEST
@scenario('features/elements.feature', 'Test The Radio Button')
def test_the_radio_button():
    pass

@given('I am on the Radio Button Elements page')
def i_am_on_the_radio_button_elements_page(browser):
    #Navigate to the demoqa.com/radio-button page
    browser.get('https://demoqa.com/radio-button')
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body")),
        message="DemoQA website is not accessible"
    )
    #Verify the page title
    assert browser.title == "DEMOQA"
    element = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[1]')
    browser.execute_script("arguments[0].scrollIntoView();", element)
    assert element.text == 'Do you like the site?', "Question does not match"
    assert browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/h1').text == 'Radio Button', "Header does not match"

@when('I select each Radio Button')
def i_select_each_radio_button(browser):
    #Click on YES
    radio_button_yes = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//label[@for="yesRadio"]'))
    )
    radio_button_yes.click()
    time.sleep(1)
    response_element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p')),
                message=f"Response for YES is not displayed"
            )
    assert response_element.text.startswith('You have selected'), f"Unexpected response: {response_element.text}"
    
    #Click on Impressive
    radio_button_imp = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//label[@for="impressiveRadio"]'))
    )
    radio_button_imp.click()
    time.sleep(1)
    response_element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p')),
                message=f"Response for Impressive is not displayed"
            )
    assert response_element.text.startswith('You have selected'), f"Unexpected response: {response_element.text}"

    #No button should not be clickable
    # Verify the element is present 
    radio_button_no = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//label[@for="noRadio"]')),
        message="No radio button label is not found"
    )

    # Try clicking and catch the error (element should not be clickable)
    try:
        radio_button_no.click()
        assert False, "No radio button should not be clickable, but it was clicked"
    except:
        pass  # Expected behavior, no need to handle further

@then('I should see the corresponding message except for No')
def i_should_see_the_corresponding_message_except_for_no(browser):
    # Verify the message for Yes radio button
    browser.find_element(By.XPATH, '//label[@for="yesRadio"]').click()
    #Verify the response is correct by checking the text
    response_element_yes = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p')),
                message=f"Response for YES is not displayed"
            )
    assert response_element_yes.text == 'You have selected Yes', f"Unexpected response: {response_element_yes.text}"
    # Verify the message for Impressive radio button
    browser.find_element(By.XPATH, '//label[@for="impressiveRadio"]').click()
    #Verify the response is correct by checking the text
    response_element_imp = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p')),
                message=f"Response for Impressive is not displayed"
            )
    assert response_element_imp.text == 'You have selected Impressive', f"Unexpected response: {response_element_imp.text}"
    
    # Verify the No radio button is disabled
    radio_button_no = browser.find_element(By.XPATH, '//label[@for="noRadio"]')
    assert 'disabled' in radio_button_no.get_attribute('class'), "No radio button is unexpectedly clickable"

#SCENARIO 3 : DYNAMIC PROPERTIES TEST
@scenario('features/elements.feature', 'Test The Dynamic Properties')
def test_the_dynamic_properties():
    pass

@given('I am on the Dynamic Properties Elements page')
def i_am_on_the_dynamic_properties_elements_page(browser):
    #Navigate to the demoqa.com/dynamic-properties page
    browser.get('https://demoqa.com/dynamic-properties')
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body")),
        message="DemoQA website is not accessible"
    )
    #Verify we are on the correct page and scroll to the title
    assert browser.title == "DEMOQA"
    title_element = browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/h1')
    browser.execute_script("arguments[0].scrollIntoView();", title_element)
    assert title_element.text == 'Dynamic Properties', "Header does not match"
    
@when('I wait 5 seconds')
def i_wait_5_seconds(browser):
    #Verify the button is present 
    button = WebDriverWait(browser, 1).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="colorChange"]')),
                message=f"Color Change button is not displayed"
            )
    #Scroll to the button
    browser.execute_script("arguments[0].scrollIntoView();", button)
    #Verify the button text color is not red
    assert 'mt-4 btn btn-primary' in button.get_attribute('class'), "No radio button is unexpectedly clickable"
    time.sleep(5)

@then('the text color of the color change button changes')
def the_text_color_of_the_color_change_button_changes(browser):
    #Verify the button is still present
    button = WebDriverWait(browser, 1).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="colorChange"]')),
                message=f"Color Change button is not displayed"
            )
    #Verify the button text color is red
    assert 'mt-4 text-danger btn btn-primary' in button.get_attribute('class'), "Color Change button text color did not change"