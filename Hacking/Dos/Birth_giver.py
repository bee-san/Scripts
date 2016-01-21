from __future__ import print_function

import os
import time
import sys
import spawn

# -------------- #
HOST = "192.168.1.1"
PASSWORD = "admin"
TELNET = "23"
# -------------- #

"""
performs a dos attack on my own network
if router is deemed to be online (using ping)
spawn a python script to take it offline
wait 7 seconds for it to take effect
see if its still online
if it is, spawn another one.
This program also changes your MAC address before you DOS
so anonymous lmao
check spawn.py for how the DOS attack works

requirements

Install macchanger
Install airecrack-ng suite
Python2[x] or Python3[x]
"""


def main():
	while True:
		check()
		# this is a problem
		#os.system("python spawn.py")
		spawn.main()
		time.sleep(3)

def check():
	while True:
		response = os.system("ping -c 1 " + HOST)
		print(response)
		if response == 0:
			return None
		time.sleep(1)

def close():
	sys.exit()

if __name__ == "__main__":
	main()
