import pytest
import sys
import json
import matplotlib
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

#Fetching required field from alert Json.
def fetch_string(text, search):
    with open("data_file.json", "w") as write_file:
        print(text, file=write_file)
    data = json.load(open("data_file.json"))
    z = data[search]
    return z

#Validating String on Success testing both functionalities - getdata and validate.
def string_validation_on_success(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html#4')
    chrome_driver.maximize_window()
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    element1 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element1.send_keys(input1)
    sleep(3)
    link2 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link2.click()
    sleep(1)
    
    #Phase - 1: Testing Getdata Functionality.
    alert = Alert(chrome_driver)
    required_string = "s1"
    validated_string = fetch_string(alert.text,required_string)
    assert input1 == validated_string
    print ("String data matched.")
    sleep(3) 
        
    #Phase - 2: Testing Validate Functionality on Success.
    alert.accept()
    link3 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[2]")
    link3.click()
    sleep(1)
    alert = Alert(chrome_driver)
    required_string = "Validation succeeded"
    assert required_string == alert.text
    print ("Retrieved Success Alert with" + input1 + "as input")
    sleep(1)
    chrome_driver.quit()
    return True

#Validating String on Failure testing both functionalities - getdata and validate.
def string_validation_on_failure(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html#4')
    chrome_driver.maximize_window()
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    element1 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element1.send_keys(input1)
    sleep(3)
    link2 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link2.click()
    sleep(1)
        
    #Phase - 1: Testing Getdata Functionality.
    alert = Alert(chrome_driver)
    required_string = "s1"
    validated_string = fetch_string(alert.text,required_string)
    assert input1 == validated_string
    print ("String data matched.")
    sleep(3) 
    alert.accept()
    link3 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[2]")
    link3.click()
    sleep(1)
       
    #Phase - 2: Testing Validate Functionality on Failure.
    required_string = "Validation error"
    link4 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']").get_attribute("data-original-title")
    assert required_string == link4
    print ("Retrieved Failure Alert with" + input1 + "as input")
    sleep(1)
    chrome_driver.quit()
    return True
