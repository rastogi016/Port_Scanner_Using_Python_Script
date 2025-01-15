import sys
import socket
from datetime import datetime
import threading

# Function to scan port
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except socket.error as e:
        print(f"Socket error on port {port}: {e}")
    except Exception as e:
        print(f"Unexpected error on port {port}: {e}")

# Main function - Argument validation and target definition
def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print("Invalid number of arguments")
        print("Usage: python Oports.py <target>")
        sys.exit(1)

    # Resolve the target hostname to IP
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Unable to resolve the hostname {target}")
        sys.exit(1)

    print("-" * 50)
    print(f"Scanning target: {target_ip}")
    print(f"Start time: {datetime.now()}")
    print("-" * 50)

    try:
        threads = []
        for port in range(1, 65536):
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nExiting Program")
        sys.exit(0)

    except socket.error as e:
        print(f"Socket error: {e}")
        sys.exit(1)

    print("\nScan Completed !!")

if __name__ == "__main__":
    main()
