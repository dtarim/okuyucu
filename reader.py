import socket

def main():
    server_address = ('localhost', 12345)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)
    
    print("Starting reader...")

    while True:
        try:
            data, address = sock.recvfrom(4096)
            print(f"Received: {data.decode('utf-8')} from {address}")
        except KeyboardInterrupt:
            print("Reader stopped.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
