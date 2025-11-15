# listener_broadcast.py
import socket

def start_broadcast_listener(port=37020):
    # Create a UDP socket (UDP does not guarantee delivery, but is great for broadcasting)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Binding to all interfaces on this port
        try:
            s.bind(('', port)) 
            print(f"[*] UDP Listener started on port {port}. Waiting for broadcast messages...")
        except socket.error as e:
            print(f"[-] Failed to bind socket: {e}")
            return

        while True: # Listen constantly
            data, addr = s.recvfrom(1024) # Receive data and sender's address
            if data:
                message = data.decode('utf-8', errors='ignore')
                print(f"[*] Received message from {addr}: {message.strip()}")

if __name__ == '__main__':
    start_broadcast_listener()

