import socket

SERVICES = {
    "SSH": 22,
    "HTTP": 80,
    "HTTPS": 443
}

HOST = "127.0.0.1"

print("Local Service Checker")
print("-" * 30)

for service, port in SERVICES.items():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((HOST, port))

        if result == 0:
            print(f"{service} (Port {port}): Running")
        else:
            print(f"{service} (Port {port}): Not Running")

        sock.close()

    except Exception as e:
        print(f"Error checking {service}: {e}")