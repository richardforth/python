#!/usr/bin/env python3
'''
Command-line toll using argparse
'''
import argparse

def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail.")

def list_ships():
    ships = ["John B", "Yankee Clipper", "Pequod"]
    print(f"Ships: {','.join(ships)}")

def greet(greeting, name):
    message = f"{greeting} {name}"
    print(message)


if __name__ == "__main__":
    # Set Application Title
    parser = argparse.ArgumentParser(description='Maritime control')

    # add a --twice option to perform the same action twice
    # NOT IMPLEMENTED HERE THOUGH
    parser.add_argument('--twice', '-t',
                        help='Do it twice',
                        action='store_true')

    # set groundwork for sub commands
    subparsers = parser.add_subparsers(dest='func')

    # add first subcommand 'ships'
    ship_parser = subparsers.add_parser('ships',
                                        help='Ship related commands')

    # ships list, or ships sail 
    ship_parser.add_argument('command',
                             choices=['list', 'sail'])

    # add second subcommand 'sailors'
    sailor_parser = subparsers.add_parser('sailors',
                                        help='Talk to a sailor')

    # sailors Jim => Ahoy there Jim
    sailor_parser.add_argument('name',
                             help='Sailors name')

    # sailors Jim -- greeting Bonjour -> Bonjour Jim
    sailor_parser.add_argument('--greeting', '-g',
                             help='Greeting',
                             default='Ahoy there')

    # start here
    args = parser.parse_args()
    if args.func == 'sailors':
        greet(args.greeting, args.name)
    elif args.func == 'ships':
        if args.command == 'list':
            list_ships()
        else:
            sail()
    else:
        parser.print_usage()
        
