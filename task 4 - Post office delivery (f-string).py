
import time

print("Hi, its a post office delivery automatic system", end="/n"), print("please follow  the rules for fluent detail entering")
time.sleep(3)

while True:
    _last_name = input("enter your last name in upper case")

    if not _last_name.upper():
        print("you dont fallow the rules, please enter your last name in upper case")
    else:
        _last_name = str(_last_name)
        _first_name = str(input("enter your first name in lower case"))
        while not _first_name.lower():
            print("we will finish tomorrow if you will not follow the rules, please enter your first name in upper case")
        else:
            _country = str(input("enter country must be only letters and more then 3 digits"))
            while not _country.isalpha() and len(_country) < 3:
                print("Hey")
                time.sleep(1)
                print("can all day do task that take 2 minutes")
                time.sleep(2)
                print("so..... follow rules")
            else:
                _cityaddress = str(input("enter your city address, no spicel requirments"))
            _zipcode = input("enter your zipcode, only digits allowed and more then 4 digits")
            while not _zipcode.isdigit() and len(_zipcode) < 4:
                print("Hey")
                time.sleep(1)
                print("you its the last detail dont you want to finish and go to eat?")
                time.sleep(1)

    print(f"{_last_name}, {_first_name}, {_country}, {_cityaddress}, {_zipcode}")








