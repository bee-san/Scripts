#!/usr/bin/env bash

echo "Forensic analysis tool"
echo "This is a report of $USER"
echo "-------------------------"
echo "screen resolution"
xdpyinfo | grep "dimensions:"
echo "-------------------------"
echo "network configuation"
ifconfig
echo "-------------------------"
echo "os version"
uname -a
echo "-------------------------"
echo "public IP"
curl ipinfo.io
echo "-------------------------"