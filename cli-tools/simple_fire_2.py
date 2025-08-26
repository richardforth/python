#!/usr/bin/env python3
'''
Simple fire example #0
NOTE: to use fire, you need to install it, eg:
sudo apt install python3-fire
'''
import fire

# For fire to work with nested command structures, we need
# to implement a class
class Ships():
    def sail(self):
        ship_name = 'Your ship'
        print(f"{ship_name} is setting sail")

    def list(self):
        ships = ['John B', 'Yankee Clipper', 'Pequod']
        print(f"Ships: {','.join(ships)}")


def sailors(greeting, name):
    message = f"{greeting} {name}"
    print(message)

class Cli():

    def __init__(self):
        self.sailors=sailors
        self.ships=Ships()
    
if __name__ == "__main__":
    fire.Fire(Cli)
