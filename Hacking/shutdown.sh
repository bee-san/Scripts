#!/usr/bin/env bash
echo "starting the dos"
python3 shut_down_router.py &
sleep 2
python3 shut_down_router.py &
sleep 4
python3 shut_down_router.py &
sleep 16
python3 shut_down_router.py &
sleep 17

echo"I have slept for"



