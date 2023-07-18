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

#Validating 2 different date formats.
def validate_different_date_format(format1, format2):
    #format1 --> 07/13/2022
    #format2 --> 2022-07-13
    format1_array = format1.split("/")
    format2_array = format2.split("-")
    if format1_array[0] == format2_array[1] and format1_array[1] == format2_array[2] and format1_array[2] == format2_array[0]:
        return True
    else:
        return False
        
#Validating 24HR time formats.
def validate_different_time_format(format1, format2):
    #format1 --> 09:30PM
    #format2 --> 21:30
    add_hours = 0
    base_format = format1
    if "PM" in format1:
        add_hours = 12
    format1 = format1.replace("AM","")
    format1 = format1.replace("PM","")
    format1_array = format1.split(":")
    format2_array = format2.split(":")
    
    if int(format1_array[0]) == 12 and "PM" in base_format:
        format1_array[0] = 12
    elif int(format1_array[0]) == 12 and "AM" in base_format:
        format1_array[0] = 0
    else:   
        format1_array[0] = int(format1_array[0]) + add_hours

    if int(format1_array[1]) == int(format2_array[1]) and int(format1_array[0]) == int(format2_array[0]):
        return True
    else:
        return False


#Validating String on Success testing both functionalities - getdata and validate.
def string_validation_on_success(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("String validation")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    element1 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element1.send_keys(input1)
    link2 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link2.click()
    sleep(1)
    
    #Phase - 1: Testing Getdata Functionality.
    alert = Alert(chrome_driver)
    required_string = "s1"
    validated_string = fetch_string(alert.text,required_string)
    assert input1 == validated_string
    print ("String data matched.")
    sleep(1) 
        
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
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("String validation")    
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    element1 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element1.send_keys(input1)
    link2 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link2.click()
    sleep(1)
        
    #Phase - 1: Testing Getdata Functionality.
    alert = Alert(chrome_driver)
    required_string = "s1"
    validated_string = fetch_string(alert.text,required_string)
    assert input1 == validated_string
    print ("String data matched.")
    sleep(1) 
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

#Validating Email on Success testing both functionalities - getdata and validate.
def email_validation_on_success(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("Additional input type format")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    password_dummy = "string"
    element1 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element1.send_keys(password_dummy)
    element2 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_1']")
    element2.send_keys(input1)
    date_dummy = "07/13/2023"
    element3 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_2']")
    element3.send_keys(date_dummy)
    time_dummy = "16:36:44.000000000"
    element4 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_3']")
    element4.send_keys(time_dummy)
    sleep(1)
    link2 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link2.click()
    sleep(1)
    
    #Phase - 1: Testing Getdata Functionality.
    alert = Alert(chrome_driver)
    required_string = "email"
    validated_string = fetch_string(alert.text,required_string)
    assert input1 == validated_string
    print ("Email data matched.")
    sleep(1) 
        
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
    
#Validating Email on Failure testing both functionalities - getdata and validate.
def email_validation_on_failure(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("Additional input type format")    
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    password_dummy = "string"
    element1 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element1.send_keys(password_dummy)
    element2 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_1']")
    element2.send_keys(input1)
    date_dummy = "07/13/2023"
    element3 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_2']")
    element3.send_keys(date_dummy)
    time_dummy = "16:36:44.000000000"
    element4 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_3']")
    element4.send_keys(time_dummy)
    link2 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link2.click()
    sleep(1)
    
    #Phase - 1: Testing Getdata Functionality.
    alert = Alert(chrome_driver)
    required_string = "email"
    validated_string = fetch_string(alert.text,required_string)
    assert input1 == validated_string
    print ("Email data matched.")
    alert.accept()
    sleep(1)
    link3 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[2]")
    link3.click()
    sleep(1)    
        
    #Phase - 2: Testing Validate Functionality on Failure.
    required_string = "Validation error"
    link4 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_1']").get_attribute("data-original-title")
    print (link4)
    assert required_string == link4
    print ("Retrieved Failure Alert with" + input1 + "as input")
    sleep(1)
    chrome_driver.quit()
    return True
    
    
#Validating date on Success testing both functionalities - getdata and validate.
def date_validation_on_success(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("Additional input type format")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    password_dummy = "string"
    element1 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element1.send_keys(password_dummy)
    email_dummy = "abc@gmail.com"
    element2 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_1']")
    element2.send_keys(email_dummy)
    element3 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_2']")
    element3.send_keys(input1)
    time_dummy = "16:36:44.000000000"
    element4 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_3']")
    element4.send_keys(time_dummy)
    link2 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link2.click()
    sleep(1)
    
    #Phase - 1: Testing Getdata Functionality.
    alert = Alert(chrome_driver)
    required_string = "date"
    validated_string = fetch_string(alert.text,required_string)
    #assert input1 == validated_string
    assert validate_different_date_format(input1, validated_string) == True
    print ("Date data matched.")
    sleep(1) 
        
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

#Validating Time on Success testing both functionalities - getdata and validate.
def time_validation_on_success(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("Additional input type format")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    password_dummy = "string"
    element1 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element1.send_keys(password_dummy)
    email_dummy = "abc@gmail.com"
    element2 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_1']")
    element2.send_keys(email_dummy)
    date_dummy = "07/13/2023"
    element3 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_2']")
    element3.send_keys(date_dummy)
    element4 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_3']")
    element4.send_keys(input1)
    link2 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link2.click()
    sleep(1)
    
    #Phase - 1: Testing Getdata Functionality.
    alert = Alert(chrome_driver)
    required_string = "time"
    validated_string = fetch_string(alert.text,required_string)
    #assert input1 == validated_string
    assert validate_different_time_format(input1, validated_string) == True
    print ("Time data matched.")
    sleep(1)
        
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

#Validating Radio Button on Success.
def radio_button_validation_on_success(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("Radio button and checkbox")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    Variable =  "//*[@id='Search']"
    Variable = Variable.replace("Search",input1)
    link2 = chrome_driver.find_element(By.XPATH, Variable)
    link2.click()
    link3 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_1']/input[1]")
    link3.click()
    sleep(1)
    link4 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link4.click()
    sleep(1)

    alert = Alert(chrome_driver)
    required_string = "radio1"
    validated_string = fetch_string(alert.text,required_string)
    assert input1 == validated_string
    print ("Radio data matched.")
    sleep(1)
        
    #Phase - 2: Testing Validate Functionality on Success.
    alert.accept()
    link5 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[2]")
    link5.click()
    sleep(1)
    alert = Alert(chrome_driver)
    required_string = "Validation succeeded"
    assert required_string == alert.text
    print ("Retrieved Success Alert with" + input1 + "as input")
    sleep(1)
    chrome_driver.quit()
    return True
    
#Validating Checkbox on Success.
def checkbox_validation_on_success(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("Radio button and checkbox")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    link2 = chrome_driver.find_element(By.XPATH, "//*[@id='Dog']")
    link2.click()
    if input1 == "ALL":
        chrome_driver.find_element(By.NAME, "Vehicle").click()
        chrome_driver.find_element(By.NAME, "Airplane").click()
        chrome_driver.find_element(By.NAME, "Cruise").click()
    else:
        link3 = chrome_driver.find_element(By.NAME, input1)
        link3.click()
    sleep(1)
    link4 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link4.click()
    sleep(1)

    alert = Alert(chrome_driver)
    required_string = "checkbox"
    validated_string = fetch_string(alert.text,required_string)
    if input1 == "ALL":
        assert "Vehicle" == validated_string[0]
        assert "Airplane" == validated_string[1]
        assert "Cruise" == validated_string[2]
    else:
        assert input1 == validated_string[0]
    print ("Checkbox data matched.")
    sleep(1)
        
    #Phase - 2: Testing Validate Functionality on Success.
    alert.accept()
    link5 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[2]")
    link5.click()
    sleep(1)
    alert = Alert(chrome_driver)
    required_string = "Validation succeeded"
    assert required_string == alert.text
    print ("Retrieved Success Alert with" + input1 + "as input")
    sleep(1)
    chrome_driver.quit()
    return True
    
#Validating Multiple Checkbox on Success.
def multiple_checkbox_validation_on_success(input1,input2):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("Radio button and checkbox")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    link2 = chrome_driver.find_element(By.XPATH, "//*[@id='Dog']")
    link2.click()
    link3 = chrome_driver.find_element(By.NAME, input1)
    link3.click()
    link4 = chrome_driver.find_element(By.NAME, input2)
    link4.click()
    sleep(1)
    link5 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link5.click()
    sleep(1)

    alert = Alert(chrome_driver)
    required_string = "checkbox"
    validated_string = fetch_string(alert.text,required_string)
    assert input1 == validated_string[0]
    assert input2 == validated_string[1]
    print ("Checkbox data matched.")
    sleep(1)
        
    #Phase - 2: Testing Validate Functionality on Success.
    alert.accept()
    link6 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[2]")
    link6.click()
    sleep(1)
    alert = Alert(chrome_driver)
    required_string = "Validation succeeded"
    assert required_string == alert.text
    print ("Retrieved Success Alert with" + input1 + "as input")
    sleep(1)
    chrome_driver.quit()
    return True

#Validating Range Button on Success.
def range_validation_on_success(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("Range input type")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    link3 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link3.click()
    sleep(1)

    alert = Alert(chrome_driver)
    required_string = "range"
    validated_string = fetch_string(alert.text,required_string)
    assert input1 == validated_string
    print ("Range data matched.")
    sleep(1)
        
    #Phase - 2: Testing Validate Functionality on Success.
    alert.accept()
    link5 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[2]")
    link5.click()
    sleep(1)
    alert = Alert(chrome_driver)
    required_string = "Validation succeeded"
    assert required_string == alert.text
    print ("Retrieved Success Alert with" + input1 + "as input")
    sleep(1)
    chrome_driver.quit()
    return True
    
#Validating Phone Number Button on Success.
def phone_number_validation_on_success(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("Phone number input type")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    element = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element.send_keys(input1)  
    link3 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link3.click()
    sleep(1)

    alert = Alert(chrome_driver)
    required_string = "telephone_number"
    validated_string = fetch_string(alert.text,required_string)
    assert input1 == validated_string
    print ("Telephone Number data matched.")
    sleep(1)
        
    #Phase - 2: Testing Validate Functionality on Success.
    alert.accept()
    link5 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[2]")
    link5.click()
    sleep(1)
    alert = Alert(chrome_driver)
    required_string = "Validation succeeded"
    assert required_string == alert.text
    print ("Retrieved Success Alert with" + input1 + "as input")
    sleep(1)
    chrome_driver.quit()
    return True
    
#Validating Phone Number Button on Failure.
def phone_number_validation_on_failure(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("Phone number input type")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    element = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element.send_keys(input1)  
    link3 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[2]")
    link3.click()
    sleep(1)

    required_string = "Validation error"
    link4 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']").get_attribute("data-original-title")
    print (link4)
    assert required_string == link4
    print ("Retrieved Failure Alert")
    sleep(1)
    chrome_driver.quit()
    return True
    
#Validating URL Type on Success.
def url_validation_on_success(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("URL input type example")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    element = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element.send_keys(input1)  
    link3 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[1]")
    link3.click()
    sleep(1)

    alert = Alert(chrome_driver)
    required_string = "url"
    validated_string = fetch_string(alert.text,required_string)
    assert input1 == validated_string
    print ("URL data matched.")
    sleep(1)
        
    #Phase - 2: Testing Validate Functionality on Success.
    alert.accept()
    link5 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[2]")
    link5.click()
    sleep(1)
    alert = Alert(chrome_driver)
    required_string = "Validation succeeded"
    assert required_string == alert.text
    print ("Retrieved Success Alert with" + input1 + "as input")
    sleep(1)
    chrome_driver.quit()
    return True
    
#Validating URL Type on Failure.
def url_validation_on_failure(input1):
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('D:/a/Team-Alpha/Team-Alpha/index.html')
    chrome_driver.maximize_window()
    link = chrome_driver.find_element(By.XPATH, "//*[@id='examples']")
    link.send_keys("URL input type example")
    link1 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseInput']/div/button")
    link1.click()
    sleep(1)
    element = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']")
    element.send_keys(input1)  
    link3 = chrome_driver.find_element(By.XPATH, "//*[@id='collapseForm']/div/div[3]/button[2]")
    link3.click()
    sleep(1)

    required_string = "Validation error"
    link4 = chrome_driver.find_element(By.XPATH, "//*[@id='BrutusinForms#0_0']").get_attribute("data-original-title")
    print (link4)
    assert required_string == link4
    print ("Retrieved Failure Alert")
    sleep(1)
    chrome_driver.quit()
    return True