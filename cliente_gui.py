#Se importan las librerias para la ejecución del programa.
#tkinder se importa para la interfaz gráfica y messagebox para la caja de texto
import socket
import tkinter as tk
from tkinter import messagebox

class GuessingGameClient: #GuessingGameClient maneja la interfaz gráfica y la comunicación con el servidor
    def __init__(self, master): #_init_ inicia la interfaz gráfica y establece una conexión
        self.master = master
        self.master.title("Bienvenido(a) al juego de la adivinanza")
        
        self.label = tk.Label(master, text="Adivina el número entre 1 y 100")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="¡Vamos, Buena Suerte!", command=self.send_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))
        self.receive_message()

    def send_guess(self): #send_guess envía la adivinanza al servidor y este recibe la respuesta
        guess = self.entry.get()
        if guess.isdigit():
            self.client_socket.send(guess.encode())
            self.receive_message() #recibe la respuesta del servidor y actualiza la interfaz gráfica
        else:
            messagebox.showerror("Incorrecto", "Por favor, digite un número correcto.") #muentra el mensaje al cliente

    def receive_message(self):
        message = self.client_socket.recv(1024).decode()
        self.result_label.config(text=message)
        if message == "¡El número es correcto!":
            self.client_socket.close()

if __name__ == "__main__":
    root = tk.Tk()
    game_client = GuessingGameClient(root)
    root.mainloop()
