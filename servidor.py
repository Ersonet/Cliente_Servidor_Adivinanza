#Se importan las librerias para la ejecución del programa.
import socket #Para las conexiones de red
import threading #Para manejar varios clientes a la vez
import random #Para generar un número al azar

def handle_client(client_socket): #Función handle_client para la comunicación con un cliente
    number_to_guess = random.randint(1, 100) #Para generar un número entre el 1 al 100
    print(f"El número a adivinar es el: {number_to_guess}") #Imprime el mensaje del servidor
    client_socket.send("Adivina el número entre 1 y 100: ".encode()) #Maneja la comunicación con un cliente

    while True:
        try:
            guess = client_socket.recv(1024).decode() #recv se usa para recibir adivinanzas del cliente
            if not guess:
                break

            guess = int(guess)
            if guess < number_to_guess:
                response = "Sigue intentando"
            elif guess > number_to_guess:
                response = "¡Vamos, tú puedes!"
            else:
                response = "¡El número es correcto!"
                client_socket.send(response.encode())
                break

            client_socket.send(response.encode()) #send se usa para enviar pistas
        except ValueError:
            client_socket.send("Por favor, ingresa un número válido.".encode())
        except Exception as e:
            print(f"Error: {e}")
            break

    client_socket.close()

def start_server(): #Inicia el servidor y el espera la conexión
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345)) #bind se usa para vincular el socket a una dirección y puerto
    server_socket.listen(5) #listen espera la conexión
    print("Servidor iniciado y esperando conexiones...") 

    while True:
        client_socket, addr = server_socket.accept() #Se usa  accept para aceptar las conexiones entrantes
        print(f"Conexión establecida con {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start() #crea un nuevo hilo

if __name__ == "__main__":
    start_server() #inicia el servidor