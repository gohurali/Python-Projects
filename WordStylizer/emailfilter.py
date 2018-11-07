import re

input_item = input('Enter an email address: ')

result = re.match("^[A-Za-z0-9\.]+@[a-zA-Z]+\.[a-z]*$", input_item)

if result is not None:
    print('successful!')
else:
    print('not a valid email')