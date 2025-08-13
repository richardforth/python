#!/usr/bin/env python

import subprocess

try:
    cp = subprocess.run(['ls', '/doesnotexist'],
                        capture_output=True,
                        universal_newlines=True,
                        check=True)
except subprocess.CalledProcessError as e:
    print("Something went wrong: ", e)
