import socket
import time

target = input("Enter IP Address or Hostname: ").strip()

try:
    ip = socket.gethostbyname(target)

    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))

    start_time = time.time()

    results = []
    open_ports = 0

    print("\n" + "=" * 40)
    print("         PORT SCANNER v1.0")
    print("=" * 40)
    print(f"Target : {target}")
    print(f"IP     : {ip}")
    print(f"Ports  : {start_port} - {end_port}")
    print("=" * 40)

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))

        if result == 0:
            open_ports += 1

            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"

            message = f"Port {port} OPEN ({service})"

            print(message)
            results.append(message)

        s.close()

    with open("results.txt", "w") as file:
        for item in results:
            file.write(item + "\n")

    end_time = time.time()
    total_time = end_time - start_time

    print("=" * 40)
    print(f"Total Open Ports : {open_ports}")
    print(f"Total Scan Time  : {total_time:.2f} seconds")
    print("Results saved to results.txt")
    print("=" * 40)

except socket.gaierror:
    print("Error: Invalid hostname or IP address.")

except ValueError:
    print("Error: Please enter valid port numbers.")

except KeyboardInterrupt:
    print("\nScan stopped by user.")