
# call function from outside
# int(  input('number?')  )

name = 'danny' # str = input('whats your name? ')

print(name, 'your name is in length', len(name))

#       variable name
print(f"{name} your name is in length len(name)")

#     text-name
print(f"name your name is in length len(name)")

print(name, 'your name is in length', len(name))
print(f"{name} your length name is in {len(name)}")

first_name = "Petros"
last_name = "Borchardt"
id = "63 251283 B 185"
phone = "0419-0288803"

print(first_name, last_name, "id number ", id, " phone ", phone)
# last_name  first_name   id                          phone
# Borchardt, Petros id[3 251283 B 185] phone-number(0419-0288803)

# outer execution
# print(int( input('number?') ))
print(str.upper( first_name ))

# inner execution
print(first_name.upper())

text: str = "Hello, World!!"
print(len("Hello, World!!"))
print(len(text))

text1: str = "   Hello, World!!   "
print(text.strip())

text2: str = "Hello, World!!"
print(text2.lower())

text3: str = "Hello, World!!"
print(text3.upper())

text4: str = "Hello, World!!"
print(text4.replace("World", "Python"))
print(text4.replace("l", "t"))
print(text4.replace("t", ""))

text5: str = "Hello, World!! good morning"
print(text5.split())
text5 = "Hello,*World!!*good*morning"
print(text5.split('*'))

print('"AasdasBcccC".swapcase()', "AasdasBcccC".swapcase())