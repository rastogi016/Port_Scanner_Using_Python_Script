
Port Scanner Using Python

This is a simple port scanner developed using Python that scans a range of ports on a given target IP address or hostname. It uses the socket and sys libraries for network communication and handling the command-line interface.

Features:
  Scans ports in the range of 50-85 on the target.
  Displays the open ports on the target.
  Handles exceptions like invalid arguments, connection issues, or invalid hostnames.
  Includes a banner displaying the start time of the scan and target being scanned.
  
Requirements:
  Python 3.x
  
Usage:
  Clone the repository or download the script.
  Open a terminal in the project directory.
  Run the script with the following command:

python3 scanner.py <target_ip_or_hostname>


Code Explanation:
Input Handling: The script accepts a target IP address or hostname as a command-line argument. If the argument is missing or incorrect, it will display the correct syntax for usage.

Port Scanning: The script iterates through a range of ports (50 to 85), attempts to connect to each one, and checks if the connection is successful (indicating the port is open).

Exception Handling:

KeyboardInterrupt: Exits the program gracefully when the user interrupts the scan.
socket.gaierror: Handles errors when the hostname cannot be resolved to an IP address.
socket.error: Catches connection errors when unable to connect to the target.


