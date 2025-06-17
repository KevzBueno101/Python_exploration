import string
import itertools

password = input('Enter your password: ')
charset = string.ascii_lowercase + string.digits

for length in range(1, 10):
    for attempt in itertools.product(charset, repeat=length):
        guess = ''.join(attempt)
        print('Trying', guess)
        if guess == password:
            print('Password hacked: ', password)
            exit()
            