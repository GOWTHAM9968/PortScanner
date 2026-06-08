import socket
import time
from colorama import init, Fore, Style

init(autoreset=True)

target = input("Enter IP Address or Hostname: ").strip()

try:
    ip = socket.gethostbyname(target)

    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))

    start_time = time.time()

    results = []
    open_ports = 0

    print("\n" + "=" * 50)
    print(Fore.CYAN + "        PORT SCANNER v1.0")
    print(Fore.CYAN + "      Cybersecurity Project")
    print("=" * 50)

    print(Fore.YELLOW + f"Target : {target}")
    print(Fore.YELLOW + f"IP     : {ip}")
    print(Fore.YELLOW + f"Ports  : {start_port} - {end_port}")
    print("=" * 50)

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

            print(Fore.GREEN + message)

            results.append(message)

        s.close()

    with open("results.txt", "w") as file:
        for item in results:
            file.write(item + "\n")

    end_time = time.time()
    total_time = end_time - start_time

    print("\n" + "=" * 50)
    print(Fore.CYAN + "SCAN SUMMARY")
    print("=" * 50)

    print(Fore.YELLOW + f"Target           : {target}")
    print(Fore.YELLOW + f"IP Address       : {ip}")
    print(Fore.YELLOW + f"Port Range       : {start_port} - {end_port}")

    print(Fore.GREEN + f"Open Ports Found : {open_ports}")

    print(Fore.CYAN + f"Scan Time        : {total_time:.2f} seconds")

    print(Fore.GREEN + "Results saved to results.txt")

    print("=" * 50)

except socket.gaierror:
    print(Fore.RED + "Error: Invalid hostname or IP address.")

except ValueError:
    print(Fore.RED + "Error: Please enter valid port numbers.")

except KeyboardInterrupt:
    print(Fore.RED + "\nScan stopped by user.")