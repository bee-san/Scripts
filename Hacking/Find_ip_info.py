import requests
print("Enter the IP address: ")
IP = input("> ")

print(requests.get('http://ipinfo.io/'))
