import test_main
"""!
@brief This is the main test file that runs in Github actions and is triggered using .github/workflows/python_tests.html
@see Solves [Issue#4](https://github.com/WSUCEG-7140/Team-Alpha/pull/27)
"""

def test_validate_string_on_success_1():
    """!
    @brief Testing String Validation with ab string
    """
    assert test_main.string_validation_on_success("ab") == True
    
def test_validate_string_on_success_2():
    """!
    @brief Testing String Validation with za string
    """
    assert test_main.string_validation_on_success("za") == True

def test_validate_string_on_failure_1():
    """!
    @brief Testing String Validation with zx string
    """
    assert test_main.string_validation_on_failure("zx") == True

def test_validate_string_on_failure_2():
    """!
    @brief Testing String Validation with aab string
    """
    assert test_main.string_validation_on_failure("aab") == True

def test_string_5():
    """!
    @brief Testing String Validation with AB string
    """
    assert test_main.string_validation_on_failure("AX") == True
    
def test_string_6():
    """!
    @brief Testing String Validation with 12 string
    """
    assert test_main.string_validation_on_failure("12") == True

def test_email_1():
    """!
    @brief Testing Email Validation with abc@gmail.com
    """
    assert test_main.email_validation_on_success("abc@gmail.com") == True

def test_email_2():
    """!
    @brief Testing Email Validation with XYZ@GMAIL.COM
    """
    assert test_main.email_validation_on_success("XYZ@GMAIL.COM") == True
    
def test_email_3():
    """!
    @brief Testing Email Validation with abc.com
    """
    assert test_main.email_validation_on_failure("abc.com") == True
  
def test_email_4():
    """!
    @brief Testing Email Validation with abc@redhat
    """
    assert test_main.email_validation_on_failure("abc@redhat") == True
    
def test_email_5():
    """!
    @brief Testing Email Validation with abc.com
    """
    assert test_main.email_validation_on_failure("@redhat.com") == True
    
def test_date_1():
    """!
    @brief Testing Date Validation with 07/13/2022 date.
    """
    assert test_main.date_validation_on_success("07/13/2022") == True
    
def test_date_2():
    """!
    @brief Testing Date Validation with 01/01/2000 date.
    """
    assert test_main.date_validation_on_success("01/01/2000") == True
    
def test_time_1():
    """!
    @brief Testing Time Functionality with 12:00 AM
    """
    assert test_main.time_validation_on_success("12:00AM") == True
    
def test_time_2():
    """!
    @brief Testing Time Functionality with 08:30 AM
    """
    assert test_main.time_validation_on_success("08:30AM") == True
    
def test_time_3():
    """!
    @brief Testing Time Functionality with 08:30 PM
    """
    assert test_main.time_validation_on_success("08:30PM") == True
    
def test_time_4():
    """!
    @brief Testing Time Functionality with 12:00 PM
    """
    assert test_main.time_validation_on_success("12:00PM") == True

def test_radio_button_1():
    """!
    @brief Testing Radio Functionality with Dog
    """
    assert test_main.radio_button_validation_on_success("Dog") == True
    
def test_radio_button_2():
    """!
    @brief Testing Radio Functionality with Cat
    """
    assert test_main.radio_button_validation_on_success("Cat") == True
 
def test_radio_button_3():
    """!
    @brief Testing Radio Functionality with Bird
    """
    assert test_main.radio_button_validation_on_success("Bird") == True
    
def test_radio_button_4():
    """!
    @brief Testing Radio Functionality on failure
    """
    assert test_main.radio_button_validation_on_failure() == True

def test_checkbox_1():
    """!
    @brief Testing Checkbox Functionality on failure
    """
    assert test_main.checkbox_validation_on_failure() == True

def test_checkbox_2():
    """!
    @brief Testing Checkbox Functionality on Success with Vehicle
    """
    assert test_main.checkbox_validation_on_success("Vehicle") == True

def test_checkbox_3():
    """!
    @brief Testing Checkbox Functionality on Success with Airplane
    """
    assert test_main.checkbox_validation_on_success("Airplane") == True
    
def test_checkbox_4():
    """!
    @brief Testing Checkbox Functionality on Success with Cruise
    """
    assert test_main.checkbox_validation_on_success("Cruise") == True
    
def test_checkbox_5():
    """!
    @brief Testing Checkbox Functionality on Success with Vehicle and Airplane
    """
    assert test_main.multiple_checkbox_validation_on_success("Vehicle","Airplane") == True
    
def test_checkbox_6():
    """!
    @brief Testing Checkbox Functionality on Success with All of them
    """
    assert test_main.checkbox_validation_on_success("ALL") == True
    
def test_range_1():
    """!
    @brief Testing Range Functionality on Success with 50 value.
    """
    assert test_main.range_validation_on_success("50") == True
    
def test_telephone_number_1():
    """!
    @brief Testing Telephone Number Functionality on Success with +1(456) 453 6574 value.
    """
    assert test_main.phone_number_validation_on_success("+1(456) 453 6574") == True
    
def test_telephone_number_2():
    """!
    @brief Testing Telephone Number Functionality on Success with +91(123) 456 7890 value.
    """
    assert test_main.phone_number_validation_on_success("+91(123) 456 7890") == True
    
def test_telephone_number_3():
    """!
    @brief Testing Telephone Number Functionality on Success with +1(TEL) COM 9999 value.
    """
    assert test_main.phone_number_validation_on_failure("+1(TEL) COM 9999") == True
    
def test_telephone_number_4():
    """!
    @brief Testing Telephone Number Functionality on Success with +1 @ 123 456 7890 value.
    """
    assert test_main.phone_number_validation_on_failure("+1 @ 123 456 7890") == True
    
def test_url_1():
    """!
    @brief Testing URL Functionality on Success with https://www.google.com value.
    """
    assert test_main.url_validation_on_success("https://www.google.com") == True
    
def test_url_2():
    """!
    @brief Testing URL Functionality on Success with https://www.bing.com value.
    """
    assert test_main.url_validation_on_success("https://www.bing.com") == True
    
def test_url_3():
    """!
    @brief Testing URL Functionality on Failure with google value.
    """
    assert test_main.url_validation_on_failure("google") == True
    
def test_reset_button():
    """!
    @brief Testing RESET Functionality.
    """
    assert test_main.reset_button_validation() == True
