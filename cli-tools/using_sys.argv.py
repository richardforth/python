#!/usr/bin/env python3
"""
simple command-line tool usingf sys.argv
"""

import sys

if __name__ == "__main__":
	print(f"The first argument:  '{sys.argv[0]}'")
	print(f"The second argument: '{sys.argv[1]}'")
	print(f"The third argument:  '{sys.argv[2]}'")
	print(f"The fourth argument: '{sys.argv[3]}'")
