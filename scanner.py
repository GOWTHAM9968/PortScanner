import socket

target = input("Enter IP Address or Hostname: ")

try:
    ip = socket.gethostbyname(target)

    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))

    print(f"\nScanning {ip}...\n")

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))

        if result == 0:
            print(f"Port {port} OPEN")

        s.close()

    print("\nScan Completed.")

except socket.gaierror:
    print("Invalid hostname or IP address.")

except ValueError:
    print("Please enter valid port numbers.")