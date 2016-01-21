#!/usr/bin/env bash

while true
	do
	telnet 192.168.1.1
	expect "Password: "
	send "admin"
	sleep 5
	echo "sys reboot"
done

