import random

print('Welcome to Your Password Generator')

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+=<>?"

number = int(input('Amount of passwords to generate: '))
number = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nhere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)

    print(passwords)

