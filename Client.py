import socket

def start_client():
    server_address = ('localhost', 6523)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    
    try:
        for _ in range(20):
            question = client_socket.recv(1024).decode()
            print("Question:", question)
            answer = input("Your answer (t/f): ")
            client_socket.sendall(answer.encode())
        
        final_score = client_socket.recv(1024).decode()
        print('Score:', final_score)
    except ConnectionAbortedError:
        print("The connection was aborted by the server.")
    except ConnectionError:
        print("A connection error occurred.")
    finally:
        client_socket.close()

start_client()
