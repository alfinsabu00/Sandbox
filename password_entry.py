"""Alfin"""

min_password = 5
password = input('Enter Password of 5 Characters Min:')
while len(password) < min_password:
    password = input('Enter password of 5 characters:')
print('*'*len(password))
