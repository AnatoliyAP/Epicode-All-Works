import socket  # Importa il modulo per la comunicazione tramite socket
import platform  # Importa il modulo per ottenere informazioni sul sistema operativo
import os  # Importa il modulo per interagire con il sistema operativo
import subprocess  # Importa il modulo per eseguire comandi di shell

SRV_ADDR = "192.168.90.101"  # Indirizzo IP del server
SRV_PORT = 8888  # Porta del server

def print_menu():
    print("\n\n1) Ottieni informazioni di sistema\n2) Elenca il contenuto della directory\n3) Avvia la shell\ne) Chiudi la connessione")

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un oggetto socket
my_sock.connect((SRV_ADDR, SRV_PORT))  # Connette il socket al server
print("Connessione stabilita")
print_menu()

while True:
    message = input("\n-Seleziona un'opzione: ")  # Richiede all'utente di selezionare un'opzione
    if message == "e":
        my_sock.sendall(message.encode())  # Invia il messaggio al server
        my_sock.close()  # Chiude la connessione
        break
    elif message == "1":
        my_sock.sendall(message.encode())  # Invia il messaggio al server
        data = my_sock.recv(1024)  # Riceve i dati dal server
        if not data:  # Se non ci sono dati ricevuti
            break
        print(data.decode('utf-8'))  # Stampa i dati decodificati come stringa
    elif message == "2":
        path = input("Inserisci il percorso: ")  # Richiede all'utente di inserire un percorso
        my_sock.sendall(message.encode())  # Invia il messaggio al server
        my_sock.sendall(path.encode())  # Invia il percorso al server
        data = my_sock.recv(1024)  # Riceve i dati dal server
        data = data.decode('utf-8').split(",")  # Decodifica i dati come stringa e li divide in una lista
        print("*" * 40)
        for x in data:
            print(x)  # Stampa ogni elemento della lista
        print("*" * 40)
    elif message == "3":
        my_sock.sendall(message.encode())  # Invia il messaggio al server
        data = my_sock.recv(1024).decode('utf-8')  # Riceve i dati dal server e li decodifica come stringa
        print(data)  # Stampa i dati
        while True:
            command = input("Inserisci un comando: ")  # Richiede all'utente di inserire un comando
            my_sock.sendall(command.encode('utf-8'))  # Invia il comando al server
            if command.lower() == 'exit':  # Se il comando Ã¨ "exit"
                break  # Esce dal ciclo
            output = my_sock.recv(1024).decode('utf-8')  # Riceve l'output dal server e lo decodifica come stringa
            print(output)  # Stampa l'output
    else:
        print_menu()  # Stampa il menu