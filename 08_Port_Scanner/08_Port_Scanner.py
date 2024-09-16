import socket
import threading


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f'Port {port} is open')
        sock.close()
    except Exception as e:
        print(f'Error: {e}')


def scan_range_of_ports(target, start_port, end_port):
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()


target_ip = input("Enter the target IP address: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

scan_range_of_ports(target_ip, start_port, end_port)
