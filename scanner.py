#!/bin/python3

import sys
from datetime import datetime
import socket

# Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4
else:
	print("Invalid amount of arguments.")
	print("Syntax python3 scanner.py <ip>")

# Adding Pretty Banner

print("-" * 50)
print("Scanning Target "  + target)
print("Time Started: " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(50, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(2)
		result = s.connect_ex((target, port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()
		
except KeyboardInterrupt:
	print("\nExisting Program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved. ")
	sys.exit()
	
except socket.error:
	print("Could not connect to server. ")
	sys.exit()

