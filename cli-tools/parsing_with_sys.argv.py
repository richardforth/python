#!/usr/bin/env python
'''
For the above to work, on linux, you must install python-is-python3,
otherwise just change the above from python to python3 and the script wont complain.

sudo apt -y install python-is-python3

'''

''' 
A simple command-line tool useing sys.argv
'''

import sys


def say_it(greeting, target):
	message = f'{greeting} {target}'
	print(message)

if __name__ == "__main__":
	greeting = 'Hello'
	name = 'Richard'

	if '--help' in sys.argv:
		help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"
		print(help_message)
		sys.exit

	if '--name' in sys.argv:
		# Get position after name flag
		name_index = sys.argv.index('--name') + 1
		if name_index < len(sys.argv):
			name = sys.argv[name_index]

	if '--greeting' in sys.argv:
		# Get position after greeting flag
		greeting_index = sys.argv.index('--greeting') + 1
		if greeting_index < len(sys.argv):
			greeting = sys.argv[greeting_index]

say_it(greeting, name)

		
