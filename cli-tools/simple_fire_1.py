#!/usr/bin/env python3
'''
Simple fire example #0
NOTE: to use fire, you need to install it, eg:
sudo apt install python3-fire
'''
import fire

def greet(greeting='Hiya', name='Richard'):
    print(f"{greeting} {name}")

def goodbye(greeting='Bye', name='Richard'):
    print(f"{greeting} {name}")

if __name__ == "__main__":
    # We can expose multiple functions by caling fire.Fire() with no arguments
    fire.Fire()
