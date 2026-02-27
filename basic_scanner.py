import socket
import sys

def portscanner(ip, portlists):
    try:
        for port in portlists:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)  # timeout in seconds

            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"Port {port}\tOpen")
            else:
                print(f"Port {port}\tClosed")

            sock.close()

    except socket.error as error:
        print(str(error))
        print("Connection Error")
        sys.exit()


# Function call
portscanner('localhost', [22, 80, 443, 445, 3389])
