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