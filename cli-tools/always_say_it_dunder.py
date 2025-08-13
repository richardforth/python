#!/usr/bin/env python
'''
If the above gives errors, on ubuntu, install python-is-python3
Alternatively update the above to say python3 instead of python
'''

def say_it():
    greeting = 'Hello'
    target = 'Richard'
    message = f'{greeting} {target}'
    print(message)

# dunder
if __name__ == "__main__":
    say_it()
