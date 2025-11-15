# listener_broadcast.py
import socket

def start_broadcast_listener(port=37020):
    # Создаем UDP-сокет (UDP не гарантирует доставку, но отлично подходит для вещания)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(('', port)) # Привязываемся ко всем адресам на этом порту
        print(f"[*] Слушатель UDP запущен на порту {port}. Ожидание сообщений в эфире...")
        
        while True: # Слушаем постоянно
            data, addr = s.recvfrom(1024) # Получаем данные и адрес отправителя
            if data:
                message = data.decode('utf-8')
                print(f"[*] Получено сообщение от {addr}: {message.strip()}")

if __name__ == '__main__':
    start_broadcast_listener()
