
import time
import datetime

print("Hi, its a post office delivery automatic system", end="/n"), print("please follow the rules for fluent detail entering")
time.sleep(3)

while True:
    _last_name = input("enter your last name in upper case")
    if _last_name.isupper():
        break
_last_name = str(_last_name)
while True:
    _first_name = input("enter your first name in lower case")
    if _first_name.islower():
        break
_first_name = str(_first_name)
while True:
    _country = input("enter country must be only letters and more then 3 digits")
    if _country.isalpha() and len(_country) > 3:
        break
_country = str(_country)

_cityaddress = input("enter your city address, no spicel requirments")
_cityaddress = str(_cityaddress)

while True:
    _zipcode = input("enter your zipcode, only digits allowed and more then 4 digits")
    if _zipcode.isdigit() and len(_zipcode) > 4:





    print(f"{_last_name}, {_first_name}, {_country}, {_cityaddress}, {_zipcode}")








