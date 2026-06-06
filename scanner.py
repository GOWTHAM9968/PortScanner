import socket

target = input("Enter IP Address or Hostname: ").strip()

try:
    ip = socket.gethostbyname(target)

    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))

    print(f"\nScanning {target} ({ip})...")
    print("-" * 40)

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"

            print(f"Port {port} OPEN ({service})")

        s.close()

    print("-" * 40)
    print("Scan Completed.")

except socket.gaierror:
    print("Error: Invalid hostname or IP address.")

except ValueError:
    print("Error: Please enter valid port numbers.")

except KeyboardInterrupt:
    print("\nScan stopped by user.")