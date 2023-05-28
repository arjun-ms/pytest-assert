
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Firefox()  # Change to the appropriate webdriver for your browser
    yield driver
    driver.quit()

def test_title(browser):
    browser.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    title = browser.find_element(By.TAG_NAME,"h1")
    title_text = title.text
    
    # Assert that the title of the page is "Simple Form"
    assert title_text == "Simple Form", "Page title is not as expected"

def test_sum(browser):
    browser.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    num1 = browser.find_element(By.XPATH, "//*[@id='sum1']")
    num1.send_keys("10")
    
    num2 = browser.find_element(By.XPATH, "//*[@id='sum2']")
    num2.send_keys("20")
    
    
    sum_element = browser.find_element(By.XPATH, "//*[@id='addmessage']")
   
    num1_value = num1.get_attribute('value')
    num2_value = num2.get_attribute('value')

    browser.find_element(By.XPATH,"//button[.='Get values']").click()
    if num1_value and num2_value:
        expected_sum = str(int(num1_value) + int(num2_value))
        assert sum_element.text == expected_sum, "Sum is not as expected"
    else:
        pytest.fail("Input fields are empty")