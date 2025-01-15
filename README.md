# **GitHub README for Port Scanner**
## **Port Scanner**
  A Python-based multithreaded port scanning tool that scans all TCP ports (1-65535) on a specified target host to identify open ports.

## **Features**
  - Scans all TCP ports (1 to 65535) on a target machine.
  - Utilizes multithreading for faster scanning.
  - Identifies open ports and displays results in real-time.
  - Handles socket errors and provides appropriate error messages.
  - Easy to use with a simple command-line interface.
## **Usage**
  1. Prerequisites
    - Python 3.x installed on your system.
  2. Run the Script
    - Open a terminal and navigate to the directory containing the script.

**Execute the script using:**
  python3 scanner.py <target>
Replace <target> with the IP address or hostname of the target machine.

**Example**
python3 scanner.py 192.168.1.1

**Output Example**
--------------------------------------------------
- Scanning target: 192.168.1.1
- Start time: 2025-01-16 14:30:00
--------------------------------------------------
Port 22 is open  
Port 80 is open  
Port 443 is open  
...  
Scan Completed !!  

## **Error Handling**
  1. Invalid Arguments: If incorrect arguments are provided:
     - Invalid number of arguments
     - Usage: python Oports.py <target>
    
  2. Host Resolution Error: If the hostname cannot be resolved:
     - Error: Unable to resolve the hostname <target>
  3. Socket Errors:
     
**The script will display detailed error messages for any socket-related issues.**

### *Important Notes*
  **Permissions:**
  - On some systems, scanning certain ports may require administrative privileges.
