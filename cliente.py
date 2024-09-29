#Se importan la interfaz para la comunicación a través de la red.
import socket

def start_client(): #maneja la comunicación con el servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345)) #Se conecta al servidor
    print("Conectado al servidor") #Imprime el mensaje de conexión

    while True: 
        message = client_socket.recv(1024).decode() #recv recibe el mensaje de parte del servidor
        print(message)
        if message == "¡Es número es Correcto!":
            break

        guess = input("El número que adivinó fue: ")
        client_socket.send(guess.encode()) #send envía la adivinanza al servidor

    client_socket.close() #cierra la conexión con el servidor

if __name__ == "__main__":
    start_client()
