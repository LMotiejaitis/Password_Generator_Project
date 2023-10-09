import random
import string

print('===Password Generator===')

def length():
    while True:
        length = (input("Enter the length of the password: "))
        if length.isdigit():
            length = int(length)
            if 0 < length < 50:
                break
            else: 
                print('Please enter a valid desired length which is not longer than 50')
        else:
            print('Please enter a valid number')
    return length
  
def number():
    while True:
        number = input('Enter the desired amount of passwords: ')
        if number.isdigit():
            number = int(number)
            if 0 < number < 50:
                break
            else:
                print('Please enter a valid amount and not more than 50')
        else:
            print('Please enter a valid number')
    return number
  
num = number()
lnth = length()

def generate_passwords(num, lnth):
    passwords = []
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(num):
        password = ''.join(random.choice(characters) for i in range(lnth))
        passwords.append(password)
    return passwords

passwords = generate_passwords(num, lnth)

def printing_passwords(passwords):
    if len(passwords) == 1:
        print('Here is your password:')
    else:
        print('Here are your passwords:')
    for i, password in enumerate(passwords):
        print(f'{i+1}. {password}\n')

printing_passwords(passwords)
