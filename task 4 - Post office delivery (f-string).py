
import time

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
    _country = input("enter country must be only letters with first capital")
    if _country.isalpha() and len(_country) >= 3:
        break
_country = str(_country)

_cityaddress = input("enter your city address, no spicel requirments")
_cityaddress = str(_cityaddress)

while True:
    _zipcode = input("enter your zipcode only digits")
    if _zipcode.isdigit() and len(_zipcode) >= 4:
        break
_zipcode = int(_zipcode)

print(f"FOR: {_last_name}, {_first_name}")
print(f"COUNTRY: {_country}")
print(f"ADDRESS: {_cityaddress}")
print(f"ZIPCODE: {_zipcode}")







