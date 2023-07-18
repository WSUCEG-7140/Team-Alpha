import test_main

def test_validate_string_on_success_1():
    ## Testing String Validation with ab string
    assert test_main.string_validation_on_success("ab") == True
    
def test_validate_string_on_success_2():
    ## Testing String Validation with za string
    assert test_main.string_validation_on_success("za") == True

def test_validate_string_on_failure_1():
    ## Testing String Validation with zx string
    assert test_main.string_validation_on_failure("zx") == True

def test_validate_string_on_failure_2():
    ## Testing String Validation with aab string
    assert test_main.string_validation_on_failure("aab") == True

def test_string_5():
    ## Testing String Validation with AB string
    assert test_main.string_validation_on_failure("AX") == True
    
def test_string_6():
    ## Testing String Validation with 12 string
    assert test_main.string_validation_on_failure("12") == True

def test_email_1():
    ## Testing Email Validation with abc@gmail.com
    assert test_main.email_validation_on_success("abc@gmail.com") == True

def test_email_2():
    ## Testing Email Validation with XYZ@GMAIL.COM
    assert test_main.email_validation_on_success("XYZ@GMAIL.COM") == True
    
def test_email_3():
    ## Testing Email Validation with abc.com
    assert test_main.email_validation_on_failure("abc.com") == True
  
def test_email_4():
    ## Testing Email Validation with abc@redhat
    assert test_main.email_validation_on_failure("abc@redhat") == True
    
def test_email_5():
    ## Testing Email Validation with abc.com
    assert test_main.email_validation_on_failure("@redhat.com") == True
    
def test_date_1():
    ##Testing Date Validation with 07/13/2022 date.
    assert test_main.date_validation_on_success("07/13/2022") == True
    
def test_date_2():
    ##Testing Date Validation with 01/01/2000 date.
    assert test_main.date_validation_on_success("01/01/2000") == True
    
def test_time_1():
    ##Testing Time Functionality with 12:00 AM
    assert test_main.time_validation_on_success("12:00AM") == True
    
def test_time_2():
    ##Testing Time Functionality with 08:30 AM
    assert test_main.time_validation_on_success("08:30AM") == True
    
def test_time_3():
    ##Testing Time Functionality with 08:30 PM
    assert test_main.time_validation_on_success("08:30PM") == True
    
def test_time_4():
    ##Testing Time Functionality with 12:00 PM
    assert test_main.time_validation_on_success("12:00PM") == True
